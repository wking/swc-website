Title: Sets and Dictionaries in Python
Directory: book

    <ol class="toc">
      <li><a href="#s:sets">Sets</a></li>
      <li><a href="#s:storage">Storage</a></li>
      <li><a href="#s:dict">Dictionaries</a></li>
      <li><a href="#s:examples">Simple Examples</a></li>
      <li><a href="#s:nanotech">Nanotech Inventory</a></li>
      <li><a href="#s:phylotree">Phylogenetic Trees</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <span class="comment"> GVW: add sparse vector example </span>

    <p>
      Fan Fullerene has just joined Molecules'R'Us,
      a nanotechnology startup that fabricates molecules
      using only the highest quality atoms.
      His first job is to build a simple inventory management system
      that compares incoming orders for molecules
      to the stock of atoms in the company's supercooled warehouse
      to see how many of those molecules we can build.
      For example,
      if the warehouse holds 20 hydrogen atoms,
      5 oxygen atoms,
      and 11 nitrogen atoms,
      Fan could make 10 water molecules (H<sub>2</sub>0)
      or 6 ammonia molecules (NH<sub>3</sub>),
      but could not make any methane (CH<sub>4</sub>)
      because there isn't any carbon.
    </p>

    <p>
      Fan could solve this problem using the tools we've seen so far.
      As we'll see, though,
      it's a lot more efficient to do it using a different data structure.
      And "efficient" means both "takes less programmer time to create"
      and "takes less computer time to execute":
      the data structures introduced in this chapter are both simpler to use and faster
      than the lists most programmers are introduced to first.
    </p>

    <section id="s:sets">

      <h2>Sets</h2>

      <div class="understand" id="u:sets">
        <h3>Understand:</h3>
        <span class="comment"> TA: "lists and arrays." In this context, what is the distinction and do they know about that distinction? </span>
        <ul>
          <li>That lists and arrays are not the only data structures available to programmers.</li>
          <li>That a set stores unique values.</li>
          <li>How to perform common operations on sets.</li>
          <li>How to use a set to eliminate duplicate values from data.</li>
        </ul>
      </div>

      <p>
        Let's start with something simpler than our actual inventory problem.
        Suppose we have a list of all the atoms in the warehouse,
        and we want to know which different kinds we have&mdash;not how many,
        but just their types.
        We could solve this problem using a list to store
        the unique atomic symbols we have seen
        as shown in <a href="#f:list_of_atoms">Figure XXX</a>.
      </p>

      <figure id="f:list_of_atoms">
        <img src="img/setdict/list_of_atoms.png" alt="Storing Atomic Symbols in a List" />
      </figure>

      <p>
        Here's a function to add a new atom to the list:
      </p>

<span class="comment"> TA: Here, 'return' is short-circuiting the function once we see the atom. Has that already been covered? Is that difficult for beginners?

TA: How about pass-by-reference? You're talking about it later in the chapter, but would a forward reference help? </span>

<pre>
def another_atom(seen, atom):
    for i in range(len(seen)):
        if seen[i] == atom:
            return # atom is already present, so do not re-add
    seen.append(atom)
</pre>

      <p>
        <code>another_atom</code>'s arguments are
        a list of the unique atoms we've already seen,
        and the symbol of the atom we're adding.
        Inside the function,
        we loop over the atoms that are already in the list.
        If we find the one we're trying to add,
        we exit the function immediately:
        we aren't supposed to have duplicates in our list,
        so there's nothing to add.
        If we reach the end of the list without finding this symbol,
        though,
        we append it.
        This is a common <a href="glossary.html#design-pattern">design pattern</a>:
        either we find pre-existing data in a loop and return right away,
        or take some default action if we finish the loop without finding a match.
      </p>

      <p>
        Let's watch this function in action.
        We start with an empty list.
        If the first atomic symbol is <code>'Na'</code>,
        we find no match (since the list is empty),
        so we add it.
        The next symbol is <code>'Fe'</code>;
        it doesn't match <code>'Na'</code>,
        so we add it as well.
        Our third symbol is <code>'Na'</code> again.
        It matches the first entry in the list,
        so we exit the function immediately.
      </p>

<span class="comment"> TA: would it help if the invocation was shown? It's not immediately obvious what the columns of the table mean. </span>

      <table>
        <tr>
          <td> <em>start</em> </td>
          <td> <code>[]</code> </td>
        </tr>
        <tr>
          <td> <code>'Na</code> </td>
          <td> <code>['Na']</code> </td>
        </tr>
        <tr>
          <td> <code>'Fe'</code> </td>
          <td> <code>['Na', 'Fe']</code> </td>
        </tr>
        <tr>
          <td> <code>'Na'</code> </td>
          <td> <code>['Na', 'Fe']</code> </td>
        </tr>
      </table>

      <p>
        This code works,
        but it is inefficient.
        Suppose there are <em>V</em> distinct atomic symbols in our data,
        and <em>N</em> symbols in total.
        Each time we add an observation to our list,
        we have to look through an average of <em>V/2</em> entries.
        The total running time for our program is therefore approximately <em>NV/2</em>.
        If <em>V</em> is small,
        this is only a few times larger than <em>N</em>,
        but what happens if we're keeping track of something like patient records rather than atoms?
        In that case,
        most values are distinct,
        so <em>V</em> is approximately the same as <em>N</em>,
        which means that our running time is proportional to <em>N<sup>2</sup>/2</em>.
        That's bad news:
        if we double the size of our data set,
        our program runs four times slower,
        and if we double it again,
        our program will have slowed down by a factor of 16.
      </p>

<span class="comment"> TA: Can you better evoke the "math class" analogy if you show a latex-rendered set here? </span>

      <p>
        There's a better way to solve this problem
        that is simpler to use and runs much faster.
        The trick is to use a <a href="glossary.html#set">set</a>
        to store the symbols.
        A set is an unordered collection of distinct items.
        The word "collection" means that a set can hold zero or more values.
        The word "distinct" means that any particular value is either in the set or not:
        a set can't store two or more copies of the same thing.
        And finally, "unordered" means that values are simply "in" the set.
        They're not in any particular order,
        and there's no first value or last value.
        (They actually are stored in some order,
        but as we'll discuss in <a href="#s:storage">the next section</a>,
        that order is as random as the computer can make it.)
      </p>

      <p>
        To create a set,
        we simply write down its elements inside curly braces
        as we would in a math class:
      </p>

<span class="comment"> TA: Is this more or less confusing than set([3, 5, 7])? Or is the point of this to show the inconsistency with empty sets? </span>

<pre>
&gt;&gt;&gt; primes = {3, 5, 7}
</pre>
      <figure id="f:simple_set">
        <img src="img/setdict/simple_set.png" alt="A Simple Set" />
      </figure>

      <p class="continue">
        However,
        we have to use <code>set()</code> to create an empty set,
        because the symbol <code>{}</code> was already being used for something else
        when sets were added to Python:
      </p>

<pre>
&gt;&gt;&gt; even_primes = set() <span class="comment"># not '{}' as in math</span>
</pre>

      <p class="continue">
        We'll meet that "something else" <a href="#s:dict">later in this chapter</a>.
      </p>

      <p>
        To see what we can do with sets,
        let's create three holding the integers 0 through 9,
        the first half of that same range of numbers (0 through 4),
        and the odd values 1, 3, 5, 7, and 9:
      </p>

<pre>
&gt;&gt;&gt; ten  = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
&gt;&gt;&gt; lows = {0, 1, 2, 3, 4}
&gt;&gt;&gt; odds = {1, 3, 5, 7, 9}
</pre>

      <p>
        If we ask Python to display one of our sets,
        it shows us this:
      </p>

<pre>
&gt;&gt;&gt; print lows
<span class="out">set([0, 1, 2, 3, 4])</span>
</pre>

      <p class="continue">
        rather than using the curly-bracket notation.
        I personally regard this as a design flaw,
        but it does remind us that we can create always create a set from a list.
      </p>

      <p>
        Sets have methods just like strings and lists,
        and,
        like the methods of strings and lists,
        most of those methods create new sets
        instead of modifying the set they are called for.
        These three come straight from mathematics:
      </p>

<pre>
&gt;&gt;&gt; print lows.union(odds)
<span class="out">set([0, 1, 2, 3, 4, 5, 7, 9])</span>
&gt;&gt;&gt; print lows.intersection(odds)
<span class="out">set([1, 3])</span>
&gt;&gt;&gt; print lows.difference(odds)
<span class="out">set([0, 2, 4])</span>
</pre>

      <p>
        Another method that creates a new set is <code>symmetric_difference</code>,
        which is sometimes called "exclusive or":
      </p>

<pre>
&gt;&gt;&gt; print lows.symmetric_difference(odds)
<span class="out">set([0, 2, 4, 5, 7, 9])</span>
</pre>

      <p class="continue">
        It returns the values that are in one set or another, but not in both.
      </p>

      <p>
        Not all set methods return new sets.
        For example,
        <code>issubset</code> returns <code>True</code> or <code>False</code>
        depending on whether all the elements in one set are present in another:
      </p>

<pre>
&gt;&gt;&gt; print lows.issubset(ten)
<span class="out">True</span>
</pre>

      <p class="continue">
        A complementary method called <code>issuperset</code> also exists,
        and does the obvious thing:
      </p>

