init python:
    class QuizQuestion():
        # TODO: explanation
        '''
        question: a string
        true: a string
        false: a list of strings
        code_label: an optional string, see game/quiz_code_snippets.txt
        '''
        def __init__(self, question, true, false, explanation=None, code_label=None):
            choices = {
            question: None,
            true: True
            }
            for f in false:
                choices[f] = False

            # a list of tuples
            # ex.
            '''
            [
            ("What is the binary representation of 10?", None),
            ("1010", True),
            ("0101", False),
            ],
            '''
            choices = []
            for f in false:
                choices.append((f, False))
            # shuffle insert the true answer
            # max is total num of choices, true plus false
            idx = renpy.random.randint(0, len(false) + 1)
            choices.insert(idx, (true, True))
            # put the question at the front
            self.choices = [(question, None)] + choices

            self.explanation = explanation
            self.code_label = code_label

    general_questions = [
    
    QuizQuestion(
        question="What is the binary representation of 10?",
        true="1010",
        false=["0101"]
        ),

    QuizQuestion(
        question="What is the size of wchar_t in bits?",
        true="16", 
        false=["8", "4"]
        ),

    QuizQuestion(
        question="How many times is the value of i checked in the following C code?",
        true="3",
        false=["2", "4", "1"],
        code_label="code1"
        ),

    QuizQuestion(
        question="Which will display `hello world` in JavaScript?",
        true="console.log('hello world')",
        false=["console.print('hello world')", "document.write('hello world')"]
        ),

    QuizQuestion(
        question="What will this Python code print?",
        true="3",
        false=["0", "1", "2", "π"],
        code_label="py_code1"
        ),

    ]

    # https://github.com/freeCodeCamp/multiple-choice-questions
    
    javascript_questions = [

    QuizQuestion(
        question="Which of the following statements is true of JavaScript?",
        true="All of these choices are correct",
        false=[
        "JavaScript supports object-oriented programming",
        "JavaScript supports functional programming",
        "JavaScript supports imperative programming",
        ]
        ),

    QuizQuestion(
        question="Is JavaScript single-threaded or multi-threaded?",
        true="JavaScript is single-threaded.",
        false=[
        "Threading only applies to compiled languages.",
        "JavaScript is multi-threaded.",
        "Threading only applies in staticly typed languages.",
        ]
        ),

    QuizQuestion(
        question="What will the following code print to the console?",
        true="dlroW olleH",
        false=[
        "[ 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd' ]",
        "[ 'd', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H' ]",
        "Hello World",
        ],
        code_label='js_code1',
        explanation="You may have expected this code to print Hello World to the console. However, when we define baz, we are not creating a new array. Rather, we are simply creating a reference to the array that was created during the assignment of bar (in fact, both variables are just references to the same object, which is stored in memory behind the scenes). Since baz is just a reference to bar, and not its own array, any operation that is performed on it, is also performed on the original array. So, when we join bar back into a string, the result is a mirror image of what you might have expected! And, of course, the same result that we would have gotten from console.log(baz.join(' '));"
        ),

    QuizQuestion(
        question="When executed in a browser's console, what will the following code output?",
        true="Window {...}\nundefined",
        false=[
        "{ baz: 'Hello', bar: [Function: bar] }\nHello",
        "Window {...}\nHello",
        "{ baz: 'Hello', bar: [Function: bar] }\nundefined"
        ],
        code_label='js_code2',
        explanation="""
        You might have expected this code to log the foo object along with Hello to the console, however, arrow function expressions are not ideally suited for method functions. Here's why: arrow functions do not create their own this context, nor do they care how the function is called; rather, they inherit their this value from the enclosing scope. So in this case, this still refers to the global context, in which baz is not defined. Had bar been written with the function keyword, this code would have worked as expected, since typically, when a function is invoked with method invokation, this will always refer to the context, or object, that the function was written in.

        Note that in different environments, the global this value can reference different things. Running this code in a browser's console, as in this example, this will always refer to the global Window object. If we ran this same code in a Node environment, however, the this value would simply be an empty global object: {}.

        In general, there's no other reason why arrow functions are not an appropriate choice for object methods. So if you use them in this way, just be careful with this!
        """
        ),

    QuizQuestion(
        question="Which of the following is a feature provided by ES6 arrow functions?",
        true="They "inherit" this from the enclosing lexical context, regardless of how the function is called.",
        false=[
        "They allow for functional composition.",
        "The only advantage is shorter syntax.",
        "They are prone to fewer memory leaks."
        ],
        explanation="""
        ES6 arrow functions take this from the context where they are written and implicitly bind it to the function. Now, regardless of where that function is called it will retain the original this value. The same result could be accomplished by explicitly binding this (e.g. .bind(this)) to the function in the context you want to bind this. Otherwise, for non-arrow functions, this will be defined by the context in which a function is called.
        """
        ),

    QuizQuestion(
        question="In JS, The use of const prevents the modification of arrays and objects.",
        true="True, these are now constant values.",
        false=["False, they are only references. The actual values in the array or object can still be mutated."],
        explanation="""
        The use of const prevents a value from being reassigned. Arrays and objects, however, can be modified without being reassigned. If you have a const object dictionary and you write dictionary[freecodecamp] = true this code will run without error. However, if you were to try to reassign this constant value by writing dictionary = 5, this would throw an error: Uncaught TypeError: Assignment to constant variable. This is an important aspect to keep in mind when working with constant values in JavaScript.
        """
        ),

    QuizQuestion(
        question="Which of the following choices will empty the array foo as well as all references to foo (such as bar)?",
        true="foo.splice(0, foo.length);",
        false=[
        "foo = [];",
        "foo.empty();",
        "foo.slice(0, foo.length);",
        ],
        explanation="""
        JavaScript's native splice method modifies a referenced array in place by removing and (optionally) adding elements. splice's first parameter indicates the index at which to begin removing elements, the second indicates how many elements to remove, while the third can be any number of elements to add to the array in their place. So by invoking splice with 0 and Array.length, and by omitting the 3rd, parameter we can reliably empty an array of any length. Another method of emptying an array that works just as well, is to explicitly set the length of the array to 0, i.e. foo.length = 0;.

        The foo = []; method would not truly empty the array. Instead, it would have only reassigned the variable foo to a new array object. The original array that foo used to point to would still exist in memory, and any other references to that array, such as bar in this case, would be unaffected.

        slice is better suited to copying arrays, and is not appropriate for this use case. Array.empty() is not a native JavaScript method, so this solution would fail.
        """
        ),

    QuizQuestion(
        question="What will the following code output to the console?",
        true="super",
        false=[
        "null",
        "cool",
        "undefined",
        ],
        code_label='js_code3',
        explanation="""
        This code logs super to the console even though a is never defined in the inner function bar, becuase bar has closure over the outer function foo.

        When a function is defined inside of another function, it is said to have "closure" over that function, meaning that it has access to the variables defined in the outer function's scope. When execution reaches the console.log() statement, JavaScript searches bar's scope for a variable called a. When it does not find one, it then searches the scope "bubble" that is the next level up, in this case, the scope created by foo. If a was not defined in foo, the search would continue, moving up to the next scope. If the outer-most, or global scope is reached and a variable is still not found, JavaScript will throw a ReferenceError.

        If the way that these functions are called tripped you up, here's the explanation: foo is an immediately invoked function expression (or IIFE), invoked by the parentheses that contain 'super'. This expression resolves before anything else occurs, and since it resolves to the function bar, the second set of parentheses are simply invoking that function, and thus the console.log() statement is executed.
        """
        ),

    QuizQuestion(
        question="What will the following code log to the console?",
        true="true\nfalse",
        false=[
        "false\ntrue",
        "false\nfalse",
        "true\ntrue"
        ],
        code_label='js_code4',
        explanation="""
        The first expression will evaluate to true since the == operator performs a non-strict comparison, meaning that if the 2 values are not of the same type, JavaScript will attempt to coerce the values into comparable types. In this case, JavaScript will coerce 0 into to a boolean, and since 0 is falsy in JavaScript, it will coerce to false.

        The === operator, on the other hand, represents strict equality, meaning that no type coercion will take place. To evaluate to true, the values on either side of this symbol must be of the same type and value. This means that the second expression evaluates to false — since false and 0 are not of the same type, no further comparison is necessary.

        Note that these principles hold true for JavaScript's inequality operators as well, non-strict: !=, strict: !==.
        """
        ),

    QuizQuestion(
        question="This code does not work correctly, it simply prints five 5s to the console. How can we use ES6 to fix this problem so that the code works as expected?",
        true="By replacing the var keyword with let",
        false=[
        "By replacing the function keyword with => syntax",
        "By replacing the var keyword with const",
        "None of these answers are correct"
        ],
        code_label='js_code5',
        explanation="""
        The major advantages of the let keyword introduced in the ECMAScript 2015 specification is the ability to "block scope" a variable to a specific block, statement, or expression. This is unlike the var keyword which creates a variable that is scoped globally to the context it is defined in — either a function or the global scope. In the case of this code, replacing var with let block scopes let to the for loop, so that each iteration refers to a new instance of the variable i, and 0-4 is printed to the console as expected.

        Prior to ES6, the best solution for this problem was to create a local scope around or within the setTimeout function and passing in the value of i during each iteration of the loop. For example, by wrapping setTimeout in an IIFE and invoking it with i.
        """
        ),

    QuizQuestion(
        question="What will the following code output to the console?",
        true='"022"\n"221-1"',
        false=[
        '4\n4',
        '"04"\n"220"',
        '"022"\n"220"'
        ],
        code_label='js_code6',
        explanation="""
        What makes this code a bit tricky is the fact that JavaScript is a "weakly" or "loosely" typed language. This means that, in part, JavaScript will allow operations to be performed on values that are not of the same data types, and as a result, it will "coerce" values that are not of the same type in order to accomodate the operation. This has a significant impact on the above code snippets. Let's look at each example in turn.

        Ex: console.log(1 + -"1" + "2" - "2");
        In JavaScript, the negation symbol, e.g. -x, is treated as a unary operator, and, according to order of operations precedence, is evaluated before the four standard mathematical operators (+, -, /, *). Thus in this snippet, the first operation performed is the negation of "1". Since this value is a string, to accomodate this operation, "1" is converted to a number. From here, the expression is evaluated from left to right, since all other operators are treated equally in precedence. First 1 is added to -1, resulting in 0, followed by 0 + "2" . However, since one of these two values is a string, the remaining value is coerced into a string, and concatenation is performed rather than addition. Now we are left with "02" + "2" , a simple string concatenation with no coersion necessary, giving us the final result of "022"

        Ex: console.log("2" + "2" + 1 + -"1");
        This example is nearly identical. However, even though "1" is coerced into a number before any other operations are performed, -1 is then coerced back into a string since it is a part of the final evaluation: "2" + "2" results in "22", "22" + 1 results in "221", and "221" + -1 gives us "221-1".
        """
        ),

    QuizQuestion(
        question="What will the following code log to the console?",
        true="undefined",
        false=[
        "ReferenceError: x is not defined",
        "TypeError: x is not defined",
        "ReferenceError: x is undefined"
        ],
        code_label='js_code7',
        explanation="""
        undefined refers to a variable that has been declared but not yet assigned a value. not defined is a ReferenceError, thrown when a variable is encountered that has not yet been declared.

        If you were to comment out the first line var x; and run the code again, ReferenceError: x is not defined would be thrown.
        """
        ),

    QuizQuestion(
        question="What is the difference between == and === in JavaScript?",
        true="== represent abstract equality and allows type coercion, whereas === uses strict equality and will not coerce its arguments.",
        false=[
        "=== can be used to test deep equality of arrays and objects, whereas == cannot.",
        "None of these are correct.",
        "These operators are interchangeable and both test for equality."
        ],
        explanation="The difference between these two equality operators is that the first allows type coercion and the second does not. Because JavaScript is a loosely typed language, the abstract equality operator can establish equality between dissimilar types. For instance, "2" == 2 evaluates to true, however, this would fail under a check of strict equality. Generally, strict equality is safer and preferred, but it's good to understand the difference between these two equality operators."
        ),

    QuizQuestion(
        ),

    QuizQuestion(
        ),

    QuizQuestion(
        ),

    ]

    web_questions = [

    ]

    algorithm_questions = [

    ]

    system_questions = [

    ]