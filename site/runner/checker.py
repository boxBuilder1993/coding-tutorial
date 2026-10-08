"""Checker API available to every check.py, in the browser and in the build.

A check.py imports what it needs from `solution` (the learner's code) and
calls `case(...)` for each assertion. `_run` executes a check.py source and
returns a JSON report; it is called by the Pyodide worker and by the build.
"""
from __future__ import annotations

import importlib
import json
import math
import sys
import traceback
from collections import deque
from typing import Any, Callable, Iterable, Optional

__all__ = [
    "case",
    "ListNode", "TreeNode",
    "from_list", "to_list", "from_level_order", "to_level_order",
]

_results: list[dict[str, Any]] = []


# --------------------------------------------------------------------------- cases

def _repr(value: Any) -> str:
    try:
        text = repr(value)
    except Exception:  # noqa: BLE001
        return "<unrepresentable>"
    return text if len(text) <= 2000 else text[:2000] + "…"


def _compare(actual: Any, expected: Any, mode: Any) -> bool:
    if callable(mode):
        return bool(mode(actual, expected))
    if mode == "exact":
        return actual == expected
    if mode == "sorted":
        return sorted(actual) == sorted(expected)
    if mode == "set":
        return set(actual) == set(expected)
    if mode == "approx":
        return math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-12)
    raise ValueError(f"unknown compare mode {mode!r}")


def case(name: str, actual: Any, expected: Any, compare: Any = "exact") -> bool:
    """Record one check. Returns whether it passed."""
    try:
        ok = _compare(actual, expected, compare)
    except Exception as exc:  # noqa: BLE001  (e.g. sorted() on None)
        _results.append({
            "name": str(name), "status": "fail",
            "expected": _repr(expected), "actual": _repr(actual),
            "message": f"could not compare: {type(exc).__name__}: {exc}",
        })
        return False
    _results.append({
        "name": str(name), "status": "pass" if ok else "fail",
        "expected": _repr(expected), "actual": _repr(actual),
    })
    return ok


# ---------------------------------------------------------------------- structures

class ListNode:
    def __init__(self, val: Any = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        try:
            return f"ListNode({to_list(self)})"
        except ValueError:
            return "ListNode(<cycle>)"


def from_list(values: Iterable[Any]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list:
    out: list = []
    seen: set[int] = set()
    while head is not None:
        if id(head) in seen:
            raise ValueError("cycle detected while converting linked list")
        seen.add(id(head))
        out.append(head.val)
        head = head.next
    return out


class TreeNode:
    def __init__(self, val: Any = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({to_level_order(self)})"


def from_level_order(values: list) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def to_level_order(root: Optional[TreeNode]) -> list:
    if root is None:
        return []
    out: list = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


# ------------------------------------------------------------------------- runner

def _forget_solution() -> None:
    for name in [k for k in sys.modules if k == "solution" or k.startswith("solution.")]:
        del sys.modules[name]
    importlib.invalidate_caches()


def _format_tb(exc: BaseException) -> str:
    # Drop the frame belonging to _run itself so the learner sees only their code.
    tb = exc.__traceback__
    if tb is not None and tb.tb_frame.f_code.co_filename == __file__:
        tb = tb.tb_next
    return "".join(traceback.format_exception(type(exc), exc, tb))


def _run(check_source: str) -> str:
    """Execute a check.py against the current `solution` module. Returns JSON."""
    global _results
    _results = []
    _forget_solution()
    sys.dont_write_bytecode = True

    status = "pass"
    error: Optional[str] = None
    missing: Optional[str] = None
    try:
        namespace = {"__name__": "__check__", "__file__": "check.py"}
        exec(compile(check_source, "check.py", "exec"), namespace)
    except NotImplementedError:
        status = "not-attempted"
    except ImportError as exc:
        error = _format_tb(exc)
        if getattr(exc, "name", None) == "solution" or "solution" in str(exc):
            status = "missing"
            # "cannot import name 'two_sum' from 'solution'"
            text = str(exc)
            if "cannot import name" in text:
                missing = text.split("'")[1] if "'" in text else None
        else:
            status = "error"
    except BaseException as exc:  # noqa: BLE001  (SyntaxError in solution, RecursionError, ...)
        status = "error"
        error = _format_tb(exc)
        # Only add a row when the failure is in the checker's own line, not
        # inside the learner's code; the summary already explains the latter.
        frames = traceback.extract_tb(exc.__traceback__)
        in_solution = any(f.filename.endswith("solution.py") for f in frames) or (
            isinstance(exc, SyntaxError) and (exc.filename or "").endswith("solution.py")
        )
        if not in_solution:
            line = next((f.lineno for f in reversed(frames) if f.filename == "check.py"), None)
            last = traceback.format_exception_only(type(exc), exc)[-1].strip()
            _results.append({
                "name": f"check.py line {line}" if line else "check.py",
                "status": "error",
                "message": last,
            })

    if status == "pass":
        if not _results:
            status = "error"
            error = "check.py recorded no cases"
        elif any(r["status"] != "pass" for r in _results):
            status = "fail"

    return json.dumps({"status": status, "cases": _results, "error": error, "missingName": missing})
