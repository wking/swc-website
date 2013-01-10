Title: Functions and Libraries in Python
Directory: book

    <ol class="toc">
      <li><a href="#s:basics">How Functions Work</a></li>
      <li><a href="#s:global">Global Variables</a></li>
      <li><a href="#s:args">Multiple Arguments</a></li>
      <li><a href="#s:return">Returning Values</a></li>
      <li><a href="#s:aliasing">Aliasing</a></li>
      <li><a href="#s:libraries">Libraries</a></li>
      <li><a href="#s:stdlib">Standard Libraries</a></li>
      <li><a href="#s:filter">Building Filters</a></li>
      <li><a href="#s:funcobj">Functions as Objects</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <p>
      On the first day of your post-doc at Euphoric State University,
      your supervisor calls you into her office to ask a favor.
      One of her previous students wrote a program to reformat and calibrate
      data produced by rock drills in the 1970s and 1990s.
      It's a useful piece of code,
      but she is now studying fossilized coral reefs,
      so she would like you to figure out how that program works
      and add some new features to it.
    </p>

    <p>
      The good news is,
      the program is only two hundred lines long.
      The bad news is,
      it's one big block of code,
      and several sections seem to be duplicated.
      Before you can start adding anything new,
      you need to clean it up.
    </p>

    <p>
      This chapter will show you how to do that,
      and along the way introduce the single most powerful idea in programming:
      abstraction.
      No programming language can possibly include everything that anyone might ever want
      (though that hasn't stopped C++ and Perl from trying&hellip;).
      Instead, languages should make it easy for people
      to create new tools to solve their specific problems,
      and the most common way to do this is
      to define <a href="glossary.html#function">functions</a>
      that combine several operations into one.
      In this chapter,
      we'll look at how functions work,
      and how to divide tasks into comprehensible, reusable chunks.
    </p>

    <section id="s:basics">

      <h2>How Functions Work</h2>

      <div class="understand" id="u:basics">
        <h3>Understand:</h3>
        <ul>
          <li>Why to break a program up into functions.</li>
          <li>How to define a new function.</li>
          <li>How to pass values into a function.</li>
          <li>How to combine functions.</li>
          <li>What a call stack is.</li>
          <li>What a variable's scope is.</li>
        </ul>
      </div>

      <p>
        As we said above,
        a function's job is to bundle several steps together
        so that they can be used as if they were a single command.
        The simplest possible function is one that just produces the same value over and over again:
      </p>

<pre src="src/funclib/zero.py">
def zero():
    return 0

result = zero()
print "zero produces", result
<span class="out">zero produces 0</span>
</pre>

      <p class="continue">
        This function is pretty pointless,
        but it does illustrate a few things.
        First, we create functions in Python using the keyword <code>def</code>,
        followed by the function's name.
        The empty parentheses signal that the function doesn't take any inputs&mdash;we'll
        see functions that do in a moment&mdash;and the colon signals
        the start of a new block of code.
        The body of the function is then indented,
        just like the body of a loop.
        The keyword <code>return</code> then specifies
        the value that the function produces.
      </p>

      <p>
        We have seen lots of examples already of calling functions,
        so the third line of code should look familiar:
        when Python sees the statement <code>result&nbsp;=&nbsp;zero()</code>
        it sets aside whatever it was doing,
        goes and does whatever the function <code>zero</code> tells it to do,
        and then continues with its original calculation using the function's result.
        In this case,
        the overall effect is to assign 0 to <code>result</code>,
        which is then printed.
      </p>

      <p>
        Functions that always produce the same value aren't particularly useful,
        so most functions take input values,
        or <a href="glossary.html#parameter">parameters</a>,
        and use them in their calculations.
        For example,
        the function <code>fahr_to_kelvin</code> takes a temperature in Fahrenheit
        (as recorded by rock drills in the 1970s)
        and returns the corresponding temperature in Kelvin:
      </p>

<pre src="src/funclib/f2k.py">
def fahr_to_kelvin(temp):
    return ((temp - 32.0) * 5.0/9.0) + 273.15

print 'water freezes at', fahr_to_kelvin(32)
print 'water boils at', fahr_to_kelvin(212)
<span class="out">water freezes at 273.15
water boils at 373.15</span>
</pre>

      <p class="continue">
        When we call <code>fahr_to_kelvin</code>,
        the value we pass in (such as <code>32</code> or <code>212</code>)
        is assigned to the variable <code>temp</code>,
        which is the function's only parameter.
        The function uses that value in its calculations,
        and returns a result as before.
      </p>

      <p>
        If one function is good,
        two must be better.
        Let's write a function to convert Kelvin to Celsius:
      </p>

<pre src="src/funclib/k2c.py">
def kelvin_to_celsius(temp):
    return temp - 273.15

print 'absolute zero is', kelvin_to_celsius(0)
<span class="out">absolute zero is -273.15</span>
</pre>

      <p class="continue">
        Instead of writing a third equation to translate Fahrenheit into Celsius,
        we can now combine the two functions we have
        to do the required calculation:
      </p>

<pre src="src/funclib/f2c.py">
def fahr_to_celsius(temp):
    degrees_k = fahr_to_kelvin(temp)
    return kelvin_to_celsius(degrees_k)

temp_f = 32.0
temp_c = fahr_to_celsius(temp_f)
print 'water freezes at', temp_c
<span class="out">water freezes at 0.0</span>
</pre>

      <p id="a:call-stack">
        To really understand what happens when we combine functions this way,
        we need to understand the <a href="glossary.html#call-stack">function call stack</a>,
        or "stack" for short.
        Here are the function definitions once again:
      </p>

<pre src="src/funclib/f2c.py">
def fahr_to_kelvin(temp):
    return ((temp - 32.0) * 5.0/9.0) + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

def fahr_to_celsius(temp):
    degrees_k = fahr_to_kelvin(temp)
    return kelvin_to_celsius(degrees_k)
</pre>

      <p class="continue">
        All three functions have a parameter called <code>temp</code>.
        Let's try calling one of the functions,
        and then printing <code>temp</code>'s value <em>after</em> the function call:
      </p>

<pre src="src/funclib/print_temp.py">
def kelvin_to_celsius(temp):
    return temp - 273.15

absolute_zero = 0.0
not_used = kelvin_to_celsius(absolute_zero)
print 'temp after function call is', temp
<span class="out">temp after function call is</span>
<span class="err">Traceback (most recent call last):
  File "src/funclib/print-temp.py", line 5, in &lt;module&gt;
    print 'temp after function call is', temp
NameError: name 'temp' is not defined</span>
</pre>

      <p class="continue">
        Why isn't <code>temp</code> defined?
        And if it isn't,
        why did we get an error for the last line of our program,
        rather than when we used <code>temp</code> inside <code>kelvin_to_celsius</code>?
      </p>

      <p>
        The answer is that
        Python doesn't actually create a variable called <code>temp</code>
        when the function is defined.
        Instead,
        it makes a note that it is supposed to create such a variable
        when <code>kelvin_to_celsius</code> is called,
        and then throw it away when the function finishes executing.
      </p>

      <p>
        This is easier to explain with pictures.
        After executing line 4 of our program,
        Python knows that <code>kelvin_to_celsius</code> refers to a function,
        and that <code>absolute_zero</code> refers to the value 0.0:
      </p>

      <figure id="f:func_call_step_1">
        <img src="img/funclib/func_call_step_1.png" alt="First Step of Function Call" />
      </figure>

      <p>
        The first thing it does when it executes line 5 is call <code>kelvin_to_celsius</code>.
        To do this,
        it creates a new storage area for variables
        and puts it on top of the one that holds
        <code>kelvin_to_celsius</code> and <code>absolute_zero</code>.
        Since the function has one parameter, <code>temp</code>,
        Python creates a variable with that name in the new storage area,
        and gives it the value 0.0
        (since that's what we passed in when we called the function):
      </p>

      <figure id="f:func_call_step_2">
        <img src="img/funclib/func_call_step_2.png" alt="Second Step of Function Call" />
      </figure>

      <p>
        This variable storage area is called
        a <a href="glossary.html#stack-frame">stack frame</a>:
        stack, because it is stacked on top of the previous area,
        and frame, because&hellip;well, just because.
        Every time a function is called&mdash;any function&mdash;Python
        creates a new frame to holds the function's variables
        and puts it on top of the stack.
        While it is executing that function's code,
        Python looks in the top stack frame to find variables;
        when the function returns,
        Python discards the top stack frame
        and starts using the one underneath it again.
      </p>

      <p>
        Since the rest of the statement on line 5
        (the line containing the function call)
        assigns the function's value to <code>not_used</code>,
        memory looks something like this after line 5 is finished:
      </p>

      <figure id="f:func_call_step_3">
        <img src="img/funclib/func_call_step_3.png" alt="Third Step of Function Call" />
      </figure>

      <p>
        It should now be clear why we got the error we did,
        and why we got it <em>where</em> we did.
        When Python executes line 6,
        the uppermost frame of the stack doesn't contain a variable called <code>temp</code>.
        The frame that <em>did</em> contain that variable
        was discarded when the call to <code>kelvin_to_celsius</code> finished.
      </p>

      <p>
        To understand why Python (and other languages) do all of this,
        let's go back to <code>fahr_to_celsius</code> again.
        Its definition,
        and the definitions of the functions it calls,
        are:
      </p>

<pre src="src/funclib/f2c.py">
def fahr_to_kelvin(temp):
    return ((temp - 32.0) * 5.0/9.0) + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

def fahr_to_celsius(temp):
    degrees_k = fahr_to_kelvin(temp)
    return kelvin_to_celsius(degrees_k)
</pre>

      <p class="continue">
        These nine lines of code define the variable <code>temp</code> three times&mdash;once
        in each function&mdash;but those three <code>temp</code>s are <em>not</em> the same variable.
        The first <code>temp</code>,
        defined on line 1,
        is created each time <code>fahr_to_kelvin</code> is called,
        and only lasts as long as that call is in progress.
        In computer science jargon,
        it is <a href="glossary.html#local-scope">local</a> to the function.
        Similarly,
        the second <code>temp</code> (on line 4) is local to <code>kelvin_to_celsius</code>,
        and the third (on line 7) to <code>fahr_to_celsius</code>.
        They only exist while the functions that own them are being executed,
        and can only be "seen" inside those functions.
      </p>

      <p>
        Again, some pictures will make this clearer
        (and it does need to be clear,
        since everything else about functions depends on this idea).
        Let's call <code>fahr_to_celsius</code> as before:
      </p>

<pre src="src/funclib/f2c.py">
temp_f = 32.0
temp_c = fahr_to_celsius(temp_f)
print 'water freezes at', temp_c
</pre>

      <p>
        Just before line 9 runs,
        the stack consists of a single frame,
        which contains the three functions
        and the variable <code>temp_f</code>:
      </p>

      <figure id="f:stack_single_frame">
        <img src="img/funclib/stack_single_frame.png" alt="A Call Stack With a Single Frame" />
      </figure>

      <p>
        When we call <code>fahr_to_celsius</code>,
        Python creates a new stack frame containing the variable <code>temp</code>,
        and assigns it the value 32.0
        (which it got from <code>temp_f</code>):
      </p>

      <figure id="f:stack_double_frame">
        <img src="img/funclib/stack_double_frame.png" alt="A New Stack Frame" />
      </figure>

      <p>
        <code>fahr_to_celsius</code> immediately calls <code>fahr_to_kelvin</code>,
        so Python creates another stack frame
        to hold <code>fahr_to_kelvin</code>'s local variables.
        This frame also contains a variable called <code>temp</code>,
        but since it's in a different frame,
        it's a different variable than <code>fahr_to_celsius</code>'s <code>temp</code>:
      </p>

      <figure id="f:stack_triple_frame">
        <img src="img/funclib/stack_triple_frame.png" alt="Yet Another Stack Frame" />
      </figure>

      <p>
        Using its <code>temp</code>,
        <code>fahr_to_kelvin</code> calculates a result of 273.15.
        When it returns that value,
        Python discards <code>fahr_to_kelvin</code>'s stack frame:
      </p>

      <figure id="f:stack_back_to_double_frame">
        <img src="img/funclib/stack_back_to_double_frame.png" alt="Back to a Double Frame" />
      </figure>

      <p class="continue">
        and creates a new variable <code>degrees_k</code> to hold that value
        in what is now the top frame&mdash;the one belonging to <code>fahr_to_celsius</code>:
      </p>

      <figure id="f:new_variable_in_double_frame">
        <img src="img/funclib/new_variable_in_double_frame.png" alt="A New Variable in the Second Frame" />
      </figure>

      <p class="continue">
        Python then goes through the same steps for the call to <code>kelvin_to_celsius</code>.
        It creates a stack frame with a variable <code>temp</code>,
        which it assigns the value 273.15:
      </p>

      <figure id="f:repeat_stack_frame">
        <img src="img/funclib/repeat_stack_frame.png" alt="Repeating the Process" />
      </figure>

      <p class="continue">
        does its calculations,
        and then discards the stack frame when the function is finished.
        Since <code>fahr_to_celsius</code> is also now done,
        Python discards its stack frame,
        creates a variable called <code>temp_c</code> in the original (bottom) frame,
        and assigns it the value 0.0:
      </p>

      <figure id="f:final_state_of_frames">
        <img src="img/funclib/final_state_of_frames.png" alt="The Final State" />
      </figure>

      <p>
        Every modern programming language uses this model to manage calculations.
        Each function call creates a new stack frame with its own variables.
        While the function is running,
        it uses the variables in its own frame,
        and when the function call is finished,
        the stack frame is discarded.
      </p>

      <p>
        The area of the program in which a particular variable is visible
        is called its <a href="glossary.html#scope">scope</a>.
        As a rule,
        programming languages do not let functions access variables in other functions' scopes
        because doing so would make large programs almost impossible to write.
        For example,
        imagine we used two functions to sum the squares of the values in a list:
      </p>

<pre src="src/funclib/sum_squares.py">
def sum(numbers):                       <span class="comment">#  1</span>
    result = 0                          <span class="comment">#  2</span>
    for x in numbers:                   <span class="comment">#  3</span>
        result = result + square(x)     <span class="comment">#  4</span>
    return result                       <span class="comment">#  5</span>
                                        <span class="comment">#  6</span>
def square(val):                        <span class="comment">#  7</span>
    result = val * val                  <span class="comment">#  8</span>
    return result                       <span class="comment">#  9</span>
                                        <span class="comment"># 10</span>
print sum([1, 2])                       <span class="comment"># 11</span>
</pre>

      <p class="continue">
        We expect to get 1<sup>2</sup>+2<sup>2</sup> = 5
        via the following steps:
      </p>

      <table border="1">
        <tr>
          <th></th>
          <th><code>sum</code></th>
          <th><code>sum</code></th>
          <th><code>square</code></th>
          <th><code>square</code></th>
        </tr>
        <tr>
          <th>Line</th>
          <th><code>result</code></th>
          <th><code>x</code></th>
          <th><code>val</code></th>
          <th><code>result</code></th>
        </tr>
        <tr>
          <td>2</td>
          <td>0</td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>3</td>
          <td>0</td>
          <td>1</td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>7</td>
          <td>0</td>
          <td>1</td>
          <td>1</td>
          <td></td>
        </tr>
        <tr>
          <td>8</td>
          <td>0</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <td>4</td>
          <td>1</td>
          <td>1</td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>3</td>
          <td>1</td>
          <td>2</td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>7</td>
          <td>1</td>
          <td>2</td>
          <td>2</td>
          <td></td>
        </tr>
        <tr>
          <td>8</td>
          <td>1</td>
          <td>2</td>
          <td>2</td>
          <td>4</td>
        </tr>
        <tr>
          <td>4</td>
          <td>1</td>
          <td>5</td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>5</td>
          <td>1</td>
          <td>5</td>
          <td></td>
          <td></td>
        </tr>
      </table>

      <p>
        If <code>sum</code>'s <code>result</code> and <code>square</code>'s <code>result</code>
        were the same variable, though,
        we would get 8 instead:
      </p>

      <table border="1">
        <tr>
          <th>Line</th>
          <th><code>result</code></th>
          <th><code>x</code></th>
          <th><code>val</code></th>
        </tr>
        <tr>
          <td>2</td>
          <td>0</td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>3</td>
          <td>0</td>
          <td>1</td>
          <td></td>
        </tr>
        <tr>
          <td>7</td>
          <td>0</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <td>8</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <td>4</td>
          <td>2</td>
          <td>1</td>
          <td></td>
        </tr>
        <tr>
          <td>3</td>
          <td>2</td>
          <td>2</td>
          <td></td>
        </tr>
        <tr>
          <td>7</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
        </tr>
        <tr>
          <td>8</td>
          <td>4</td>
          <td>2</td>
          <td>2</td>
        </tr>
        <tr>
          <td>4</td>
          <td>8</td>
          <td>2</td>
          <td></td>
        </tr>
        <tr>
          <td>5</td>
          <td>8</td>
          <td>2</td>
          <td></td>
        </tr>
      </table>

      <p class="continue">
        What's worse,
        if we changed the name of the variable in <code>square</code>
        from <code>result</code> to <code>y</code>,
        the final answer would be 5 again.
        Changing the name of a variable shouldn't matter:
        <em>f(x)=x<sup>2</sup></em> and <em>f(y)=y<sup>2</sup></em>
        ought to calculate the same value,
        and if changing a variable name in one part of our program
        can change the result calculated by another,
        we will have to keep the entire program in our head
        in order to make any change safely.
      </p>

      <p>
        The fundamental issue here is one of evolution rather than one of technology.
        Human short-term memory can only hold a few items at a time;
        the value is sometimes given as "seven plus or minus two",
        and while that is an over-simplification,
        it's a good guideline.
        If we need to remember more unrelated bits of information than that for more than a few seconds,
        they become jumbled and we start making mistakes.
      </p>

      <p>
        If we have to keep more than half a dozen things straight in our mind
        in order to understand or change a piece of code,
        we will therefore start making mistakes.
        Most programming languages therefore enforce a "local scope only" rule
        so that programmers can ignore what's inside the functions they are calling,
        or what's outside the functions they are writing,
        and use their short-term memory for the task at hand instead.
      </p>

      <div class="keypoints" id="k:basics">
        <h3>Summary</h3>
        <ul>
          <li>Define a function using <code>def <em>name</em>(...)</code></li>
          <li>The body of a function must be indented.</li>
          <li>Use <code><em>name</em>(...)</code> to call a function.</li>
          <li>Use <code>return</code> to return a value from a function.</li>
          <li>The values passed into a function are assigned to its parameters in left-to-right order.</li>
          <li>Function calls are recorded on a call stack.</li>
          <li>Every function call creates a new stack frame.</li>
          <li>The variables in a stack frame are discarded when the function call completes.</li>
          <li idea="perf">Grouping operations in functions makes code easier to understand and re-use.</li>
        </ul>
      </div>

    </section>

    <section id="s:global">

      <h2>Global Variables</h2>

      <div class="understand" id="u:global">
        <h3>Understand:</h3>
        <ul>
          <li>What global scope is.</li>
          <li>Why functions shouldn't communicate via global variables.</li>
        </ul>
      </div>

      <p>
        There is one important pragmatic exception to the "local scope only" rule.
        Every function also has access to the <a href="glossary.html#global-scope">global scope</a>,
        which is all the top-level definitions in the program
        (i.e., ones that aren't inside any particular function).
        In our pictures,
        the global scope is the bottom-most frame on the stack,
        which is there when the program starts and never goes away.
      </p>

      <p>
        Functions need access to the global scope because
        that is where other functions are defined.
        Going back to our temperature calculator,
        if <code>fahr_to_celsius</code> could only see variables defined in its local scope,
        it wouldn't be able to see either <code>fahr_to_kelvin</code>
        or <code>kelvin_to_celsius</code>,
        and therefore wouldn't be able to call them.
      </p>

      <p>
        Programmers also usually put constants at the top level of their program
        (i.e., define them in the global scope)
        so that they don't need to pass them into functions.
        For example,
        it's common to see code like this:
      </p>

<pre src="src/funclib/constant.py">
SCALING = 2.5

def scale_up(x):
    return x * SCALING

def scale_down(x):
    return x / SCALING
</pre>

      <p class="continue">
        (Many programmers write constants' names in upper case as a cue to readers,
        but Python doesn't enforce this.)
        When Python executes <code>scale_up</code> (or <code>scale_down</code>),
        it looks inside that function's scope for a variable called <code>SCALING</code>.
        Since there isn't one,
        it then checks the global scope,
        where it finds what it needs:
      </p>

      <figure id="f:searching_scopes">
        <img src="img/funclib/searching_scopes.png" alt="Searching Scopes" />
      </figure>

      <p>
        Defining <code>SCALING</code> once at the top of the program
        ensures that both functions always use the same scaling factor;
        this code has the same effect:
      </p>

<pre src="src/funclib/constant_duplicated.py">
def scale_up(x):
    return x * 2.5

def scale_down(x):
    return x / 2.5
</pre>

      <p class="continue">
        but it would be very easy for a programmer to change the scaling factor in one function
        and forget to change it in the other.
      </p>

      <p>
        Putting constants in the global scope is good style,
        but the following is definitely not:
      </p>

<pre src="src/funclib/badglobal.py">
largest = 0

def fixup(values):
    global largest
    for i in range(len(values)):
        if values[i] &lt; 0.0:
            values[i] = 0.0
        if values[i] &gt; largest:
            largest = values[i]

def scale(values):
    for i in range(len(values)):
        values[i] = values[i] / largest
</pre>

      <p class="continue">
        Here,
        the function <code>fixup</code> puts the largest value it has seen
        in a global variable called <code>largest</code>,
        which the function <code>scale</code> then uses.
      </p>

      <div class="box">
        <h3>The <code>global</code> Statement</h3>

        <p>
          Since we actually assign a value to <code>largest</code> inside <code>fixup</code>,
          instead of just reading its value,
          we have to tell Python that we want to use the global variable <code>largest</code>
          rather than creating one inside the function
          (which is what it would do by default);
          this is why we need the statement:
        </p>

<pre>
    global largest
</pre>

        <p class="continue">
          at the top of the function.
        </p>
      </div>

      <p>
        Using a global variable to move information from one function to another
        works fine in simple cases:
      </p>

<pre src="src/funclib/badglobal.py">
rows = [1.0, 4.0, -2.5, 3.5]
fixup(rows)
scale(rows)
print rows
<span class="out">[0.25, 1.0, 0.0, 0.875]</span>
</pre>

      <p class="continue">
        but look what happens when we start working with multiple data sets:
      </p>

<pre src="src/funclib/badglobal.py">
columns = [1.5, 1.5, -2.0, 3.0]
fixup(columns)
scale(columns)
print columns
<span class="out">[0.375, 0.375, 0.0, 0.75]</span>
</pre>

      <p class="continue">
        If we actually want each data set fixed up and scaled separately,
        the answer for <code>columns</code> should be <code>[0.5, 0.5, 0.0, 1.0]</code>.
        The problem is that
        the values in <code>columns</code> are actually being scaled by
        the largest value found in <code>rows</code>.
        Bugs like this,
        which are caused by <a href="glossary.html#side-effect">side effects</a>
        that aren't visible in either the functions' definitions or calls,
        are notoriously difficult to track down.
        In fact,
        one of the reasons Python requires us to use the <code>global</code> statement
        in <code>fixup</code>
        is to make the use of global variables more obvious,
        and to discourage us from doing so.
      </p>

      <div class="keypoints" id="k:global">
        <h3>Summary</h3>
        <ul>
          <li>Every function always has access to variables defined in the global scope.</li>
          <li idea="perf">Programmers often write constants' names in upper case to make their intention easier to recognize.</li>
          <li idea="perf">Functions should <em>not</em> communicate by modifying global variables.</li>
        </ul>
      </div>

    </section>

    <section id="s:args">

      <h2>Multiple Arguments</h2>

      <div class="understand" id="u:args">
        <h3>Understand:</h3>
        <ul>
          <li>How to pass multiple values into a function.</li>
          <li>How and why to specify default values for parameters.</li>
        </ul>
      </div>

      <p>
        The functions we have seen so far have had only one parameter.
        When we define a function,
        however,
        we can give it any number of parameters.
        When the function is called and a new stack frame is created,
        a new variable is defined for each of those parameters,
        and the actual values given by the caller are assigned to the parameters in order from left to right.
        For example,
        if we define <code>average3</code> to calculate the average of three numbers:
      </p>

<pre src="src/funclib/average_3.py">
def average3(a, b, c):
    return (a + b + c) / 3.0
</pre>

      <p class="continue">
        and call it like this:
      </p>

<pre src="src/funclib/average_3.py">
x = 2
y = 2
z = 5
print average3(x, y, z)
<span class="out">3.0</span>
</pre>

      <p class="continue">
        then just before the function returns,
        the program's memory looks like this:
      </p>

      <figure id="f:memory_before_return">
        <img src="img/funclib/memory_before_return.png" alt="State of Memory Before Function Return" />
      </figure>

      <p>
        Calling a function with the wrong number of values is an error:
      </p>

<pre src="src/funclib/average_3_wrong.py">
print average3(1, 5)
<span class="err">Traceback (most recent call last):
  File "src/funclib/average-3-wrong.py", line 4, in &lt;module&gt;
    print 1, 5, '=&gt;', average3(1, 5)
TypeError: average3() takes exactly 3 arguments (2 given)</span>
</pre>

      <p class="continue">
        This is only sensible:
        if we pass two values to <code>average3</code>,
        Python has no way of knowing what third value to use.
        We can tell it what we want
        by specifying <a href="glossary.html#default-value">default values</a> for parameters:
      </p>

<pre src="src/funclib/average_3_default.py">
def average3(a=0.0, b=0.0, c=0.0):
    return (a + b + c) / 3.0
</pre>

      <p>
        The meaning is straightforward:
        if the caller doesn't tell the function what value to use for <code>a</code>,
        the function should use 0.0,
        and similarly for the other parameters.
        We can now call our function in four different ways:
      </p>

<pre src="src/funclib/average_3_default.py">
print '()', average3()
print '(1.0)', average3(1.0)
print '(1.0, 2.0)', average3(1.0, 2.0)
print '(1.0, 2.0, 5.0)', average3(1.0, 2.0, 5.0)
<span class="out">() 0.0
(1.0) 0.333333333333
(1.0, 2.0) 1.0
(1.0, 2.0, 5.0) 2.66666666667</span>
</pre>

      <p class="continue">
        We still can't call this function with more than three parameters,
        though,
        since once again Python wouldn't know where to put the fourth and higher.
      </p>

      <p>
        Allowing people to call <code>average3</code> with fewer than three values
        isn't actually very useful.
        What <em>is</em> useful is using sensible defaults to save ourselves
        from writing several slightly-different versions of a function.
        For example,
        suppose we need a function that averages a list of numbers.
        The obvious solution is:
      </p>

<pre src="src/funclib/average_list_simple.py">
def average_list(values):
    result = 0.0
    for v in values:
        result += v
    return result / len(values)

for test in [[1.0], [1.0, 2.0], [1.0, 2.0, 5.0]]:
    print test, '=&gt;', average_list(test)
<span class="out">[1.0] =&gt; 1.0
[1.0, 2.0] =&gt; 1.5
[1.0, 2.0, 5.0] =&gt; 2.66666666667</span>
</pre>

      <p class="continue">
        Before we go on, notice that there is a bug in this function:
        if it is called for an empty list,
        the expression <code>result&nbsp;/&nbsp;len(values)</code> try to divide by zero.
        We will look at how to handle this case <a href="#p:average-none">below</a>.
      </p>

      <p>
        Now suppose that we want to be able to calculate averages for parts of our data
        instead of always calculating the average for the whole data set.
        One way would be to require the caller to slice the list:
        <span class="fixme">has slicing been introduced?</span>
      </p>

<pre>
a = average_list(values[20:90])
</pre>

      <p class="continue">
        but another would be to allow them to tell <code>average_list</code> what range to use.
        This is what most list and string methods do:
        if they are passed one value,
        they work from that index to the end of the data,
        while if they are passed two,
        they work on the range those indices delimit.
        For example,
        the string method <code>str.count</code> can be called three ways:
      </p>

      <table id="a:string-count">
        <tr>
          <td>Call</td>
          <td>Result</td>
        </tr>
        <tr>
          <td><code>'This is his DNA.'.count('is')</code></td>
          <td>3</td>
        </tr>
        <tr>
          <td><code>'This is his DNA.'.count('is', 4)</code></td>
          <td>2</td>
        </tr>
        <tr>
          <td><code>'This is his DNA.'.count('is', 4, 8)</code></td>
          <td>1</td>
        </tr>
      </table>

      <p>
        Here's how to do this ourselves:
      </p>

<pre src="src/funclib/average_with_defaults.py">
def average_list(values, start=0, end=None):
    if end is None:
        end = len(values)
    result = 0.0
    i = start
    while i &lt; end:
        result += values[i]
        i += 1
    return result / (end - start)
</pre>

      <p class="continue">
        If <code>average_list</code> is called with three values,
        they will be assigned to <code>values</code>, <code>start</code>, and <code>end</code>,
        which gives the caller complete control over the function's behavior.
        If it is called with just two parameters,
        then <code>end</code> will have the value <code>None</code>.
        The initial <code>if</code> statement will spot this case
        and re-set <code>end</code> to the length of <code>values</code>
        so that the loop that does the averaging will run correctly.
        And if <code>average_list</code> is called with just one value,
        <code>start</code> will have the value 0,
        which is what we want it to be
        to start the loop with the first element of the list.
        (In this case,
        <code>end</code> will again be <code>None</code>,
        so it will be re-set as before.)
        Here's what our function looks like in action:
      </p>

<pre src="src/funclib/average_with_defaults.py">
numbers = [1.0, 2.0, 5.0]
print '(', numbers, ') =&gt;', average_list(numbers)
print '(', numbers, 1, ') =&gt;', average_list(numbers, 1)
print '(', numbers, 1, 2, ') =&gt;', average_list(numbers, 1, 2)
<span class="out">( [1.0, 2.0, 5.0] ) =&gt; 2.66666666667
( [1.0, 2.0, 5.0] 1 ) =&gt; 3.5
( [1.0, 2.0, 5.0] 1 2 ) =&gt; 2.0</span>
</pre>

      <figure id="f:calls_with_defaults">
        <img src="img/funclib/calls_with_defaults.png" alt="Calls With Defaults" />
      </figure>

      <div class="box">
        <h3>How Older Languages Do It</h3>

        <p>
          If the language we are using doesn't let us define default parameter values,
          we could turn our function into three:
        </p>

<pre src="src/funclib/average_without_defaults.py">
def average_list_range(values, start, end):
    result = 0.0
    i = start
    while i &lt; end:
        result += values[i]
        i += 1
    return result / (end - start)

def average_list_from(values, start):
    return average_list_range(values, start, len(values))

def average_list_all(values):
    return average_list_range(values, 0, len(values))
</pre>

        <p class="continue">
          This is a very common <a href="glossary.html#design-pattern">design pattern</a>
          in many programming languages.
          We start by defining the most general function we can think of&mdash;in
          this case, one that work on a fully-specified range&mdash;and
          then write <a href="glossary.html#wrapper-function">wrapper functions</a>
          as easy-to-use shortcuts for common cases.
          These wrapper functions do <em>not</em> duplicate what's in the general function;
          instead, they call it,
          filling in some or all of the parameters it requires with sensible defaults.
        </p>

        <p>
          The problem with this approach is that
          we have to come up with names for all those little functions.
          Default parameters were invented to solve this problem:
          instead of writing lots of functions,
          we write one,
          and provide default values for some or all of its parameters.
        </p>
      </div>

      <p>
        One restriction on functions with default values
        is that all of the parameters that have default values must come <em>after</em>
        all of the parameters that don't.
        To see why,
        imagine we were allowed to mix defaulting and non-defaulting parameters like this:
      </p>

<pre src="src/funclib/average_with_defaults_wrong.py">
def average_list(<span class="highlight">start=None, values, end=None</span>):
    if start is None:
        start = 0
    if end is None:
        end = len(values)
    result = 0.0
    i = start
    while i &lt; end:
        result += values[i]
        i += 1
    return result / (end - start)
</pre>

      <p>
        If we call the function with just one parameter,
        it's pretty clear that its value has to be assigned to <code>values</code>.
        But what should Python do if the function is called with two parameters,
        like <code>average_list([1.0, 2.0, 5.0], 1)</code>?
        Should it use the provided values for the first and second parameters,
        and the default for the third?
        Or should it use the first parameter's default,
        and assign the given values to the second and third?
        We know what we want,
        but Python doesn't:
        remember, it can't infer anything from variables' names.
        We could define some sort of rule to tell it what to do in this case,
        but it's simpler and safer to disallow the problem in the first place.
        This is why methods like <code>str.count</code> take parameters
        in <a href="#a:string-count">the order they do</a>:
        the more likely a parameter is to be changed,
        the closer to the front of the parameter list it should be.
      </p>

      <p id="p:average-none">
        Now let's go back and figure out what the average of an empty list should be.
        Broadly speaking, there are three possibilities:
      </p>

      <ol>

        <li>
          Return 0.0 or some other number.
        </li>

        <li>
          Return some other value, such as <code>None</code>.
        </li>

        <li>
          Treat this as an error,
          i.e.,
          let the divide-by-zero error happen.
        </li>

      </ol>

      <p>
        Many people pick the first option
        (some even arguing that since zero is the average of all possible numbers,
        it's the only sensible choice).
        The danger of doing this is that it might mask errors in code.
        For example,
        if a file-reading function has a bug in it,
        and returns an empty list instead of a list of numbers,
        we'd really like our program to report an error
        <a href="quality.html#s:defensive">as soon as possible</a>.
        If <code>average_list</code> absorbs an error instead of failing,
        the user may not realize something has gone wrong
        until millions of instructions later,
        which makes debugging harder.
      </p>

      <p>
        The second option&mdash;returning a non-numerical value&mdash;is almost always a worse choice,
        because it complicates the calling code.
        People want to be able to write:
      </p>

<pre>
&hellip;    &hellip;    &hellip;
scaling_factor = average_list(neighbors) / 3.0
center_cell = scaling_factor * center_cell
&hellip;    &hellip;    &hellip;
</pre>

      <p class="continue">
        but if <code>average_list</code> might return <code>None</code>,
        their code will only be safe if they write:
      </p>

<pre>
&hellip;    &hellip;    &hellip;
scaling_factor = average_list(neighbors) / 3.0
if temp is not None:
    center_cell = scaling_factor * center_cell
&hellip;    &hellip;    &hellip;
</pre>

      <p>
        Given what we have seen so far,
        and allowing the divide-by-zero error to occur,
        is actually the safest choice:
        if our program ever does try to calculate the average of an empty list,
        it will fail right away.
        We will see a better way to handle this situation <a href="quality.html#s:except">later</a>.
      </p>

      <div class="keypoints" id="k:args">
        <h3>Summary</h3>
        <ul>
          <li>A function may take any number of arguments.</li>
          <li idea="perf">Define default values for parameters to make functions more convenient to use.</li>
          <li>Defining default values only makes sense when there are sensible defaults.</li>
        </ul>
      </div>

    </section>

    <section id="s:return">

      <h2>Returning Values</h2>

      <div class="understand" id="u:return">
        <h3>Understand:</h3>
        <ul>
          <li>How to return values from a function at any time.</li>
          <li>Why functions shouldn't return values at arbitrary points.</li>
          <li>What a function returns if it doesn't return anything explicitly.</li>
        </ul>
      </div>

      <p>
        All of our functions so far have ended with a <code>return</code> statement,
        and that has been the only <code>return</code> statement they've contained.
        Once again,
        this doesn't have to be the case:
        it is often easier to write functions that return from several places,
        though this can also make them harder to read.
      </p>

      <p>
        Let's start with a function that calculates the sign of a number:
      </p>

<pre src="src/funclib/sign.py">
def sign(num):
    if num &lt; 0:
        return -1
    if num == 0:
        return 0
    return 1
</pre>

      <p class="continue">
        If we call it with a negative number,
        the first branch of the <code>if</code> returns -1.
        If we call it with 0,
        the <code>return</code> in the second <code>if</code> is executed,
        and if we call it with a positive number,
        neither of the <code>if</code> branches is taken,
        so we <a href="glossary.html#fall-through">fall through</a> to the final <code>return</code>,
        which produces the value 1:
      </p>

<pre src="src/funclib/sign.py">
print -5, '=&gt;', sign(-5)
print 0, '=&gt;', sign(0)
print 241, '=&gt;', sign(241)
<span class="out">-5 =&gt; -1
0 =&gt; 0
241 =&gt; 1</span>
</pre>

      <p>
        One common use of multiple return statements
        is to handle special cases at the start of a function.
        For example,
        suppose we decide that we want the average of an empty list to be zero after all.
        We could modify our averaging function to check for this case
        before doing anything else:
      </p>

<pre src="src/funclib/average_empty.py">
def average_list(values):

    <span class="comment"># The average of no values is 0.0.</span>
    if len(values) == 0:
        return 0.0

    <span class="comment"># Handle actual values.</span>
    result = 0.0
    for v in values:
        result += v
    return result / len(values)
</pre>

        <p class="continue">
          The early <code>return</code> statement (plus a comment)
          makes it very clear to whoever is reading this code
          that we are handling an empty list in a special way.
          Compare this to an implementation that uses <code>if</code> and <code>else</code>
          to separate the two cases
          while keeping a single <code>return</code> statement at the end of the function:
        </p>

<pre src="src/funclib/average_empty.py">
def average_list(values):

    <span class="comment"># The average of no values is 0.0.</span>
    if len(values) == 0:
        result = 0.0

    <span class="comment"># Handle actual values.</span>
    else:
        result = 0.0
        for v in values:
            result += v
        result /= len(values)

    <span class="comment"># Return final result.</span>
    return result
</pre>

      <p class="continue">
        This version is easier to understand in one way,
        but harder in another.
        What makes it harder is our limited short-term memory:
        the body of the <code>else</code> is only four lines long,
        but reading and understanding those lines
        may push the special handling of the empty list out of our mind.
        In this case,
        the code is short enough that
        we will probably be able to retain the special case,
        but if the calculation was more complex,
        we would lose sight of the big picture.
      </p>

      <p>
        What makes it easier is its regularity:
        each possible case of input (empty or non-empty) is handled in a conditional branch,
        and each branch's job is to assign a value to <code>result</code>
        for the function to return.
        If there were six or seven special cases,
        this pattern would help us keep track of what what going on&mdash;provided
        we knew (or recognized) the pattern.
      </p>

      <p>
        The psychological term for what's going on here is
        <a href="glossary.html#chunk">chunking</a>,
        which refers to the way people group items together in memory.
        For example, when you look at the five dots on a dice:
      </p>

      <figure id="f:five_spots">
        <img src="img/funclib/five_spots.png" alt="Five Spots" />
      </figure>

      <p class="continue">
        what you actually "see" is the X pattern,
        and what you remember is that pattern rather than five individual dots.
        rather than remembering five individual dots.
        Similarly,
        you remember common words such as "common" as words,
        not as sequences of letters,
        and so on.
      </p>

      <p>
        One of the key differences between experts and novices is that
        experts are better at chunking:
        they don't actually have larger short-term memories,
        but since they recognize a broader repertoire of patterns,
        they are able to manage more information.
        Turning that over,
        the more recognizable patterns are used in a program,
        the easier it is for people to keep it in their heads.
        And as Chase and Simon discuss in their classic paper
        "<a href="bib.html#chase-simon-chess">Perception in chess</a>",
        things that <em>don't</em> conform to patterns can actually be <em>harder</em> for experts to recognize,
        since their brains will mis-match and "correct" what's actually there.
      </p>

      <p>
        Here's a third version of our function that doesn't use an early return.
        and only has one conditional branch:
      </p>

<pre src="src/funclib/average_empty.py">
def average_list(values):
    result = 0.0
    if len(values) &gt; 0:
        for v in values:
            result += v
        result /= len(values)
    return result
</pre>

      <p class="continue">
        Many people find this version harder to understand than either of the previous two,
        even though it is shorter.
        The reason is that the special case isn't handled explicitly.
        Instead,
        this function returns 0 for the empty list
        because of the code that <em>isn't</em> executed:
        if the list is empty,
        the loop doesn't run,
        so the initial value of <code>result</code>
        becomes the function's final value by default.
        Spotting this,
        and keeping track of what the function isn't doing as well as what it is,
        is difficult enough that
        many people won't realize there is a special case at all.
      </p>

      <p>
        One last thing to note about functions in Python is that
        every function returns something:
        if there isn't an explicit <code>return</code> statement,
        the value returned is <code>None</code>.
        For example,
        let's comment out the last line of our sign function:
      </p>

<pre src="src/funclib/sign_commented.py">
def sign(num):
    if num &lt; 0:
        return -1
    if num == 0:
        return 0
<span class="comment">#    return 1</span>

print -5, '=&gt;', sign(-5)
print 0, '=&gt;', sign(0)
print 241, '=&gt;', sign(241)
<span class="out">-5 =&gt; -1
0 =&gt; 0
241 =&gt; None</span>
</pre>

      <p class="continue">
        The sign of 241 is now <code>None</code> instead of 1,
        because when the function is called with a positive value,
        neither of the <code>if</code> branches is taken,
        and execution "falls off" the end of the function.
      </p>

      <p>
        Other languages do this differently.
        In C,
        for example,
        trying to use the "result" of a function that doesn't explicitly return something
        is a compilation error&mdash;the program can't even be run.
        No matter what the language,
        this is one reason why commenting out blocks of code is a bad idea:
        it's all too easy to accidentally disable a <code>return</code> statement
        buried inside the code that's no longer being executed.
      </p>

      <div class="keypoints" id="k:return">
        <h3>Summary</h3>
        <ul>
          <li>A function may return values at any point.</li>
          <li>A function should have zero or more <code>return</code> statements at its start to handle special cases, and then one at the end to handle the general case.</li>
          <li>"Accidentally" correct behavior is hard to understand.</li>
          <li>If a function ends without an explicit <code>return</code>, it returns <code>None</code>.</li>
        </ul>
      </div>

    </section>

    <section id="s:aliasing">

      <h2>Aliasing</h2>

      <div class="understand" id="u:aliasing">
        <h3>Understand:</h3>
        <ul>
          <li>How and when aliasing will occur during function calls.</li>
        </ul>
      </div>

      <p>
        We said <a href="#a:call-stack">earlier</a> that
        values are copied into parameters whenever a function is called.
        But as we explained in the <a href="python.html#s:alias">previous chapter</a>,
        variables don't actually store values:
        they are actually just names that refer to values.
        To see what this means for our programs,
        here's a function that takes a string and a list as parameters,
        and appends something to both:
      </p>

<pre src="src/funclib/appender.py">
def appender(a_string, a_list):
    a_string = a_string + 'turing'
    a_list.append('turing')
</pre>

      <p class="continue">
        And here is some code to set up a pair of variables and call that function:
      </p>

<pre src="src/funclib/appender.py">
string_val = 'alan'
list_val = ['alan']
appender(string_val, list_val)
print 'string', string_val
print 'list', list_val
<span class="out">string alan
list ['alan', 'turing']</span>
</pre>

      <p>
        Why did the list change when the string didn't?
        To find out,
        let's trace the function's execution.
        Just before the call,
        the global frame has two variables
        that refer to a string and a list:
      </p>

      <figure id="f:append_before_call">
        <img src="img/funclib/append_before_call.png" alt="Before Appending" />
      </figure>

      <p class="continue">
        The call creates a new stack frame with aliases for those values:
      </p>

      <figure id="f:append_during_call">
        <img src="img/funclib/append_during_call.png" alt="While Appending" />
      </figure>

      <p>
        The <code>a_string&nbsp;+&nbsp;'turing'</code> creates a new string <code>'alanturing'</code>;
        assigning this to the variable <code>a_string</code>
        changes what that local variable refers to,
        but doesn't change what the global variable <code>string_val</code> refers to:
      </p>

      <figure id="f:append_new_string">
        <img src="img/funclib/append_new_string.png" alt="A New String" />
      </figure>

      <p>
        The statement <code>a_list.append('turing')</code>,
        however,
        actually modifies the list that <code>a_list</code> is pointing to:
      </p>

      <figure id="f:append_same_list">
        <img src="img/funclib/append_same_list.png" alt="But the Same List" />
      </figure>

      <p>
        But this is the same thing that the variable <code>list_val</code> in the caller is pointing to.
        When the function returns and the call frame is thrown away,
        the new string <code>'alanturing'</code> is therefore lost,
        because the only reference to it was in the function call's stack frame.
        The change to the list,
        on the other hand,
        is kept,
        because the function actually modified the list in place:
      </p>

      <figure id="f:append_final_state">
        <img src="img/funclib/append_final_state.png" alt="The Final State of Memory" />
      </figure>

      <p>
        Let's change one line in the function:
      </p>

<pre src="src/funclib/appender_2.py">
def appender(a_string, a_list):
    a_string = a_string + 'turing'
    <span class="highlight">a_list = a_list + ['turing']</span>
</pre>

      <p class="continue">
        and see what happens when we run the same experiment:
      </p>

<pre src="src/funclib/appender_2.py">
string_val = 'alan'
list_val = ['alan']
appender(string_val, list_val)
print 'string', string_val
print 'list', list_val
<span class="out">string alan
list ['alan']</span>
</pre>

      <p>
        The answer is different because
        concatenating (adding) two lists creates a new list,
        rather than modifying either of the lists being concatenated.
        As a result,
        the local variable <code>a_list</code> is the only thing that refers to the list
        <code>['alan', 'turing']</code>,
        so that value is discarded when the function finishes
        and <code>list_val</code>'s value is undisturbed.
      </p>

      <div class="box">
        <h3>Memory Models</h3>

        <p>
          Python's treatment of lists
          (and other mutable data that we'll see <a href="setdict.html">later</a>)
          isn't the only way to handle things.
          For example,
          MATLAB functions
          use a rule called <a href="glossary.html#copy-on-write">copy on write</a>.
          Initially,
          it creates aliases for arrays that are passed into functions.
          The first time a function assigns to an array,
          though,
          MATLAB clones the array
          and changes the clone rather than the original
          (<a href="#f:copy_on_write">Figure XXX</a>).
          This saves it from copying data when it doesn't need to,
          while guaranteeing that functions don't have side effects
          (which makes them easier to think about).
        </p>

        <figure id="f:copy_on_write">
          <img src="img/funclib/copy_on_write.png" alt="Copy on Write" />
        </figure>

        <p>
          Other languages have slightly different rules about scoping and aliasing.
          Together,
          those rules make up the language's
          <a href="glossary.html#memory-model">memory model</a>.
          Understanding that model is perhaps the most important step
          in understanding how programs written in the language actually work,
          and more importantly,
          how to debug them when they don't.
        </p>
      </div>

      <div class="keypoints" id="k:aliasing">
        <h3>Summary</h3>
        <ul>
          <li>Values are actually passed into functions by reference, which means that they are aliased.</li>
          <li>Aliasing means that changes made to a mutable object like a list inside a function are visible after the function call completes.</li>
        </ul>
      </div>

    </section>

    <section id="s:libraries">

      <h2>Libraries</h2>

      <div class="understand" id="u:libraries">
        <h3>Understand:</h3>
        <ul>
          <li>How to import code in one Python module for use in another.</li>
          <li>That code is executed as it's imported.</li>
          <li>That each module corresponds to a variable scope.</li>
        </ul>
      </div>

      <p>
        A function is a way to turn a bunch of related statements into a single chunk that can be re-used.
        A <a href="glossary.html#module">module</a>
        or <a href="glossary.html#library">library</a>
        (for our purposes, the terms mean the same thing)
        does for functions what functions do for statements:
        group them together to create more usable chunks.
        This hierarchical organization is similar in spirit to that used in biology:
        instead of family, genus, and species, we have module, function, and statement.
      </p>

      <p>
        Every Python file can be used as a module by other programs.
        <span class="fixme">import has already been introduced</span>
        To load a module into a program,
        we use the <code>import</code> statement.
        For example,
        suppose we have created a Python file called <code>halman.py</code>
        that defines a single function called <code>threshold</code>:
      </p>

<pre src="src/funclib/halman.py">
<span class="comment"># halman.py</span>
def threshold(signal):
  return 1.0 / sum(signal)
</pre>

      <p class="continue">
        If we want to call this function in a program stored in another file,
        we use <code>import halman</code> to load the contents of <code>halman.py</code>,
        and then call the function as <code>halman.threshold</code>:
      </p>

<pre src="src/funclib/use_halman.py">
import halman
readings = [0.1, 0.4, 0.2]
print 'signal threshold is', halman.threshold(readings)
</pre>

      <p class="continue">
        We can then run the program that does the <code>import</code>
        and calls the function:
      </p>

<pre>
$ <span class="in">python use_halman.py</span>
<span class="out">signal threshold is 1.42857</span>
</pre>

      <p>
        When a module is imported,
        Python executes the statements it contains
        (which are usually function definitions).
        It then creates an object to store references to all the items defined in that module
        and assigns it to a variable with the same name as the module.
        For example,
        let's create a file called <code>noisy.py</code> that prints out a message
        and then defines <code>NOISE_LEVEL</code> to be 1/3:
      </p>

<pre src="src/funclib/noisy.py">
<span class="comment"># noisy.py</span>
print 'Is this module being loaded?'
NOISE_LEVEL = 1./3.
</pre>

      <p class="continue">
        When it imports <code>noisy</code>
        Python executes the first statement&mdash;the <code>print</code>&mdash;and
        displays a message on the screen:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">import noisy</span>
<span class="out">Is this module being loaded?</span>
</pre>

      <p class="continue">
        Importing the module also defines the variable <code>NOISE_LEVEL</code>.
        Inside the main program,
        we can access as <code>noisy.NOISE_LEVEL</code>:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">print noisy.NOISE_LEVEL</span>
<span class="out">0.33333333</span>
</pre>

      <p>
        Just like a function,
        each module is a separate scope,
        so that variable names defined inside a module belong to that module
        and don't collide with variable names defined elsewhere.
        When a function wants to a find a variable,
        it actually looks in its own scope,
        then in its module.
        Our earlier rule "function then global" is just a special case of this,
        since the global scope is just the module scope of our main program.
      </p>

      <figure id="f:name_resolution">
        <img src="img/funclib/name_resolution.png" alt="Name Resolution" />
      </figure>

      <p>
        To see how this works,
        let's create a file called <code>module.py</code>
        that defines both a variable called <code>NAME</code>
        and a function called <code>func</code> that prints it out:
      </p>

<pre src="src/funclib/module.py">
<span class="comment"># module.py</span>
NAME = 'Transylvania'

def func(arg):
  return NAME + ' ' + arg
</pre>

      <p class="continue">
        In our main program,
        we also define a variable called <code>NAME</code>,
        then import our module.
        When we call <code>module.func</code>
        it sees the <code>NAME</code> variable that was defined inside the module,
        not the one that was defined globally:
      </p>

<pre src="src/funclib/use_module.py">
&gt;&gt;&gt; <span class="in">NAME = 'Hamunaptra'</span>
&gt;&gt;&gt; <span class="in">import module</span>
&gt;&gt;&gt; <span class="in">print module.func('!!!')</span>
<span class="out">Transylvania !!!</span>
</pre>

      <p>
        Once again,
        rules about where and how to look things up might seem arcane,
        but it would be practically impossible to write large programs
        without some kind of scoping them.
        Restricting lookup to the current function,
        its module,
        and the top level of the program makes it easier for people to understand code,
        since there are only three places where the variables used on a particular line might be,
        two of which (the containing function and the file it's in)
        are guaranteed to be nearby.
      </p>

      <div class="box">
        <h3>How Other Languages Do It</h3>

        <p>
          When a dynamic language like Python (or MATLAB, R, Ruby, or Perl) loads a program,
          it actually does two things:
        </p>

        <ol>
          <li>
            translate the statements into instructions the computer can execute,
            and
          </li>
          <li>
            execute those instructions.
          </li>
        </ol>

        <p>
          Compiled languages like Fortran, C++, and Java do these things separately:
          a <a href="glossary.html#compiler">compiler</a> does the translation,
          saving the instructions in a file on disk,
          which a separate <a href="glossary.html#loader">loader</a>
          copies into memory for execution some time later
          (<a href="#f:compiling_vs_interpreting">Figure XXX</a>).
          In general,
          compiled languages therefore don't execute instructions while loading;
          instead,
          they wait until everything is in memory before running any of it.
        </p>

        <figure id="f:compiling_vs_interpreting">
          <img src="img/funclib/compiling_vs_interpreting.png" alt="Compiling vs. Interpreting" />
        </figure>

      </div>

      <div class="keypoints" id="k:libraries">
        <h3>Summary</h3>
        <ul>
          <li idea="turing">Any Python file can be imported as a library.</li>
          <li>The code in a file is executed when it is imported.</li>
          <li>Every Python file is a scope, just like every function.</li>
        </ul>
      </div>

    </section>

    <section id="s:stdlib">

      <h2>Standard Libraries</h2>

      <div class="understand" id="u:stdlib">
        <h3>Understand:</h3>
        <ul>
          <li>What is in the standard math library.</li>
          <li>What is in the system library.</li>
          <li>Several ways to import things from libraries.</li>
        </ul>
      </div>

      <p>
        The real power of a language is in its libraries:
        they are the distilled wisdom and effort
        of all the programmers who have come before us.
        Python's standard library contains over a hundred modules,
        and the fastest way to become a more productive programmer
        is to become familiar with them.
        One of the most useful is <code>math</code>,
        which defines <code>sqrt</code> for square roots,
        <code>hypot</code> for calculating x<sup>2</sup>+y<sup>2</sup>,
        and values for <em>e</em> and &pi; that are as accurate as the machine can make them.
      </p>

<pre>
&gt;&gt;&gt; <span class="in">import math</span>
&gt;&gt;&gt; <span class="in">print math.sqrt(2)</span>
<span class="out">1.4142135623730951</span>
&gt;&gt;&gt; <span class="in">print math.hypot(2, 3)</span>  <span class="comment"># sqrt(x**2 + y**2)</span>
<span class="out">3.6055512754639891</span>
&gt;&gt;&gt; <span class="in">print math.e, math.pi</span>   <span class="comment"># as accurate as possible</span>
<span class="out">2.7182818284590451 3.1415926535897931</span>
</pre>

      <p>
        Since <code>math.sqrt</code> is a handful to type,
        and <code>sqrt</code> is probably not ambiguous,
        Python provides several ways to import things.
        For example,
        we can import specific functions from a library and then call them directly,
        rather than using the <code>modulename.functionname</code> syntax:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">from math import sqrt</span>
&gt;&gt;&gt; <span class="in">sqrt(3)</span>
<span class="out">1.7320508075688772</span>
</pre>

      <p class="continue">
        We can also import a function under a different name,
        so that if two modules define functions with the same name,
        we can give one or the other a different name when we want to use them together:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">from math import hypot as euclid</span>
&gt;&gt;&gt; <span class="in">euclid(3, 4)</span>
<span class="out">5.0</span>
</pre>

      <p>
        We can also use <code>import *</code>
        to bring everything in the module into the current scope at once.
        This has the same effect as using <code>from module import a</code>,
        <code>from module import b</code>,
        and so on for every name in the module:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">from math import *</span>
&gt;&gt;&gt; <span class="in">sin(pi)</span>
<span class="out">1.2246063538223773e-16</span>
</pre>

      <p class="continue">
        <code>import *</code> is usually a bad idea:
        if someone adds a new function or variable to the next version of the module,
        your <code>import *</code> could silently overwrite something that you have written,
        or are importing from somewhere else.
        Bugs like this can be extremely hard to find,
        since nothing seemed to change in your program.
      </p>

      <p>
        Another useful library is <code>sys</code> (short for "system").
        It defines constants to tell us what version of Python we're using,
        what operating system we're running on,
        and how large integers are:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">import sys</span>
&gt;&gt;&gt; <span class="in">print sys.version</span>
<span class="out">2.7 (r27:82525, Jul  4 2010, 09:01:59) [MSC v.1500 32 bit (Intel)]</span>
&gt;&gt;&gt; <span class="in">print sys.platform</span>
<span class="out">win32</span>
&gt;&gt;&gt; <span class="in">print sys.maxint</span>
<span class="out">2147483647</span>
&gt;&gt;&gt; <span class="in">print sys.path</span>
<span class="out">['',
 'C:\\WINDOWS\\system32\\python27.zip',
 'C:\\Python27\\DLLs', 'C:\\Python27\\lib',
 'C:\\Python27\\lib\\plat-win',
 'C:\\Python27', 'C:\\Python27\\lib\\site-packages']</span>
</pre>

      <p>
        The most commonly-used element of <code>sys</code>, though, is <code>sys.argv</code>,
        which holds a list of the <a href="glossary.html#command-line-arguments">command-line arguments</a>
        used to run the program.
        The name of the script itself is in <code>sys.argv[0]</code>;
        all the other arguments are put in <code>sys.argv[1]</code>, <code>sys.argv[2]</code>, and so on.
        For example, here's a program that does nothing except print out its command-line arguments:
      </p>

<pre src="src/funclib/echo.py">
<span class="comment"># echo.py</span>
import sys
for i in range(len(sys.argv)):
  print i, '"' + sys.argv[i] + '"'
</pre>

      <p class="continue">
        If it is run without any arguments,
        it reports that <code>sys.argv[0]</code> is <code>echo.py</code>:
      </p>

<pre>
$ <span class="in">python echo.py</span>
<span class="out">0 echo.py</span>
</pre>

      <p class="continue">
        When it is run with arguments, though, it displays those as well:
      </p>

<pre>
$ <span class="in">python echo.py first second</span>
<span class="out">0 echo.py</span>
<span class="out">1 first</span>
<span class="out">2 second</span>
</pre>

      <p>
        We can use this to write command-line tools like a simple calculator:
      </p>

<pre src="src/funclib/calculator.py">
import sys

total = 0
for value in sys.argv[1:]:
    total += float(value)
print total
$ <span class="in">python calculator.py 1 2 3</span>
<span class="out">6.0</span>
</pre>

      <p class="continue">
        Notice that we loop over <code>sys.argv[1:]</code>,
        i.e.,
        over everything except the first element of <code>sys.argv</code>.
        That first element is always the name of our program
        (in this case, <code>calculator.py</code>),
        which we definitely don't want to try to add to our running total.
      </p>

      <p>
        A more common use of <code>sys.argv</code> is
        to pass the names of a bunch of files into our program.
        Suppose,
        for example,
        that we have a function called <code>summarize</code>
        that opens a file,
        reads the values in it,
        and returns the minimum, average, and maximum:
      </p>

<pre src="summarize.py">
def summarize(filename):
    reader = open(filename, 'r')
    least, greatest, total, count = 0.0, 0.0, 0.0
    for line in reader:
        current = float(line)
        least = min(least, current)
        greatest = max(least, current)
        total += current
        count += 1
    reader.close()
    return least, total / count, greatest
</pre>

      <p class="continue">
        If we want to display summaries for several files at once,
        we can require the user to give them as command-line arguments:
      </p>

<pre>
$ python summarize.py july.dat august.dat september.dat
</pre>

      <p class="continue">
        and connect the command line with the program's internals using <code>sys.argv</code>:
      </p>

<pre src="summarize.py">
all_filenames = sys.argv[1:]  <span class="comment"># Again, don't include the program name</span>
for filename in all_filenames:
    low, ave, high = summarize(filename)
    print filename, low, ave, high
</pre>

      <div class="keypoints" id="k:stdlib">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>from <em>library</em> import <em>something</em></code> to import something under its own name.</li>
          <li>Use <code>from <em>library</em> import <em>something</em> as <em>alias</em></code> to import something under the name <code><em>alias</em></code>.</li>
          <li><code>from <em>library</em> import *</code> imports everything in <code><em>library</em></code> under its own name, which is usually a bad idea.</li>
          <li>The <code>math</code> library defines common mathematical constants and functions.</li>
          <li>The system library <code>sys</code> defines constants and functions used in the interpreter itself.</li>
          <li><code>sys.argv</code> is a list of all the command-line arguments used to run the program.</li>
          <li><code>sys.argv[0]</code> is the program's name.</li>
          <li><code>sys.argv[1:]</code> is everything except the program's name.</li>
        </ul>
      </div>

    </section>

    <section id="s:filter">

      <h2>Building Filters</h2>

      <div class="understand" id="u:filter">
        <h3>Understand:</h3>
        <ul>
          <li>How to build a program that behaves like a Unix filter.</li>
          <li>How to decide what should be done in a function and what should be done by its caller.</li>
          <li>How to get help interactively.</li>
          <li>How to provide interactive help.</li>
          <li>How a file can tell if it's being used as the main program or being loaded as a library.</li>
        </ul>
      </div>

      <p>
        As well as creating a list of a program's command-line arguments,
        <code>sys</code> also connects the program to standard input,
        standard output,
        and standard error
        (which were introduced in the chapter on <a href="shell.html#s:pipefilter">the Unix shell</a>).
        Here's a typical example of how these variables are used together:
      </p>

<pre src="src/funclib/count.py">
import sys

def count_lines(reader):
    result = 0
    for line in reader:
        result += 1
    return result

if len(sys.argv) == 1:
    count_lines(sys.stdin)
else:
    for filename in sys.argv[1:]:
        rd = open(filename, 'r')
        count_lines(rd)
        rd.close()
</pre>

      <p class="continue">
        This program looks at <code>sys.argv</code> to see if it was called with any filenames as arguments or not.
        If there were no arguments,
        then <code>sys.argv</code> will only hold the name of the program,
        and its length will be 1.
        In that case, the program reads data from standard input:
      </p>

<pre>
$ <span class="in">python count.py &lt; a.txt</span>
<span class="out">48</span>
</pre>

      <p class="continue">
        Otherwise,
        the program assumes its command-line arguments are the names of files.
        It opens each one in turn,
        counts how many lines are in it,
        and then closes it:
      </p>

<pre>
$ <span class="in">python count.py a.txt b.txt</span>
<span class="out">48
227</span>
</pre>

      <div class="box">
        <h3>Who Opens?</h3>

        <p>
          There's a subtle but important difference between <code>count_lines</code>
          and the <code>summarize</code> function we wrote earlier.
          <code>summarize</code> expects a filename as its sole parameter,
          and opens and closes that file itself.
          <code>count_lines</code>,
          on the other hand,
          expects to be given a handle to an already-open file,
          i.e.,
          it expects whoever is calling it to take care of the opening and closing.
        </p>

        <p>
          Why the difference?
          Because we want to use the same <code>count_lines</code> function
          for both the files whose names we're given on the command line,
          and for <code>sys.stdin</code>.
          Putting it another way,
          we can't call <code>open</code> with <code>sys.stdin</code> as a parameter&mdash;it's
          already an open file, not a string&mdash;so
          we have to do our opening before we call the function.
        </p>

        <p>
          We <em>could</em> push responsibility for opening down into the function if we really wanted to,
          so that our main program was just:
        </p>

<pre src="src/funclib/count_2.py">
if len(sys.argv) == 1:
    count_lines(sys.stdin)
else:
    for filename in sys.argv[1:]:
        count(filename)
</pre>

        <p class="continue">
          If we do this,
          though,
          the function has to check whether its parameter is a string
          (which we interpret to mean "the name of a file")
          or something else
          (which we hope is an open file we can read from).
          We have to do the same check at the end of the function as well
          to close the file if we opened it:
        </p>

<pre src="src/funclib/count_2.py">
def count_lines(source):
<span class="highlight">    if type(source) == str:
        reader = open(source, 'r')</span>
    result = 0
    for line in reader:
        result += 1
<span class="highlight">    if type(source) == str:
        reader.close()</span>
    return result
</pre>

        <p class="continue">
          Most people find the original easier to understand,
          since it does a better job of separating
          the calculation from the file management.
        </p>

      </div>

      <p>
        Let's go back to our original program
        and write it a little more politely:
      </p>

<pre src="src/polite_count.py">
'''Count lines in files.  If no filename arguments given,
read from standard input.'''

import sys

def count_lines(reader):
  '''Return number of lines in text read from reader.'''
  return len(reader.readlines())

if __name__ == '__main__':
  if len(sys.argv) == 1:
    print count_lines(sys.stdin)
  else:
    r = open(sys.argv[1], 'r')
    print count_lines(r)
    r.close()
</pre>

      <p class="continue">
        The two significant changes are
        the strings at the start of the module and of the function <code>count_lines</code>,
        and the funny-looking line that compares <code>__name__</code> to <code>'__main__'</code>.
        Let's look at them in that order.
      </p>

      <p>
        To help us find our way around libraries,
        Python provides a <code>help</code> function.
        If <code>math</code> has been imported,
        the call <code>help(math)</code> prints out the documentation embedded in the math library:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">import math</span>
&gt;&gt;&gt; <span class="in">help(math)</span>
<span class="out">Help on module math:
NAME
    math
FILE
    /usr/lib/python2.5/lib-dynload/math.so
MODULE DOCS
    http://www.python.org/doc/current/lib/module-math.html
DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.
FUNCTIONS
    acos(...)
        acos(x)
        Return the arc cosine (measured in radians) of x.
    &hellip;        &hellip;        &hellip;</span>
</pre>

      <p>
        Here's how this works.
        If the first thing in a module or function other than blank lines or comments is a string,
        and that string isn't assigned to a variable,
        Python saves it as the documentation string,
        or <a href="glossary.html#docstring">docstring</a>,
        for that module or function.
        These docstrings are what online (and offline) help display.
        For example,
        let's create a file <code>adder.py</code> with a single function <code>add</code>,
        and write docstrings for both the module and the function:
      </p>

<pre src="src/funclib/adder.py">
<span class="comment"># adder.py</span>
'''Addition utilities.'''

def add(a, b):
  '''Add arguments.'''
  return a+b
</pre>

      <p class="continue">
        If we import <code>adder</code>,
        <code>help(adder)</code> prints out all of its docstrings,
        i.e., the documentation for the module itself and for all of its functions:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">import adder</span>
&gt;&gt;&gt; <span class="in">help(adder)</span>
<span class="out">NAME
    adder - Addition utilities.
FUNCTIONS
    add(a, b)
        Add arguments.</span>
</pre>

      <p class="continue">
        We can also be more selective,
        and only display the help for a particular function instead:
      </p>

<pre>
&gt;&gt;&gt; help(adder.add)
<span class="out">add(a, b)
       Add arguments.</span>
</pre>

      <p>
        The second part of our more polite program was that odd-looking <code>if</code> statement.
        It depends on a trick to do something useful,
        and that trick needs a bit of explaining.
        When Python reads in a file,
        it assigns a value to a special variable called <code>__name__</code>
        (with two underscores before and after).
        If the file is being run as the main program,
        <code>__name__</code> is assigned the string <code>'__main__'</code>
        (again with two underscores before and after).
        If the file is being loaded as a module by some other program,
        though,
        Python assigns the module's name to <code>__name__</code> instead.
        To show this in action,
        let's create a Python file called <code>my_name.py</code>
        that does nothing but print out the value of <code>__main__</code>:
      </p>

<pre src="my_name.py">
print __name__
</pre>

      <p class="continue">
        If we run it directly from the command line,
        it tells us that <code>__name__</code> has the value <code>'__main__'</code>:
      </p>

<pre>
$ <span class="in">python my_name.py</span>
<span class="out">__name__</span>
</pre>

      <p class="continue">
        If we import this file into an interactive Python session,
        though,
        what's printed out during the import is different:
      </p>

<pre>
$ <span class="in">python</span>
&gt;&gt;&gt; <span class="in">import my_name</span>
<span class="out">my_name</span>
</pre>

      <p class="continue">
        We get the same behavior if we import <code>my_name</code> into another program:
      </p>

<pre>
$ <span class="in">cat test_import.py</span>
<span class="out">import my_name</span>
$ <span class="in">python test_import.py</span>
<span class="out">my_name</span>
</pre>

      <p>
        Now,
        suppose that a file contains the conditional statement
        <code>if __name__ == '__main__'</code>.
        The code inside the <code>if</code> will only run if the file is the main program,
        because that's the only situation in which <code>__name__</code> will be <code>'__main__'</code>.
        Put another way,
        the statements inside the conditional will <em>not</em> be run
        if the file is being loaded as a library by some other program.
        This makes it easy to write modules
        that can be used as both programs in their own right,
        and as libraries by other pieces of code.
      </p>

      <p>
        For example,
        the file <code>stats.py</code> defines a function <code>average</code>,
        and then runs three simple tests&mdash;but
        only if <code>__name__</code> has the value <code>'__main__'</code>:
      </p>

<pre src="src/stats.py">
# stats.py
'''Useful statistical tools.'''

def average(values):
  '''Return average of values or None if no data.'''
  if values:
    return sum(values) / len(values)
  else:
    return None

if __name__ == '__main__':
  print 'test 1 should be None:', average([])
  print 'test 2 should be 1:', average([1])
  print 'test 3 should be 2:', average([1, 2, 3])
</pre>

      <p class="continue">
        If we import this file into an interactive session,
        it doesn't produce any output,
        because <code>stats.__name__</code> has been assigned the value <code>'stats'</code>:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">import stats</span>
&gt;&gt;&gt; <span class="in">print stats.__name__</span>
<span class="out">stats</span>
</pre>

      <p class="continue">
        If we run this file directly, though,
        that same <code>__name__</code> variable will be assigned the value <code>'__main__'</code>,
        so the test <em>will</em> be run:
      </p>

<pre>
$ <span class="in">python stats.py</span>
<span class="out">test 1 should be None: None
test 2 should be 1: 1
test 3 should be 2: 2</span>
</pre>

      <p class="continue">
        This is another common design pattern in Python:
        group related functions into a module,
        then put some tests for those functions in the same module
        under <code>if __name__ == '__main__'</code>,
        so that if the module is run as the main program,
        it will check itself.
      </p>

      <div class="box">
        <h3>How Other Languages Do It</h3>

        <p>          
          The <code>__name__ == 'main'</code> idiom is
          one of the few things that Python got wrong:
          it's economical,
          in that it doesn't introduce any special-purpose machinery that doesn't have to be there anyway,
          but novices have to master several difficult concepts
          before they can understand how it works.
        </p>

        <p>
          Other languages handle the "where do I start?" problem differently.
          C,
          for example,
          expects programs to have a function called <code>main</code>,
          which is automatically invoked to start the program running.
        </p>

      </div>

      <div class="keypoints" id="k:filter">
        <h3>Summary</h3>
        <ul>
          <li>If a program isn't told what files to process, it should process standard input.</li>
          <li idea="paranoia">Programs that explicitly test values' types are more brittle than ones that rely on those values' common properties.</li>
          <li>The variable <code>__name__</code> is assigned the string <code>'__main__'</code> in a module when that module is the main program, and the module's name when it is imported by something else.</li>
          <li>If the first thing in a module or function is a string that isn't assigned to a variable, that string is used as the module or function's documentation.</li>
          <li>Use <code>help(<em>name</em>)</code> to display the documentation for something.</li>
        </ul>
      </div>

    </section>

    <section id="s:funcobj">

      <h2>Functions as Objects</h2>

      <div class="understand" id="u:funcobj">
        <h3>Understand:</h3>
        <ul>
          <li>That a function is just another kind of data.</li>
          <li>How to create an alias for a function.</li>
          <li>How to pass a function to another function.</li>
          <li>How to store a reference to a function in a list.</li>
          <li>How to use higher-level functions to eliminate redundancy in programs.</li>
        </ul>
      </div>

      <p>
        An integer is just 32 or 64 bits of data that a variable can refer to,
        while a string is just a sequence of bytes that a variable can also refer to.
        Functions are just more bytes in memory&mdash;ones that happen to represent instructions.
        That means that variables can refer to them
        just as they can refer to any other data.
      </p>

      <p>
        This insight&mdash;the fact that code is just another kind of data,
        and can be manipulated like integers or strings&mdash;is
        one of the most useful and powerful in all computing.
        To understand why,
        let's have a closer look at what actually happens when we define a function:
      </p>

<pre src="src/funclib/threshold.py">
def threshold(signal):
    return 1.0 / sum(signal)
</pre>

      <p class="continue">
        These two lines tell Python that <code>threshold</code> is
        a function that returns one over the sum of the values in <code>signal</code>.
        When we define it,
        Python translates the statements in the function into a blob of bytes,
        then creates a variable called <code>threshold</code> and makes it point at that blob:
      </p>

      <figure id="f:defining_function">
        <img src="img/funclib/defining_function.png" alt="Defining a Function" />
      </figure>

      <p class="continue">
        This is not really any different from assigning the string <code>'alan turing'</code>
        to the variable <code>name</code>.
        the only difference is what's in the memory the variable points to.
      </p>

      <p>
        If <code>threshold</code> is just a reference to something in memory,
        we should be able to assign that reference to another variable.
        Sure enough,
        we can,
        and when we call the function via that newly-created alias,
        the result is exactly what we would get
        if we called the original function with the same parameters,
        because there's really only one function&mdash;it just has two names:
      </p>

<pre src="src/funclib/threshold.py">
data = [0.1, 0.4, 0.2]
print threshold(data)
<span class="out">1.42857</span>
t = threshold
print t(data)
<span class="out">1.42857</span>
</pre>

      <figure id="f:aliasing_function">
        <img src="img/funclib/aliasing_function.png" alt="Aliasing a Function" />
      </figure>

      <div class="box">
        <h3>Aliasing and Importing</h3>

        <p>
          We have created aliases for functions before without realizing it.
          When we execute <code>from math import sqrt as square_root</code>,
          we are loading the <code>math</code> module,
          then creating an alias called <code>square_root</code>
          for its function <code>sqrt</code>.
        </p>
      </div>

      <p>
        If a function is just another kind of data,
        and we can create an alias for it,
        can we put it in a list?
        More precisely,
        can we put a reference to a function in a list?
        Let's define two functions,
        <code>area</code> and <code>circumference</code>,
        each of which takes a circle's radius as a parameter and returns the appropriate value:
      </p>

<pre src="src/funclib/funclist.py">
def area(r):
    return pi * r * r

def circumference(r):
    return 2 * pi * r
</pre>

      <p class="continue">
        Once those functions are defined, we can put them into a list
        (more precisely, put references to them in a list):
      </p>

<pre src="src/funclib/funclist.py">
funcs = [area, circumference]
</pre>

      <figure id="f:list_of_functions">
        <img src="img/funclib/list_of_functions.png" alt="A List of Functions" />
      </figure>

      <p>
        We can now loop through the functions in the list,
        calling each in turn.
        Sure enough,
        the output is what we would get if we called <code>area</code>
        and then <code>circumference</code>:
      </p>

<pre src="src/funclib/funclist.py">
for f in funcs:
    print f(1.0)
<span class="out">3.14159
6.28318</span>
</pre>

      <p>
        Let's go a little further.
        Instead of storing a reference to a function in a list,
        let's pass that reference into another function,
        just as we would pass a reference to an integer, a string, or a list.
        Here's a function called <code>call_it</code> that takes two parameters:
        a reference to some other function, and some other value.
      </p>

<pre src="src/funclib/passfunc.py">
def call_it(func, value):
    return func(value)
</pre>

      <p class="continue">
        All <code>call_it</code> does is call that other function with the given value as a parameter:
      </p>

<pre src="src/funclib/passfunc.py">
print call_it(area, 1.0)
<span class="out">3.14159</span>

print call_it(circumference, 1.0)
<span class="out">6.28318</span>
</pre>

      <p>
        Now it's time for the payoff.
        Here's a function called <code>do_all</code>
        that applies a function&mdash;anything at all that takes one argument&mdash;to
        each value in a list,
        and returns a list of the results:
      </p>

<pre src="src/funclib/doall.py">
def do_all(func, values):
    result = []
    for v in values:
        temp = func(v)
        result.append(temp)
    return result
</pre>

      <p>
        If we call <code>do_all</code> with <code>area</code> and a list of numbers,
        we get what we would get if we called <code>area</code> directly on each number in turn:
      </p>

<pre src="src/funclib/doall.py">
print do_all(area, [1.0, 2.0, 3.0])
<span class="out">[3.14159, 12.56636, 28.27431]</span>
</pre>

      <p class="continue">
        And if we define a function to "slim down" strings of text
        by throwing away their first and last characters,
        we can apply it to every string in a list,
        without having to write another copy of the code that loops through the list,
        calls the function,
        and concatenates the results:
      </p>

<pre src="src/funclib/doall.py">
def slim(text):
    return text[1:-1]

print do_all(slim, ['abc', 'defgh'])
<span class="out">b efg</span>
</pre>

      <p>
        Functions that operate on other functions are called
        <a href="glossary.html#higher-order-functions">higher-order functions</a>.
        They're common in mathematics:
        integration,
        for example,
        is a function that operates on some other function.
        In programming,
        higher-order functions allow us to mix and match pieces of code
        rather than duplicating them.
      </p>

      <p>
        As another example,
        let's look at <code>combine_values</code>,
        which takes a function and a list of values as parameters,
        and combines the values in the list using the function provided:
      </p>

<pre src="src/funclib/combine.py">
def combine_values(func, values):
    current = values[0]
    for i in range(1, len(values)):
        current = func(current, values[i])
    return current
</pre>

      <p class="continue">
        Now let's define <code>add</code> and <code>mul</code> to add and multiply values:
      </p>

<pre src="src/funclib/combine.py">
def add(x, y):
    return x + y

def mul(x, y):
    return x * y
</pre>

      <p class="continue">
        If we combine 1, 3, and 5 with <code>add</code>, we get their sum, 9:
      </p>

<pre src="src/funclib/combine.py">
print combine_values(add, [1, 3, 5])
<span class="out">9</span>
</pre>

      <p class="continue">
        If we combine the same values with <code>mul</code>, we get their product, 15:
      </p>

<pre src="src/funclib/combine.py">
print combine_values(mul, [1, 3, 5])
<span class="out">15</span>
</pre>

      <p class="continue">
        This same higher-order function <code>combine_values</code> could concatenate lists of strings, too,
        or multiply several matrices together, or whatever else we wanted,
        without us having to write or test the loop ever again.
        Without higher-order functions,
        we would have to  write one function for each combination of data structure and operation,
        i.e.,
        one function to add numbers,
        another to concatenate strings,
        a third to sum matrices,
        and so on.
        <em>With</em> higher-order functions,
        on the other hand,
        we only write one function for each basic operation,
        and one function for each kind of data structure.
        Since A plus B is usually a lot smaller than A times B,
        this saves us coding, testing, reading, and debugging.
      </p>

      <p>
        Several higher-order functions are built in to Python.
        One is <code>filter</code>,
        which constructs a new list containing all the values in an original list
        for which some function is true:
      </p>

<pre src="src/funclib/hof.py">
def positive(x):
    return x &gt; 0

print filter(positive, [-5, 3, -2, 9, 0])
<span class="out">[3, 9]</span>
</pre>

      <p class="continue">
        Another is <code>map</code>,
        which applies a function to every element of a list and returns a list of results:
      </p>

<pre src="src/funclib/hof.py">
def bump(x):
    return x + 10

print map(bump, [-5, 3, -2, 9, 0])
<span class="out">[5, 13, 8, 19, 10]</span>
</pre>

      <p class="continue">
        And then there's <code>reduce</code>,
        which combines values using a binary function,
        returning a single value as a result:
      </p>

<pre src="src/funclib/hof.py">
def add(x, y):
    return x + y

print reduce(add, [-5, 3, -2, 9, 0])
<span class="out">5</span>
</pre>

      <p>
        Combining all of these is a very powerful way to do a lot of computation
        with very little typing:
      </p>

<pre src="src/funclib/hof.py">
print reduce(add, map(bump, filter(positive, [-5, 3, -2, 9, 0])))
<span class="out">32</span>
</pre>

      <p class="continue">
        Reading from the inside out, we have:
      </p>

      <ol>
        <li>
          filtered the list, keeping only the positive values,
        </li>
        <li>
          bumped them up by 10, and
        </li>
        <li>
          summed the results.
        </li>
      </ol>

      <p class="continue">
        Written out, this is:
      </p>

<pre src="src/funclib/hof.py">
total = 0
for val in [-5, 3, -2, 9, 0]:
    if val &gt; 0:
        total += (val + 10)
print total
</pre>

      <p>
        The functional approach is usually more economical,
        and isn't too bad to read once calls are indented:
      </p>

<pre>
print reduce(add,
             map(bump,
             filter(positive,
                    [-5, 3, -2, 9, 0])))
</pre>

      <p class="continue">
        However,
        the all-in-one-loop approach <em>is</em> faster,
        since each call in the functional approach is creating its own temporary list of results,
        only to have it discarded by the next function in the chain.
        As always,
        we should only worry about this once we are sure that
        (a) the program is working correctly,
        and (b) its performance really is a problem.
      </p>

      <div class="box">
        <h3>List Comprehensions</h3>
        <p class="fixme">explain list comprehensions</p>
      </div>

      <div class="keypoints" id="k:funcobj">
        <h3>Summary</h3>
        <ul>
          <li idea="turing">A function is just another kind of data.</li>
          <li>Defining a function creates a function object and assigns it to a variable.</li>
          <li>Functions can be assigned to other variables, put in lists, and passed as parameters.</li>
          <li>Writing higher-order functions helps eliminate redundancy in programs.</li>
          <li>Use <code>filter</code> to select values from a list.</li>
          <li>Use <code>map</code> to apply a function to each element of a list.</li>
          <li>Use <code>reduce</code> to combine the elements of a list.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

      <p>
        Functions are a way to divide code up into more comprehensible pieces:
        essentially,
        to replace several pieces of information with one to make the whole easier to understand.
        Functions are therefore not just about eliminating redundancy:
        they are worth writing even if they're only called once.
      </p>

      <p>
        In fact,
        functions are such a powerful idea that
        many people regard programming as the art of defining a mini-language
        in which the solution to the original problem is trivial.
        To close off this chapter,
        let's try to answer a frequently-asked question:
        when should we write functions?
        And what should we put in them?
      </p>

      <p>
        The answers to these questions depend on the fact that
        human short-term memory can only hold a few things at a time.
        If we try to remember more than a double handful of unrelated bits of information
        for more than a few seconds,
        they become jumbled and we start making mistakes.
        In particular,
        if someone has to keep several dozen things straight in their mind
        in order to understand a piece of code,
        that code is too long.
      </p>

      <p>
        Let's consider an example:
      </p>

<pre src="src/funclib/cognitive_limits_initial.py">
for x in range(1, GRID_WIDTH-1):
  for y in range(1, GRID_HEIGHT-1):
    if (density[x-1][y] &gt; density_threshold) or \
       (density[x+1][y] &gt; density_threshold):
      if (flow[x][y-1] &lt; flow_threshold) or\
         (flow[x][y+1] &lt; flow_threshold):
        temp = (density[x-1][y] + density[x+1][y]) / 2
        if abs(temp - density[x][y]) &gt; update_threshold:
          density[x][y] = temp
</pre>

      <p class="continue">
        This code uses meaningful variable names,
        and is well structured,
        but it's still a lot to digest in one go.
        Let's replace the loop bounds with function calls
        that give us a bit more context:
      </p>

<pre src="src/funclib/cognitive_limits_bounds.py">
for x in grid_interior(GRID_WIDTH):
  for y in grid_interior(GRID_HEIGHT):
    if (density[x-1][y] &gt; density_threshold) or \
       (density[x+1][y] &gt; density_threshold):
      if (flow[x][y-1] &lt; flow_threshold) or\
         (flow[x][y+1] &lt; flow_threshold):
        temp = (density[x-1][y] + density[x+1][y]) / 2
        if abs(temp - density[x][y]) &gt; update_threshold:
          density[x][y] = temp
</pre>

      <p class="continue">
        <code>grid_interior(num)</code> might just return <code>range(1, num-1)</code>,
        but try reading the first two lines of this code aloud,
        and then the first two lines of what it replaced,
        and see which is easier to understand.
      </p>

      <p>
        Now let's replace those two <code>if</code> statements with function calls as well:
      </p>

<pre src="src/funclib/cognitive_limits_threshold.py">
for x in grid_interior(GRID_WIDTH):
  for y in grid_interior(GRID_HEIGHT):
    if density_exceeds(density, x, y, density_threshold):
      if flow_exceeds(flow, x, y, flow_threshold):
        temp = (density[x-1][y] + density[x+1][y]) / 2
        if abs(temp - density[x][y]) > tolerance:
          density[x][y] = temp
</pre>

      <p class="continue">
        Again, we've provided more information about what we're actually doing.
        Finally, let's create and call a function
        to handle updates to our data structure:
      </p>

<pre src="src/funclib/cognitive_limits_final.py">
for x in grid_interior(GRID_WIDTH):
  for y in grid_interior(GRID_HEIGHT):
    if density_exceeds(density, x, y, density_threshold):
      if flow_exceeds(flow, x, y, flow_threshold):
        update_on_tolerance(density, x, y, tolerance)
</pre>

      <p class="continue">
        Our original nine lines have become five,
        and those five are all at the same mental level.
        It's hard to pin down exactly what that phrase means,
        but most programmers would agree that
        the first version mixed high-level ideas about boundaries and update conditions
        with low-level details of grid access and cell value comparisons.
        In contrast,
        this version only has the high-level stuff;
        the low-level implementation details are hidden in those functions.
      </p>

      <p>
        A conscientious programmer who wrote the code we started with
        would go back and <a href="glossary.html#refactor">refactor</a> it
        to turn it into something like our final version
        before committing it to <a href="svn.html">version control</a>.
        If she did this often enough,
        she would eventually find herself writing the final version first,
        just as mathematicians find themselves skipping more and more "obvious" steps
        as they do more proofs.
        When we see someone "just writing" something elegant,
        the odds are good that they have spent time rewriting their own poor code,
        and in doing so,
        turned conscious decision into unconscious action.
      </p>

    </section>