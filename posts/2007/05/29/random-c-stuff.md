<html><body><p>While browing through comp.lang.c found this interesting discussion.



</p><pre>



/* Without using /, % or * operator, write a function to divide a number by 3.

 * */

#include 



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



</pre>



Never have explored the capablities of stdlib. Infact, with C Programming

Language out of touch for so many months, I was thinking this program will

seriously fail, thinking kind of how come div_t datatype, d.quote

(object.property ?) etc. gcc will crib saying dont using c++. But it worked

perfectly fine.</body></html>