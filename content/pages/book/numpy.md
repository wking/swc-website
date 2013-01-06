Title: Numerical Programming With NumPy
Directory: book

    <ol class="toc">
      <li><a href="#s:basics">Basics</a></li>
      <li><a href="#s:storage">Storage</a></li>
      <li><a href="#s:indexing">Indexing</a></li>
      <li><a href="#s:linalg">Linear Algebra</a></li>
      <li><a href="#s:plotting">Plotting</a></li>
      <li><a href="#s:recommend">Making Recommendations</a></li>
      <li><a href="#s:life">The Game of Life</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <p>
      Madica Medicine is studying patients with Babbage's Syndrome,
      a rare disorder whose sufferers believe
      they are living in Victorian England.
      She has data on how well each patient has responded to several different treatments,
      and would like to know how similar patients' responses are to one another,
      and whether one treatment is superior to another.
    </p>

    <p>
      Since Madica is new to this research area,
      she would also like to know what papers would be most useful for her to read.
      Luckily,
      she has access to a web site where scientists post ratings of papers,
      and she knows the names of a few key researchers in the area.
      What she needs is some way to combine their ratings to create recommendations.
    </p>

    <p>
      All three problems can be solved by manipulating matrices.
      In this chapter,
      we'll look at how Madica (and other scientists) can do this efficiently,
      both in terms of their time and the computer's.
    </p>

    <section id="s:basics">

      <h2>Basics</h2>

      <div class="understand" id="u:basics">
        <h3>Understand:</h3>
        <ul>
          <li>Why most numerical programmers should use high-level libraries instead of writing loops directly.</li>
          <li>That most numerical libraries use a data-parallel programming model.</li>
          <li>How to create multi-dimensional arrays with specific values.</li>
          <li>How to create arrays with commonly-occurring values.</li>
          <li>Why the values in such arrays must be homogeneous.</li>
          <li>How to specify or change the type of the values in an array.</li>
          <li>How to copy the values in an array.</li>
        </ul>
      </div>

      <p>
        One way to manipulate matrices in a program is to write lots of loops,
        but doing this obscures the underlying mathematical operations.
        In most languages,
        for example,
        something as simple as <em>a<sub>i,j</sub> = b<sub>i,j</sub>+kv<sub>i</sub></em>
        turns into three lines,
        two of which are just management:
      </p>

<pre>
for i in 1..N:
    for j in 1..N:
        a[i, j] = b[i, j] + k * v[i]
