from solution import task_order
from checker import case


def valid_for(prereqs):
    def check(actual, expected):
        if sorted(actual) != sorted(prereqs):
            return False
        pos = {t: i for i, t in enumerate(actual)}
        return all(pos[p] < pos[t] for t, ps in prereqs.items() for p in ps)
    return check


morning = {"wake": [], "dress": ["wake"], "eat": ["wake"], "leave": ["dress", "eat"]}
case("morning", task_order(morning), "any valid order", compare=valid_for(morning))
case("empty", task_order({}), [])
single = {"a": []}
case("single", task_order(single), ["a"])
chain = {"c": ["b"], "b": ["a"], "a": []}
case("chain", task_order(chain), ["a", "b", "c"])
diamond = {1: [], 2: [1], 3: [1], 4: [2, 3], 5: [4]}
case("diamond", task_order(diamond), "any valid order", compare=valid_for(diamond))