<pre>
&gt;&gt;&gt; print lows.issuperset(odds)
<span class="out">False</span>
</pre>

      <p>
        We can count how many values are in a set using <code>len</code>
        (just as we would to find the length of a list or string),
        and check whether a particular value is in the set or not using <code>in</code>:
      </p>

<pre>
&gt;&gt;&gt; print len(odds)
<span class="out">7</span>
&gt;&gt;&gt; print 6 in odds
<span class="out">False</span>
</pre>

      <p class="continue">
        Finally,
        some methods modify the sets they are called for.
        The most commonly used is <code>add</code>,
        which adds an element to the set:
      </p>

<span class="comment"> TA: Maybe compare .add() to .append() ? </span>

<pre>
&gt;&gt;&gt; lows.add(9)
&gt;&gt;&gt; print lows
<span class="out">set([0, 1, 2, 3, 4, 9])</span>
</pre>

      <p class="continue">
        If the thing being added is already in the set,
        <code>add</code> has no effect,
        because any specific thing can appear in a set at most once:
      </p>

<pre>
&gt;&gt;&gt; lows.add(9)
&gt;&gt;&gt; print lows
<span class="out">set([0, 1, 2, 3, 4, 9])</span>
</pre>

      <p>
        We can also clear the set:
      </p>

<pre>
&gt;&gt;&gt; lows.clear()
&gt;&gt;&gt; print lows
<span class="out">set()</span>
</pre>

      <p class="continue">
        or remove individual elements:
      </p>

<pre>
&gt;&gt;&gt; lows.remove(0)
&gt;&gt;&gt; print lows
<span class="out">set([1, 2, 3, 4])</span>
</pre>

      <p>
        Removing elements is similar to deleting things from a list,
        but there's an important difference.
        When we delete something from a list,
        we specify its <em>location</em>.
        When we delete something from a set,
        though,
        we must specify the <em>value</em> that we want to take out,
        because sets are not ordered.
        If that value isn't in the set,
        <code>remove</code> does nothing.
      </p>

      <p>
        To help make programs easier to type and read,
        most of the methods we've just seen can be written using arithmetic operators as well.
        For example, instead of <code>lows.issubset(ten)</code>,
        we can write <code>lows &lt;= ten</code>,
        just as if we were using pen and paper.
        There are even a couple of operators,
        like the strict subset test <code>&lt;</code>,
        that don't have long-winded equivalents.
      </p>

      <table>
        <tr>
          <td> <em>difference</em> </td>
          <td> <code>lows.difference(odds)</code> </td>
          <td> <code>lows - odds</code> </td>
        </tr>
        <tr>
          <td> <em>intersection</em> </td>
          <td> <code>lows.intersection(odds)</code> </td>
          <td> <code>lows &amp; odds</code> </td>
        </tr>
        <tr>
          <td> <em>subset</em> </td>
          <td> <code>lows.issubset(ten)</code> </td>
          <td> <code>lows &lt;= ten</code> </td>
        </tr>
        <tr>
          <td> <em>strict subset</em> </td> <td> </td>
          <td> <code>lows &lt; ten</code> </td>
        </tr>
        <tr>
          <td> <em>superset</em> </td>
          <td> <code>lows.issuperset(ten)</code> </td>
          <td> <code>lows &gt;= odds</code> </td>
        </tr>
        <tr>
          <td> <em>strict superset</em> </td> <td> </td>
          <td> <code>lows &gt;= odds</code> </td>
        </tr>
        <tr>
          <td> <em>exclusive or</em> </td>
          <td> <code>lows.symmetric_difference(odds)</code> </td>
          <td> <code>lows ^ odds</code> </td>
        </tr>
        <tr>
          <td> <em>union</em> </td>
          <td> <code>lows.union(odds)</code> </td>
          <td> <code>lows | odds</code> </td>
        </tr>
      </table>

      <div class="box">

        <h3>Negation</h3>

        <p>
          One operator that <em>isn't</em> in this list is "not".
          Mathematicians are quite comfortable negating sets:
          for example, the negation of the set {1, 2} is all numbers that aren't 1 or 2.
          This is a lot harder to do in a program, though.
          To continue with our example,
          we'd expect the integer 3 to be in the negation of the set <code>{1, 2}</code>,
          but is 107.7382?
          Or the string "pterodactyl"?
        </p>

      </div>

      <p>
        The fact that the values in a set are distinct makes them
        a convenient way to get rid of duplicate values,
        like the "unique atoms" problem at the start of this section.
        Suppose we have a file containing the names of all the atoms in our warehouse,
        and our task is to produce a list of the their types.
        Here's how simple that code is:
      </p>

<pre src="src/setdict/unique_atoms.py">
import sys

filename = sys.argv[1]
source = open(filename, 'r')
atoms = set()
for line in source:
    name = line.strip()
    atoms.add(name)
print atoms
</pre>

      <p>
        We start by opening the file
        and creating an empty set which we will fill with atomic symbols.
        As we read the lines in the file,
        we strip off any whitespace (such as the newline character at the end of the line)
        and put the resulting strings in the set.
        When we're done,
        we print the set.
        Here are a couple of simple tests:
      </p>

      <table>
        <tr>
          <td valign="top"><strong>file contents</strong></td>
          <td valign="top"><strong>result</strong></td>
        </tr>
        <tr>
          <td valign="top"><code>
            Fl
          </code></td>
          <td valign="top"><code>
            set(['Fl'])
          </code></td>
        </tr>
        <tr>
          <td colspan="2"><hr/></td>
        </tr>
        <tr>
          <td valign="top">
            Na<br/>Fe<br/>Na
          </td>
          <td valign="top">
            set(['Na', 'Fe'])
          </td>
        </tr>
      </table>

      <p>
        The answers are correct,
        but the display might be a bit confusing:
        what are those extra square brackets for?
        The answer is that
        if we want to construct a set with values using <code>set()</code>,
        we have to pass those values in a single object,
        such as a list.
        This syntax:
      </p>

<pre>
set('Na', 'Fe', 'Fl')
</pre>

      <p class="continue">
        does <em>not</em> work,
        even though it seems more natural.
        On the other hand,
        this means that we can construct a set from almost anything
        that a <code>for</code> loop can iterate over:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">set('lithium')</span>
<span class="out">set(['i', 'h', 'm', 'l', 'u', 't'])</span>
</pre>

      <p>
        But hang on:
        if we're adding characters to the set in the order
        <code>'l'</code>, <code>'i'</code>, <code>'t'</code>, <code>'h'</code>, <code>'i'</code>, <code>'u'</code>, <code>'m'</code>,
        why does Python show them in the order
        <code>'i'</code>, <code>'h'</code>, <code>'m'</code>, <code>'l'</code>, <code>'u'</code>, <code>'t'</code>?
        To answer that question,
        we need to look at how sets are actually stored,
        and why they're stored that way.
      </p>

      <div class="keypoints" id="k:sets">
        <h3>Summary</h3>
        <ul>
          <li idea="tools">Use sets to store distinct unique values.</li>
          <li>Create sets using <code>set()</code> or <code>{<em>v1</em>, <em>v2</em>, ...}</code>.</li>
          <li>Sets are mutable, i.e., they can be updated in place like lists.</li>
          <li>A loop over a set produces each element once, in arbitrary order.</li>
          <li>Use sets to find unique things.</li>
        </ul>
      </div>

    </section>

    <section id="s:storage">

      <h2>Storage</h2>

      <div class="understand" id="u:storage">
        <h3>Understand:</h3>
        <ul>
          <li>How a hash table stores data.</li>
          <li>The problems that can arise if mutable values are stored in a hash table.</li>
          <li>How to store multi-part values in a hash table.</li>
        </ul>
      </div>

      <p>
        Let's create a set,
        add the string <code>'lithium'</code> to it
        (as a single item, not character by character),
        and print the result:
      </p>

<pre>
&gt;&gt;&gt; things = set()
&gt;&gt;&gt; things.add('lithium')
&gt;&gt;&gt; print things
<span class="out">set(['lithium'])</span>
</pre>

      <p class="continue">
        As expected, the string is in the set.
        Now let's try adding a list to the same set:
      </p>

