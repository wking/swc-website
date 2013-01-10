Title: Basic Programming With Python
Directory: book

    <ol class="toc">
      <li><a href="#s:basic">Basic Operations</a></li>
      <li><a href="#s:program">Creating Programs</a></li>
      <li><a href="#s:types">Types</a></li>
      <li><a href="#s:io">Reading Files</a></li>
      <li><a href="#s:stdio">Standard Input and Output</a></li>
      <li><a href="#s:for">Repeating Things</a></li>
      <li><a href="#s:logic">Making Choices</a></li>
      <li><a href="#s:flag">Flags</a></li>
      <li><a href="#s:parse">Reading Data Files</a></li>
      <li><a href="#s:provenance">Provenance Revisited</a></li>
      <li><a href="#s:lists">Lists</a></li>
      <li><a href="#s:morelist">More About Lists</a></li>
      <li><a href="#s:nestloop">Nesting Loops</a></li>
      <li><a href="#s:nestlist">Nesting Lists</a></li>
      <li><a href="#s:alias">Aliasing</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <span class="comment"> LH: don't hard-code data values into your programs. Instead,
    pass them to your programs via command-line arguments or input
    files. </span>

    <p>
      A cochlear implant is a small device placed in the inner ear
      to give the hearing impaired a sense of sound.
      To test how effective they are,
      Aurora Audio wants to measure three things:
      the range of tones people can hear,
      how well they can discriminate between similar tones.
      and the softest volume they can notice.
      Each test is supposed to be scored from 0 to 5,
      but after her volunteers submitted their data,
      she found that some had scored from -5 to 5 instead.
      She needs to clean up the data before using it.
    </p>

    <span class="comment"> JK: It's unclear who the volunteer is. "range of tones that XX
         volunteers can hear" might be better. </span>

    <p>
      If Aurora had only one data set,
      the fastest solution might be to use a spreadsheet.
      However,
      she actually has over a hundred data sets,
      with more coming in each week.
      Since she doesn't want to spend hours doing the same things over and over again,
      she wants to write a small program to clean up her data for her.
      To do that,
      she's going to have to learn how to program,
      and that's what the next couple of chapters are about.
    </p>

    <p>
      We will use a programming language called Python for our examples.
      Python is free,
      reasonably well documented,
      and widely used in science and engineering.
      Our main reason for choosing it,
      though,
      is that newcomers find it easier to read than most other languages.
      It also allows people to do useful things
      without having to master advanced concepts like object-oriented programming.
    </p>

    <p>
      Our first few programs will show you how to manipulate data stored in text files.
      This is a bit old fashioned,
      but it's still a common task in every branch of science.
      It's also simple:
      flashier approaches,
      like manipulating images and doing 3D graphics,
      require extra software that can be painful to install.
    </p>

    <section id="s:basic">

      <h2>Basic Operations</h2>

      <div class="understand" id="u:basic">
        <h3>Understand:</h3>
        <ul>
          <li>How to use the Python interpreter interactively.</li>
          <li>How to do basic arithmetic.</li>
          <li>How to assign values to variables.</li>
        </ul>
      </div>

      <p>
        The best way to learn how to program is to start programming,
        so let's run the Python interpreter
        and type in the following:
      </p>

      <span class="comment"> JK: Presumably this link will go somewhere eventually - would be 
           good to make sure it includes install instructions for Python, 
           perhaps with a note about Enthough distro for academic users. </span>

<pre>
&gt;&gt;&gt; <span class="in">print 1 + 1</span>
<span class="out">2</span>
</pre>

      <p class="continue">
        The <code>&gt;&gt;&gt;</code> <a href="glossary.html#prompt">prompt</a>
        is the interpreter's way of telling us that it's waiting for input,
        like the <code>$</code> prompt in <a href="shell.html">the shell</a>.
        When we enter 1+1,
        Python does the calculation we've asked for
        and prints the result.
      </p>

      <p>
        Now type this:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">x = 1+1</span>
</pre>

      <p class="continue">
        Python doesn't display anything this time
        (except another prompt).
        Instead,
        as <a href="#f:first_variable">Figure 1</a> shows,
        it creates a <a href="glossary.html#variable">variable</a> called <code>x</code>
        and assigns it the value 2.
        We can then get that variable's value simply by entering its name:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">print x</span>
<span class="out">2</span>
</pre>

      <figure id="f:first_variable">
        <img src="img/python/first_variable.png" alt="Our First Variable" />
      </figure>

      <div class="box">

        <h3>Statements vs. Expressions</h3>

        <p>
          Python is a fairly relaxed language,
          but there are still some things it won't let us do.
          For example,
          this doesn't work:
        </p>

<pre>
print x = 1 + 2
<span class="err">SyntaxError: invalid syntax</span>
</pre>

        <span class="comment"> JK: This print syntax is for Python 2.X - since some first-time 
             users may install 3 without realizing the difference, there should 
             probably be (1) a box explaining the difference and recommending 
             one or the other, either here on the page that describes Python 
             installation, and (2) a box mentioning that Python 3 changes some
             syntax, with the print function as an example, since print is
             to be one of the few immediately obvious differences for
             beginners. </span>

        <p class="continue">
          The problem is that printing and assignment are both
          <a href="glossary.html#statement">statements</a>,
          and statements cannot be mixed together.
          1+2, on the other hand,
          is an <a href="glossary.html#expression">expression</a>&mdash;something
          that produces a new value&mdash;and expressions can be combined in many ways.
          Except for assignment,
          every statement in Python begins with a keyword like <code>print</code>,
          so it's usually easy to tell them apart.
        </p>

      </div>

      <p>
        We can now use that variable's value in calculations:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">print x * 2</span>
4
</pre>

      <p class="continue">
        including ones that create more variables:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">y = x * 2</span>
&gt;&gt;&gt; <span class="in">print y</span>
<span class="out">4</span>
</pre>

      <p class="continue">
        We can change a variable's value
        by assigning something new to it:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">x = 10</span>
&gt;&gt;&gt; <span class="in">print x</span>
10
</pre>

      <p class="continue">
        As <a href="#f:assign_new_value">Figure XXX</a> shows,
        assigning something to <code>x</code> changes what it points to,
        but does not change anything else.
        In particular,
        <code>y</code> still has the value 4 after this assignment:
        it is not automatically updated when <code>x</code>'s value changes,
        as it would in a spreadsheet.
      </p>

      <figure id="f:assign_new_value">
        <img src="img/python/assign_new_value.png" alt="Assigning a New Value" />
      </figure>

      <p>
        Here's a more complex calculation:
      </p>

<pre src="src/python/fahrenheit_to_kelvin_unreadable.py">
&gt;&gt;&gt; <span class="in">x = 98.6</span>
&gt;&gt;&gt; <span class="in">y = (x - 32.0) * (5.0 / 9.0) + 273.15</span>
&gt;&gt;&gt; <span class="in">print y</span>
<span class="out">310.15</span>
</pre>

      <p class="continue">
        Its meaning becomes clearer if we rewrite it as:
      </p>

<pre src="src/python/fahrenheit_to_kelvin.py">
&gt;&gt;&gt; <span class="in">temp_fahr = 98.6</span>
&gt;&gt;&gt; <span class="in">temp_kelvin = (temp_fahr - 32.0) * (5.0 / 9.0) + 273.15</span>
&gt;&gt;&gt; <span class="in">print "body temperature in Kelvin:", temp_kelvin</span>
<span class="out">body temperature in Kelvin: 310.15</span>
</pre>

      <p>
        The first line creates a new variable called <code>temp_fahr</code>
        (short for "temperature in Fahrenheit")
        and gives it the value 98.6
        (<a href="#f:first_memory_model">Figure XXX</a>).
        The second line creates another variable to hold the temperature in Kelvin
        (hence its name).
        It calculates a value for this variable
        that depends on the value of <code>temp_fahr</code>.
        The last line prints the result.
        The <a href="glossary.html#string">character string</a>
        (or just "string" for short)
        inside double quotes is printed as-is,
        followed by the value of <code>temp_kelvin</code>.
      </p>

      <figure id="f:first_memory_model">
        <img src="img/python/first_memory_model.png" alt="First Memory Model" />
      </figure>

    <span class="comment"> JK: There's a bit of a semantic jump here from entering statements to 
         a "program", even though this is still a set of three statements that
         can't be run in a self-contained sense like the "programs" described
         later. </span>

      <p>
        Like every program,
        this one stores data and does calculations.
        We use variables to do the first,
        and write instructions that use those variables to do the second.
        And like every <em>good</em> program,
        this one is written with human beings in mind.
        Computers get faster every year,
        but our brains don't.
        As a result,
        the real bottleneck in scientific computing is usually not
        how fast the program runs,
        but how long it takes us to write it.
        This is why we use variable names like <code>temp_fahr</code> and <code>temp_kelvin</code>
        instead of <code>x</code> and <code>y</code>.
      </p>

      <div class="box">

        <h3>Creating Variables</h3>

        <p>
          Python creates a variable whenever a value is assigned to a name,
          but won't let us get the value of a variable that hasn't been assigned one.
          For example,
          if we try to do this:
        </p>

<pre>
&gt;&gt;&gt; <span class="in">double_temp = temp_celsius * 2</span>
</pre>

        <p class="continue">
          then Python prints an error message:
        </p>

<pre>
<span class="err">Traceback (most recent call last):
  File "&lt;undefined-variable.py&gt;", line 1, in &lt;module&gt;
NameError: name 'temp_celsius' is not defined</span>
</pre>

        <p class="continue">
          We'll explain what "module" means <a href="funclib.html">later</a>.
          What's important now is that this strictness helps catch a lot of typing mistakes:
          if we mistakenly type <code>temp_far</code> instead of <code>temp_fahr</code>:
        </p>

<pre>
&gt;&gt;&gt; <span class="in">temp_kelvin = (<span class="highlight">temp_far</span> - 32.0) * (5.0 / 9.0) + 273.15</span>
</pre>

        <span class="comment"> JK: Not sure which class caused this, but looks like the
             highlighted text has the same backgroundc color as the box? </span>

        <p class="continue">
          then Python will tell us something's gone wrong.
          It can't help us if we type 3.20 instead of 32.0, though;
          if we want to catch that mistake,
          we'll actually have to <a href="quality.html">test our program</a>.
        </p>

      </div>

      <p>
        Readability is also why we put the temperature in Fahrenheit in a variable,
        then use that variable in line 2,
        rather than just putting 98.6 directly in the calculation.
        If we ever want to convert another temperature,
        it's easier to see and change the value on line 1
        than it would be to find it buried in the middle of a line of arithmetic.
      </p>

      <p>
        Finally,
        this first program also shows how arithmetic is done.
        '+' means addition,
        '*' means multiplication,
        and parentheses group things together,
        just as they do in pen-and-paper arithmetic.
        We have to use parentheses here because
        (also as in arithmetic)
        multiplication takes precedence over addition:
        the expression <code>2*3+5</code> means,
        "Multiply two by three, then add five,"
        rather than,
        "Add three and five, then multiple by two."
        If we want the latter,
        we have to write <code>2*(3+5)</code>.
      </p>

      <div class="box">

        <h3>Repeating Commands</h3>

        <p>
          Just as we could repeat previous commands in the shell
          by using the <a href="shell.html#a:repeat">up arrow</a>,
          so too can we repeat commands in the Python interpreter.
          And while the standard interpreter doesn't have an equivalent
          of the shell's <code>history</code> command,
          more advanced shells like IPython do
          (along with much more).
        </p>

      </div>

      <div class="keypoints" id="k:basic">
        <h3>Summary</h3>
        <ul>
          <li>Use '=' to assign a value to a variable.</li>
          <li>Assigning to one variable does not change the values associated with other variables.</li>
          <li>Use <code>print</code> to display values.</li>
          <li>Variables are created when values are assigned to them.</li>
          <li>Variables cannot be used until they have been created.</li>
          <li>Addition ('+'), subtraction ('-'), and multiplication ('*') work as usual in Python.</li>
          <li idea="perf">Use meaningful, descriptive names for variables.</li>
        </ul>
      </div>

    </section>

    <section id="s:program">

      <h2>Creating Programs</h2>

      <div class="understand" id="u:program">
        <h3>Understand:</h3>
        <ul>
          <li>How to create and run programs.</li>
        </ul>
      </div>

      <p>
        Typing in commands over and over again is tedious and error-prone.
        Just as we saved shell commands in <a href="shell.html#s:scripts">shell scripts</a>,
        we can save Python commands in files
        and then have the Python interpreter run those.
        Using your favorite text editor,
        put the following three lines into a plain text file:
      </p>

