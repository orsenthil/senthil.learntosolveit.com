<html><body><p>Syntax and Semantics



What's with All the Parentheses?

* extensive use of parentheses and prefix notation.

* when John McCarthy first invented Lisp, he intended to implement a more Algol-like syntax, which he called M-expressions.

* The project of defining M-expressions precisely and compiling them or at least translating them into S-expressions was neither finalized nor explicitly abandoned. It just receded into the indefinite future, and a new generation of programmers appeared who preferred [S-expressions] to any FORTRAN-like or ALGOL-like notation that could be devised.



Breaking Open the Black Box

* In most programming languages, the language processor--whether an interpreter or a compiler--operates as a black box.

* Language processor is divided into three subsystems.

1) a lexical analyzer breaks up the stream of characters into tokens.

2) and feeds them to a parser that builds a tree representing the expressions in the program, according to the language's grammar.

3) This tree--called an abstract syntax tree--is then fed to an evaluator that either interprets it directly or compiles it into some other language such as machine code.



* Common Lisp defines two black boxes, one that translates text into Lisp objects and another that implements the semantics of the language in terms of those objects. The first box is called the reader, and the second is called the evaluator



* Each black box defines one level of syntax. The reader defines how strings

of characters can be translated into Lisp objects called s-expressions.



<!--more Further Notes on Syntax and Semantics-->



* (foo 1 2) is  legal s-expression whereas ("foo" 1 2) is not, because a list

starting with string has no meaning.



* This split of Black Box into two has a couple of consequences:

* One is that you can use s-expressions, as an externalizable data format (

remember the file database example) for data other than source code, using READ to read it and PRINT to print it.



* The other consequence is that since the semantics of the language are defined in terms of trees of objects rather than strings of characters, it's easier to generate code within the language than it would be if you had to generate code as text. 



* Generating code completely from scratch is only marginally easier--building

 up lists vs. building up strings is about the same amount of work. The real

 win, however, is that you can generate code by manipulating existing data. (

This is the basis of macros in lisp)





S-expressions



* Elements of s-expressions are lists and atoms

* Lists are delimited by parentheses and can contain any number of

whitespace-separated elements. ( Recursion here)

* Atoms are everything else.

* Comments--which aren't, technically speaking, s-expressions--start with a semicolon, extend to the end of a line, and are treated essentially like whitespace.



* Since lists are syntactically so trivial, the only remaining syntactic rules

 you need to know are those governing the form of different kinds of atoms (

 numbers, strings and names)



* Numbers are fairly straightforward: any sequence of digits--possibly prefaced with a sign (+ or -), containing a decimal point (.) or a solidus (/), or ending with an exponent marker--is read as a number.

E.g: 123, 3/7, 1.0,1.0e0, 1.0d0, 1.0e-4,+42,-42



* All rationals are internally represented in a simplified form.

* On the other hand, 1.0, 1.0d0, and 1 can all denote different objects

because the different floating-point representations and integers are

different types.



* Strings are enclosed in double quotes.Within a string a backslash (\) escapes the next character, causing it to be included in the string regardless of what it is. The only two characters that must be escaped within a string are double quotes and the backslash itself. 



* Names used in Lisp programs, such as FORMAT and hello-world, and *db* are represented by objects called symbols.



* Almost any character can appear in a name. Whitespace characters cannot

appear, because the elements of the list are separated by whitespace.

* No periods only name.

* open and close parentheses, double and single quotes, backtick, comma,

colon, semicolon, backslash, and vertical bar are for syntactic purposes in

lisp. if wish to include them in name, precede with backslash or two vertical

bars.



* While reading names, the reader converts all unescaped characters in a name

to their uppercase equivalents. Thats why REPL prints the upper case name

* Standard style, these days, is to write code in all lowercase and let the reader change names to uppercase



* the reader interns symbols--after it has read the name and converted it to

all uppercase, the reader looks in a table called a package for an existing

symbol with the same name. If cant find one, create a new symbol and add it

to the table or return the symbol as already in the table.



* hyphenated names is a convention.

* Global variables are given names that start and end with *

* Constants are given names, starting and ending with +.

* Few programmers, define name starting with % and %%.



* The syntax of list, number,strings and symbols represent a good amount of

lisp programs.



x             ; the symbol X

()            ; the empty list

(1 2 3)       ; a list of three numbers

("foo" "bar") ; a list of two strings

(x y z)       ; a list of three symbols

(x 1 "foo")   ; a list of a symbol, a number, and a string

(+ (* 2 3) 4) ; a list of a symbol, a list, and a number.



An only slightly more complex example is the following four-item list that contains two symbols, the empty list, and another list, itself containing two symbols and a string:



(defun hello-world ()

  (format t "hello, world"))





S-expressions as Lisp Forms.



* Common Lisp's evaluation rule defines a second level of syntax that

determines which s-expressions can be treated as Lisp forms.

* Any atom--any nonlist or the empty list--is a legal Lisp form as is any list that has a symbol as its first element.