</pre>

      <p>
        Instead of repeatedly writing loops like these,
        most programmers use high-performance libraries written in low-level languages like Fortran and C.
        For example,
        the Fortran subroutine in <a href="#f:packing">Figure XXX</a>,
        which is taken from a numerical package called LAPACK,
        adds a complex vector to the product of a constant and another complex vector:
      </p>

      <figure id="f:caxpy">
        <img src="img/numpy/caxpy.png" alt="CAXPY Fortran Subroutine" />
      </figure>

      <p>
        People devote their entire careers to writing and tuning functions like this,
        and most large scientific programs today are built
        by gluing together calls to these libraries.
        However,
        functions with names like <code>CAXPY</code> and half a dozen arguments
        aren't any more readable than the double loop they replace
        (though they are usually much faster,
        since they'll have been tuned by specialists).
        For this reason,
        many programmers today write numerical code
        in high-level languages like MATLAB, R, or Python.
        The features in these langauges are almost always implemented using
        the same high-performance libraries people could call directly;
        while wrapping them up does cost a little in performance,
        they increase overall productivity
        in all but a handful of cases.
      </p>

      <p>
        Most high-level numerical languages and tools use a
        <a href="glossary.html#data-parallel">data-parallel</a>
        programming model,
        which means operations act on entire arrays instead of using a lot of loops.
        This chapter will show a few of the things that those libraries can do,
        and,
        more importantly,
        how to think when using them.
        We will use Python's NumPy for our examples,
        but the ideas translate directly to MATLAB and similar languages.
      </p>

      <p>
        It's important to keep in mind that
        scientific programmers use arrays in at least three ways:
        as matrices in the mathematical sense,
        to represent physical grids
        (like a latitude-longitude grid in climate modeling),
        or as general-purpose multi-dimensional data storage.
        These different use cases are one of the reasons why
        arrays have such a bewildering variety of features:
        in a sense,
        their usability is a victim of their own usefulness.
      </p>

      <p>
        NumPy
        (which is short for "Numerical Python")
        provides high-performance arrays for Python.
        Most importantly,
        it provides a data-parallel programming model:
        if we want to multiply a vector,
        a matrix,
        and the transpose of the vector,
        we write <code>x*A*x.T</code>
        and the computer fills in any loops that are required.
      </p>

      <p>
        To get started with NumPy,
        let's create an array from a list of numbers:
      </p>

<pre src="src/numpy/create_array.py">
import numpy
vals = [1, 2, 3]
arr = numpy.array(vals)
print 'array is', arr
<span class="out">[1 2 3]</span>
</pre>

      <p class="continue">
        We <code>import numpy</code> and then call <code>numpy.array</code>
        with a list of initial values as an argument.
        The resulting array is three elements long.
        Note that if we use <code>print</code> to display the array,
        Python shows us its values in square brackets,
        without the separating commas that it uses for lists.
        If we just ask Python to display the array interactively,
        on the other hand,
        it shows us what we would have to type in to re-create it:
      </p>

<pre>
&gt;&gt;&gt; <span class="in">import numpy</span>
&gt;&gt;&gt; <span class="in">arr = numpy.array([1, 2, 3])</span>
&gt;&gt;&gt; <span class="in">arr</span>
<span class="out">array([1, 2, 3])</span>
</pre>

      <p>
        Unlike Python lists,
        NumPy arrays must be <a href="glossary.html#homogeneous">homogeneous</a>:
        all values must have exactly the same type.
        This allows values to be packed together as shown in <a href="#f:packing">Figure XXX</a>,
        which not saves memory,
        but is also faster to process.
        We'll discuss this in more detail in
        <a href="#s:storage">the next section</a>.
      </p>

      <figure id="f:packing">
        <img src="img/numpy/packing.png" alt="Packing Values" />
      </figure>

      <p>
        If we give NumPy initial values of different types,
        it finds the most general type
        and stores all the values in the array using that type.
        For example,
        if we construct an array from an integer and a float,
        the array's values are both floats:
      </p>

<pre src="src/numpy/mixed_types.py">
arr = numpy.array([1, 2.3])
print arr
<span class="out">[1.  2.3]</span>
</pre>

      <p>
        If we want a specific type,
        we can pass an optional argument to <code>array</code> called <code>dtype</code>
        (for "data type").
        For example,
        we can tell NumPy to create an array of 32-bit floats
        even though all the initial values are integers:
      </p>

<pre src="src/numpy/force_type.py">
print numpy.array([1, 2, 3, 4], dtype=numpy.float32)
<span class="out">[ 1. 2. 3. 4.]</span>
</pre>

      <p>
        NumPy provides many basic numerical data types,
        each of which is identified by a name like <code>float32</code>.
        The three called <code>int</code>, <code>float</code>, and <code>complex</code>
        are whatever the underlying hardware uses as its native type,
        which is usually either 32 or 64 bits long.
        That word "either" is why programs usually shouldn't use them:
        halving or doubling the precision of the values in a program
        will almost always change its results.
      </p>

      <div class="box">
        <h3>The Dangers of Making Things Simple</h3>

        <p>
          Programs that use <code>int</code>, <code>float</code>, and <code>complex</code>
          should <em>not</em> import them as:
        </p>

<pre>
from numpy import int, float, complex
</pre>

        <p class="continue">
          because those three names are also the names of built-in Python types.
        </p>

      </div>

      <p>
        If we have a matrix whose values are of one type,
        but for some reason want values of another type,
        we can use its <code>astype</code> method
        to create a new matrix:
      </p>

<pre src="src/numpy/astype.py">
arr = numpy.array([1, 2, 3, 4], dtype=numpy.int32)
print arr
<span class="out">[1 2 3 4]</span>
print arr.astype(numpy.float32)
<span class="out">[ 1.  2.  3.  4.]</span>
</pre>

      <p>
        What we should <em>not</em> do is change the array's data type directly
        (even though the language lets us do this).
        If,
        for example,
        we tell NumPy to start treating an array of floating point numbers as integers,
        it won't convert the values:
        instead,
        it will just start interpreting their bits differently:
      </p>

<pre src="src/numpy/change_dtype.py">
import numpy
arr = numpy.array([1.0, 2.0, 3.0, 4.0], dtype=numpy.float32)
print arr
<span class="out">[ 1.  2.  3.  4.]</span>
arr.dtype = numpy.int32
print arr
<span class="out">[1065353216 1073741824 1077936128 1082130432]</span>
</pre>

      <p>
        There are many other ways to create arrays besides calling <code>array</code>.
        For example,
        the <code>zeros</code> function takes a tuple specifying array dimensions as an argument
        and returns an array of zeros of that size:
      </p>

<pre src="src/numpy/zeros.py">
import numpy as np
z = np.zeros((2, 3))
print z
<span class="out">[[0. 0. 0.],
 [0. 0. 0.]]</span>
</pre>

      <p class="continue">
        Note that we are importing NumPy as <code>np</code> in order to save a bit of typing.
        We'll do this in all the examples below as well.
        Notice also that the array's data type is <code>float</code>
        unless something else is specified using <code>dtype</code>.
      </p>

      <p>
        The <code>ones</code> and <code>identity</code> functions work much the same way as <code>zeros</code>:
      </p>

<pre src="src/numpy/ones_identity.py">
o = np.ones((2, 3))
print o
<span class="out">[[1. 1. 1.],
 [1. 1. 1.]]</span>
z = np.identity((2))
print z
<span class="out">[[1. 0.],
 [0. 1.]]</span>
</pre>

      <p>
        It's also possible to create NumPy arrays
        without filling them with data using the <code>empty</code> function.
        This function does not initialize the values,
        so the array contains whatever bits were lying around in memory when it was called:
      </p>

<pre src="src/numpy/empty.py">
e = np.empty((2, 2))
print e
<span class="out">[[3.82265e-297, 4.94944e+173],
 [1.93390e-309, 1.00000e+000]]</span>
</pre>

      <p class="continue">
        This might not seem particularly useful,
        but if a program is going to overwrite an array immediately after creating it,
        there's no point taking the time to fill it.
      </p>

      <div class="box">
        <h3>The Simplest Case Looks Odd</h3>

        <p>
          Calls to <code>zeros</code>, <code>ones</code>, <code>identity</code>, and <code>empty</code>
          can look a little odd when they're being used to create vectors:
        </p>

<pre src="src/numpy/vector_ones.py">
print np.ones((5,))
<span class="out">[ 1.  1.  1.  1.  1.]</span>
</pre>

        <p class="continue">
          The inner parentheses are there because
          dimensions have to be given as a tuple,
          rather than separately.
          The comma is there because otherwise <code>(5)</code> would be interpreted as
          "the number 5"
          rather than
          "the tuple containing only the number 5"
          in order to be consistent with <code>(3+2)</code>.
        </p>

      </div>

      <p>
        As with everything else in Python,
        assigning an array to a variable does not copy its data,
        but instead creates an alias for the original data:
      </p>

<pre src="src/numpy/alias.py">
first = np.ones((2, 2))
print first
<span class="out">[[1. 1.],
 [1. 1.]]</span>
second = first
print second
<span class="out">[[1. 1.],
 [1. 1.]]</span>
second[0, 0] = 9
print first
<span class="out">[[9. 1.],
 [1. 1.]]</span>
</pre>

      <p>
        Notice while we're here that when we subscript a NumPy array to select a single element,
        we put all the indices inside one set of square brackets separated with commas,
        rather than bracketing each index separately:
        it's <code>a[0,&nbsp;1]</code>,
        not <code>a[0][1]</code>,
        because the array is a single object,
        taking a single subscript,
        rather than something like a list of lists,
        which requires one index for the outer list
        and another for the inner.
      </p>

      <p>
        If we really want a copy of the array so that we can make changes
        without affecting the original data,
        we must use the <code>copy</code> method:
      </p>

<pre src="src/numpy/alias.py">
print first
<span class="out">[[1. 1.],
 [1. 1.]]</span>
second = first.copy()
second[0, 0] = 9
print first
<span class="out">[[1. 1.],
 [1. 1.]]</span>
</pre>

      <p>
        Arrays have properties as well as methods.
        We have already met the array's data type, <code>dtype</code>.
        Another important property is <code>shape</code>,
        which is a tuple of the array's size along each dimension:
      </p>

<pre src="src/numpy/shape.py">
print first
<span class="out">[[1. 1.],
 [1. 1.]]</span>
print first.shape
<span class="out">(2, 2)</span>
</pre>

      <p class="continue">
        Notice that there are no parentheses after <code>shape</code>:
        it is a piece of data,
        not a method call.
        Also note that the tuple in <code>shape</code>
        is exactly what we pass into functions like <code>zeros</code> to create new arrays,
        which makes it easy to reproduce the shape of existing data:
      </p>

<pre>
blank = np.zeros(first.shape)
print blank
<span class="out">[[ 0.  0.]
 [ 0.  0.]]</span>
</pre>

      <p>
        Another data member is <code>size</code>,
        which is the total number of elements in the array:
      </p>

<pre>
block = np.zeros((4, 7, 3))
print block.size
<span class="out">84</span>
</pre>

      <p class="continue">
        Strictly speaking,
        <code>size</code> is redundant,
        since its value is always the product of the elements in the array's <code>shape</code>,
        but it's often very handy to have.
      </p>

      <div class="keypoints" id="k:basics">
        <h3>Summary</h3>
        <ul>
          <li idea="perf">High-level libraries are usually more efficient for numerical programming than hand-coded loops.</li>
          <li>Most such libraries use a data-parallel programming model.</li>
          <li>Arrays can be used as matrices, as physical grids, or to store general multi-dimensional data.</li>
          <li>NumPy is a high-level array library for Python.</li>
          <li><code>import numpy</code> to import NumPy into a program.</li>
          <li>Use <code>numpy.array(<em>values</em>)</code> to create an array.</li>
          <li>Initial values must be provided in a list (or a list of lists).</li>
          <li>NumPy arrays store homogeneous values whose type is identified by <code><em>array</em>.dtype</code>.</li>
          <li>Use <code><em>old</em>.astype(<em>newtype</em>)</code> to create a new array with a different type rather than assigning to <code>dtype</code>.</li>
          <li><code>numpy.zeros</code> creates a new array filled with 0.</li>
          <li><code>numpy.ones</code> creates a new array filled with 1.</li>
          <li><code>numpy.identity</code> creates a new identity matrix.</li>
          <li><code>numpy.empty</code> creates an array but does not initialize its values (which means they are unpredictable).</li>
          <li>Assigning an array to a variable creates an alias rather than copying the array.</li>
          <li>Use <code><em>array</em>.copy</code> to create a copy of an array.</li>
          <li>Put all array indices in a single set of square brackets, like <code>array[<em>i0</em>, <em>i1</em>].</code></li>
          <li><code><em>array</em>.shape</code> is a tuple of the array's size in each dimension.</li>
          <li><code><em>array</em>.size</code> is the total number of elements in the array.</li>
        </ul>
      </div>

    </section>

    <section id="s:storage">

      <h2>Storage</h2>

      <div class="understand" id="u:storage">
        <h3>Understand:</h3>
        <ul>
          <li>That arrays are stored using descriptors and data blocks.</li>
          <li>That many operations on arrays create new descriptors that alias existing data blocks.</li>
        </ul>
      </div>

      <p>
        In order to do anything more with NumPy arrays,
        we need to understand how they are stored in memory,
        just as we needed to learn about <a href="setdict.html#s:storage">hash tables</a>
        in order to understand sets and dictionaries.
        To start,
        let's take a look at what happens when we transpose a matrix:
      </p>

<pre src="src/numpy/transpose.py">
first = np.array([[1, 2, 3],
                  [4, 5, 6]])
print first
<span class="out">[[1 2 3],
 [4 5 6]]</span>
t = first.transpose()
print t
<span class="out">[[1 4],
 [2 5],
 [3 6]]</span>
first[1, 1] = 999
print t
<span class="out">[[1 4],
 [2 999],
 [3 6]]</span>
</pre>

      <p class="continue">
        The transposed array's elements appear to be in a different order,
        as desired.
        On the other hand,
        it looks like <code>transpose</code> is creating an alias,
        since changes to the original array are reflected in the transposed array.
      </p>

      <p>
        The secret is that NumPy doesn't store an array as a single block of memory.
        Instead,
        it stores two things:
        the data,
        and a <a href="glossary.html#descriptor">descriptor</a>
        that specifies how to interpret the data block:
        what data type it is,
        how many dimensions it has,
        its size along each dimension,
        and the <a href="glossary.html#stride">stride</a>,
        or spacing of elements,
        along each axis
        (<a href="#f:descriptor">Figure XXX</a>).
      </p>

      <figure id="f:descriptor">
        <img src="img/numpy/descriptor.png" alt="Array Descriptors" />
      </figure>

      <p>
        When we "transpose" a matrix,
        NumPy doesn't change the data itself.
        Instead,
        it creates a new descriptor that points at the same data,
        but counts down instead of up
        (<a href="#f:transpose">Figure XXX</a>):
      </p>

      <figure id="f:transpose">
        <img src="img/numpy/transpose.png" alt="Array Transposition" />
      </figure>

      <p class="continue">
        NumPy does this because it's a lot faster than copying the actual data.
        If we have a 1000&times;1000 matrix <em>A</em>,
        for example,
        we shouldn't have to copy a million numbers
        just to calculate <em>A&middot;A<sup>T</sup></em>
      </p>

      <p>
        The <code>ravel</code> method does something similar to <code>transpose</code>:
        it creates a one-dimensional alias for the original data.
        As you'd expect,
        the result's shape has a single value,
        which is the number of elements we started with:
      </p>

<pre src="src/numpy/ravel.py">
first = np.zeros((2, 3))
second = first.ravel()
print second.shape
<span class="out">(6,)</span>
</pre>

      <p>
        What order do raveled values appear in?
        Let's start by thinking about a 2&times;4 array <code>A</code>.
        It looks two-dimensional, but the computer's memory is 1-dimensional:
        each location is identified by a single integer address.
        Any program that works with multi-dimensional data
        must lay those values out in some order.
        One possibility is <a href="glossary.html#row-major-order">row-major order</a>, which concatenates the rows
        (<a href="#f:array_layout">Figure XXX</a>).
        This is what C uses, and since Python was originally written in C, it uses the same convention.
        In contrast, <a href="glossary.html#column-major-order">column-major order</a> concatenates the columns.
        Fortran does this, and MATLAB follows along.
      </p>

      <figure id="f:array_layout">
        <img src="img/numpy/array_layout.png" alt="Array Layout" />
      </figure>

      <p>
        Neither option is intrinsically better than the other,
        but the fact that there are two choices causes headaches
        when data has to be moved from one programming language to another.
        If your Python code wants to call an eigenvalue function written in Fortran,
        you will probably have to rearrange the data first,
        just as you have to be careful about 0-based versus 1-based indexing.
        (Note that you cannot use the array's <code>transpose</code> method to do this,
        since, as explained earlier,
        it doesn't actually move data around.)
      </p>

      <p>
        There are many other ways to reshape arrays,
        which once again create aliases instead of rearranging the data.
        The most common is (unsurprisingly) called <code>reshape</code>.
        Its arguments are the array's new dimensions,
        <em>not</em> a tuple of those dimensions
        (which is proof that no library is completely consistent):
      </p>

<pre src="src/numpy/reshape.py">
first = np.array([1, 2, 3, 4, 5, 6])
print first.shape
<span class="out">(6,)</span>
second = first.reshape(2, 3)
print second
<span class="out">[[1 2 3],
 [4 5 6]]</span>
</pre>

      <p>
        Since <code>reshape</code> re-uses the existing data,
        the new shape must have the same size as the original&mdash;we cannot add or drop elements:
      </p>

<pre src="src/numpy/bad_reshape.py">
first = np.zeros((2, 2))
print first.reshape(3, 3)
<span class="err">ValueError: total size of new array must be unchanged</span>
</pre>

      <p class="continue">
        If we really want to change the physical size of the data,
        we have to use <code>array.resize</code>.
        This works in place, i.e., it actually modifies the array
        instead of just creating a new descriptor:
      </p>

<pre src="src/numpy/resize.py">
print block
<span class="out">[[ 10  20  30],
 [110 120 130],
 [210 220 230]])</span>
block.resize(2, 2)
print block
<span class="out">[[ 10  20],
 [ 30 110]]</span>
</pre>

      <p class="continue">
        As the example above shows,
        when we resize a 3&times;3 array to be 2&times;2,
        we get the first four values from the data block,
        rather than the values from the first two rows and columns.
        (And note that,
        once again,
        the new dimensions are passed directly rather than in a tuple.)
      </p>

      <p>
        If we enlarge the array by resizing,
        the new locations are assigned zero.
        Which locations are "new" is determined by the raveling order of the array:
        as the example below shows,
        the existing values are packed into the first part of memory,
        <em>not</em> into the upper left corner of the logical matrix.
      </p>

<pre src="src/numpy/ravel_resize.py">
ones = np.ones((2, 2))
print ones
<span class="out">[[ 1.  1.]
 [ 1.  1.]]</span>
ones.resize(3, 3)
print ones
<span class="out">[[ 1.  1.  1.]
 [ 1.  0.  0.]
 [ 0.  0.  0.]]</span>
</pre>

      <div class="keypoints" id="k:storage">
        <h3>Summary</h3>
        <ul>
          <li>Arrays are stored using descriptors and data blocks.</li>
          <li>Many operations create a new descriptor, but alias the original data block.</li>
          <li>Array elements are stored in row-major order.</li>
          <li><code><em>array</em>.transpose</code> creates a transposed alias for an array's data.</li>
          <li><code><em>array</em>.ravel</code> creates a one-dimensional alias for an array's data.</li>
          <li><code><em>array</em>.reshape</code> creates an arbitrarily-shaped alias for an array's data.</li>
          <li><code><em>array</em>.resize</code> resizes an array's data in place, filling with zero as necessary.</li>
        </ul>
      </div>

    </section>

    <section id="s:indexing">

      <h2>Indexing</h2>

      <div class="understand" id="u:indexing">
        <h3>Understand:</h3>
        <ul>
          <li>How to operate on regular subsets of the elements of an array.</li>
          <li>How to operate on array elements at arbitrary locations.</li>
          <li>How to operate on array elements according to their values.</li>
        </ul>
      </div>

      <p>
        Arrays are subscripted by integers,
        just like lists and strings,
        and they can be sliced like other sequences as well.
        For example,
        if <code>block</code> is the array shown in <a href="#f:slicing">Figure XXX</a>,
        then <code>block[0:3, 0:2]</code> selects its first three rows and the first two columns.
        As always,
        a slice <code>start:end</code> includes the element at <code>start</code>,
        but not the element at <code>end</code>.
      </p>

      <figure id="f:slicing">
        <img src="img/numpy/slicing.png" alt="Slicing Arrays" />
      </figure>

      <p>
        As with other sliceable things,
        it's possible to assign to slices of arrays.
        For example,
        we can assign zero to the center elements of <code>block</code> in a single statement:
      </p>

<pre src="src/numpy/assign_to_slice.py">
print block
<span class="out">[[ 10  20  30  40],
 [110 120 130 140],
 [210 220 230 240]]</span>
block[1, 1:3] = 0
print block
<span class="out">[[ 10  20  30  40],
 [110   0   0 140],
 [210 220 230 240]]</span>
</pre>

      <p class="continue">
        One important difference between slicing arrays and slicing lists
        is that slicing an array creates an alias&mdash;or rather,
        a new descriptor that only refers to a portion of the original array's data block
        (<a href="#f:slice_alias">Figure XXX</a>):
      </p>

<pre src="src/numpy/slice_alias.py">
original = np.ones((3, 2))
print original
<span class="out">[[ 1.  1.]
 [ 1.  1.]
 [ 1.  1.]]</span>
slice = original[0:2, 0:2]
print slice
<span class="out">[[ 1.  1.]
 [ 1.  1.]]</span>
slice[:,:] = 0
print slice
<span class="out">[[ 0.  0.]
 [ 0.  0.]]</span>
print original
<span class="out">[[ 0.  0.]
 [ 0.  0.]
 [ 1.  1.]]</span>
</pre>

      <figure id="f:slice_alias">
        <img src="img/numpy/slice_alias.png" alt="Slicing and Alaising" />
      </figure>

      <p>
        Notice in the example above that we used <code>slice[:,:]</code>
        to refer to all of the array's elements at once.
        All of Python's other slicing shortcuts work as well,
        so that expressions like <code>original[-2:, 1:]</code> behave consistently
        (though it may take a bit of practice to figure out exactly what they mean).
      </p>

      <p>
        Slicing on both sides of an assignment is a handy way to move data around.
        If <code>vector</code> is a one-dimensional array,
        then <code>vector[1:4]</code> selects locations 1, 2, and 3,
        while <code>vector[0:3]</code> selects locations 0, 1, and 2.
        Assigning the former to the latter therefore overwrites the lower three values with the upper three,
        leaving the uppermost value untouched:
      </p>

<pre src="src/numpy/slice_shift.py">
vector = np.array([10, 20, 30, 40])
vector[0:3] = vector[1:4]
print vector
<span class="out">[20 30 40 40]</span>
</pre>

      <p class="continue">
        The same thing works if we shift the data up instead of down:
      </p>

<pre src="src/numpy/slice_shift.py">
vector = np.array([10, 20, 30, 40])
vector[1:4] = vector[0:3]
print vector
<span class="out">[10 10 20 30]</span>
</pre>

      <p class="continue">
        It's worth mentioning this because if we try to do these shifts by writing loops ourselves,
        it's all too easy to copy one value upward (or downward) instead of shifting values:
      </p>

<pre src="src/numpy/loop_shift.py">
vector = [10, 20, 30, 40]
for i in range(1, len(vector)):
    vector[i] = vector[i-1]
print vector
<span class="out">[10, 10, 10, 10]</span>
</pre>

      <p class="continue">
        Try fixing this code so that it actually does a shift,
        and you'll see why most programmers prefer to use slices
        and let the library figure out the details.
      </p>

      <p>
        We can do even more sophisticated things by using a list or another array as a subscript.
        For example,
        if <code>subscript</code> is the list <code>[3, 1, 2]</code>,
        then <code>vector[subscript]</code> creates a new array
        whose elements are pulled from <code>vector</code> in that order
        (<a href="#f:list_subscript">Figure XXX</a>):
      </p>

<pre src="src/numpy/subscript_list.py">
vector = np.array([0, 10, 20, 30])
print vector
<span class="out">[ 0 10 20 30]</span>
subscript = [3, 1, 2]
print vector[subscript]
<span class="out">[30 10 20]</span>
</pre>

      <figure id="f:list_subscript">
        <img src="img/numpy/list_subscript.png" alt="Subscripting With a List" />
      </figure>

      <p>
        This works in multiple dimensions as well.
        For example, if we have a 2&times;2 matrix,
        and subscript it with the list containing only the index 1,
        the result is the second row of the matrix:
      </p>

<pre src="src/numpy/subscript_2d.py">
square = np.array([[5, 6], [7, 8]])
print square[ [1] ]
<span class="out">[[7 8]]</span>
</pre>

      <p class="continue">
        Why does the subscript have to be in a list?
        And why does it return that particular row?
        The answers are in the NumPy documentation,
        and while those answers aren't simple,
        every bit of complexity is there for a good reason.
      </p>

      <p>
        Let's have a look at another way to subscript.
        If we compare our vector's elements to the value 25,
        we get a vector with <code>True</code> where the element passed the test
        and <code>False</code> where it didn't.
        (As we saw in the previous section,
        <code>dtype=bool</code> is NumPy's way of telling us what the array elements' data type is.)
      </p>

<pre src="src/numpy/vector_less.py">
print vector
<span class="out">[ 0 10 20 30]</span>
print vector &lt; 25
<span class="out">[ True  True  True False]</span>
</pre>

      <p>
        We can use a Boolean array like this as a <a href="glossary.html#mask">mask</a>
        to select certain elements from our original array.
        Here,
        the expression <code>vector[vector&lt;25]</code> gives us
        a vector containing only the elements that passed the test
        (<a href="#f:vector_mask">Figure XXX</a>):
      </p>

<pre src="src/numpy/vector_mask.py">
print vector
<span class="out">[ 0 10 20 30]</span>
print vector[ vector &lt; 25 ]
<span class="out">[ 0 10 20]</span>
</pre>

      <figure id="f:vector_mask">
        <img src="img/numpy/vector_mask.png" alt="Masking a Vector" />
      </figure>

      <p>
        When we subscript an array with a list, another array, or a Boolean mask,
        the result is <em>not</em> an alias:
        data actually is copied.
        The reason is that we cannot represent the mask as a combination of strides and offsets,
        so we cannot simply created a new descriptor to alias the existing data.
        Despite this,
        some magic behind the scenes <em>does</em> let us assign to masked arrays:
      </p>

<pre src="src/numpy/assign_to_mask.py">
print vec
<span class="out">[0 1 2 3]</span>
vec[vec &lt; 2] = 100
print vec
<span class="out">[100 100   2   3]</span>
</pre>

      <p>
        Operators like <code>&lt;</code> and <code>==</code> work the way we would expect with arrays,
        i.e.,
        they do whatever they would do for individual elements,
        but for every corresponding pair of elements.
        There is one trick, though.
        Python does not allow objects to re-define the meaning of <code>and</code>, <code>or</code>, and <code>not</code>,
        since they are keywords.
        The expression <code>(vector &lt;= 20) and (vector &gt;= 20)</code> therefore produces an error message
        instead of selecting elements with exactly the value 20:
      </p>

<pre src="src/numpy/cannot_and.py">
print vector
<span class="out">[0 10 20 30]</span>
print vector &lt;= 20
<span class="out">[True True True False], dtype=bool)</span>
print (vector &lt;= 20) and (vector &gt;= 20)
<span class="err">ValueError: The truth value of an array with more than one element is ambiguous.</span>
</pre>

      <p>
        One solution is to use the functions <code>logical_and</code> and <code>logical_or</code>,
        which combine the elements of Boolean arrays like their namesakes:
      </p>

