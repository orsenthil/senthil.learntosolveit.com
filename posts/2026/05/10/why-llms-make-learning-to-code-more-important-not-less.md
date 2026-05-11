<!--
.. title: Why LLMs Make Learning to Code More Important, Not Less
.. slug: why-llms-make-learning-to-code-more-important-not-less
.. date: 2026-05-10 19:40:57 UTC+00:00
.. tags: 
.. category:
.. link:
.. description:
.. type: text
-->

_This is the transcript of my talk at OMSCS Conference 2026_

Hello, everyone. I'm Senthil Kumaran, a software developer at Uber. I've been programming for more than 20 years. I completed my OMSCS specialization in 2019 with specializations related to Computer Vision and Computational Systems. I had taken twelve courses in all, and I've stayed close to the program ever since.

This is my first presentation at an academic conference, and I'm grateful to be here.

I chose this topic last year, when we were being bombarded daily with new developments in large language models. The chorus was loud and clear: programming is dead. The industry, or at least parts of it, wants you to believe that. 

But if you are a programmer, and especially if you work alongside really good programmers in serious open-source projects or in industry, you know how far that claim is from the truth. 

Things have changed. Things have improved. But it is nowhere near what people who don't program think it is.

So, that's the topic of my talk: why large language models make learning to code more important, and not less.

**A note on my favorite teacher**

<img src="https://github.com/user-attachments/assets/3a70ef30-438d-418c-9529-fa77f5962162" />

Before I get into the substance, I want to say something about the teacher who inspired me to take OMSCS in the first place. I had taken several of his lectures online, and there is a particular quality to his teaching that resonated with me deeply. 

He has a real intuition for his subjects, he tries to share that intuition with students, he makes complex ideas approachable, and he understands and communicates the value of hard work.

When you have a favorite teacher and you really pay attention, you recognize that the way they explain hard things just clicks. And the whole point of any of this, the whole point of education, is understanding and intuition.

Programming has never been about coding. Programming is about understanding and intuition, and these are the qualities we should be drawing out in any domain we work in.

**Feynman's blackboard**

<img alt="Image" src="https://github.com/user-attachments/assets/f1fac986-7bc7-4495-8bc3-4c7cc14eb774" />


This is a famous photograph of Feynman's blackboard at the time of his death.  It's covered in string theory equations, but in the corner is a line that has stayed with me:

_What I cannot create, I do not understand._

This is profound. If you want to understand something, you have to create it. 

If I want to learn a complex topic, I solve problems in it, I build a model of it, I make a project out of it. Those are the topics I have understood best. Even writing a paper is creating. The act of creating is the act of understanding.

The other line on that blackboard says: Know how to solve every problem that has been solved. We build on the basics. We solve the problems that have already been solved, and we build up from there so that we are ready when new problems
arrive.