* For purposes of discussion, you can think of the evaluator as a function that takes as an argument a syntactically well-formed Lisp form and returns a value, which we can call the value of the form.

* The simplest Lisp forms, atoms, can be divided into two categories: symbols and everything else.

*  symbol, evaluated as a form, is considered the name of a variable and

evaluates to the current value of the variable.

* For instance, the symbol PI names a constant variable whose value is the best possible floating-point approximation to the mathematical constant pi.

* All other atoms--numbers and strings are the kinds you've seen so far--are

self-evaluating objects.

* It's also possible for symbols to be self-evaluating in the sense that the variables they name can be assigned the value of the symbol itself. Two important constants that are defined this way are T and NIL, the canonical true and false values.

* Another class of self-evaluating symbols are the keyword symbols--symbols whose names start with :.

* To determine what kind of form a given list is, the evaluator must determine whether the symbol that starts the list is the name of a function, a macro, or a special operator.



Function Calls

* The evaluation rule for function call forms is simple: evaluate the remaining elements of the list as Lisp forms and pass the resulting values to the named function.

(function-name argument*)

* Thus, the following expression is evaluated by first evaluating 1, then evaluating 2, and then passing the resulting values to the + function, which returns 3:

(+ 1 2)



Special Operators

* Because all the arguments to a function are evaluated before the function is called, there's no way to write a function that behaves like the IF operator

* To solve this problem, Common Lisp defines a couple dozen so-called special operators, IF being one, that do things that functions can't do. There are 25 in all, but only a small handful are used directly in day-to-day programming.

* The rule for IF is pretty easy: evaluate the first expression. If it evaluates to non-NIL, then evaluate the next expression and return its value. Otherwise, return the value of evaluating the third expression or NIL if the third expression is omitted.

* An even simpler special operator is QUOTE, which takes a single expression as its "argument" and simply returns it, unevaluated.

* QUOTE is used commonly enough that a special syntax for it is built into the reader. Instead of writing the following:



(quote (+ 1 2))



you can write this:



'(+ 1 2)



This syntax is a small extension of the s-expression syntax understood by the reader. From the point of view of the evaluator, both those expressions will look the same: a list whose first element is the symbol QUOTE and whose second element is the list (+ 1 2).15



Macros:

* While special operators extend the syntax of Common Lisp beyond what can be expressed with just function calls, the set of special operators is fixed by the language standard. Macros, on the other hand, give users of the language a way to extend its syntax

* The evaluation of a macro form proceeds in two phases: First, the elements of the macro form are passed, unevaluated, to the macro function. Second, the form returned by the macro function--called its expansion--is evaluated according to the normal evaluation rules.



*  For instance, when you compile a whole file of source code with the

function COMPILE-FILE, all the macro forms in the file are recursively

expanded until the code consists of nothing but function call forms and

special forms. This macroless code is then compiled into a FASL file that

the LOAD function knows how to load.



* Since the evaluator doesn't evaluate the elements of the macro form before

passing them to the macro function, they don't need to be well-formed Lisp

forms.



* In other words, each macro defines its own local syntax. For instance, the backwards macro from Chapter 3 defines a syntax in which an expression is a legal backwards form if it's a list that's the reverse of a legal Lisp form.



* macros (while syntantically similar to functions) provide an exciting hook

into the compiler.



Truth, Falsehood and Equality.

* T for True, NIL for False value and everything else is True.

* tricky thing about NIL is that it's the only object that's both an atom and a list: in addition to falsehood, it's also used to represent the empty list.

* nil, (), 'nil, '() evaluate to NIL.

* t, 't evaluate to T.

*  Common Lisp provides a number of type-specific equality predicates: = is used to compare numbers, CHAR= to compare characters, and so on.

* EQ tests for "object identity"--two objects are EQ if they're

identical.(Dont use as they are implementation dependent)

* Thus, Common Lisp defines EQL to behave like EQ except that it also is guaranteed to consider two objects of the same class representing the same numeric or character value to be equivalent.

*EQUAL loosens the discrimination of EQL to consider lists equivalent if they

have the same structure and contents, recursively, according to EQUAL. EQUAL

also considers strings equivalent if they contain the same characters.

* EQUALP is similar to EQUAL except it's even less discriminating. It considers two strings equivalent if they contain the same characters, ignoring differences in case. 



Formatting Lisp Code.

*  The indentation should reflect the structure of the code.

* Macro and special forms that implement control constructs are typically indented a little differently: the "body" elements are indented two spaces relative to the opening parenthesis of the form.

(defun print-list (list)

  (dolist (i list)

    (format t "item: ~a~%" i)))

* re-indent a whole expression by positioning the cursor on the opening parenthesis and typing C-M-q. 

* Or you can re-indent the whole body of a function from anywhere within it by typing C-c M-q.

* Finally, comments should be prefaced with one to four semicolons depending on the scope of the comment as follows:

*;;;; four colon comments for file header. ;;; three colon for paragraph.

;; for the code following, which is indented along with code.</p></body></html>