<pre>
&gt;&gt;&gt; things.add([1, 2, 3])
<span class="err">TypeError: unhashable type: 'list'</span>
</pre>

      <p class="continue">
        Why doesn't that work?
        And what does that word "unhashable" mean?
      </p>

      <p>
        When we create a set,
        the computer allocates a block of memory to store references to the set's elements.
        When we add something to the set,
        or try to look something up,
        the computer uses a <a href="glossary.html#hash-function">hash function</a> to figure out where to look.
        A hash function is any function that produces a seemingly-random number
        when given some data as input.
        For example,
        one way to hash a string is to add up the numerical values of its characters.
        If the string is "zebra",
        those values are 97 for lower-case 'a',
        98 for lower-case 'b',
        and so on up to 122 for lower-case 'z'.
        When we add them up,
        we will always get the same result.
        We can use that result to figure out
        where to store a reference to our string
        in the memory set aside for our hash table
        (<a href="#f:set_storage">Figure XXX</a>).
      </p>

      <figure id="f:set_storage">
        <img src="img/shell/set_storage.png" alt="Hash Code for a String" />
      </figure>

      <p>
        Now let's take a look at how a list would be stored.
        If the list contains the same five characters,
        it will be stored in memory like this:
      </p>

      <figure id="f:list_of_characters">
        <img src="img/shell/list_of_characters.png" alt="A List of Characters" />
      </figure>

      <p>
        Using addition as our hash function once again,
        we would get a hash value of 532 for the list,
        so we would store it in the set's memory like this:
      </p>

      <figure id="f:hash_list">
        <img src="img/shell/hash_list.png" alt="Hashing a List" />
      </figure>

      <p>
        But what happens if we change the characters in the list
        after we've added it to the set?
        For example,
        suppose that we change the first letter in the list from 'z' to 's'.
        The hash function's value is now 523 instead of 532,
        which means that the modified list belongs in a different place in the set.
        However, the reference to the list is still in the old location:
        the set doesn't know that the list's contents have changed,
        so it hasn't moved its reference to the right location:
      </p>

      <figure id="f:hash_mutate">
        <img src="img/shell/hash_mutate.png" alt="After Mutation" />
      </figure>

      <p>
        This is bad news.
        If we now ask, "Is the list containing 's', 'e', 'b', 'r', and 'a' in the set?"
        the answer will be "no",
        because the reference to the list isn't stored in the location that our hash function tells us to look.
        It's as if someone changed their name from "Tom Riddle" to "Lord Voldemort",
        but we left all the personnel records filed under 'R'.
      </p>

      <p>
        This problem arises with any <a href="glossary.html#mutable">mutable</a> structure&mdash;i.e.,
        any structure whose contents or value can be changed after its creation.
        Integers and strings are safe to hash because their values are fixed,
        but the whole point of lists is that we can grow them,
        shrink them,
        and overwrite their contents.
      </p>

      <p>
        Different languages and libraries handle this problem in different ways.
        One option is to have each list keep track of the sets that it is in,
        and move itself whenever its values change.
        However, this is expensive:
        every time a program touched a list,
        it would have to see if it was in any sets,
        and if it was,
        recalculate its hash code and update all the references to it.
      </p>

      <p>
        A second option is to shrug and say, "It's the programmer's fault."
        This is what most languages do,
        but it's also expensive:
        programmers can spend hours tracking down the bugs that arise
        from data being in the wrong place.
      </p>

      <p>
        Python uses a third option:
        it only allows programmers to put <a href="glossary.html#immutable">immutable</a> values in sets.
        After all,
        if something's value can't change,
        neither can its hash code or its location in a hash table.
      </p>

      <p>
        But if sets can only hold immutable values,
        what do we do with mutable ones?
        In particular,
        how should we store things like (x,y) coordinates,
        which are naturally represented as lists,
        or people's names,
        which are naturally represented as lists of first, middle, and last names?
        Again, there are several options.
      </p>

      <p>
        The first is to concatenate those values somehow.
        For example,
        if we want to store "Charles" and "Darwin",
        we'd create the string "Charles Darwin" and store that.
        This is simple to do,
        but our code will wind up being littered with string joins and string splits,
        which will make it slower to run and harder to read.
        More importantly,
        it's oly safe to do if
        we can find a concatenator that can never come up in our data.
        (If we join "Paul Antoine" and "St. Cyr" using a space,
        there would be three possible ways to split it apart again.)
      </p>

      <p>
        The second option&mdash;the right one&mdash;is to use <a href="glossary.html#tuple">tuples</a> instead of lists.
        A tuple is an immutable list,
        i.e., a sequence of values that cannot be changed after its creation.
        Tuples are created exactly like lists,
        except we use parentheses instead of square brackets:
      </p>

<pre>
&gt;&gt;&gt; full_name = ('Charles', 'Darwin')
</pre>

      <p class="continue">
        They are indexed the same way,
        too,
        and functions like <code>len</code> do exactly what we'd expect:
      </p>

<pre>
&gt;&gt;&gt; print full_name[0]
<span class="out">Charles</span>
&gt;&gt;&gt; len(full_name)
<span class="out">2</span>
</pre>

      <p class="continue">
        What we <em>cannot</em> do is assign a new value to a tuple element,
        i.e., change the tuple after it has been created:
      </p>

<pre>
&gt;&gt;&gt; full_name[0] = 'Erasmus'
<span class="err">TypeError: 'tuple' object does not support item assignment</span>
</pre>

      <p class="continue">
        This means that a tuple's hash code never changes,
        and <em>that</em> means that tuples can be put in sets:
      </p>

<pre>
&gt;&gt;&gt; names = set()
&gt;&gt;&gt; names.add(('Charles', 'Darwin'))
&gt;&gt;&gt; print names
<span class="out">set([('Charles', 'Darwin')])</span>
</pre>

      <div class="keypoints" id="k:storage">
        <span class="comment"> TA: "for abitrary keys" is the first reference to the word "key" so far. Previously used "values". </span>
        <h3>Summary</h3>
        <ul>
          <li idea="algo">Sets are stored in hash tables, which guarantee fast access for arbitrary keys.</li>
          <li>The values in sets must be immutable to prevent hash tables misplacing them.</li>
          <li>Use tuples to store multi-part elements in sets.</li>
        </ul>
      </div>

    </section>

    <section id="s:dict">

      <h2>Dictionaries</h2>

      <div class="understand" id="u:dict">
        <h3>Understand:</h3>
        <ul>
          <li>That a dictionary stores key-value pairs in a hash table.</li>
          <span class="comment"> TA: "looked up by value" Not "by key"? </span>
          <li>That dictionaries allow things to be looked up by value.</li>
          <li>That the keys in a dictionary must be unique.</li>
          <li>That a dictionary's keys must be immutable.</li>
          <li>How to perform common operations on dictionaries.</li>
          <li>Why dictionaries are intrinsically more efficient than lists for some applications.</li>
        </ul>
      </div>

      <p>
        Now that we know how to find out what kinds of atoms are in our inventory,
        we want to find out how many of each we have.
        Our input is a list of several thousand atomic symbols,
        and the output we want is a list of names and counts.
      </p>

      <p>
        The right way to solve this problem is
        to use a <a href="glossary.html#dictionary">dictionary</a> to store our data.
        A dictionary is a unordered collection of key-value pairs
        (<a href="#f:simple_dict">Fixture XXX</a>).
        Like the elements in a set,
        keys are immutable, unique, and not stored in any particular order.
        There are no restrictions on the values stored with those keys:
        in particular, they don't have to be immutable or unique.
      </p>

      <figure id="f:simple_dict">
        <img src="img/setdict/simple_dict.png" alt="A Simple Dictionary" />
      </figure>

      <p>
        We can create a new dictionary by putting key-value pairs inside curly braces,
        using a colon to connect each pair.
        For example,
        let's create a dictionary with two entries and assign it to the variable <code>birthdays</code>:
      </p>

<pre>
&gt;&gt;&gt; birthdays = {'Newton' : 1642, 'Darwin' : 1809}
</pre>

      <p class="continue">
        The dictionary's keys are the strings <code>'Newton'</code> and <code>'Darwin'</code>.
        The value associated with <code>'Newton'</code> is 1642,
        while the value associated with <code>'Darwin'</code> is 1809.
        We can get the value associated with a key by putting the key in square brackets:
      </p>

<pre>
&gt;&gt;&gt; print birthdays['Newton']
<span class="out">1642</span>
</pre>

      <p class="continue">
        This looks just like subscripting a string or list,
        except dictionary keys don't have to be integers&mdash;they can be strings,
        tuples, and so on.
        It's just like using a phonebook or a real dictionary:
        instead of looking things up by location using an integer index,
        we look things up by name.
      </p>

      <p>
        If we want to add another key-value pair to a dictionary,
        all we have to do is assign a value to the key:
      </p>

<pre>
&gt;&gt;&gt; birthdays['Turing'] = 1612
&gt;&gt;&gt; print birthdays
<span class="out">{'Turing' : 1612, 'Newton' : 1642, 'Darwin' : 1809}</span>
</pre>

      <p>
        If the key is already in the dictionary,
        assignment replaces the value associated with it
        rather than adding another entry
        (since each key can appear at most once).
        Let's fix Turing's birthday by replacing 1612 with 1912:
      </p>

<pre>
&gt;&gt;&gt; birthdays['Turing'] = 1912
&gt;&gt;&gt; print birthdays
<span class="out">{'Turing' : 1912, 'Newton' : 1642, 'Darwin' : 1809}</span>
</pre>

      <p>
        Trying to get the value associated with a key that <em>isn't</em> in the dictionary is an error,
        just like trying to get the fifth element of a three-element list.
        For example, let's try to find Florence Nightingale's birthday:
      </p>

<pre>
&gt;&gt;&gt; print birthdays['Nightingale']
<span class="err">KeyError: 'Nightingale'</span>
</pre>

      <p>
        If we're not sure whether a key is in a dictionary or not,
        we can test for it using <code>in</code>:
      </p>

<pre>
&gt;&gt;&gt; print 'Nightingale' in birthdays
<span class="out">False</span>
&gt;&gt;&gt; print 'Darwin' in birthdays
<span class="out">True</span>
</pre>

      <p>
        Finally, we can see how many entries are in the dictionary using <code>len</code>:
      </p>

<pre>
&gt;&gt;&gt; print len(birthdays)
<span class="out">3</span>
</pre>

      <p class="continue">
        and loop over the keys in a dictionary using <code>for</code>:
      </p>

