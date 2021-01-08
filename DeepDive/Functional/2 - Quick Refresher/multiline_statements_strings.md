# PYTHON PROGRAM
    ---------> physical lines of code  * end with a physical newline character
        ---------> logical lines of code * end with a logical NEWLINE token
            ---------> tokenized 

LINE CONVERSION can be **implicit** or **explicit**

### IMPLICIT

Expressions in:
    
* list literals: []
* tuple literals: ()
* dictionary literals: {}
* set literals: {}
* function arguments/parameters which also support inline comments

e.g.

### Lists

    [1,  # item 1
     2,  # this is an inline comment
     3]  # item 3

### Functions

    # Defining a function
    def function(a,
                 b,  # comment
                 c):
        print(a, b, c)

    # Calling a function
    function(a,
             b,  # comment
             c):


### EXPLICIT

e.g.

    if a or \ <---- must use the backslash 
       b and c


### Triple single/double quotes

    """ This is a 
    multiline string """