<pre src="src/numpy/logical_funcs.py">
print vector
print np.logical_and(vector &lt;= 20, vector &gt;= 20)
<span class="out">[False False  True False]</span>
print vector[np.logical_and(vector &lt;= 20, vector &gt;= 20)]
<span class="out">[20]</span>
</pre>

      <p class="continue" id="p:boolean-ops">
        Another is to use the <code>&amp;</code> and <code>|</code> operators.
        These normally work on the bits making up data,
        but NumPy redefines them to be "and" and "or" for Boolean arrays:
      </p>

<pre src="src/numpy/logical_funcs.py">
print vector[(vector &lt;= 20) &amp; (vector &gt;= 20)]
<span class="out">[20]</span>
</pre>

      <p>
        Finally,
        NumPy provides a whole-array alternative to <code>if</code> and <code>else</code> called <code>where</code>.
        Its first argument is a Boolean mask.
        Where that is true, it takes the value from its second argument;
        where it is false, it takes its third.
        For example, <code>where(vector &lt; 25, vector, 0)</code> produces an array
        whose values are taken from <code>vector</code> where they are less than 25,
        and 0 where they are greater than or equal to 25.
        Similarly, <code>where(vector &gt; 25, vector/10, vector)</code> scales large values or leaves values alone:
      </p>

