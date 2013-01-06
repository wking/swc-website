Title: Development
Directory: book

    <ol class="toc">
      <li><a href="#s:grid">The Grid</a></li>
      <li><a href="#s:alias">Aliasing</a></li>
      <li><a href="#s:random">Randomness</a></li>
      <li><a href="#s:neighbors">Neighbors</a></li>
      <li><a href="#s:ties">Handling Ties</a></li>
      <li><a href="#s:assembly">Putting It All Together</a></li>
      <li><a href="#s:bugs">Bugs</a></li>
      <li><a href="#s:refactor">Refactoring</a></li>
      <li><a href="#s:test">Testing</a></li>
      <li><a href="#s:performance">Performance</a></li>
      <li><a href="#s:profile">Profiling</a></li>
      <li><a href="#s:fail">Speeding It Up</a></li>
      <li><a href="#s:lazy">A New Beginning</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <p>
      Ethan Ecosystem is studying the way pollutants spreads through fractured rock
      (<a href="#f:invasion_percolation">Figure XXX</a>).
      To simulate this,
      he wants to use a model called
      <a href="glossary.html#invasion-percolation">invasion percolation</a>,
      which has been used to model many other phenomena as well.
    </p>

    <figure id="f:invasion_percolation">
      <img src="img/python/invasion_percolation.png" alt="Invasion Percolation" />
    </figure>

    <p>
      In its simplest form,
      invasion percolation represents the rock that the pollutant is spreading through
      as a two-dimensional grid of square cells filled with random values.
      The algorithm starts by marking the center cell as being polluted,
      then looks at that cell's four neighbors
      (<a href="#f:invasion_percolation_algorithm">Figure XXX</a>).
      The one with the lowest value is the one that has the least resistance to the spread of the pollutant,
      so the algorithm marks that as being filled as well.
      It then looks at the six neighbors of the entire filled region,
      and once again finds and marks the one with the lowest value.
      This process continues until a certain percentage of cells have been filled
      (i.e., there's no more pollutant),
      or until the pollution reaches the boundary of the grid.
    </p>

    <figure id="f:invasion_percolation_algorithm">
      <img src="img/python/invasion_percolation_algorithm.png" alt="Invasion Percolation Algorithm" />
    </figure>

    <p>
      If two or more cells on the boundary are tied equal for the lowest value,
      the algorithm can either fill them all in simultaneously,
      or pick one at random and fill that in.
      Either way,
      the fractal this algorithm produces will tell Ethan how quickly the pollutant will spread,
      and how much of the rock will be contaminated.
    </p>

    <p>
      But if Ethan wants to look at the statistical properties of these fractals,
      he will need to do many simulation on large grids.
      That means his program has to be fast,
      so this chapter will look at three things:
    </p>

    <ol>

      <li>
        How do we build a program like this in the first place?
      </li>

      <li>
        How do we tell if it's working correctly?
      </li>

      <li>
        How do we speed it up?
      </li>

    </ol>

    <p>
      The order of the second and third steps is important.
      There's no point speeding something up if it isn't working correctly,
      or if we don't know whether it's working correctly or not.
      Once we know how to tell,
      on the other hand,
      we can focus on performance improvement,
      secure in the knowledge that if one of our bright ideas breaks things,
      our program will let us know.
    </p>

    <section id="s:grid">

      <h2>The Grid</h2>

      <div class="understand" id="u:grid">
        <h3>Understand:</h3>
        <ul>
          <li>How to represent a two-dimensional grid using a list of lists.</li>
          <li>How to leave markers in code to keep track of tasks that still need to be done.</li>
        </ul>
      </div>

      <p>
        Let's start by looking at
        how to represent a two-dimensional grid in Python.
        By "two-dimensional",
        we mean something that's indexed by X and Y coordinates.
        Our grid is discrete:
        we need to store values for locations (1, 1), (1, 2), and so on,
        but not locations like (1.512, 7.243).
      </p>

      <div class="box">
        <h3>Why Not Use a NumPy Array?</h3>
        <p class="fixme">explain: pedagogic value, and we're going to throw it all away anyway</p>
      </div>

      <p>
        Each cell in the grid stores a single random value
        representing the permeability of the rock.
        We also need a way to mark cells that have been filled with pollutant.
        Once a cell has been filled,
        we don't care about its value any longer,
        so we can use any number that isn't going to appear in the grid otherwise
        as a marker to show which cells have been filled.
        For now,
        we'll use -1.
      </p>

      <p>
        Note that this means we're using integers in two ways.
        The first is as actual data values;
        the second is as flags to represent the state of a cell.
        This is simple to do,
        but if we ever get data who values happen to contain the numbers that we're using to mark filled cells,
        our program will misinterpret them.
        Bugs like this can be very hard to track down.
      </p>

      <p>
        Before we go any further,
        we also have to make some decisions about the shapes of our grids.
        First,
        do grids always have to be square, i.e., N&times;N,
        or can we have rectangular grids whose X and Y sizes are different?
        Second,
        do grids always have to be odd-sized,
        so that there's a unique center square for us to fill at the start,
        or can we have a grid that is even in size along one or both axes?
      </p>

      <p>
        The real question is,
        how general should we make the first version of this program&mdash;indeed,
        of <em>any</em> program?
        Some people say, "Don't build it until you need it,"
        while others say, "A week of hard work can sometimes save you an hour of thought."
        Both sayings are true,
        but as in any other intellectually demanding field,
        knowing what rules to apply when comes with experience,
        and the only way to get experience is to work through many examples
        (and make a few mistakes).
        Again,
        let's do the simple thing for now,
        and assume that grids are always square and odd-sized.
      </p>

      <p>
        Now, how are we going to store the grid?
        One way is to use a <a href="python.html#g:nested-list">nested list</a>.
        This lets us use double subscripts to refer to elements,
        which is really what we mean by "two dimensional".
        Here's a piece of code that builds a grid of 1's as a list of lists;
        we'll come back later and show how to fill those cells with random values instead:
      </p>

<pre src="src/programming/grid_ones.py">
# Create an NxN grid of random integers in 1..Z.
assert N &gt; 0, "Grid size must be positive"
assert N%2 == 1, "Grid size must be odd"
grid = []
for x in range(N):
    grid.append([])
    for y in range(N):
        grid[-1].append(1) # FIXME: need a random value
</pre>

      <p>
        The first thing we do is check that the grid size <code>N</code> is a sensible value.
        We then assign an empty list to the variable <code>grid</code>.
        The first time through the outer loop,
        we append a new empty list to the outer list.
        Each pass through the inner loop,
        we append the value 1 to that inner list
        (<a href="#f:building_grid">Figure XXX</a>).
        We go back through the outer loop to append another sub-list,
        which we grow by adding more 1's,
        and so on until we get the grid that we wanted.
      </p>

      <figure id="f:building_grid">
        <img src="img/python/building_grid.png" alt="Building the Grid" />
      </figure>

      <div class="box">
        <h3>FIXME</h3>

        <p>
          At any point when writing a program,
          there may be half a dozen things that need to be done next.
          The problem is,
          we can only write one at a time.
          It's therefore a common practice to add comments to the code
          to remind ourselves of things we need to come back and fill in (or tidy up) later.
          It's equally common to start such comments with a word like "FIXME" or "TODO"
          to make them easier to find with tools like <a href="shell.html#s:find"><code>grep</code></a>.
        </p>

      </div>

      <div class="keypoints" id="k:grid">
        <h3>Summary</h3>
        <ul>
          <li idea="perf">Get something simple working, then start to add features, rather than putting everything in the program at the start.</li>
          <li>Leave FIXME markers in programs as you are developing them to remind yourself what still needs to be done.</li>
        </ul>
      </div>

    </section>

    <section id="s:alias">

      <h2>Aliasing</h2>

      <div class="understand" id="u:alias">
        <h3>Understand:</h3>
        <ul>
          <li>How list aliasing can cause subtle errors in programs.</li>
        </ul>
      </div>

      <p>
        Before we go further with our list-of-lists implementation,
        we need to revisit the issue of <a href="python.html#s:alias">aliasing</a>
        and look at some bugs that can arise when your programs uses it.
        Take another look at the list-of-lists in
        <a href="#f:building_grid">Figure XXX</a>.
        A single list serves as the structure's spine,
        while the sublists store the actual cell values.
      </p>

      <p>
        Here's some code that tries to create such a structure
        but gets it wrong:
      </p>

<pre src="src/programming/alias_buggy.py">
# Incorrect code
assert N > 0, "Grid size must be positive"
assert N%2 == 1, "Grid size must be odd"
grid = []
<span class="highlight">EMPTY = []</span>
for x in range(N):
  <span class="highlight">grid.append(EMPTY)</span>
  for y in range(N):
    grid[-1].append(1)
</pre>

      <p>
        The only change we've made is to introduce a variable called <code>EMPTY</code>
        so that we can say, "Append EMPTY to the grid" in our loop.
        How can this be a bug?
        Aren't meaningful variable names supposed to be a good thing?
      </p>

      <p>
        To see what's wrong,
        let's trace the execution of this program.
        We start by assigning an empty list to the variable <code>grid</code>.
        We then assign another empty list to the variable <code>EMPTY</code>.
        In the first pass through our loop,
        we append the empty list pointed to by <code>EMPTY</code> to the list pointed to by <code>grid</code>
        to get the structure shown in <a href="#f:alias_bug">Figure XXX</a>.
        We then go into our inner loop and append a 1 to that sublist.
        Going around the inner loop again,
        we append another 1,
        and another.
        We then go back to the outer loop and append <code>EMPTY</code> again.
      </p>

      <figure id="f:alias_bug">
        <img src="img/python/alias_bug.png" alt="Aliasing Bug" />
      </figure>

      <p>
        The structure shown on the left is now broken:
        both cells of the list pointed to by <code>grid</code> point to the same sublist,
        because <code>EMPTY</code> is still pointing to that list,
        even though we've changed it.
        When we go into the inner loop the second time,
        we're appending 1's to the same list that we used last time.
      </p>

      <div class="box">

        <h3>Debugging With Pictures</h3>

        <p>
          Aliasing bugs are notoriously difficult to track down
          because the program isn't doing anything illegal:
          it's just not doing what we want in this particular case.
          Many debugging tools have been built over the last thirty years
          that draw pictures of data structures
          to show programmers what they're actually creating,
          but none has really caught on yet,
          primarily because pictures of the objects and references in real programs
          are too large and too cluttered to be comprehensible.
          As a result,
          many programmers wind up drawing diagrams like
          <a href="#f:alias_bug">Figure XXX</a>
          by hand while they're debugging.
        </p>

      </div>

      <div class="keypoints" id="k:alias">
        <h3>Summary</h3>
        <ul>
          <li>Draw pictures of data structures to aid debugging.</li>
        </ul>
      </div>

    </section>

    <section id="s:random">

      <h2>Randomness</h2>

      <div class="understand" id="u:random">
        <h3>Understand:</h3>
        <ul>
          <li>That computer-generated "random" numbers aren't actually random.</li>
          <li>How to create pseudo-random numbers in a program.</li>
          <li>How to re-generate a particular sequence of pseudo-random numbers.</li>
        </ul>
      </div>

      <p>
        Now that we have a grid,
        let's fill it with random numbers chosen uniformly from some range 1 to Z.
        We should check the science on this,
        as there was nothing in our original specification that said the values should be uniformly distributed,
        but once again we'll do something simple,
        make sure it's working,
        and then change it later.
        Our code looks like this:
      </p>

<pre src="src/programming/random_grid.py">
<span class="highlight">from random import seed, randint</span>
assert N &gt; 0, "Grid size must be positive"
assert N%2 == 1, "Grid size must be odd"
<span class="highlight">assert Z &gt; 0, "Range must be positive"</span>
<span class="highlight">seed(S)</span>
grid = []
for x in range(N):
    grid.append([])
    for y in range(N):
        grid[-1].append(<span class="highlight">randint(1, Z)</span>)
</pre>

      <p class="continue">
        The changes are pretty small:
        we import a couple of functions from a library,
        check that the upper bound on our random number range makes sense,
        initialize the random number generator,
        and then call <code>randint</code> to generate a random number
        each time we need one.
      </p>

      <p>
        To understand these changes,
        let's step back and look at a small program
        that does nothing but generate a few seemingly random numbers:
      </p>

<pre src="src/programming/random_calls.py">
from random import seed, randint
seed(4713983)
for i in range(5):
    print randint(1, 10),
<span class="out">7 2 6 6 5</span></pre>

      <p class="continue">
        The first step is to import functions from the standard Python random number library
        called (unsurprisingly) <code>random</code>.
        We then initialize the sequence of "random" numbers we're going to generate&mdash;you'll
        see in a moment why there are quotes around the word "random".
        We can then call <code>randint</code>
        to produce the next random number in the sequence as many times as we want.
      </p>

      <p>
        Pseudo-random number generators like the one we're using have some important limitations,
        and it's important that you understand them before you use them in your programs.
        Consider this simple "random" number generator:
      </p>

<pre src="src/programming/random_generator.py">
base = 17  # a prime
value = 4  # anything in 0..base-1
for i in range(20):
    value = (3 * value + 5) % base
    print value,
<span class="out">0 5 3 14 13 10 1 8 12 7 9 15 16 2 11 4 0 5 3 14</span></pre>

      <p class="continue">
        It depends on two values:
      </p>

      <ol>

        <li>
          The <em>base</em>,
          which is a prime number,
          determines how many integers we'll get before the sequence starts to repeat itself.
          Computers can only represent a finite range of numbers,
          so sooner or later, any supposedly random sequence will start to repeat.
          Once they do, values will appear in exactly the same order they did before.
        </li>

        <li>
          The <em>seed</em> controls where the sequence starts.
          With a seed of 4,
          the sequence starts at the value 0.
          Changing the seed to 9 shifts the sequence over:
          we get the same numbers in the same order,
          but starting from a different place.
          We'll use this fact later one when it comes time to test our invasion percolation program.
        </li>

      </ol>

      <p>
        These numbers aren't actually very random at all.
        For example,
        did you notice that the number 6 never appeared anywhere in the sequence?
        Its absence would probably bias our statistics in ways that would be very hard to detect.
        But look at what happens if 6 <em>does</em> appear:
      </p>

<pre src="src/programming/random_generator_6.py">
base = 17
value = 6
for i in range(20):
    value = (3 * value + 5) % base
    print value,
<span class="out">6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6</span></pre>

      <p class="continue">
        As you can see,
        3 times 6 plus 5 mod 17 is 6 again,
        and so our sequence gets stuck.
        How can we prove that this won't ever happen for an arbitrary seed in a random number generator?
        And how can we prove that something subtler won't go wrong?
      </p>

      <p>
        In fact,
        computers can't generate real random numbers.
        But if we're clever,
        they <em>can</em> generate numbers with many of the same statistical properties as the real thing.
        This is very hard to get right,
        so you should <em>never</em> try to build your own random number generator.
        Instead, you should always use a function from a good, well-tested library (like Python's).
      </p>

      <blockquote>
        Any one who considers arithmetical methods of producing random digits is,
        of course,
        in a state of sin.
        For,
        as has been pointed out several times,
        there is no such thing as a random number.
        There are only methods to produce random numbers,
        and a strict arithmetic procedure of course is not such a method.
        <br/>
        &mdash; John von Neumann
      </blockquote>

      <div class="keypoints" id="k:random">
        <h3>Summary</h3>
        <ul>
          <li>Use a well-tested random number generation library to generate pseudorandom values.</li>
          <li>If a random number generation library is given the same seed, it will produce the same sequence of values.</li>
        </ul>
      </div>

    </section>

    <section id="s:neighbors">

      <h2>Neighbors</h2>

      <div class="understand" id="u:neighbors">
        <h3>Understand:</h3>
        <ul>
          <li>How to examine the neighbors of a cell in a two-dimensional grid.</li>
          <li>What short-circuit evaluation is and when it occurs.</li>
        </ul>
      </div>

      <p>
        Now that we have filled our grid,
        let's find cells' neighbors.
        (We need to do this because pollutant can only spread to cells
        that are adjacent to ones that have already been filled.)
        The blue cell shown in <a href="#f:filling_neighbors">Figure XXX</a>
        is a neighbor of the filled region
        if any of the green cells already have that special marker value.
        Note that we're not looking at the cells that are on the diagonals:
        we should check the science on this,
        but again,
        we'll do the simple thing for now
        and change it later if we need to.
      </p>

      <div class="box">

        <h3>How to Put Things Off</h3>

        <p>
          This is the second time we've said,
          "We'll change it later if we need to."
          Each time we say this,
          we should design our software so that making the change is as easy as possible&mdash;ideally,
          a matter of changing one function call or one parameter value.
          We haven't done that yet,
          but we will by the end of this chapter.
        </p>

      </div>

      <figure id="f:filling_neighbors">
        <img src="img/python/filling_neighbors.png" alt="Filling Neighbors" />
      </figure>

      <p>
        Here's a piece of code that tests to see whether a cell is a candidate for being filled in:
      </p>

<pre>
# Is a cell a candidate for filling?
# Version 1: has bugs!
for x in range(N):
    for y in range(N):
        if is_filled(grid, x-1, y) \
        or is_filled(grid, x+1, y) \
        or is_filled(grid, x, y-1) \
        or is_filled(grid, x, y+1):
            ...cell (x, y) is a candidate...
</pre>

      <p class="continue">
        It seems simple:
        for each (x, y) coordinate in the grid,
        look at the cells that are left, right, up, and down.
        If any of them is filled,
        then this cell is a candidate for filling.
      </p>

      <p>
        However,
        this code doesn't take into account what happens at the edges.
        If we subtract 1 when <code>x</code> is zero,
        we get an X coordinate of -1.
        In Python,
        that means the last cell in the row
        (since negative indices count backward from the end of a list).
        That will wrap around to the far edge,
        which is definitely not what we want.
      </p>

      <p>
        The situation on the other border isn't quite as bad:
        if we add one to the X coordinate when we're at the right-hand edge,
        our neighbor index will be out of bounds
        and Python will raise an exception,
        so at least we'll know we did something wrong.
      </p>

      <p>
        Here's another version of the code that tests for this:
      </p>

<pre>
# Is a cell a candidate for filling?
# Version 2: long-winded
for x in range(N):
    for y in range(N):
        if x &gt; 0:
            if is_filled(grid, x-1, y):
                ...cell (x, y) is a candidate...
        ...repeat for the other three cases...
</pre>

      <p class="continue">
        For each (x, y) coordinate,
        we test to make sure that <code>x</code> is greater than zero,
        i.e,
        that we're not on the left edge,
        before checking to see if the cell to our left is filled.
        We repeat a similar double test for each of the other directions.
      </p>

      <p>
        We can make this a bit more readable by combining the two tests with <code>and</code>
      </p>

<pre>
# Is a cell a candidate for filling?
# Version 3: good enough for production
for x in range(N):
    for y in range(N):
        if (x &gt; 0) and is_filled(x-1, y):
            ...cell (x, y) is a candidate...
        elif (x &lt; N-1) and is_filled(x+1, y):
            ...and so on...
</pre>

      <p>
        This works because of
        <a href="glossary.html#short-circuit-evaluation">short-circuit evaluation</a>.
        In Python (and in most other modern programming languages),
        <code>and</code> only tests the second condition if the first one is true,
        because if the first condition is false,
        the <code>and</code> is guaranteed to be false.
        Similarly,
        if the first condition in an <code>or</code> is true,
        Python doesn't both to evaluate the second condition.
        We talk about this a bit more in <a href="ref.html#s:bool">the appendix</a>.
      </p>

      <div class="box">

        <h3>Options</h3>

        <p>
          There are several other good ways to structure even this short piece of code.
          For example,
          we could check that the X and Y indices are in range inside <code>is_filled</code>,
          and always return false if they're not.
          We could also use one big conditional instead of an <code>if</code>
          and four <code>elif</code>s
          in order to avoid duplicating the code that does something to a cell
          if it is indeed a candidate:
        </p>

<pre>
        if ((x &gt; 0)   and is_filled(x-1, y)) \
        or ((x &lt; N-1) and is_filled(x+1, y)) \
        or ((y &gt; 0)   and is_filled(x, y-1)) \
        or ((y &lt; N-1) and is_filled(x, y+1)):
            ...cell (x, y) is a candidate...
</pre>

        <p class="continue">
          There's no clear reason to choose any of these approaches over any of the others,
          at least not yet,
          so we'll continue with the one we have.
        </p>

      </div>

      <div class="keypoints" id="k:neighbors">
        <h3>Summary</h3>
        <ul>
          <li><code>and</code> and <code>or</code> stop evaluating arguments as soon as they have an answer.</li>
        </ul>
      </div>

    </section>

    <section id="s:ties">

      <h2>Handling Ties</h2>

      <div class="understand" id="u:ties">
        <h3>Understand:</h3>
        <ul>
          <li>How to translate complex tests into program statements systematically.</li>
        </ul>
      </div>

      <p>
        The next thing on our to-do list is
        to resolve ties between cells that share the lowest value on the boundary.
        For example,
        our specification says that we should choose one of the three highlighted cells
        in <a href="#f:handling_ties">Figure XXX</a> at random.
        How do we keep track of the cells we're supposed to be choosing from?
      </p>

      <figure id="f:handling_ties">
        <img src="img/python/handling_ties.png" alt="Handling Ties" />
      </figure>

      <p>
        We're going to do this using a set,
        which we will fill with (x,y) tuples holding the coordinates of boundary cells
        that have the lowest value we've seen so far,
        and use a separate variable to store that lowest value.
        Every time we look at a new cell,
        we will have to consider three cases:
      </p>

      <ol>

        <li>
          <em>Its value is greater than the minimum we've seen so far,</em>
          so we can ignore it,
          because we know there are better cells elsewhere.
        </li>

        <li>
          <em>The value of the new cell is equal to the current minimum,</em>
          so we must add the new cell's (x,y) coordinates to our set.
        </li>

        <li>
          <em>The new value is less than the current minimum,</em>
          so we must replace all the coordinates that are currently in the set
          with the coordinates of the new cell,
          and re-set our minimum to be this new value.
        </li>

      </ol>

      <p>
        An example will make this clearer.
        Suppose the range of values cells can take on is 1 to 10.
        Before we start looking at cells,
        we assign 11 to <code>min_val</code>
        (because it is one greater than the maximum possible value that could be in the grid)
        and assign an empty set to <code>min_set</code>
        (because we haven't look at any cells yet).
        We then take a look at our first cell
        (<a href="#f:handling_ties_example">Figure XXX</a>).
        Its value is less than <code>min_val</code>,
        so we re-set <code>min_val</code> to 4 (the value of the cell),
        and we put the coordinates of this cell (in this case, X equals 12, Y equals 23) into the set.
      </p>

      <figure id="f:handling_ties_example">
        <img src="img/python/handling_ties_example.png" alt="Example of Handling Ties" />
      </figure>

      <p>
        When we look at the next cell,
        its value is greater than the currently known minimum value,
        so we ignore it.
        The third cell is tied equal for the minimum value,
        so we add its coordinates&mdash;in this case, (11,22)&mdash;to our set.
        The next cell is greater than the minimum value, so we ignore it.
      </p>

      <p>
        The fifth cell we examine has a value less than the minimum value we've seen previously,
        so we throw out all of the coordinates we've saved in the set,
        and put the coordinates of this cell into the set in their place.
        Finally,
        the last boundary cell has a value equal to this new minimum,
        so we add its coordinates to the set.
      </p>

      <p>
        Here's the code that implements all this:
      </p>

<pre>
# Keep track of cells tied for lowest value
min_val = Z+1
min_set = set()
for x in range(N):
    for y in range(N):
        if ...is a neighbor...:
            if grid[x][y] == min_val:
                min_set.add((x, y))
            elif grid[x][y] &lt; min_val:
                min_val = grid[x][y]
                min_set = set([(x, y)])
</pre>

      <div class="box">

        <h3>Seeing What Isn't There</h3>

        <p>
          Notice that since we don't need to do anything
          when a cell's value is greater than the minimum we've seen so far,
          there isn't an <code>else</code> to handle that case.
          Some people would add a comment to make that explicit,
          so that the logic is complete:
        </p>

<pre>
            if grid[x][y] == min_val:
                min_set.add((x, y))
            elif grid[x][y] &lt; min_val:
                min_val = grid[x][y]
                min_set = set([(x, y)])
<span class="highlight">            else:
                pass # do nothing if cell value &gt; min_val</span>
</pre>

        <p class="continue">
          but other people would find this more confusing than helpful.
          As always,
          the most important thing is to be consistent:
        </p>

      </div>

      <p>
        Once we have the set of candidate cells,
        we can use the <code>random</code> library's <code>choice</code> function to pick one:
      </p>

<pre>
# Choose a cell
from random import ..., choice

min_val = Z+1
min_set = set()
...loop...
assert min_set, "No cells found"
candidates = list(min_set)
x, y = choice(candidates)
</pre>

      <p class="continue">
        Before we call <code>choice</code>,
        we check that the set actually has something in it
        (because if there are no cells in the set when we finish our loop,
        then something's gone wrong with our program).
        We then convert the set to a list,
        because the random choice function requires an argument that can be indexed,
        and then use that function to choose one element from the list.
      </p>

      <div class="keypoints" id="k:ties">
        <h3>Summary</h3>
        <ul>
          <li>Turn complex tests into conditional stepwise.</li>
          <li>Include do-nothing branches if it makes the code easier to understand.</li>
        </ul>
      </div>

    </section>

    <section id="s:assembly">

      <h2>Putting It All Together</h2>

      <div class="understand" id="u:assembly">
        <h3>Understand:</h3>
        <ul>
          <li>How to assemble a program once its pieces are understood.</li>
        </ul>
      </div>

      <p>
        We now know how to:
      </p>

      <ul>

        <li>
          create a grid,
        </li>

        <li>
          fill it with random numbers,
        </li>

        <li>
          mark cells that have been filled,
        </li>

        <li>
          find cells that might be filled next, and
        </li>

        <li>
          choose one of them at random.
        </li>

      </ul>

      <p class="continue">
        It's time to put all this together to create a complete program.
        We will assemble the code in exactly the order we would write it
        (in fact,
        in the order in which I <em>did</em> write it,
        because everything so far has actually been
        a rational reconstruction of the things I realized I needed to have known
        after I wrote the first version of this code).
        We'll start at the top and work down,
        introducing functions and variables as we need them,
        and tidy up a little bit along the way.
        Here's what we write first:
      </p>

<pre src="src/dev/invperc_initial.py">
'''Invasion percolation simulation.
usage: invperc.py grid_size value_range random_seed
'''
import sys, random

# Main driver.
if __name__ == '__main__':
    main(sys.argv[1:])
</pre>

      <p>
        We start with a <a href="glossary.html#docstring">docstring</a>
        to remind ourselves of what this program does.
        We then import the libraries we need and call a <code>main</code> function,
        passing in all of the command-line arguments except the first
        (which is the name of our script).
        That function starts like this:
      </p>

<pre src="src/dev/invperc_initial.py">
    # Parse parameters.
    arguments = sys.argv[1:]
    try:
        grid_size = int(arguments[0])
        value_range = int(arguments[1])
        random_seed = int(arguments[2])
    except IndexError:
        fail('Expected 3 arguments, got %d' % len(arguments))
    except ValueError:
        fail('Expected int arguments, got %s' % str(arguments))
</pre>

      <p class="continue">
        This code converts the first three values in <code>arguments</code> to integers
        and assign them to <code>grid_size</code>, <code>value_range</code>, and <code>random_seed</code>.
        If we get an <code>IndexError</code>,
        it means that one of the indices 0, 1, or 2 wasn't valid,
        so we don't have enough arguments.
        If we get a <code>ValueError</code>,
        it means that one of our attempts to convert a string to an integer failed,
        so again we print an error message.
      </p>

      <p>
        We have used a function called <code>fail</code> to report errors.
        This doesn't exist yet,
        so we should go and write it:
      </p>

<pre src="src/dev/invperc_initial.py">
def fail(msg):
    '''Print error message and halt program.'''
    print &gt;&gt; sys.stderr, msg
    sys.exit(1)
</pre>

      <p>
        We give the function a docstring because every function should have one.
        Inside the function,
        we print the message to standard error so that it will appear on the user's console,
        then exit.
        <a href="#f:structure_a">Figure XXX</a> shows
        the structure of the program so far:
        a documentation string,
        our <code>fail</code> function,
        and the main driver of our program.
      </p>

      <figure id="f:structure_a">
        <img src="img/python/structure_a.png" alt="Program Structure (A)" />
      </figure>

      <p>
        The next step in <code>main</code> is to actually run the simulation.
        We do that by seeding the random number generator,
        creating a random grid,
        marking the center cell as filled,
        and then filling the rest of the grid:
      </p>

<pre src="src/dev/invperc_initial.py">
    # Run simulation.
    random.seed(random_seed)
    grid = create_random_grid(grid_size, value_range)
    mark_filled(grid, grid_size/2, grid_size/2)
    fill_grid(grid) + 1
</pre>

      <p>
        This code uses three functions that don't exist yet,
        so we will have to go back and write them.
        Before doing that, though,
        let's finish off the main body of the program.
        The last task we have is to report results,
        but we haven't actually decided what to do about this:
        nothing in our specification told us whether we were supposed to draw the fractal,
        calculate some statistics,
        or do something else entirely.
        For now, we'll just print the number of cells we have filled in:
      </p>

<pre src="src/dev/invperc_initial.py">
    # Run simulation.
    random.seed(random_seed)
    grid = create_random_grid(grid_size, value_range)
    mark_filled(grid, grid_size/2, grid_size/2)
    <span class="highlight">num_filled_cells =</span> fill_grid(grid) + 1
    <span class="highlight">print '%d cells filled' % num_filled_cells</span>
</pre>

      <p class="continue">
        We have changed <code>fill_grid</code> so that it returns the number of cells it filled in,
        and then we print that number.
        Note that we have to add one to the value returned by <code>fill_grid</code>
        because we marked the center cell as being filled manually.
        This is a little bit clumsy:
        someone who hasn't read our code carefully might reasonably think that <code>fill_grid</code> returns
        the total number of cells that are filled, not one less than that.
        We should go back and tidy that up later.
      </p>

      <p>
        Here's the function to create a random grid,
        reproduced from earlier:
      </p>

<pre src="src/dev/invperc_initial.py">
def create_random_grid(N, Z):
    '''Return an NxN grid of random values in 1..Z.
    Assumes the RNG has already been seeded.'''

    assert N &gt; 0, 'Grid size must be positive'
    assert N%2 == 1, 'Grid size must be odd'
    assert Z &gt; 0, 'Random range must be positive'
    grid = []
    for x in range(N):
        grid.append([])
        for y in range(N):
            grid[-1].append(random.randint(1, Z))
    return grid
</pre>

      <p class="continue">
        It checks that the parameters it's been passed make sense,
        then it builds a list of lists of random values.
        It assumes that the random number generator has already been seeded,
        i.e., it is not going to seed the random number generator itself.
        <a href="#f:structure_b">Figure XXX</a> shows
        where we put this function in our program file.
      </p>

      <figure id="f:structure_b">
        <img src="img/python/structure_b.png" alt="Program Structure (B)" />
      </figure>

      <p>
        Next is <code>mark_filled</code>,
        which,
        as its name suggests,
        marks a grid cell as being filled:
      </p>

<pre src="src/dev/invperc_initial.py">
def mark_filled(grid, x, y):
    '''Mark a grid cell as filled.'''

    assert 0 &lt;= x &lt; len(grid), \
           'X coordinate out of range (%d vs %d)' % \
           (x, len(grid))
    assert 0 &lt;= y &lt; len(grid), \
           'Y coordinate out of range (%d vs %d)' % \
           (y, len(grid))

    grid[x][y] = -1
</pre>

      <p class="continue">
        We use assertions to test that the X and Y coordinates we've been given are actually in bounds.
        You might think we don't need this code,
        because if the X or Y coordinate is out of bounds,
        Python will fail and print its own error message,
        but there are three reasons to put these assertions in:
      </p>

      <ol>

        <li>
          The assertions tell readers what we expect of X and Y.
        </li>

        <li>
          These error messages are more meaningful that Python's generic "IndexError: index out of range" message.
        </li>

        <li>
          Negative values of X and Y won't actually cause exceptions.
        </li>

      </ol>

      <p>
        The last line in this function assigns -1 to <code>grid[x][y]</code>.
        We're using -1 to indicate filled cells,
        but we don't know if people are going to remember that when they're reading our code:
        if you say "grid at X, Y assigned -1", it's not immediately clear what you're doing.
        So let's make a small change right now:
        near the top of our program we'll create a variable called <code>FILLED</code>,
        and give it the value -1,
        so that in our function we can say "grid at X, Y is assigned FILLED":
      </p>

<pre src="src/dev/invperc_initial.py">
FILLED = -1

...other functions...

def mark_filled(grid, x, y):
    ...body of function...
    grid[x][y] = FILLED
</pre>

      <p class="continue">
        <code>FILLED</code> is written in capital letters because we think of it as a constant,
        and by convention,
        constants are normally written in all caps.
        Putting constants at the top of the file is also a (strong) convention.
      </p>

      <p>
        The next function in our to-do list is <code>fill_grid</code>.
        The docstring says that it fills an N&times;N grid until the filled region hits the boundary,
        and that it assumes that the center cell has been filled before it is called:
      </p>

<pre src="src/dev/invperc_initial.py">
def fill_grid(grid):
    '''Fill an NxN grid until filled region hits boundary.'''

    N = len(grid)
    num_filled = 0
    while True:
        candidates = find_candidates(grid)
        assert candidates, 'No fillable cells found!'
        x, y = random.choice(list(candidates))
        mark_filled(grid, x, y)
        num_filled += 1
        if x in (0, N-1) or y in (0, N-1):
            break

    return num_filled
</pre>

      <p class="continue">
        We begin by setting up <code>N</code> and <code>num_filled</code>,
        which are the grid size and the number of cells that this function has filled so far
        We then go into a seemingly-infinite loop,
        at the bottom of which we test to see if we're done,
        and if so,
        break out.
        We could equally well do something like this:
      </p>

<pre>
    <span class="highlight">filling = True</span>
    while <span class="highlight">filling</span>:
        ...
        if x in (0, N-1) or y in (0, N-1):
            <span class="highlight">filling = False</span>
</pre>

      <p>
        However we control filling,
        we use another function called <code>find_candidates</code>
        to find the set of cells that we might fill.
        This function hasn't been written yet,
        so we add it to our to-do list.
        We then check that the set of candidates it has found has something in it,
        because if we haven't found any candidates for filling,
        something has probably gone wrong with our program.
        And then,
        as discussed <a href="#s:random">earlier</a>,
        we make a random choice to choose the cell we're going to fill,
        then mark it and increment our count of filled cells.
        <a href="#f:structure_c">Figure XXX</a> shows
        where this function fits in the file.
      </p>

      <figure id="f:structure_c">
        <img src="img/python/structure_c.png" alt="Program Structure (C)" />
      </figure>

      <p>
        <code>find_candidates</code> is next on our to-do list:
      </p>

<pre src="src/dev/invperc_initial.py">
def find_candidates(grid):
    '''Find low-valued neighbor cells.'''

    N = len(grid)
    min_val = sys.maxint
    min_set = set()
    for x in range(N):
        for y in range(N):
            if (x &gt; 0) and (grid[x-1][y] == FILLED) \
            or (x &lt; N-1) and (grid[x+1][y] == FILLED) \
            or (y &gt; 0) and (grid[x][y+1] == FILLED) \
            or (y &lt; N-1) and (grid[x][y+1] == FILLED):
                ...let's stop right there...
</pre>

      <p>
        We're going to stop right there because this code is already hard to read
        and we haven't even finished it.
        In fact,
        it contains a bug&mdash;one of those <code>y+1</code>'s should be a <code>y-1</code>&mdash;but
        you probably didn't notice that because there was too much code to read at once.
      </p>

      <p>
        A good rule of thumb is, "Listen to your code as you write it."
        If the code is difficult to understand when read aloud,
        then it's probably going to be difficult to understand when you're debugging,
        so you should try to simplify it.
        This version of <code>find_candidates</code> introduces
        a helper function called <code>is_candidate</code>:
      </p>

<pre src="src/dev/invperc_is_candidate.py">
def find_candidates(grid):
    '''Find low-valued neighbor cells.'''
    N = len(grid)
    min_val = sys.maxint
    min_set = set()
    for x in range(N):
        for y in range(N):
            if is_candidate(grid, x, y):
                ...now we're talking...
</pre>

      <p class="continue">
        This is much clearer when read aloud.
        Let's finish the function
        by adding the code we figured out earlier:
      </p>

<pre src="src/dev/invperc_is_candidate.py">
                if is_candidate(grid, x, y):
                    # Has current lowest value.
                    if grid[x][y] == min_val:
                        min_set.add((x, y))
                    # New lowest value.
                    elif grid[x][y] &lt; min_val:
                        min_val = grid[x][y]
                        min_set = set([(x, y)])
</pre>

      <figure id="f:structure_d">
        <img src="img/python/structure_d.png" alt="Program Structure (D)" />
      </figure>

      <p>
        As <a href="#f:structure_d">Figure XXX</a> shows,
        the <code>find_candidates</code> function fits right above <code>fill_grid</code> in our file.
        We can then insert the <code>is_candidate</code> function we wrote in the previous section
        right above <code>find_candidates</code>
        and write it:
      </p>

<pre src="src/dev/invperc_is_candidate.py">
def is_candidate(grid, x, y):
    '''Is a cell a candidate for filling?'''

    return (x &gt; 0) and (grid[x-1][y] == FILLED) \
        or (x &lt; N-1) and (grid[x+1][y] == FILLED) \
        or (y &gt; 0) and (grid[x][y-1] == FILLED) \
        or (y &lt; N-1) and (grid[x][y+1] == FILLED)
</pre>

      <p>
        There are no functions left on our to-do list,
        so it's time to run our program&mdash;except it's not.
        It's actually time to <em>test</em> our program,
        because there's a bug lurking in the code that we just put together.
        Take a moment,
        read over the final code,
        and try to find it
        before moving on to the next section.
      </p>

      <div class="keypoints" id="k:assembly">
        <h3>Summary</h3>
        <ul>
          <li idea="perf;paranoia">Put programs together piece by piece.</li>
          <li>Write one complete function at a time rather than diving into sub-functions right away.</li>
        </ul>
      </div>

    </section>

    <section id="s:bugs">

      <h2>Bugs</h2>

      <div class="understand" id="u:bugs">
        <h3>Understand:</h3>
        <ul>
          <li>How to halt a running program.</li>
          <li>That we should test programs on simple cases first.</li>
        </ul>
      </div>

      <p>
        Let's run the program that we created in the previous section:
      </p>

<pre>
$ <span class="in">python invperc.py 3 10 17983</span>
<span class="out">2 cells filled</span></pre>

      <p class="continue">
        The program tells us that 2 cells have been filled,
        which is what we'd expect:
        in a 3&times;3 grid,
        we fill always the center cell and one other,
        then we hit the boundary.
        Let's try a larger grid:
      </p>

<pre>
$ <span class="in">python invperc.py 5 10 27187</span>
...a minute passes...
<span class="in">Ctrl-C</span></pre>

      <p class="continue">
        After a minute,
        we use Control-C to halt the program.
        It's time to fire up the debugger&hellip;
      </p>

      <figure id="f:debugger">
        <img src="img/python/debugger.png" alt="Debugging the Grid" />
      </figure>

      <p>
        The initial grid looks OK:
        it is a 3-element list,
        each of whose entries is another 3-element list with values in the range 1 to 10.
        There's even a -1 in the right place
        (remember, we're using -1 to mark filled cells).
      </p>

      <p>
        The next cell gets chosen and filled correctly,
        and then the program goes into an infinite loop in <code>find_candidates</code>.
        Inside this loop,
        <code>min_set</code> contains the points (2,2) and (1,2),
        and <code>min_val</code> is -1.
        That's our problem:
        our marker value, -1,
        is less than any of the actual values in the grid.
        Once we have marked two cells,
        each of those marked cells is adjacent to another marked cell,
        so we are repeatedly re-marking cells that have already been marked
        without ever growing the marked region.
      </p>

      <p>
        This is easy to fix.
        The code that caused the problem is:
      </p>

<pre src="src/dev/invperc_initial.py">
def find_candidates(grid):
    N = len(grid)
    min_val = sys.maxint
    min_set = set()
    for x in range(N):
        for y in range(N):
            if is_candidate(grid, x, y):
                ...handle == min_val and &lt; min_val cases...
</pre>

      <p class="continue">
        All we have to do is insert a check to say,
        "If this cell is already filled,
        continue to the next iteration of the loop."
        The code is:
      </p>

<pre src="src/programming/invperc_no_refill.py">
def find_candidates(grid):
    N = len(grid)
    min_val = sys.maxint
    min_set = set()
    for x in range(N):
        for y in range(N):
<span class="highlight">            if grid[x][y] == FILLED:
                pass
            elif</span> is_candidate(grid, x, y):
            ...handle == min_val and &lt; min_val cases...
</pre>

      <p class="continue">
        With this change,
        our program now runs for several different values of N.
        But that doesn't prove that it's correct;
        in order to convince ourselves of that,
        we're going to have to do a bit more work.
      </p>

      <div class="keypoints" id="k:bugs">
        <h3>Summary</h3>
        <ul>
          <li idea="paranoia">Test programs with successively more complex cases.</li>
        </ul>
      </div>

    </section>

    <section id="s:refactor">

      <h2>Refactoring</h2>

      <div class="understand" id="u:refactor">
        <h3>Understand:</h3>
        <ul>
          <li>That reorganizing code can make testing (and maintenance) easier.</li>
          <li>That randomness of any kind makes programs hard to test.</li>
          <li>How to replace pseudo-random behavior in programs with predictable behavior.</li>
        </ul>
      </div>

      <p>
        We have found and fixed one bug in our program,
        but how many others <em>haven't</em> we found?
        More generally,
        how do we validate and verify a program like this?
        Those two terms sound similar, but mean different things.
        Verification means, "Is our program free of bugs?"
        or, "Did we built the program right?"
        Validation means, "Are we implementing the right model?"
        i.e., "Did we build the right thing?"
        The second question depends on the science we're doing,
        so we'll concentrate on the first.
      </p>

      <p>
        To begin addressing it,
        we need to make our program more testable.
        And since testing anything that involves randomness is difficult,
        we need to come up with examples that <em>aren't</em> random.
        One is a grid has the value 2 everywhere,
        except in three cells that we have filled with 1's
        (<a href="#f:test_case_grid">Figure XXX</a>).
        If our program is working correctly,
        it should fill exactly those three cells and nothing else.
        If it doesn't,
        we should be able to figure out pretty quickly why not.
      </p>

      <figure id="f:test_case_grid">
        <img src="img/python/test_case_grid.png" alt="Test Case" />
      </figure>

      <p>
        How do we get there from here?
        The overall structure of our program is shown
        in <a href="#f:before_refactoring">Figure XXX</a>:
      </p>

      <figure id="f:before_refactoring">
        <img src="img/python/before_refactoring.png" alt="Program Before Refactoring" />
      </figure>

      <p class="continue">
        The function we want to test is <code>fill_grid</code>,
        so let's reorganize our code to make it easier to create specific grids.
        Grids are created by the function <code>create_random_grid</code>,
        which takes the grid size and random value range as arguments:
      </p>

<pre>
def create_random_grid(N, Z):
    ...

def main(arguments):
    ...
    grid = create_random_grid(grid_size, value_range)
    ...
</pre>

      <p>
        Let's split that into two pieces.
        The first will create an N&times;N grid containing the value 0,
        and the second will overwrite those values with random values in the range 1 to Z:
      </p>

<pre>
...
def create_grid(N):
    ...

def fill_grid_random(grid, Z):
    ...

def main(arguments):
    ...
    grid = create_grid(grid_size)
    fill_grid_random(grid, value_range)
    ...
</pre>

      <p class="continue">
        We can now use some other function to fill the grid with non-random values
        when we want to test specific cases,
        <em>without</em> duplicating the work of creating the grid structure.
      </p>

      <p>
        Another part of the program we will need to change is
        the <code>main</code> function
        that takes command-line arguments
        and converts them into a grid size,
        a range of random values,
        and a random number seed:
      </p>

<pre>
def main(arguments):
    '''Run the simulation.'''

    # Parse parameters.
    try:
        grid_size = int(arguments[0])
        value_range = int(arguments[1])
        random_seed = int(arguments[2])
    except IndexError:
        fail('Expected 3 arguments, got %d' % len(arguments))
    except ValueError:
        fail('Expected integer arguments, got %s' % str(arguments))

    # Run simulation.
    ...
</pre>

      <p>
        Let's introduce a new argument in the first position called <code>scenario</code>:
      </p>

<pre>
def main(arguments):
    '''Run the simulation.'''

    # Parse parameters.
    try:
        <span class="highlight">scenario = arguments[0]
        grid_size = int(arguments[1])
        value_range = int(arguments[2])
        random_seed = int(arguments[3])</span>
    except IndexError:
        fail('Expected 3 arguments, got %d' % len(arguments))
    except ValueError:
        fail('Expected integer arguments, got %s' % str(arguments))

    # Run simulation.
    ...
</pre>

      <p class="continue">
        <code>scenario</code> doesn't need to be converted to an integer:
        it's just a string value specifying what we want to do.
        If the user gives us the word "random",
        we'll do exactly what we've been doing all along.
        For the moment,
        we will fail if the user gives us anything else,
        but later on we will use <code>scenario</code> to determine
        which of our test cases we want to run.
      </p>

      <p>
        But wait a moment:
        we're not going to use random numbers when we fill the grid manually for testing.
        We're also not going to need the value range,
        or even the grid size,
        so let's move argument handling and random number generation seeding
        into the <code>if</code> branch that handles the random scenario.
        Once we make this change,
        we determine the scenario by looking at the first command-line argument,
        and then if that value is the word "random",
        we look at the remaining arguments to determine the grid size,
        the value range, and the random seed.
        If the first argument <em>isn't</em> the word "random", then we fail:
      </p>

<pre>
    # Parse parameters.
    scenario = arguments[0]
    try:
        if scenario == 'random':

            # Parse arguments.
            grid_size = int(arguments[1])
            value_range = int(arguments[2])
            random_seed = int(arguments[3])

            # Run simulation.
            random.seed(random_seed)
            grid = create_random_grid(grid_size, value_range)
            mark_filled(grid, grid_size/2, grid_size/2)
            num_filled_cells = fill_grid(grid) + 1
            print '%d cells filled' % num_filled_cells

        else:
            fail('Unknown scenario "%s"' % scenario)
    except IndexError:
        fail('Expected 3 arguments, got %d' % len(arguments))
    except ValueError:
        fail('Expected integer arguments, got %s' % str(arguments))
</pre>

      <p>
        The block of code inside the <code>if</code> is large enough
        that it's hard to see how what <code>else</code>
        and the two <code>except</code>s line up with.
        Let's factor some more:
      </p>

<pre>
def do_random(arguments):
    # Parse arguments.
    grid_size = int(arguments[1])
    value_range = int(arguments[2])
    random_seed = int(arguments[3])

    # Run simulation.
    random.seed(random_seed)
    grid = create_random_grid(grid_size, value_range)
    mark_filled(grid, grid_size/2, grid_size/2)
    num_filled_cells = fill_grid(grid) + 1
    print '%d cells filled' % num_filled_cells

def main(arguments):
    '''Run the simulation.'''

    scenario = arguments[0]
    try:
        if scenario == 'random':
            do_random(arguments)
        else:
            fail('Unknown scenario "%s"' % scenario)
    except IndexError:
        fail('Expected 3 arguments, got %d' % len(arguments))
    except ValueError:
        fail('Expected integer arguments, got %s' % str(arguments))

# Main driver.
if __name__ == '__main__':
    main(sys.argv[1:])
</pre>

      <p>
        That's easier to follow,
        but selecting everything but the first command-line argument
        in the <code>if</code> at the bottom,
        then selecting everything but the first of <em>those</em> values
        at the start of <code>main</code>,
        is a bit odd.
        Let's clean that up,
        and move the <code>try</code>/<code>except</code> into <code>do_random</code> at the same time
        (since the functions that handle other scenarios might have different error cases).
      </p>

<pre src="src/dev/invperc_refactoring.py">
def do_random(arguments):
    '''Run a random simulation.'''

    # Parse arguments.
    try:
        grid_size = int(arguments[1])
        value_range = int(arguments[2])
        random_seed = int(arguments[3])
    except IndexError:
        fail('Expected 3 arguments, got %d' % len(arguments))
    except ValueError:
        fail('Expected integer arguments, got %s' % str(arguments))

    # Run simulation.
    random.seed(random_seed)
    grid = create_random_grid(grid_size, value_range)
    mark_filled(grid, grid_size/2, grid_size/2)
    num_filled_cells = fill_grid(grid) + 1
    return num_filled_cells
    print '%d cells filled' % num_filled_cells

def main(scenario, arguments):
    '''Run the simulation.'''

    if scenario == 'random':
        do_random(arguments)
    else:
        fail('Unknown scenario "%s"' % scenario)

# Main driver.
if __name__ == '__main__':
    assert len(sys.argv) &gt; 1, 'Must have at least a scenario name'
    main(sys.argv[1], sys.argv[2:])
</pre>

      <figure id="f:revised_structure">
        <img src="img/python/revised_structure.png" alt="Result of Refactoring" />
      </figure>

      <p>
        <a href="#f:revised_structure">Figure XXX</a> shows
        the structure of our program after refactoring.
        We have the documentation string,
        which we've updated to remind people that the first argument is the name of the scenario.
        Our <code>fail</code> function hasn't changed.
        We've split grid creation into two functions.
        Our <code>fill_grid</code> function now fills the middle cell and returns the count of <em>all</em> filled cells.
        And we have a function to parse command-line arguments.
        This argument-parsing function is actually specific to the random case.
        We should probably rename it, to make that clear.
      </p>

      <p>
        Now let's step back.
        We were supposed to be testing our program,
        but in order to make it more testable,
        we had to reorganize it first.
        The jargon term for this is "refactoring",
        which means "changing a program's structure without modifying its behavior or functionality in order to improve its quality."
        Now that we've done this refactoring,
        we can write tests more easily.
        More importantly,
        now that we've thought this through,
        we are more likely to write the next program of this kind in a testable way
        right from the start.
      </p>

      <div class="keypoints" id="k:refactor">
        <h3>Summary</h3>
        <ul>
          <li>Refactor programs as necessary to make testing easier.</li>
          <li>Replace randomness with predictability to make testing easier.</li>
        </ul>
      </div>

    </section>

    <section id="s:test">

      <h2>Testing</h2>

      <div class="understand" id="u:test">
        <h3>Understand:</h3>
        <ul>
          <li>How to build scaffolding to aid testing.</li>
          <li>That building test scaffolding saves time in the long run.</li>
        </ul>
      </div>

      <p>
        Let's start by adding another clause to the main body of the program
        so that if the scenario is <code>"5x5_line"</code> we will create a 5&times;5 grid,
        fill a line of cells from the center to the edge with lower values,
        and then check that <code>fill_grid</code> does the right thing
        (<a href="#f:5x5_line">Figure XXX</a>):
      </p>

<pre src="src/dev/invperc_5x5.py">
if __name__ == '__main__':
    scenario = sys.argv[1]
    if scenario == 'random':
        do_random(arguments)
    elif scenario == '5x5_line':
        do_5x5_line()
    else:
        fail('Unknown scenario "%s"' % scenario)
</pre>

      <figure id="f:5x5_line">
        <img src="img/python/5x5_line.png" alt="Racing for the Border" />
      </figure>

      <p>
        The function <code>do_5x5_line</code> is pretty simple:
      </p>

<pre src="src/dev/invperc_5x5.py">
def do_5x5_line():
    '''Run a test on a 5x5 grid with a run to the border.'''

    grid = create_grid(5)
    init_grid_5x5_line(grid)
    num_filled_cells = fill_grid(grid)
    check_grid_5x5_line(grid, num_filled_cells)
</pre>

      <p class="continue">
        The functions <code>create_grid</code> and <code>fill_grid</code> already exist:
        in fact,
        the whole point of this exercise is that we're re-using <code>fill_grid</code>
        in order to test it.
        The new test-specific functions
        are <code>init_grid_5x5_line</code> and <code>check_grid_5x5_line</code>.
        We're going to have to write a similar pair of functions for each of our tests,
        so we'll write the first pair,
        then use that experience to guide some further refactoring.
        Here's the first function
      </p>

<pre src="src/dev/invperc_5x5.py">
def init_grid_NxN_line(grid):
    '''Fill NxN grid with straight line to edge for testing purposes.'''

    N = len(grid)
    for x in range(N):
        for y in range(N):
            grid[x][y] = 2

    for i in range(N/2 + 1):
        grid[N/2][i] = 1
</pre>

      <p>
        It's just as easy to write this function for the N&times;N case as for the 5&times;5 case,
        so we generalize early.
        The first part of the function is easy to understand:
        find the value of N by looking at the grid,
        then fill all of the cells with the integer 2.
        The second part,
        which fills the cells from the center to the edge in a straight line with the lower value 1,
        isn't as easy to understand:
        it's not immediately obvious that <code>i</code> should go in the range from 0 to N/2+1,
        or that the X coordinate should be N/2 and the Y coordinate should be <code>i</code> for the cells that we want to fill.
      </p>

      <p>
        When we say "it's not obvious,"
        what we mean is,
        "There's the possibility that it will contain bugs."
        If there are bugs in our test cases,
        then we're just making more work for ourselves.
        We'll refactor this code later so that it's easier for us to see that it's doing the right thing.
      </p>

      <p>
        Here's the code that checks that an N&times;N grid
        with a line of cells from the center to the edge has been filled correctly:
      </p>

<pre>
def check_grid_NxN_line(grid, num_filled):
    '''Check NxN grid straight line grid.'''

    N = len(grid)
    assert num_filled == N/2 + 1, 'Wrong number filled'

    for x in range(N):
        for y in range(N):
            if (x == N/2) and (y &lt;= N/2):
                assert grid[x][y] == FILLED, 'Not filled!'
            else:
                assert grid[x][y] != FILLED, 'Wrongly filled!'
</pre>

      <p class="continue">
        Again,
        it's as easy to check for the N&times;N case as the 5&times;5 case,
        so we've generalized the function.
        But take a look at that <code>if</code>:
        are we sure that the only cells that should be filled are
        the ones with X coordinate equal to N/2 and Y coordinate from 0 to N/2?
        Shouldn't that be N/2+1?
        Or 1 to N/2,
        or maybe the X coordinate should be N/2+1.
      </p>

      <p>
        In fact,
        these two functions <em>are</em> correct,
        and when they're run,
        they report that <code>fill_grid</code> behaves properly.
        But writing and checking two functions like this for each test
        won't actually increase our confidence in our program,
        because the tests themselves might contain bugs.
        We need a simpler way to create and check tests,
        so that our testing is actually helping us create a correct program
        rather than giving us more things to worry about.
        How do we do that?
      </p>

      <p>
        Let's go back to the example in <a href="#f:5x5_line">Figure XXX</a>.
        Why don't we just "draw" our test cases exactly as shown?
        The reason is that modern programming languages don't actually let you draw things,
        but we can get close with a little bit of work.
        Let's write our test fixture as a string:
      </p>

<pre>
fixture = '''2 2 2 2 2
             2 2 2 2 2
             1 1 1 2 2
             2 2 2 2 2
             2 2 2 2 2'''
</pre>

      <p class="continue">
        and write the result as a similar string:
      </p>

<pre>
result = '''. . . . .
            . . . . .
            * * * . .
            . . . . .
            . . . . .'''
</pre>

      <p class="continue">
        As you can probably guess,
        the '*' character means "this cell should be filled",
        while the '.' means "this cell should hold whatever value it had at the start".
        Here's how we want to use them:
      </p>

<pre src="src/dev/invperc_fixture.py">
def do_5x5_line():
    '''Run a test on a 5x5 grid with a run to the border.'''

    fixture  = '''2 2 2 2 2
                  2 2 2 2 2
                  1 1 1 2 2
                  2 2 2 2 2
                  2 2 2 2 2'''

    expected = '''. . . . .
                  . . . . .
                  * * * . .
                  . . . . .
                  . . . . .'''

    fixture = parse_grid(fixture)
    num_filled_cells = fill_grid(fixture)
    check_result(expected, fixture, num_filled_cells)
</pre>

      <p>
        Parsing a grid is pretty easy:
      </p>

<pre src="src/dev/invperc_fixture.py">
def parse_grid(fixture):
    '''Turn a string representation of a grid into a grid of numbers.'''

    result = [x.strip().split() for x in fixture.split('\n')]
    size = len(result)
    for row in result:
        if len(row) != size:
            fail('Badly formed fixture')
        for i in range(len(row)):
            row[i] = int(row[i])
    return result
</pre>

      <p class="continue">
        Checking cells is pretty easy too:
      </p>

<pre src="src/dev/invperc_fixture.py">
def check_result(expected, grid, num_filled):
    '''Check the results of filling.'''
    expected, count = convert_grid(expected)

    if len(expected) != len(grid):
        fail('Mis-match between size of expected result and size of grid')
    if count != num_filled:
        fail('Wrong number of cells filled')

    for i in range(len(expected)):
        g = grid[i]
        e = expected[i]
        if len(g) != len(e):
            fail('Rows are not the same length')
        for j in range(len(g)):
            if g[j] and (e[j] != FILLED):
                fail('Cell %d,%d should be filled but is not' % (i, j))
            elif (not g[j]) and (e[j] == FILLED):
                fail('Cell %d,%d should not be filled but is' % (i, j))
    return result
</pre>

      <p>
        We still have one function to write,
        though&mdash;the one that parses a string of '*' and '.' characters
        and produces a grid of trues and falses.
        But this is almost exactly the same as what we do to parse a fixture.
        The only difference is how we convert individual items.
        Let's refactor:
      </p>

<pre src="src/dev/invperc_fixture.py">
<span class="highlight">def is_star(x):
    '''Is this cell supposed to be filled?'''
    return x == '*'</span>

def parse_general(fixture, <span class="highlight">converter</span>):
    '''Turn a string representation of a grid into a grid of <span class="highlight">values</span>.'''

    result = [x.strip().split() for x in fixture.split('\n')]
    size = len(result)
    for row in result:
        if len(row) != size:
            fail('Badly formed fixture')
        for i in range(len(row)):
            row[i] = <span class="highlight">converter</span>(row[i])
    return result

def do_5x5_line():
    '''Run a test on a 5x5 grid with a run to the border.'''

    ...define fixture and expected strings...

    fixture = <span class="highlight">parse_general</span>(fixture, <span class="highlight">int</span>)
    num_filled_cells = fill_grid(fixture)
    expected = <span class="highlight">parse_general(fixture, is_star)</span>
    check_result(expected, fixture, num_filled_cells)
</pre>

      <p>
        Writing the functions to parse fixture strings might seem like a lot of work,
        but what are you comparing it to?
        Are you comparing the time to write those functions to
        the time it would take to inspect printouts of real grids,
        or step through the program over and over again in the debugger?
        And did you think to include the time it would take to re-do this after every change to your program?
        Or are you comparing it to the time it would take to retract a published paper
        after you find a bug in your code?
      </p>

      <p>
        In real applications,
        it's not unusual for test code to be anywhere from 20% to 200% of the size
        of the actual application code
        (and yes, 200% does mean more test code than application code).
        But that's no different from physical experiments:
        if you look at the size and cost of the machines used to create a space probe,
        it's many times greater than the size and cost of the space probe itself.
      </p>

      <p>
        The good news is,
        we're now in a position to replace our <code>fill_grid</code> function
        with one that is harder to get right,
        but which will run many times faster.
        If our tests have been designed well,
        they shouldn't have to be rewritten because they'll all continue to work the same way.
        This is a common pattern in scientific programming:
        create a simple version first,
        check it,
        then replace the parts one by one with more sophisticated parts that are harder to check
        but give better performance.
      </p>

      <div class="keypoints" id="k:test">
        <h3>Summary</h3>
        <ul>
          <li>Write support code to make testing easier.</li>
        </ul>
      </div>

    </section>

    <section id="s:performance">

      <h2>Performance</h2>

      <div class="understand" id="u:performance">
        <h3>Understand:</h3>
        <ul>
          <li>That many programs aren't actually worth speeding up.</li>
          <li>That we should make sure programs are correct before trying to improve their performance.</li>
          <li>How to measure a program's running time.</li>
          <li>How to estimate the way a program's running time grows with problem size.</li>
        </ul>
      </div>

      <blockquote>
        Machine-independent code has machine-independent performance.
        <br/>
        &mdash; anonymous
      </blockquote>

      <p>
        Now that it's easy to write tests,
        we can start worrying about our program's performance.
        When people use that phrase,
        they almost always mean the program's speed.
        In fact, speed is why computers were invented:
        until networks and fancy graphics came along,
        the reason computers existed was
        to do in minutes or hours what would take human beings weeks or years.
      </p>

      <p>
        Scientists usually want programs to go faster for three reasons.
        First, they want a solution to a single large problem,
        such as, "What's the lift of this wing?"
        Second, they have many problems to solve,
        and need answers to all of them&mdash;a typical example is,
        "Compare this DNA sequences to every one in the database and tell me what the closest matches are."
        Finally, scientists may have a deadline and a fixed set of resources
        and want to solve as big a problem as possible within the constraints.
        Weather prediction falls into this category:
        given more computing power,
        scientists use more accurate (and more computationally demanding) models,
        rather than solving the old models faster.
      </p>

      <p>
        Before trying to make a program go faster,
        there are two questions we should always ask ourselves.
        First, does our program actually need to go faster?
        If we only use it once a day,
        and it only takes a minute to run,
        speeding it up by a factor of 10 is probably not worth
        a week of our time.
      </p>

      <p>
        Second, is our program correct?
        There's no point making a buggy program faster:
        more wrong answers per unit time doesn't move science forward
        (although it may help us track down a bug).
        Just as importantly,
        almost everything we do to make programs faster also makes them more complicated,
        and therefore harder to debug.
        If our starting point is correct,
        we can use its output to check the output of our optimized version.
        If it isn't, we've probably made our life more difficult.
      </p>

      <p>
        Let's go back to invasion percolation.
        To find out how fast our program is,
        let's add a few lines to the program's main body:
      </p>

<pre>
if __name__ == '__main__':

    ...get simulation parameters from command-line arguments...

    # Run simulation.
<span class="highlight">    start_time = time.time()</span>
    random.seed(random_seed)
    grid = create_random_grid(grid_size, value_range)
    mark_filled(grid, grid_size/2, grid_size/2)
    num_filled = fill_grid(grid) + 1
<span class="highlight">    elapsed_time = time.time() - start_time</span>
<span class="highlight">    print 'program=%s size=%d range=%d seed=%d filled=%d time=%f' % \</span>
<span class="highlight">          (sys.argv[0], grid_size, value_range, random_seed, num_filled, elapsed_time)</span>
    if graphics:
        show_grid(grid)
</pre>

      <p class="continue">
        The first new line records the time when the program starts running.
        The other new lines use that to calculate how long the simulation took,
        and then display the program's parameters and running time.
      </p>

      <p>
        We need to make one more change
        before we start running lots of simulation.
        We were seeding the random number generator using the computer's clock time:
      </p>

<pre>
    start_time = time.time()
    ...
    random_seed = int(start_time)
</pre>

      <p class="continue">
        But what if a simulation runs very quickly?
        <code>time.time()</code> returns a floating point number;
        <code>int</code> truncates this by throwing away the fractional part,
        so if our simulation runs in less than a second,
        two (or more) might wind up with the same seed,
        which in turn will mean they have the same "random" values in their grids.
        (This isn't a theoretical problem&mdash;we actually tripped over it while writing this chapter.)
      </p>

      <p>
        One way to fix this is to to shift those numbers up.
        For now let's guess that every simulation will take at least a tenth of a millisecond to run,
        so we'll multiply the start time by ten thousand,
        then truncate it so that it is less than a million:
      </p>

<pre>
RAND_SCALE = 10000    # Try to make sure random seeds are distinct.
RAND_RANGE = 1000000  # Range of random seeds.
...
    random_seed = int(start_time * RAND_SCALE) % RAND_RANGE
</pre>

      <p>
        The final step is to write a shell script that runs the program multiple times
        for various grid sizes:
      </p>

<pre>
for size in {11..81..10}
do
  for counter in {1..20}
  do
    python invperc.py -g -n $size -v 100
  done
done
</pre>

      <p class="continue">
        (We could equally well have added a few more lines to the program itself
        to run a specified number of simulations
        instead of just one.)
        If we average the 20 values for each grid size, we get the following:
      </p>

      <table class="outlined">
        <tr> <td></td> <td>11</td> <td>21</td> <td>31</td> <td>41</td> <td>51</td> <td>61</td> </tr>
        <tr> <td>cells&nbsp;filled</td> <td>16.60</td> <td>45.75</td> <td>95.85</td> <td>157.90</td> <td>270.50</td> <td>305.75</td> </tr>
        <tr> <td>time&nbsp;taken</td> <td>0.003971</td> <td>0.035381</td> <td>0.155885</td> <td>0.444160</td> <td>1.157350</td> <td>1.909516</td> </tr>
        <tr> <td>time/cell</td> <td>0.000239</td> <td>0.000773</td> <td>0.001626</td> <td>0.002813</td> <td>0.004279</td> <td>0.006245</td> </tr>
      </table>

      <p>
        Is that good enough?
        Let's fit a couple of fourth-order polynomials to our data:
      </p>

      <table class="outlined">
        <tr> <td></td> <td><em> x<sup>4</sup> </em></td> <td><em> x<sup>3</sup> </em></td> <td><em> x<sup>2</sup> </em></td><td><em>x<sup>1</sup></em></td><td><em>x<sup>0</sup></em></td></tr>
        <tr> <td>time&nbsp;taken</td> <td>2.678&times;10<sup> -07</sup></td> <td>-2.692&times;10<sup> -05</sup></td> <td>1.760&times;10<sup> -03</sup></td> <td>-3.983&times;10<sup> -02</sup></td> <td>2.681&times;10<sup>-01</sup></td></tr>
        <tr> <td>time/cell</td> <td>-1.112&times;10<sup> -10</sup></td> <td>1.996&times;10<sup> -08</sup></td> <td>4.796&times;10<sup> -07</sup></td> <td>2.566&times;10<sup> -05</sup></td> <td>-1.295&times;10<sup>-04</sup></td></tr>
      </table>

      <p>
        According to the first polynomial,
        a single run on a 1001&times;1001 grid will take almost 68 hours.
        What can we do to make it faster?
        The <em>wrong</em> answer is,
        "Guess why it's slow, start tweaking the code, and hope for the best."
        The right answer is to ask the computer where the time is going.
      </p>

      <p>
        Before we do that,
        though,
        we really ought to justify our decision to model the program's performance
        using a fourth-order polynomial.
        Suppose our grid is N&times;N.
        Each time it wants to find the next cell to fill,
        our program examines each of the N<sup>2</sup> cells.
        In the best case,
        it has to fill about N/2 cells to reach the boundary
        (basically, by racing straight for the edge of the grid).
        In the worst case,
        it has to fill all of the interior cells
        before "breaking out" to the boundary,
        which means it has to fill (N-2)&times;(N-2) cells.
        That worst case therefore has a runtime of N<sup>2</sup>(N-2)<sup>2</sup> steps,
        which,
        for large N,
        is approximately N<sup>4</sup>.
        (For example,
        when N is 71,
        the difference between the two values is only about 5%.)
      </p>

      <p>
        This kind of analysis is computing's equivalent of engineers' back-of-the-envelope calculations.
        In technical terms,
        we would say that our algorithm is O(N<sup>4</sup>).
        In reality,
        because we're creating a fractal,
        we're actually going to fill about N<sup>1.5</sup> cells on average,
        so our running time is actually O(N<sup>3.5</sup>).
        That's still too big for practical simulations,
        though,
        so it's time to figure out what we can do about it.
      </p>

      <div class="keypoints" id="k:performance">
        <h3>Summary</h3>
        <ul>
          <li>Scientists want faster programs both to handle bigger problems and to handle more problems with available resources.</li>
          <li idea="perf">Before speeding a program up, ask, "Does it need to be faster?" and, "Is it correct?"</li>
          <li>Recording start and end times is a simple way to measure performance.</li>
          <li idea="algo">Analyze algorithms to predict how a program's performance will change with problem size.</li>
        </ul>
      </div>

    </section>

    <section id="s:profile">

      <h2>Profiling</h2>

      <div class="understand" id="u:profile">
        <h3>Understand:</h3>
        <ul>
          <li>What an execution profiler is.</li>
          <li>The difference between deterministic and statistical profilers.</li>
          <li>How to interpret a profiler's output.</li>
        </ul>
      </div>

      <p>
        Timing an entire program is a good way to find out if we're making things better or not,
        but some way to know where the time is going would be even better.
        The tool that will do that for us is called a <a href="glossary.html#profiler">profiler</a>
        because it creates a profile of a program's execution time,
        i.e.,
        it reports how much time is spent in each function in the program, or even on each line.
      </p>

      <p>
        There are two kinds of profilers.
        A <a href="glossary.html#deterministic-profiler">deterministic</a> profiler inserts instructions in a program
        to record the clock time at the start and end of every function.
        It doesn't actually modify the source code:
        instead, it adds those instructions behind the scenes after the code has been translated into something the computer can actually run.
        For example, suppose our program looks like this:
      </p>

<pre>
def swap(values):
    for i in range(len(values)/2):
        values[i], values[-1-i] = values[-1-i], values[i]

def upto(N):
    for i in xrange(1, N):
        temp = [0] * i
        swap(temp)

upto(100)
</pre>

      <p class="continue">
        A deterministic profiler would insert timing calls that worked like this:
      </p>

<pre>
def swap(values):
<span class="highlight">    _num_calls['swap'] += 1</span>
<span class="highlight">    _start_time = time.time()</span>
    for i in range(len(values)/2):
        values[i], values[-1-i] = values[-1-i], values[i]
<span class="highlight">    _total_time['swap'] += (time.time() - _start_time)</span>

def upto(N):
<span class="highlight">    _num_calls['upto'] += 1</span>
<span class="highlight">    _start_time = time.time()</span>
    for i in xrange(1, N):
        temp = [0] * i
        swap(temp)
<span class="highlight">    _total_time['upto'] += (time.time() - _start_time)</span>

<span class="highlight">_num_calls['swap'] = 0</span>
<span class="highlight">_total_time['swap'] = 0</span>
<span class="highlight">_num_calls['upto'] = 0</span>
<span class="highlight">_total_time['upto'] = 0</span>
upto(100)
</pre>

      <p class="continue">
        (Note that the profiler wouldn't actually change the source of our program;
        these extra operations are inserted after the program has been loaded into memory.)
      </p>

      <p>
        Once the program has been run,
        the profiler can use the two dictionaries <code>_num_calls</code> and <code>_total_time</code>
        to report the average running time per function call.
        Going further,
        the profiler can also keep track of which functions are calling which,
        so that (for example) it can report times for calls to <code>swap</code> from <code>upto</code>
        separately from calls to <code>swap</code> from some other function <code>downfrom</code>.
      </p>

      <p>
        The problem with deterministic profiling is that
        adding those timing calls changes the runtime of the functions being measured,
        since reading the computer's clock and recording the result both take time.
        The smaller the function's runtime, the larger the distortion.
        This can be avoided by using a <a href="glossary.html#statistical-profiler">statistical</a> profiler.
        Instead of adding timing calls to the code,
        it freezes the program every millisecond or so and makes a note of what function is running.
        Like any sampling procedure,
        this produces become more accurate as more data is collected,
        so statistical profilers work well on long-running programs,
        but can produce misleading results for short ones.
      </p>

      <p>
        Python's <code>cProfile</code> module is a deterministic profiler.
        It records times and call counts and saves data in a file for later analysis.
        We can use it to see where time goes in our initial list-of-lists invasion percolation program:
      </p>

<pre src="src/dev/profile_first.py">
import cProfile, pstats
from invperc import main

cProfile.run('main(["51", "100", "127391"])', 'list.prof')
p = pstats.Stats('list.prof')
p.strip_dirs().sort_stats('time').print_stats()
</pre>

      <p>
        We start by importing <code>cProfile</code>, the actual profiling tool, on line 1.
        We also import <code>pstats</code>,
        a helper module for analyzing the data files <code>cProfile</code> produces.
      </p>

      <p>
        The second line imports the <code>main</code> function from our program.
        We give that starting point to <code>cProfile.run</code> on line 3,
        along with the name of the file we want the profiling results stored in.
        Notice that the call is passed as a string:
        <code>cProfile</code> uses Python's built-in <code>eval</code> function
        to run the command in this string,
        just as if we had typed it into the interpreter.
        Notice also that the arguments are passed as strings,
        since that's what <code>main</code> is expecting.
      </p>

      <p>
        Line 4 reads the profiling data back into our program
        and wraps it up in a <code>pstats.Stats</code> object.
        It may seem silly to write the data out only to read it back in,
        but the two activities are often completely separate:
        we can accumulate profiling data across many different runs of a program,
        then analyze it all at once.
      </p>

      <p>
        Finally, line 5 strips directory names off the accumulated data,
        sorts them according to run time, and prints the result.
        We strip directory names because all of the code we're profiling is in a single file;
        in larger programs, we'll keep the directory information
        (even though it makes the output a bit harder to read)
        so that we can separate <code>fred.calculate</code>'s running time from <code>jane.calculate</code>'s.
      </p>

      <p>
        Here's what the output looks like:
      </p>

<pre src="src/dev/profile_first.txt">
135 cells filled
Thu Jun 28 13:54:55 2012    list.prof

         697631 function calls in 0.526 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   339489    0.355    0.000    0.376    0.000 invperc.py:64(is_candidate)
      134    0.136    0.001    0.515    0.004 invperc.py:73(find_candidates)
   340029    0.021    0.000    0.021    0.000 {len}
     2601    0.005    0.000    0.005    0.000 random.py:160(randrange)
     7072    0.004    0.000    0.004    0.000 {range}
     2601    0.002    0.000    0.007    0.000 random.py:224(randint)
        1    0.001    0.001    0.008    0.008 invperc.py:39(fill_random_grid)
        1    0.001    0.001    0.001    0.001 invperc.py:27(create_grid)
        1    0.001    0.001    0.516    0.516 invperc.py:92(fill_grid)
     2735    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
     2652    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      134    0.000    0.000    0.000    0.000 random.py:259(choice)
      135    0.000    0.000    0.000    0.000 invperc.py:52(mark_filled)
        1    0.000    0.000    0.526    0.526 invperc.py:108(do_random)
        1    0.000    0.000    0.526    0.526 invperc.py:186(main)
        1    0.000    0.000    0.000    0.000 {function seed at 0x0221C2B0}
       40    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 random.py:99(seed)
        1    0.000    0.000    0.526    0.526 &lt;string&gt;:1(&lt;module&gt;)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
</pre>

      <p>
        The columns are the number of calls,
        the total time spent in that function,
        the time per call,
        the total cumulative time (i.e., the total time for that function and everything it calls),
        the cumulative time per call,
        and then which function the stat is for.
        As we can see,
        <code>is_candidate</code> accounts for two thirds of our runtime:
        if we want to make this program faster,
        that's what we should speed up.
      </p>

      <div class="box">

        <h3>Wall Clock Time vs. CPU Time</h3>

        <p>
          When profiling programs,
          particularly on machines that are running other applications at the same time,
          it's important to remember the distinction between
          <a href="glossary.html#cpu-time">CPU time</a>
          and
          <a href="glossary.html#wall-clock-time">wall-clock time</a>.
          The first is how much time the computer's processor actually spent running the program;
          the second is how long the program actually took to run.
          The two are different because the CPU has a lot of things to do
          besides running our program,
          even on a machine that's supposedly otherwise idle.
          The operating system itself needs time,
          for example,
          as do disk and network I/O.
        </p>

      </div>

      <div class="keypoints" id="k:profile">
        <h3>Summary</h3>
        <ul>
          <li idea="tools">Use a profiler to determine which parts of a program are responsible for most of its running time.</li>
        </ul>
      </div>

    </section>

    <section id="s:lazy">

      <h2>A New Beginning</h2>

      <div class="understand" id="u:lazy">
        <h3>Understand:</h3>
        <ul>
          <li>That using a more efficient algorithm is usually a better way to improve performance than tuning an inefficient algorithm.</li>
          <li>That programs can usually trade space (extra memory) for running time.</li>
          <li>The importance of building a simple, trustworthy version of a program before trying to build a faster but more complex version.</li>
        </ul>
      </div>

      <p>
        If checking whether cells are candidates is the slowest step,
        let's try to reduce the number of times we have to do that.
        Instead of re-examining every cell in the grid each time we want to fill one,
        let's keep track of which cells are currently on the boundary in some kind of auxiliary data structure,
        then choose randomly from all the cells in that set that share the current lowest value.
        When we fill in a cell,
        we add its neighbors to the "pool" of neighbors (unless they're already there).
      </p>

      <p>
        Here's the modified <code>fill_grid</code> function:
      </p>

<pre src="src/dev/invperc_pool.py">
def fill_grid(grid):
    '''Fill an NxN grid until filled region hits boundary.'''

    x, y = grid.size/2, grid.size/2
    pool = set()
    pool.add((grid[x][y], x, y))
    num_filled = 0
    on_edge = False

    while not on_edge:
        x, y = get_next(pool)
        grid.mark_filled(x, y)
        num_filled += 1
        if (x == 0) or (x == grid.size-1) or (y == 0) or (y == grid.size-1):
            on_edge = True
        else:
            if x &gt; 0:           make_candidate(grid, pool, x-1, y)
            if x &lt; grid.size-1: make_candidate(grid, pool, x+1, y)
            if y &gt; 0:           make_candidate(grid, pool, x,   y-1)
            if y &lt; grid.size-1: make_candidate(grid, pool, x,   y+1)

    return num_filled
</pre>

      <p class="continue">
        This function creates a set called <code>pool</code>
        that keeps track of the cells currently on the edge of the filled region.
        Each loop iteration gets the next cell out of this pool,
        fills it in,
        and (potentially) adds its neighbors to the set.
      </p>

      <p>
        This function is 21 lines long,
        compared to 15 for our original <code>fill_grid</code> function,
        but four of those six lines are the calls to <code>make_candidate</code>,
        which adds a neighbor to the pool if it isn't already there.
        Let's have a look at <code>get_next</code> and <code>make_candidate</code>:
      </p>

<pre>
def get_next(pool):
    '''Take a cell randomly from the equal-valued front section.'''

    temp = list(pool)
    temp.sort()
    v = temp[0][0]
    i = 1
    while (i &lt; len(temp)) and (temp[i][0] == v):
        i += 1
    i = random.randint(0, i-1)
    v, x, y = temp[i]
    pool.discard((v, x, y))
    return x, y

def make_candidate(grid, pool, x, y):
    '''Ensure that (x, y, v) is a candidate.'''

    v = grid_get(grid, x, y)
    if v == FILLED:
        return
    pool.add((v, x, y))
</pre>

      <p>
        This is definitely more complicated that what we started with:
        we now have to keep a second data structure (the pool) up to date,
        and in sync with the grid.
        But look at the payoff:
      </p>

      <table class="outlined">
        <tr> <td></td> <td>11</td> <td>21</td> <td>31</td> <td>41</td> <td>51</td> <td>61</td> </tr>
        <tr> <td>list&nbsp;of&nbsp;lists</td> <td>0.000333</td> <td>0.025667</td> <td>0.088833</td> <td>0.227167</td> <td>0.455000</td> <td>1.362667</td> </tr>
        <tr> <td>set&nbsp;pool</td> <td>0.000050</td> <td>0.003000</td> <td>0.009100</td> <td>0.016130</td> <td>0.012000</td> <td>0.027050</td> </tr>
        <tr> <td>ratio</td> <td>6.66</td> <td>8.56</td> <td>9.76</td> <td>14.1</td> <td>37.9</td> <td>50.4</td> </tr>
      </table>

      <p>
        Now <em>that</em> is a speedup.
        If we assume that we fill about N<sup>1.5</sup> cells in an N&times;N grid,
        the running time of our algorithm is about N<sup>1.5</sup> instead of N<sup>3.5</sup>,
        because we only need to inspect four new cells in every iteration
        instead of checking all N<sup>2</sup> each time.
        As a result, the bigger our grids get, the bigger our savings are.
      </p>

      <div class="keypoints" id="k:lazy">
        <h3>Summary</h3>
        <ul>
          <li idea="algo">Better algorithms are better than better hardware.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

      <p>
        There are two important lessons to take away from this exercise.
        First, choosing the right algorithms and data structures can yield enormous speedups,
        so we should always look there first for performance gains.
        This is where a broad knowledge of computer science comes in handy:
        any good book on data structures and algorithms describes dozens or hundreds of things
        that are exactly what's needed to solve some obscure but vital performance problem.
      </p>

      <p>
        Second,
        well-structured programs are easier to optimize than poorly-structured ones.
        If we build our program as a collection of functions,
        we ought to be able to change those functions more or less independently of one another
        to try out new ideas.
        As is almost always the case,
        improving the quality of our work improves our performance:
        it is the opposite of an either/or tradeoff.
      </p>

    </section>