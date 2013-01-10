Title: Quality
Directory: book

    <ol class="toc">
      <li><a href="#s:defensive">Defensive Programming</a></li>
      <li><a href="#s:except">Handling Errors</a></li>
      <li><a href="#s:unit">Unit Testing</a></li>
      <li><a href="#s:numbers">Numbers</a></li>
      <li><a href="#s:coverage">Coverage</a></li>
      <li><a href="#s:debug">Debugging</a></li>
      <li><a href="#s:testable">Designing Testable Code</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <p>
      Laura Landscape is studying the impact of climate change on agriculture.
      She has several thousand aerial photographs of farms taken in the early 1980s,
      and she wants to compare those with photographs of the same fields taken since 2007
      to see what has changed.
    </p>

    <p>
      The first step is to find regions where fields overlap.
      Luckily,
      the area she is studying is in Saskatchewan,
      where fields actually are rectangular.
      A student intern has written a function that finds the regions of overlap
      between the fields in different photographs.
      Having used student code before,
      she wants to test it before putting it into production.
      She also thinks she might have to make the function faster,
      to handle larger data sets,
      and she wants to have tests in place so that her optimizations don't break anything.
      What should she do?
    </p>

    <p>
      Nobody actually enjoys testing software:
      we'd all rather be writing new programs,
      or better yet,
      using the ones we have to do some new science.
      If you'd like to skip this lecture,
      you can,
      provided that:
    </p>

    <ol>

      <li>
        your programs always work correctly the first time you run them;
      </li>

      <li>
        you don't actually care whether they're doing the right thing or not,
        as long as their output <em>looks</em> plausible; or
      </li>

      <li>
        you enjoy wasting time,
        because experience and research both show that
        improving quality is the best way to improve productivity.
      </li>

    </ol>

    <p>
      We said "improving quality" rather than testing
      because as Steve McConnell once said,
      trying to improve the quality of software by doing more testing
      is like trying to lose weight by weighing yourself more often.
      Testing just tells us what the quality <em>is</em>;
      if we want to improve it,
      so that we don't have to throw away a week's worth of analysis because of a missing semi-colon,
      we have to change our programs,
      and change the way we go about writing programs.
      That's what this chapter is really about.
    </p>

    <section id="s:defensive">

      <h2>Defensive Programming</h2>

      <div class="understand" id="u:defensive">
        <h3>Understand:</h3>
        <ul>
          <li>That programs should detect errors as early as possible.</li>
          <li>How to use assertions to establish that something is true in a program.</li>
          <li>That functions should define and obey contracts with their users.</li>
        </ul>
      </div>

      <p>
        The first and most important step in creating quality programs is
        to follow the rules outlined in <a href="python.html">previous</a> <a href="funclib.html">chapters</a>
        for writing readable code.
        The second is to realize that since nobody is perfect,
        programs should be designed to detect both their own errors,
        and errors in the way they are used.
        This is called <a href="glossary.html#defensive-programming">defensive programming</a>,
        and is akin to adding a self-test function to a piece of lab equipment.
      </p>

      <p>
        In most modern languages,
        we do this by adding <a href="glossary.html#assertion">assertions</a> to our programs.
        An assertion is simply a statement that something is supposed to be true
        at a certain point in the program.
        For example,
        here's the <code>combine_values</code> function from
        the section on <a href="funclib.html#s:funcobj">functional programming</a>:
      </p>

<pre src="src/quality/combine.py">
def combine_values(func, values):
    current = values[0]
    for i in range(1, len(values)):
        current = func(current, values[i])
    return current
</pre>

      <p>
        If we want to add up the values in a list,
        we call it like this:
      </p>

<pre>
def add(a, b):
    return a + b

numbers = [1, 3, 6, 7, 9]
print combine_values(add, numbers)
<span class="out">26</span>
</pre>

      <p class="continue">
        If we call it with an empty list, though,
        it fails,
        because the first statement tries to get the list's first element:
      </p>

<pre>
print combine_values(add, [])
<span class="err">IndexError: list index out of range</span>
</pre>

      <p>
        Let's add an assertion to test for this case explicitly:
      </p>

<pre src="src/quality/combine2.py">
def combine_values(func, values):
    <span class="highlight">assert len(values) &gt; 0, 'Cannot combine values from empty list'</span>
    current = values[0]
    for i in range(1, len(values)):
        current = func(current, values[i])
    return current

print combine_values(add, [])
<span class="err">AssertionError: Cannot combine values from empty list</span>
</pre>

      <p>
        This assertion documents the <a href="glossary.html#contract">contract</a>
        between the function and its caller:
        the function will only produce a value
        if the caller provides a list containing some data.
        We could use a comment or docstring to do the same thing,
        but the assertion has the advantage of being executable:
        the program actually does the check
        every time the function is called.
      </p>

      <p>
        Good programs are littered with assertions&mdash;in fact,
        10-20% of the statements in many widely-used programs
        are there to check that the other 80-90% are working correctly.
        Broadly speaking,
        assertions fall into three categories:
      </p>

      <ul>

        <li>
          A <a href="glossary.html#precondition">precondition</a> is
          something that has to be true
          in order for a piece of code to work correctly.
        </li>

        <li>
          A <a href="glossary.html#postcondition">postcondition</a> is
          something that has to be true at the end of a piece of code
          if it worked correctly.
        </li>

        <li>
          An <a href="glossary.html#invariant">invariant</a> is
          something that is always true at a particular point inside a piece of code.
        </li>

      </ul>

      <figure id="f:rectangle_rep">
        <img src="img/python/rectangle_rep.png" alt="Representing Rectangles" />
      </figure>

      <p>
        For example,
        suppose we are representing rectangles using a pair of pairs
        <code>[[x<sub>0</sub>, y<sub>0</sub>], [x<sub>1</sub>, y<sub>1</sub>]]</code>
        (<a href="#f:rectangle_rep">Figure XXX</a>).
        In order to normalize some calculations,
        we need to resize the rectangle so that it is 1.0 units long on its longest axis.
        Here's a function that does that:
      </p>

<pre src="src/quality/rectangle_resize.py">
def normalize_rectangle(rect):
    [[x0, y0], [x1, y1]] = rect
    assert x0 &lt; x1, 'Invalid X coordinates'
    assert y0 &lt; y1, 'Invalid Y coordinates'
    dx = x1 - x0
    dy = y1 - y0
    if dx &gt; dy:
        scaled = float(dy) / dx
        upper = [1.0, scaled]
    else:
        scaled = float(dx) / dy
        upper = [scaled, 1.0]

    assert 0 &lt; upper[0] &lt;= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 &lt; upper[1] &lt;= 1.0, 'Calculated upper Y coordinate invalid'

    return [[0, 0], upper]
</pre>

      <p class="continue">
        The first two assertions test that the inputs are valid,
        i.e.,
        that the upper X and Y coordinates are greater than their lower counterparts.
        Notice that the test is greater than, not greater than or equal to;
        this tells us (and the computer)
        that rectangles aren't allowed to have zero width or height.
        The last two assertions check that the upper coordinates of the scaled rectangle are valid:
        neither can be zero
        (because that would mean the rectangle had zero width or height),
        and neither can be greater than 1.
      </p>

      <p>
        If the inputs are correct,
        and our calculation is correct,
        then these two conditions should always hold,
        so strictly speaking,
        these two assertions are redundant.
        However,
        programmers aren't perfect,
        and if there <em>is</em> a bug in our calculations,
        we want the program to complain about it as early as possible.
      </p>

      <p>
        This principle is sometimes stated as, "Fail early, fail often."
        The longer the gap between when something goes wrong and when we realize it,
        the more lines of code and program execution history we have to wade through
        in order to track the problem down.
      </p>

      <div class="box">
        <h3>Assertions and Bugs</h3>

        <p>
          Another rule that good programmers follow is, "Bugs become assertions."
          Whenever we fix a bug in a program,
          we should add some assertions to the program at that point
          to catch the bug if it reappears.
          After all,
          if we made the mistake once,
          we (or someone else) might well make it again,
          and few things are as frustrating as having someone delete several carefully-crafted lines of code
          that fixed a subtle problem
          because they didn't realize what problem those lines were there to fix.
        </p>
      </div>

      <div class="box">
        <h3>Assertions and Types</h3>

        <p>
          It's common to see code like this
          from people who have just learned about assertions:
        </p>

<pre src="src/quality/rectangle_resize.py">
def normalize_rectangle(rect):
    assert type(rect) == list, 'Input is not a list'
    assert len(rect) == 2, 'Input rectangle does not have two elements'
    assert len(rect[0]) == 2, 'Low coordinate of rectangle does not have two elements'
    assert type(rect[0][0]) in (int, float), 'Low X coordinate is not a number'
    ...
</pre>

        <p class="continue">
          In essence,
          these assertions are emulating the checks that are built into
          statically-typed languages like Java and C++,
          which require programmers to declare what kind of data every variable can store.
          For the most part,
          they aren't very useful in dynamically-typed languages like Python:
        </p>

        <ol>

          <li>
            The statement that unpacks the values in <code>rect</code>
            and assigns them to <code>x0</code>, <code>y0</code>, <code>x1</code>, and <code>y1</code>
            will fail if <code>rect</code> doesn't have the right structure,
            so the assertion doesn't do any checking that the program isn't doing already.
          </li>

          <li>
            These checks are overly restrictive.
            There's no reason we shouldn't be able to pass in tuples of coordinates instead of lists,
            or use rational (fractional) numbers instead of integers or floats,
            but if we do either of those things,
            the assertions given above will fail.
            Rather than checking how something is implemented (i.e., what types are used),
            assertions should check what those things can do
            (i.e., what operations we can perform on them).
            We will talk about this more when we talk about the difference between
            <a href="#s:testable">interface and implementation</a>.
          </li>

        </ol>

      </div>

      <div class="keypoints" id="k:defensive">
        <h3>Summary</h3>
        <ul>
          <li idea="paranoia">Design programs to catch both internal errors and usage errors.</li>
          <li idea="paranoia">Use assertions to check whether things that ought to be true in a program actually are.</li>
          <li idea="perf">Assertions help people understand how programs work.</li>
          <li>Fail early, fail often.</li>
          <li idea="paranoia">When bugs are fixed, add assertions to the program to prevent their reappearance.</li>
        </ul>
      </div>

    </section>

    <section id="s:except">

      <h2>Handling Errors</h2>

      <div class="understand" id="u:except">
        <h3>Understand:</h3>
        <ul>
          <li>Why functions shouldn't use status code to indicate whether they ran correctly or not.</li>
          <li>What exceptions are and when they can occur.</li>
          <li>How to handle exceptions.</li>
          <li>That there are different kinds of exceptions, which can be handled separately.</li>
          <li>That exceptions can and should be handled a long way from where they occur.</li>
          <li>How to raise an exception.</li>
        </ul>
      </div>

      <p>
        It's a sad fact, but things sometimes go wrong in programs.
        Some of these errors have external causes, like missing or badly-formatted files.
        Others are internal, like bugs in code.
        Either way, there's no need for panic:
        it's actually pretty easy to handle errors in sensible ways.
      </p>

      <p>
        First, though, let's have a look at how programmers used to do error handling.
        Back in the Dark Ages,
        programmers would have functions return some sort of status
        to indicate whether they had run correctly or not.
        This led to code like this:
      </p>