<pre src="src/python/greeting.py">
left = "hello"
right = "there"
print left, right
</pre>

      <p class="continue">
        and then save it as <code>greeting.py</code>.
        (By convention,
        Python files end in '.py'
        rather than '.txt'.)
        To run it from the shell,
        type:
      </p>

<pre>
$ <span class="in">python greeting.py</span>
<span class="out">hello there</span>
</pre>

      <p>
        When the Python interpreter executes a file,
        it runs the commands in that file
        just as if they had been typed in interactively.
        It doesn't wait until the whole file has been read
        to start executing;
        instead,
        as the example below shows,
        it runs each command as soon as it can:
      </p>

    <span class="comment"> JK: I think what was intended here was for the first 3 lines to 
         replace the existing 3 lines in greeting.py, then 'python greeting.py' 
         was to be run from the shell? If so, having the first 3 new lines in a 
         separate blue box might be more clear. Also, the text below currently
         references a.py. </span>

<pre src="src/python/executing_file.py">
print "before"
1/0
print "after"
<span class="out">before</span>
<span class="err">Traceback (most recent call last):
  File "a.py", line 2, in &lt;module&gt;
    1/0
ZeroDivisionError: integer division or modulo by zero</span>
</pre>

      <p class="continue">
        Note that this can lead to some confusing output.
        For example,
        if we change the example above to:
      </p>

<pre>
print "before", 1/0, "after"
</pre>

      <p class="continue">
        then the output is:
      </p>

<pre><span class="out">before</span>
<span class="err">Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ZeroDivisionError: integer division or modulo by zero</span>
</pre>

      <div class="keypoints" id="k:program">
        <h3>Summary</h3>
        <ul>
          <li>Store programs in files whose names end in <code>.py</code> and run them with <code>python <em>name.py</em></code>.</li>
        </ul>
      </div>

    </section>

    <section id="s:types">

      <h2>Types</h2>

      <div class="understand" id="u:types">
        <h3>Understand:</h3>
        <ul>
          <li>What data types are.</li>
          <li>The differences between integers, floating-point numbers, and strings.</li>
          <li>How to call a function.</li>
          <li>Why computers shouldn't guess what people want.</li>
        </ul>
      </div>

      <p>
        Let's take another look at our program:
      </p>

<pre src="src/python/fahrenheit_to_kelvin.py">
temp_fahr = 98.6
temp_kelvin = (temp_fahr - 32.0) * (5.0 / 9.0) + 273.15
print "body temperature in Kelvin:", temp_kelvin
<span class="out">body temperature in Kelvin: 310.15</span>
</pre>

      <p>
        Why have we written 5.0/9.0 instead of 5/9?
        Let's see what happens if we take out the .0's:
      </p>

<pre src="src/python/fahrenheit_to_kelvin_int.py">
&gt;&gt;&gt; <span class="in">temp_fahr = 98.6</span>
<span class="highlight">temp_kelvin = (temp_fahr - 32) * (5 / 9) + 273.15</span>
&gt;&gt;&gt; <span class="in">print "body temperature in Kelvin:", temp_kelvin</span>
<span class="out">body temperature in Kelvin: 273.15</span>
</pre>

      <p>
        That's not right.
        To understand what's gone wrong,
        let's look at 5/9:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">5/9</span>
<span class="out">0</span>
</pre>

      <p>
        The problem is that integers and floating point numbers
        (or <a href="glossary.html#float">floats</a>)
        are different things to a computer.
        If a number doesn't have a decimal point,
        then Python stores its value as an integer (with no fractional part).
        When it divides one integer by another,
        it throws away the remainder.
        If a number contains a decimal point,
        though,
        Python stores it as a float.
        When it does division (or any other kind of arithmetic),
        the result is a float if either of the values involved is a float:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">10 / 3</span>
<span class="out">3</span>
&gt;&gt;&gt; <span class="in">10.0 / 3</span>
<span class="out">3.3333333333333335</span>
</pre>

      <p class="continue">
        This makes sense,
        but only if you understand how the chips inside computers work.
        Version 3 of Python changed the rules for division
        so that it returns fractional numbers whenever it needs to.
        However,
        we're using Python 2.7 in this course,
        so 10/3 is 3 until further notice.
      </p>

      <span class="comment"> JK: I would suggest bringing this up earlier, since it's also 
           relevant to the print statement. Also, does dynamic typing need to 
           be introduced, or at least mentioned, around here somewhere? An 
           example could be x=2, type(x) >>> int, x='hello', type(x) >>>
           string. </span>

      <p>
        Every value in a program has a specific <a href="glossary.html#type">type</a>
        which determines how it behaves
        and what can be done to it.
        We can find out what type something is
        using a built-in <a href="glossary.html#function">function</a> called <code>type</code>:
      </p>


        <span class="comment"> JK: Typo here, should be 'int' not 'int, and same for float. </span>
<pre>
&gt;&gt;&gt; <span class="in">type(12)</span>
<span class="out">&lt;type 'int&gt;</span>
&gt;&gt;&gt; <span class="in">type(12.0)</span>
<span class="out">&lt;type 'float&gt;</span>
</pre>

      <p>
        Integers and floating-point numbers are two common types;
        another is the character string.
        We can create one by putting characters inside either single or double quotes
        (as long as they match at the beginning and end):
      </p>

<pre src="src/python/simple_string.py">
&gt;&gt;&gt; <span class="in">name = "Alan Turing"</span>
&gt;&gt;&gt; <span class="in">born = 'June 23, 1912'</span>
&gt;&gt;&gt; <span class="in">print name, born</span>
<span class="out">Alan Turing June 23, 1912</span>
</pre>

      <p>
        We can also "add" strings:
      </p>

<pre src="src/python/simple_string.py">
&gt;&gt;&gt; <span class="in">full = name + " (" + born + ")"</span>
&gt;&gt;&gt; <span class="in">print full</span>
<span class="out">Alan Turing (June 23, 1912)</span>
</pre>

      <p>
        What we <em>can't</em> do is add numbers and strings:
      </p>

<pre src="src/python/add_numbers_strings.py">
&gt;&gt;&gt; <span class="in">print 2 + "three"</span>
<span class="err">Traceback (most recent call last):
  File "add-numbers-strings.py", line 1, in &lt;module&gt;
    print 2 + "three"
TypeError: unsupported operand type(s) for +: 'int' and 'str'</span>
</pre>

      <p>
        The string "2three" would be a reasonable result in this case,
        but it's not so clear what <code>2+"3"</code> should do:
        should it produce the integer 5 or the string <code>"23"</code>?
        Rather than guessing at the programmer's intentions,
        Python expects some guidance:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">print 2 + int("3")</span>
<span class="out">5</span>
&gt;&gt;&gt; <span class="in">print str(2) + "3"</span>
<span class="out">23</span>
</pre>

      <p>
        <code>int</code> and <code>str</code> are two more built-in functions
        which convert values to particular types.
        We'll look at functions in much more detail
        in <a href="funclib.html">the next chapter</a>.
      </p>

      <div class="keypoints" id="k:types">
        <h3>Summary</h3>
        <ul>
          <li>The most commonly used data types in Python are integers (<code>int</code>), floating-point numbers (<code>float</code>), and strings (<code>str</code>).</li>
          <li>Strings can start and end with either single quote (') or double quote (&quot;).</li>
          <li>Division ('/') produces an <code>int</code> result when given <code>int</code> values: one or both arguments must be <code>float</code> to get a <code>float</code> result.</li>
          <li>"Adding" strings concatenates them, multiplying strings by numbers repeats them.</li>
          <li idea="meaning">Strings and numbers cannot be added because the behavior is ambiguous: convert one to the other type first.</li>
          <li>Variables do not have types, but values do.</li>
        </ul>
      </div>

    </section>

    <section id="s:io">

      <h2>Reading Files</h2>

      <div class="understand" id="u:io">
        <h3>Understand:</h3>
        <ul>
          <li>Where computers store information.</li>
          <li>How to open a file and read data from it.</li>
          <li>How "lines" are stored in text files.</li>
          <li>How to call a method.</li>
          <li>How to write to a file.</li>
        </ul>
      </div>

      <p>
        Broadly speaking,
        modern computers store data in one of six places
        (<a href="#f:memory_architecture">Figure XXX</a>):
      </p>

      <ol>

        <li>
          Inside the processor itself.
        </li>

        <li>
          Inside a short-term memory called cache.
        </li>

        <li>
          In main memory.
        </li>

        <li>
          On a local disk.
        </li>

        <li>
          On disk somewhere else on a network.
        </li>

        <li>
          In an offline archive,
          such as a DVD jukebox.
        </li>

      </ol>

      <figure id="f:memory_architecture">
        <img src="img/python/memory_architecture.png" alt="Where Data is Stored" />
      </figure>

      <p>
        Each level is tens to thousands of times faster than the one below it,
        but tens to thousands of times more expensive per byte.
        Computer systems have therefore been designed to expose some of these layers to users,
        but not others:
        for example,
        it's actually hard to figure out exactly when data is in the CPU,
        in cache,
        or in main memory.
      </p>

      <p>
        In practice,
        this six-level hierarchy can be divided into three layers:
      </p>

      <ol>

        <li>
          The data is in memory.
          The program can manipulate it directly,
          but changes will not be saved when the program ends.
        </li>

        <li>
          The data is on disk.
          The program has to read it into memory to work with it,
          and write changes back out,
          but those changes will persist after the program ends.
        </li>

        <li>
          The data is far away,
          and may not be available when we want it.
        </li>

      </ol>

    <span class="comment"> JK: Could be a teachable moment here about "the cloud" as something 
         that makes data that's actually far away look like it's on disk - if 
         you wanted a digression ;-) </span>

      <p>
        We'll deal with the third issue in a <a href="web.html">later chapter</a>.
        For now,
        let's look at how to get data out of a file on our computer's hard drive.
        Suppose our hearing test data files are formatted like this:
      </p>

<span class="comment"> This is referred to later as cochlear01.txt, might be worth saying 
     "suppose we have a hearing data file named cochlear01.txt that is..." </span>

<pre src="src/python/cochlear01.txt">
Subject: 1782
Date:    2012-05-21
Test     Run  Score
----     ---  -----
range    1    3
range    2    5
discrim  1    1
discrim  2    1
discrim  4    1.5
volume   1    3.5
volume   2    4.0
</pre>

      <p class="continue">
        It's easy to see where the tester decided that half-point scores were OK.
        We can also see that the tester either forgot to record
        the result of the third discrimination test,
        or decided to leave it out.
        Before worrying about that,
        let's write a small program that extracts the subject ID from a data file:
      </p>

    <span class="comment"> JK: Might want a "save these lines in a file called 
         get-subject-data.py in the same directory as data file" here for
         clarity. </span>

<pre src="src/python/get_subject_date.py">
reader = file('cochlear01.txt', 'r')
first_line = reader.readline()
print first_line
reader.close()
</pre>

      <p>
        The first line uses a built-in function called <code>file</code>
        to open our file.
        Its first argument is the name of the file being opened.
        Its second is the string <code>'r'</code>,
        which signals that we want to read from this file
        (rather than write to it).
      </p>

      <p>
        <code>file</code>
        creates a connection (or <a href="glossary.html#handle">handle</a>)
        between the program and the data on disk
        (<a href="#f:file_object">Figure XXX</a>),
        which is assigned to the variable <code>reader</code>.
        There's nothing special about that name&mdash;we could call it <code>newton</code>&mdash;but
        whatever we call it,
        we can ask it to read a line from the file for us
        and assign that string to <code>first_line</code>
        by calling its <a href="glossary.html#method">method</a> <code>readline</code>.
        The program then prints that line and tells the file to close itself.
        This last step isn't strictly necessary in a small program&mdash;Python
        automatically closes any files that are open when the program finishes&mdash;but
        it's a good habit to get into,
        since the operating system limits the number of files any one program can have open at a time.
      </p>

      <figure id="f:file_object">
        <img src="img/python/file_object.png" alt="File Objects" />
      </figure>

      <div class="box">

        <h3>Methods</h3>

        <p>
          <code>readline</code> is a special kind of function
          called a <a href="glossary.html#method">method</a>.
          It's attached to a particular object&mdash;in this case,
          to the file handle <code>reader</code>.
          You can think of objects and methods as nouns and verbs,
          so when we write <code>reader.readline()</code>,
          we're asking whatever the variable <code>reader</code> points at
          to do <code>readline</code> for us.
          As <a href="#f:methods">Figure XXX</a> shows,
          the methods are associated with the thing the variable points at,
          not with the variable itself.
        </p>

        <figure id="f:methods">
          <img src="img/python/methods.png" alt="Where Methods are Stored" />
        </figure>

      </div>

      <p>
        Here's what happens when we run our program:
      </p>

