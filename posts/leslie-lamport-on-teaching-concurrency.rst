.. title: Leslie Lamport on Teaching Concurrency
.. slug: leslie-lamport-on-teaching-concurrency
.. date: 2016-12-20 19:17:54 UTC-08:00
.. tags: 
.. type: text
.. has_math: yes

This post is a short discussion on the `Leslie Lamport`_ 's paper "`Teaching Concurrency`_".

Lamport's basic premise is that understanding the system the most important part, and engineers often muddy their
understanding with implementation details as soon as they start talking about programming languages suitable for
concurrency.

He even challenges engineers to come up with the solution for concurrency problems without using "semaphores_",
"monitors_", or any other construct that were invented and provided as a tool. Using those, he says, is like using the
'sort' to routine the language to implement a sorting algorithm.


    The modern field of concurrency started with Dijkstra’s 1965 paper on the mutual exclusion problem. For most of the
    1970s, one “solved” the mutual exclusion problem by using semaphores or monitors or conditional critical regions or
    some other language construct. This is like solving the sorting problem by using a programming language with a sort
    command. Most of your colleagues can explain how to implement mutual exclusion using a semaphore. How many of them
    can answer the following question: Can one implement mutual exclusion without using lower-level constructs that,
    like semaphores, assume mutually exclusive access to a resource?


Lamport's approach to problem solving suggests, we need to think of computing problem as series of states instead of
series of steps. I think, series of steps tend to give some linearity the approach, while series of states tend to
indicate that sub-parts of the system can have multiple states and the next state each sub-part can take only depends
upon the current state and action that leads the state transition to the next state.


    It is more useful to think about states than sequences of steps because what a computing device does next depends on
    its current state, not on what steps it took in the past.

    To describe a computation we need to describe a sequence of states. More often, we need to describe the set of
    computations that can be produced by some particular computing device, such as an algorithm. There is one method that
    works in practice: describing a set of computations by

    (1) the set of all initial initial states and
    (2) A next-state relation that describes, for every state, the possible next states that is, the set of states
        reachable from that state by a single step.

On computational thinking.

    How should we describe computations?

    Most computer scientists would probably interpret this question to mean, what language should we use? Imagine an
    art historian answering “how would you describe impressionist painting?” by saying “in French”.

    Programming and hardware-design languages don’t help an engineer understand what problem a system should solve.
    Thinking of computations as sequences of states, rather than as something described by a language, is the first
    step towards such understanding.

Lamport also describes in great details about importance of problem specification. Sometimes, when the problem is
specified clearly and understood problem, the solution becomes easy.  Most of our struggles seems to be with coming to
grasp the problem specification.

    The great contribution of Dijkstra’s paper on mutual exclusion was not his solution; it was stating the problem.
    (It is remarkable that, in this first paper on the subject, Dijkstra stated all the requirements that distinguish
    mutual exclusion from fundamentally simpler and less interesting problems.)

*On concurrency, itself*

He gives an example of concurrency problem  that according to him is "trivial". It took me some reading to understand
the problem. `StackOverflow.com`_ certainly helped.


    Once an engineer understands what a computation is and how it is described, she can understand the most important
    concept in concurrency: invariance. A computing device does the correct thing only because it maintains a correct
    state. Correctness of the state is expressed by an invariant—a predicate that is true in every state of every
    computation.

    Invariance is the key to understanding concurrent systems, but few engineers or computer scientists have learned to
    think in terms of invariants. Here is a simple example.

**Now, the problem**

Consider N processes numbered from 0 through N − 1 in which each process i executes

.. math::

    x[i] :=1;


    y[i] := x[(i−1)modN]

and stops, where each :math:`x[i]` initially equals 0. (The reads and writes of each :math:`x[i]` are assumed to be
atomic.)

This algorithm satisfies the following property: after every process has stopped, :math:`y[i]` equals 1 for at least
one process :math:`i` .

It is easy to see that the algorithm satisfies this property; the last process :math:`i` to write :math:`y[i]` must set
it to 1. But that process doesnt set :math:`y[i]` to 1 because it was the last process to write y.

What a process does depends only on the current state, not on what processes wrote before it. The algorithm satisfies
this property because it maintains an inductive invariant.

**Explanation**

The explanation on how :math:`y[i]` equals for 1 at least one process :math:`i` goes like this.

1. The :math:`x_s` model the following behavior: :math:`x[i]` is 1 if and only if the process :math:`i` has already run.
2. After all processes have completed, all :math:`x_s` are thus set to 1.
3. The :math:`y_s` are a bit trickier: :math:`y[i]` is set if :math:`x[i-1]` was set, that is, :math:`y[i]` is 1 if and
   only if the predecessor of :math:`i` had already run when :math:`i` was doing its write to :math:`y`.

I essentially to had resort to `StackOverflow.com`_ post author's explanation to completely understand this.

The program invariant is:

    If a process has set :math:`y[i]`, it must already have set :math:`x[i]` to 1.
    This is true regardless whether :math:`y[i]` is set to 0 or 1.

    Proving this invariant is quite easy: In the beginning, none of the :math:`y_s` is set, so it holds trivially.
    During program execution, each write to :math:`y[i]` is `sequenced after`_ a write to :math:`x[i]`. Therefore
    the invariant also holds for every step of the program afterwards.

The further reasoning goes like this.

    The last process to finish sets :math:`y[i]` to 1 because, by definition of being the last process, its
    predecessor must have already finished execution at that point (ie. its y value is already set).

    Which means, because of the invariant, its :math:`x` value (which determines the last process' :math:`y` value)
    has to be 1.

The alternate way to look at this problem can give some intuitive understanding too.

    You cannot find an execution order in which all :math:`y_s` are set to 0. Doing so would require all processes to
    execute before their predecessor. However, since our processes are arranged in a ring (that is, if I follow the
    predecessor chain I will eventually end up at my starting point again), this leads to the contradiction that at
    least one process must have finished executing before it wrote to :math:`y`.


To understand this concurrency problem, it requires some notion of syntax, a prior understanding of proving hypothesis,
and possibly discussing the problem and solution.

Trying to understand itself, I guess, is a progress.

.. _Teaching Concurrency: http://research.microsoft.com/en-us/um/people/lamport/pubs/teaching-concurrency.pdf
.. _Leslie Lamport: https://en.wikipedia.org/wiki/Leslie_Lamport
.. _semaphores: https://en.wikipedia.org/wiki/Semaphore_(programming)
.. _monitors: https://en.wikipedia.org/wiki/Monitor_(synchronization)
.. _StackOverflow.com: http://stackoverflow.com/questions/24989756/what-is-the-inductive-invariant-of-the-simple-concurrent-program
.. _sequenced after: https://en.wikipedia.org/wiki/Sequence_point
