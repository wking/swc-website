Post_Id: 4889
Author: Matt Davis
Title: Introduction to NumPy Tutorial
Tags: tutorial

<p>Today I did a tutorial moving quickly through the basic usage of <a href="http://docs.scipy.org/doc/numpy/reference/">NumPy</a>, the essential library for doing numeric computing with Python. We covered <a href="http://docs.scipy.org/doc/numpy/reference/routines.array-creation.html">building arrays</a>; <a href="http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html">indexing</a>; array math; NumPy's<a href="http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs"> element-wise functions</a>; array <a href="http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html#array-attributes">attributes</a> and <a href="http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html#array-methods">methods</a>; <a href="http://docs.scipy.org/doc/numpy/reference/routines.random.html">random numbers</a>; <a href="http://docs.scipy.org/doc/numpy/reference/maskedarray.html">masked arrays</a>; and <a href="http://docs.scipy.org/doc/numpy/reference/routines.testing.html">array comparison</a>.</p>
<p>I presented using the <a href="http://ipython.org">IPython</a> <a href="http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html">HTML Notebook</a>. I enjoyed it because I never had to switch between a terminal and text editor, but I wonder what the people viewing thought. A nice feature of the notebook is that I can export it, both as a PDF and in the .ipynb format importable by IPython. The PDF is <a href="|filename|/files/2012/06/NumpyLesson.pdf">here</a>, and the .ipynb file <a href="https://raw.github.com/gist/2847673/2973541fd2d1209f511efbdda81c3dc6c7d7b7c9/NumpyLesson.ipynb">here</a>.</p>
<p>One thing we didn't cover was input/output. NumPy <a href="http://docs.scipy.org/doc/numpy/reference/routines.io.html">has functions</a> for <a href="http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html#numpy.loadtxt">loading data from</a>/<a href="http://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html#numpy.savetxt">saving to</a> text files, and functions for <a href="http://docs.scipy.org/doc/numpy/reference/generated/numpy.save.html#numpy.save">saving to</a>/<a href="http://docs.scipy.org/doc/numpy/reference/generated/numpy.load.html#numpy.load">loading from</a> special NumPy binary files. The latter are useful for saving intermediate results. I've <a href="http://j.mp/KP8L7P">previously discussed</a> numpy.loadtxt and numpy.genfromtxt on my <a href="http://j.mp/penandpants">personal blog</a>.</p>
<p>One question I got was for advice for people switching from Matlab. I've never really used Matlab so I can't answer that question, but I found a relevant page on scipy.org: <a href="http://www.scipy.org/NumPy_for_Matlab_Users">NumPy for Matlab Users</a>.</p>