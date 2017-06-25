<html><body><code>Practical: A Simple Database



* In this chapter you'll write a simple database for keeping track of CDs.

* Common Lisp provides three distinct kinds of operators: functions, macros, and special operators.



CDs and Records

* To keep track of CDs that need to be ripped to MP3s and which CDs should be

ripped first, each record in the database will contain the title and artist

of the CD, a rating of how much the user likes it, and a flag saying whether

it has been ripped.



* need a way to represent a single database record.

* user defined class - CLOS ( Common Lisp Object System)



CL-USER&gt; (list 1 2 3)

(1 2 3)



* A plist is a list where every other element, starting with the first, is a

symbol that describes what the next element in the list is. Symbol can be

thought of as a name.



* For the symbols that name the fields in the CD database, you can use a particular kind of symbol, called a keyword symbol.



CL-USER&gt; (list :a 1 :b 2 :c 3)

(:A 1 :B 2 :C 3)



* function GETF, which takes a plist and a symbol and returns the value in the

plist following the symbol.



CL-USER&gt; (getf (list :a 1 :b 2 :c 3) :c)

3



* make-cd that will take the four fields as arguments and return a plist

representing that CD.



CL-USER&gt; (defun make-cd(title artist rating ripped)

       (list :title title :artist artist :rating rating :ripped ripped))

MAKE-CD

CL-USER&gt;

* DEFUN tells us that this form is defining a new function.

* When make-cd is called, the arguments passed to the call will be bound to the variables in the parameter list. For instance, to make a record for the CD Roses by Kathy Mattea, you might call make-cd like this:



CL-USER&gt; (make-cd "Roses" "Kathy Mattea" 7 t)

(:TITLE "Roses" :ARTIST "Kathy Mattea" :RATING 7 :RIPPED T)

CL-USER&gt;



<!--more Read the Notes further...-->





Filling CDs.

* Larger Constructs to hold records.

* Also for simplicity you can use a global variable, *db*, which you can

define with the DEFVAR macro. The asterisks (*) in the name are a Lisp

naming convention for global variables.



* You can use the PUSH macro to add items to *db*. But it's probably a good idea to abstract things a tiny bit, so you should define a function add-record that adds a record to the database.



CL-USER&gt; (defun add-record (cd) (push cd *db*))

ADD-RECORD



* add-record and make-cd together to add CDs to the database.



CL-USER&gt; (add-record (make-cd "Fly" "Dixie Chicks" 8 t))

((:TITLE "Fly" :ARTIST "Dixie Chicks" :RATING 8 :RIPPED T))

CL-USER&gt; (add-record (make-cd "Roses" "Kathy Mattea" 7 t))

((:TITLE "Roses" :ARTIST "Kathy Mattea" :RATING 7 :RIPPED T)

 (:TITLE "Fly" :ARTIST "Dixie Chicks" :RATING 8 :RIPPED T))

CL-USER&gt; (add-record (make-cd "Home" "Dixie Chicks" 9 t))

((:TITLE "Home" :ARTIST "Dixie Chicks" :RATING 9 :RIPPED T)

 (:TITLE "Roses" :ARTIST "Kathy Mattea" :RATING 7 :RIPPED T)

 (:TITLE "Fly" :ARTIST "Dixie Chicks" :RATING 8 :RIPPED T))

CL-USER&gt;



* Current value of *db* by typing *db*



CL-USER&gt; *db*



* dump-db function that dumps out the database in a more human-readable

format.



CL-USER&gt; (defun dump-db()

       (dolist (cd *db*)

         (format t "~{~a:~10t~a~%~}~%" cd)))

DUMP-DB

CL-USER&gt; 



* looping over all the elements of *db* with the DOLIST macro, binding each element to the variable cd in turn. For each value of cd, you use the FORMAT function to print it.

* In format, t is shorthand for the stream *standard-output*.