<pre>
params, <span class="highlight">status</span> = read_params(param_file)
<span class="highlight">if status != OK:
  log.error('Failed to read', param_file)
  sys.exit(ERROR)</span>

grid, <span class="highlight">status</span> = read_grid(grid_file)
<span class="highlight">if status != OK:
  log.error('Failed to read', grid_file)
  sys.exit(ERROR)</span>
</pre>

      <p class="continue">
        The unhighlighted code is what we really want;
        the highlighted lines are there to check that files were opened and read properly,
        and to report errors and exit if not.
      </p>

      <p>
        A lot of code is still written this way,
        but this coding style makes it hard to see the forest for the trees.
        When we're reading a program,
        we want to understand what's supposed to happen when everything works,
        and only then think about what might happen if something goes wrong.
        When the two are interleaved,
        both are harder to understand.
        The net result is that most programmers don't bother to check the status codes their functions return.
        Which means that when errors <em>do</em> occur,
        they're even harder to track down.
      </p>

      <p>
        Luckily, there's a better way.
        Modern languages like Python allow us to use
        <a href="glossary.html#exception">exceptions</a>
        to handle errors.
        More specifically,
        using exceptions allows us to separate the "normal" flow of control
        from the "exceptional" cases that arise when something goes wrong,
        which makes both easier to understand:
      </p>

<pre>
try:
  params = read_params(param_file)
  grid = read_grid(grid_file)
except:
  log.error('Failed to read', filename)
  sys.exit(ERROR)
</pre>

      <p class="continue">
        As a fringe benefit,
        this often allows us to eliminate redundancy in our error handling.
      </p>

      <p>
        To join the two parts together,
        we use the keywords <code>try</code> and <code>except</code>.
        These work together like <code>if</code> and <code>else</code>:
        the statements under the <code>try</code> are what should happen if everything works,
        while the statements under <code>except</code> are what the program should do if something goes wrong.
      </p>

      <p>
        We have actually seen exceptions before without knowing it,
        since by default,
        when an exception occurs,
        Python prints it out and halts our program.
        For example,
        trying to open a nonexistent file triggers a type of exception called an <code>IOError</code>,
        while an out-of-bounds index to a list triggers an <code>IndexError</code>:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">open('nonexistent.txt', 'r')</span>
<span class="err">IOError: No such file or directory: 'nonexistent.txt'</span>
&gt;&gt;&gt; <span class="in">values = [0, 1, 2]</span>
&gt;&gt;&gt; <span class="in">values[99]</span>
<span class="err">IndexError: list index out of range</span>
</pre>

      <p>
        We can use <code>try</code> and <code>except</code> to deal with these errors ourselves
        if we don't want the program simply to fall over.
        Here,
        for example,
        we put our attempt to open a nonexistent file inside a <code>try</code>,
        and in the <code>except</code>, we print a not-very-helpful error message:
      </p>

<span>
try:
  reader = open('nonexistent.txt', 'r')
except IOError:
  print 'Whoops!
<span class="out">Whoops!</span>
</span>

      <p class="continue">
        Notice that the output is blue,
        signalling that it was printed normally,
        rather than red,
        which is shown for errors.
        When Python executes this code,
        it runs the statement inside the <code>try</code>.
        If that works, it skips over the <code>except</code> block without running it.
        If an exception occurs inside the <code>try</code> block,
        though,
        Python compares the type of the exception to the type specified by the <code>except</code>.
        If they match, it executes the code in the <code>except</code> block.
      </p>

      <figure id="f:exception_flowchart">
        <img src="img/quality/exception_flowchart.png" alt="Flow of Control with Exceptions" />
      </figure>

      <p>
        Note,
        by the way,
        that <code>IOError</code> is Python's way of reporting several kinds of problems
        related to input and output:
        not just files that don't exist,
        but also things like not having permission to read files,
        and so on.
      </p>
      <p>
        We can put as many lines of code in a <code>try</code> block as we want,
        just as we can put many statements under an <code>if</code>.
        We can also handle several different kinds of errors afterward.
        For example,
        here's some code to calculate the entropy at each point in a grid:
      </p>


<pre>try:
    params = read_params(param_file)
    grid = read_grid(grid_file)
    entropy = lee_entropy(params, grid)
    write_entropy(entropy_file, entropy)
except IOError:
    log_error_and_exit('IO error')
except ArithmeticError:
    log_error_and_exit('Arithmetic error')
</pre>

      <p class="continue">
        Python tries to run the four statements inside the <code>try</code> as normal.
        If an error occurs in any of them,
        Python immediately jumps down
        and tries to find an <code>except</code> whose type matches the type of the error that occurred.
        If it's an <code>IOError</code>,
        Python jumps into the first error handler.
        If it's an <code>ArithmeticError</code>,
        Python jumps into the second handler instead.
        It will only execute one of these,
        just as it will only execute one branch
        of a series of <code>if</code>/<code>elif</code>/<code>else</code> statements.
      </p>

      <p>
        This layout has made the code easier to read,
        but we've lost something important:
        the message printed out by the <code>IOError</code> branch doesn't tell us
        which file caused the problem.
        We can do better if we capture and hang on to the object that Python creates
        to record information about the error:
      </p>

<pre>
try:
    params = read_params(param_file)
    grid = read_grid(grid_file)
    entropy = lee_entropy(params, grid)
    write_entropy(entropy_file, entropy)
except IOError <span class="highlight">as err</span>:
    log_error_and_exit('Cannot read/write' <span class="highlight">+ err.filename</span>)
except ArithmeticError <span class="highlight">as err</span>:
    log_error_and_exit(err.message)