<pre src="src/numpy/where.py">
print vector
<span class="out">[10 20 30 40]</span>
print np.where(vector &lt; 25, vector, 0)
<span class="out">[10 20  0  0]</span>
print np.where(vector &gt; 25, vector/10, vector)
<span class="out">[10 20  3  4]</span>
</pre>

      <p>
        The <code>choose</code> and <code>select</code> functions do similar things,
        but work in slightly different ways
        (<a href="#f:array_conditionals">Figure XXX</a>).
        Again,
        the number of possibilities can be overwhelming at first,
        but each of these functions exists for a reason,
        and if we are going to spend a lot of time doing matrix calculations,
        it is worth learning their ins and outs.
      </p>

      <figure id="f:array_conditionals">
        <img src="img/numpy/array_conditionals.png" alt="Array Conditionals" />
      </figure>

      <div class="keypoints" id="k:indexing">
        <h3>Summary</h3>
        <ul>
          <li>Arrays can be sliced using <code><em>start</em>:<em>end</em>:<em>stride</em></code> along each axis.</li>
          <li>Values can be assigned to slices as well as read from them.</li>
          <li>Arrays can be used as subscripts to select items in arbitrary ways.</li>
          <li>Masks containing <code>True</code> and <code>False</code> can be used to select subsets of elements from arrays.</li>
          <li>Use '&amp;' and '|' (or <code>logical_and</code> and <code>logical_or</code>) to combine tests when subscripting arrays.</li>
          <li>Use <code>where</code>, <code>choose</code>, or <code>select</code> to select elements or alternatives in a single step.</li>
        </ul>
      </div>

    </section>

    <section id="s:linalg">

      <h2>Linear Algebra</h2>

      <div class="understand" id="u:linalg">
        <h3>Understand:</h3>
        <ul>
          <li>How to perform common linear algebra operations on arrays.</li>
        </ul>
      </div>

      <p>
        NumPy arrays make it easy to do things with rectangular blocks of data,
        but they aren't the matrices that mathematicians use.
        For example,
        let's create an array and then multiply it by itself:
      </p>