<pre>
&gt;&gt;&gt; for name in birthdays:
...     print name, birthdays[name]
...
<span class="out">Turing 1912
Newton 1642
Darwin 1809</span>
</pre>

      <p class="continue">
        This is a little bit different from looping over a list.
        When we loop over a list,
        the loop gives us the values,
        since the "keys" 0, 1, 2, and so on usually aren't particularly informative.
        When we loop over a dictionary, on the other hand,
        the loop gives us the keys, which we can use to look up the values.
      </p>

      <p>
        Now, let's go back and count those atoms.
        The main body of our program looks like this:
      </p>

<pre src="src/setdict/count_atoms.py">
import sys

if __name__ == '__main__':
    reader = open(sys.argv[1], 'r')
    lines = reader.readlines()
    reader.close()
    count = count_atoms(lines)
    for atom in count:
        print atom, count[atom]
</pre>

      <p class="continue">
        The first three lines read the input file into a list of strings.
        We then call a function <code>count_atoms</code> to turn that list into
        a dictionary of atomic symbols and counts.
        Once we have that dictionary,
        we use a loop like the one we just saw to print out its contents.
      </p>

      <p>
        Here's the function that does the counting:
      </p>

<pre src="src/setdict/count_atoms.py">
def count_atoms(lines):
  '''Count unique lines of text, returning dictionary.'''

    result = {}
    for atom in lines:
        atom = atom.strip()
        if atom not in result:
            result[atom] = 1
        else:
            result[atom] = result[atom] + 1

    return result
</pre>

      <p>
        We start with a docstring to explain the function's purpose to whoever has to read it next.
        We then create an empty dictionary to fill with data,
        and use a loop to process the lines from the input file one by one.
      </p>

      <p>
        After stripping whitespace off the atom's symbol,
        we check to see if we've seen it before.
        If we haven't,
        we set its count to 1,
        because we've now seen that atom one time.
        If we <em>have</em> seen it before,
        we add one to the previous count
        and store that new value back in the dictionary.
        Finally, when the loop is done, we return the dictionary we've created.
      </p>

      <p>
        Let's watch this function in action.
        Before we read any data, our dictionary is empty.
        After we see <code>'Na'</code> for the first time,
        our dictionary has one entry:
        its key is <code>'Na'</code>, and its value is 1.
        When we see <code>'Fe'</code>,
        we add another entry to the dictionary
        with that string as a key and 1 as a value.
        Finally, when we see <code>'Na'</code> for the second time,
        we add one to its count.
      </p>

      <table>
        <tr>
          <td> <em>start</em> </td>
          <td> <code>{}</code> </td>
        </tr>
        <tr>
          <td> <code>Na</code> </td>
          <td> <code>{'Na' : 1}</code> </td>
        </tr>
        <tr>
          <td> <code>Fe</code> </td>
          <td> <code>{'Na' : 1, 'Fe' : 1}</code> </td>
        </tr>
        <tr>
          <td> <code>Na</code> </td>
          <td> <code>{'Na' : 2, 'Fe' : 1}</code> </td>
        </tr>
      </table>

      <p>
        We could achieve the same thing using a list of lists,
        where each sub-list is a <code>[symbol, count]</code> pair.
        But just like sets,
        dictionaries are stored using hash tables,
        which guarantee that finding or modifying values takes roughly constant time.
        This is a lot better than the list-based method,
        where the time grows in proportion to the number of pairs in the list.
      </p>

      <p>
        Suppose,
        for example,
        that we have 100,000 atoms in our inventory
        of 50 different kinds.
        If the file is randomly ordered,
        we will soon have seen every symbol at least once.
        After that,
        every new observation will involve scanning approximately half of the list.
        The total number of lookups required to build the list will therefore be
        100,000&nbsp;&times;&nbsp;50/2,
        or 2.5 million.
      </p>

      <p>
        If we use a dictionary,
        on the other hand,
        each lookup will take about three times as long as looking at a single element of a list
        (because we have to calculate a hash code).
        However,
        we never have to search the dictionary:
        once we have the hash code,
        we can find the corresponding entry in a single step.
        The total number of steps required to build the dictionary
        will therefore be roughly 3&nbsp;&times;&nbsp;100,000,
        or 300,000.
        That is more than eight times faster than the list-based implementation.
      </p>

      <p>
        But now suppose that we have N patient records,
        and that each patient is only seen once or twice.
        <span class="comment"> TA: You mean list-of-pairs? </span>
        Using a pair-of-pairs approach,
        it will take roughly N<sup>2</sup> steps to build our data structure,
        but if we use a dictionary,
        it will only takes 3 steps.
        If N is a million, that's quite a savings.
      </p>

      <p>
        Just as we use tuples for multi-part entries in sets,
        we can use them for multi-part keys in dictionaries.
        For example,
        if we want to store the years in which scientists were born
        using their full names,
        we could do this:
      </p>

<pre>
birthdays = {
    ('Isaac', 'Newton') : 1642,
    ('Charles', 'Robert', 'Darwin') : 1809,
    ('Alan', 'Mathison', 'Turing') : 1912
}
</pre>

      <p class="continue">
        If we do this,
        though,
        we have to look things up by the full key:
        there is no way to ask for
        all the entries whose keys contain the word <code>'Darwin'</code>.
        On the other hand,
        we <em>can</em> get all of the keys in a list:
      </p>

