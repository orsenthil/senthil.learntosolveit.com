.. title: Dominant Resource Fairness
.. slug: dominant-resource-fairness
.. date: 2017-01-04 19:27:53 UTC-08:00
.. tags: computer science, papers, research
.. category:
.. link:
.. description:
.. type: text

I was reading the paper on `Dominant Resource Fairness`_ and found it approachable, interesting and fairly easy to
understand.

`Dominant Resource Fairness`_ is a resource allocation strategy used by a system like `Mesos`_.

In general terms, resources are basically things that a group will need and the idea is the allocate the resources
amongst the members of the group in an efficient way. Examples could be the amount of money (resource) to be
distributed across a group of people in the community or the processor cores in a multi-core processor that needs to be
distributed and allocated to the process running on that processor.

The Dominant Resource Fairness uses `Linear Programming`_ technique to solve the problem of resource sharing.

In a datacenter with multiple computers, having multiple CPUs, multiple memories, network cards and many other resources,
those needs to be shared across the processes that are running in the datacenter. DRF uses the concept of a dominant
resource. The Dominant share is the maximum share that an entity (process) has been allocated for any resource. For
e.g, if if a process A has heavy CPU usage and process B has heavy memory usage, the dominant resource for process A is
CPU and the dominant resource for process B is Memory.

Dominant Resource Fairness seeks to maximize the minimum dominant share across all entities. That's the formulation
for the linear programming problem for you. Doing it across in a distributed way for different tasks with different
requirements is the challenge that is being solved.

For example, if user A runs CPU-heavy tasks and user B runs memory-heavy tasks, the DRF attempts to equalize CPU share
of user A with the memory share of user B. In this case, the DRF would allocate more CPU and less memory to the tasks
run by user A, and allocate less CPU and more memory to the tasks run by user B. In the single resource case -- where
all jobs are requesting the same resources -- the DRF reduces to max-min fairness for that resource.

Some interesting anecdotes I found in the paper include, enforcing "fairness" in resource sharing is a difficult
problem by itself.

    A big search company provided dedicated machines for jobs only if the users could guarantee high utilization. The
    company soon found that users would sprinkle their code with infinite loops to artificially inflate utilization
    levels.

The paper also quoted economic research on difficultly in ensuring fairness.

    Competitive equilibrium from equal incomes (CEEI), a popular fair allocation policy preferred in the micro-economic
    domain is not strategy proof.


.. _Dominant Resource Fairness: https://people.eecs.berkeley.edu/~alig/papers/drf.pdf
.. _Mesos: http://mesos.apache.org/
.. _Linear Programming: https://en.wikipedia.org/wiki/Linear_programming
