<html><body><p>While listening to an introductory programming class, came across the mention of this this "<a href="http://en.wikipedia.org/wiki/Ariane_5_Flight_501">Ariane 5 Flight 501</a>" failure incident, which was caused by Arithmetic Exception and Integer overflow resulted from automatic type casting float to integer in the ADA program. Very costly software bug.



<a href="http://www-aix.gsi.de/~giese/swr/ariane5.html">This German article</a> discusses the issue. Below is the English translation of the same with the help of translate.google.com with <i>some comments</i>.



</p><hr>

    Ariane 5 - 501 (1-3) Ariane 5 - 501 (1-3)



4th June 1996, Kourou / FRZ. Guyana, ESA Guyana, ESA



Maiden flight of the new European launcher (weight: 740 tons, payload 7-18 t) with 4 Cluster satellites

Development costs in 10 years: DM 11 800 million <i>I am not sure about 11 space 800 million. If it is, then its 4 trillion Rupees roughly.</i>



Ada program of the inertial navigation system (excerpt):

<pre>

 ... 

 declare 

   vertical_veloc_sensor: float; 

   horizontal_veloc_sensor: float; 

   vertical_veloc_bias: integer; 

   horizontal_veloc_bias: integer; 

   ... 

 begin 

   declare 

     pragma suppress(numeric_error, horizontal_veloc_bias);

   begin 

     sensor_get (vertical_veloc_sensor); 

     sensor_get (horizontal_veloc_sensor); 

     vertical_veloc_bias := integer(vertical_veloc_sensor); 

     horizontal_veloc_bias := integer(horizontal_veloc_sensor); 

     ... 

   exception exceptionnelle 

     When numeric_error =&gt; calculate_vertical_veloc (); 

     when others =&gt; use_irs1 (); 

   end; 

  irs2 end;



</pre>



Effect:

37 seconds after ignition of the rocket (30 seconds after Liftoff) Ariane 5 reached 3700 m in altitude with a horizontal velocity of 32768.0 (internal units).This value was about five times higher than that of Ariane 4th



The transformation into a whole number led to an overflow, but was not caught.



The replacement computer (redundancy!) Had the same problem 72 msec before and immediately switched from <i>that</i>.



This resulted in that diagnostic data to the main computer were sent to this interpreted as trajectory data.Consequently, nonsensical control commands to the side, pivoting solid engines, and later to the main engine, to the deviate Flight no large (over 20 degrees) to correct them. 



The rocket, however, threatened damage control and tested all himself (39 sec). <i> I guess auto-destruct.</i>



An intensive test of the navigation and main computer had not been undertaken since the software was in tested Ariane 4.



Damage:

DM 250 million start-up costs (<i>~ 8.5 billion INR</i>)

DM 850 million Cluster satellites (<i>~ 29 billion INR</i>)

DM 600 million for future improvements (<i>~ 20 billion INR</i>)

Loss of earnings for 2 to 3 years



The next test flight was only 17 months later carried out - 1 Stage ended prematurely firing.



The first commercial flight took place in December 1999.



Tragedy:



The problematic part of the program was only in preparation for the launch and the launch itself needed.

It should only be a transitional period to be active, for security reasons: 50 sec, to the ground station at a launch control over the interruption would have.



Despite the very different behavior of the Ariane 5 was nothing new about value.



Optimization:

Only 3 of 7 for a variables overflow examined - for the other 4 variables evidence existed that the values would remain small enough (Ariane 4).



This evidence was not for the Ariane 5 and this was not even understood.

Problem was with the of reuse of software!



Incredible - after 40 years of software-defect findings:



It was during program design assumes that only hardware failure may occur!

Therefore, the replacement computers also identical software. The system specification established that in case of failure of the computer is off and the replacement computer einspringt. A restart of a computer was not useful, since the redefinition of the flying height is too expensive.



PS: The attempt to establish new 4 Cluster satellites to launch, succeeded in July and August 2000 with two Russian launchers.



<hr></body></html>