<pre>
all_keys = birthdays.keys()
print all_keys
<span class="out">[('Isaac', 'Newton'), ('Alan', 'Mathison', 'Turing'), ('Charles', 'Robert', 'Darwin')]</span>
</pre>

      <p>
        The <code>keys</code> method should be used sparingly,
        since it actually creates a new list in memory
        (the dictionary doesn't store the keys as a list internally).
        In particular,
        we <em>shouldn't</em> loop over a dictionary's entries like this:
      </p>

<pre>
for key in some_dict.keys():
    ...do something with key and some_dict[key]
</pre>

      <p class="continue">
        since "<code>for key in some_dict</code>" is shorter and much more efficient.
      </p>

      <div class="keypoints" id="k:dict">
        <h3>Summary</h3>
        <ul>
          <li idea="tools">Use dictionaries to store key-value pairs with distinct keys.</li>
          <li>Create dictionaries using <code>{<em>k1</em>:<em>v1</em>, <em>k2</em>:<em>v2</em>, ...}</code></li>
          <li>Dictionaries are mutable, i.e., they can be updated in place.</li>
          <li>Dictionary keys must be immutable, but values can be anything.</li>
          <li>Use tuples to store multi-part keys in dictionaries.</li>
          <li><code><em>dict</em>[<em>key</em>]</code> refers to the dictionary entry with a particular key.</li>
          <li><code><em>key</em> in <em>dict</em></code> tests whether a key is in a dictionary.</li>
          <li><code>len(<em>dict</em>)</code> returns the number of entries in a dictionary.</li>
          <li>A loop over a dictionary produces each key once, in arbitrary order.</li>
          <li><code><em>dict</em>.keys()</code> creates a list of the keys in a dictionary.</li>
          <li><code><em>dict</em>.values()</code> creates a list of the keys in a dictionary.</li>
        </ul>
      </div>

    </section>

    <section id="s:examples">

      <h2>Simple Examples</h2>

      <div class="understand" id="u:examples">
        <h3>Understand:</h3>
        <ul>
          <li>How to aggregate values using dictionaries.</li>
          <li>Why actual data values should be used to initialize variables.</li>
        </ul>
      </div>

      <p>
        To see how useful dictionaries can be,
        let's switch tracks and do some birdwatching.
        We'll start with the question, "How early in the day did we see each kind of bird?"
        Our data consists of the date and time of the observation, the bird's name, and an optional comment:
      </p>

<pre>
2010-07-03    05:38    loon
2010-07-03    06:02    goose
2010-07-03    06:07    loon
2010-07-04    05:09    ostrich   # hallucinating?
2010-07-04    05:29    loon
     &hellip;           &hellip;        &hellip;
</pre>

      <p>
        We want the minimum of all the times associated with each bird name,
        so we'll use a dictionary with the bird name as the key and the earliest observation time as the value.
      </p>

      <p>
        First, let's read our data file and create a list of tuples,
        each of stores has a date, time, and bird name as strings:
      </p>

<pre src="src/setdict/early_bird.py">
def read_observations(filename):
    '''Read data, return [(date, time, bird)...].'''

    reader = open(filename, 'r')
    result = []

    for line in reader:
        fields = line.split('#')[0].strip().split()
        assert len(fields) == 3, 'Bad line "%s"' % line
        result.append(fields)

    return result
</pre>

      <p class="continue">
        This function follows the pattern we've seen many times before.
        We set up by opening the input file and creating an empty list that we'll append records to.
        We then process each line of the file in turn.
        Splitting the line on the <code>'#'</code> character and taking the first part of the result
        gets rid of any comment that might be present;
        stripping off whitespace and then splitting breaks the remainder into fields.
        To prevent trouble later on, we check that there actually are three fields before going on.
        (An industrial-strength version of this function would also check that the date and time were properly formatted,
        but we'll skip that for now.)
        Once we've done our check, we append the triple containing the date, time, and bird name to the list we're going to return.
      </p>

      <p>
        Here's the function that turns that list of tuples into a dictionary:
      </p>

<pre src="src/setdict/early_bird.py">
def earliest_observation(data):
    '''How early did we see each bird?'''

    result = {}
    for (date, time, bird) in data:
        if bird not in result:
            result[bird] = time
        else:
            result[bird] = min(result[bird], time)

    return result
</pre>

      <p class="continue">
        Once again,
        the pattern should by now be familiar.
        We start by creating an empty dictionary.
        Our loop handles one tuple at a time,
        splitting that tuple into its component parts for use in the loop body.
        If this bird's name is not already a key in our dictionary,
        this must be its first appearance,
        so the time it was seen becomes the earliest observation time.
        Otherwise,
        if there is already an entry for this bird in the dictionary,
        we keep the minimum of the stored time and the new time
        (instead of adding 1 to the count of observations
        as we did in the previous example).
      </p>

      <p>
        Now, what if we want to find out which birds were seen on each day that we were observing?
        This is similar to the problem we just solved, so our solution will have a similar structure.
        However, since we probably saw more than one kind of bird each day,
        the values in our dictionary need to be some sort of collection.
        And since we're only interested in which birds we saw, we can use a set.
        Here's our function:
      </p>

<pre src="src/setdict/birds_by_date.py">
def birds_by_date(data):
    '''Which birds were seen on each day?'''

    result = {}
    for (date, time, bird) in data:
        if date not in result:
            result[date] = {bird}
        else:
            result[date].add(bird)

    return result
</pre>

      <p class="continue">
        Again, we start by creating an empty dictionary,
        and process each record in turn, unpacking it automatically in the loop header.
        Since we're recording birds by date,
        the keys in our dictionary are dates rather than bird names.
        If the current date isn't already a key in the dictionary,
        we create a set containing only this bird,
        and store it in the dictionary with the date as the key.
        Otherwise,
        we add this bird to the set associated with the date.
        We don't need to check whether the bird is already in that set,
        since the set will automatically eliminate any duplication.
      </p>

      <p>
        Let's watch this function in action.
        We start with an empty set,
        as shown in <a href="#f:bird_date">Figure XXX</a>.
        After reading the first observation,
        we add an entry to our dictionary with the string <code>'2010-07-03'</code> as its key
        and an empty set as its value.
        We then immediately add the name <code>'loon'</code> to that set.
      </p>

      <figure id="f:bird_date">
        <img src="img/setdict/bird_date.png" alt="Birds by Date" />
      </figure>

      <p>
        Our next observation is a goose on the same day,
        so we put <code>'goose'</code> in the set we just created.
        Our third observation is another loon.
        Since adding a value to a set that's already present has no effect,
        our data structure doesn't change.
        Next, though, we have the first observation for July 4th.
        Since it's the first time we've seen this date,
        our function adds a new entry to the main dictionary with <code>'2010-07-04'</code> as the key
        and a set as the value,
        then adds <code>'ostrich'</code> to that set.
        Finally,
        we have another damn loon,
        which goes into the second of our sets,
        and we're done.
      </p>

      <p>
        For our last example, we'll find which bird we saw least frequently.
        Actually, we'll find which <em>birds</em>,
        since two or more may be tied for the low score&mdash;forgetting that values may not be unique
        is a common mistake in data crunching,
        and often a hard one to track down.
      </p>

      <p>
        One way to solve this problem is to do two passes over our data.
        We'll assume that we already have a dictionary of bird names and total observation counts.
        To find the minimum value,
        we loop over all entries in the dictionary:
      </p>

<pre>
for bird in counts:
    if counts[bird] &lt; least:
        least = counts[bird]
</pre>

      <p class="continue">
        We then use another loop to build the set of bird names that share that minimum value:
      </p>

<pre>
result = set()
for bird in counts:
    if counts[bird] == least:
        result.add(bird)
</pre>

      <p>
        There's a flaw in this code, though:
        we have not initialized <code>least</code>.
        It's not safe to set it to a "large" value, like 1000,
        because while it's unlikely that we'll have seen every type of bird at least 1000 times,
        it's not impossible.
      </p>

      <p>
        Another choice that <em>will</em> work is to initialize it to
        the largest integer the computer can represent,
        which Python stores in <code>sys.maxint</code>.
        While it's still possible that we'll have seen everything more often than this
        (imagine, for example, that we were counting atoms instead of counting birds),
        there's no way we could get those observations into our program.
      </p>

      <p>
        The right choice, though, is to initialize <code>least</code> from the data itself.
        We'll start by setting it to the special value <code>None</code>,
        and then check for this value inside our loop.
        If <code>least</code> is <code>None</code>,
        it means we haven't processed any data yet,
        so we'll assign whatever value we're looking at to <code>least</code>.
        After that,
        all the less-than comparisons will do the right thing.
        The resulting code looks like this:
      </p>

<pre>
least = None
for bird in counts:
    if least is None:
        least = counts[bird]
    elif counts[bird] &lt; least:
        least = counts[bird]
</pre>

      <p class="continue">
        This is another common design pattern:
        if we don't know what range of values our data might take on,
        we initialize variables with a "don't know" marker (such as <code>None</code>),
        then replace those markers with actual values as quickly as possible.
      </p>

      <p>
        Now let's combine the two passes into one.
        We start by creating both <code>least</code> and <code>result</code>,
        then loop over our dictionary of counts:
      </p>

<pre>
least = None
result = set()
for bird in counts:
    num = counts[bird]
    &hellip;    &hellip;    &hellip;
</pre>

      <p class="continue">
        In our loop, we have four cases to consider:
      </p>

      <table>
        <tr>
          <td valign="top">
            <code>least</code> is <code>None</code>
          </td>
          <td valign="top">
            This is the first record we have processed,
            so we need to re-set <code>least</code> and <code>result</code>.
          </td>
        </tr>
        <tr>
          <td valign="top">
            <code>num &lt; least</code>
          </td>
          <td valign="top">
            We have found a new minimum,
            so we need to re-set <code>least</code> and <code>result</code>.
          </td>
        </tr>
        <tr>
          <td valign="top">
            <code>num == least</code>
          </td>
          <td valign="top">
            We have seen this bird the current least number of times,
            so we need to add it to <code>result</code>.
          </td>
        </tr>
        <tr>
          <td valign="top">
            <code>num &gt; least</code>
          </td>
          <td valign="top">
            We have seen this bird more than the least number of times,
            so we can ignore it.
          </td>
        </tr>
      </table>

      <p>
        Here's what that decision table looks like in code:
      </p>

<pre>
least = None
result = set()
for bird in counts:
    num = counts[bird]
    if least is None:
        least = num
        result = {bird}
    elif num &lt; least:
        least = num
        result = {bird}
    elif num == least:
        result.add(bird)
    else:
        # do nothing
</pre>

      <p class="continue">
        We can simplify this a bit by combining the first two cases
        (since they do the same thing)
        and getting rid of the last one
        (since it does nothing):
      </p>

<pre>
least = None
result = set()
for bird in counts:
    num = counts[bird]
    if (least is None) or (num &lt; least):
        least = num
        result = {bird}
    elif num == least:
        result.add(bird)
</pre>

      <p class="continue">
        Remember, <code>or</code> only evaluates its right side if it has to,
        so if <code>least</code> is <code>None</code>,
        this code won't get an error by comparing <code>num</code> to <code>None</code>.
      </p>

      <p>
        Let's watch this function run with an input dictionary containing three entries.
        We initialize <code>number</code> to 0 and <code>result</code> to an empty set
        (<a href="#f:min_bird">Figure XXX</a>).
        Processing the first entry in the dictionary takes us into our three cases:
        <code>num</code> is assigned 3, and <code>'loon'</code> is put in our set of birds.
        The second entry has a new minimum count,
        so we replace both the value of <code>num</code> and our set.
        Finally,
        the third bird's count is the same as the current minimum,
        so we just add it to the set,
        and we're done.
      </p>

      <figure id="f:min_bird">
        <img src="img/setdict/min_bird.png" alt="Least Seen Bird" />
      </figure>

      <div class="keypoints" id="k:examples">
        <h3>Summary</h3>
        <ul>
          <li>Use dictionaries to count things.</li>
          <li idea="paranoia">Initialize values from actual data instead of trying to guess what values could "never" occur.</li>
        </ul>
      </div>

    </section>

    <section id="s:nanotech">

      <h2>Nanotech Inventory</h2>

      <div class="understand" id="u:nanotech">
        <h3>Understand:</h3>
        <ul>
          <li>That dictionaries can be nested like lists.</li>
        </ul>
      </div>

      <p>
        We can now build a solution to Fan's original nanotech inventory problem.
        Our goal is to find out how many molecules of various kinds we can make using the atoms in our warehouse.
        The number of molecules of any particular type we can make
        is limited by the scarcest atom that molecule requires.
        For example,
        if we have five nitrogen atoms and ten hydrogen atoms,
        we can only make three ammonia molecules,
        because we need three hydrogen atoms for each.
      </p>

      <p>
        The formulas for the molecules we know how to make
        are stored in a file like this:
      </p>

<pre>
# Molecular formula file

helium : He 1
water : H 2 O 1
hydrogen : H 2
</pre>

      <p class="continue">
        and our inventory is stored in a file like this:
      </p>

<pre>
# Atom inventory file

He 1
H 4
O 3
</pre>

      <p>
        Let's start with our inventory.
        Our input consists of pairs of strings and numbers,
        which by now should suggest using a dictionary for storage.
        The keys will be atomic symbols,
        and the values will be the number of atoms of that kind we currently have in stock
        (<a href="#f:nanotech_inventory">Figure XXX</a>).
        If an atom isn't listed in our inventory,
        we'll assume that we don't have any in stock.
      </p>

      <figure id="f:nanotech_inventory">
        <img src="img/setdict/nanotech_inventory.png" alt="Nanotech Inventory" />
      </figure>

      <p>
        What about the formulas for all the molecules we know how to make?
        Again, the right answer is a dictionary:
        its keys will be the name of molecules,
        and each value will be a dictionary storing
        atomic symbols and the number of atoms of that type in the molecule&mdash;the same structure,
        in fact,
        that we're using for our inventory.
        <a href="#f:nanotech_formulas">Figure XXX</a> shows
        an outer dictionary that maps the word <code>'water'</code>
        to a dictionary storing the number of oxygen and hydrogen atoms in a single water molecule,
        and the word <code>'ammonia'</code> to a dictionary storing
        the number of nitrogen and hydrogen atoms in a single ammonia molecule.
      </p>

      <figure id="f:nanotech_formulas">
        <img src="img/setdict/nanotech_formulas.png" alt="Storing Formulas" />
      </figure>

      <p>
        Finally,
        we'll store the results of our calculation in yet another dictionary,
        this one mapping the names of molecules to how many molecules of that kind we can make
        (<a href="#f:nanotech_results">Figure XXX</a>):
      </p>

      <figure id="f:nanotech_results">
        <img src="img/setdict/nanotech_results.png" alt="Nanotech Results" />
      </figure>

      <p>
        The main body of the program is straightforward:
        it just reads in the input files, does our calculation, and prints the result.
      </p>

<pre src="src/setdict/nanotech.py">
'''Calculate how many molecules of each type can be made with the atoms on hand.'''

import sys

if __name__ == '__main__':
    inventory = read_inventory(sys.argv[1])
    formulas = read_formulas(sys.argv[2])
    counts = calculate_counts(inventory, formulas)
    show_counts(counts)
</pre>

      <p>
        Reading the inventory file is simple.
        We take each interesting line in the file,
        split it to get an atomic symbol and a count,
        and store them together in a dictionary:
      </p>

<pre src="src/setdict/nanotech.py">
def read_inventory(filename):
    '''Read inventory of available atoms.'''

    result = {}
    for line in read_lines(filename):
        name, count = line.split(' ')
        result[name] = int(count)

    return result
</pre>

      <p class="continue">
        For clarity's sake, we have used a helper function called <code>read_lines</code>
        to read a file and strip out blank lines and comments:
      </p>

<pre src="src/setdict/nanotech.py">
def read_lines(filename):
    '''Read lines from file, stripping out blank lines and comments.'''

    reader = open(filename, 'r')
    lines = []
    for line in reader:
        line = line.split('#')[0].strip()
        if line:
            lines.append(line)
    reader.close()

    return lines
</pre>

      <p>
        Using that same function,
        the function that reads in a file of molecular formulas is only slightly more complex
        than the one that reads in inventory:
      </p>

<pre src="src/setdict/nanotech.py">
def read_formulas(filename):
    '''Read molecular formulas from file.'''

    result = {}                                        # 1
    for line in read_lines(filename):

        name, atoms = line.split(':')                  # 2
        name = name.strip()

        atoms = atoms.strip().split(' ')               # 3
        formula = {}
        for i in range(0, len(atoms), 2):              # 4
            formula[atoms[i]] = int(atoms[i+1])        # 5

        result[name] = formula                         # 6

    return result                                      # 7
</pre>

      <p class="continue">
        We start by creating the dictionary we're going to store the results in (#1).
        For each line in the file that has some data,
        we split on the colon ':' to separate the molecule's name (which may contain spaces) from its formula (#2).
        We then split the formulas into a list of strings that alternate between atomic symbols and counts (#3).
        In the inner loop (#4),
        we move forward through those values two elements at a time,
        storing the atomic symbol and count in a dictionary (#5).
        Once we're done, we store that dictionary as the value for the molecule name in the main dictionary (#6).
        When we've processed all the lines,
        we return the final result (#7).
      </p>

      <p>
        Now that we have all our data,
        it's time to calculate how many molecules of each kind we can make.
        <code>inventory</code> maps atomic symbols to counts,
        and so does <code>formulas[name]</code>,
        so let's loop over all the molecules in our formulas and "divide" those two dictionaries
        using another helper function:
      </p>

<pre src="src/setdict/nanotech.py">
def calculate_counts(inventory, formulas):
    '''Calculate how many of each molecule can be made with inventory.'''

    counts = {}
    for name in formulas:
        counts[name] = dict_divide(inventory, formulas[name])

    return counts
</pre>

      <p class="continue">
        It might seem like overkill to write yet another function in this case,
        but experience shows that if we have a choice between big functions in which nothing is obviously wrong,
        or little functions in which obviously nothing is wrong,
        we should choose the latter.
        Here's that helper function:
      </p>

<pre src="src/setdict/nanotech.py">
def dict_divide(inventory, molecule):
    '''Calculate how much of a single molecule can be made with inventory.'''

    number = None
    for atom in molecule:
        required = molecule[atom]
        available = inventory.get(atom, 0)
        limit = available / required
        if (number is None) or (limit &lt; number):
            number = limit

    return number
</pre>

      <p class="continue">
        This function loops over all the atoms in the molecule we're trying to build,
        see what limits the available inventory puts on us,
        and return the minimum of all those results.
        This function uses a few patterns that come up frequently in many kinds of programs,
        so let's have a closer look.
      </p>

      <p>
        The first pattern is to initialize the value we're going to return to <code>None</code>,
        then test for that value inside the loop
        to make sure we re-set it to a legal value the first time we have real data.
        In this case, we could just as easily use -1
        or some other impossible value as an "uninitialized" flag for <code>number</code>.
      </p>

      <p>
        Since we're looping over the keys of <code>molecule</code>,
        we know that we can get the value stored in <code>molecule[atom]</code>.
        However, that atom might not be a key in <code>inventory</code>,
        so we use <code>inventory.get(atom, 0)</code> to get either the stored value or a sensible default.
        In this case zero, the sensible default is 0,
        because if the atom's symbol isn't in the dictionary, we don't have any of it.
        This is our second pattern.
      </p>

      <p>
        The third is using calculate, test, and store to find a single value&mdash;in this case, the minimum&mdash;from
        a set of calculated values.
        We could calculate the list of available over required values,
        then find the minimum of the list,
        but doing the minimum test as we go along saves us having to store the list of intermediate values.
        It's probably not a noticeable time saving in this case,
        but it would be with larger data sets.
      </p>

      <p>
        The last step in building our program is to show how many molecules of each kind we can make.
        We could just loop over our result dictionary,
        printing each molecule's name and the number of times we could make it,
        but let's sort the results by molecule name to make things easier to find:
      </p>

<pre src="src/setdict/nanotech.py">
def show_counts(counts):
    '''Show how many of each kind of molecule we can make.'''

    names = counts.keys()
    names.sort()
    for name in names:
        print name, counts[name]
</pre>

      <p>
        It's time to test our code.
        Let's start by using an empty inventory and a single formula:
      </p>

      <table border="1" width="100%">
        <tr>
          <td width="33%">
            Inventory
          </td>
          <td width="33%">
            Formulas
          </td>
          <td width="33%">
            Output
          </td>
        </tr>
        <tr>
          <td valign="top">
<pre>
# inventory-00.txt
</pre>
          </td>
          <td valign="top">
<pre>
# formulas-01.txt
helium : He 1
</pre>
          </td>
          <td valign="top">
<pre>
</pre>
          </td>
        </tr>
      </table>

      <p class="continue">
        There's no output, which is what we expect.
        Let's add one atom of helium to our inventory:
      </p>

      <table border="1" width="100%">
        <tr>
          <td width="33%">
            Inventory
          </td>
          <td width="33%">
            Formulas
          </td>
          <td width="33%">
            Output
          </td>
        </tr>
        <tr>
          <td valign="top">
<pre>
# inventory-01.txt
He 1
</pre>
          </td>
          <td valign="top">
<pre>
# formulas-01.txt
helium : He 1
</pre>
          </td>
          <td valign="top">
<pre>
helium 1
</pre>
          </td>
        </tr>
      </table>

      <p class="continue">
        That seems right as well.
        Let's add some hydrogen, but don't give the program any formulas that use hydrogen:
      </p>

      <table border="1" width="100%">
        <tr>
          <td width="33%">
            Inventory
          </td>
          <td width="33%">
            Formulas
          </td>
          <td width="33%">
            Output
          </td>
        </tr>
        <tr>
          <td valign="top">
<pre>
# inventory-02.txt
He 1
H 4
</pre>
          </td>
          <td valign="top">
<pre>
# formulas-01.txt
helium : He 1
</pre>
          </td>
          <td valign="top">
<pre>
helium 1
</pre>
          </td>
        </tr>
      </table>

      <p class="continue">
        The output doesn't change, which is correct.
        Let's try adding the formula for water,
        which does use hydrogen,
        but not providing any oxygen:
      </p>

      <table border="1" width="100%">
        <tr>
          <td width="33%">
            Inventory
          </td>
          <td width="33%">
            Formulas
          </td>
          <td width="33%">
            Output
          </td>
        </tr>
        <tr>
          <td valign="top">
<pre>
# inventory-02.txt
He 1
H 4
</pre>
          </td>
          <td valign="top">
<pre>
# formulas-02.txt
helium : He 1
water: H 2 O 1
</pre>
          </td>
          <td valign="top">
<pre>
helium 1
</pre>
          </td>
        </tr>
      </table>

      <p class="continue">
        As we hoped, there's no water in the output, but helium is still appearing as it should.
        Let's add the formula for molecular hydrogen:
      </p>

      <table border="1" width="100%">
        <tr>
          <td width="33%">
            Inventory
          </td>
          <td width="33%">
            Formulas
          </td>
          <td width="33%">
            Output
          </td>
        </tr>
        <tr>
          <td valign="top">
<pre>
# inventory-02.txt
He 1
H 4
</pre>
          </td>
          <td valign="top">
<pre>
# formulas-03.txt
helium : He 1
water: H 2 O 1
hydrogen: H 2
</pre>
          </td>
          <td valign="top">
<pre>
helium 1
hydrogen 2
</pre>
          </td>
        </tr>
      </table>

      <p class="continue">
        Sure enough, we can make two molecules of hydrogen
        (each of which uses two atoms).
        Finally,
        let's put some oxygen in the warehouse:
      </p>

      <table border="1" width="100%">
        <tr>
          <td width="33%">
            Inventory
          </td>
          <td width="33%">
            Formulas
          </td>
          <td width="33%">
            Output
          </td>
        </tr>
        <tr>
          <td valign="top">
<pre>
# inventory-03.txt
He 1
H 4
O 3
</pre>
          </td>
          <td valign="top">
<pre>
# formulas-03.txt
helium : He 1
water: H 2 O 1
hydrogen: H 2
</pre>
          </td>
          <td valign="top">
<pre>
helium 1
hydrogen 2
water 2
</pre>
          </td>
        </tr>
      </table>

      <p class="continue">
        That's right too:
        we can make two water molecules
        (because we don't have enough hydrogen to pair with our three oxygen atoms).
        There are quite a few other interesting tests still to run,
        but things are looking good so far.
      </p>

      <p>
        Our code is a <em>lot</em> simpler than it would be
        if we used lists of pairs of atom names and counts to store things.
        It's also a lot more efficient,
        and (while it may not feel that way yet)
        much easier to read.
      </p>

      <div class="keypoints" id="k:nanotech">
        <h3>Summary</h3>
        <ul>
          <li>Nested dicionaries are as useful as nested lists.</li>
          <li>Use names as keys rather than matching them to arbitrary integer indices.</li>
        </ul>
      </div>

    </section>

    <section id="s:phylotree">

      <h2>Phylogenetic Trees</h2>

      <div class="understand" id="u:phylotree">
        <h3>Understand:</h3>
        <ul>
          <li>That many "matrix" problems may be best solved using dictionaries.</li>
          <li>Why the values in multi-part keys should be ordered somehow.</li>
        </ul>
      </div>

      <p>
        As Theodosius Dobzhansky said almost a century ago,
        nothing in biology makes sense except in the light of evolution.
        Since mutations usually occur one at a time,
        the more similarities there are between the DNA of two species,
        the more recently they had a common ancestor.
        We can use this idea to reconstruct the evolutionary tree for a group of organisms
        using a hierarchical clustering algorithm.
      </p>

      <p>
        We don't have to look at the natural world very hard
        to realize that some organisms are more alike than others.
        For example, if we look at the appearance, anatomy, and lifecycles
        of the seven fish shown in <a href="#f:species_pairs">Figure XXX</a>,
        we can see that three pairs are closely related.
        But where does the seventh fit in?
        And how do the pairs relate to each other?
      </p>

      <figure id="f:species_pairs">
        <img src="img/phylotree/species_pairs.png" alt="Pairing Up Species" />
      </figure>

      <p>
        The first step is to find the two species that are most similar,
        and construct their plausible common ancestor.
        We then pair two more, and two more,
        and start joining pairs to individuals,
        or pairs with other pairs.
        Eventually, all the organisms are connected.
        We can redraw those connections as a tree,
        using the heights of branches to show the number of differences between the species we're joining up
        (<a href="#f:species_tree">Figure XXX</a>).
      </p>

      <figure id="f:species_tree">
        <img src="img/phylotree/species_tree.png" alt="Tree of Life" />
      </figure>

      <p>
        Let's turn this into an algorithm:
      </p>

<pre>
U = {all organisms}
while U != {}:
  a, b = two closest entries in U
  p = common parent of {a, b}
  U = U - {a, b}
  U = U + {p}
</pre>

      <p class="continue">
        Initially, our universe U contains all the organisms we're interested in.
        While there are still organisms that haven't been connected to the tree,
        we find the two that are closest,
        calculate their common parent,
        remove the two we just paired up from the set,
        and insert the newly-created parent.
        The set of ungrouped organisms shrinks by one each time,
        so this algorithm eventually terminates.
        And we can keep track of the pairings on the side to reconstruct the tree when we're done.
      </p>

      <p>
        Now, what does "closest" mean?
        One rule is called <em>unweighted pair-group method using arithmetic averages</em>, or UPGMA.
        Let's illustrate it by calculating a phylogenetic tree for humans, vampires, werewolves, and mermaids.
        The distances between each pair of species is shown in the table below
        (we only show the lower triangle because it's symmetric):
      </p>

      <table border="1">
        <tr>
          <td> &nbsp; </td>
          <td> human </td>
          <td> vampire </td>
          <td> werewolf </td>
          <td> mermaid </td>
        </tr>
        <tr>
          <td> human </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> vampire </td>
          <td> 13 </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> werewolf </td>
          <td> 5 </td>
          <td> 6 </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> mermaid </td>
          <td> 12 </td>
          <td> 15 </td>
          <td> 29 </td>
          <td> &nbsp; </td>
        </tr>
      </table>

      <p>
        The closest entries&mdash;i.e., the pair with minimum distance&mdash;are human and werewolf.
        We will replace this with a common ancestor, which we will call HW.
        Its height will be 1/2 the value of the entry,
        and for each other species X,
        we will calculate a new score for HW and X as (HX + WX - HW)/2.
        For example, we will combine HV and VW (in yellow) and HM and MW (in green):
      </p>

      <table border="1">
        <tr>
          <td> &nbsp; </td>
          <td> human </td>
          <td> vampire </td>
          <td> werewolf </td>
          <td> mermaid </td>
        </tr>
        <tr>
          <td> human </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> vampire </td>
          <td bgcolor="yellow"> 13 </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> werewolf </td>
          <td bgcolor="pink"> 5 </td>
          <td bgcolor="yellow"> 6 </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> mermaid </td>
          <td bgcolor="lightgreen"> 12 </td>
          <td> 15 </td>
          <td bgcolor="lightgreen"> 29 </td>
          <td> &nbsp; </td>
        </tr>
      </table>

      <p class="continue">
        Our new matrix looks like this:
      </p>

      <table border="1">
        <tr>
          <td> &nbsp; </td>
          <td> HW </td>
          <td> vampire </td>
          <td> mermaid </td>
        </tr>
        <tr>
          <td> HW </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> vampire </td>
          <td bgcolor="yellow"> 7 </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> mermaid </td>
          <td bgcolor="lightgreen"> 18 </td>
          <td> 15 </td>
          <td> &nbsp; </td>
        </tr>
      </table>

      <figure id="f:phylo_combine_tree_1">
        <img src="img/phylotree/phylo_combine_tree_1.png" alt="Tree During Combining" />
      </figure>

      <p>
        The height of HW is half of the 5 we eliminated, or 2.5
        (<a href="#f:phylo_combine_tree_1">Figure XXX</a>).
        Repeating this step, we combine HW with V:
      </p>

      <table border="1">
        <tr>
          <td> &nbsp; </td>
          <td> HWV </td>
          <td> mermaid </td>
        </tr>
        <tr>
          <td> HWV </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> mermaid </td>
          <td bgcolor="lightblue"> 15 </td>
          <td> &nbsp; </td>
        </tr>
      </table>

      <p class="continue">
        and finally HWV with M.
        Our final tree looks like <a href="#f:phylo_combine_tree_2">Figure XXX</a>,
        with the "missing" heights are implied by the differences between branch values.
      </p>

      <figure id="f:phylo_combine_tree_2">
        <img src="img/phylotree/phylo_combine_tree_2.png" alt="Tree After Combining" />
      </figure>

      <p>
        We illustrated our algorithm with a triangular matrix,
        but the order of the rows and columns is arbitrary.
        It's really just a lookup table mapping pairs of organisms to numbers.
        And as soon as we think of lookup tables,
        we should think of dictionaries.
        The keys are pairs of organisms,
        which we will keep in alphabetical order so that there's no confusion between 'HW' and 'WH'.
        The values are the distances between those organisms,
        so this table:
      </p>

      <table border="1">
        <tr>
          <td> &nbsp; </td>
          <td> human </td>
          <td> vampire </td>
          <td> werewolf </td>
          <td> mermaid </td>
        </tr>
        <tr>
          <td> human </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> vampire </td>
          <td> 13 </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> werewolf </td>
          <td> 5 </td>
          <td> 6 </td>
          <td> &nbsp; </td>
          <td> &nbsp; </td>
        </tr>
        <tr>
          <td> mermaid </td>
          <td> 12 </td>
          <td> 15 </td>
          <td> 29 </td>
          <td> &nbsp; </td>
        </tr>
      </table>

      <p class="continue">
        becomes this dictionary:
      </p>

<pre>
{
    ('human',   'mermaid')  : 12,
    ('human',   'vampire')  : 13,
    ('human',   'werewolf') :  5,
    ('mermaid', 'vampire')  : 15,
    ('mermaid', 'werewolf') : 29,
    ('vampire', 'werewolf') :  6
}
</pre>

      <p>
        Let's write some code.
        To start,
        we'll translate the algorithm we discussed earlier into something that looks like Python:
      </p>

<pre>
while len(scores) &gt; 0:
    min_pair = find_min_pair(species, scores)
    parent, height = create_new_parent(scores, min_pair)
    print parent, height
    old_score = remove_entries(species, scores, min_pair)
    update(species, scores, min_pair, parent, old_score)
</pre>

      <p class="continue">
        The scores are in a dictionary called <code>scores</code>,
        and the names of the species are in a list called <code>species</code>,
        which is sorted alphabetically.
        While we have some scores left to process,
        we find the closest pair,
        create a new parent,
        print it out,
        remove entries that refer to the pair we're combining,
        and add new entries to the scores table.
        (In a complete program,
        we'd save the parent and height somewhere
        so that we could reconstruct the tree afterward.)
      </p>

      <p>
        The next step is to write the functions our algorithm assumes.
        The first is <code>min_pair</code>,
        which finds the closest pair of organisms in the scores table:
      </p>

<pre src="src/setdict/phylogen.py">
def find_min_pair(species, scores):
    '''Find minimum-value pair of species in scores.'''

    min_pair, min_val = None, None
    for pair in combos(species):

        assert pair in scores, 'Pair (%s, %s) not in scores' % pair
        if (min_val is None) or (scores[pair] &lt; min_val):
            min_pair, min_val = pair, scores[pair]

    assert min_val is not None, 'No minimum value found in scores'
    return min_pair
</pre>

      <p class="continue">
        The algorithm is simple,
        but it assumes we have a way to generate all valid combinations of organisms from the species list,
        so we'll need to write that.
        It's also worth noting the <code>assert</code> statements
        that check that the data we're working with is sensible
        and that we actually found a minimum value.
        Remember, good programs fail early and fail often.
      </p>

      <p>
        Now let's write the function that generates pairs of species.
        It uses a double loop to construct a list of pairs:
      </p>

<pre src="src/setdict/phylogen.py">
def combos(species):
    '''Generate all combinations of species.'''

    result = []
    for i in range(len(species)):
        for j in range(i+1, len(species)):
            result.append((species[i], species[j]))

    return result
</pre>

      <p class="continue">
        Notice the starting index on the inner loop:
        if the outer loop is at position <code>i</code>,
        the inner loop starts at <code>i+1</code>,
        which ensures that each possible pair is only generated once.
      </p>

      <p>
        Notice also that every pair will always be alphabetically sorted,
        because the overall list is sorted that way.
        This ensures that any two names will always be paired in the same order,
        which is crucial to the algorithm working correctly.
      </p>

      <p>
        Looking back at the program's main body,
        the next function we need to write is <code>create_new_parent</code>.
        It's pretty simple:
        we just concatenate the names of the two organisms we're combining,
        and give that presumed parental species a score that is
        half the score for the pair we're combining.
        We'll put square brackets around the name to make it more readable,
        and so that we can easily see the order in which things were paired up:
      </p>

<pre src="src/setdict/phylogen.py">
def create_new_parent(scores, pair):
    '''Create record for new parent.'''

    parent = '[%s %s]' % pair
    height = scores[pair] / 2.
    return parent, height
</pre>

      <p>
        Going back at our main program once again,
        we need to remove entries from the scores table that refer to the organisms we're pairing up.
        We also need to take their names out of the list of species.
        That's pretty easy to do:
      </p>

<pre src="src/setdict/phylogen.py">
def remove_entries(species, scores, pair):
    '''Remove species that have been combined.'''

    left, right = pair
    species.remove(left)
    species.remove(right)
    old_score = scores[pair]
    del scores[pair]
    return old_score
</pre>

      <p class="continue">
        Notice that this function returns the old score, which we need in the main program.
        This isn't a great design:
        there's nothing in the name <code>remove_entries</code> to suggest that
        we're saving and returning the old score,
        and it isn't obvious why we're doing this when we're reading this function.
        As an exercise,
        try rewriting the main program so that <code>remove_entries</code> doesn't have to return anything,
        and see if you think it's easier to understand.
      </p>

      <p>
        Our fifth function updates the scores table and species list.
        It's the most complicated of them all.
        For each species that <em>isn't</em> being paired up,
        we have to:
      </p>

      <ol>

        <li>
          calculate the combination of that species with the two halves of the new pair,
          saving the scores for later use;
        </li>

        <li>
          create a pair that includes the newly-constructed parent; and
        </li>

        <li>
          save our work.
        </li>

      </ol>

      <p class="continue">
        When we're done,
        we have to add the newly-created parent to the list of species,
        and then re-sort that list
        (remember, our <code>combos</code> function assumes that
        species' names appear in order).
        The whole thing looks like this:
      </p>

<pre src="src/setdict/phylogen.py">
def update(species, scores, pair, parent, parent_score):
    '''Replace two species from the scores table.'''

    left, right = pair
    for other in species:
        l_score = tidy_up(scores, left, other)
        r_score = tidy_up(scores, right, other)
        new_pair = make_pair(parent, other)
        new_score = (l_score + r_score - parent_score)/2.
        scores[new_pair] = new_score

    species.append(parent)
    species.sort()
</pre>

      <p>
        Again, this is not a very good design:
        it won't be clear to the next person reading the function
        why the call to <code>species.sort</code> has to be there.
        if it isn't clear why something is being done where it is,
        it should be moved or explained.
        As an exercise,
        try to reorganize the code
        to make the reasoning clearer.
      </p>

      <p>
        Our program now has five functions and a main body.
        We're still not done, though:
        we need to write the <code>tidy_up</code> function we referred to in <code>update</code>.
        It in turn assumes a function called <code>make_pair</code> that combines a pair of species,
        which simply constructs a tuple of the species' names ordered alphabetically.
        Remember, we're ordering names so that each pair has a unique representation.
        Our two new functions look like this:
      </p>

<pre src="src/setdict/phylogen.py">
def tidy_up(scores, old, other):
    '''Clean out references to old species.'''
    pair = make_pair(old, other)
    score = scores[pair]
    del scores[pair]
    return score

def make_pair(left, right):
    '''Make an ordered pair of species.'''

    if left &lt; right:
        return (left, right)
    else:
        return (right, left)
</pre>

      <p>
        We have nothing left to write, so let's try it out.
        If we run it with the four species we used as an example earlier,
        the output is:
      </p>

<pre>
$ <span class="in">python phylogen.py</span>
<span class="out">[human werewolf] 2.5
[[human werewolf] vampire] 3.5
[[[human werewolf] vampire] mermaid] 6.5</span>
</pre>

      <p class="continue">
        These are the same values we had in our example tree,
        so the program might be right.
        As one last exercise,
        try making up two or three other (simpler) test cases
        that will exercise the code we've written.
      </p>

      <div class="keypoints" id="k:phylotree">
        <h3>Summary</h3>
        <ul>
          <li idea="algo">Problems that are described using matrices can often be solved more efficiently using dictionaries.</li>
          <li>When using tuples as multi-part dictionary keys, order the tuple entries to avoid accidental duplication.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

        <p>
          Every programmer meets lists (or arrays or matrices) early in her career.
          Most never meet sets and dictionaries,
          and that's a shame:
          for many problems,
          they're more efficient in both human and machine terms.
          They're also the basis of some advanced programming techniques
          that give us much more control over what our programs do
          and how they do it.
          To see how,
          try this at an interactive Python prompt:
        </p>

<pre>
&gt;&gt;&gt; globals()
{'__builtins__': &lt;module '__builtin__' (built-in)&gt;,
 '__doc__': None,
 '__name__': '__main__',
 '__package__': None}
</pre>

        <p class="continue">
          That's right&mdash;Python actually stores the program's variables
          in a dictionary.
          In fact,
          it uses several such dictionaries,
          one for the global variables
          and one for each function that's currently being called:
        </p>

<pre>
&gt;&gt;&gt; def example(first, second):
...     print 'globals in example', globals()
...     print 'locals in example', locals()
... 
&gt;&gt;&gt; example(22, 33)
globals in example {'__builtins__': &lt;module '__builtin__' (built-in)&gt;,
                    '__doc__': None,
                    '__name__': '__main__',
                    '__package__': None,
                    'example': &lt;function example at 0x50b630&gt;}
locals in example {'second': 33,
                   'first': 22}
</pre>

      <p>
        You now know everything you need to know
        in order to build a programming language of your own.
        But please don't:
        the world will be much better off
        if you keep doing science instead.
      </p>

    </section>