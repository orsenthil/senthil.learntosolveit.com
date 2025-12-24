---
title: "Random C Stuff."
slug: random-c-stuff
date: 2007-05-29 20:17:00
tags: c, stdlib, programming, division
category: Programming
description: Exploring the div function in C's stdlib to divide a number by 3 without using standard arithmetic operators
---

```c

/**
 *Without using /, % or * operator, write a function to divide a number by 3.
 **/

#include <stdio.h>

int divideby3(int);

int main(int argc,char **argv)
{
	int res;
	res = divideby3(9);
	printf("%d",res);
	return 0;
}

int divideby3(int aNumber)
{
	div_t d = div(aNumber, 3);
	return d.quot;
}

```

Never have explored the capablities of {{% wikipedia article="C standard library" text="stdlib" %}}. Infact, with C Programming
Language out of touch for so many months, I was thinking this program will
seriously fail, thinking kind of how come div_t datatype, d.quote
(object.property ?) etc. {{% wikipedia article="GNU Compiler Collection" text="gcc" %}} will crib saying dont using c++. But it worked
perfectly fine.

----


umm, {{% wikipedia article="Struct (C programming language)" text="structs" %}} are part of standard C.

div_t is a struct:

<pre>
/* Returned by `div'.  */


typedef struct {
int quot;                   /* Quotient.  */
int rem;                    /* Remainder.  */

} div_t;</pre>

_bluesmoon_

----


Yes , I realized about struct datatype in C and unfortunately forgot the mention that in the post. All I was thinking about is, it was so out-of-mind (due to out-of-sight) and all obj.property and obj.method was what coming up.

_Senthil_