<pre src="elementwise_mult.py">
print a
<span class="out">[[1 2]
 [3 4]]</span>
print a * a
<span class="out">[[ 1  4]
 [ 9 16]]</span>
</pre>

      <p class="continue">
        NumPy does the operation elementwise instead of doing "real" matrix multiplication.
        To do the latter, we must use the <code>dot</code> method:
      </p>

<pre src="elementwise_mult.py">
print np.dot(a, a)
<span class="out">[[ 7 10]
 [15 22]]</span>
</pre>

      <p class="continue">
        On the bright side,
        elementwise operation means that array addition works as you would expect:
      </p>

<pre src="elementwise_mult.py">
print a + a
<span class="out">[[2 4]
 [6 8]]</span>
</pre>

      <p class="continue">
        And since there's only one sensible way to interpret an expression like "array plus one",
        NumPy does the sensible thing there too:
      </p>

<pre src="elementwise_mult.py">
print a + 1
<span class="out">[[2 3]
 [4 5]]</span>
</pre>

      <p>
        Like other array-based libraries or languages,
        NumPy provides many useful tools for common linear algebra operations.
        We can add up the values in our array with a single function call:
      </p>

<pre src="src/numpy/linalg_ops.py">
print np.sum(a)
<span class="out">10</span>
</pre>

      <p class="continue">
        We can also calculate partial sums along each axis
        by passing an extra argument into <code>sum</code>
        (<a href="#f:sum_axis">Figure XXX</a>):
      </p>

<pre src="src/numpy/linalg_ops.py">
print np.sum(a, 0)
<span class="out">[4 6]</span>
print np.sum(a, 1)
<span class="out">[3 7]</span>
</pre>

      <figure id="f:sum_axis">
        <img src="img/numpy/sum_axis.png" alt="Summing Along Axes" />
      </figure>

      <p>
        It's very important to use NumPy's summation function
        (<code>np.sum</code> in the examples above)
        rather than Python's built-in <code>sum</code>:
      </p>

<pre src="src/numpy/linalg_ops.py">
print sum(a)
<span class="out">[4 6]</span>
print sum(a, 0)
<span class="out">[4 6]</span>
print sum(a, 1)
<span class="out">[5 7]</span>
</pre>

      <p class="continue">
        This is one of the reasons most people prefer to use array methods
        instead of functions:
      </p>

<pre src="src/numpy/linalg_methods.py">
print a
<span class="out">[[1, 2], [3, 4]]</span>
print a.sum()
<span class="out">10</span>
print a.sum(0)
<span class="out">[4 6]</span>
print a.sum(1)
<span class="out">[3 7]</span>
</pre>

      <p>
        Let's return to the original example in this chapter.
        Madica is studying the progress of Babbage's Syndrome in some test subjects.
        Her observations are in an array:
        each row corresponds to one patient,
        and each column is an hourly count of responsive T cells:
      </p>

<pre src="src/numpy/patient_data.py">
print data
<span class="out">[[ 1  3  3  5 12 10  9]
 [ 0  1  2  4  8  7  8]
 [ 0  4 11 15 21 28 37]
 [ 2  2  2  3  3  2  1]
 [ 1  3  4  5 10  8  6]]</span>
</pre>

      <p class="continue">
        This means that the zeroth column of our data is the initial T cell count for all patients,
        while the zeroth row is all hourly samples for patient 0:
      </p>

<pre src="src/numpy/patient_data.py">
print data[:, 0]   <span class="comment"># t0 count for all patients</span>
<span class="out">[1 0 0 2 1]</span>
print data[0, :]   <span class="comment"># all samples for patient 0</span>
<span class="out">[ 1  3  3  5 12 10  9]</span>
</pre>

      <p>
        <code>data.mean()</code> gives us the average T cell count for all patients at all times:
      </p>

<pre src="src/numpy/patient_data.py">
data.mean()
<span class="out">6.88571428571</span>
</pre>

      <p class="continue">
        It's nice to know we can do this,
        but it's not a particularly meaningful statistic.
        The mean of the data along axis 0,
        on the other hand,
        gives us the average across all patients for each hour:
      </p>

<pre src="src/numpy/patient_data.py">
data.mean(0)   <span class="comment"># over time</span>
<span class="out">[  0.8   2.6   4.4   6.4  10.8  11.   12.2]</span>
</pre>

      <p class="continue">
        This is much more useful,
        since it is the average progress of the disease.
        Similarly,
        the mean along axis 1 gives us the average T cell count per patient across all times,
        which could be useful if we need to normalize the data:
      </p>

<pre src="src/numpy/patient_data.py">
data.mean(1)   <span class="comment"># per patient</span>
<span class="out">[  6.14285714   4.28571429  16.57142857   2.14285714   5.28571429]</span>
</pre>

      <p>
        It might be even more interesting to look at
        what happened to people who started with no responsive T cells at all.
        The first step is to select the first column of data,
        i.e., the initial T cell counts for each patient,
        and compare these to zero.
        This produces a Boolean array with <code>True</code>
        for each row of the array that meets our criteria:
      </p>

<pre src="src/numpy/patient_data.py">
print data[:, 0]
<span class="out">[1 0 0 2 1]</span>
print data[:, 0] == 0.
<span class="out">[False  True  True False False]</span>
</pre>

      <p class="continue">
        If we use this to index the original array,
        we get the two rows for which the count at <em>t<sub>0</sub></em> is zero:
      </p>