</pre>

      <p>
        If something goes wrong in the <code>try</code>,
        Python creates an exception object,
        fills it with information,
        and assigns it to the variable <code>err</code>.
        (There's nothing special about this variable name&mdash;we can use anything we want.)
        Exactly what information is recorded depends on what kind of error occurred;
        Python's documentation describes the properties of each type of error in detail,
        but we can always just print the exception object.
        In the case of an I/O error,
        we print out the name of the file that caused the problem.
        And in the case of an arithmetic error,
        printing out the message embedded in the exception object is what Python would have done anyway.
      </p>

      <p>
        So much for how exceptions work:
        how should they be used?
        Some programmers use <code>try</code> and <code>except</code> to give their programs default behaviors.
        For example,
        if this code can't read the grid file that the user has asked for,
        it creates a default grid instead:
      </p>

<pre>
try:
    grid = read_grid(grid_file)
except IOError:
    grid = default_grid()
</pre>

      <p>
        Other programmers would explicitly test for the grid file,
        and use <code>if</code> and <code>else</code> for control flow:
      </p>

<pre>
if file_exists(grid_file):
    grid = read_grid(grid_file)
else:
    grid = default_grid()
</pre>

      <p>
        It's mostly a matter of taste,
        but we prefer the second style.
        As a rule,
        exceptions should only be used to handle exceptional cases.
        If the program knows how to fall back to a default grid,
        that's not an unexpected event.
        Using <code>if</code> and <code>else</code>
        instead of <code>try</code> and <code>except</code>
        sends different signals to anyone reading our code,
        even if they do the same thing.
      </p>

      <p>
        Novices often ask another question about exception handling style as well,
        but before we address it,
        there's something in our example that you might not have noticed.
        Exceptions can actually be thrown a long way:
        they don't have to be handled immediately.
        Take another look at this code:
      </p>

<pre>
try:
    params = read_params(param_file)
    grid = read_grid(grid_file)
    entropy = lee_entropy(params, grid)
    write_entropy(entropy_file, entropy)
except IOError as err:
    log_error_and_exit('Cannot read/write' + err.filename)
except ArithmeticError as err:
    log_error_and_exit(err.message)
</pre>

      <p class="continue">
        The four lines in the <code>try</code> block are all function calls.
        They might catch and handle exceptions themselves,
        but if an exception occurs in one of them that <em>isn't</em> handled internally,
        Python looks in the calling code for a matching <code>except</code>.
        If it doesn't find one there,
        it looks in that function's caller,
        and so on.
        If we get all the way back to the main program without finding an exception handler,
        Python's default behavior is to print an error message like the ones we've been seeing all along.
      </p>

      <p>
        This rule is the origin of the saying,
        "Throw low, catch high."
        There are many places in our program where an error might occur.
        There are only a few, though, where errors can sensibly be handled.
        For example,
        a linear algebra library doesn't know whether it's being called directly from the Python interpreter,
        or whether it's being used as a component in a larger program.
        In the latter case,
        the library doesn't know if the program that's calling it is being run from the command line or from a GUI.
        The library therefore shouldn't try to handle or report errors itself,
        because it has no way of knowing what the right way to do this is.
        It should instead just raise an exception,
        and let its caller figure out how best to handle it.
      </p>

      <p>
        Finally,
        we can raise exceptions ourselves if we want to.
        In fact,
        we <em>should</em> do this,
        since it's the standard way in Python to signal that something has gone wrong.
        Here,
        for example,
        is a function that reads a grid and checks its consistency:
      </p>

<pre>
def read_grid(grid_file):
    '''Read grid, checking consistency.'''

    data = read_raw_data(grid_file)
    if not grid_consistent(data):
        raise Exception('Inconsistent grid: ' + grid_file)
    result = normalize_grid(data)

    return result
</pre>

      <p class="continue">
        The <code>raise</code> statement creates a new exception with a meaningful error message.
        Since <code>read_grid</code> itself doesn't contain a <code>try</code>/<code>except</code> block,
        this exception will always be thrown up and out of the function,
        to be caught and handled by whoever is calling <code>read_grid</code>.
        We can define new types of exceptions if we want to.
        And we should,
        so that errors in our code can be distinguished from errors in other people's code.
        However,
        this involves classes and objects,
        which is outside the scope of these lessons.
      </p>

      <div class="keypoints" id="k:except">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>raise</code> to raise exceptions.</li>
          <li>Raise exceptions to report errors rather than trying to handle them inline.</li>
          <li>Use <code>try</code> and <code>except</code> to handle exceptions.</li>
          <li>Catch exceptions where something useful can be done about the underlying problem.</li>
          <li>An exception raised in a function may be caught anywhere in the active call stack.</li>
        </ul>
      </div>

    </section>

    <section id="s:unit">

      <h2>Unit Testing</h2>

      <div class="understand" id="u:unit">
        <h3>Understand:</h3>
        <ul>
          <li>That testing can't catch all mistakes, but is still worth doing.</li>
          <li>What a unit test is.</li>
          <li>That unit tests should be independent of each other.</li>
          <li>Why we want to ensure that all unit tests are always run.</li>
          <li>How to write unit tests using a standard library.</li>
          <li>That testing effort should focus on boundary cases.</li>
          <li>That tests help us specify what code should do.</li>
        </ul>
      </div>

      <p>
        Now that we know how to defend against errors,
        and how to handle them,
        we can look at how to test our programs.
        First,
        though,
        it's important to understand that testing can only do so much.
        Suppose we are testing a function that compares two 7-digit phone numbers.
        There are 10<sup>7</sup> such numbers,
        which means that there are 10<sup>14</sup> possible test cases for our function.
        At a million tests per second,
        it would take us 155 days to run them all.
        And that's only one simple function:
        exhaustively testing a real program with hundreds or thousands of functions,
        each taking half a dozen arguments,
        would take many times longer than the expected lifetime of the universe.
      </p>

      <p>
        And how would we actually write 10<sup>14</sup> tests?
        More importantly,
        how would we check that the tests themselves were all correct?
      </p>

      <p>
        In reality,
        all that testing can do is show that there <em>might</em> be a problem in a piece of code.
        If testing doesn't find a failure,
        there could still be bugs lurking there that we just didn't find.
        And if testing says there <em>is</em> a problem,
        it could well be a problem with the test rather than the program.
      </p>

      <p>
        So why test?
        Because it's one of those things that shouldn't work in theory,
        but is surprisingly effective in practice.
        It's just like mathematics:
        any theorem proof might contain a flaw that just hasn't been noticed yet,
        but somehow we manage to make progress.
      </p>

      <p>
        The obstacle to testing isn't actually whether or not it's useful,
        but whether or not it's easy to do.
        If it isn't,
        people will always find excuses to do something else.
        It's therefore important to make things as painless as possible.
        In particular, it has to be easy for people to:
      </p>

      <ul>

        <li>
          add or change tests,
        </li>

        <li>
          understand the tests that have already been written,
        </li>

        <li>
          run those tests, and
        </li>

        <li>
          understand those tests' results.
        </li>

      </ul>

      <p>
        Test results must also be reliable to be useful.
        If a testing tool says that code is working when it's not,
        or reports problems when there actually aren't any,
        people will lose faith in it and stop using it.
      </p>

      <p>
        Let's start with the simplest kind of testing.
        A <a href="glossary.html#unit-test">unit test</a> is
        a test that exercises one component, or unit, in a program.
        Every unit test has five parts.
        The first is the <a href="glossary.html#fixture">fixture</a>,
        which is the thing the test is run on:
        the inputs to a function,
        or the data files to be processed.
      </p>

      <p>
        The second part is the <a href="glossary.html#test-action">action</a>,
        which is what we do to the fixture.
        Ideally,
        this just involves calling a function,
        but some tests may involve more.
      </p>

      <p>
        The third part of every unit test is its <a href="glossary.html#expected-result">expected result</a>,
        which is what we expect the piece of code we're testing to do or return.
        If we don't know the expected result,
        we can't tell whether the test passed or failed.
        As we'll see <a href="#s:unit">later</a>,
        defining fixtures and expected results can be a good way to design software.
      </p>

      <p>
        The first three parts of the unit test are used over and over again.
        The fourth part is the <a href="glossary.html#test-result">actual result</a>,
        which is what happens when we run the test on a particular day,
        with a particular version of our software.
      </p>

      <p>
        The fifth and final part of our test is a <a href="glossary.html#test-report">report</a>
        that tells us whether the test passed,
        or whether there's a failure of some kind that needs human attention.
        As with the actual result,
        this could be different each time we run the test.
      </p>

      <p>
        So much for terminology:
        what does this all look like in practice?
        Suppose we're testing a function called <code>dna_starts_with</code>.
        It returns <code>True</code> if its second argument is a prefix of the first
        (i.e., if one sequence starts with another),
        and <code>False</code> otherwise:
      </p>

<pre>
&gt;&gt;&gt; dna_starts_with('actggt', 'act')
True
&gt;&gt;&gt; dna_starts_with('actggt', 'ctg')
False
</pre>

      <p>
        We'll build a simple set of tests for this function from scratch to introduce some key ideas,
        then introduce a Python library that can take care of the repetitive details.
      </p>

      <p>
        Let's start by testing our code directly using <code>assert</code>.
        Here,
        we call the function four times with different arguments,
        checking that the right value is returned each time.
      </p>

<pre>
assert dna_starts_with('a', 'a')
assert dna_starts_with('at', 'a')
assert dna_starts_with('at', 'at')
assert not dna_starts_with('at', 't')
</pre>

      <p>
        This is better than nothing,
        but it has several shortcomings.
        First, there's a lot of repeated code:
        only a fraction of what's on each line is unique and interesting.
        That repetition makes it easy to overlook things,
        like the <code>not</code> used to check that
        the last test returns <code>False</code> instead of <code>True</code>.
      </p>

      <p>
        This code also only tests up to the first failure.
        If any of the tests doesn't produce the expected result,
        the <code>assert</code> statement will halt the program.
        It would be more helpful if we could get data from all of our tests every time they're run,
        since the more information we have,
        the faster we're likely to be able to track down bugs.
      </p>

      <p>
        Here's a different approach.
        First, let's put each test in a function with a meaningful name:
      </p>

<span class="comment">
Steve Haddock:
def longer_genome_starts_with_base():
    assert dna_starts_with('at', 'a')

you wouldn't ever really call that a genome.

also,,using ATG as the starts_with sequence would make most sense, since that is the "start codon" for most genes
</span>

<pre>
def single_base_starts_with_itself():
    assert dna_starts_with('a', 'a')

def longer_genome_starts_with_base():
    assert dna_starts_with('at', 'a')

def longer_genome_starts_with_itself():
    assert dna_starts_with('at', 'at')

def longer_genome_doesnt_start_with():
    assert not dna_starts_with('at', 't')
</pre>

      <p class="continue">
        Of course, those tests won't run themselves,
        so we'll add one more function at the bottom of the program
        that calls each test in turn:
      </p>

<pre>
def run():
    single_base_starts_with_itself()
    longer_genome_starts_with_base()
    longer_genome_starts_with_itself()
    longer_genome_doesnt_start_with()
</pre>

      <p>
        So far, this isn't much of an improvement&mdash;in fact,
        it's made things worst.
        But what if we put all our tests in a list,
        and then loop over that list,
        calling each function in turn?
      </p>

<pre>
def run():
    tests = [single_base_starts_with_itself,
             longer_genome_starts_with_base,
             longer_genome_starts_with_itself,
             longer_genome_doesnt_start_with]
    for t in tests:
        t()
</pre>

      <p class="continue">
        This will still crash the first time a test fails,
        though,
        so let's add some error handling:
      </p>

<pre>
def run():
    tests = [single_base_starts_with_itself,
             longer_genome_starts_with_base,
             longer_genome_starts_with_itself,
             longer_genome_doesnt_start_with]
    pass = fail = error = 0
    for t in tests:
        try:
            t()
            pass += 1
        except AssertionError:
            fail += 1
        except:
            error += 1
    return pass, fail, error
</pre>

      <p>
        This version makes the pattern in our testing clear (well, clear-ish).
        Each function is called exactly once;
        if it runs without an assertion,
        we count the test as a success.
        If an assertion fails,
        we count the test as a failure,
        and if any other exception occurs,
        we add one to our count of errors
        (i.e., of tests that are themselves broken).
      </p>

      <p>
        This pattern is so common that libraries have been written to support it in
        <a href="http://en.wikipedia.org/wiki/XUnit">dozens of different programming languages</a>.
        We'll use a Python library called Nose to illustrate the ideas.
        In Nose, each test is a function whose name begins with the letters <code>test_</code>.
        We can group tests together in files,
        whose names also begin with the letters <code>test_</code>.
        To execute our tests, we run the command <code>nosetests</code>.
        This automatically searches the current directory and its sub-directories for test files
        and runs the tests they contain.
      </p>

      <p>
        To see how this works,
        let's use it to test the <code>dna_starts_with</code> function.
        All we have to do is
        delete the <code>run</code> function (which we no longer need)
        and change the names of the individual tests:
      </p>

<pre>
def test_single_base_starts_with_itself():
    assert dna_starts_with('a', 'a')

def test_longer_genome_starts_with_base():
    assert dna_starts_with('at', 'a')

def test_longer_genome_starts_with_itself():
    assert dna_starts_with('at', 'at')

def test_longer_genome_doesnt_start_with():
    assert not dna_starts_with('at', 't')
</pre>

      <p>
        To run these tests,
        we simply type:
      </p>

<pre>
$ <span class="in">nosetests</span>
<span class="out">....
----------------------------------------------------------------------
Ran 4 tests in 0.004s

OK</span>
</pre>

      <p class="continue">
        Each '.' represents a successful test.
        To see what happens if a test fails,
        let's add two more functions to the file that are deliberately broken:
      </p>

<pre>
def test_deliberate_failure():
    assert dna_starts_with('at', 'xxx')

def test_deliberate_error():
    infinity = 1/0
    assert dna_starts_with('at', 'a')
</pre>

<pre>
~/foo $ nosetests
....FE
======================================================================
ERROR: test_dna.test_deliberate_error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/python2.7/site-packages/nose-1.0.0-py2.7.egg/nose/case.py", line 187, in runTest
    self.test(*self.arg)
  File "/home/scb/testing/test_dna.py", line 20, in test_deliberate_error
    infinity = 1/0
ZeroDivisionError: integer division or modulo by zero

======================================================================
FAIL: test_dna.test_deliberate_failure
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/python2.7/site-packages/nose-1.0.0-py2.7.egg/nose/case.py", line 187, in runTest
    self.test(*self.arg)
  File "/home/scb/testing/test_dna.py", line 17, in test_deliberate_failure
    assert dna_starts_with('at', 'xxx')
AssertionError

----------------------------------------------------------------------
Ran 6 tests in 0.055s

FAILED (errors=1, failures=1)
</pre>

      <p>
        Of course, the Nose library can't think of test cases for us.
        We still have to decide what to test, and how many tests to run.
        How should we go about deciding which tests to write?
        The answer comes from economics:
        we want the tests that are most likely to give us useful information
        that we don't already have.
        For example,
        if <code>dna_starts_with('atc', 'a')</code> works,
        there's probably not much point testing <code>dna_starts_with('ttc', 't')</code>:
        it's hard to think of a bug that would show up in one case,
        but not in the other.
      </p>

      <p>
        We should therefore try to choose tests that are as different from each other as possible,
        so that we force the code we're testing to execute in all the different ways it can.
        Another way of thinking about this is that we should try to find
        <a href="glossary.html#boundary-case">boundary cases</a>.
        If a function works for zero,
        one,
        and a million values,
        it will probably work for eighteen values.
      </p>

      <p>
        Let's apply this idea to the overlapping rectangles problem from the introduction.
        A "normal" case is two rectangles that overlap by half in each direction:
      </p>

      <figure id="f:simple_rectangle_test_case">
        <img src="img/quality/simple_rectangle_test_case.png" alt="A Simple Test Case" />
      </figure>

      <p clas="continue">
        What other tests would be useful?
        One would be two rectangles that overlap by half in each direction..
        Another is the case where
        the rectangle on the left extends above and below the one on the right,
        so none of the corners of the left rectangle are involved.
        And in a third
        the two rectangles are exactly the same width,
        but have different vertical extents.
        This will tell us whether the overlap function behaves correctly
        when rectangles intersect along entire lines,
        rather than just crossing at points.
        And then there's the case where the second rectangle is contained entirely within the first,
        so their edges don't actually cross at all.
      </p>

      <figure id="f:more_rectangle_test_cases">
        <img src="img/quality/more_rectangle_test_cases.png" alt="More Test Cases" />
      </figure>

      <p>
        But what do we expect if the two rectangles share an edge,
        but their areas don't overlap?
        And what if they only share a corner?
        Should the function we're testing tell us that these rectangles don't overlap?
        Should it return a point,
        rather than a rectangle?
        Or should it return a rectangle with zero area?
      </p>

      <figure id="f:boundary_cases">
        <img src="img/quality/boundary_cases.png" alt="Boundary Cases" />
      </figure>

      <p>
        Thinking about tests in terms of boundary cases helps us find examples like this,
        where it isn't immediately obvious what the right answer is.
        Writing those tests forces us to define how the function we're testing
        is supposed to behave&mdash;i.e., what correct behavior actually is.
      </p>

      <p>
        Let's turn all of this into working code.
        Here's a test for the case where rectangles only touch at a corner:
      </p>

<pre>
def test_touch_at_corner():
    assert overlap([[0, 0], [2, 2]], [[2, 2], [4, 4]]) == None
</pre>

      <p class="continue">
        As you can see, we've decided that this doesn't count as overlap.
        Our test is an unambiguous,
        runnable answer to our question about how the function is supposed to behave.
      </p>

      <p>
        Here's our second test:
        two rectangles that have exactly the same extent,
        so their overlap is the same again.
      </p>

<pre>
def test_touch_at_corner():
    r = [[0, 0], [2, 2]]
    assert overlap(r, r) == r
</pre>

      <p class="continue">
        This wasn't actually in the set of test cases we came up with earlier,
        but it's still a good test.
        And here's a third test, where one rectangle is skinnier than another:
      </p>

<pre>
def test_partial_overlap():
    red = [[0, 3], [2, 5]]
    blue = [[1, 0], [2, 4]]
    assert overlap(red, blue) == [[1, 3], [2, 4]]
</pre>

      <p class="continue">
        This test case actually turned up a bug in the first version of the overlap function that we wrote.
        Here's the function:
      </p>

<pre>
def overlap(red, blue):
    '''Return overlap between two rectangles, or None.'''

    [[red_lo_x, red_lo_y], [red_hi_x, red_hi_y]] = red
    [[blue_lo_x, blue_lo_y], [blue_hi_x, blue_hi_y]] = blue

    if (red_lo_x &gt;= blue_hi_x) or (red_hi_x &lt;= blue_lo_x) or \
       (red_lo_y &gt;= blue_hi_x) or (red_hi_y &lt;= blue_lo_y):
        return None

    lo_x = max(red_lo_x, blue_lo_x)
    lo_y = max(red_lo_y, blue_lo_y)
    hi_x = min(red_hi_x, blue_hi_x)
    hi_y = min(red_hi_y, blue_hi_y)

    return [[lo_x, lo_y], [hi_x, hi_y]]
</pre>

      <p class="continue">
        It takes the coordinates of each rectangle as input,
        unpacks them to get the high and low X and Y coordinates of each rectangle,
        checks to make sure that the rectangles actually overlap,
        then calculates the coordinates of the overlap and returns the result as a new rectangle.
        By looking at which test cases pass and fail,
        it's pretty easy to discover that
        we are comparing the low Y coordinate of one rectangle with the high X coordinate of the other
        (probably as a result of copying and pasting):
      </p>

<pre>
def overlap(red, blue):
    '''Return overlap between two rectangles, or None.'''

    [[red_lo_x, red_lo_y], [red_hi_x, red_hi_y]] = red
    [[blue_lo_x, blue_lo_y], [blue_hi_x, blue_hi_y]] = blue

    if (red_lo_x &gt;= blue_hi_x) or (red_hi_x &lt;= blue_lo_x) or \
       <span class="highlight">(red_lo_y &gt;= blue_hi_x)</span> or (red_hi_y &lt;= blue_lo_y):
        return None

    lo_x = max(red_lo_x, blue_lo_x)
    lo_y = max(red_lo_y, blue_lo_y)
    hi_x = min(red_hi_x, blue_hi_x)
    hi_y = min(red_hi_y, blue_hi_y)

    return [[lo_x, lo_y], [hi_x, hi_y]]
</pre>

      <p>
        Stepping back,
        the most important lesson in this episode isn't the details of the Nose library.
        It's that our time is more valuable than the computer's,
        so we should spend it doing the things the computer can't,
        like thinking of interesting test cases and what our code is actually supposed to do.
        Nose and other libraries like it are there to handle
        all the things that we <em>shouldn't</em> have to re-think each time.
        They will also help guide we toward good practices,
        to make our testing and programming more productive.
      </p>

      <p>
        Testing tells us whether our program is doing what it's supposed to do.
        But if it's done right,
        it will also tell us <em>what</em> our program actually <em>is</em> supposed to be doing.
        As we saw earlier,
        we can think of tests as runnable specifications of a program's behavior.
        Unlike design documents or comments in the code,
        we can actually run our tests,
        so it's harder for them to fall out of sync with the program's actual behavior.
        In well-run projects,
        tests also act as examples to show newcomers how the code should be used,
        and how it's supposed to behave under different circumstances.
      </p>

      <div class="box">
        <h3>Assertions and Tests</h3>

        <p>
          Some people believe that every time a bug is fixed,
          the programmer should add assertions to the program
          to catch it if it ever reappears.
          Other people believe that tests should be used for this,
          i.e.,
          that when a bug is found,
          the programmer should write a test that fails if the bug is present,
          but passes if the bug is fixed.
          Both are good practices,
          and over time,
          individual programmers and projects usually settle on a mix of the two.
        </p>
      </div>

      <div class="keypoints" id="k:unit">
        <h3>Summary</h3>
        <ul>
          <li>Testing cannot prove that a program is correct, but is still worth doing.</li>
          <li>Use a unit testing library like Nose to test short pieces of code.</li>
          <li>Write each test as a function that creates a fixture, executes an operation, and checks the result using assertions.</li>
          <li idea="paranoia">Every test should be able to run independently: tests should <em>not</em> depend on one another.</li>
          <li>Focus testing on boundary cases.</li>
          <li idea="perf">Writing tests helps us design better code by clarifying our intentions.</li>
        </ul>
      </div>

    </section>

    <section id="s:numbers">

      <h2>Numbers</h2>

      <div class="understand" id="u:numbers">
        <h3>Understand:</h3>
        <ul>
          <li>How computers represent numbers.</li>
          <li>That floating point numbers are inexact, uneven approximations of real numbers.</li>
          <li>The difference between absolute error and relative error.</li>
          <li>That tests of numerical code should be written in terms of relative error.</li>
          <li>Three strategies for testing numerical programs.</li>
        </ul>
      </div>

      <p>
        Let's start by looking at how numbers are stored.
        If we only have the two digits 0 and 1,
        the natural way to store a positive integer is to use base 2,
        so 1001<sub>2</sub> is (1&times;2<sup>3</sup>)+(0&times;2<sup>2</sup>)+(0&times;2<sup>1</sup>)+(1&times;2<sup>0</sup>) = 9<sub>10</sub>.
        It's equally natural to extend this scheme to negative numbers by reserving one bit for the sign.
        If, for example, we use 0 for positive numbers and 1 for those that are negative,
        +9<sub>10</sub> would be 01001<sub>2</sub> and -9<sub>10</sub> would be 11001<sub>10</sub>.
      </p>

      <p>
        There are two problems with this.
        The first is that this scheme gives us two representations for zero (00000<sub>2</sub> and 10000<sub>2</sub>).
        This isn't necessarily fatal,
        but any claims this scheme has to being "natural" disappear when we have to write code like:
      </p>

<pre>
if (length != +0) and (length != -0):
</pre>

      <p>
        As for the other problem,
        it turns out that the circuits needed to do addition and other arithmetic on this
        <a href="glossary.html#sign-and-magnitude">sign and magnitude representation</a>
        are more complicated than the hardware needed for another called
        <a href="glossary.html#twos-complement">two's complement</a>.
        Instead of mirroring positive values,
        two's complement rolls over when going below zero,
        just like a car's odometer.
        If we're using four bits per number,
        so that 0<sub>10</sub> is 0000<sub>2</sub>,
        then -1<sub>10</sub> is 1111<sub>2</sub>.
        -2<sub>10</sub> is 1110<sub>2</sub>,
        -3<sub>10</sub> is 1101<sub>2</sub>,
        and so on until we reach the most negative number we can represent,
        1000<sub>2</sub>, which is -8.
        Our representation then wraps around again, so that 0111<sub>2</sub> is 7<sub>10</sub>.
      </p>

      <p>
        This scheme isn't intuitive,
        but it solves sign and magnitude's "double zero" problem,
        and the hardware to handle it is faster and cheaper.
        As a bonus,
        we can still tell whether a number is positive or negative by looking at the first bit:
        negative numbers have a 1, positives have a 0.
        The only odd thing is its asymmetry:
        because 0 counts as a positive number,
        numbers go from -8 to 7, or -16 to 15, and so on.
        As a result, even if <code>x</code> is a valid number, <code>-x</code> may not be.
      </p>

      <p>
        Finding a good representation for real numbers
        (called <a href="#glossary.html#floating-point">floating point numbers</a>,
        since the decimal point can move around)
        is a much harder problem.
        The root of the problem is that
        we cannot represent an infinite number of real values with a finite set of bit patterns.
        And unlike integers,
        no matter what values we <em>do</em> represent,
        there will be an infinite number of values between each of them that we can't.
      </p>

      <p>
        Floating point numbers are usually represented using sign, magnitude, and an exponent.
        In a 32-bit word,
        the IEEE&nbsp;754 standard calls for 1 bit of sign,
        23 bits for the magnitude (or <em>mantissa</em>),
        and 8 bits for the exponent.
        To illustrate the problems with floating point,
        we'll use a much dumber representation:
        we'll only worry about positive values without fractional parts,
        and we'll only use 3 for the magnitude and 2 for the exponent.
      </p>

      <p>
        <a href="#f:simple_float">Figure XXX</a>
        shows the values that we can represent this way.
        Each one is the mantissa times two to the exponent.
        For example, the decimal values 48 is binary 110 times 2 to the binary 11 power,
        which is 6 times 2 to the third,
        or 6 times 8.
        (Note that real floating point representations like the IEEE&nbsp;754 standard
        don't have the redundancy shown in this table,
        but that doesn't affect our argument.)
      </p>

      <figure id="f:simple_float">
        <img src="img/numpy/simple_float.png" alt="Simple Representation of Floating Point Numbers" />
      </figure>

      <p>
        The first thing you should notice is that there are a lot of values we <em>can't</em> store.
        We can do 8 and 10, for example, but not 9.
        This is exactly like the problems hand calculators have with fractions like 1/3:
        in decimal, we have to round that to 0.3333 or 0.3334.
      </p>

      <p>
        But if this scheme has no representation for 9,
        then 8+1 must be stored as either 8 or 10.
        This raises an interesting question:
        if 8+1 is 8, what is 8+1+1?
        If we add from the left, 8+1 is 8, plus another 1 is 8 again.
        If we add from the right, though, 1+1 is 2, and 2+8 is 10.
        Changing the order of operations can make the difference between right and wrong.
        There's no randomness involved&mdash;a particular order of operations
        will always produce the same result&mdash;but
        as the number of steps increases,
        so too does the difficulty of figuring out what the best order is.
      </p>

      <p>
        This is the sort of problem that numerical analysts spend their time on.
        In this case, if we sort the values we're adding, then add from smallest to largest,
        it gives us a better chance of getting the best possible answer.
        In other situations,
        like inverting a matrix,
        the rules are much more complicated.
      </p>

      <p>
        Here's another observation about our uneven number line:
        the spacing between the values we can represent is uneven,
        but the relative spacing between each set of values stays the same,
        i.e., the first group is separated by 1, then the separation becomes 2, then 4, then 8,
        so that the ratio of the spacing to the values stays roughly constant.
        This happens because we're multiplying the same fixed set of mantissas by ever-larger exponents,
        and it points us at a couple of useful definitions.
      </p>

      <p>
        The <a href="glossary.html#absolute-error">absolute error</a> in some approximation
        is simply the absolute value of the difference between the actual value and the approximation.
        The <a href="glossary.html#relative-error">relative error</a>,
        on the other hand,
        is the ratio of the absolute error to the value we're approximating.
        For example, if we're off by 1 in approximating 8+1 and 56+1,
        the absolute error is the same in both cases,
        but the relative error in the first case is 1/9 = 11%,
        while the relative error in the second case is only 1/57 = 1.7%.
        When we're thinking about floating point numbers,
        relative error is almost always more useful than absolute error.
        After all,
        it makes little sense to say that we're off by a hundredth when the value in question is a billionth.
      </p>

      <p>
        To see why this matters, let's have a look at a little program:
      </p>

<pre src="src/numpy/nines.py">
nines = []
sums = []
current = 0.0
for i in range(1, 10):
    num = 9.0 / (10.0 ** i)
    nines.append(num)
    current += num
    sums.append(current)
for i in range(len(nines)):
    print '%.18f %.18f' % (nines[i], sums[i])
</pre>

      <p class="continue">
        The loop runs over the integers from 1 to 9 inclusive.
        Using those values, we create the numbers 0.9, 0.09, 0.009, and so on, and put them in the list <code>vals</code>.
        We then calculate the sum of those numbers.
        Clearly, this should be 0.9, 0.99, 0.999, and so on.
        But is it?
      </p>

      <table>
        <tr><td>1</td><td>0.900000000000000022</td><td>0.900000000000000022</td></tr>
        <tr><td>2</td><td>0.089999999999999997</td><td>0.989999999999999991</td></tr>
        <tr><td>3</td><td>0.008999999999999999</td><td>0.998999999999999999</td></tr>
        <tr><td>4</td><td>0.000900000000000000</td><td>0.999900000000000011</td></tr>
        <tr><td>5</td><td>0.000090000000000000</td><td>0.999990000000000046</td></tr>
        <tr><td>6</td><td>0.000009000000000000</td><td>0.999999000000000082</td></tr>
        <tr><td>7</td><td>0.000000900000000000</td><td>0.999999900000000053</td></tr>
        <tr><td>8</td><td>0.000000090000000000</td><td>0.999999990000000061</td></tr>
        <tr><td>9</td><td>0.000000009000000000</td><td>0.999999999000000028</td></tr>
      </table>

      <p>
        Here are our answers.
        The first column is the loop index;
        the second, what we actually got when we tried to calculate 0.9, 0.09, and so on,
        and the third is the cumulative sum.
      </p>

      <p>
        The first thing you should notice is that the very first value contributing to our sum is already slightly off.
        Even with 23 bits for a mantissa,
        we cannot exactly represent 0.9 in base 2,
        any more than we can exactly represent 1/3 in base 10.
        Doubling the size of the mantissa would reduce the error,
        but we can't ever eliminate it.
      </p>

      <p>
        The second thing to notice is that our approximation to 0.0009 actually appears accurate,
        as do all of the approximations after that.
        This may be misleading, though:
        after all,
        we've only printed things out to 18 decimal places.
        As for the errors in the last few digits of the sums,
        there doesn't appear to be any regular pattern in the way they increase and decrease.
      </p>

      <p>
        This phenomenon is one of the things that makes testing scientific programs hard.
        If a function uses floating point numbers,
        what do we compare its result to
        if we want to check that it's working correctly?
        If we compared the sum of the first few numbers in <code>vals</code> to what it's supposed to be,
        the answer could be <code>False</code>,
        even if we're initializing the list with the right values,
        and calculating the sum correctly.
        This is a genuinely hard problem,
        and no one has a good generic answer.
        The root of our problem is that we're using approximations,
        and each approximation has to be judged on its own merits.
      </p>

      <p>
        There are things you can do, though.
        The first rule is,
        compare what you get to analytic solutions whenever you can.
        For example,
        if you're looking at the behavior of drops of liquid helium,
        start by checking your program's output on a stationary spherical drop in zero gravity.
        You should be able to calculate the right answer in that case,
        and if your program doesn't work for it,
        it probably won't work for anything else.
      </p>

      <p>
        The second rule is to compare more complex versions of your code to simpler ones.
        If you're about to replace a simple algorithm for calculating heat transfer with one that's more complex,
        but hopefully faster,
        don't throw the old code away.
        Instead,
        use its output as a check on the correctness of the new code.
        And if you bump into someone at a conference who has a program that can calculate some of the same results as yours,
        swap data sets:
        it'll help you both.
      </p>

      <p>
        The third rule is, never use <code>==</code> (or <code>!=</code>) on floating point numbers,
        because two numbers calculated in different ways will probably not have exactly the same bits.
        Instead,
        check to see whether two values are within some tolerance,
        and if they are,
        treat them as equal.
        Doing this forces you to make your tolerances explicit,
        which is useful in its own right
        (just as putting error bars on experimental results is useful).
      </p>

      <p>
        Finally,
        and most importantly,
        if you're doing any calculation on a computer at all,
        take half an hour to read Goldberg's excellent paper,
        "<a href="bib.html#goldberg-floating-point">What Every Computer Scientist Should Know About Floating-Point Arithmetic</a>".
      </p>

      <div class="keypoints" id="k:numbers">
        <h3>Summary</h3>
        <ul>
          <li>Floating point numbers are approximations to actual values.</li>
          <li>Use tolerances rather than exact equality when comparing floating point values.</li>
          <li>Use integers to count and floating point numbers to measure.</li>
          <li>Most tests should be written in terms of relative error rather than absolute error.</li>
          <li>When testing scientific software, compare results to exact analytic solutions, experimental data, or results from simpler or previously-tested programs.</li>
        </ul>
      </div>

    </section>

    <section id="s:coverage">

      <h2>Coverage</h2>

      <div class="understand" id="u:coverage">
        <h3>Understand:</h3>
        <ul>
          <li>What code coverage is.</li>
          <li>How to use tools to calculate code coverage.</li>
          <li>Why complete code coverage doesn't guarantee that code has been fully tested.</li>
          <li>How to use coverage to guide testing effort.</li>
        </ul>
      </div>

      <p>
        The <a href="glossary.html#code-coverage">code coverage</a> of a set of tests
        is the percentage of the application code those tests exercise.
        For example,
        suppose our function is:
      </p>

<pre>
def sign(num):
    if num &lt; 0:
        return -1
    if num == 0:
        return 0
    return 1
</pre>

      <p class="continue">
        If our entire test suite consists of:
      </p>

<pre>
def test_positive_number():
    assert sign(-1) == -1
</pre>

      <p class="continue">
        then only three of the six lines in the function are actually being tested:
      </p>

<pre>
<span class="highlight">def sign(num):
    if num &lt; 0:
        return -1</span>
    if num == 0:
        return 0
    return 1
</pre>

      <p class="continue">
        so the coverage is only 50%.
        If we add a second test:
      </p>

<pre>
def test_zero():
    assert sign(0.0) == 0
</pre>

      <p class="continue">
        the coverage goes to 83%,
        and if we add a third:
      </p>

<pre>
def test_positive():
    assert sign(172891) &gt; 0
</pre>

      <p class="continue">
        the coverage reaches 100%.
      </p>

      <p>
        Code coverage is often used as a rough indication of
        how well tested a piece of software is&mdash;after all,
        if the coverage of a set of tests is less than 100%,
        then some lines of code aren't being tested at all.
        However,
        even 100% coverage doesn't guarantee that code has been completely tested.
        To see why,
        consider the following code
        (adapted from <a href="http://nedbatchelder.com/blog/200710/flaws_in_coverage_measurement.html">this example</a>):
      </p>

<pre src="src/quality/sensitivity.py">
def sensitivity(alpha, beta):
    if alpha:
        factor = 0
    else:
        factor = 2

    if beta:
        result = 2.0/factor
    else:
        result = factor/2.0

    return result
</pre>

      <p class="continue">
        These three tests achieve 100% code coverage:
      </p>

<pre>
def test_neither():
    assert sensitivity(False, False) == 1

def test_alpha_only():
    assert sensitivity(True, False) == 0

def test_beta_only():
    assert sensitivity(False, True) == 1
</pre>

      <p class="continue">
        but <code>sensitivity(True, True)</code> still fails with a <code>ZeroDivisionError</code>.
        The problem is that the tests don't achieve 100% <a href="glossary.html#path-coverage">path coverage</a>:
        even though every line is exercised at least once,
        there are paths through the code that aren't ever taken
        (<a href="#f:path_coverage">Figure XXX</a>).
      </p>

      <figure id="f:path_coverage">
        <img src="img/quality/path_coverage.png" alt="Line Coverage vs. Path Coverage" />
      </figure>

      <p>
        While code coverage isn't sufficient to show that everything has been tested,
        it is still useful.
        In particular,
        looking at which lines have and have not been exercised
        in a newly-written or modified piece of code
        can help developers think of tests they should write.
        The simplest tool to use for calculating coverage in Python is <code>coverage.py</code>.
        To see how it works,
        suppose <code>sensitivity.py</code> contains the following:
      </p>

<pre src="src/quality/sensitivity.py">
def sensitivity(alpha, beta):
    if alpha:
        factor = 0
    else:
        factor = 2

    if beta:
        result = 2.0/factor
    else:
        result = factor/2.0

    return result

assert sensitivity(False, False) == 1
assert sensitivity(True, False) == 0
</pre>

      <p class="continue">
        If we run the coverage tool from the shell  using:
      </p>

<pre>
$ coverage sensitivity.py
</pre>

      <p class="continue">
        it creates a file called <code>.coverage</code>
        that records which lines were executed.
        This file isn't text,
        so opening it in an editor isn't useful;
        instead,
        to see what we did and didn't exercise,
        we run:
      </p>

<pre>
$ coverage html
</pre>

      <p class="continue">
        which creates a directory called <code>htmlcov</code>,
        inside which is a page called <code>index.html</code>.
        When we open this in a browser,
        we see a summary of the coverage statistics:
      </p>

      <table>
        <thead>
          <tr>
            <th>Module</th>
            <th>statements</th>
            <th>missing</th>
            <th>excluded</th>
            <th>coverage</th>
          </tr>
        </thead>
        <tfoot>
          <tr>
            <td>Total</td>
            <td>10</td>
            <td>1</td>
            <td>0</td>
            <td align="right">90%</td>
          </tr>
        </tfoot>
        <tbody>
          <tr>
            <td><u>sensitivity</u></td>
            <td>10</td>
            <td>1</td>
            <td>0</td>
            <td align="right">90%</td>
          </tr>
        </tbody>
      </table>

      <p>
        If we follow the link to <code>sensitivity.py</code>,
        we see:
      </p>

      <div>
        <p><strong>Coverage for sensitivity : 90%</strong></p>
        <p>10 statements 9 run 1 missing 0 excluded</p>
<pre>
 1  def sensitivity(alpha, beta):
 2      if alpha:
 3          factor = 0
 4      else:
 5          factor = 2
 6
 7      if beta:
 8<span class="highlight">          result = 2.0/factor</span>
 9      else:
10          result = factor/2.0
11
12      return result
13
14  assert sensitivity(False, False) == 1
15  assert sensitivity(True, False) == 0
</pre>

      </div>

      <p class="continue">
        which tells us that line 8 hasn't been run.
        It's up to us to figure out why not,
        and what to do about it,
        but at least we now know what our problem is.
      </p>

      <div class="keypoints" id="k:coverage">
        <h3>Summary</h3>
        <ul>
          <li idea="paranoia">Use a coverage analyzer to see which parts of a program have been tested and which have not.</li>
        </ul>
      </div>

    </section>

    <section id="s:debug">

      <h2>Debugging</h2>

      <div class="understand" id="u:debug">
        <h3>Understand:</h3>
        <ul>
          <li>Why using <code>print</code> statements to debug is inefficient.</li>
          <li>What a symbolic debugger is.</li>
          <li>How to set a breakpoint in a debugger.</li>
          <li>How to inspect values using a debugger.</li>
          <li>How to debug programs systematically.</li>
        </ul>
      </div>

      <p>
        Programmers spend a lot of time debugging,
        so it's worth learning how to do it systematically.
        We'll talk about tools first,
        since they'll make everything else less painful.
        We'll then talk about some techniques.
        Throughout,
        we'll assume that we built the right thing the wrong way;
        requirements errors are actually a major cause of software project failure,
        but they're out of scope for now.
      </p>

      <p>
        When something goes wrong in a program like this:
      </p>

<pre src="src/quality/to_debug.py">
import sys

def insert_or_increment(counts, species, number):
    # Look for species in list.
    for (s, n) in counts:
        # If we have seen it before, add to its count and exit.
        if s == species:
            n += number
            return
    # Haven't seen it before, so add it.
    counts.append([species, number])

source = open(sys.argv[1], 'r')
counts = []
for line in source:
    species, number = line.strip().split(',')
    insert_or_increment(counts, species, int(number))
counts.sort()
for (s, n) in counts:
    print '%s: %d' % (s, n)
</pre>

      <p class="continue">
        most people start debugging by adding <code>print</code> statements:
      </p>

<pre src="src/quality/debug_print.py">
def insert_or_increment(counts, species, number):
    # Look for species in list.
    <span class="highlight">print 'insert_or_increment(', counts, ',', species, ',', number, ')'</span>
    for (s, n) in counts:
        <span class="highlight">print '...checking against', s, n</span>
        # If we have seen it before, add to its count and exit.
        if s == species:
            n += number
            <span class="highlight">print '...species matched, so returning with', counts</span>
            return
    # Haven't seen it before, so add it.
    counts.append([species, number])
    <span class="highlight">print 'new species, so returning with', counts</span>
</pre>

      <p class="continue">
        and then paging through output like this:
      </p>

<pre src="src/quality/debug_print.txt">
insert_or_increment( [] , marlin , 5 )
new species, so returning with [['marlin', 5]]
insert_or_increment( [['marlin', 5]] , shark , 2 )
...checking against marlin 5
new species, so returning with [['marlin', 5], ['shark', 2]]
insert_or_increment( [['marlin', 5], ['shark', 2]] , marlin , 1 )
...checking against marlin 5
...species matched, so returning with [['marlin', 5], ['shark', 2]]
insert_or_increment( [['marlin', 5], ['shark', 2]] , turtle , 5 )
...checking against marlin 5
...checking against shark 2
new species, so returning with [['marlin', 5], ['shark', 2], ['turtle', 5]]
insert_or_increment( [['marlin', 5], ['shark', 2], ['turtle', 5]] , herring , 3 )
...checking against marlin 5
...checking against shark 2
...checking against turtle 5
new species, so returning with [['marlin', 5], ['shark', 2], ['turtle', 5], ['herring', 3]]
insert_or_increment( [['marlin', 5], ['shark', 2], ['turtle', 5], ['herring', 3]] , herring , 4 )
...checking against marlin 5
...checking against shark 2
...checking against turtle 5
...checking against herring 3
...species matched, so returning with [['marlin', 5], ['shark', 2], ['turtle', 5], ['herring', 3]]
insert_or_increment( [['marlin', 5], ['shark', 2], ['turtle', 5], ['herring', 3]] , marlin , 1 )
...checking against marlin 5
...species matched, so returning with [['marlin', 5], ['shark', 2], ['turtle', 5], ['herring', 3]]
herring: 3
marlin: 5
shark: 2
turtle: 5
</pre>

      <p>
        This works for small problems&mdash;i.e.,
        it gives the programmer enough insight into the problem to fix it&mdash;but
        it doesn't scale to larger programs or harder problems.
        First,
        adding print statements is a good way to add typos,
        particularly when we have to modify the block structure of the program
        to fit them in.
        It's also time-consuming to type things,
        delete them,
        type more in,
        and so on.
        It's especially tedious if we're working in a language like C++, Fortran, or Java
        that requires compilation.
        Finally,
        if we're printing lots of information,
        it's all too easy to miss the crucial bit as it flies by on the screen.
      </p>

      <p>
        A <a href="glossary.html#debugger">debugger</a> is
        a program that controls the execution of some
        <a href="glossary.html#target-program">target program</a>&mdash;typically,
        one that has a bug in it that we're trying to track down.
        Debuggers are more properly called <em>symbolic</em> debuggers
        because they show us the source code we wrote,
        rather than raw machine instructions
        (although debuggers exists to do that too).
        While the target program is running,
        the debugger can:
      </p>

      <ul>
        <li>
          pause, resume, or restart it;
        </li>
        <li>
          display or change values in it; and
        </li>
        <li>
          watch for calls to particular functions or changes to particular variables.
        </li>
      </ul>

      <p>
        Here's what a typical debugger looks like in action:
      </p>

      <figure id="f:debugger_screenshot">
        <img src="img/quality/debugger_screenshot.png" alt="A Debugger in Action" />
      </figure>

      <p>
        The most important parts of this display are
        the source code window and the call stack display.
        The former shows us where we are in the program;
        the latter,
        what variables are in scope and what their values are.
        Most debuggers also display whatever the target program has printed to standard output recently.
      </p>

      <p>
        We typically start a debugging session by setting
        a <a href="glossary.html#breakpoint">breakpoints</a> in the target program.
        This tells the debugger to suspend the target program whenever it reaches that line
        so that we can inspect the program's state.
        For example,
        <a href="#f:debugger_screenshot">Figure XXX</a> shows the state of the program
        when adding four herrings to the list of species' counts.
        The program is paused while it processes the first entry in the list
        to let us explore our data and call stack,
        without having to modify the code in any way.
        We can also use the debugger to:
      </p>

      <ul>
        <li>
          <a href="glossary.html#single-step">single-step</a>,
          i.e., execute one statement at a time;
        </li>
        <li>
          <a href="glossary.html#step-into">step into</a> function calls;
        </li>
        <li>
          <a href="glossary.html#step-over">step over</a> them; or
        </li>
        <li>
          run to the end of the current function.
        </li>
      </ul>

      <p class="continue">
        This allows us to see how values are changing,
        which branches the program is actually taking,
        which functions are actually being called,
        and most importantly,
        why.
      </p>

      <p>
        But debuggers can do much more than this.
        For example,
        most debuggers let us move up and down the call stack,
        so that when our program is halted,
        we can see the current values of variables in <em>any</em> active function call,
        not just the one we're in.
      </p>

      <p>
        Most debuggers also support
        <a href="glossary.html#conditional-breakpoint">conditional breakpoints</a>,
        which only takes effect if some condition is met.
        For example,
        we can set a breakpoint inside a loop so that the target program only halts
        when the loop index is greater than 100.
        This saves us having to step through 100 uninteresting iterations of the loop.
      </p>

      <p>
        We can also use the debugger to modify values while the program is running.
        For example,
        suppose we have a theory about why a bug is occurring.
        We can run the target program to that point,
        change the value of a particular variable,
        then resume the target program.
        This trick is sometimes used to test out error-handling code,
        since it's easier to change <code>time_spent_waiting</code> to 600 seconds in debugger
        than to pull out the network cable and wait ten minutes&hellip;
      </p>

      <div class="box">
        <h3>Post Mortem</h3>

        <p>
          Debuggers for compiled languages often support
          <a href="glossary.html#post-mortem-debugging">post mortem debugging</a>.
          When a program fails badly,
          it creates a <a href="glossary.html#core-dump">core dump</a>:
          a large file containing a bitwise copy of
          everything that was in the program's memory.
          A post-mortem debugger loads that memory image into the debugger
          to see where it was and what state it was in when it failed.
          This isn't as useful as watching it run,
          but sometimes the best you can do
        </p>
      </div>

      <p>
        Many people recommend using the scientific method to debug programs
        (e.g., David Agans' book <a href="bib.html#agans-debugging"><cite>Debugging</cite></a>).
        In practice,
        though,
        most programmers don't do this.
        Instead,
        what <a href="bib.html#lawrance-debug-foraging">Lawrance and colleagues</a> found is that
        they forage for information by
        reading the code and (re-)running the program
        to build up a mental model of what it's doing
        until they see where the bug is,
        then make a change and see if it has the desired effect.
      </p>

      <p>
        No matter how we think of it,
        systematic (i.e., productive) debugging follows a few simple rules.
        First,
        <em>try to get it right the first time</em>,
        since the simplest bugs to fix are the ones that don't exist.
        Most of the techniques we have discussed in this chapter,
        such as defensive programming and test-driven development,
        are meant to accomplish this.
      </p>

      <p>
        Second,
        make sure that we <em>know what the program is supposed to do</em>.
        If we don't know that the output or behavior is supposed to be,
        we can't even be sure there <em>is</em> a bug,
        much less whether we've fixed it.
      </p>

      <div class="box">
        <h3>Extrapolation is the Root of Many Evils</h3>

        <p>
          If the case is covered by a test case,
          then we're in good shape;
          if it isn't,
          we need to ask whether we actually know enough to create that test case.
          In particular,
          if this situation isn't covered by
          the formulas we're trying to implement,
          or whatever other specification we've been given,
          we need to ask whether we have the right to extrapolate and fill in the blank.
        </p>
      </div>

      <p>
        Third,
        <em>make sure it's plugged in</em>,
        i.e.,
        make sure we're actually exercising the problem that we think we are.
        Are we giving it the right test data?
        Is it configured the way we think it is?
        Is it the version we think it is?
        Has the feature that's "failing" actually been implemented yet?
        It's very easy&mdash;particularly when we're tired or frustrated&mdash;to spend
        hours trying to debug a failure
        that doesn't actually exist.
      </p>

      <p>
        The next rule of debugging is <em>make it fail reliably</em>.
        We can only debug things when they go wrong;
        if we can't find a test case that fails every time,
        we're going to waste a lot of time watching the program <em>not</em> fail.
      </p>

      <p>
        What if we can't make it fail reliably?
        What if the problem involves timing,
        random numbers,
        network load,
        or something we just haven't figured out yet?
        In that case,
        we should apply rule number four:
        <em>divide and conquer</em>.
        The smaller the gap between cause and effect,
        the easier the relationship is to see,
        so once we have a case that fails,
        we should try to simplify it
        so that we have less of the program to worry about.
      </p>

      <p>
        If we can simplify the failure by using smaller or simpler input,
        without modifying our program,
        we should do so.
        If we have to modify the program,
        the best way is to start adding assertions.
        Does the failure first show up in function X?
        If so,
        add an assertion at the start of the function to make sure its inputs are valid.
        If they aren't,
        add assertions at the start of the functions that call X,
        and so on.
        This is a good way to stop ourselves from introducing new bugs as you fix old ones,
        since we can leave those assertions in the code forever if we want.
      </p>

      <p>
        The corollary to rule number 4 is rule number 5:
        <em>change one thing at a time</em>.
        The more things we change at once,
        the harder it is to keep track of what we've done
        and what effect it had.
        Every time we make a change,
        even a small one,
        we should re-run all of our tests immediately.
      </p>

      <p>
        Finally,
        the most important rule is <em>be humble</em>.
        Don't keep telling yourself why it <em>should</em> work:
        if it doesn't, it doesn't.
        And don't be too proud to ask for help:
        if you can't find the problem in 15 minutes,
        ask someone rather than spending another hour banging your head against a wall.
      </p>

      <div class="keypoints" id="k:debug">
        <h3>Summary</h3>
        <ul>
          <li>Use an interactive symbolic debugger instead of <code>print</code> statements to diagnose problems.</li>
          <li>Set breakpoints to halt the program at interesting points instead of stepping through execution.</li>
          <li>Try to get things right the first time.</li>
          <li>Make sure you know what the program is supposed to do before trying to debug it.</li>
          <li>Make sure the program is actually running the test case you think it is.</li>
          <li>Make the program fail reliably.</li>
          <li>Simplify the test case or the program in order to localize the problem.</li>
          <li>Change one thing at a time.</li>
          <li>Be humble.</li>
        </ul>
      </div>

    </section>

    <section id="s:testable">

      <h2>Designing Testable Code</h2>

      <div class="understand" id="u:testable">
        <h3>Understand:</h3>
        <ul>
          <li>The difference between interface and implementation.</li>
          <li>Why testing should focus on interfaces rather than implementations.</li>
          <li>Why and how to replace software components with simplified versions of themselves during testing.</li>
        </ul>
      </div>

      <p>
        One of the most important ideas in computing is the difference between <em>interface</em> and <em>implementation</em>.
        Something's <a href="glossary.html#interface">interface</a> specifies how it interacts with the world:
        what it will accept as input, and what output it produces.
        Again,
        it's like a contract in business:
        if Party A does X, then Party B guarantees Y.
      </p>

      <p>
        Something's <a href="glossary.html#implementation">implementation</a> is how it accomplishes whatever it does.
        This might involve calculation, database lookups, or anything else.
        The key is, it's hidden inside the thing:
        how it does what it does is nobody else's business.
        For example,
        here's an outline for a Python function
        that integrates a function of one variable over a certain interval:
      </p>

<pre>
def integrate(func, x1, x2):
    ...math goes here...
    return result
</pre>

      <p class="continue">
        Its interface is simple:
        given a function and the low and high bounds on the interval,
        it returns the appropriate integral.
        A fuller definition of its interface would also specify
        how it behaves when it's given bad parameters,
        error bounds on the result,
        and so on.
      </p>

      <p>
        Its implementation could use any of a dozen algorithms.
        In fact,
        its implementation could change over time as new algorithms are developed.
        As long as its contract with the outside world stays the same,
        none of the programs that use it should need to change.
        This allows users to concentrate on their tasks,
        while giving whoever wrote this function the freedom to tweak it without making work for other people.
      </p>

      <p>
        We often use this idea&mdash;the separation between interface and implementation&mdash;to simplify unit testing.
        The goal of unit testing is to test the components of a program one by one&mdash;that's
        why it's called "unit" testing.
        But the components in real programs almost always depend on each other:
        this function calls that one,
        this data structure refers to the one over there,
        and so on.
        How can we isolate the component under test from the rest of the program
        so that we can test it on its own?
      </p>

      <p>
        One technique is to replace the components we're <em>not</em> currently testing
        with simplified versions that have the same interfaces,
        but much simpler implementations,
        just as a director would use a stand-in rather than a star when fiddling with the lighting for a show.
        Doing this for programs that have already been written
        sometimes requires some reorganization, or <a href="glossary.html#refactor">refactoring</a>.
        But once we understand the technique,
        we can build programs with it in mind to make testing easier.
      </p>

      <p>
        Let's go back to our photographs of fields in Saskatchewan.
        We want to test a function that reads a photo from a file.
        (Remember that a photo is just a set of rectangles.)
        Here's a plausible outline of the function:
      </p>

<pre>
def read_photo(filename):
    result = set()
    reader = open(filename, 'r')
    ...fill result with rectangles in file...
    reader.close()
    return result
</pre>

      <p class="continue">
        It creates a set to hold the rectangles making up the photo,
        opens a file,
        and then reads rectangles from the file and puts them in the set.
        When the input is exhausted,
        the function closes the file and returns the set.
      </p>

      <p>
        Here is a unit test for that function
        that reads data from a file called <code>unit.pht</code>,
        then checks that the result is a set containing exactly one rectangle:
      </p>

<pre>
def test_photo_containing_only_unit():
    assert read_photo('unit.pht') == { ((0, 0), (1, 1)) }
</pre>

      <p>
        This is pretty straightforward,
        but experience teaches us that it's a bad way to organize things.
        First,
        this test depends on an external file,
        and on that file being in exactly the right place.
        Over time,
        files can be lost,
        or moved around,
        which makes tests that depend on them break.
      </p>

      <p>
        Second,
        it's hard to understand a test if the fixture it depends on isn't right there with it.
        Yes,
        it's easy to open the file and read it,
        but every bit of extra effort is a bit less testing people will actually do.
      </p>

      <p>
        Third,
        file I/O is slower than doing things in memory&mdash;tens or hundreds of thousands of times slower.
        If your program has hundreds of tests,
        and each one takes a second to run,
        developers will have to wait several minutes to find out whether their latest change has broken anything that used to work.
        The most likely result is that they'll run the tests much less frequently,
        which means they'll waste more time backtracking to find and fix bugs
        that could have been caught when they were fresh if the tests only took seconds to run.
      </p>

      <p>
        Here's how to fix this.
        Imagine for a moment that instead of reading rectangles, we're just counting them:
      </p>

<pre>
def count_rect(filename):
    reader = open(filename, 'r')
    count = 0
    for line in reader:
        count += 1
    reader.close()
    return count
</pre>

      <p class="continue">
        This simple function assumes the file contains one rectangle per line,
        with no blank lines or comments.
        (Of course,
        a real rectangle counting function would probably be more sophisticated,
        but this is enough to illustrate our point.)
        Here's the function after refactoring:
      </p>

<pre>
def count_rect_in(reader):
    count = 0
    for line in reader:
        count += 1
    return count

def count_rect(filename):
    reader = open(filename, 'r')
    result = count_rect_in(reader)
    reader.close()
    return result
</pre>

      <p class="continue">
        We've taken the inner core of the original function and made it a function in its own right.
        This new function does the actual work&mdash;i.e.,
        it counts rectangles&mdash;but
        it does <em>not</em> open the file that the rectangles are read from.
        That's still done by the original function.
        It opens the input file,
        calls the new function that we extracted,
        then closes the file and returns the result.
        Notice that this function keeps the name of the original function,
        so that any program that used to call <code>count_rect</code> can still do so.
      </p>

      <p>
        Now let's write some tests:
      </p>

<pre>
from StringIO import StringIO

Data = '''0 0 1 1
1 0 2 1
2 0 3 1'''

def test_num_rect():
    reader = StringIO(Data)
    assert count_rect_in(reader) == 3
</pre>

      <p class="continue">
        This piece of code checks that <code>count_rect_in</code>&mdash;the
        function that actually does the hard work&mdash;handles
        the three-rectangle case properly.
        But instead of an external file,
        we're using a string in the test program as a fixture.
      </p>

      <p>
        To make this string look like a file,
        we're relying on a Python class called <code>StringIO</code>.
        As the name suggests,
        this acts like a file,
        but uses a string instead of the disk for storing data.
        <code>StringIO</code> has all the same methods as a file,
        like <code>readline</code>,
        so <code>count_rect_in</code> doesn't know that it isn't reading from a real file on disk.
      </p>

      <p>
        We can use this same trick to test functions that are supposed to write to files as well.
        For example,
        here's a unit test to check that another function,
        <code>photo_write_to</code>,
        can correctly write out a photo containing only the unit square:
      </p>

<pre>
def test_write_unit_only():
    fixture = { ((0, 0), (1, 1)) }
    writer = StringIO()
    photo_write_to(fixture, writer)
    result = writer.getvalue()
    assert result == '0 0 1 1\n'
</pre>

      <p class="continue">
        Once again,
        we create a <code>StringIO</code> and pass that to the function instead of an actual open file.
        If <code>photo_write_to</code> only writes to the file using the methods that real files provide,
        it won't know that it's been passed something else.
        And once we're finished writing,
        we can call <code>getvalue</code> to get the text that we wrote,
        and check it to make sure it's what it's supposed to be.
      </p>

      <p>
        In order to make output testable,
        though,
        there's one more thing we have to do.
        Here's a possible implementation of <code>photo_write_to</code>:
      </p>

<pre>
def photo_write_to(photo, writer):
    contents = list(photo)
    contents.sort()
    for rect in contents:
        print &gt;&gt; writer, rect[0][0], rect[0][1],
                         rect[1][0], rect[1][1]
</pre>

      <p class="continue">
        It puts the rectangles in the photo into a list,
        sorts that list,
        then writes the rectangles one by one.
        Why do the extra work of sorting?
        Why not just loop over the set and write the rectangles out directly?
      </p>

      <p>
        Let's work backwards to the answer.
        This version of <code>photo_write_to</code> is shorter and faster than the previous one:
      </p>

<pre>
def photo_write_to(photo, writer):
    contents = list(photo)
    for rect in contents:
        print &gt;&gt; writer, rect[0][0], rect[0][1],
                         rect[1][0], rect[1][1]
</pre>

      <p class="continue">
        However,
        there is no way to predict its output for any photo that contains two or more rectangles.
        For example, here are two fields of corn ready for harvest:
      </p>

      <figure id="f:cornfields">
        <img src="img/quality/cornfields.png" alt="Corn Fields" />
      </figure>

      <p class="continue">
        And here are two lines of Python that we might put in a unit test to represent the photo,
        and write it to a file or a <code>StringIO</code>:
      </p>

<pre>
two_fields = { ((0, 0), (1, 1)), ((1, 0), (2, 1)) }
photo_write(two_fields, ...)
</pre>

      <p>
        The function's output might look like this:
      </p>

<pre>
0 0 1 1
1 0 2 1
</pre>

      <p class="continue">
        but it could equally well look like this, with the rectangles in reverse order:
      </p>

<pre>
1 0 2 1
0 0 1 1
</pre>

      <p>
        because sets are stored in an arbitrary order that is under the computer's control.
        Since we don't know what that order is,
        we can't predict the output if we loop over the set directly,
        which means we don't know what to compare the output to.
        If we sort the rectangles,
        on the other hand,
        they'll always be in the same order,
        and to sort them,
        we have to put them in a list first.
      </p>

      <p>
        One final lesson for this section:
        you probably haven't noticed,
        but the tests we've written in this episode are inconsistent.
        Here's the fake "file" we created for testing the photo-reading function:
      </p>

<pre>
Data = '''0 0 1 1
1 0 2 1
2 0 3 1'''
</pre>

      <p class="continue">
        And here's the string we used to check the output of our photo-writing function:
      </p>

<pre>
def test_write_unit_only():
    fixture = { ((0, 0), (1, 1)) }
    ...
    assert result == '0 0 1 1\n'
</pre>

      <p class="continue">
        Notice that one string has a newline at the end and the other doesn't.
        It doesn't matter whether we require this or not&mdash;either
        convention is better than saying "maybe",
        because if we allow both,
        our code becomes more complicated,
        and more testing will be required.
      </p>

      <p>
        Stepping back,
        the most important lesson in this section isn't how to test functions that do I/O.
        The most important idea is that we should design our programs so that their components can be tested.
        To do this,
        we should depend on interfaces,
        not implementations:
        on the contracts that functions provide,
        not on the details of how they accomplish whatever they do.
      </p>

      <p>
        Following this rule will make it easy for us to replace components that you're <em>not</em> currently testing
        with simplified versions to make it easier to test the ones you <em>are</em> interested in.
        It will also save us from writing your tests over and over
        as the internals of the functions you are testing are changed.
        Interfaces are longer-lived than implementations:
        if you rely on the former rather than the latter,
        you'll spend less time rewriting tests,
        and more time figuring out what effect climate change is having on fields in Saskatchewan.
      </p>

      <p>
        Another rule when you're designing programs to be testable is
        to isolate interactions with the outside world.
        For example,
        code that opens file should be separated from code that reads data,
        so that you can test the latter without needing to do the former.
        Finally,
        you should make the things you are going to examine to check the result of a test deterministic,
        i.e.,
        the result of a particular function call should always be exactly the same value,
        so that you can compare it directly to the expected result.
        Unfortunately,
        this last rule can sometimes be hard to follow in scientific programs
        because of floating-point approximations.
      </p>

      <div class="keypoints" id="k:testable">
        <h3>Summary</h3>
        <ul>
          <li idea="perf">Separating interface from implementation makes code easier to test and re-use.</li>
          <li>Replace some components with simplified versions of themselves in order to simplify testing of other components.</li>
          <li>Do not create arbitrary, variable, or random results, as they are extremely hard to test.</li>
          <li>Isolate interactions with the outside world when writing tests.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

      <p>
        It's pretty obvious that if we want to be sure our programs are right,
        we need to put in some effort.
        What isn't so obvious is that
        focusing on quality is also the best way&mdash;in fact, the <em>only</em> way&mdash;to
        improve productivity as well.
        Getting something wrong and then fixing it
        almost always takes longer than getting it right in the first place.
        (As some people are fond of saying,
        a week of hard work can sometimes save you an hour of thought.)
        Designing testable code,
        practicing defensive programming,
        writing and running tests,
        and thinking about what the right answer is supposed to be
        all help get us answers faster,
        as well as ones that are more likely to be correct.
      </p>

    </section>