<pre>
$ <span class="in">python get-subject-date.py</span>
<span class="out">Subject: 1782

</span>
</pre>

      <p>
        It's not easy to see, but there's actually an extra blank line in the output.
        Where does it come from?
      </p>

      <p>
        The answer depends on the fact that text files aren't stored in lines:
        that's just how things like text editors and shell commands display them.
        A text file is actually stored as a sequence of bytes
        (<a href="#f:text_file_storage">Figure XXX</a>).
        Some of those happen to be newline characters,
        and most tools interpret them as meaning "end of line".
        In particular,
        when asked to read the next line from a file,
        Python's file-reading functions read up to and including the end-of-line marker
        and return that.
      </p>

      <figure id="f:text_file_storage">
        <img src="img/python/text_file_storage.png" alt="Text File Storage" />
      </figure>

      <p>
        Nothing says files have to be stored this way, though.
        On Windows,
        text files use two characters&mdash;a carriage return and a newline&mdash;to
        mark the end of line.
        If we are using Python on Windows,
        it automatically translates those two characters into a single newline when reading,
        and translates newlines back into those two characters when writing,
        so that our programs don't have to worry about it.
      </p>

      <p>
        Coming back to our program,
        the <code>print</code> command automatically adds an end-of-line marker
        to its output.
        We can tell it not to do that by putting a comma at the end of the line.
        This usually makes things confusing:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">print 5</span>
<span class="out">5</span>
&gt;&gt;&gt; <span class="in">print 5,</span>
<span class="out">5</span>&gt;&gt;&gt;
</pre>

      <p class="continue">
        but it's useful when we want to prevent newlines doubling up:
      </p>

<pre src="src/python/get_subject_date_newline.py">
reader = file('cochlear01.txt', 'r')
first_line = reader.readline()
print first_line<span class="highlight">,</span>
reader.close()
<span class="out">Subject: 1782</span>
</pre>

      <p>
        A better way to solve the problem is to get rid of the line ending on the string:
      </p>

<pre src="src/python/get_subject_date_newline.py">
reader = file('cochlear01.txt', 'r')
first_line = reader.readline()
<span class="highlight">first_line = first_line.strip()</span>
print first_line
reader.close()
<span class="out">Subject: 1782</span>
</pre>

    <span class="comment"> JK: "...and, like files, strings have methods." is a tricky statment 
         since you mean file in the Python object sense, not the sense of a 
         string of bytes called my_file.txt that's sitting on disk. "File 
         objects", or "the reader variable", might be more clear. </span> 

      <p class="continue">
        <code>first_line</code> is a string,
        and,
        like files,
        strings have methods.
        One of them, <code>strip</code>,
        creates a new string by removing any leading or trailing spaces, tabs, or line-ending characters
        from the original string
        (<a href="#f:string_strip">Figure XXX</a>).
        It does <em>not</em> modify the original string:
        in Python,
        any string has a fixed value,
        just as the integer <code>5</code>'s value is always fixed at 5.
      </p>

      <figure id="f:string_strip">
        <img src="img/python/string_strip.png" alt="Stripping Strings" />
      </figure>

      <div class="box">

        <h3>Writing Files</h3>

        <p>
          Writing to a file is as easy as reading from one:
        </p>