<pre src="src/numpy/patient_data.py">
data[ data[:, 0] == 0. ]
<span class="out">[[ 0  1  2  4  8  7  8]
 [ 0  4 11 15 21 28 37]]</span>
</pre>

      <p>
        Now let's find the mean T cell count over time for just those people.
        Once again,
        we start by selecting column 0 and testing it to create a Boolean mask.
        Using that mask as a subscript gives us the rows that have zero in the first place.
        We can now use the <code>mean</code> function along axis zero
        (i.e., across patients)
        which gives us the average behavior of patients who started with no responsive T cells at all:
      </p>

<pre src="src/numpy/patient_data.py">
print data[ data[:, 0] == 0. ].mean(0)
<span class="out">[  0.    2.5   6.5   9.5  14.5  17.5  22.5]</span>
</pre>

      <p>
        This example highlights two key practices for good matrix programming.
        The first is to build expressions from the inside out.
        For example,
        the one-liner above is logically equivalent to:
      </p>

<pre>
first_col = data[:, 0]
zero_at_zero = (first_col == 0)
patient_rows = data[zero_at_zero]
patient_rows.mean(0)
</pre>

      <p class="continue">
        Beginners find the four-line version easier to figure out,
        but with practice,
        naturally start writing the denser form.
      </p>

      <p>
        The other key practice,
        which we alluded to in the introduction,
        is to write high-level statements without loops
        and let the computer worry about how to do the operations element by element.
        This is just as true for MATLAB or R as it is for Python.
      </p>

      <div class="keypoints" id="k:linalg">
        <h3>Summary</h3>
        <ul>
          <li>Addition, multiplication, and other arithmetic operations work on arrays element-by-element.</li>
          <li>Operations involving arrays and scalars combine the scalar with each element of the array.</li>
          <li><code><em>array</em>.dot</code> performs "real" matrix multiplication.</li>
          <li><code><em>array</em>.sum</code> calculates sums or partial sums of array elements.</li>
          <li><code><em>array</em>.mean</code> calculates array averages.</li>
        </ul>
      </div>

    </section>

    <section id="s:plotting">

      <h2>Plotting</h2>

      <p class="fixme">Plotting: visualize the medical data versus time.</p>

    </section>

    <section id="s:recommend">

      <h2>Making Recommendations</h2>

      <div class="understand" id="u:plotting">
        <h3>Understand:</h3>
        <ul>
          <li>How to get data into matrix form for efficient manipulation.</li>
          <li>How to do simple statistical calculations involving matrices.</li>
        </ul>
      </div>

      <p>
        We can now use NumPy to build the academic matchmaking tool that Madica wanted.
        More specifically,
        we can build a recommendation tool that measures how similar people's reading interests are
        based on their ratings of papers they have read
        and the ratings given by other people in their field.
        Our program will be based on the movie recommendation example in Toby Segaran's excellent book
        <a href="bib.html#segaran-collective-intelligence"><cite>Programming Collective Intelligence</cite></a>.
      </p>

      <p>
        The first step is to decide on recommendation criteria.
        We want to take into account how highly the paper was rated by other people,
        but we also want to consider how similar people are to one another:
        if you and I both rate the same papers highly,
        I should put more weight on your rating of a new paper
        than on a rating from someone who likes papers I dislike and vice versa.
      </p>

      <p>
        We will divide our program into three pieces.
        First, we will take a list of previous ratings and store them in a NumPy array.
        Second, we will construct two ways to measure
        the similarity between two papers or between two people's ratings.
        And finally,
        we will use those measures to tell people who has interests similar to theirs.
      </p>

      <p>
        Most people have only read a few of the thousands of papers in any field.
        This means our rating data is <a href="glossary.html#sparse">sparse</a>,
        i.e.,
        mostly empty.
        One way to store sparse data is to use a dictionary of dictionaries:
        the keys in the outer dictionary are people,
        while the inner dictionaries store pairs of papers and ratings:
      </p>

