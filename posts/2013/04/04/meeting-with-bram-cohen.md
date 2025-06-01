.. title: Meeting with Bram Cohen
.. slug: meeting-with-bram-cohen
.. date: 2013-04-04 08:14:26
.. tags: software,technology
.. description: 
.. categories: 
.. wp-status: publish

During PyCon Sprints, I met {{% wikipedia article="Bram_Cohen" %}} who had come
down to talk to Guido and have a word on networking protocol world. It was
interesting to see two experts talking. Later I invited Bram to give a tech talk
at Twitter. Bram gladly accepted it and came to Twitter office to talk to us
about his latest invention http://live.bittorrent.com He had been working on
Distributed Live Streaming for few years and thought it was a hard problem to
solve. He could dedicate himself to it and came out with live.bittorrent.com -
Using this anyone can live stream a video. You can become a live video publisher
too and people all around the word can see your channel in real time. This is a
huge break through. My experience at Akamai helps me realize the kind of break
through this can bring to real time live streaming.  


Bram went with the technical aspects of the design of the live bittorrent
technology and how to keep the delays as minimum as possible. He was talking at
the network packets level and explaining how the packets need to be distributed
from one node to another so that delay can be as minimum as possible and what
are the bottlenecks that exist during the packet transfer. The innovative
solutions that he had use to make these possible. He started by giving a pitch
to <a href="http://cr.yp.to/djb.html">Dan Bernstein</a>'s ciphers and explained
about the TCP handshake and udp transfers and how 
{{% wikipedia article="Micro_Transport_Protocol" %}} goes in the background during transfers
and not affect peak real time traffic.  The details could by got only if I read
through his spec a couple of times.


One interesting thing that struck me was. One engineer asked the question, "how
did he test his development of live bittorrent system?". Bram got excited to
share his valuable experience in doing that. He said, few years ago he made a
point saying "Remove all psychic powers in software development" - by this he
meant, remove all assumptions that a software will work "magically", "assume"
that it work under all conditions, but rather encode the scenarios and simulate
all the possible scenarios under which you want your software to work and then
run your software through it. To this effect, he seemed to built a small
simulator which can help him test the system. That was a good learning and major
take away for me from this session.