<pre src="src/python/writing.py">
writer = file('mydata.txt', 'w')
print &gt;&gt; writer, 'largest value:', 20
print &gt;&gt; writer, 'smallest value:', -2
writer.close()
</pre>

        <p class="continue">
          We begin by opening the file in <code>'w'</code> (write) mode.
          This gives us a handle that we can use in subsequent operations,
          which we assign to a variable.
          (We've called it <code>writer</code> here,
          but we could call it anything.)
          After that,
          we can print to the file exactly as we have been printing to the screen;
          as always,
          we close the file when we're done
          (which is when the last few things we've written to the file are actually stored on disk).
        </p>

        <p>
          Opening a file for writing erases its previous content,
          or creates the file if it didn't already exist.
          If we don't want to erase any previous content,
          we can open the file for appending using <code>'a'</code> instead of <code>'w'</code>.
        </p>

      </div>

      <div class="keypoints" id="k:io">
        <h3>Summary</h3>
        <ul>
          <li>Data is either in memory, on disk, or far away.</li>
          <li>Most things in Python are objects, and have attached functions called methods.</li>
          <li>When lines are read from files, Python keeps their end-of-line characters.</li>
          <li>Use <code>str.strip</code> to remove leading and trailing whitespace (including end-of-line characters).</li>
          <li>Use <code>file(<em>name</em>, <em>mode</em>)</code> to open a file for reading ('r'), writing ('w'), or appending ('a').</li>
          <li>Opening a file for writing erases any existing content.</li>
          <li>Use <code>file.readline</code> to read a line from a file.</li>
          <li>Use <code>file.close</code> to close an open file.</li>
          <li>Use <code>print &gt;&gt; file</code> to print to a file.</li>
        </ul>
      </div>

    </section>

    <section id="s:stdio">

      <h2>Standard Input and Output</h2>

      <div class="understand" id="u:stdio">
        <h3>Understand:</h3>
        <ul>
          <li>How to import a module.</li>
          <li>How to read from standard input.</li>
          <li>How to write to standard output.</li>
        </ul>
      </div>

      <p>
        Our program currently reads the header from <code>cochlear01.txt</code>
        every time we run it.
        There's not much point in that:
        what we really want is to read from any file,
        or from several files in turn.
        Doing that requires a bit of machinery we haven't seen yet,
        so let's solve a simpler problem:
        reading from standard input instead of from a file.
        Once we can do that,
        we can run our program as:
      </p>

<pre>
$ <span class="in">python get-subject-date.py &lt; somefile.txt</span>
</pre>

      <p class="continue">
        or read from several files using:
      </p>

<pre>
$ <span class="in">for inputfile in cochlear*.txt
do
    python get-subject-date.py &lt; $inputfile
done</span>
</pre>

      <p>
        Here's the modified program:
      </p>

<pre src="src/python/get_subject_date_stdin.py">
<span class="highlight">import sys
reader = sys.stdin</span>
first_line = reader.readline()
first_line = first_line.strip()
print first_line
reader.close()
</pre>

      <p class="continue">
        The two lines that have changed are highlighted at the top of the program.
        The first loads a library called <code>sys</code>,
        which connects Python to the system it is running on.
        The second line sets <code>reader</code> to be <code>sys.stdin</code>,
        which is just the standard input stream we met in
        <a href="shell.html#s:pipefilter:pipes">our discussion of pipes</a>.
        Nothing else changes,
        since standard input tries really hard to behave like an open file
        (<a href="#f:replacing_with_stdin">Figure XXX</a>).
        In particular,
        the object that <code>sys.stdin</code> (and hence <code>reader</code>) points at
        has a method with the same name and behavior as a file's <code>readline</code> method,
        and another with the same name and behavior as a file's <code>close</code>,
        so we can swap one for the other without having to modify anything else.
      </p>

      <figure id="f:replacing_with_stdin">
        <img src="img/python/replacing_with_stdin.png" alt="Replacing a File with Standard Input" />
      </figure>

      <div class="box">

        <h3>Interactive Testing</h3>

        <p>
          One other benefit of reading from standard input when no files are supplied
          is that it allows interactive testing:
          we can run our program
          and then just type in things we want it to read.
          If we do this,
          we must type control-D to signal the end of input
          (or control-Z in a Windows shell).
        </p>

      </div>

      <div class="box">

        <h3>Writing to Standard Output</h3>

        <p>
          Just as we can write to an open file using <code>print &gt;&gt; handle</code>,
          we can write to standard output using <code>print &gt;&gt; sys.stdout</code>.
          This is redundant, though,
          since <code>print</code> sends things to standard output by default.
        </p>

      </div>

      <div class="keypoints" id="k:stdio">
        <h3>Summary</h3>
        <ul>
          <li>The operating system automatically gives every program three open "files" called standard input, standard output, and standard error.</li>
          <li>Standard input gets data from the keyboard, from a file when redirected with '&lt;', or from the previous stage in a pipeline with '|'.</li>
          <li>Standard output writes data to the screen, to a file when redirected with '&gt;', or to the next stage in a pipeline with '|'.</li>
          <li>Standard error also writes data to the screen, and is not redirected by '&gt;' or '|'.</li>
          <li>Use <code>import <em>library</em></code> to import a library.</li>
          <li>Use <code>library.thing</code> to refer to something imported from a library.</li>
          <li>The <code>sys</code> library provides open "files" called <code>sys.stdin</code> and <code>sys.stdout</code> for standard input and output.</li>
        </ul>
      </div>

    </section>

    <section id="s:for">

      <h2>Repeating Things</h2>

      <div class="understand" id="u:for">
        <h3>Understand:</h3>
        <ul>
          <li>How to repeat things using a loop.</li>
          <li>That the loop variable takes on a different value each time through the loop.</li>
          <li>How to tell what statements are in the body of a loop.</li>
        </ul>
      </div>

      <p>
        Computers are useful because they can do lots of calculations on lots of data,
        which means we need a concise way to represent multiple steps.
        (After all,
        writing out a million additions would take longer than doing them.)
        Let's start by finding out how many lines we have in our data file:
      </p>

<pre src="src/python/count_line_in_file.py">
reader = file('cochlear01.txt', 'r')
number = 0
for line in reader:
    number = number + 1
reader.close()
print number, 'lines in file'
<span class="out">11 lines in file</span>
</pre>

      <p class="continue">
        Once again, we create a connection to the file using <code>file</code>.
        We then use a <a href="glossary.html#for-loop">for loop</a>
        to get one line from the file at a time.
        We don't do anything with the lines;
        instead,
        we add 1 to the value of <code>number</code> each time we see a new one.
        Once we're done,
        we close the file
        (so that other people and programs can access it safely)
        and report our findings
        (<a href="#f:for_loop">Figure XXX</a>).
      </p>

      <figure id="f:for_loop">
        <img src="img/python/for_loop.png" alt="For Loop" />
      </figure>

      <p>
        The indented line is called the <a href="glossary.html#loop-body">body</a> of the loop.
        It's the command that Python executes repeatedly.
        When Python is expecting us to type in the body of a loop interactively,
        it changes its prompt from <code>&gt;&gt;&gt;</code> to <code>...</code>
        as a reminder.
      </p>

      <p>
        The variable <code>line</code> is sometimes called
        the <a href="glossary.html#loop-variable">loop variable</a>.
        There's nothing special about its name:
        we could equally well have called it <code>something</code>.
        What's important is that the <code>for</code> loop repeatedly
        assigns a value to it,
        then executes the loop body one more time.
      </p>

      <p>
        Python always uses indentation to show what's in the body of a loop
        (or anything else&mdash;we'll see other things that have bodies soon).
        This means that:
      </p>

<pre src="src/python/incorrectly_nested.py">
for line in reader:
    print line.strip()
    print "done"
</pre>

       <p class="continue">
         and:
       </p>

<pre src="src/python/correctly_nested.py">
for line in reader:
    print line.strip()
print "done"
</pre>

      <p class="continue">
        are different programs.  The first one prints:
      </p>

<pre>
<span class="out">Subject: 1782
done
Date:    2012-05-21
done
Test     Run  Score
done
...</span>
</pre>

      <p class="continue">
        because the statement <code>print "done"</code> is inside the loop body.
        The second prints:
      </p>

<pre>
<span class="out">Subject: 1782
Date:    2012-05-21
Test     Run  Score
...
volume   2    4.0
done
</span>
</pre>

      <p class="continue">
        because it is not.
      </p>

      <div class="box">

        <h3>Why Indentation?</h3>

        <p>
          Most other languages use visible markers to show the beginnings and ends of loop bodies,
          such as:
        </p>

<pre>
for value in data {
    print value
}
</pre>

        <p class="continue">
          or:
        </p>

<pre>
for value in data
begin
    print value
end
</pre>

        <p>
          Python uses indentation because studies done in the 1980s showed
          that's what people actually pay attention to.
          If we write something as:
        </p>
<pre>
for value in data {
    print value
}
    print "done"
</pre>

        <p class="continue">
          then most people reading the code in a hurry will "see"
          the second <code>print</code> statement as part of the loop.
        </p>

      </div>

      <div class="keypoints" id="k:for">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>for <em>variable</em> in <em>something</em>:</code> to loop over the parts of something.</li>
          <li>The body of a loop must be indented consistently.</li>
          <li>The parts of a string are its characters; the parts of a file are its lines.</li>
        </ul>
      </div>

    </section>

    <section id="s:logic">

      <h2>Making Choices</h2>

      <div class="understand" id="u:logic">
        <h3>Understand:</h3>
        <ul>
          <li>How to choose what statements to execute using conditionals.</li>
          <li>How to combine conditional tests.</li>
          <li>What an in-place operator is.</li>
        </ul>
      </div>

      <p>
        Let's make one more change to our program.
        If you recall,
        our data files look like this:
      </p>

<pre src="src/python/cochlear01.txt">
Subject: 1782
Date:    2012-05-21
Test     Run  Score
----     ---  -----
range    1    3
range    2    5
discrim  1    1
discrim  2    1
discrim  4    1.5
volume   1    3.5
volume   2    4.0
</pre>

      <p class="continue">
        The first four lines aren't actually data,
        so we really shouldn't include them in our count:
      </p>

<pre src="src/python/count_line_in_file_corrected.py">
reader = file('cochlear01.txt', 'r')
number = 0
for line in reader:
    number = number + 1
reader.close()
print number <span class="highlight">- 4</span>, 'lines in file'
<span class="out">7 lines in file</span>
</pre>

      <p>
        Of course,
        if anyone ever puts more (or less) than four descriptive lines at the top of a data file,
        our count will be wrong again.
        What we <em>really</em> want to do is skip everything up to the dashed lines.
        We also want to check that all the scores are between 0 and 5.
      </p>

      <p>
        Let's step back and build up the machinery we need.
        Suppose that our data files contained nothing but a single number on each line:
      </p>

<pre src="src/python/simple_cochlear02.txt">
3
5
<span class="highlight">-1</span>
1
1.5
<span class="highlight">7</span>
4.0
</pre>

      <p class="continue">
        (We have deliberately added two out-of-range values for our program to find.)
        Here's a program that reads the data
        and counts the number that fall outside the allowed range:
      </p>

<pre src="src/python/counting_outliers_wrong.py">
import sys
num_outliers = 0
for value in sys.stdin:
    if value &lt; 0:
        num_outliers = num_outliers + 1
    if value &gt; 5:
        num_outliers = num_outliers + 1
print num_outliers, "values out of range"
</pre>

      <p class="continue">
        The command <code>if</code> means exactly what it does in English:
        if a particular condition is true,
        then do the statement or statements that are in the <code>if</code> statement's body
        (i.e., indented underneath it).
        Here,
        we are using one <code>if</code> to see if the current value is less than 0,
        and another to see if it is greater than 5.
        In either case,
        we add one to the count of outliers.
        If neither condition is satisfied,
        the value is clean,
        and <code>num_outliers</code> won't be changed in that loop
        (<a href="#f:loop_cond_flow">Figure XXX</a>).
      </p>

      <figure id="f:loop_cond_flow">
        <img src="img/python/loop_cond_flow.png" alt="Conditional Execution" />
      </figure>

      <p>
        When we run this program, though, we don't get a count of outliers.
        Instead,
        we get an error message:
      </p>

<pre>
$ <span class="in">python count-outliers.py &lt; cochlear01.txt</span>
<span class="err">fixme: error message</span>
</pre>

      <p class="continue">
        The problem is once again one of types:
        the loop variable <code>line</code> holds a string like <code>'3'</code>,
        not the number 3.
        The fix is straightforward:
      </p>

<pre src="src/python/counting_outliers_wrong.py">
import sys
num_outliers = 0
for line in sys.stdin:
    value = float(line)
    if value &lt; 0:
        num_outliers = num_outliers + 1
    if value &gt; 5:
        num_outliers = num_outliers + 1
print num_outliers, "values out of range"
<span class="out">2 values out of range</span>
</pre>

      <p>
        We can combine our two tests using <code>and</code> and <code>or</code>:
      </p>

<pre src="src/python/simple_and_or.py">
import sys
num_outliers = 0
for line in sys.stdin:
    value = float(line)
    if (value &lt; 0) or (value &gt; 5):
        num_outliers = num_outliers + 1
print num_outliers, "values out of range"
<span class="out">2 values out of range</span>
</pre>

    <span class="comment"> JK: Here as before, I might find the box somewhat confusing if I were 
         a beginner. Either the lines are supposed to be entered sequentially
         in an interpreter, in which case the prompts are missing, or all lines 
         except the final one should be in a text file and run, which one can
         infer but requires a small mental jump - or was this style introduced
         earlier in the book? </span>

      <p class="continue">
        Alternatively,
        we could count how many values are in range by reversing the test:
      </p>

<pre src="src/python/simple_in_range.py">
import sys
num_valid = 0
for line in sys.stdin:
    value = float(line)
    if (0 &lt;= value) and (n &lt;= value):
        num_valid = num_valid + 1
print num_valid, "values in range"
<span class="out">5 values in range</span>
</pre>

    <span class="comment"> JK: I think there's an error in the above - should it read 
         if (0 <= value) and (value <= 5): ? In any event, there's no n 
         variable here. </span>

      <p class="continue">
        or even:
      </p>

<pre src="src/python/single_range_test.py">
import sys
num_valid = 0
for line in data:
    value = float(line)
    if <span class="highlight">0 &lt;= value &lt;= 5</span>:
        num_valid = num_valid + 1
print num_valid, "values in range"
<span class="out">5 values in range</span>
</pre>

      <p>
        And if we want to count both at once,
        we can use <code>else</code>.
        The code it controls is executed when the code in the <code>if</code> <em>isn't</em>:
      </p>

<pre src="src/python/simple_else.py">
import sys
num_outliers = 0
num_valid = 0
for line in sys.stdin:
    value = float(line)
    if 0 &lt;= value &lt;= 5:
        num_valid = num_valid + 1
    else:
        num_outliers = num_outliers + 1
print num_valid, "in range and", num_outliers, "outliers"
<span class="out">5 in range and 2 outliers</span>
</pre>

      <div class="box">

        <h3>In-Place Operators</h3>

        <p>
          We have seen expressions like:
        </p>

<pre>
num_valid = num_valid + 1
</pre>

        <p class="continue">
          several times now.
          In Python and many other languages,
          we can simplify this by writing:
        </p>

<pre>
num_valid += 1
</pre>

        <p class="continue">
          which means,
          "Update the value on the left using addition with the value on the right."
          Similarly,
          we can also double values using <code>*=</code> like this:
        </p>

<pre>
something *= 2
</pre>

        <p class="continue">
          and so on for other binary (two-valued) operators.
          It may seem like a small saving,
          but it actually prevents a lot of bugs
          by eliminating duplicated code.
        </p>

      </div>

      <div class="keypoints" id="k:logic">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>if <em>test</em></code> to do something only when a condition is true.</li>
          <li>Use <code>else</code> to do something when a preceding <code>if</code> test is not true.</li>
          <li>The body of an <code>if</code> or <code>else</code> must be indented consistently.</li>
          <li>Combine tests using <code>and</code> and <code>or</code>.</li>
          <li>Use '&lt;', '&lt;=', '&gt;=', and '&gt;' to compare numbers or strings.</li>
          <li>Use '==' to test for equality and '!=' to test for inequality.</li>
          <li>Use <code><em>variable</em> += <em>expression</em></code> as a shorthand for <code><em>variable</em> = <em>variable</em> + <em>expression</em></code> (and similarly for other arithmetic operations).</li>
        </ul>
      </div>

    </section>

    <section id="s:flag">

      <h2>Flags</h2>

      <div class="understand" id="u:flag">
        <h3>Understand:</h3>
        <ul>
          <li>What Boolean values are.</li>
          <li>How to keep track of events using flag variables.</li>
        </ul>
      </div>

      <p>
        An expression like <code>value &lt; 0</code> produces one of two values
        called (unsurprisingly) <code>True</code> and <code>False</code>.
        These values can be assigned to variables like anything else:
      </p>

<pre>
x = 5
is_less_than = x &lt; 0
print is_less_than
<span class="out">False</span>
</pre>

      <p>
        It's very common to assign <code>True</code> and <code>False</code> to variables
        to keep track of whether some event has happened.
        For example,
        we could create a variable called <code>have_seen_dashed_line</code>
        to keep track of whether or not we have seen the dashed line that separates
        the header in a data file from the actual data.
        Its initial value will be <code>False</code>,
        because we obviously haven't seen the dashed line before we've read any input.
        As soon as we do see the dashed line,
        we set it to <code>True</code>:
      </p>

<pre>
import sys
have_seen_dashed_line = False
for line in data:
    if line.startswith('---'):
        have_seen_dashed_line = True
print 'Did we ever see the dashed line?', have_seen_dashed_line
<span class="out">True</span>
</pre>

      <p>
        A variable that is used this way is often called
        a <a href="glossary.html#flag">flag</a>.
        We can use the <code>have_seen_dashed_line</code> flag's value
        to decide whether or not to count a line as data:
      </p>

<pre>
import sys
have_seen_dashed_line = False
number = 0
for line in data:
    if line.startswith('---'):
        have_seen_dashed_line = True
    if have_seen_dashed_line:
        number = number + 1
print 'Number of data lines:', number
<span class="out">Number of data lines: 8</span>
</pre>

      <figure id="f:set_and_increment">
        <img src="img/python/set_and_increment.png" alt="Flagging and Incrementing" />
      </figure>

      <p>
        Whoops&mdash;that's almost right, but not quite.
        There are only 7 data lines in our file:
        why are we reporting 8?
        The reason is that when we see the dashed line,
        we set <code>have_seen_dashed_line</code> to <code>True</code>,
        then immediately check its value,
        see that it's true,
        and increment <code>number</code>
        (<a href="#f:set_and_increment">Figure XXX</a>).
        What we want to do is <em>either</em> set the flag
        (so that we'll start incrementing on the next iteration),
        <em>or</em> add one to <code>number</code>.
        Here's the fixed program:
      </p>

<pre>
import sys
have_seen_dashed_line = False
number = 0
for line in data:
    if line.startswith('---'):
        have_seen_dashed_line = True
    else:
        if have_seen_dashed_line:
            number = number + 1
print 'Number of data lines:', number
<span class="out">Number of data lines: 7</span>
</pre>

    <span class="comment"> JK: This is definitely a style question, but I would prefer to see
         the if line.startswith set the flag and then continue, and then the 
         second check of the flag remain its own if. That shows me that the 
         two conditions are not logically dependent, as in the first 
         necessarily must fail for the second to be evaluated. Tehnically, this
         is true here, but probably not in the spirit of the code. </span>

      <p>
        And here's a version that combines the second <code>if</code> with the <code>else</code>:
      </p>

<pre>
import sys
have_seen_dashed_line = False
number = 0
for line in data:
    if line.startswith('---'):
        have_seen_dashed_line = True
    elif have_seen_dashed_line:
        number = number + 1
print 'Number of data lines:', number
<span class="out">Number of data lines: 7</span>
</pre>

      <p class="continue">
        Organizing the <a href="glossary.html#branch">branches</a> of the <code>if</code> this way
        makes it clearer that exactly one will be executed.
      </p>

      <div class="keypoints" id="k:flag">
        <h3>Summary</h3>
        <ul>
          <li>The two Boolean values <code>True</code> and <code>False</code> can be assigned to variables like any other values.</li>
          <li>Programs often use Boolean values as flags to indicate whether something has happened yet or not.</li>
        </ul>
      </div>

    </section>

    <section id="s:parse">

      <h2>Reading Data Files</h2>

      <div class="understand" id="u:parse">
        <h3>Understand:</h3>
        <ul>
          <li>How to parse simple text files.</li>
        </ul>
      </div>

      <p>
        It's finally time to clean up Aurora's actual cochlear implant data files.
        Once again,
        these files typically look like this:
      </p>

<pre src="src/python/cochlear01.txt">
Subject: 1782
Date:    2012-05-21
Test     Run  Score
----     ---  -----
range    1    3
range    2    5
discrim  1    1
discrim  2    1
discrim  4    1.5
volume   1    3.5
volume   2    4.0
</pre>

      <p>
        We already have a program that ignores everything up to and including the dashed lines:
      </p>

<pre>
import sys
have_seen_dashed_line = False
number = 0
for line in data:
    if line.startswith('---'):
        have_seen_dashed_line = True
    elif have_seen_dashed_line:
        number = number + 1
print 'Number of data lines:', number
</pre>

      <p class="continue">
        Let's modify it to report scores that are outside the range 0&ndash;5.
        First,
        we need a way to break each line into columns.
        Luckily for us,
        strings know how to split themselves into fields:
      </p>

<pre>
&gt;&gt;&gt; typical_line = 'volume   2    4.0'
&gt;&gt;&gt; name, number, score = typical_line.split()
&gt;&gt;&gt; name
'volume'
&gt;&gt;&gt; number
'2'
&gt;&gt;&gt; score
'4.0'
</pre>

    <span class="comment"> JK: It becomes clear later that these lines should be placed in a file 
         called check.py - might want to say that here. </span>

      <p class="continue">
        The <code>string.split</code> returns as many new strings
        as there are whitespace-separated fields in the original string.
        In our case,
        there are three fields,
        so we can assign them result of <code>split</code> to three separate variables simultaneously.
        The third field,
        which we have put in the variable <code>score</code>,
        is a string;
        if we want its value as a floating-point number,
        we'll have to convert it using the <code>float</code> function.
        Combining this code with the program we already had,
        we get:
      </p>

<pre>
import sys
have_seen_dashed_line = False
for line in data:
    if line.startswith('---'):
        have_seen_dashed_line = True
    elif have_seen_dashed_line:
<span class="highlight">        name, number, score = line.split()
        score = float(score)</span>
</pre>

      <p>
        A simple <code>if</code> statement is the last piece of the puzzle:
      </p>

<pre>
import sys
have_seen_dashed_line = False
for line in data:
    if line.startswith('---'):
        have_seen_dashed_line = True
    elif have_seen_dashed_line:
        name, number, score = line.split()
        score = float(score)
        if (score &lt; 0.0) or (score &gt; 5.0):
            print 'Out of range:', name, number, score
</pre>

      <p>
        If we run this on our sample data file,
        it produces no output,
        because all the scores in the file are valid:
      </p>

<pre>
$ <span class="in">python check.py &lt; cochlear01.txt</span>
$
</pre>

      <p class="continue">
        But if we make some of the scores invalid,
        like this:
      </p>

<pre src="src/python/cochlear01.txt">
Subject: 1782
Date:    2012-05-21
Test     Run  Score
----     ---  -----
range    1    3
range    2    <span class="highlight">7.5</span>
discrim  1    1
discrim  2    1
discrim  4    1.5
volume   1    <span class="highlight">-3</span>
volume   2    4.0
</pre>

      <p class="continue">
        then the output changes to:
      </p>

<pre>
<span class="out">Out of range: range 2 7.5
Out of range: volume 1 -3.0</span>
</pre>

      <p class="continue">
        which is what we wanted.
      </p>

      <div class="keypoints" id="k:parse">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>str.split()</code> to split a string into pieces on whitespace.</li>
          <li>Values can be assigned to any number of variables at once.</li>
        </ul>
      </div>

    </section>

    <section id="s:provenance">

      <h2>Provenance Revisited</h2>

      <div class="understand" id="u:provenance">
        <h3>Understand:</h3>
        <ul>
          <li>How programs can add provenance to files.</li>
          <li>How programs can carry provenance forward.</li>
        </ul>
      </div>

      <p>
        As we said near the end of <a href="svn.html#provenance">the previous chapter</a>,
        if we put a string like:
      </p>

<pre>
$Revision: ...$
</pre>

      <p class="continue">
        in a file,
        Subversion can automatically update it
        each time we commit a change to that file.
        Let's add put <code>$Revision:$</code> in our program:
      </p>

<pre>
import sys
<span class="highlight">my_version = '$Revision: 143$'</span>
<span class="highlight">'Processed by check.py:', my_version</span>
have_seen_dashed_line = False
for line in data:
    if line.startswith('---'):
        have_seen_dashed_line = True
    elif have_seen_dashed_line:
        name, number, score = line.split()
        score = float(score)
        if (score &lt; 0.0) or (score &gt; 5.0):
            print 'Out of range:', name, number, score
<span class="out">Processed by check.py: $Revision: 143$
Out of range: range 2 7.5
Out of range: volume 1 -3.0</span>
</pre>

      <p>
        This is kind of handy:
        our output now automatically includes a description of who produced it&mdash;<em>exactly</em> who,
        i.e.,
        not just the name of the program,
        but also which version.
        To see why this is useful,
        let's rewrite the program so that it clips scores to lie inside 0&ndash;5
        instead of just reporting outlying values:
      </p>

<pre>
import sys
my_version = '$Revision: 143$'
'Processed by clip.py:', my_version
have_seen_dashed_line = False
for line in data:

    if have_seen_dashed_line:
        name, number, score = line.split()
        score = float(score)
        if score &lt; 0.0:
            print 0.0
        elif score &gt; 5.0:
            print 5.0
        else:
            print score

    else:
        print line.rstrip()
        if line.startswith('---'):
            have_seen_dashed_line = True
</pre>

      <div class="box">

        <h3>Ordering</h3>

        <p>
          Note that this version checked the <code>have_seen_dashed_line</code> flag first,
          then handles the case where the flag isn't yet true.
          Some people find this ordering easier to understand,
          because the "main" case that handles actual data comes first.
          Others prefer the original,
          arguing that the cases should appear in the order in which
          we expect the data to occur.
          It doesn't matter which we use,
          as long as we're consistent with our other loops.
        </p>

      </div>

      <p>
        When we run this program on the data that has invalid scores, it prints:
      </p>

<pre>
<span class="out"><span class="highlight">Processed by clip.py: $Revision: 143$</span>
Subject: 1782
Date:    2012-05-21
Test     Run  Score
----     ---  -----
range    1    3
<span class="highlight">range    2    5.0</span>
discrim  1    1
discrim  2    1
discrim  4    1.5
<span class="highlight">volume   1    0.0</span>
volume   2    4.0</span>
</pre>

      <p>
        The three most important lines are highlighted.
        Two of them&mdash;the data lines&mdash;have been cleaned up;
        the line at the very top tells us who did the cleaning up.
        This is another step in our march toward having a real data provenance system:
        now,
        if we discover a bug in a program,
        we can look at our files and see which ones had been processed by that program.
        As we'll see in the <a href="funclib.html">next chapter</a>,
        we can extend this further to carry provenance information forward through an entire pipeline.
      </p>

      <div class="keypoints" id="k:provenance">
        <h3>Summary</h3>
        <ul>
          <li idea="paranoia">Put version numbers in programs' output to establish provenance for data.</li>
        </ul>
      </div>

    </section>

    <section id="s:lists">

      <h2>Lists</h2>

      <div class="understand" id="u:lists">
        <h3>Understand:</h3>
        <ul>
          <li>How to store many related values in a list.</li>
          <li>How to use a loop to operate on the values in a list.</li>
          <li>That programs should be tested on small, simple cases.</li>
        </ul>
      </div>

      <p>
        To start our exploration of lists,
        let's run an interpreter and try this:
      </p>

<pre src="src/python/sum_values.py">
&gt;&gt;&gt; <span class="in">data = [1, 3, 5]</span>
&gt;&gt;&gt; <span class="in">for value in data:</span>
... <span class="in">    print value</span>
...
<span class="out">1
3
5</span>
</pre>

      <p>
        <code>[1, 3, 5]</code> is a <a href="glossary.html#list">list</a>:
        a single object that stores multiple values
        (<a href="#f:simple_list">Figure XXX</a>).
        Just as a <code>for</code> loop over an open file
        reads lines from that file one by one
        and assigns them to the loop variable,
        a <code>for</code> loop over a list assigns each value in the list
        to the loop variable in turn.
      </p>

      <figure id="f:simple_list">
        <img src="img/python/simple_list.png" alt="A Simple List" />
      </figure>

      <p>
        Let's do something a bit more useful:
      </p>

<pre src="src/python/first_mean.py">
data = [1, 4, 2, 3, 3, 4, 3, 4, 1]
total = 0
for n in data:
    total += n
mean = total / len(data)
print "mean is", mean
<span class="out">mean is 2</span>
</pre>

      <p class="continue">
        This loop adds each value in the list to <code>total</code>.
        Once the loop is over,
        we divide <code>total</code> by the length of the list,
        which we find using the built-in function <code>len</code>.
      </p>

      <p>
        Unfortunately,
        the result in the example above is wrong:
        The total of the numbers in the list is 25,
        but we're printing 2 instead of 25/9
        (which is 2.7777&hellip;).
        The problem once again is that we're dividing one integer by another,
        which throws away the remainder.
        We can fix this by initializing <code>total</code> to 0.0
        (so that all the additions involve a floating-point number and an integer,
        which produces a floating-point number),
        or by using the <code>float</code> function to do the conversion explicitly:
      </p>

<pre src="src/python/second_mean.py">
data = [1, 4, 2, 3, 3, 4, 3, 4, 1]
total = 0
for n in data:
    total += n
mean = <span class="highlight">float(total)</span> / len(data)
print "mean is", mean
<span class="out">mean is 2.77777777778</span>
</pre>

      <p>
        The <em>real</em> problem isn't a matter of integers versus floats, though.
        The real problem with this program is that
        we didn't know whether the answer was right or wrong,
        so we couldn't tell if the program was correct or not.
        After all,
        the average of these nine numbers might well have been 2.
      </p>

      <p>
        The fact that a program runs without crashing doesn't mean it's correct.
        One way to make programs easier to check
        is to run them on smaller or more regular data.
        For example,
        If we ran the program on <code>[1, 4]</code>,
        we'd probably notice that we were getting 2 instead of 2.5.
        Writing programs so that they're checkable is another idea
        that we'll explore in detail <a href="quality.html">later</a>.
      </p>

      <div class="box">

        <h3>Even Simpler</h3>

        <p>
          Python actually has a built-in function called <code>sum</code>,
          so we can get rid of the loop entirely:
        </p>

<pre src="src/python/loopless.py">
total = sum(data)
print "mean is", float(total) / len(data)
</pre>

        <p class="continue">
          and shorten this even further by calling <code>float</code>
          directly on the result of <code>sum</code>:
        </p>

<pre src="src/python/one_liner.py">
print "mean is", float(sum(data)) / len(data)
</pre>

        <p>
          <code>float(sum(data))</code> is like <em>sin(log(x))</em>:
          the inner function is evaluated first,
          and its result is used as the input to the outer function.
          It's important to get the parentheses in the right place,
          since the expressions:
        </p>

<pre src="src/python/one_liner.py">
float(sum(data)) / len(data)
</pre>

        <p class="continue">
          and
        </p>

<pre src="src/python/incorrect_one_liner.py">
float(sum(data) / len(data))
</pre>

        <p class="continue">
          calculate different things.
          In the first,
          <code>float</code> is applied to <code>sum(data)</code>,
          i.e.,
          Python adds up all the numbers,
          then converts the result to a floating-point value
          before dividing by <code>len(data)</code>
          to get the mean.
        </p>

        <p>
          In the second,
          Python adds up the numbers,
          divides by <code>len(data)</code> to get an integer result,
          and then converts that integer to a floating point number.
          This is just our original bug in a more compact form.
          Once again,
          the only way to guard against it is to test the program.
        </p>

      </div>

      <div class="keypoints" id="k:lists">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>[<em>value</em>, <em>value</em>, ...]</code> to create a list of values.</li>
          <li><code>for</code> loops process the elements of a list, in order.</li>
          <li><code>len(<em>list</em>)</code> returns the length of a list.</li>
          <li><code>[]</code> is an empty list with no values.</li>
        </ul>
      </div>

    </section>

    <section id="s:morelist">

      <h2>More About Lists</h2>

      <div class="understand" id="u:morelist">
        <h3>Understand:</h3>
        <ul>
          <li>That lists can be modified in place.</li>
          <li>How to access arbitrary elements in a list.</li>
          <li>What an out-of-bounds error is.</li>
          <li>How to generate a list of legal indices for a list.</li>
          <li>When to use short or long variable names.</li>
        </ul>
      </div>

      <p>
        Lists (and their equivalents in other languages)
        are used more than any other data structure,
        so let's have a closer look at them.
        First,
        lists are <a href="glossary.html#mutable">mutable</a>,
        i.e.,
        they can be changed after they are created:
      </p>

<pre src="src/python/appending.py">
data = [1, 4, 2, 3]
result = []
current = 0
for n in data:
    current = current + n
    result.append(current)
print "running total:", result
<span class="out">[1, 5, 7, 10]</span>
</pre>

      <p class="continue">
        <code>result</code> starts off as an <a href="glossary.html#empty-list">empty list</a>,
        and <code>current</code> starts off as zero
        (<a href="#f:running_total">Figure XXX</a>).
        Each time the loop executes&mdash;i.e.,
        for each number in <code>values</code>&mdash;Python
        adds the next value in the list to <code>current</code>
        to calculate the running total.
        It then append this value to <code>result</code>,
        so that when the program finishes,
        we have a complete list of partial sums.
      </p>

      <figure id="f:running_total">
        <img src="img/python/running_total.png" alt="Running Total" />
      </figure>

      <p>
        What if we want to double the values in <code>data</code> in place?
        We could try this:
      </p>

<pre src="src/python/incorrect_doubling_in_place.py">
data = [1, 4, 2, 3]
for n in data:
    n = 2 * n
print "doubled data is:", data
<span class="out">doubled data is [1, 4, 2, 3]</span>
</pre>

      <p class="continue">
        but as we can see,
        it doesn't work.
        When Python calculates <code>2*n</code>,
        it creates a new value in memory
        (<a href="#f:doubling_list">Figure XXX</a>).
        It then makes the variable <code>n</code> point at the value for a few microseconds
        before going around the loop again
        and pointing <code>n</code> at the next value from the list instead.
        Since nothing is pointing to the temporary value we just created any longer,
        Python throws it away.
      </p>

      <figure id="f:doubling_list">
        <img src="img/python/doubling_list.png" alt="Failed Attempt to Double Values in a List" />
      </figure>

      <p>
        The solution to our problem is to <a href="glossary.html#list-indexing">index</a> the list,
        which is just like subscripting a vector in mathematics.
        Here are some examples:
      </p>

<pre src="src/python/modify_list.py">
scientists = ["Newton", "Darwing", "Turing"]
print "length:", len(scientists)
<span class="out">length: 3</span>
print "first element:", scientists[0]
<span class="out">first element: Newton</span>
print "second element:", scientists[1]
<span class="out">second element: Darwing</span>
print "third element:", scientists[2]
<span class="out">third element: Turing</span>
</pre>

      <div class="box">

        <h3>It Seemed Like a Good Idea at the Time</h3>

    <span class="comment"> JK: Harsh! ;-) Having spent a lot of time in Matlab and R before 
         coming over to Python, I personally find indexing by 0 (combined with 
         Python's overall indexing syntax) to be preferable, as it helps me
         avoid off-by-one errors and gives the (to me) obvious answer for
         list = [0,1,2,3,4], len(list[0:3]) or len(list[1:4]) >>> 3, not 4. </span>

        <p>
          For reasons that made sense in 1970,
          when the C programming language was invented,
          Python lists are indexed from 0 to N-1 rather than 1 to N.
          C++, C#, Java, and other languages that imitate C also use 0 to N-1,
          while Fortran, Pascal, MATLAB,
          and other languages that imitate human beings use 1 to N.
        </p>

      </div>

      <p>
        How does indexing help us?
        Well,
        after noticing that we have misspelled Darwin's name as "Darwing",
        we can fix it by assigning a new value to that location in the list:
      </p>

<pre src="src/python/modify_list_continued.py">
scientists[1] = "Darwin"
print scientists
<span class="out">["Newton", "Darwin", "Turing"]</span>
</pre>

      <p class="continue">
        <a href="#f:update_list">Figure XXX</a> shows
        the list before and after the change.
        Again,
        once we've made the update,
        nothing is pointing to the string "Darwing" with a "g" on the end,
        so the memory it's using is recycled.
      </p>

      <figure id="f:update_list">
        <img src="img/python/update_list.png" alt="Successfully Doubling Values in a List" />
      </figure>

      <p>
        In order for Python to give us a sensible value,
        the index we provide for a list must be in range,
        i.e.,
        between 0 and one less than the length of the list.
        If it's too large,
        we get an error message:
      </p>

<pre src="src/python/list_out_of_range.py">
scientists = ["Newton", "Darwin", "Turing"]
print scientists[55]
<span class="err">Traceback (most recent call last):
  File "list-04.py", line 2, in &lt;module&gt;
    print "out of range:", scientists[55]
IndexError: list index out of range</span>
</pre>

      <p class="continue">
        The error message doesn't appear
        until Python actually tries to fetch the out-of-bounds value.
        If this is in the middle of some other operation,
        we may see some partial output before our error message:
      </p>

<pre src="src/python/list_out_of_range_partial.py">
scientists = ["Newton", "Darwin", "Turing"]
print "out of range:", scientists[55]
<span class="out">out of range:</span>
<span class="err">Traceback (most recent call last):
  File "list-04.py", line 2, in &lt;module&gt;
    print "out of range:", scientists[55]
IndexError: list index out of range</span>
</pre>

      <p>
        And here's something else that's useful.
        In Python (but <em>not</em> in most other languages),
        negative indices count backward from the end of a list:
      </p>

<pre src="src/python/list_negative_indexing.py">
scientists = ["Newton", "Darwin", "Turing"]
print "last:", scientists[-1]
print "penultimate:", scientists[-2]
<span class="out">last: Turing
penultimate: Darwin</span>
</pre>

      <p class="continue">
        It's a lot easier to type <code>scientists[-1]</code>
        than <code>scientists[len(scientists)-1]</code>
        to get the last item in a list,
        but it does take some getting used to.
      </p>

      <p>
        Now, back to our original problem of doubling values in place.
        We now know that we can do this:
      </p>

<pre src="src/python/explicit_doubling.py">
data = [1, 4, 2]
data[0] = 2 * data[0]
data[1] = 2 * data[1]
data[2] = 2 * data[2]
print "doubled data is:", data
<span class="out">doubled data is [2, 8, 4]</span>
</pre>

      <p class="continue">
        but it clearly doesn't scale:
        we're not going to write a million statements
        to update a list of a million values.
        We need to use a loop,
        but instead of looping over the values in the list,
        we want to loop over the allowed indices of the list.
        To do this,
        we will rely on a function called <code>range</code>
        which creates a list of the first N integers:
      </p>

<pre src="src/python/range_5.py">
print range(5)
<span class="out">[0, 1, 2, 3, 4]</span>
</pre>

      <p>
        Once again,
        the values go from 0 to one less than the number given to <code>range</code>,
        which just happens to be exactly the indices of a list of that length.
        Let's try it out:
      </p>

<pre src="src/python/range_loop.py">
data = [1, 4, 2]
indices = range(3)
for i in indices:
    print i, data[i]
<span class="out">0 1
1 4
2 2</span>
</pre>

      <p class="continue">
        then fold the call to <code>range</code> into the loop:
      </p>

<pre src="src/python/range_loop_2.py">
data = [1, 4, 2]
for i in <span class="highlight">range(3)</span>:
    print i, data[i]
<span class="out">0 1
1 4
2 2</span>
</pre>

      <p>
        This program is correct, but fragile:
        if we add more values to the list,
        Python will still only execute the loop three times,
        so we'll still only print the first three values in the list:
      </p>

<pre src="src/python/incorrect_range_loop.py">
data = [1, 4, 2<span class="highlight">, 5, 1, 3</span>]
for i in range(3):
    print i, data[i]
<span class="out">0 1
1 4
2 2</span>
</pre>

      <p>
        What we want is for the loop to automatically adjust itself
        based on the length of the list:
      </p>

<pre src="src/python/data_length_loop.py">
data = [1, 4, 2, 5, 1, 3]
<span class="highlight">data_length = len(data)</span>
for i in range(<span class="highlight">data_length</span>):
    print i, data[i]
<span class="out">0 1
1 4
2 2
3 5
4 1
5 3</span>
</pre>

      <p>
        We can get rid of the variable <code>data_length</code>
        by putting the call to <code>len(data)</code>
        inside the call to <code>range</code>:
      </p>

<pre src="src/python/idiomatic_range_loop.py">
data = [1, 4, 2, 5, 1, 3]
for i in range(<span class="highlight">len(data)</span>):
    print i, data[i]
<span class="out">0 1
1 4
2 2
3 5
4 1
5 3</span>
</pre>

      <p class="continue">
        Again,
        <code>range(len(data))</code> is like <em>sin(log(x))</em>:
        the inner function is evaluated first,
        and its result becomes the input to the outer function.
        Put together like this,
        they are a common <a href="glossary.html#idiom">idiom</a> in Python,
        i.e.,
        a way of saying something that everyone recognizes and uses.
        When an experienced programmer sees:
      </p>

<pre>
for i in range(len(something)):
</pre>

      <p class="continue">
        what she "hears" is:
      </p>

<pre>
for each legal index of something:
</pre>

      <p>
        The reason this idiom is better than what we started with is that
        there is no duplicated information.
        Instead of having a list of length 3,
        and looping from 0 up to 3,
        we have a list of any length whatever,
        and loop from 0 up to that length.
        In general,
        anything that is repeated two or more times in a program
        will eventually be wrong in at least one.
        Putting it another way,
        any piece of information should appear exactly once in a program,
        so that if it needs to change,
        it only needs to be changed in one place.
      </p>

      <div class="box">

        <h3>Short and Long Variable Names</h3>

        <p>
          We have said several times that programs should use meaningful variable names.
          Are we not violating our own rule by using <code>i</code> as a variable in this program?
          The short answer is "yes", but it's a defensible violation.
          Suppose we re-write our loop as:
        </p>

<pre>
data = [1, 4, 2, 5, 1, 3]
for location in range(len(data)):
    print location, data[location]
</pre>

        <p class="continue">
          The longer name are more meaningful,
          but it also takes longer to read.
          Since the original <code>i</code> is only used for a few lines,
          users will easily be able to keep its meaning in short-term memory
          as long as they need to.
          On balance,
          therefore,
          the short name are better in this case.
        </p>

        <p>
          This is actually a general principle in program design.
          A variable that holds a simple value,
          and is only used in a few adjacent lines of code,
          can (and usually should) have a short name.
          A variable that holds a complex value,
          or one which is used over more than a few lines of code,
          should have a longer name
          in order to optimize the tradeoff between reading speed
          and the limitations of human short-term memory.
        </p>

      </div>

    <span class="comment"> JK: Also, to hearken back to the previous paragraph, the use of i as a 
         counter in a for loop is arguably another common idiom that 
         experienced programmers will recognize right away as a counter. At 
         least if they're not also mathematicians who read it as an imaginary 
         number... </span>

      <p>
        Let's finally go back and double the values in place:
      </p>

<pre src="src/python/doubling_in_place.py">
data = [1, 4, 2, 5, 3, 4, 5]
for i in range(len(data)):
    data[i] = 2 * data[i]
print data
<span class="out">[2, 8, 4, 10, 6, 8, 10]</span>
</pre>

      <div class="box">

        <h3>Left and Right</h3>

        <p>
          Seeing the expression <em>x = 2x</em>,
          most mathematicians would say,
          "Right&mdash;so <em>x</em> is zero."
          Seeing the same expression,
          most programmers would say,
          "Right&mdash;you're doubling the value of <em>x</em>."
          <a href="#f:double_in_place">Figure XXX</a> shows
          how that actually works:
        </p>

        <ol>

          <li>
            Python reads the current value of <code>x</code> from memory.
          </li>

          <li>
            It multiplies that value by 2,
            storing the result in a temporary location&hellip;
          </li>

          <li>
            &hellip;and then modifies <code>x</code> to point at the new value.
          </li>

        </ol>

        <figure id="f:double_in_place">
          <img src="img/python/double_in_place.png" alt="Doubling in Place" />
        </figure>

        <p>
          Now look at what happens when Python execute the statements:
        </p>

<pre>
x = 5
y = x
x = 2 * x
</pre>

        <ol>

          <li>
            The variable <code>x</code> is created,
            and set to point at the value 5
            (<a href="#f:new_values_for_variables">Figure XXX</a>).
          </li>

          <li>
            The variable <code>y</code> is created,
            and set to point at the same value.
          </li>

          <li>
            The value 10 (i.e., 2&times;5) is created and stored in a temporary location.
          </li>

          <li>
            <code>x</code> is altered to point at that value.
          </li>

        </ol>

        <figure id="f:new_values_for_variables">
          <img src="img/python/new_values_for_variables.png" alt="New Values for Variables" />
        </figure>

        <p>
          After these operations are complete,
          <code>y</code> is left pointing at the original value, 5.
          It does <em>not</em> point at the same thing <code>x</code> does any longer,
          and its value is <em>not</em> automatically recalculated
          to keep it twice the value of <code>x</code>.
        </p>

      </div>

      <div class="keypoints" id="k:morelist">
        <h3>Summary</h3>
        <ul>
          <li>Lists are mutable: they can be changed in place.</li>
          <li>Use <code><em>list</em>.append(<em>value</em>)</code> to append something to the end of a list.</li>
          <li>Use <code><em>list</em>[<em>index</em>]</code> to access a list element by location.</li>
          <li>The index of the first element of a list is 0; the index of the last element is <code>len(<em>list</em>)-1</code>.</li>
          <li>Negative indices count backward from the end of the list, so <code><em>list</em>[-1]</code> is the last element.</li>
          <li>Trying to access an element with an out-of-bounds index is an error.</li>
          <li><code>range(<em>number</em>)</code> produces the list of numbers <code>[0, 1, ..., <em>number</em>-1]</code>.</li>
          <li><code>range(len(<em>list</em>))</code> produces the list of legal indices for <code><em>list</em></code>.</li>
        </ul>
      </div>

    </section>

    <section id="s:nestloop">

      <h2>Nesting Loops</h2>

      <div class="understand" id="u:nestloop">
        <h3>Understand:</h3>
        <ul>
          <li>That loops can be nested to operate on combinations of items.</li>
          <li>That the range of inner loops can depend on the state of outer loops.</li>
          <li>That doing this allows programs to handle more cases without changes.</li>
        </ul>
      </div>

      <p>
        Going back to Aurora's data cleanup problem,
        suppose that the scores in each data set
        are always supposed to ramp upward:
        if we ever see a value that's less than the value before it,
        something's gong wrong.
        Here's a program that tries to check that
        (again, using inline data instead of reading from a file
        to make the sample code clearer):
      </p>

<pre src="src/python/incorrect_upward_check.py">
data = [1, 2, 2, 3, 4, 4, 5, 6, 5, 6, 7, 7, 8]
for i in range(len(data)):
    if data[i] &lt; data[i-1]:
        print "failure at index:", i
    i = i + 1
<span class="out">failure at index: 0
failure at index: 8</span>
</pre>

      <p class="continue">
        Whoops&mdash;why is it telling us that there's a failure at index 0?
        Take a close look at the third line:
        when <code>i</code> is 0,
        it compares <code>data[0]</code> to <code>data[-1]</code>,
        but as we said earlier,
        index -1 means the last element of the list.
        We need to make sure that we only compare the <em>second</em> and higher elements
        to the ones before them:
      </p>

<pre src="src/python/correct_upward_check.py">
data = [1, 2, 2, 3, 4, 4, 5, 6, 5, 6, 7, 7, 8]
for i in <span class="highlight">range(1, len(data))</span>:
    if data[i] &lt; data[i-1]:
        print "failure at index:", i
    i = i + 1
<span class="out">failure at index: 8</span>
</pre>

      <p class="continue">
        This program uses the fact that <code>range(low, high)</code>
        generates the values from <code>low</code> to <code>high-1</code>.
        We can also use <code>range(low, high, stride)</code>
        to generate values that are spaced <code>stride</code> apart,
        so that <code>range(5, 20, 3)</code> produces
        <code>[5, 8, 11, 14, 17]</code>.
        (Remember,
        <code>range</code> goes up to but not including the top value.)
      </p>

    <span class="comment"> JK: I like the data smoothing example, but, just to stay in character, 
         it's unclear how it relates to Aurora's problem exactly? There wasn't 
         anything set up in her problem statement related to consecutive data, 
         or smoothing. Later on, this is referred to as "Aurora's data 
         smoothing". </span>

      <p>
        Now suppose that we need to add up successive triples of our data
        to smooth out the scores.
        Our first try steps through the indices three at a time:
      </p>

<pre src="src/python/a_step_too_far.py">
data = [1, 2, 2, 3, 4, 4, 5, 6, 5, 6, 7, 7, 8]
result = []
for i in range(0, len(data), 3):
    sum = data[i] + data[i+1] + data[i+2]
    result.append(sum)
print "grouped data:", result
<span class="err">Traceback (most recent call last):
  File "group-by-threes-fails.py", line 6, in &lt;module&gt;
    sum = data[i] + data[i+1] + data[i+2]
IndexError: list index out of range</span>
</pre>

      <p class="continue">
        It's not immediately obvious what's wrong,
        but a bit of experimenting with shorter lists turns up the problem.
        If the number of elements in the list isn't exactly divisible by 3,
        our program is going to try to reach past the end of the list.
        For example,
        if we have a 4-element list,
        we will add up the values at locations 0, 1, and 2,
        then try to add up the values at locations 3, 4, and 5,
        but locations 4 and 5 aren't valid
        (<a href="#f:a_step_too_far">Figure XXX</a>).
      </p>

      <figure id="f:a_step_too_far">
        <img src="img/python/a_step_too_far.png" alt="A Step Too Far" />
      </figure>

      <p>
        How we should fix this is a question for a scientist
        (or at least a statistician).
        Should we throw away the top few values if there aren't enough to make another triple,
        or add up as many as there are and hope for the best?
        Let's assume the latter for now:
      </p>

<pre src="src/python/awkward_smoothing.py">
data = [1, 2, 2, 3, 4, 4, 5, 6, 5, 6, 7, 7, 8]
result = []
for i in range(0, len(data), 3):
    sum = data[i]
    if (i+1) &lt; len(data):
        sum += data[i+1]
    if (i+2) &lt; len(data):
        sum += data[i+2]
    result.append(sum)
print "grouped data:", result
<span class="out">grouped data: [5, 11, 16, 20, 8]</span>
</pre>

      <p>
        This works,
        but it feels clumsy:
        if we were adding up in groups of ten,
        we'd have a lot of <code>if</code> statements.
        We need a better way.
      </p>

      <p>
        Our first step toward that better way looks like this:
      </p>

<pre src="src/python/simple_nested_loop.py">
vowels = "ae"
consonants = "dnx"
for v in vowels:
    for c in consonants:
        print v + c
<span class="out">ad
an
ax
ed
en
ex</span>
</pre>

      <p>
        <a href="#f:nested_flowchart">Figure XXX</a> shows
        what's going on in this <a href="glossary.html#nested-loop">nested loop</a>.
        Each time the <a href="glossary.html#outer-loop">outer loop</a> executes,
        Python runs the entire <a href="glossary.html#inner-loop">inner loop</a>.
        The innermost <code>print</code> statement therefore executes six times,
        because the outer loop runs twice,
        and the inner loop runs three times for each of those iterations.
      </p>

      <figure id="f:nested_flowchart">
        <img src="img/python/nested_flowchart.png" alt="Nested Loops" />
      </figure>

      <p>
        In this case,
        both loops execute a fixed number of times,
        but that doesn't have to be the case.
        It's common,
        for example,
        to set the number of times an inner loop runs
        based on the current value of the outer loop's counter:
      </p>

<pre src="src/python/triangle_nested_loop.py">
for i in range(4):
    for j in range(i):
        print i, j
<span class="out">1 0
2 0
2 1
3 0
3 1
3 2</span>
</pre>

      <figure id="f:triangle_nested_loop">
        <img src="img/python/triangle_nested_loop.png" alt="Nested Loop Execution" />
      </figure>

      <p>
        <a href="#f:triangle_nested_loop">Figure XXX</a> traces
        this little program's execution.
        The first time through,
        <code>i</code> is 0.
        Since <code>range(0)</code> is the empty list <code>[]</code>,
        the inner loop is effectively:
      </p>

<pre>
    for j in []:
        print i, j
</pre>

      <p class="continue">
        so it doesn't execute at all.
        The next time,
        though,
        when <code>i</code> is 1,
        the inner loop is effectively:
      </p>

<pre>
    for j in [0]:
        print i, j
</pre>

      <p class="continue">
        so the innermost <code>print</code> statement is executed once
        with <code>i</code> equal to 1 and <code>j</code> equal to 0.
        The third time around the outer loop,
        <code>i</code> is 2,
        so <code>range(i)</code> is <code>[0, 1]</code>.
        This makes the inner loop execute twice,
        and so on.
      </p>

      <p>
        Now let's go back to Aurora's data smoothing.
        We can step through the data in threes like this:
      </p>

<pre>
for i in range(0, len(data), 3):
    ...body of loop...
</pre>

      <p>
        If we know that the length of a list is an exact multiple of three,
        we can always loop from index <code>i</code>
        up to (but not including) <code>i+3</code>:
      </p>

<pre>
for i in range(0, len(data), 3):
    for j in range(i, i+3):
        ...body of loop...
</pre>

      <p>
        If the list isn't long enough for us to do this,
        we want to go as high as
        the least of <code>i+3</code> and <code>len(data)</code>.
        Using Python's built-in <code>min</code> function,
        this is:
      </p>

<pre>
min(i+3, len(data))
</pre>

      <p class="continue">
        so we can write our inner loop as:
      </p>

<pre>
for i in range(0, len(data), 3):
    upper_bound = min(i+3, len(data))
    for j in range(i, upper_bound):
        ...smooth data...
</pre>

      <p>
        Here's the completed data smoothing program:
      </p>

<pre src="src/python/data_smoothing.py">
data = [1, 2, 2, 3, 4, 4, 5, 6, 5, 6, 7, 7, 8]
result = []
for i in range(0, len(data), 3):
    upper_bound = min(i+3, len(data))
    sum = 0
    for j in range(i, upper_bound):
        sum += data[j]
    result.append(sum)
print "grouped data:", result
<span class="out">grouped data: [5, 11, 16, 20, 8]</span>
</pre>

      <p>
        This program works,
        but there's room for improvement.
        If we ever want to change the smoothing interval,
        we have to replace the number 3 in two places.
        If we put that value in a variable <code>width</code>,
        we'll only need to change it once:
      </p>

<pre src="src/python/data_smoothing_generalized.py">
data = [1, 2, 2, 3, 4, 4, 5, 6, 5, 6, 7, 7, 8]
<span class="highlight">width = 3</span>
result = []
for i in range(0, len(data), <span class="highlight">width</span>):
    upper_bound = min(i+<span class="highlight">width</span>, len(data))
    sum = 0
    for j in range(i, upper_bound):
        sum += data[j]
    result.append(sum)
print "grouped data:", result
<span class="out">grouped data: [5, 11, 16, 20, 8]</span>
</pre>

      <p>
        This change also tells readers
        (including our future selves)
        that the stride in the outer loop,
        and the offset used to calculate <code>upper_bound</code>,
        are always supposed to be the same.
        That's yet another reason to use variables with meaningful names:
        it tells people when values are intentionally the same,
        as opposed to accidentally the same.
      </p>

      <div class="keypoints" id="k:nestloop">
        <h3>Summary</h3>
        <ul>
          <li><code>range(<em>start</em>, <em>end</em>)</code> creates the list of numbers from <code><em>start</em></code> up to, but not including, <code><em>end</em></code>.</li>
          <li><code>range(<em>start</em>, <em>end</em>, <em>stride</em>)</code> creates the list of numbers from <code><em>start</em></code> up to <code><em>end</em></code> in steps of <code><em>stride</em></code>.</li>
          <li>Use nested loops to do things for combinations of things.</li>
          <li>Make the range of the inner loop depend on the state of the outer loop to automatically adjust how much data is processed.</li>
          <li>Use <code>min(...)</code> and <code>max(...)</code> to find the minimum and maximum of any number of values.</li>
        </ul>
      </div>

    </section>

    <section id="s:nestlist">

      <h2>Nesting Lists</h2>

      <div class="understand" id="u:nestlist">
        <h3>Understand:</h3>
        <ul>
          <li>That lists can contain other lists.</li>
          <li>That nested lists are a common way to represent regular (tabular) data.</li>
        </ul>
      </div>

      <p>
        One of the hearing tests Aurora uses
        asks people to point out where a sound is coming from.
        The data files contain lists of XY coordinates:
      </p>

<pre>
4.2 1.7
3.1 5.0
0.8 6.1
... ...
</pre>

      <p>
        She has roughly 100 such files,
        and one more file (in the same format)
        that holds the actual location of each sound.
        She wants to calculate the average distance between
        each actual and reported location.
      </p>

      <p>
        The first step is to read a file
        and extract the XY values on each line:
      </p>

<pre src="src/python/read_separate_xy.py">
x_values = []
y_values = []
reader = file('data.txt', 'r')
for line in reader:
    x, y = line.split()
    x = float(x)
    x_values.append(x)
    y = float(y)
    y_values.append(y)
reader.close()
</pre>

      <p>
        We can make this a bit more readable
        by combining the calls to <code>float</code> and <code>append</code>:
      </p>

<pre src="src/python/read_separate_xy_combined.py">
x_values = []
y_values = []
reader = file('data.txt', 'r')
for line in reader:
    x, y = line.split()
    x_values.append(float(x))
    y_values.append(float(y))
reader.close()
</pre>

      <p class="continue">
        but the basic approach is still unwieldy.
        What we really want is a list of XY coordinates,
        not two parallel lists of X and Y coordinates.
        We can easily create what we want
        using <a id="g:nested-list" href="glossary.html#nested-list">nested list</a>.
        <a href="#f:simple_nested_list">Figure XXX</a> shows
        what we're going to do,
        and the code below shows
        how we would create a nested list by hand
        for specific XY values:
      </p>

    <span class="comment"> JK: Tuples? I'm just thinking of this now, because I would normally 
         treat x, y as a tuple (no particular reason, just force of habit) 
         presuming that x and y didn't need to change later. I see the argument 
         for using lists throughout here, but maybe a box that just mentions 
         that tuples exist, they work like lists (in this context) except that
         the values they contain can't be changed, and that they come up in  
         other people's programs? </span>

<pre src="src/python/nested_list_explicit.py">
&gt;&gt;&gt; <span class="in">coordinates = [ [4.2, 1.7], [3.1, 5.0], [0.8, 6.1] ]</span>
&gt;&gt;&gt; <span class="in">print coordinates[0]</span>
<span class="out">[4.2, 1.7]</span>
&gt;&gt;&gt; <span class="in">print coordinates[0][1]</span>
<span class="out">1.7</span>
</pre>

      <figure id="f:simple_nested_list">
        <img src="img/python/simple_nested_list.py" alt="A Simple Nested List" />
      </figure>

      <p>
        This isn't as complicated as it first looks.
        Just as a variable can point at any object,
        so too can any entry in a list.
        And since a list is just an object in memory,
        one list can contain a reference to another.
        This is why <code>coordinates[0]</code> is <code>[4.2, 1.7]</code>:
        the first entry of the outer list is
        a reference to an entire sublist.
        We could just as easily write:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">temp = coordinates[0]</span>
&gt;&gt;&gt; <span class="in">print temp</span>
<span class="out">[4.2, 1.7]</span>
</pre>

      <p class="continue">
        And since <code>x[1]</code> is 4.2,
        so too is <code>coordinates[0][1]</code>:
        the first subscript select the sublist,
        while the second selects an element from that sublist
        (<a href="#f:indexing_nested_lists">Figure XXX</a>).
      </p>

      <figure id="f:indexing_nested_lists">
        <img src="img/python/indexing_nested_lists.png" alt="Indexing Nested Lists" />
      </figure>

      <p>
        It's important to understand that the inner list isn't "in" the outer list:
        what the outer list contains is a reference to the inner one.
        We'll return to this <a href="#s:alias">later</a>.
      </p>

      <p>
        With nested lists in hand,
        it's straightforward to create a list of coordinate pairs:
      </p>

<pre src="src/python/nested_vector.py">
values = []
reader = file('data.txt', 'r')
for line in reader:
    x, y = line.split()
    coord = [float(x), float(y)]
    values.append(coord)
reader.close()
</pre>

      <p class="continue">
        Each time the loop executes,
        this program splits the line into two strings,
        creates a new two-element list containing the corresponding numbers,
        and then appends that list to <code>values</code>.
      </p>

      <p>
        Now suppose that we have two such lists,
        and we want to find the average distance between corresponding coordinates.
      </p>

<pre src="src/python/vector_diff.py">
expected = [ [4.0, 2.0], [3.0, 5.0], [1.0, 6.0] ]
actual   = [ [4.2, 1.7], [3.1, 5.0], [0.8, 6.1] ]
x_diff, y_diff = 0.0,  0.0
for i in range(len(actual)):
    e = expected[i]
    a = actual[i]
    x_diff += abs(e[0] - a[0])
    y_diff += abs(e[1] - a[1])
print "average errors:", x_diff / len(actual), y_diff / len(actual)
<span class="out">average errors: 0.166666666667 0.133333333333</span>
</pre>

      <p class="continue">
        The first two lines set up our data:
        in a real program,
        we'd read values from files.
        The next line initializes <code>x_diff</code> and <code>y_diff</code>,
        which will hold the errors in X and Y respectively.
        Each iteration of the loop
        sets <code>a</code> and <code>e</code> to point at
        corresponding elements of the vectors.
        <code>a[0]</code> is then the X coordinate of an actual point,
        while <code>e[0]</code> is the X coordinate of the corresponding expected point,
        so <code>abs(e[0] - a[0])</code> is the difference,
        which we add to <code>x_diff</code> using <code>+=</code>.
      </p>

      <div class="keypoints" id="k:nestlist">
        <h3>Summary</h3>
        <ul>
          <li>Use nested lists to store multi-dimensional data or values that have regular internal structure (such as XYZ coordinates).</li>
          <li>Use <code><em>list_of_lists</em>[<em>first</em>]</code> to access an entire sub-list.</li>
          <li>Use <code><em>list_of_lists</em>[<em>first</em>][<em>second</em>]</code> to access a particular element of a sub-list.</li>
          <li>Use nested loops to process nested lists.</li>
        </ul>
      </div>

    </section>

    <section id="s:alias">

      <h2>Aliasing</h2>

      <div class="understand" id="u:alias">
        <h3>Understand:</h3>
        <ul>
          <li>That a program can contain many aliases for a single piece of data.</li>
          <li>That changes made through any of those aliases are visible through all the others.</li>
        </ul>
      </div>

      <p>
        At this point,
        we need to take a small side trip to explore something which is very useful,
        but which can also be the source of some hard-to-find bugs.
        Consider the following snippet of Python:
      </p>

<pre src="src/python/aliasing.py">
&gt;&gt;&gt; <span class="in">outer = [ [10, 20, 30], [40, 50, 60] ]</span>
&gt;&gt;&gt; <span class="in">inner = outer[0]</span>
</pre>

      <p class="continue">
        After these two lines have been executed,
        the program's memory is as shown in <a href="#f:aliasing_a">Figure XXX</a>:
        <code>outer</code> refers to a two-element list
        containing references to a couple of three-element lists,
        while <code>inner</code> refers to the first of those three-element lists.
      </p>

      <figure id="f:aliasing_a">
        <img src="src/python/aliasing_a.png" alt="First Step of Aliasing Example" />
      </figure>

      <p>
        Now let's change the last value of the list that <code>inner</code> refers to:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">inner[2] = 99</span>
</pre>

      <p class="continue">
        This changes memory as shown in <a href="#f:aliasing_b">Figure XXX</a>,
        which means that the values of both <code>inner</code> <em>and</em> <code>outer</code>
        have changed:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">print inner</span>
<span class="out">[10, 20, 99]</span>
&gt;&gt;&gt; <span class="in">print outer</span>
<span class="out">[[10, 20, 99], [40, 50, 60]]</span>
</pre>

      <figure id="f:aliasing_b">
        <img src="src/python/aliasing_b.png" alt="Second Step of Aliasing Example" />
      </figure>

    <span class="comment"> JK: Might also be worth introducing the word 'pointer' here </span>

      <p>
        This is called <a href="glossary.html#alias">aliasing</a>,
        and it is not a bug:
        the program is supposed to work this way.
        It doesn't have to, though;
        Python's creator could have decided that:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">inner = outer[0]</span>
</pre>

      <p class="continue">
        would create a copy of <code>outer[0]</code>
        and assign that to <code>inner</code>
        rather than aliasing the first element of <code>outer</code>
        (<a href="#f:aliasing_copy">Figure XXX</a>).
        That would be easier to understand&mdash;there would be no chance that
        assigning to one variable would cause another variable's value to change&mdash;but
        it would also be less efficient.
        If our sublists contain a million elements each,
        and we're assigning them to temporary variables
        simply to make our program more readable,
        copying would cause unnecessary slow-down.
      </p>

      <figure id="f:aliasing_copy">
        <img src="src/python/aliasing_copy.png" alt="Copying Instead of Aliasing" />
      </figure>

      <p>
        When a programming language copies data,
        and when it creates aliases instead,
        is one of the most important things a programmer must know about it.
        As we'll see when we start doing <a href="web.html">web programming</a>,
        it's also one of the most important things to know about large systems of any kind.
        If we query a database,
        is the result a copy of the data as it was when we made the query,
        or a reference to the master copy?
        In the first case,
        we can now change the data however we want without affecting other people,
        but we won't see any updates they make
        (<a href="#f:aliasing_data">Figure XXX</a>).
        In the second case,
        we will automatically see updates to the data,
        but that means our program has to cope with changes at unpredictable times
        (and also has to re-fetch the data each time it needs it,
        which will reduce performance).
        Neither approach is right or wrong:
        there are simply engineering tradeoffs that we have to be aware of.
      </p>

      <figure id="f:aliasing_data">
        <img src="src/python/aliasing_data.png" alt="Aliasing Data" />
      </figure>

    <span class="comment"> JK: While copying in Python can certainly be hard to understand, it 
         might be worth a box and a mention that there is a module called copy
         (or the function copy.copy) that will make a copy if that's really
         what you want to do. Otherwise, it sort of implies that if you 
         actually want to make a copy, you can't. </span>

      <div class="keypoints" id="k:alias">
        <h3>Summary</h3>
        <ul>
          <li>Several variables can alias the same data.</li>
          <li>If that data is mutable (e.g., a list), a change made through one variable is visible through all other aliases.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

      <p>
        Novices (and people looking for an argument) often ask,
        "What's the best programming language?"
        The answer depends on what we want to do.
        If we want to write small programs quickly,
        and be able to manage the complexity of larger ones,
        then dynamic languages like Python, Ruby, R, and MATLAB are good choices:
        they optimize programming time over execution time.
        If we want to squeeze the last ounce of performance out of our hardware,
        then compiled languages like C++, C#, and modern dialects of Fortran
        are currently better options.
        And if we want a user interface that runs (almost) everywhere,
        Javascript has become a surprisingly strong contender.
      </p>

    </section>