<pre>
raw_scores = {
    'Bhargan Basepair' : {
        'Jackson 1999' : 2.5,
        'Chen 2002' : 3.5,
    },
    'Fan Fullerene' : {
        'Jackson 1999' : 3.0,
        &hellip;
        &hellip;    &hellip;    &hellip;
</pre>

      <p>
        Let's write a function called <code>prep_data</code>
        to convert this structure into a list with the names of all the people,
        another list with the IDs of all the papers,
        and a NumPy array of ratings:
      </p>

<pre>
def prep_data(all_scores):
    <span class="comment"># 1. Names of all people in alphabetical order.</span>
    people = all_scores.keys()
    people.sort()

    <span class="comment"># 2. Names of all papers in alphabetical order.</span>
    papers = set()
    for person in people:
        for title in all_scores[person].keys():
            papers.add(title)
    papers = list(papers)
    papers.sort()

    <span class="comment"># 3. Create and fill array.</span>
    ratings = np.zeros((len(people), len(papers)))
    for (person_id, person) in enumerate(people):
        for (title_id, title) in enumerate(papers):
            r = scores[person].get(title, 0)
            ratings[person_id, title_id] = float(r)

    return people, papers, ratings
</pre>

      <p>
        Let's have a closer look at how this function works
        (<a href="#f:reformat_data">Figure XXX</a>):
        The main dictionary of ratings has people's names as keys,
        so all we need to do in step 1 to get a list of names is ask the dictionary for its keys.
        We sort this list to help with testing:
        Python doesn't store dictionary entries in any particular order,
        but our sorted list will always be in a unique order.
      </p>

      <figure id="f:reformat_data">
        <img src="img/numpy/reformat_data.png" alt="Reformatting Data" />
      </figure>

      <p>
        Getting a list of all the papers' names in step 2 is a bit more complicated.
        We start by creating an empty set called <code>papers</code>,
        then loop over the sub-dictionaries in <code>all_scores</code>
        to add the names of the papers in each to our set.
        This takes care of any duplication,
        since set elements are guaranteed to be unique.
        Once everything is in the set,
        we convert it to a list and sort it.
      </p>

      <p>
        We can now create our ratings matrix (step 3).
        We know how many unique people and papers there are,
        so we create an array of zeroes with that many rows and columns.
        We then loop over the lists we created in steps 1 and 2
        and use those values to index our dictionary-of-dictionaries.
        If there is a score for a particular combination of person and paper,
        we copy it into our matrix;
        otherwise, we put in a zero.
      </p>

      <p>
        The next step is to figure out how we're going to measure similarity.
        Dozens of different measures have been developed,
        but whichever we use,
        we have to treat zeroes in our matrix carefully:
        a 0 specifies no ranking rather than a very poor ranking,
        which means we need to mask on our array
        so that we only do statistics on papers that have actually been rated
        by both of the people we are comparing.
      </p>

      <p>
        Our first similarity measure is called the inverse sum of squares.
        It is based on the distance between two N-dimensional vectors,
        where N is the number of papers that both people rated.
        In two dimensions the distance is given by the norm
        <em>distance<sup>2</sup> = (x<sub>A</sub>-x<sub>B</sub>)<sup>2</sup> + (y<sub>A</sub>-y<sub>B</sub>)<sup>2</sup></em>.
        In higher dimensions, we simply add more (<em>x<sub>i</sub>-x<sub>j</sub>)<sup>2</sup></em> terms.
      </p>

      <p>
        A small sum of squares means the ratings being considered are all nearly the same.
        Since we want 1 to correspond to perfect agreement and a 0 to complete disagreement,
        we invert the sum of squares,
        adding 1 the denominator to achieve the desired range and to avoid division by zero.
        The final formula is <em>sim(A,B) = 1/(1 + norm(A,B))</em>.
      </p>

      <p>
        Let's write a function to calculate this:
      </p>

<pre>
def sim_distance(prefs, left_index, right_index):

    <span class="comment"># Where do both people have preferences?</span>
    left_has_prefs  = prefs[left_index,  :] &gt; 0
    right_has_prefs = prefs[right_index, :] &gt; 0
    mask = np.logical_and(left_has_prefs, right_has_prefs)

    <span class="comment"># Not enough signal.</span>
    if np.sum(mask) &lt; EPS:
        return 0

    <span class="comment"># Return sum-of-squares distance.</span>
    diff = prefs[left_index, mask] - prefs[right_index, mask]
    sum_of_squares = np.linalg.norm(diff) ** 2
    return 1/(1 + sum_of_squares)
</pre>

      <p class="continue">
        <code>left_index</code> and <code>right_index</code> are the rows of the data we are interested in,
        i.e., the people whose preferences we are comparing.
        Since we only want to compare rankings if two people have both rated a paper,
        the first thing we do is create a mask that is <code>True</code> in those columns where both rows are nonzero.
        If no papers were rated by both people, we return zero immediately.
        Otherwise, we compute the norm of the difference of the ratings and we return the similarity score.
        (We can use a library function <code>np.linalg.norm</code> to compute the actual difference,
        but we need to square it to get the sum of squares.)
      </p>

      <p>
        One problem with the inverse sum of squares is that
        it penalizes people for using different scales.
        For example,
        if one person tends to be twice as harsh or twice as enthusiastic as another,
        this metric will judge them to be very different.
        We might get better answers if we look at how papers are ranked relative to other rankings
        instead of at absolute values.
        Pearson's Correlation score does this by
        normalizing the data and reporting the correlation between scores.
      </p>

      <p>
        Pearson's Correlation is related to the line of best fit.
        For example,
        the graph in <a href="#f:correlation">Figure XXX</a> shows high correlation
        because the papers that were rated highly by Jean were also rated highly by Betty.
        if the points were randomly scattered,
        we would call that low correlation and want to report a low score.
      </p>

      <figure id="f:correlation">
        <img src="img/numpy/correlation.png" alt="Correlation" />
      </figure>

      <p>
        To calculate Pearson's Correlation,
        we need to know two things:
      </p>

      <ol>
        <li>
          the standard deviation,
          which is the average amount that a rating deviates from the mean rating;
          and
        </li>
        <li>
          the covariance,
          which measures how two variables change together.
          Covariance is positive and large if higher values of X correspond to higher values of Y,
          negative and large if higher values of X correspond to lower values of Y,
          and it will be zero if there is no pattern.
        </li>
      </ol>

      <p>
        Pearson's Correlation score is the covariance normalized by both standard deviations,
        i.e., <em>cov(X, Y) / &sigma;<sub>X</sub>&sigma;<sub>Y</sub></em>.
        We want to use NumPy routines to do as much of the calculation as possible,
        so after hunting around the documentation,
        we find that <code>np.cov</code> can take two N&times;1 arrays
        and produce a matrix that contains:
      </p>

      <table border="1">
        <tr>
          <td align="center">
            <em>var(X)</em>
          </td>
          <td align="center">
            <em>cov(X, Y)</em>
          </td>
        </tr>
        <tr>
          <td align="center">
            <em>cov(X, Y)</em>
          </td>
          <td align="center">
            <em>var(Y)</em>
          </td>
        </tr>
      </table>

      <p class="continue">
        Since the standard deviation is the square root of the variance,
        it looks like this one function is all we will need.
        Here's our function:
      </p>

<pre>
def sim_pearson(prefs, left_index, right_index):

    <span class="comment"># 1. Where do both have ratings?</span>
    rating_left  = prefs[left_index,  :]
    rating_right = prefs[right_index, :]
    mask = np.logical_and(rating_left &gt; 0, rating_right &gt; 0)

    <span class="comment"># 2. Return zero if there are no common ratings.</span>
    num_common = sum(mask)
    if num_common == 0:
        return 0

    <span class="comment"># 3. Calculate Pearson score "r"</span>
    varcovar = np.cov(rating_left[mask], rating_right[mask])
    numerator = varcovar[0, 1]
    denominator = sqrt(varcovar[0, 0]) * sqrt(varcovar[1,1])
    if denominator &lt; EPS:
        return 0
    r = numerator / denominator
    return r
</pre>

      <p class="continue">
        Step 1 is to create a mask so that we only include elements of the two arrays that are nonzero.
        If there are no common ratings,
        we return zero in step 2 as we did in our previous function.
        If there are some common ratings,
        we can go ahead and compute the Pearson score.
        The variance of the left rating is stored in position <code>[0,0]</code> of the matrix <code>varcovar</code>,
        the variance of the right rating is stored at <code>[1,1]</code>,
        and off-diagonal elements are the covariance.
        After a quick check to avoid division by zero,
        we return the quotient of the covariance and the product of the standard deviations.
      </p>

      <p>
        Now that we have tools for scoring pairs of people,
        we can answer our original question:
        who is most similar to whom?
        Since each row of our matrix is a single person's scores,
        this comes down to applying either similarity metric to the rows of the array
        and then sorting the results to find the <em>N</em> people who are most similar:
      </p>

<pre>
def top_matches(ratings, person, num, similarity):
    scores = []
    for other in range(ratings.shape[0]):
        if other != person:
            s = similarity(ratings, person, other)
            scores.append((s, other))

    scores.sort()
    scores.reverse()

    return scores[0:num]
</pre>

      <p class="continue">
        Here, <code>person</code> is who we're trying to match other people against.
        For each of those other people,
        we compute a similarity score and append it to the list.
        Finally, we sort the list,
        then reverse it so that the highest scores will be at the front
        and return the first <code>num</code> entries.
      </p>

      <p>
        One thing to notice about this function is that
        we are passing in the particular similarity function to use
        as an argument (called, not surprisingly, <code>similarity</code>).
        This will be either <code>sim_distance</code> or <code>sim_pearson</code>;
        since both functions take the same arguments,
        and produce interchangeable results,
        we only have to write <code>top_matches</code> once.
      </p>

      <p>
        We can use what we just built to measure how similar papers are to each other
        simply by transposing our matrix
        so that rows represent papers instead of people.
        With a bit more work,
        we can also use it to recommend papers based on similarity scores,
        just as Amazon.com recommends books that are like ones previously purchased.
      </p>

      <p>
        The most important lesson, though, is that
        leaving all the number crunching to NumPy let us build a high-performance solution
        with only a page of code.
        In fact,
        the bulk of this program is there
        to get data into a format the library can work with.
        That is typical of most data crunching problems,
        and is another reason why general-purpose languages like Python
        are the right choice for scientific computing:
        they come with tools to do the "other 90%" of the work scientists need to do.
      </p>

      <div class="box">
        <h3>Sparse Arrays</h3>

        <p class="fixme">Describe SciPy sparse arrays.</p>

      </div>

      <div class="keypoints" id="k:plotting">
        <h3>Summary</h3>
        <ul>
          <li>Getting data in the right format for processing often requires more code than actually processing it.</li>
          <li>Data with many gaps should be stored in sparse arrays.</li>
          <li><code><em>numpy</em>.cov</code> calculates variancess and covariances.</li>
        </ul>
      </div>

    </section>

    <section id="s:life">

      <h2>The Game of Life</h2>

      <div class="understand" id="u:life">
        <h3>Understand:</h3>
        <ul>
          <li>How to use arrays to represent grids rather than matrices.</li>
          <li>How to manage boundary conditions using "extra" array cells.</li>
          <li>That most array operations are already implemented in standard libraries.</li>
        </ul>
      </div>

      <p>
        As we said in the introduction,
        scientific programmers use arrays in several different ways.
        The recommendation example above shows them being used for linear algebra;
        in this section,
        we'll see how to use them to represent a physical grid.
      </p>

      <p>
        The problem we'll tackle is called the Game of Life,
        and was invented by the mathematician John Conway in 1970.
        The game's world is a rectangular grid of cells,
        each of which is either "alive" or "dead".
        At each time step,
        every cell simultaneously updates itself according to the following rule:
      </p>

      <ol>
        <li>
          If a live cell has two or three live neighbors, it stays alive.
        </li>
        <li>
          If a dead cell has exactly three live neighbors, it becomes alive.
        </li>
        <li>
          In all other cases,
          the cell either dies or stays dead.
        </li>
      </ol>

      <p>
        These simple rules produce a bewildering variety of behaviors
        depending on the grid's initial state.
        In fact,
        it has been shown that the Game of Life is
        <a href="glossary.html#turing-complete">Turing complete</a>,
        i.e.,
        it can perform any imaginable computation
        given enough time and space.
      </p>

      <p>
        Let's start by writing the main body of our simulation:
      </p>

<pre src="src/numpy/life_looping.py">
def main(args):
    length = int(args[1])
    if len(args) &gt; 2:
        generations = int(args[2])
    else:
        generations = length - 1
    evolve(length, generations)

if __name__ == '__main__':
    main(sys.argv)
</pre>

      <p class="continue">
        This expects the user to give it a length,
        which is the size of the (square) world,
        and optionally the number of generations to run the simulation for.
        It then calls the function <code>evolve</code>
        to run the simulation.
      </p>

      <p>
        The <code>evolve</code> function looks like this:
      </p>

<pre src="src/numpy/life_looping.py">
def evolve(length, generations):
    current = np.zeros((length, length), np.uint8)  <span class="comment"># create the initial world</span>
    current[length/2, 1:(length-1)] = 1             <span class="comment"># initialize the world</span>
    next = np.zeros_like(current)                   <span class="comment"># hold the world's next state</span>

    <span class="comment"># advance through each time step</span>
    show(current)
    for i in range(generations):
        advance(current, next)
        current, next = next, current
        show(current)
</pre>

      <p class="continue">
        Here,
        <code>current</code> holds the current state of the world,
        which we evolve forward into a similarly-sized array <code>next</code>.
        We initialize <code>current</code> with a single vertical bar of cells;
        this isn't as interesting as other patterns,
        but we can come back and build more interesting initializers later.
        The main loop then displays the current state of the world
        and repeatedly advances it,
        leapfrogging <code>current</code> and <code>next</code> after each update
        (<a href="#f:leapfrog">Figure XXX</a>):
      </p>

      <figure id="f:leapfrog">
        <img src="img/numpy/leapfrog.png" alt="Leapfrogging the Simulation" />
      </figure>

      <p>
        We'll skip over the implementation of <code>show</code>:
        it just prints stars and spaces to show live and dead cells
        (<a href="#f:ascii_output">Figure XXX</a>).
        <code>advance</code> ought to be simple too:
        given an N&times;N world,
        it just loops over the (i,j) indices of <code>current</code>,
        counts the number of neighbors each cell has,
        then assigns either 1 or 0 to <code>next</code>.
      </p>

      <figure id="f:ascii_output">
<pre>
+-----+
|     |
|  *  |
|  *  |
|  *  |
|     |
+-----+
</pre>
        <caption>ASCII Output</caption>
      </figure>

      <p>
        But just as <a href="db.html#s:null">real-world data has holes</a>,
        real-world simulations have boundaries.
        How should we update the cell at (0,0)?
        Should we assume its hypothetical neighbors outside the world are all 0 (or all 1)?
        Or give them random values?
        Or wrap the edges around to create a torus
        (<a href="#f:torus">Figure XXX</a>),
        or invent special update rules for edge and corner cells?
      </p>

      <figure id="f:torus">
        <img src="img/numpy/torus.png" alt="Periodic Boundary Conditions" />
      </figure>

      <p>
        The simplest solution for now is to fix the values of the boundary cells at 0,
        and only update the (N-2)&times;(N-2) cells in the interior&mdash;again,
        we can come back later and implement something more sophisticated
        once we have the basic simulation working.
        With that decision made,
        our <code>advance</code> function looks like this:
      </p>

<pre src="src/numpy/life_looping.py">
def advance(current, next):
    assert current.shape[0] == current.shape[1], \
           'Expected square universe'
    length = current.shape[0]
    next[:, :] = 0
    for i in range(1, length-1):
        for j in range(1, length-1):
            neighbors = np.sum(current[i-1:i+2, j-1:j+2])
            if current[i, j] == 1:
                if 2 &lt;= (neighbors-1) &lt;= 3:
                    next[i, j] = 1
            else:
                if neighbors == 3:
                    next[i, j] = 1
</pre>

      <p class="continue">
        The hardest part of writing this is getting the indexing right.
        We want to loop over the interior cells,
        so we use <code>range(1, length-1)</code> as the span of our loops.
        To select the 3&times;3 region around cell (i,j) we use
        <code>[i-1:i+2, j-1:j+2]</code>;
        the asymmetry (-1 but +2) comes from the fact that
        Python includes the lower bound of a range but excludes the upper bound.
        The test in the inner <code>if</code> then looks at <code>neighbors-1</code>
        instead of <code>neighbors</code>
        because we don't want to include the 1 for the cell we're checking
        in our considerations.
        We could change the inner <code>if</code> to be:
      </p>

<pre>
                if 3 &lt;= neighbors &lt;= 4:
</pre>

      <p class="continue">
        but that will confuse most readers:
        the rules mention 2 and 3, not 3 and 4,
        so we should use the former values.
      </p>

      <p>
        At this point we have a working program,
        but it breaks one of our rules:
        we're looping over the elements of the array.
        We can fix this using a function from the SciPy signal processing library
        called <code>convolve</code>.
        Convolution can be thought of as the product of two functions,
        or,
        if we're working with grids,
        as the result of combining the values in one grid
        according to the weights in another.
        To use it,
        we import the function:
      </p>

<pre src="src/numpy/life_convolve.py">
from scipy.signal import convolve
</pre>

      <p class="continue">
        and then define the weights we want around each cell:
      </p>

<pre src="src/numpy/life_convolve.py">
FILTER = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]], dtype=np.uint8)
</pre>

      <p class="continue">
        Advancing to the next time step is then as simple as:
      </p>