* Format directives start with ~ (much the way printf's directives start with %).

-----

One of the coolest FORMAT directives is the ~R directive. Ever want to know

how to say a really big number in English words? Lisp knows.

CL-USER&gt; (format nil "~R" 42424242424242424242424242424242424242424242424242)

"forty-two quindecillion, four hundred and twenty-four quattuordecillion, two hundred and forty-two tredecillion, four hundred and twenty-four duodecillion, two hundred and forty-two undecillion, four hundred and twenty-four decillion, two hundred and forty-two nonillion, four hundred and twenty-four octillion, two hundred and forty-two septillion, four hundred and twenty-four sextillion, two hundred and forty-two quintillion, four hundred and twenty-four quadrillion, two hundred and forty-two trillion, four hundred and twenty-four billion, two hundred and forty-two million, four hundred and twenty-four thousand, two hundred and forty-two"

CL-USER&gt; 

----

* ~a directive is the aesthetic directive; it means to consume one argument

and output it in a human-readable form. This will render keywords without

the leading : and strings without quotation marks.



CL-USER&gt; (format t "~a" "Dixie Chicks")

Dixie Chicks

NIL

CL-USER&gt; (format t "~a" :title)

TITLE

NIL

CL-USER&gt;



* The ~t directive is for tabulating. The ~10t tells FORMAT to emit enough spaces to move to the tenth column before processing the next ~a. A ~t doesn't consume any arguments.

CL-USER&gt; (format t "~a:~10t~a" :artist "Dixie Chicks")

ARTIST:   Dixie Chicks

NIL

CL-USER&gt;



* When FORMAT sees ~{ the next argument to be consumed must be a list. FORMAT loops over that list, processing the directives between the ~{ and ~}.

* The ~% directive doesn't consume any arguments but tells FORMAT to emit a newline. 



* we could have removed dolist macro call and used the format directive

itself:



CL-USER&gt; (defun dump-db()

       (format t "~{~{~a:~10t~a~%~}~%~}" *db*))

DUMP-DB

CL-USER&gt;



Improving User Interaction.

* need some way to prompt the user for a piece of information and read it.



CL-USER&gt; (defun prompt-read(prompt)

       (format *query-io* "~a: " prompt)

       (force-output *query-io*)

       (read-line *query-io*))

PROMPT-READ

CL-USER&gt;

* format to emit the prompt.

* FORCE-OUTPUT is necessary in some implementations to ensure that Lisp doesn't wait for a newline.

* read a single line of text with the aptly named READ-LINE function

* query-io is a global variable, can be recognized by the *query-io* naming.



combing make-cd with prompt-read



CL-USER&gt; (defun prompt-for-cd()

       (make-cd

        (prompt-read "Title")

        (prompt-read "Artist")

        (prompt-read "Rating")

        (prompt-read "Ripped [y/n]")))

PROMPT-FOR-CD

CL-USER&gt;



* prompt-read returns a string, for converting the value to integer, lets use

lisp's parse-integer function.

* parse-integer takes an optional argument :junk-allowed which tells to relax

the conversion, if there is any exception.

* junk-allowed returns nill, if that cannot find the integer, to get over and

set it as 0, we use the or macro.



CL-USER&gt; (parse-integer (prompt-read "Rating"))

Rating: 10



10

2

CL-USER&gt; (parse-integer(prompt-read "Rating"):junk-allowed t)

Rating: 10



10

2

CL-USER&gt; (parse-integer(prompt-read "Rating"):junk-allowed t)

Rating: Senthil



NIL

0

CL-USER&gt; (or(parse-integer(prompt-read "Rating"):junk-allowed t)0)

Rating: Senthil



0

CL-USER&gt;



* For y or n prompt, we can use common lisp function Y-OR-N-P, that will

reprompt the user till  something starting with Y,y,N,n is entered.





So, the final prompt-for-cd will be:



CL-USER&gt; (defun prompt-for-cd ()

       (make-cd

        (prompt-read "Title")

        (prompt-read "Artist")

        (or (parse-integer (prompt-read "Rating"):junk-allowd t)0)

        (y-or-n-p "Ripped [y/n]")))

PROMPT-FOR-CD



* lets go for adding a bunch of CDs.

* You can use the simple form of the LOOP macro, which repeatedly executes a body of expressions until it's exited by a call to RETURN.



CL-USER&gt; (defun add-cds()

       (loop (add-record (prompt-for-cd))

         (if (not (y-or-n-p "Another? [y/n]"))(return))))

ADD-CDS

CL-USER&gt; 



Saving and Loading the Database



*save-db function that takes a filename as an argument and saves the current state of the database.



CL-USER&gt; (defun save-db (filename)

       (with-open-file (out filename

                :direction :output

                :if-exists :supersede)

         (with-standard-io-syntax

           (print *db* out))))

SAVE-DB

CL-USER&gt;



* WITH-OPEN-FILE macro opens a file, binds the stream to a variable, executes a set of expressions, and then closes the file. The list following WITH-OPEN-FILE is not function,but list of parameters to WITH-OPEN-FILE, defines the file to open to out stream, direction, output and if the file exists, then supersede.

After opening the file, we need to print the content using print command, which is different from formant, it prints in lisp recognizable objects which be read back by lisp-reader.

* WITH-STANDARD-IO-SYNTAX ensures that certain variables that affect the behavior of PRINT are set to their standard values.



CL-USER&gt; (save-db "~/my-cds.db")



If open my-cds.db, we will find the output as in *db* at CL-USER&gt; prompt.



The function to load the database back is similar.



CL-USER&gt; (defun load-db(filename)

       (with-open-file (in filename)

         (with-standard-io-syntax

           (setf *db* (read in)))))

LOAD-DB

CL-USER&gt;



* The SETF macro is Common Lisp's main assignment operator. It sets its first argument to the result of evaluating its second argument.



Querying the Database

* query database.

Something LIKE (select :artist "Dixie Chicks")

* REMOVE-IF-NOT takes a predicate and a list and returns a copy of the list,

containing only the predicate.

* The predicate argument can be any function that accepts a single argument

* and returns a boolean value--NIL for false and anything else for true.



CL-USER&gt; (remove-if-not #'evenp '(1 2 3 4 5 6 7 8 9 10))

(2 4 6 8 10)

CL-USER&gt;



* The funny notation #' is shorthand for "Get me the function with the following name." Without the #', Lisp would treat evenp as the name of a variable and look up the value of the variable, not the function.



* We can also pass, remove-if-not, an anonymous function.



CL-USER&gt; (remove-if-not #'(lambda (x)(= 0(mod x 2)))' (1 2 3 4 5 6 7 8 9 10))

(2 4 6 8 10)

CL-USER&gt;



* The anonymous function here is (lambda (x) (=0 (mod x 2))) which returns

true when x is even, else false.



* Note that lambda isn't the name of the function--it's the indicator you're defining an anonymous function.



* To select record using artist, we use the property of plist, getf, and equal

to compare and put them all together in a lambda expression.



CL-USER&gt; (remove-if-not 

      #'(lambda (cd) (equal (getf cd :artist) "Dixie Chicks")) *db*)

((:TITLE "Home" :ARTIST "Dixie Chicks" :RATING 9 :RIPPED T)

 (:TITLE "Fly" :ARTIST "Dixie Chicks" :RATING 8 :RIPPED T))

CL-USER&gt;



* To wrap the whole expression in a function.

CL-USER&gt; (defun select-by-artist (artist)

       (remove-if-not

        #'(lambda (cd) (equal (getf cd :artist)artist)) *db*))

SELECT-BY-ARTIST

CL-USER&gt; 

* Anonymous functions, embeds the required details like artist.



* More general select function, with Anonymous function at the next stage.



CL-USER&gt; (defun select (selector-fn)

       (remove-if-not selector-fn *db*))

SELECT

CL-USER&gt; (select #'(lambda (cd) (equal (getf cd :artist) "Dixie Chicks")))

((:TITLE "Home" :ARTIST "Dixie Chicks" :RATING 9 :RIPPED T)

 (:TITLE "Fly" :ARTIST "Dixie Chicks" :RATING 8 :RIPPED T))

CL-USER&gt;



* Anonymous function creation can be wrapped up.



CL-USER&gt; (defun artist-selector (artist)

       #'(lambda (cd) (equal (getf cd :artist) artist)))

ARTIST-SELECTOR

CL-USER&gt; (select (artist-selector "Dixie Chicks"))

((:TITLE "Home" :ARTIST "Dixie Chicks" :RATING 9 :RIPPED T)

 (:TITLE "Fly" :ARTIST "Dixie Chicks" :RATING 8 :RIPPED T))

CL-USER&gt;





* Write a general purpose, selector function generator, a function that,

depending upon what arguments is getting passed, will generate a selector

function for different fields, or different combination of fields.



*Keyword parameters

*Write functions with varying number of parameters, which are bound to the

corresponding arguments to the call to the function.



(defun foo (&amp;key a b c) (list a b c))



The only difference is the &amp;key at the beginning of the argument list. However, the calls to this new foo will look quite different. These are all legal calls with the result to the right of the ==&gt;:



(foo :a 1 :b 2 :c 3)  ==&gt; (1 2 3)

(foo :c 3 :b 2 :a 1)  ==&gt; (1 2 3)

(foo :a 1 :c 3)       ==&gt; (1 NIL 3)

(foo)                 ==&gt; (NIL NIL NIL)



* Need to differentiate between NIL assigned when no value passed vs

explicitly assigned NIL.



* To allow this, when you specify a keyword parameter you can replace the simple name with a list consisting of the name of the parameter, a default value, and another parameter name, called a supplied-p parameter.

* supplied-p parameter will set to true or false if an arugment was passed to

the function call.



(defun foo (&amp;key a (b 20) (c 30 c-p)) (list a b c c-p))



Now the same calls from earlier yield these results:



(foo :a 1 :b 2 :c 3)  ==&gt; (1 2 3 T)

(foo :c 3 :b 2 :a 1)  ==&gt; (1 2 3 T)

(foo :a 1 :c 3)       ==&gt; (1 20 3 T)

(foo)                 ==&gt; (NIL 20 30 NIL)



* A general selector function, based on the above discussions will be:



(defun where (&amp;key title artist rating (ripped nil ripped-p))

  #'(lambda (cd)

      (and

       (if title    (equal (getf cd :title)  title)  t)

       (if artist   (equal (getf cd :artist) artist) t)

       (if rating   (equal (getf cd :rating) rating) t)

       (if ripped-p (equal (getf cd :ripped) ripped) t))))



* Updating Existing Records--Another Use for WHERE



(defun update (selector-fn &amp;key title artist rating (ripped nil ripped-p))

  (setf *db*

        (mapcar

         #'(lambda (row)

             (when (funcall selector-fn row)

               (if title    (setf (getf row :title) title))

               (if artist   (setf (getf row :artist) artist))

               (if rating   (setf (getf row :rating) rating))

               (if ripped-p (setf (getf row :ripped) ripped)))

             row) *db*)))



* CL-USER&gt; (update (where :artist "Dixie Chicks") :rating 11)

NIL



* Function to delete rows.



(defun delete-rows (selector-fn)

  (setf *db* (remove-if selector-fn *db*)))





* Remove Duplication and winning Big

* When a Lisp expression contains a call to a macro, instead of evaluating the arguments and passing them to the function, the Lisp compiler passes the arguments, unevaluated, to the macro code, which returns a new Lisp expression that is then evaluated in place of the original macro call.

* The main syntactic difference between a function and a macro is that you

* define a macro with DEFMACRO instead of DEFUN.



CL-USER&gt;(defmacro backwards (expr) (reverse expr))

CL-USER&gt; (backwards ("hello, world" t format))

hello, world

NIL

When the REPL started to evaluate the backwards expression, it recognized that backwards is the name of a macro. So it left the expression ("hello, world" t format) unevaluated, which is good because it isn't a legal Lisp form. It then passed that list to the backwards code. The code in backwards passed the list to REVERSE, which returned the list (format t "hello, world").







</code>



</body></html>