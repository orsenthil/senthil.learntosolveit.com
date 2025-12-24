.. title: How identation works for Python programs?
.. slug: how-identation-works-for-python-programs
.. date: 2008-05-29 19:02:00
.. tags: python, indentation, syntax, parsing
.. category: Programming
.. description: An explanation of how Python's lexical analyzer handles indentation using a stack-based approach to create code blocks.

It is well explained in [this article](http://www.secnetix.de/~olli/Python/block_indentation.hawk).

It is the lexical analyzer that takes care of the indentation and not the python parser. Lexical analyzer maintains a stack for the indentation.
1) First for no indentation, it would stored 0 in the stack [0]
2) Next when any Indentation occurs, it denotes it by token INDENT and pushes the indent value to the stack[0]. Think of it as a beinging { brace in the C program. And if we visualized, the can be only one INDENT statement per line.
4) When de-indent occurs in a line, as many values are popped out of the stack as the new reduced indentation till the value on the top of the stack is equal to new indentation (if not equal, error) and for each value popped out a DEDENT token in written. (Like multiple end }} in C)

A simple code like this

```
if x:
    if true:
        print 'yes'
print 'end'
```

Would be written as:

<pre>

`<if><x><:>`                           # Stack[0]
`<INDENT><if><true><:>`  # Stack [0,4]
`<INDENT><print><'><yes><'>` # Stack [0,4,8]
`<DEDENT><DEDENT><print><'><end><'>` #Stack[0]

</pre>

The parser would just consider the  as <INDENT> as { of the block and  <DEDENT>  as } of the block would be able to parse it as logical blocks.

[That](http://www.secnetix.de/~olli/Python/block_indentation.hawk) was a well written article again.