<pre src="src/numpy/life_convolve.py">
def advance(current, next):
    assert current.shape[0] == current.shape[1], \
           'Expected square universe'
    next[:, :] = 0
    neighbors = convolve(current, FILTER, mode='same')
    next[(current == 1) &amp; ((neighbors == 2) | (neighbors == 3))] = 1
    next[(current == 0) &amp; (neighbors == 3)] = 1
</pre>

      <p class="continue">
        (As explained <a href="#p:boolean-ops">earlier</a>,
        we have to use <code>&amp;</code> and <code>|</code>
        instead of <code>and</code> and <code>or</code>
        to combine tests on arrays.)
        This implementation isn't just shorter than our first version:
        it's also more efficient,
        since <code>convolve</code> works directly on the low-level data blocks
        inside our arrays.
        The hardest part is actually discovering that <code>convolve</code> exists,
        and figuring out that it's the tool we need for this job.
      </p>

      <div class="keypoints" id="k:life">
        <h3>Summary</h3>
        <ul>
          <li>Padding arrays with fixed elements is an easy way to implement boundary conditions.</li>
          <li><code>scipy.signal.convolve</code> applies a weighted mask to each element of an array.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

      <p class="fixme">
        Mention Pandas.
      </p>

      <p>
        Finally, always remember that you're not the first person to program with matrices.
        Always take a look at the online documentation for NumPy before writing any functions of your own.
        The library includes routines to conjugate, convolve, and correlate matrices,
        to extract diagonals, calculate FFTs, gradients, histograms, and least squares,
        and to find net present value if you're doing financial mathematics.
        It can find roots, solve sets of linear equations, and do singular value decomposition.
        These functions are all faster than anything you could easily write,
        and what's more,
        someone else has tested and debugged them.
      </p>

    </section>