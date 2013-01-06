Journal: True
Post_Id: 3426
Author: Greg Wilson
Title: Another Example of small-p Patterns
Tags: content

<p>A couple of weeks ago, I asked whether people would find an exploration of <a href="|filename|2010-06-11-counting-things.md">ways to count things</a> useful. The consensus was "yes", so I've started drawing up notes. While working on them, it occurred to me that "ways to persist things" might be just as interesting.  Some of the approaches that could be discussed are:</p>
<ol>
<li>Save a list of numbers (one per line).</li>
<li>Save a matrix using a header line to record dimensions (introducing the idea of metadata) and M values per line.</li>
<li>Save a matrix without metadata (which requires the length of the second and subsequent lines to be checked).</li>
<li>Save mixed atomic values (which gets hard when strings are allowed).</li>
<li>Saving records whose structure is known in advance (the hardest of the bunch, since this is the point where aliasing appears).</li>
<li>Saving in binary rather than ASCII.</li>
<li>Creating self-describing data (save the format at the top, then the data).</li>
</ol>
<p>What other persistence patterns do you think would be worth explaining, and why?</p>
