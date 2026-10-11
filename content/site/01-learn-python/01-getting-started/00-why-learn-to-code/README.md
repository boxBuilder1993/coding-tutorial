# Why learn to code when AI can write it?

A fair question. An AI assistant will write a working Python program from a
sentence of English, faster than any human, and it never gets tired. So why
spend hours learning to do by hand what a tool does in seconds?

The short answer: the tool does not know when it is wrong, and neither will
you, unless you can read what it wrote. This page explains that properly,
because it is the reason this course exists in the form it does.

## What AI is genuinely good at

Start with the honest part. AI assistants are remarkable at:

- Writing routine code quickly, the kind you have written a hundred times.
- Knowing the names and arguments of functions across thousands of
  libraries, better than any one person can.
- Explaining code you did not write, in plain language.
- Being a patient tutor at two in the morning.

Anyone who tells you these tools are useless is wrong, and you should use
them. The question is how.

## How it fails

An assistant does not look things up or run your code. It produces text
that looks like code it has seen before. Most of the time that text is
right. When it is wrong, it is wrong in specific, recognisable ways:

- **It invents things.** A function that does not exist, an argument the
  library does not accept, a method with a plausible name that was never
  written. The code looks perfect and crashes on the first run, or worse,
  runs and does something else.
- **It solves the example, not the problem.** Ask for code that handles a
  list of prices, and you get code that works on the three prices you
  mentioned and breaks on an empty list, a negative number, or a list
  with one item. The exercises in this course test exactly those cases,
  which is why they feel picky.
- **It fixes what you pointed at.** Report a bug and it will change
  something so that bug goes away. Whether the change is correct, or
  quietly breaks a different case, it does not know.
- **It sounds the same either way.** This is the trait that matters most.
  Right or wrong, the answer arrives in the same confident, well-formatted
  prose. Nothing in the output tells you which one you got. The only way
  to know is to read the code and understand it yourself.

## What that means for you

The work did not disappear when the typing got automated. It moved. Someone
still has to:

1. Say precisely what is wanted, which is harder than it sounds and is
   most of what programming ever was.
2. Read what came back and decide whether it does that.
3. Test it, including the cases the assistant did not think of.
4. Find and fix what is wrong, which means understanding why it is wrong.

Every one of those requires reading code at least as well as the machine
writes it. You cannot review what you cannot read. A person who can only
prompt is not using a power tool; they are being used by one, and they
will not find out until something breaks.

## What blind use costs

None of this is hypothetical. Code that nobody on the team understands
gets shipped, and the first person to find the bug is a customer. A
snippet pasted from an assistant quietly leaks data because the person
pasting it could not see the problem. A script runs for months producing
numbers that are subtly wrong. And on a personal level: you spend an
afternoon arguing with a tool that keeps confidently handing you the same
broken answer, with no way to tell it what is actually wrong, because you
cannot see it either.

The people who get the most out of these tools are the ones who could have
written the code themselves, more slowly. They can skim what comes back,
spot the invented function, notice the missing edge case, and say "no, do
it this way". That is the skill. It is the same skill it always was.

## Why Python

If you are going to learn one language for this, Python is the right one,
for three reasons:

- **It is the language of machine learning and data work.** The systems
  behind the assistants themselves are built and trained with Python.
  Anyone who wants to work near that field, or simply to analyse data,
  will be reading and writing it.
- **It is the language AI tools are most fluent in.** More Python exists
  on the internet than almost anything else, so assistants produce it most
  readily. That cuts both ways: it is the easiest language to get code in,
  and the easiest to get plausible wrong code in.
- **It is readable.** Python looks close to English, so it is the fastest
  route to the skill that matters, which is reading code and knowing what
  it does.

## How this course is built around that

You will notice there is no assistant inside the editor here. That is
deliberate. The exercises check real edge cases, the ones an assistant
skips, so you learn to think of them. Every exercise has a **Copy tutor
prompt** button that turns your assistant into a questioner that refuses to
hand over code, so you can use it without it doing the learning for you.

And the finish line, the 120 problems in Practice, is defined as solving
them without help. Not because help is bad, but because that is the exact
moment you become someone who can use the help safely.

Next: [Values and print](../01-values-and-print).