And the rest is string theory equations — which, as it happens, you can now point an LLM at and have it walk you through, line by line. [That itself is part of my point](https://claude.ai/share/8002eaf4-3210-49cf-9930-b1039bc90484).

**The world feels like it's on steroids**

<img alt="Image" src="https://github.com/user-attachments/assets/c6415fa6-b2c1-465f-adfd-82171d99c692" />

Deep neural networks and the applications built on top of them, large language models, have turned our world upside down. Every day there is more news about automating human work, especially programmers. Major labs are talking in numbers that are hard to comprehend.

I want to step back on the money for a moment, because the world tends to translate everything into dollars and miss what's actually happening. 

When you read that "Amazon invested a billion dollars in Anthropic," if you read a little deeper, a lot of that is compute. If you run a major lab, you need an enormous amount of compute to train your models. If you are an infrastructure provider, you have compute that's available for rent. Investing compute instead of cash is a win-win, but the public framing collapses it all into a single dollar figure. Even programming-specific tools have absorbed this energy.  Cursor, for example, has raised at valuations that climbed from 10 billion to 60 billion with SpaceX deals. 

So when some people are saying programming is no longer required, while the industry is pouring this kind of money into LLM-based programming tools, you have to ask: is the claim that, coding is dead, a valid statement?

Given the hype and drumbeat, honestly, when I submitted this proposal a year ago, I was worried that what the industry claims would become true. 

Today I am more convinced than before:

LLMs have not made learning programming obsolete. They have made it more important, and in fact, they have expanded the programmer's toolset.


**A wonderful time to learn programming**

This is a wonderful and exciting time to learn programming and grow as a software developer. Things that used to be inaccessible are suddenly within reach.

You can study Knuth efficiently now. His work is hard science, and historically required a particular kind of mindset and patience. If you worked as a software developer shipping features for customers, even a strong interest in Knuth would leave the book sitting on your shelf. You'd attempt one or two problems and stop. I have done this.

Now I can solve ten problems where each one used to take five days and now takes one. And I do it by asking the right questions and asking the LLM to handle the mechanical grunt work, then sitting with the result until I actually understand it.

You can do this with any of the great technical books. Algorithms by Sedgewick represents 40 years of effort by its authors. We're not going to absorb 40 years of work in coursework. But we can now absorb it in something on the order of
years, understanding their work deeply, and that's an enormous shift.

<img src="https://github.com/user-attachments/assets/3ba23e84-4333-4dd8-a78b-55e253e5c95f" />

ref: [https://joshmpollock.com/dijkstras-algorithm-article/](https://joshmpollock.com/dijkstras-algorithm-article/)


And people are doing this. Someone built an interactive visual exploration of the Dijkstra shortest-path algorithm following the Sedgewick book. They understood the model, asked an LLM to help them build the simulation, and ended up with exactly what I'm describing: a one-to-one correspondence between what you read, what you build, and what you understand.

**Tools to learn programming**

The same shift makes it dramatically easier to build great software, the kind of software that ends up in app stores and on people's phones. The barrier is lower. But to build software, you still have to learn programming. That has not
changed.

There is a perception that you can just prompt an LLM and ship an app. Yes, you can produce something. But what you have is an artifact, not software. The moment you need to tweak it, if you don't understand programming, you are stuck.  This is why most non-programmers who try this route stall at the first version.  They didn't build it. They wished for it. Building requires understanding the basics, and that means learning to program.

**So how do you actually learn programming today?**

My favorite tool is Exercism, a site that teaches you by solving problems in dozens of languages. Before LLMs, learning a language on Exercism was slow. You'd get stuck, post in the forum, wait two days for a response, finally have it click, and continue. Mastering one or two languages might have taken years.

Exercism is great in that you can have a mentor work with you too. But still as humans, you try to be kind to the mentor, try not to ask "dumb questions" or "lazy" questions.

_We don't have to fear that with machines._

Now you can ask your own personal tutor, an AI of your choice, to help you learn — not solve for you, but teach you. The trick is configuring the AI properly. 

In my claude.md or agent.md file, I give the AI a specific role:

```
You are my PhD-level programming languages and computer science teacher. Your
job is not to give me solutions. It is to guide me to write them myself.

Then I give it specific rules:

Never give me a solution. Help me discover it step by step.

Name the concept. When I bring a problem, name the computer science idea and the
language construct at the heart of it. Explain its syntax, semantics, edge
cases, gotchas, and how it compares to similar constructs in other languages I
know.

Tie it to the machine. Connect language constructs to the underlying memory
model: recursion to call stacks, statics to the data segment, pointers to
address spaces, closures to heap-allocated environments. 

Keep this directly tied to what we're working on, not a generic lecture.

Break it down. Give me an ordered list of small sub-tasks to attempt one at a
time. Don't dump all of it at once. Present one step, then wait.

Use tiny, self-contained examples when introducing new syntax in the language.

When I share my code, point out bugs precisely — line number, what's wrong, why.
Ask a leading question to help me fix it. Don't hand me the fix.

If logic is right but style is off, mention it briefly and move on.
Be brutally honest. Attack my assumptions and point out my weak spots.
```

<img src="https://github.com/user-attachments/assets/3f9175a8-0f08-40dc-8dcf-286643fe75ab" />



With instructions like these, the LLM stops being an answer machine and starts behaving like a teacher. The first thing it now says to me is, "Let's start by making sure you understand the problem before writing any code." This single shift has taught me lessons I would never have arrived at on my own, about heap-allocated storage, about caller expectations of ownership, about the assumptions a test makes about the code it exercises. 

<img src="https://github.com/user-attachments/assets/dd12aea9-696e-4411-a86a-87d261ccf489" />


It pulls me into corners of the language I would never have looked into.


<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/lgpPDJ2GeUU?si=pNmFEYz0oWlH5NAr&amp;start=4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


[https://www.youtube.com/watch?v=lgpPDJ2GeUU](https://www.youtube.com/watch?v=lgpPDJ2GeUU)

**Practice, accelerated**

Solving problems is essential, but so is everyday practice. I built a small system of programming-language templates filled with comments that ask you to mechanically fill in the next concept. Open one of these in an AI-aware editor and the autocomplete fills in the snippets, you read, you tab, you read, you tab.

This is not "the AI does it for me." It's the opposite. By skipping the mechanical typing, you cross directly into the part that actually matters: the flow and structure of the program. 

The latency between curiosity and understanding collapses. You stay in the editor. You don't context-switch into a chat window. The AI sees what you're doing and responds to it.

<img src="https://github.com/user-attachments/assets/2925271a-0e62-4da9-953a-6d6c21e14677" />

This is an effective way to learn programming: understanding the toolset, fundamentals, design, and structure of various programming languages.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Hl93y8BarYE?si=wJhTlqNb2HlehKve&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


[https://www.youtube.com/watch?v=Hl93y8BarYE](https://www.youtube.com/watch?v=Hl93y8BarYE)


Let's shift a bit into Software Engineering that is more than programming.  

**Designing, writing and communicating.**

The article [Don't Let AI Write For You](https://alexhwoods.com/dont-let-ai-write-for-you/) by Alex H Woods brings some of these points in greater detail. In essence, these are


**Writing is thinking**

Writing is an essential part of programming, and it deserves its own treatment.

In short, writing is thinking. We gain the understanding of the system by writing.

> The goal of writing is not to have written. It is to increase your
> understanding, and the understanding of those around you.

Often with writing we start with an ambiguous state of the world, sort it out,
and come out with a structure that is clean and coherent. That is the point of
writing. LLMs help, but the understanding of the concept is the human part. 

We never want to skip the understanding part with the writing.

**Writing is exercising**. 

I like running. Solving a problem is like exercising.  Doing something hard,
pushing the boundary, just makes us better.

You are often doing it for that innate feeling that is within you, that you want
to improve, you want to cross that boundary. You want to feel good.

> Asking an LLM to do your writing for you is like paying somebody to do your workout. It is not your workout. 

In fact, people get this. Even middle-school students get this, and serious people do not respect when they see that the real work is outsourced to a machine.

Communicating is also how we build trust. 

If I communicate an output of a LLM without a serious understanding, we are building things like the house of cards.

You don't know when it will collapse.

If I send a document that is LLM output, I am often not near the source of truth.
This is merely an output that LLM thinks that I and my colleagues want to hear.
It misses the point, sometimes, seriously.

And when we realize it, it is usually embarrassing.

> Each LLM-generated document is a missed opportunity to think and to build trust.

This matters especially in programs like OMSCS, where students are expected to write their own code and their own analyses. If you understand the work and the LLM just helps you finish faster, great. If you don't, you're trading the actual education for something that is not so valuable.

**Effective writing with LLMs**

That said, LLMs are extraordinary research partners. 

In my own writing, design docs, on-call alert analyses, even Slack questions. I
instruct the LLM through claude.md to bring specific depth to specific topics:

- Database and storage engines — discuss transaction model, isolation level,
  replication protocol, read/write path. Reference Spanner, Bigtable, DynamoDB,
  Kafka, Zookeeper.

- Consensus protocols — reference the Paxos, Raft, Viewstamped Replication, and
  pBFT papers, and cite the specific section and theorem.

- Distributed algorithms — vector clocks, CRDTs, consistent hashing, two-phase
  commit.

- Schedulers and resource managers — reference Borg, Omega, Mesos.

- Networking — BBR, congestion control, RDMA.

I work on compute infrastructure at Uber, large-scale autoscaling, that works
extensively with distributed systems, with millions of CPU allocations and GPU
allocations for batch, training and inference jobs.

<img src="https://github.com/user-attachments/assets/a60e118a-4e7c-482a-a03b-8aa4d718f019" />

So when an alert fires and I need to understand a system, the LLM hands me back
not just the answer but the canonical paper, the relevant section, the theorem.
Every alert becomes *my* reinforcement-learning loop into a fundamental concept.


**I love it!**

An expert programmer would have built this intuition over decades. With a
PhD-level tutor on call for daily affairs, you can build it now.

**When AI goes wrong**

There's a wonderful article called "The machine didn't take your craft, you gave it up." by  [David Abram](https://www.davidabram.dev/musings/the-machine-didnt-take-your-craft/). It captures the failure modes of using AI precisely.

The hardest part of the job was never typing the code. Coding helps us to think deeply and accurately. The code and tests are often the best source of truth, but that is only one part of the stack.

The hard part, is how we build it, how we understand the system as a whole, how we reason with it, and how it works under pressure. How to debug when there is customer at the other end.

How to use the proper tools, how to be yourself, when you are challenged by the system, and you strive to work around it.

These are accomplished only by having a "sound mental model", and intuition for the system, and knowing the details carefully and through hard work.

The hard part has always been understanding, especially with multi-dimensional contexts in our mind.

If we abandon the contexts that we know and accept what the model suggests, we are often giving up on solving the correct problem.

LLMs can help, they can help a lot. But as engineers, we take the decision. It is our work.

**Not getting trapped by the news of the day**

A line from the creator of Redis I keep coming back to: don't let the daily noise — RAG, MCP, whatever the acronym is this week — consume all your energy.

Some of it is useful. A lot of it is hype from people who can't compete with the AI itself, so they pump the products around it. 

> The actual product, for the most part, is the neural network.

I'll close with two small notes. 

First, an example of AI slop in the wild: I asked NotebookLM to generate a quiz from Attention Is All You Need, and it produced the question, "How did the authors decide to handle the order of the names in the publication?" Who cares? 

Second, a few weeks ago, there was an accidental release of source code, which I wanted to study! It was taken down. Just like we have outages with Software Engineering. We're all figuring this out together.

Finally, I'll leave you with a line from Emerson:

> To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.

We have always tried this. I think, it will continue to hold true.

<img src="https://github.com/user-attachments/assets/90e2d825-a684-4a80-b7c2-0ff75445d33e" />

Thank you.

