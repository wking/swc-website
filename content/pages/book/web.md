Title: Web Programming in Python
Directory: book

    <ol class="toc">
      <li><a href="#s:history">How We Got Here</a></li>
      <li><a href="#s:formatting">Formatting Rules</a></li>
      <li><a href="#s:attributes">Attributes</a></li>
      <li><a href="#s:morehtml">More HTML</a></li>
      <li><a href="#s:processing">Processing HTML and XML</a></li>
      <li><a href="#s:search">Finding Nodes</a></li>
      <li><a href="#s:http">How the Web Works</a></li>
      <li><a href="#s:client">Getting Data</a></li>
      <li><a href="#s:server">Providing Data</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <p>
      Carla Climate is studying climate change in the Northern and Southern hemispheres.
      As part of her work,
      she wants to see whether the gap between annual temperatures in Canada and Australia
      increased during the Twentieth Century.
      The raw data she needs is available online;
      her goal is to get it,
      do her calculations,
      and then post her results so that other scientists can use them.
    </p>

    <p>
      This chapter is about how she can do that.
      More specifically,
      it's about how to fetch data from the web,
      and how to create web pages that are useful to both human beings and computers.
      What we will <em>not</em> cover is how to build interactive web applications:
      our experience has shown that all we can do in the time we have
      is show you how to create security holes,
      which we're reluctant to do.
      <span class="comment"> CC: The preceding sentence is confusing; is it entirely necessary. If so, can it be rewritten?</span>
      However,
      everything in this chapter is a prerequisite for doing that,
      and there are lots of other good tutorials available
      if you decide that's what you really need.
      <span class="comment"> CC: Do you want to point people to where they might find these?</span>
    </p>

    <section id="s:history">

      <h2>How We Got Here</h2>

      <div class="understand" id="u:history">
        <h3>Understand:</h3>
        <ul>
          <li>The difference between structured and unstructured data.</li>
          <li>The relationship between HTML and XML.</li>
        </ul>
      </div>

      <p>
        To start,
        let's have another look at the hearing tests from
        <a href="python.html">our chapter on Python programming</a>.
        The easiest way to store their <span class="comment"> CC: suggestion: those </span> results is to put them in a plain text file
        with one row for each test:
      </p>

<pre>
Date         Experimenter        Subject          Test       Score
----------   ------------        -------          -----      -----
2011-05-02   A. Binet            H. Ebbinghaus    DL-11      88%
2011-05-07   A. Binet            H. Ebbinghaus    DL-12      71%
2011-05-02   A. Binet            W. Wundt         DL-11      29%
2011-05-02   C. S. Pierce        W. Wundt         DL-11      45%
</pre>

      <p>
        This is easy for a human being to read,
        not least because it looks exactly like what
        a conscientious researcher would write in a lab notebook.
        It's a lot harder for a computer to understand, though.
        A program would have to know that the first line of the file contains column titles,
        that the second can be ignored,
        that the first field of each row thereafter should be translated from text into a date,
        that the fields after that start in particular columns
        (since the number of spaces between them is variable,
        and the number of spaces inside names can also vary&mdash;compare
        "A.&nbsp;Binet" with "C.&nbsp;S.&nbsp;Pierce"),
        and so on.
        Such a program would not be particularly hard to write,
        but having to write a new program for each set of test results
        would quickly become tedious.
      </p>

      <p>
        Now consider something a little less structured,
        like this quotation from Richard Feynman's 1965 Nobel Prize acceptance speech:
      </p>

      <blockquote>
        As a by-product of this same view,
        I received a telephone call one day at the graduate college at Princeton from Professor Wheeler,
        in which he said,
        "Feynman, I know why all electrons have the same charge and the same mass."
        "Why?"
        "Because, they are all the same electron!"
      </blockquote>

      <p>
        A lot of information is implicit in these four sentences,
        like the fact that "Wheeler" and "Feynman" are particular people,
        that "Princeton" is a place,
        that the speakers are alternating (with Wheeler speaking first),
        and so on.
        None of that is "visible" to a computer program,
        so if we had a database containing millions of documents
        and wanted to see which ones mentioned both John Wheeler
        (the physicist, not the geologist)
        and Princeton (the university, not the glacier),
        we might have to wade through a lot of false matches.
        What we need is an unambiguous way to tell a computer
        what the meanings of various words in each document are.
        <span class="comment"> CC: awkward sentence structure </span>
      </p>

      <p>
        The first major effort to tackle this problem dates back to 1969,
        when Charles Goldfarb and others at IBM created
        the <a href="glossary.html#sgml">Standard Generalized Markup Language</a>, or SGML.
        It was designed as a way of adding extra data
        to medical and legal documents so that programs could search them more accurately.
        It was a very complex specification (over 500 pages long),
        and unless you were a specialist,
        you probably didn't even know it existed:
        all you saw was the query program built on top of it.
      </p>

      <p>
        But in 1989 Tim Berners-Lee borrowed the syntax of SGML
        to create the <a href="glossary.html#html">HyperText Markup Language</a>, or HTML,
        for his new "World Wide Web".
        HTML looked superficially the same as SGML, but it was much (much) simpler:
        almost anyone could write it, so almost everyone did.
        However, HTML had a small vocabulary that users could not change or extend.
        They could say, "This is a paragraph," or, "This is a table,"
        but not, "This is a chemical formula," or, "This is a person's name."
      </p>

      <p>
        Instead of adding thousands of new terms for different application domains,
        a new standard for <em>defining</em> terms was created.
        These rules,
        called the <a href="glossary.html#xml">Extensible Markup Language</a> (XML),
        were standardized in 1998.
        They are much more complex than HTML,
        but still simpler than SGML,
        and hundreds of specialized vocabularies have now been defined in terms of XML.
      </p>

      <p>
        Just to confuse things,
        along with the XML standard
        came a new version of HTML called XHTML
        that re-defined things people were already using in strict XML terms.
        <span class="comment"> CC: Not sure you want to use phrases like "to confuse things" because it sets people up to think that the information contained within it is hard or complicated. </span>
        It never became as popular as its creators hoped,
        so yet another standard called HTML5 was created.
        It's currently a very hot topic,
        primarily because the combination of it and Javascript
        allows developers to create fancy cross-platform user interfaces.
        <span class="comment"> CC: Will your users understand what you mean by fancy, cross-platform user interfaces? </span>
        In what follows,
        though,
        we'll ignore most of that
        and concentrate on basics that haven't changed (much) in 20 years.
        <span class="comment"> CC: perhaps focus on what's going to be covered, "For our purposes here, though, we'll concentrate on some basics that haven't changed (much) in 20 years." </span>
      </p>

      <div class="keypoints" id="k:history">
        <h3>Summary</h3>
        <ul>
          <li>Structured data is much easier for machines to process than unstructured data.</li>
          <li>Markup languages like SGML, HTML, and XML can be used to add semantic information to text.</li>
        </ul>
      </div>

    </section>

    <section id="s:formatting">

      <h2>Formatting Rules</h2>

      <div class="understand" id="u:formatting">
        <h3>Understand:</h3>
        <ul>
          <li>How HTML elements are represented as text.</li>
          <li>That HTML elements must be nested to form a tree.</li>
        </ul>
      </div>

      <p>
        A basic HTML <a href="glossary.html#document">document</a>
        contains <a href="glossary.html#element">elements</a>
        and <a href="glossary.html#text">text</a>.
        (The full specification allows for many other things
        with names like "external entity references" and "processing instructions",
        but we will ignore them.)
        The text in a document is its main content.
        As far as HTML is concerned, text has no intrinsic meaning:
        "Feynman" is just seven characters,
        not a person.
      </p>

      <p>
        Elements are <a href="glossary.html#metadata">metadata</a>:
        they describe the meaning of the document's content.
        For example,
        one element might indicate a heading,
        while another might signal that its text is a cross-reference or a person's name.
        Elements usually,
        but don't always,
        contain text.
        For example,
        a caption element might contain the text,
        "Figure 9: Division by Zero".
      </p>

      <p>
        Elements are written using <a href="glossary.html#tag-xml">tags</a>,
        which must be enclosed in angle brackets <code>&lt;&hellip;&gt;</code>.
        For example, <code>&lt;cite&gt;</code> is used to mark the start of a citation,
        and <code>&lt;/cite&gt;</code> is used to mark its end.
        Elements must be properly nested:
        if an element called <code>inner</code> begins inside an element called <code>outer</code>,
        <code>inner</code> must end before <code>outer</code> ends.
        This means that <code>&lt;outer&gt;&hellip;&lt;inner&gt;&hellip;&lt;/inner&gt;&lt;/outer&gt;</code> is legal HTML,
        but <code>&lt;outer&gt;&hellip;&lt;inner&gt;&hellip;&lt;/outer&gt;&lt;/inner&gt;</code> is not.
      </p>

      <p>
        Here are some commonly-used HTML tags:
      </p>

      <table>
        <tr>
          <th>Tag</th>
          <th>Usage</th>
        </tr>
        <tr>
          <td><code>html</code></td>
          <td>Root element of entire HTML document.</td>
        </tr>
        <tr>
          <td><code>body</code></td>
          <td>Body of page (i.e., visible content).</td>
        </tr>
        <tr>
          <td><code>h1</code></td>
          <td>Top-level heading.  Use <code>h2</code>, <code>h3</code>, etc. for second- and third-level headings.</td>
        </tr>
        <tr>
          <td><code>p</code></td>
          <td>Paragraph.</td>
        </tr>
        <tr>
          <td><code>em</code></td>
          <td>Emphasized text.</td>
        </tr>
      </table>

      <p class="continue">
        And here is a simple HTML document that uses them:
      </p>

<pre>
&lt;html&gt;&lt;body&gt;&lt;h1&gt;Dimorphism&lt;/h1&gt;&lt;p&gt;Occurring or existing in two different &lt;em&gt;forms&lt;/em&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;
</pre>

      <p>
        A web browser like Firefox might present this document as:
      </p>

      <figure id="f:very_simple">
        <img src="img/web/very_simple.png" alt="A Very Simple Web Page" />
      </figure>

      <p class="continue">
        Other devices will display it differently.
        A phone,
        for example,
        might use a different background color for the heading,
        while a screen reader might read the text aloud for someone with visual disabilities.
      </p>

      <p>
        Different presentations are possible because
        HTML helps separate content from presentation,
        or in computer science terms,
        <a href="glossary.html#model">models</a> from <a href="glossary.html#view">views</a>.
        The model is the data itself;
        the view is how that data is displayed,
        such as a particular pattern of light and dark pixels on our screen
        or a particular sequence of sounds on our headphones.
        Elements tell a computer what different pieces of text mean;
        the computer can then decide what view to use to display the information.
      </p>

      <p>
        People can construct models from views almost effortlessly&mdash;if you are able to read,
        it's almost impossible <em>not</em> to see the letters "HTML"
        in the following block of text:
      </p>

<pre>
*   *  *****  *   *  *
*   *    *    ** **  *
*****    *    * * *  *
*   *    *    *   *  *
*   *    *    *   *  ****
</pre>

      <p class="continue">
        Computers,
        on the other hand,
        are very bad at reconstructing models from views.
        In fact, many of the things we do without apparent effort,
        like understanding sentences,
        are still open research problems in computer science.
        That's the real reason markup languages were invented:
        they allow us to specify semantic information&mdash;the "what" that we infer so easily&mdash;in
        ways that computers can work with.
      </p>

      <p>
        There are a few other formatting rules we need to know
        in order to create and understand documents.
        If we are writing HTML by hand
        instead of using a <a href="glossary.html#wysiwyg">WYSIWYG</a> editor,
        <span class="comment"> CC: will this be understandable to newbies?</span>
        we might lay it out like this to make it easier to read:
      </p>

<pre>
&lt;html&gt;
  &lt;body&gt;
    &lt;h1&gt;Dimorphism&lt;/h1&gt;
    &lt;p&gt;Occurring or existing in two different &lt;em&gt;forms&lt;/em&gt;.&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <p class="continue">
        Doing this doesn't change how most browsers render the document,
        since they usually ignore "extra" whitespace.
        As we'll see when we start writing programs of our own, though,
        that whitespace doesn't magically disappear when a program reads the document in,
        so at some point we have to decide what to do with it.
      </p>

      <p id="a:single-tag">
        A second formatting rule is that
        if the element doesn't contain anything,
        we can write it using the short form <code>&lt;cite/&gt;</code>
        instead of <code>&lt;cite&gt;&lt;/cite&gt;</code>.
        We'll see examples of empty elements <a href="#a:empty-element">later</a>.
        <span class="comment"> CC: perhaps explain why this shorthand method is useful to coders? </span>
      </p>

      <p>
        Finally,
        we must use <a href="glossary.html#escape-sequence">escape sequences</a>
        to represent the special characters <code>&lt;</code> and <code>&gt;</code>.
        These are just like the backslashed escape sequences we use
        to represent quotation marks in strings in programs.
      </p>

      <table>
        <tr>
          <th>Sequence</th>
          <th>Character</th>
        </tr>
        <tr>
          <td><code>&amp;lt;</code></td>
          <td><code>&lt;</code></td>
        </tr>
        <tr>
          <td><code>&amp;gt;</code></td>
          <td><code>&gt;</code></td>
        </tr>
        <tr>
          <td><code>&amp;quot;</code></td>
          <td><code>&quot;</code></td>
        </tr>
        <tr>
          <td><code>&amp;amp;</code></td>
          <td><code>&amp;</code></td>
        </tr>
      </table>

      <p>
        One final formatting rule is that
        every document must have a single <a href="glossary.html#root-element">root element</a>,
        i.e., a single element must enclose everything else.
        When combined with the rule that elements must be properly nested,
        this means that every document can be thought of as a <a href="glossary.html#tree">tree</a>.
        For example,
        we could draw the logical structure of our little document
        as shown in <a href="#f:very_simple_tree">Figure XXX</a>.
        We will use this fact when we start writing programs.
      </p>

      <figure id="f:very_simple_tree">
        <img src="img/web/very_simple_tree.png" alt="Tree View of a Very Simple Web Page" />
      </figure>

      <div class="keypoints" id="k:formatting">
        <h3>Summary</h3>
        <ul>
          <li>HTML documents contain elements and text.</li>
          <li>Elements are represented using tags.</li>
          <li>Different devices may display HTML differently.</li>
          <li>Every document must have a single root element.</li>
          <li>Tags must be properly nested to form a tree.</li>
          <li>Special characters must be written using escape sequences beginning with &amp;.</li>
        </ul>
      </div>

    </section>

    <section id="s:attributes">

      <h2>Attributes</h2>

      <div class="understand" id="u:attributes">
        <h3>Understand:</h3>
        <ul>
          <li>How to customize elements with attributes.</li>
          <li>When to use attributes rather than nested elements.</li>
        </ul>
      </div>

      <p>
        Elements can be customized by giving them <a href="glossary.html#attribute">attributes</a>.
        These are name/value pairs enclosed in the opening tag such as:
      </p>

<pre>
&lt;h1 align="center"&gt;A Centered Heading&lt;/h1&gt;
</pre>

      <p class="continue">
        or:
      </p>

<pre>
&lt;p class="disclaimer"&gt;This planet provided as-is.&lt;/p&gt;
</pre>

      <p>
        Any particular attribute name may appear at most once in any element,
        just like keys may be present at most once in a <a href="setdict.html#s:dict">dictionary</a>,
        so <code>&lt;p align="left" align="right"&gt;&hellip;&lt;/p&gt;</code> is illegal.
        Attributes' values <em>must</em> be in quotes in XML,
        but since old-style browsers accept unquoted values like <code>&lt;p align=center&gt;&hellip;&lt;p&gt;</code>,
        HTML5 allows single-word values to be unquoted.
        <span class="comment"> CC: do you want to encourage folks to always quote attributes? if so, you might want to suggest that here </span>
      </p>

      <p>
        Another similarity between attributes and dictionaries is that
        attributes are unordered.
        They have to be <em>written</em> in some order,
        just as the keys and values in a dictionary have to be displayed in some order when they are printed,
        but as far as the rules of HTML are concerned,
        the elements:
      </p>

<pre>
&lt;p align="center" class="disclaimer"&gt;This web page is made from 100% recycled pixels.&lt;/p&gt;
</pre>

      <p class="continue">
        and:
      </p>

<pre>
&lt;p class="disclaimer" align="center"&gt;This web page is made from 100% recycled pixels.&lt;/p&gt;
</pre>

      <p class="continue">
        mean the same thing.
      </p>

      <p>
        When should we use attributes, and when should we nest elements?
        As a general rule,
        we should use attributes when:
      </p>

      <ul>

        <li>
          each value can occur at most once for any element;
        </li>

        <li>
          the order of the values doesn't matter; and
        </li>

        <li>
          those values have no internal structure,
          i.e.,
          we will never need to parse an attribute's value
          in order to understand it.
        </li>

      </ul>

      <p class="continue">
        In all other cases, we should use nested elements.
        However, many widely-used XML formats break these rules
        in order to make it easier for people to write XML by hand.
        For example,
        in the Scalable Vector Graphics (SVG) format used to describe images as XML,
        we would define a rectangle as follows:
      </p>

<pre>
&lt;rect width="300" height="100" style="fill:rgb(0,0,255); stroke-width:1; stroke:rgb(0,0,0)"/&gt;
</pre>

      <p class="continue">
        In order to understand the <code>style</code> attribute,
        a program has to somehow know to split it on semicolons,
        and then to split each piece on colons.
        This quirky extra parsing wouldn't be required if the rectangle was written as:
      </p>

<pre>
&lt;rect width="300" height="100"&gt;
  &lt;fill&gt;
    &lt;red value="0"&gt;
    &lt;green value="0"&gt;
    &lt;blue value="255"&gt;
  &lt;fill&gt;
  &lt;stroke-width value="1"&gt;
  &lt;stroke&gt;
    &lt;red value="0"&gt;
    &lt;green value="0"&gt;
    &lt;blue value="0"&gt;
  &lt;stroke&gt;
&lt;rect&gt;
</pre>

      <p class="continue">
        but that's obviously a lot more work for a human being to type in (or read).
        Even then, one could argue that some "special" knowledge is required
        to translate the string <code>"0"</code> into the integer 0,
        and that this should be written something like this:
      </p>

<pre>
&lt;rect&gt;
  &lt;width type="int" value="300"/&gt;
  &lt;height type="int" value="100"/&gt;
  &lt;fill&gt;
    &lt;red type="int" value="0"/&gt;
    &lt;green type="int" value="0"/&gt;
    &lt;blue type="int" value="255"/&gt;
  &lt;/fill&gt;
  &lt;stroke-width type="int" value="1"/&gt;
  &lt;stroke&gt;
    &lt;red type="int" value="0"/&gt;
    &lt;green type="int" value="0"/&gt;
    &lt;blue type="int" value="0"/&gt;
  &lt;/stroke&gt;
&lt;/rect&gt;
</pre>

      <p class="continue">
        As always,
        designers must try to strike a balance between pragmatism and purity.
        As the airplane designer Donald Douglas once said,
        "Not everything worth doing is worth doing right."
        <span class="comment"> CC: this section is a bit confusing; what are you hoping students will understand by learning about these workarounds? </span>
      </p>

      <div class="keypoints" id="k:attributes">
        <h3>Summary</h3>
        <ul>
          <li>Elements can be customized by adding key-value pairs called attributes.</li>
          <li>An element's attributes must be unique, and are unordered.</li>
          <li>Attribute values should not have any internal structure.</li>
        </ul>
      </div>

    </section>

    <section id="s:morehtml">

      <h2>More HTML</h2>

      <div class="understand" id="u:morehtml">
        <h3>Understand:</h3>
        <ul>
          <li>That metadata should go in the document's head.</li>
          <li>How to add lists, tables, images, and links to HTML.</li>
        </ul>
      </div>

      <p>
        Well-written HTML pages have a <code>head</code> element as well as a <code>body</code>,
        and that head should contain <a href="glossary.html#metadata">metadata</a> about the page.
        The most common element inside <code>head</code> is <code>title</code>,
        which,
        as its name suggests,
        gives the page's title.
        Another common item is <code>meta</code>,
        whose two attributes <code>name</code> and <code>content</code>
        allow authors to embed arbitrary information in their pages.
        If we add these to the web page we wrote earlier,
        we might have:
      </p>

<pre>
&lt;html&gt;
  &lt;head&gt;
    &lt;title&gt;Dimorphism Defined&lt;title&gt;
    &lt;meta name="author" content="Alan Turing"/&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;Dimorphism&lt;/h1&gt;
    &lt;p&gt;Occurring or existing in two different &lt;em&gt;forms&lt;/em&gt;.&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <p class="continue">
        The text "Dimorphism Defined" does not show up anywhere in the web page,
        but most browsers will display it the title bar,
        and search engines use it
        and the information in <code>meta</code> elements
        to figure out what the page is about.
      </p>

      <p id="p:hide-paragraph">
        Well-written pages also use comments (just like code).
        These start with <span class="comment">, and end with, </span> <code>&lt;!--</code>, and end with <code>--&gt;</code>,
        and cannot be nested
        (which means that commenting out a region that already includes a commented-out region
        may have unexpected consequences).
        Well-written pages do <em>not</em> put content in comments&mdash;not even
        content that isn't supposed to be displayed,
        since programs may or may not have access to such material.
        A better way to hide something is to tell the browser not to display it:
      </p>

<pre src="src/web/hide_paragraph.html">
&lt;html&gt;
  &lt;body&gt;
    &lt;p&gt;this is visible&lt;/p&gt;
    &lt;p style="display:none"&gt;this is not&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <img src="img/web/hide_paragraph.png" alt="Hiding a Paragraph"/>

      <p class="continue">
        An even better way is to use Cascading Style Sheets, or CSS,
        which we will discuss in the <a href="ref.html#s:css">appendix</a>.
        Before then,
        though,
        let's look at a few more things we can put in our documents.
      </p>

      <p>
        HTML provides two kinds of lists:
        <code>ul</code> to mark an unordered (bulleted) list,
        and <code>ol</code> for an ordered (numbered) one.
        Items inside either kind of list must be wrapped in <code>li</code> elements:
      </p>

<pre src="src/web/nested_lists.html">
&lt;html&gt;
  &lt;body&gt;
    &lt;ul&gt;
      &lt;li&gt;A. Binet
        &lt;ol&gt;
          &lt;li&gt;H. Ebbinghaus&lt;/li&gt;
          &lt;li&gt;W. Wundt&lt;/li&gt;
        &lt;/ol&gt;
      &lt;/li&gt;
      &lt;li&gt;C. S. Pierce
        &lt;ol&gt;
          &lt;li&gt;W. Wundt&lt;/li&gt;
        &lt;/ol&gt;
      &lt;/li&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <figure id="f:nested_lists">
        <img src="img/web/nested_lists.png" alt="Nested Lists"/>
      </figure>

      <p class="continue">
        Note how elements are nested:
        since the ordered lists "belong" to the unordered list items above them,
        they are inside those items' <code>&lt;li&gt;&hellip;&lt;/li&gt;</code> tags.
      </p>

      <p>
        HTML also provides tables, but they are awkward to use:
        tables are naturally two-dimensional,
        but text is one-dimensional.
        (Things get even worse when we have split columns and multi-row items.)
        <span class="comment"> CC: Again, not sure that you want to introduce the idea of things getting worse or being complicated </span>
        The <code>table</code> element marks the table itself;
        within that,
        each row is wrapped in <code>tr</code> (for "table row"),
        and within those,
        column items are wrapped in <code>th</code> (for "table heading")
        or <code>td</code> (for "table data"):
      </p>

<pre src="src/web/simple_table.html">
&lt;html&gt;
  &lt;body&gt;
    &lt;table&gt;
      &lt;tr&gt;
        &lt;th&gt;&lt;/th&gt;
        &lt;th&gt;A. Binet&lt;/th&gt;
        &lt;th&gt;C. S. Pierce&lt;/th&gt;
      &lt;/tr&gt;
      &lt;tr&gt;
        &lt;th&gt;H. Ebbinghaus&lt;/th&gt;
        &lt;td&gt;88%&lt;/td&gt;
        &lt;td&gt;NA&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr&gt;
        &lt;th&gt;W. Wundt&lt;/th&gt;
        &lt;td&gt;29%&lt;/td&gt;
        &lt;td&gt;45%&lt;/td&gt;
      &lt;/tr&gt;
    &lt;/table&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <figure id="f:simple_table">
        <img src="img/web/simple_table.png" alt="A Simple Table" />
      </figure>

      <p>
        Tables are sometimes used to do multi-column layout,
        as well as for tabular data,
        but this is a bad idea.
        To understand why,
        consider two other HTML tags:
        <code>i</code>, meaning "italics",
        and <code>em</code>, meaning "emphasis".
        The former directly controls how text is displayed,
        but by doing so,
        it breaks the separation between model and view that is the heart of markup's usefulness.
        Without understanding the text that has been italicized,
        a program cannot understand whether it is meant to indicate someone shouting,
        the definition of a new term,
        or the title of a book.
        The <code>em</code> tag, on the other hand, has exactly one meaning,
        and that meaning is different from the meaning of <code>dfn</code> (a definition)
        or <code>cite</code> (a citation).
      </p>

      <p>
        HTML pages can also contain images.
        (In fact,
        the World Wide Web didn't really take off until
        the Mosaic browser allowed people to mix graphics with text.)
        The word "contain" is actually misleading, though:
        HTML documents can only contain text,
        so we cannot store an image "in" a page.
        Instead,
        we must put it in some other file,
        and insert a reference to that file in the HTML using the <code>img</code> tag.
        Its <code>src</code> attribute specifies where to find the image file;
        this can be a path to a file on the same host as the web page,
        or a URL for something stored elsewhere.
      </p>

<pre src="src/web/simple_image.html">
&lt;html&gt;
  &lt;body&gt;
    &lt;p&gt;My daughter's first online chat:&lt;/p&gt;
    &lt;img src="madeleine.jpg"/&gt;
    &lt;p&gt;but probably not her last.&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <figure id="f:simple_image">
        <img src="img/web/simple_image.png" alt="Simple Images" />
      </figure>

      <p>
        Whenever we refer to an image,
        we should use the <code>img</code> tag's <code>alt</code> attribute
        to provide a title or description of the image.
        This is what screen readers for people with visual handicaps will say aloud to "display" the image,
        and it helps search engines find things.
        Adding this to our previous example gives:
      </p>

<pre>
&lt;html&gt;
  &lt;body&gt;
    &lt;p&gt;My daughter's first online chat:&lt;/p&gt;
    &lt;img src="madeleine.jpg" <span class="highlight">alt="Madeleine's first online chat"</span>/&gt;
    &lt;p&gt;but probably not her last.&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <p class="continue" id="a:empty-element">
        Notice, by the way, that the <code>img</code> element is written as
        <code>&lt;img&hellip;/&gt;</code>,
        i.e.,
        as a <a href="#a:single-tag">single tag</a> rather than separate opening and closing tags.
        This makes sense because the element doesn't contain any text:
        the content is referred to by its <code>src</code> attribute.
      </p>

      <p>
        Finally, the links within and between pages are what make HTML "hypertext".
        We create links using the <code>a</code> element.
        Whatever is inside the element is displayed and (usually) underlined for clicking.
        This is usually a few words text,
        but it can also be an entire paragraph,
        a table,
        or an image.
        <span class="comment"> CC: here's an opportunity to discuss future ways of addressing presentation, e.g., removing underlining, changing link colors, css, etc.</span>
      </p>

      <p>
        The <code>a</code> element's <code>href</code> attribute
        specifies what the link is pointing at.
        This can be either a local filename or a URL.
        For example,
        we can create a listing of the examples we've written so far like this:
      </p>

<pre src="src/web/simple_listing.html">
&lt;html&gt;
  &lt;body&gt;
    &lt;p&gt;
      Simple HTML examples for
      &lt;a href="http://software-carpentry.org"&gt;Software Carpentry&lt;/a&gt;.
    &lt;/p&gt;
    &lt;ol&gt;
      &lt;li&gt;&lt;a href="very-simple.html"&gt;a very simple page&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href="hide-paragraph.html"&gt;hiding paragraphs&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href="nested-lists.html"&gt;nested lists&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href="simple-table.html"&gt;a simple table&lt;/a&gt;&lt;/li&gt;
      &lt;li&gt;&lt;a href="simple-image.html"&gt;a simple image&lt;/a&gt;&lt;/li&gt;
    &lt;/ol&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <figure id="f:simple_listing">
        <img src="img/web/simple_listing.png" alt="Using Hyperlinks" />
      </figure>

      <p>
        The hyperlink element is called <code>a</code> because it is also used
        to create <a href="glossary.html#anchor">anchors</a> in documents
        by giving them a <code>name</code> attribute instead of an <code>href</code>.
        An anchor is simply a location in a document that can be linked to.
        For example,
        suppose we formatted the Feynman quotation given earlier like this:
      </p>

<pre>
&lt;blockquote&gt;
  As a by-product of this same view, I received a telephone call one day
  at the graduate college at &lt;a name="pu"&gt;Princeton&lt;/a&gt;
  from Professor Wheeler, in which he said,
  "Feynman, I know why all electrons have the same charge and the same mass."
  "Why?"
  "Because, they are all the same electron!"
&lt;/blockquote&gt;
</pre>

      <p class="continue">
        If this quotation was in a file called <code>quote.html</code>,
        we could then create a hyperlink directly to the mention of Princeton
        using <code>&lt;a&nbsp;href="quote.html#pu"&gt;</code>.
        The <code>#</code> in the <code>href</code>'s value separates the path to the document
        from the anchor we're linking to.
        Inside <code>quote.html</code> itself,
        we could link to that same location simply using
        <code>&lt;a&nbsp;href="#pu"&gt;</code>.
      </p>

      <p>
        Using the <code>a</code> element for both links and targets was poor design&mdash;programs
        are simpler to write if each element has one purpose, and one alone&mdash;but
        we're stuck with it now.
        A more modern way to create anchors is to add an <code>id</code> attribute
        to some other element.
        For example,
        if we wanted to be able to link to the quotation itself,
        we could write:
      </p>

<pre>
&lt;blockquote <span class="highlight">id="wheeler-electron-quote"</span>&gt;
  As a by-product of this same view, I received a telephone call one day
  at the graduate college at &lt;a name="pu"&gt;Princeton&lt;/a&gt;
  from Professor Wheeler, in which he said,
  "Feynman, I know why all electrons have the same charge and the same mass."
  "Why?"
  "Because, they are all the same electron!"
&lt;/blockquote&gt;
</pre>

      <p class="continue">
        and then refer to <code>quote.html#wheeler-electron-quote</code>.
        Of course
        this only works if what we want to link to
        is already wrapped in some element or other;
        if we really do want to jump into the middle of a paragraph,
        we can wrap the target text in a <code>span</code> element,
        which by default has no effect on display.
        <span class="comment"> CC: perhaps provide more information about the span element here so the student can parse this adequately</span>
      </p>

      <div class="keypoints" id="k:morehtml">
        <h3>Summary</h3>
        <ul>
          <li>Put metadata in <code>meta</code> elements in a page's <code>head</code> element.</li>
          <li>Use <code>ul</code> for unordered lists and <code>ol</code> for ordered lists.</li>
          <li>Add comments to pages using <code>&lt;!--</code> and <code>--&gt;</code>.</li>
          <li>Use <code>table</code> for tables, with <code>tr</code> for rows and <code>td</code> for values.</li>
          <li>Use <code>img</code> for images.</li>
          <li>Use <code>a</code> to create hyperlinks.</li>
          <li>Give elements a unique <code>id</code> attribute to link to it.</li>
        </ul>
      </div>

    </section>

    <section id="s:processing">

      <h2>Processing HTML and XML</h2>

      <div class="understand" id="u:processing">
        <h3>Understand:</h3>
        <ul>
          <li>How the Document Object Model represents HTML and XML.</li>
          <li>How to construct a document in memory and then convert it to text.</li>
        </ul>
      </div>

      <p>
        The standard way to represent XML and HTML in a program is called
        the <a href="glossary.html#document-object-model">Document Object Model</a> (DOM).
        It creates a <a href="glossary.html#tree">tree</a>
        containing one node for each element, attribute, or block of text.
        For historical reasons,
        Python's standard library includes several libraries that implement the DOM;
        we'll use the simpler one, called <code>ElementTree</code>.
        With it,
        the tree representing our web page about dimorphism
        looks like <a href="#f:dimorphism_tree">Figure XXX</a>.
      </p>

      <figure id="f:dimorphism_tree">
        <img src="img/web/dimorphism_tree.png" alt="Tree Representation of Dimorphism Page" />
      </figure>

      <p>
        There are basically two ways to create a tree like this:
        parse a string (or file) containing XML,
        or build the nodes one by one and put them together manually.
        The former is more common,
        since the usual way to store and exchange XML or HTML is as text.
        Programs often use the latter to create data for output,
        and then convert the tree to text for storage or exchange.
      </p>

      <p>
        Let's start by turning text into HTML, and then back into text:
      </p>

<pre src="src/web/parse_simple_page.py">
import xml.etree.ElementTree as ET

page = '''&lt;html&gt;
  &lt;body&gt;
    &lt;h1&gt;Dimorphism&lt;/h1&gt;
    &lt;p class="definition"&gt;Occurring or existing in two different &lt;u&gt;forms&lt;/u&gt;.&lt;/p&gt;
    &lt;p&gt;
      The most notable form is sexual dimorphism,
      in which males and females have noticeably different appearances.
    &lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;'''

doc = ET.fromstring(page)
text = ET.tostring(doc, 'utf-8')
print text
</pre>

      <p class="continue">
        We start by importing the <code>xml.etree.ElementTree</code> library
        and giving it the alias <code>ET</code>
        (which is a lot easier to type and read).
        The multi-line string assigned to the variable <code>page</code>
        is the "document" we will parse.
        Parsing itself takes just a single call to <code>ET.fromstring</code>;
        it returns the root node of the DOM tree corresponding to that document.
        We then convert that tree back to text by calling <code>ET.tostring</code>.
        The <code>'utf-8'</code> argument specifies how we want characters represented;
        we discuss this elsewhere.
        <span class="comment"> CC: link to where else discussed?</span>
      </p>

      <p>
        The program's output is:
      </p>

<pre><span class="out">&lt;html&gt;
  &lt;body&gt;
    &lt;h1&gt;Dimorphism&lt;/h1&gt;
    &lt;p class="definition"&gt;Occurring or existing in two different &lt;u&gt;forms&lt;/u&gt;.&lt;/p&gt;
    &lt;p&gt;
      The most notable form is sexual dimorphism,
      in which males and females have noticeably different appearances.
    &lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;</span>
</pre>

      <p class="continue">
        which is exactly what we started with.
      </p>

      <p>
        Now let's build the dimorphism document by hand:
      </p>

<pre src="src/web/build_simple_page.py">
import xml.etree.ElementTree as ET

root = ET.Element('html')

body = ET.Element('body')
root.append(body)

title = ET.SubElement(body, 'h1')
title.text = 'Dimorphism'

p1 = ET.SubElement(body, 'p')
p1.text = 'Occurring or existing in two different '
u = ET.SubElement(p1, 'u')
u.text = 'forms'
p1.tail = '.'

long_text = '''The most notable form is sexual dimorphism,
in which males and females have noticeably different appearances.'''
ET.SubElement(body, 'p').text = long_text

print ET.tostring(root)
</pre>

      <p>
        There's much less to this program than first appears.
        It starts by creating an object of type <code>Element</code>,
        which is the class the ElementTree library uses to represent nodes.
        The argument to <code>Element</code>'s constructor,
        <code>html</code>,
        specifies the element's type.
      </p>

      <p>
        The next two lines create another node of type <code>body</code>
        and then append that to the root node.
        At this point, our tree looks like
        <a href="#f:partial_tree">Figure XXX</a>:
      </p>

      <figure id="f:partial_tree">
        <img src="img/web/partial_tree.png" alt="Partially-Constructed Tree" />
      </figure>

      <p>
        The rest of the program does little more than create and append nodes.
        Because creating a node and appending it to another one is so common,
        ElementTree provides a convenience function called <code>SubElement</code>
        which combines the two steps.
        The two lines:
      </p>

<pre>
title = ET.SubElement(body, 'h1')
title.text = 'Dimorphism'
</pre>

      <p class="continue">
        create a new node of type <code>h1</code>,
        append it to the <code>body</code> node,
        and then set the text content of the title node to be the string <code>'Dimorphism'</code>.
      </p>

      <p>
        The next step is the most complicated.
        We need to create a paragraph node
        whose <code>class</code> attribute has the value <code>definition</code>,
        and which contains three things:
      </p>

      <ol>

        <li>
          the text <code>'Occurring or existing in two different&nbsp;'</code>
          (with a space at the end);
        </li>

        <li>
          a <code>u</code> element containing the text <code>'forms'</code>;
          and
        </li>

        <li>
          another piece of text containing the period '.' that ends the sentence.
        </li>

      </ol>

      <p>
        Creating the paragraph node and appending it to our body node is easy:
        we just call <code>SubElement</code>.
        Setting an attribute is also easy:
        every node has a dictionary called <code>attrib</code>
        whose keys are attribute names
        and whose values are those attributes' values.
        The single line:
      </p>

<pre>
p1.attrib['class'] = 'definition'
</pre>

      <p class="continue">
        therefore creates the attribute we want.
      </p>

      <p>
        Now for the paragraph's content.
        The first part is easy: we just set <code>p1.text</code>.
        And underlining the word "forms" is easy too:
        we create a node of type <code>u</code> and append it to the paragraph.
        But where should the closing period be stored?
      </p>

      <p>
        Along with <code>text</code>,
        ElementTree nodes have another text field called <code>tail</code>,
        which stores the text <em>after</em> the node
        but before the start of anything else.
        Since the period is in the paragraph,
        the right place to store it is therefore <code>u.tail</code>
        (since putting it in <code>p1.tail</code> would imply that
        it came after the end of the first paragraph,
        but before the start of the next paragraph).
      </p>

      <p>
        Finally,
        we create the second paragraph that elaborates dimorphism's definition
        by combining node creation and text setting in a single line:
      </p>

<pre>
ET.SubElement(body, 'p').text = long_text
</pre>

      <p class="continue">
        This works because <code>SubElement</code> returns the node it just created,
        so we can immediately set its <code>text</code> value.
      </p>

      <figure id="f:final_tree">
        <img src="img/web/final_tree.png" alt="Final Tree" />
      </figure>

      <p>
        In memory,
        our document is now something like <a href="#f:final_tree">Figure XXX</a>.
        If we convert it to text,
        we get:
      </p>

<pre>
<span class="out">&lt;html&gt;&lt;body&gt;&lt;h1&gt;Dimorphism&lt;/h1&gt;&lt;p class="definition"&gt;Occurring or existing in two&crarr;
different &lt;u&gt;forms&lt;/u&gt;.&lt;/p&gt;&lt;p&gt;The most notable form is sexual dimorphism,
in which males and females have noticeably different appearances.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</span>
</pre>

      <p class="continue">
        (As before, we use &crarr; to break a line that's too long to fit on the screen.)
        This has all the content we created,
        but <em>only</em> that content.
        We didn't create text nodes containing carriage returns and blanks,
        so <code>tostring</code> didn't insert them.
        Most machine-generated XML isn't nicely indented
        because computers don't care,
        but XML intended for human beings to read usually is.
      </p>

      <p>
        There is another reason why what we see might not be what we created.
        Here's another simple program that converts text to a node tree and back:
      </p>

<pre src="src/web/round_trip.py">
import xml.etree.ElementTree as ET

original = '''&lt;root&gt;&lt;node
                     front="1"
                     back="2"&gt;content&lt;/node&gt;&lt;/root&gt;'''


doc = ET.fromstring(original)
print ET.tostring(doc, 'utf-8')
<span class="out">&lt;root&gt;&lt;node back="2" front="1"&gt;content&lt;/node&gt;&lt;/root&gt;</span>
</pre>

      <p class="continue">
        <code>node</code>'s attributes are all on one line in the output,
        and in a different order than they were in the input.
        The reason for the first difference is that XML ignores whitespace inside elements:
        the parser simply throws away
        the extra spaces and newlines inside the definition of <code>&lt;node&hellip;&gt;</code>.
        The reason for the second is that attributes are treated as a dictionary,
        and dictionary keys are unordered.
        As far as the rules of XML are concerned,
        the input and output are the same thing.
        Unfortunately,
        as far as string comparison and tools like <code>diff</code> are concerned,
        they are not.
      </p>

      <p>
        Our example may make building trees seem like a lot of work,
        but in practice,
        programs almost always wrap the steps up in a few functions.
        For example,
        here's a function that converts a Python list into an HTML ordered list:
      </p>

<pre src="src/web/list_to_ol.py">
import xml.etree.ElementTree as ET

def convert(values):
    '''Convert a list of values to an &lt;ol&gt; list.'''

    result = ET.Element('ol')
    for v in values:
        ET.SubElement(result, 'li').text = str(v)
    return result

root = convert([1, "two", 3.4])
print ET.tostring(root)
<span class="out">&lt;ol&gt;&lt;li&gt;1&lt;/li&gt;&lt;li&gt;two&lt;/li&gt;&lt;li&gt;3.4&lt;/li&gt;&lt;/ol&gt;</span>
</pre>

      <div class="keypoints" id="k:processing">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>xml.etree.ElementTree</code> to parse HTML and XML and manipulate it in memory.</li>
          <li>Use the same library to create elements in memory rather than concatenating and printing strings.</li>
          <li>An element's <code>text</code> property stores the text it contains.</li>
          <li>An element's <code>tail</code> property stores the text that comes immediately after it.</li>
        </ul>
      </div>

    </section>

    <section id="s:search">

      <h2>Finding Nodes</h2>

      <div class="understand" id="u:search">
        <h3>Understand:</h3>
        <ul>
          <li>How to find DOM elements using XPath.</li>
        </ul>
      </div>

      <p>
        Most databases are read more often than they're written,
        so most of <a href="db.html">our discussion of SQL</a>
        focuses on finding things.
        Most web pages are read more than once too,
        so tools like the ElementTree library provide tools for locating nodes of interest.
        The most important of these is the <code>findall</code> method,
        which searches all the children of a node
        to find things that match a pattern.
        For example,
        if some molecular formulas are stored like this:
      </p>

<pre src="src/web/molecular_formulas.xml">
&lt;formulas&gt;
  &lt;formula name="ammonia"&gt;
    &lt;atom symbol="N" number="1"/&gt;
    &lt;atom symbol="H" number="3"/&gt;
  &lt;/formula&gt;
  &lt;formula name="water"&gt;
    &lt;atom symbol="H" number="2"/&gt;
    &lt;atom symbol="O" number="1"/&gt;
  &lt;/formula&gt;
  &lt;formula name="methanol"&gt;
    &lt;atom symbol="C" number="1"/&gt;
    &lt;atom symbol="O" number="1"/&gt;
    &lt;atom symbol="H" number="4"/&gt;
  &lt;/formula&gt;
&lt;/formulas&gt;
</pre>

      <p class="continue">
        then this program will count how many formulas there are:
      </p>

<pre src="src/web/count_formulas.py">
import sys
import xml.etree.ElementTree as ET

doc = ET.parse(sys.argv[1])
root = doc.getroot()
formulas = root.findall("./formula")
print len(formulas)
<span class="out">3</span>
</pre>

      <p>
        The key to this programs is <code>root.findall("./formula")</code>.
        The pattern <code>"./formula"</code> means,
        "Starting with this node ('.'),
        examine its children ('/')
        for elements with the tag 'formula."
        The result of the <code>findall</code> call is a list of nodes that match.
      </p>

      <p>
        The mini-language used for patterns is called
        <a href="glossary.html#xpath">XPath</a>.
        Some common XPath expressions are:
      </p>

      <table>
        <tr>
          <td>
            <code>tag</code>
          </td>
          <td>
            All immediate children with the given tag.
            <code>"formula"</code> selects all child <code>formula</code> elements,
            and <code>"formula/atom"</code> selects all <code>atom</code> elements
            that are children of <code>formula</code> children.
          </td>
        </tr>
        <tr>
          <td>
            <code>*</code>
          </td>
          <td>
            All child elements.
            <code>"*/atom"</code> selects all grandchild <code>atom</code> elements,
            regardless of what the intervening parent is.
          </td>
        </tr>
        <tr>
          <td>//</td>
          <td>
            All subelements on all levels beneath the current element.
            <code>".//atom"</code> selects all <code>atoms</code> elements in the entire tree.
          </td>
        </tr>
        <tr>
          <td><code>.</code></td>
          <td>
            The current node.
            It is mostly used at the beginning of a path to indicate that it is a relative path.
          </td>
        </tr>
        <tr>
          <td><code>..</code></td>
          <td>The parent element.</td>
        </tr>
        <tr>
          <td><code>[@attrib]</code></td>
          <td>
            All elements with the given attribute (regardless of that attribute's value).
            <code>'.//atom[@name]'</code> selects all atoms in the tree
            that have a <code>name</code> attribute,
            but not any <code>atom</code> elements that are missing that attribute.
          </td>
        </tr>
        <tr>
          <td>
            <code>[@attrib="value"]</code>
          </td>
          <td>
            All elements for which the given attribute has the given value.
            <code>'.//atom[@symbol="C"]'</code> finds all carbon atoms.
          </td>
        </tr>
        <tr>
          <td>
            <code>[tag]</code>
          </td>
          <td>
            All elements that have a child element with the given tag.
            <code>'atom[comment]</code>' finds all <code>atom</code> nodes
            that have an immediate child of type <code>comment</code>.
          </td>
        </tr>
        <tr>
          <td>
            <code>[position]</code>
          </td>
          <td>
            All elements that located in the given position relative to their parent.
            The position can be either an integer (1 is the first position),
            the expression <code>last()</code> for the last position,
            or a position relative to <code>last()</code>,
            such as <code>last()-1</code>.
          </td>
        </tr>
      </table>

      <p>
        We can use these expressions to find all the <code>atom</code> nodes
        that are <em>not</em> immediate children of <code>formula</code> nodes.
      </p>

<pre src="src/web/validate_doc.py">
import xml.etree.ElementTree as ET

source = '''&lt;formulas&gt;
  &lt;formula name="ammonia"&gt;
    &lt;atom symbol="N" number="1"/&gt;
    &lt;atom symbol="H" number="3"/&gt;
  &lt;/formula&gt;
  &lt;atom symbol="H" number="2"/&gt;       <span class="comment">&lt;!-- mistake! --&gt;</span>
  &lt;formula name="water"&gt;
    &lt;atom symbol="O" number="1"&gt;
      &lt;atom symbol="H" number="2"/&gt;   <span class="comment">&lt;!-- another mistake --&gt;</span>
    &lt;/atom&gt;
  &lt;/formula&gt;
&lt;/formulas&gt;'''

doc = ET.fromstring(source)
all_atoms = doc.findall('.//atom')
proper_atoms = doc.findall('.//formula/atom')
wrongly_placed = set(all_atoms) - set(proper_atoms)
for atom in wrongly_placed:
    print ET.tostring(atom)
<span class="out">&lt;atom number="2" symbol="H" /&gt;

&lt;atom number="2" symbol="H" /&gt;

</span>
</pre>

      <p class="continue">
        After converting the XML document to a tree,
        this program uses <code>doc.findall</code> to get all of the <code>atom</code> nodes,
        and then uses it again to find all the <code>atom</code> nodes
        that are immediate children of <code>formula</code> nodes.
        Subtracting the second set from the first
        gives the nodes that are <em>not</em> immediate children of <code>formula</code> nodes,
        i.e.,
        that are in the wrong place.
        The loop at the end then prints them out.
      </p>

      <p>
        A couple of things are worth pointing out about this program.
        First,
        the ElementTree library doesn't record where in the document nodes are from,
        so we can't pinpoint the line or character position of the offending nodes.
        Second,
        the double-spacing on the output comes from the fact that
        our original document contained lots of whitespace
        to make it easier for human beings to read,
        and ElementTree kept this whitespace
        (storing it as the <code>tail</code> value for various nodes).
        This kind of extra whitespace is always an annoyance when we're programming,
        so it's tempting to leave it out.
        However,
        doing so makes it harder for human beings to read the raw XML
        using line-oriented editors.
        Most modern browsers will display the XML as a tree
        (<a href="#f:xml_in_browser">Figure XXX</a>)
        but native XML-oriented editing tools are still clumsy.
      </p>

      <figure id="f:xml_in_browser">
        <img src="img/web/xml_in_browser.png" alt="XML in the Browser" />
      </figure>

      <div class="keypoints" id="k:search">
        <h3>Summary</h3>
        <ul>
          <li>Use XPath expressions to identify nodes in a document.</li>
          <li>Use a node's <code>findall</code> method to find children matching an XPath expression.</li>
        </ul>
      </div>

    </section>

    <section id="s:http">

      <h2>How the Web Works</h2>

      <div class="understand" id="u:http">
        <h3>Understand:</h3>
        <ul>
          <li>The difference between client-server and peer-to-peer architectures.</li>
          <li>What IP addresses, host names, and sockets are.</li>
          <li>HTTP's request-response cycle.</li>
          <li>What HTTP requests and responses contain.</li>
        </ul>
      </div>

      <p>
        Now that we understand the web's most common data format,
        it's time to look at how data is moved around on the web.
        Broadly speaking,
        web applications are built in one of two ways.
        A <a href="glossary.html#client-server-architecture">client/server architecture</a>
        is one in which many <a href="glossary.html#client">clients</a>
        communicate with a central <a href="glossary.html#server">server</a>
        (<a href="#f:client_server">Figure XXX</a>).
        This model is asymmetric:
        clients ask for things,
        and servers provide them.
        Web browsers and web servers like Apache are the best-known example of this model,
        but many <a href="shell.html#a:dbms">database management systems</a> are also servers.
      </p>

      <figure id="f:client_server">
        <img src="img/web/client_server.png" alt="Client-Server Architecture" />
      </figure>

      <p>
        In contrast,
        a <a href="glossary.html#peer-to-peer-architecture">peer-to-peer architecture</a>
        is one in which all processes exchange information equally
        (<a href="#f:peer_to_peer">Figure XXX</a>).
        This is symmetric,
        in that every participant both provides and receives data;
        the best-known example is probably filesharing systems like BitTorrent,
        but again,
        there are many others.
        Peer-to-peer systems are generally harder to design than client-server systems,
        but they are also more resilient.
        If a centralized web server fails,
        the whole system goes down,
        while if one node in a filesharing network goes down,
        the rest can (usually) carry on.
      </p>

      <figure id="f:peer_to_peer">
        <img src="img/web/peer_to_peer.png" alt="Peer-to-Peer Architecture" />
      </figure>

      <p>
        Under the hood,
        both kinds of systems
        (and pretty much every other networked application)
        run on a layered family of standards called
        <a href="glossary.html#internet-protocol">Internet Protocol</a> (IP).
        IP works by breaking messages down into small <a href="glossary.html#packet">packets</a>,
        each of which is forwarded from one machine to another
        along any available route
        until it reaches its destination
        (<a href="#f:packets">Figure XXX</a>).
      </p>

      <figure id="f:packets">
        <img src="img/web/packets.png" alt="Packet-Based Communication" />
      </figure>

      <p>
        The only layer in IP that concerns us is
        the <a href="glossary.html#tcp">Transmission Control Protocol</a> layer.
        TCP/IP guarantees that every packet we send is received,
        and that packets are received in the right order.
        Putting it another way,
        it provides a reliable stream of data from one place to another,
        so that sending data between computers looks as much as possible
        like reading and writing files.
      </p>

      <p>
        Programs using IP communicate through <a href="glossary.html#socket">sockets</a>.
        Each socket is one end of a point-to-point communication channel,
        and provides the same kind of read and write operations as files
        (<a href="#f:socket">Figure XXX</a>).
      </p>

      <figure id="f:socket">
        <img src="img/web/socket.png" alt="Sockets" />
      </figure>

      <p>
        A socket's <a href="glossary.html#host-address">host address</a>
        or <a href="glossary.html#ip-address">IP address</a>
        identifies a particular machine on the network.
        This address consists of four 8-bit numbers,
        such as <code>208.113.154.118</code>.
        The <a href="glossary.html#dns">Domain Name System</a> (DNS)
        matches these numbers to symbolic names
        like <code>"software-carpentry.org"</code>.
        If we want,
        we can use tools like <code>nslookup</code> to query DNS directly:
      </p>

<pre>
$ <span class="in">nslookup software-carpentry.org</span>
<span class="out">Server:  admin1.private.tor1.mozilla.com
Address:  10.242.75.5

Non-authoritative answer:
Name:    software-carpentry.org
Address:  173.236.199.157</span>
</pre>

      <p>
        A socket's <a href="glossary.html#port">port number</a>
        is just a number in the range 0-65535
        that uniquely identifies the socket on the host machine.
        (If the IP address is like a company's phone number,
        then the port number is like an extension number.)
        Ports 0-1023 are reserved for the operating system's use;
        anyone else can use the remaining ports.
      </p>

      <figure id="f:sockets">
        <img src="img/web/sockets.png" alt="Sockets"/>
      </figure>

      <p>
        The <a href="glossary.html#http">Hypertext Transfer Protocol</a> (HTTP)
        specifies how programs exchange documents over the World Wide Web.
        Originally,
        the communicating parties were usually web browsers and web servers,
        but these days HTTP is used in many other creative ways.
        In principle,
        HTTP communication is simple:
        the client sends a request specifying what it wants over a socket connection,
        and the server sends some data in response.
        (or an error message).
        The data may be HTML copied from a file on disk
        or generated dynamically by a program,
        an image,
        or just about anything else
        (<a href="#f:http_content">Figure XXX</a>).
      </p>

      <figure id="f:http_content">
        <img src="img/web/http_content.png" alt="HTTP Content" />
      </figure>

      <p>
        The most important thing about HTTP is
        that it is <a href="glossary.html#stateless-protocol">stateless</a>.
        The server doesn't automatically store any state,
        i.e.,
        it doesn't remember anything between requests:
        each connection and request is handled on its own.
        If an application wants to keep track of things between requests
        (such as the user's identity),
        it's the application's job to do it.
      </p>

      <figure id="f:http_cycle">
        <img src="img/web/http_cycle.png" alt="HTTP Request Cycle"/>
      </figure>

      <figure id="f:http_request">
        <img src="img/web/http_request.png" alt="HTTP Request"/>
      </figure>

      <p>
        An HTTP request has three parts
        (<a href="#f:http_request">Figure XXX</a>).
        The HTTP method is almost always either
        <code>"GET"</code> (to fetch information)
        or
        <code>"POST"</code> (to submit form data or upload files).
        The URL identifies the thing the request wants;
        it may be a path to a file on disk,
        such as <code>/index.html</code>,
        but it's entirely up to the server how to interpret the URL.
        The HTTP version is usually <code>"HTTP/1.0"</code> or <code>"HTTP/1.1"</code>;
        the differences between the two don't matter to us.
      </p>

      <div class="box">
        <h3>The Internet vs. the Web</h3>

        <p>
          A lot of people use these two terms synonymously,
          but they're actually very different things.
          The Internet is a network of networks
          that allows (almost) any computer to communicate with (almost) any other.
          That communication can be email,
          File Transfer Protocol (FTP),
          streaming video,
          or any of a hundred other things.
        </p>

        <p>
          The World-Wide Web,
          on the other hand,
          is just one particular way to share data on top of
          the kind of network that the Internet provides.
          Originally,
          the web only allows people to view documents in browsers,
          but its HTTP protocol has been used to do many other things since
          (such as instant messaging and gaming).
        </p>

      </div>

      <p>
        An <a href="glossary.html#http-header">HTTP header</a> is a key/value pair,
        such as the three shown below:
      </p>

<pre>
Accept: text/html
Accept-Language: en, fr
If-Modified-Since: 16-May-2005
</pre>

      <p class="continue">
        A key may appear any number of times,
        so that (for example)
        a request can specify that it's willing to accept several types of content.
      </p>

      <p>
        The body is any extra data associated with the request.
        This is used when submitting data via web forms,
        when uploading files,
        and so on.
        There <em>must</em> be a blank line between the last header and the start of the body
        to signal the end of the headers;
        forgetting it is a common mistake.
      </p>

      <p>
        One header,
        called <code>Content-Length</code>,
        tells the server how many bytes to expect to read in the body of the request.
        There's no magic in any of this:
        an HTTP request is just text,
        and any program that wants to can create one or parse one.
      </p>

      <figure id="f:http_response">
        <img src="img/web/http_response.png" alt="HTTP Response"/>
      </figure>

      <p>
        HTTP responses are formatted like HTTP requests
        (<a href="#f:http_response">Figure XXX</a>).
        The version, headers, and body have the same form
        and mean the same thing.
        The status code is a number indicating what happened
        when the request was processed by the server.
        200 means "everything worked",
        404 means "not found",
        and other codes have other meanings
        (<a href="#f:http_codes">Figure XXX</a>).
        The status phrase repeats that information in a human-readable phrase
        like "OK" or "not found".
      </p>

      <figure id="f:http_codes">
        <table>
          <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Meaning</th>
          </tr>
          <tr>
            <td>100</td>
            <td>Continue</td>
            <td>Client should continue sending data</td>
          </tr>
          <tr>
            <td>200</td>
            <td>OK</td>
            <td>The request has succeeded</td>
          </tr>
          <tr>
            <td>204</td>
            <td>No Content</td>
            <td>The server has completed the request, but doesn't need to return any data</td>
          </tr>
          <tr>
            <td>301</td>
            <td>Moved Permanently</td>
            <td>The requested resource has moved to a new permanent location</td>
          </tr>
          <tr>
            <td>307</td>
            <td>Temporary Redirect</td>
            <td>The requested resource is temporarily at a different location</td>
          </tr>
          <tr>
            <td>400</td>
            <td>Bad Request</td>
            <td>The request is badly formatted</td>
          </tr>
          <tr>
            <td>401</td>
            <td>Unauthorized</td>
            <td>The request requires authentication</td>
          </tr>
          <tr>
            <td>404</td>
            <td>Not Found</td>
            <td>The requested resource could not be found</td>
          </tr>
          <tr>
            <td>408</td>
            <td>Timeout</td>
            <td>The server gave up waiting for the client</td>
          </tr>
          <tr>
            <td>418</td>
            <td>I'm a teapot</td>
            <td>No, really</td>
          </tr>
          <tr>
            <td>500</td>
            <td>Internal Server Error</td>
            <td>An error occurred in the server that prevented it fulfilling the request</td>
          </tr>
          <tr>
            <td>601</td>
            <td>Connection Timed Out</td>
            <td>The server did not respond before the connection timed out</td>
          </tr>
        </table>
        <caption>HTTP Codes</caption>
      </figure>

      <div class="keypoints" id="k:http">
        <h3>Summary</h3>
        <ul>
          <li>Most communication on the web uses TCP/IP sockets.</li>
          <li>Socket endpoints are identified by a host address and a port number.</li>
          <li>The Domain Name System translates human-readable names into host addresses.</li>
          <li>HTTP is a stateless request-response protocol.</li>
          <li>An HTTP request contains a method, headers, and a body.</li>
          <li>An HTTP response also contains a response code.</li>
        </ul>
      </div>

    </section>

    <section id="s:client">

      <h2>Getting Data</h2>

      <div class="understand" id="u:client">
        <h3>Understand:</h3>
        <ul>
          <li>How to get data from the web using HTTP.</li>
          <li>How URL query parameters are formatted.</li>
        </ul>
      </div>

      <p>
        Opening sockets, constructing HTTP requests, and parsing responses is tedious,
        so most people use libraries to do most of the work.
        Python comes with such a library called <code>urllib2</code>
        (because it's a replacement for an earlier library called <code>urllib</code>),
        but it can be fairly complicated for beginners to use.
        Instead,
        we recommend the <code>Requests</code> library.
        Here's an example that shows how to read a page using it:
      </p>

<pre src="src/web/requests_client.py">
import requests
response = requests.get("http://software-carpentry.org/testpage.html")
print 'status code:', response.status_code
print 'content length:', response.headers['content-length']
print response.text
<span class="out">status code: 200
content length: 126
&lt;html&gt;
  &lt;head&gt;
    &lt;title&gt;Software Carpentry Test Page&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;p&gt;Use this page to test requests.&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;</span>
</pre>

      <p>
        Sometimes a URL isn't enough on its own:
        for example,
        when searching on Google, we have to specify what the search terms are.
        We could do this as part of the path in the URL,
        but it's more flexible to add parameters to the URL instead.
        To do this,
        we put a '?' on the end of the URL,
        then add key-value pairs separated by the '&amp;' character.
        For example,
        the URL <code>http://www.google.ca?q=Python</code>
        ask Google to search for pages related to Python,
        while
        <code>http://www.google.ca/search?q=Python&amp;client=Firefox</code>
        asks it to search for pages that mention Python
        while telling Google that the program doing the search is the Firefox browser.
        We can pass whatever parameters we want,
        whenever we want,
        but it's up to the application running on the web site to decide
        which ones to pay attention to,
        and how to interpret them.
      </p>

      <p>
        Of course,
        if '?' and '&amp;' are special characters,
        there must be a way to escape them.
        The <a href="glossary.html#url-encoding">URL encoding</a> standard
        represents special characters using <code>"%"</code> followed by a 2-digit hexadecimal code,
        and replaces spaces with the '+' character
        (<a href="#f:url_encoding">Figure XXX</a>).
        Thus,
        to search Google for "grade&nbsp;=&nbsp;A+" (with the spaces),
        we would use the URL <code>http://www.google.ca/search?q=grade+%3D+A%2B</code>.
      </p>

      <figure id="f:url_encoding">
        <table>
          <tr>
            <th>Character</th>
            <th>Encoding</th>
          </tr>
          <tr>
            <td><code>"#"</code></td>
            <td><code>%23</code></td>
          </tr>
          <tr>
            <td><code>"$"</code></td>
            <td><code>%24</code></td>
          </tr>
          <tr>
            <td><code>"%"</code></td>
            <td><code>%25</code></td>
          </tr>
          <tr>
            <td><code>"&amp;"</code></td>
            <td><code>%26</code></td>
          </tr>
          <tr>
            <td><code>"+"</code></td>
            <td><code>%2B</code></td>
          </tr>
          <tr>
            <td><code>","</code></td>
            <td><code>%2C</code></td>
          </tr>
          <tr>
            <td><code>"/"</code></td>
            <td><code>%2F</code></td>
          </tr>
          <tr>
            <td><code>":"</code></td>
            <td><code>%3A</code></td>
          </tr>
          <tr>
            <td><code>";"</code></td>
            <td><code>%3B</code></td>
          </tr>
          <tr>
            <td><code>"="</code></td>
            <td><code>%3D</code></td>
          </tr>
          <tr>
            <td><code>"?"</code></td>
            <td><code>%3F</code></td>
          </tr>
          <tr>
            <td><code>"@"</code></td>
            <td><code>%40</code></td>
          </tr>
        </table>
        <caption>URL Encoding</caption>
      </figure>

      <p>
        Encoding things by hand is very error-prone,
        so the Requests library lets us pass in
        a dictionary of key-value pairs instead
        via the keyword argument <code>params</code>:
      </p>

<pre src="src/web/urlencode.py">
import requests
parameters = {'q' : 'Python', 'client' : 'Firefox'}
response = requests.get('http://www.google.com/search', params=parameters)
print 'actual URL:', response.url
<span class="out">actual URL: http://www.google.com/search?q=Python&amp;client=Firefox</span>
</pre>

      <p>
        Suppose we want to write a script that actually <em>does</em> search Google.
        Constructing a URL is easy.
        Sending it and reading the response is easy too,
        but parsing the response is hard,
        since there's a lot of stuff in the page that Google sends back.
        Many first-generation web applications relied on
        <a href="glossary.html#screen-scraping">screen scraping</a>
        to get data,
        i.e.,
        extract information from the page by throwing regular expressions at it.
        (They usually had to use regular expressions
        because a lot of the HTML wasn't well-formed,
        and couldn't be interpreted by real XML or HTML parsers.)
      </p>

      <p>
        Screen scraping was always hard to get right if the page layout is complex.
        It was also fragile:
        whenever the layout of the pages changed,
        the application could break
        because data was no longer where it had been.
      </p>

      <p>
        Modern applications separate data from presentation
        by providing some sort of <a href="glossary.html#web-services">web services</a> interface.
        When a client sends a request,
        it indicates whether it wants machine-oriented data or human-readable HTML
        (<a href="#f:web_services">Figure XXX</a>).
        If it asks for the former,
        the server sends back something in XML or some other format
        that is easy for the client to parse.
        This data format is also much less likely to change over time,
        since the information provided by a site
        usually doesn't evolve as rapidly as
        the way that information is displayed.
      </p>

      <figure id="f:web_services">
        <img src="img/web/web_services.png" alt="Web Services"/>
      </figure>

      <p>
        Using "live" data from the web is wonderful,
        but only when it works.
        (As a case in point,
        we wanted to use bird-watching data from <a href="http://ebird.org">ebird.org</a> in this example,
        but their server was locked down for security reasons
        when it came time for us to write our examples.
        This is another way in which software is like other experimental apparatus:
        odds are that when you need it most,
        it will be broken or someone will have borrowed it.)
      </p>

      <p>
        We therefore chose to use climate data from the World Bank instead.
        According to <a href="http://data.worldbank.org/developers/climate-data-api">the documentation</a>,
        data for a particular country can be found at:
      </p>

<pre>
http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/<em>VARIABLE</em>/year/<em>ISO</em>.<em>FORMAT</em>
</pre>

      <p class="continue">
        where:
      </p>

      <ul>
        <li>
          <em>VARIABLE</em> is either "pr" (for precipitation) or "tas" (for surface temperature);
        </li>
        <li>
          <em>ISO</em> is the International Standards Organization's 3-letter country code
          for the country of interest
          (e.g., "FRA" for France);
          and
        </li>
        <li>
          <em>FORMAT</em> is "XML" for XML,
          and other strings for other things
          that we'll talk about later.
        </li>
      </ul>

      <p class="continue">
        The data returned when we get this URL looks like this:
      </p>

<pre>
&lt;list&gt;
  &lt;domain.web.V1WebCru&gt;
    &lt;year&gt;1901&lt;/year&gt;
    &lt;data&gt;21.357021&lt;/data&gt;
  &lt;/domain.web.V1WebCru&gt;
  &lt;domain.web.V1WebCru&gt;
    &lt;year&gt;1902&lt;/year&gt;
    &lt;data&gt;21.382462&lt;/data&gt;
  &lt;/domain.web.V1WebCru&gt;
  ...
&lt;/list&gt;
</pre>

      <p class="continue">
        i.e.,
        an outer <code>list</code> element (the document root)
        that contains any number of <code>domain.web.V1WebCru</code> elements,
        each of which contains <code>year</code> and <code>data</code> elements.
        That long, clumsy name <code>domain.web.V1WebCru</code> probably means something to someone,
        but we don't need to care:
        all we need to know is that each element with that tag
        contains a single year's data.
      </p>

      <p>
        Let's start by writing the main program:
      </p>

<pre src="src/web/temperatures.py">
def main(args):
    first_country = 'AUS'
    second_country = 'CAN'
    if len(args) &gt; 0:
        first_country = args[0]
    if len(args) &gt; 1:
        second_country = args[1]
    ratios(first_country, second_country)

if __name__ == '__main__':
    main(sys.argv[1:])
</pre>

      <p>
        This uses a function called <code>ratios</code>,
        which fetches data
        and then displays the annual ratios:
      </p>

<pre src="src/web/temperatures.py">
def ratios(first_country, second_country):
    '''Show ratio of average temperatures for two countries over time.'''
    first = get_temps(first_country)
    second = get_temps(second_country)
    assert len(first) == len(second), 'Length mis-match in results'
    keys = first.keys()
    keys.sort()
    for k in keys:
        print k, first[k] / second[k]
</pre>

      <p>
        <code>ratios</code> depends in turn on a function <code>get_temps</code>:
      </p>

<pre src="src/web/temperatures.py">
def get_temps(country_code):
    '''Get annual temperatures for a country.'''
    doc = get_xml(country_code)
    result = {}
    for element in doc.findall('domain.web.V1WebCru'):
        year = find_one(element, 'year').text
        temp = find_one(element, 'data').text
        result[int(year)] = kelvin(float(temp))
    return result
</pre>

      <p class="continue">
        which depends on a helper function called <code>get_xml</code>
        to actually download text from the World Bank web site
        and parse it to produce an XML document:
      </p>

<pre src="src/web/temperatures.py">
def get_xml(country_code):
    '''Get XML temperature data for a country.'''
    url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/%s.XML'
    u = url % country_code
    response = requests.get(u)
    doc = ET.fromstring(response.text)
    return doc
</pre>

      <p class="continue">
        The last two functions we need to finish this program are <code>kelvin</code>,
        which converts temperatures from Celsius to Kelvin,
        and <code>find_one</code>,
        which pulls exactly one node out of an XML document:
      </p>

<pre src="src/web/temperatures.py">
def kelvin(celsius):
    '''Convert degrees C to degrees K.'''
    return celsius + 273.15

def find_one(node, pattern):
    '''Get exactly one child that matches an XPath pattern.'''
    all_results = node.findall(pattern)
    assert len(all_results) == 1, 'Got %d children instead of 1' % len(all_results)
    return all_results[0]
</pre>

      <p>
        Let's try running this program with no arguments
        (which compares Australia to Canada):
      </p>

<pre>
$ <span class="in">python temperatures.py</span>
<span class="out">1901 1.10934799048
1902 1.11023963325
1903 1.10876094164
...  ...
2007 1.10725265753
2008 1.10793365185
2009 1.10865537105</span>
</pre>

      <p class="continue">
        and then compare Malaysia with Norway:
      </p>

<pre>
$ <span class="in">python temperatures.py MYS NOR</span>
<span class="out">1901 1.08900632708
1902 1.09536126502
1903 1.08935268463
...  ...
2007 1.08564675748
2008 1.08481881663
2009 1.08720464013</span>
</pre>

      <p>
        Only 24 lines in this program do anything webbish
        (the functions <code>get_temps</code>, <code>get_xml</code>, and <code>find_one</code>),
        and six of those lines are blank or documentation.
        The remaining 30 lines are the user interface
        (handling command-line arguments and printing output)
        and data manipulation
        (converting temperatures and calculating ratios).
        The good news is that
        the webbish stuff only grows slowly as we do more complicated statistics.
      </p>

      <div class="keypoints" id="k:client">
        <h3>Summary</h3>
        <ul>
          <li>Use Python's Requests library to make HTTP requests.</li>
          <li>Let the library format URL parameters.</li>
          <li>Many web sites now provide machine-oriented data as well as human-readable pages.</li>
          <li>The URLs and query parameters needed to fetch data are specified by the web site.</li>
        </ul>
      </div>

    </section>

    <section id="s:server">

      <h2>Providing Data</h2>

      <div class="understand" id="u:server">
        <h3>Understand:</h3>
        <ul>
          <li>That writing secure dynamic web applications is hard.</li>
          <li>That providing dynamically-generated static pages is a good alternative.</li>
          <li>How and why to create an index for such pages.</li>
          <li>How to keep track of what dynamic data has already been processed.</li>
        </ul>
      </div>

      <p>
        The next logical step is to provide data to others
        by writing some kind of server application.
        The basic idea is simple:
        wait for someone to connect and send an HTTP request,
        parse it,
        figure out what it's asking for,
        fetch that data,
        format it as HTML (or XML, or something),
        and send it back
        (<a href="#f:web_application">Figure XXX</a>).
      </p>

      <figure id="f:web_application">
        <img src="img/web/web_application.png" alt="Web Application Lifecycle"/>
      </figure>

      <p>
        But we're not going to show you how to do this,
        because experience has shown that all we can actually do in a short lecture
        is show you how to create security holes.
        Here's just one example.
        Suppose you want to write a web application that accepts URLs of the form
        <code>http://my.site/data?species=homo.sapiens</code>
        and fetches a database record
        containing information about that species.
        One way to do it in Python might look like this:
      </p>

<pre>
def get_species(url):
    '''Get data for a particular species.'''
    params = url.split('?')[1]                                # Get everything after the '?'
    pairs = params.split('&amp;')                                 # Get the name1=value1&amp;name2=value2 pairs
    pairs = [pairs.split('=') for p in pairs]                 # Split the name=value pairs
    pairs = dict(pairs)                                       # Convert to a {name : value} dictionary
    species = pairs['species']                                # Get the species we want to look up
    sql = '''SELECT * FROM Species WHERE Name = "%s";'''      # Template for SQL query
    sql = sql % species                                       # Insert the species name
    cursor.execute(sql)                                       # Send query to database
    results = cursor.fetchall()                               # Get all the results
    return results[0]
</pre>

      <p>
        We've taken out all the error-checking&mdash;for example,
        this code will fail if there aren't actually any query parameters,
        or if the species' name isn't in the database&mdash;but
        that's not the problem.
        The problem is what happens if someone sends us this URL:
      </p>

<pre>
http://my.site/data?species=homo.sapiens&quot;;DROP TABLE Species&quot;--
</pre>

      <p class="continue">
        Why?
        Because the dictionary of query parameters produced by
        the first five lines of the function
        will be:
      </p>

<pre>
{ 'species' : 'homo.sapiens&quot;;DROP TABLE Species;--' }
</pre>

      <p class="continue">
        which means that the SQL query will be:
      </p>

<pre>
SELECT * FROM Species WHERE Name = "homo.sapiens&quot;;DROP TABLE Species;--";
</pre>

      <p class="continue">
        which is the same as:
      </p>

<pre>
SELECT * FROM Species WHERE Name = "homo.sapiens";
DROP TABLE Species;
</pre>

      <p>
        In other words,
        this selects something from the database,
        then throws away the entire <code>Species</code> table.
        It's called an <a href="glossary.html#sql-injection">SQL injection attack</a>,
        because the user is injecting arbitrary (and usually damaging) SQL
        into our database query,
        and it's just one of hundreds of different ways that villains can try to compromise a web application.
        Built properly,
        web sites can withstand such attacks,
        but "properly" takes time.
      </p>

      <p>
        Instead,
        we will look at how to write programs that create plain old HTML pages
        that can then be shared with the world by a standard web server like Apache.
        Using our previous example (ratios of average annual temperatures) as a starting point,
        we'll create pages whose names look like
        <code>http://my.site/tempratio/AUS-CAN.html</code>,
        and which contain data formatted like this:
      </p>

<pre>
&lt;html&gt;
  &lt;head&gt;
    &lt;meta name="revised" content="2012-09-15" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;Ratio of Average Annual Temperatures for AUS and CAN&lt;/h1&gt;
    &lt;table class="data"&gt;
      &lt;tr&gt;
        &lt;td class="year"&gt;1901&lt;/td&gt;
        &lt;td class="data"&gt;1.10934799048&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr&gt;
        &lt;td class="year"&gt;1902&lt;/td&gt;
        &lt;td class="data"&gt;1.11023963325&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr&gt;
        &lt;td class="year"&gt;1903&lt;/td&gt;
        &lt;td class="data"&gt;1.10876094164&lt;/td&gt;
      &lt;/tr&gt;
      ...
      &lt;tr&gt;
        &lt;td class="year"&gt;2007&lt;/td&gt;
        &lt;td class="data"&gt;1.10725265753&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr&gt;
        &lt;td class="year"&gt;2008&lt;/td&gt;
        &lt;td class="data"&gt;1.10793365185&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr&gt;
        &lt;td class="year"&gt;2009&lt;/td&gt;
        &lt;td class="data"&gt;1.10865537105&lt;/td&gt;
      &lt;/tr&gt;
    &lt;/table&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <p>
        The first step is to calculate ratios,
        which we did in the <a href="#s:client">previous section</a>.
        Our updated main program is:
      </p>

<pre src="src/web/make_data_page.py">
def main(args):
    first_country = 'AUS'
    second_country = 'CAN'
    index_page = 'index.html'
    if len(args) &gt; 0:
        first_country = args[0]
    if len(args) &gt; 1:
        second_country = args[1]
    if len(args) &gt; 2:
        index_page = args[2]
    make_page(sys.stdout, first_country, second_country)
    update_index(index_page, first_country, second_country)
</pre>

      <p>
        The second step is to translate the temperature values into a web page,
        which we'll do using the ElementTree library:
      </p>

<pre src="src/web/make_data_page.py">
def make_page(output, first_country, second_country):
    '''Create page showing temperature ratios.'''

    first_data = get_temps(first_country)
    second_data = get_temps(second_country)

    the_date = date.isoformat(date.today())

    html = ET.Element('html')
    head = ET.SubElement(html, 'head')
    revised = ET.SubElement(head, 'meta', {'name'    : 'revised',
                                           'content' : the_date})

    body = ET.SubElement(html, 'body')
    h1 = ET.SubElement(body, 'h1')
    h1.text = 'Ratio of Average Annual Temperatures for %s and %s' % \
              (first_country, second_country)

    make_table(body, first_data, second_data)

    output.write(ET.tostring(html))
</pre>

      <p class="continue">
        For readability's sake,
        we have put the code that actually generates the table
        in a separate function:
      </p>

<pre src="src/web/make_data_page.py">
def make_table(parent, first_data, second_data):
    '''Create table in page showing temperature ratios.'''
    table = ET.SubElement(parent, 'table')
    table.attrib['class'] = 'data'
    keys = first_data.keys()
    keys.sort()
    for year in keys:
        tr = ET.SubElement(table, 'tr')
        td_year = ET.SubElement(tr, 'td', {'class' : 'year'})
        td_year.text = str(year)
        td_data = ET.SubElement(tr, 'td', {'class' : 'data'})
        td_data.text = str( first_data[year] / second_data[year] )
</pre>

      <p>
        But we're only half-done at this point.
        If we're going to calculate these tables for many different countries,
        how will other scientists know which ones we've done?
        In other words,
        how can we make our data findable?
      </p>

      <p>
        The standard answer for the last few hundred years has been,
        "Create an index."
        On the web,
        we can do this by creating a file called <code>index.html</code>
        and putting it in the directory that holds our data files,
        because by default,
        most web servers will give clients that file
        when they're asked for the directory itself.
        In other words,
        if someone points a browser (or any other program)
        at <code>http://my.site/tempratio/</code>,
        the web server will look for <code>/tempratio</code>.
        When it realizes that path is a directory rather than a file,
        it will look inside that directory for a file called <code>index.html</code>
        and return that.
        This is <em>not</em> guaranteed&mdash;system administrators
        can and do set up other default behaviors&mdash;but it is a common convention,
        and we can always tell our colleagues to fetch
        <code>http://my.site/tempratio/</code>
        if they want the current index anyway.
      </p>

      <p>
        What should be in <code>index.html</code>?
        The answer is simple:
        a table of some kind showing what files are available
        and when they were created.
        The first piece of information is the most important;
        the second allows users to determine
        what has been added since they last looked at our site
        without having to download actual data files.
        Our <code>index.html</code> will therefore be something like this:
      </p>

<pre>
&lt;html&gt;
  &lt;head&gt;
    &lt;meta name="revised" content="2012-09-15" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;Index of Average Annual Temperature Ratios&lt;/h1&gt;
    &lt;table class="data"&gt;
      &lt;tr&gt;
        &lt;td class="revised"&gt;2012-09-12&lt;/td&gt;
        &lt;td class="country"&gt;AUS&lt;/td&gt;
        &lt;td class="country"&gt;CAN&lt;/td&gt;
      &lt;/tr&gt;
      ...
      &lt;tr&gt;
        &lt;td class="revised"&gt;2012-09-15&lt;/td&gt;
        &lt;td class="country"&gt;MYS&lt;/td&gt;
        &lt;td class="country"&gt;NOR&lt;/td&gt;
      &lt;/tr&gt;
    &lt;/table&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <p>
        Unlike our actual data files,
        this file is added to incrementally:
        each time we generate a new version,
        we have to include all the data that was in the old version as well.
        We therefore need to remember what we've done.
        The usual way to do this in a real application
        is to use a database of some kind,
        but we're going to try something simpler.
        Let's start by creating an empty <code>index.html</code> page
        in our <code>/tempratio</code> directory:
      </p>

<pre>
&lt;html&gt;
  &lt;head&gt;
    &lt;meta name="revised" content="" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;Index of Average Annual Temperature Ratios&lt;/h1&gt;
    &lt;table class="data"&gt;
    &lt;/table&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <p>
        Each time we generate a new data set,
        we will read this file in,
        updated the revision date in the <code>meta</code> element in the header,
        add one row to the table for our new data file,
        and write it back out.
        In other words,
        we'll use the index file itself as
        our long-term record of what we've done.
      </p>

      <p>
        Here's the function that does that:
      </p>

<pre src="src/web/make_data_page.py">
def update_index(path_to_index, first_country, second_country):
    '''Update the index of our data files.'''

    the_date = date.isoformat(date.today())
    doc = ET.parse(path_to_index)

    replace_meta(doc, the_date)
    add_record(doc, the_date, first_country, second_country)

    writer = open(path_to_index, 'w')
    writer.write(ET.tostring(doc))
</pre>

      <p>
        And here are the two helper functions that <code>update_index</code> depends on.
        The first replaces the date in the index page's metadata:
      </p>

<pre src="src/web/make_data_page.py">
def replace_meta(doc, the_date):
    '''Replace the revision date in the page header.'''
    node = doc.findall('.//meta[@name="revised"]')[0]
    node.attrib['content'] = the_date
</pre>

      <p class="continue">
        while the second adds another row to the index table:
      </p>

<pre src="src/web/make_data_page.py">
def add_record(doc, the_date, first_country, second_country):
    '''Add a record for another country pair to the index table.'''
    table = doc.findall('.//table[@class="data"]')
    row = ET.SubElement(table, 'tr')
    for (coltype, data) in (('revised', the_date),
                            ('country', first_country),
                            ('country', second_country)):
        col = ET.SubElement(row, 'td', {'class' : coltype})
        col.text = data
</pre>

      <p>
        We now have an index that tells anyone who wants to know
        what data is available.
        It still doesn't include the URLs to the data files themselves;
        they can easily be constructed from the country names,
        but that's bad design,
        since it requires the client to know something about this data in particular.
        A much better approach is to add the links to the table itself
        so that we have:
      </p>

<pre>
&lt;html&gt;
  &lt;head&gt;
    &lt;meta name="revised" content="2012-09-15" /&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;Index of Average Annual Temperature Ratios&lt;/h1&gt;
    &lt;table class="data"&gt;
      &lt;tr&gt;
        &lt;td class="revised"&gt;2012-09-12&lt;/td&gt;
        &lt;td class="country"&gt;AUS&lt;/td&gt;
        &lt;td class="country"&gt;CAN&lt;/td&gt;
        &lt;td class="url"&gt;&lt;a href="http://my.site/tempratio/AUS-CAN.html"&gt;AUS-CAN.html&lt;/a&gt;&lt;/td&gt;
      &lt;/tr&gt;
      ...
      &lt;tr&gt;
        &lt;td class="revised"&gt;2012-09-15&lt;/td&gt;
        &lt;td class="country"&gt;MYS&lt;/td&gt;
        &lt;td class="country"&gt;NOR&lt;/td&gt;
        &lt;td class="url"&gt;&lt;a href="http://my.site/tempratio/MYS-NOR.html"&gt;MYS-NOR.html&lt;/a&gt;&lt;/td&gt;
      &lt;/tr&gt;
    &lt;/table&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre>

      <p>
        By using the standard <code>a</code> tag and its <code>href</code> attribute,
        we have made it possible for search engines to understand this data:
        they don't need to know anything about concatenating country names
        in order to know what's a link,
        or what other files are available.
      </p>

      <p>
        All right:
        now that we can create pages,
        how can other people use them?
        Let's suppose for the moment that
        every time we provide a new data file,
        our collaborators will want to get it,
        but that they only want each file once.
        We have given them the URL of the index page
        (which is <code>http://my.site/tempratio/index.html</code>),
        so the first thing they'll do is grab that:
      </p>

<pre>
response = requests.get('http://my.site/tempratio/index.html')
doc = ET.fromstring(response.text)
</pre>

      <p class="continue">
        and then extract all of the entries:
      </p>

<pre>
rows = doc.findall('.//table[@class="data"]/tr')
entries = set()
for r in rows:
    the_date = r.findall('./td[@class="revised"]')[0].text
    the_countries = r.findall('./td[@class="country"]')
    country_a = the_countries[0].text
    country_b = the_countries[1].text
    url = r.findall('./td[@class="url"]/a').attrib['href']
    new_entry = (the_date, country_a, country_b, url)
    entries.add(new_entry)
</pre>

      <p>
        This creates a set of tuples,
        each of which has a date,
        two countries,
        and a URL.
        What it <em>doesn't</em> do is subtract the ones we have seen before.
        In order to do that,
        we need to keep some sort of record of what's already been examined.
        We can do that in two ways:
      </p>

      <ol>

        <li>
          <em>On the server</em>:
          give everyone with access to the data a user ID,
          and have the server keep track of what they have downloaded
        </li>

        <li>
          <em>On the client</em>:
          have each user keep track of their downloads themselves.
        </li>

      </ol>

      <p>
        The first is better if people are frequently grabbing data from different machines,
        i.e.,
        if one person uses several different computers,
        but we still want to think of them as one person.
        The second is a lot less in every other case,
        since it doesn't require us to set up accounts,
        manage logins,
        and so on,
        so we'll do that.
        In particular,
        we'll save a copy of the last <code>index.html</code> file we downloaded,
        then "subtract" its entries from what's in the latest downloaded index file
        to find out what we actually need to grab.
      </p>

      <p>
        By now,
        the first step should seem familiar:
      </p>

<pre src="src/web/get_data_page.py">
def main(args):
    '''Main driver for program.'''

    assert len(args) == 2
    url, filename = args

    current_index = get_web(url)
    old_index = get_file(filename)

    new_index = current_index - old_index
    show_index(new_index)

    save_index(filename, current_index)

if __name__ == '__main__':
    main(sys.argv[1:])
</pre>

      <p>
        Getting an index from the web
        and getting one out of a file
        are almost the same:
      </p>

<pre src="src/web/get_data_page.py">
INDEX_URL = 'http://my.site/tempratio/index.html'

def get_web(url):
    '''Get index from a URL on the web.'''
    response = requests.get(INDEX_URL)
    doc = ET.fromstring(response.text)
    return parse_index(doc)

def get_file(filename):
    '''Get index from a file on disk.'''
    reader = open(filename, 'r')
    data = reader.read()
    reader.close()
    doc = ET.fromstring(data)
    return parse_index(doc)
</pre>

      <p class="continue">
        The common code is in <code>parse_index</code>,
        which grabs rows out of the data table
        and extracts the date and country fields
        (we'll leave URL handling as an exercise):
      </p>

<pre src="src/web/get_data_page.py">
def parse_index(doc):
    '''Get a set of (date, country_a, country_b) tuples from an index file.'''
    index = set()
    rows = doc.findall('.//table[@class="data"]/tr')
    for r in rows:
        the_date = r.findall('./td[@class="revised"]')[0].text
        the_countries = r.findall('./td[@class="country"]')
        country_a = the_countries[0].text
        country_b = the_countries[1].text
        new_entry = (the_date, country_a, country_b)
        index.add(new_entry)
    return index
</pre>

      <p>
        We don't have to write a function
        to determine which entries we haven't seen before:
        that's just subtracting one set from another.
        To display a list of unseen entries,
        we sort the index
        (so that entries will be in order by date)
        and loop over it:
      </p>

<pre src="src/web/get_data_page.py">
def show_index(index):
    '''Display index in order.'''
    temp = sorted(index)
    for (date, country_a, country_b) in temp:
        print date, country_a, country_b
</pre>

      <p class="continue">
        and to save the new index information,
        we just convert it back to text
        and write that to the local file:
      </p>

<pre src="src/web/get_data_page.py">
def save_index(filename, index):
    '''Save index as XML for next time.'''
    writer = open(filename, 'w')
    writer.write(ET.tostring(index))
    writer.close()
</pre>

      <p>
        As with our original temperature ratio example,
        only a small part of this code has anything to do with the web:
        only two lines (in <code>get_web</code>) touch the network at all.
        Everything else is about reading and interpreting the data
        that we've pulled from the web,
        which is as it should be.
      </p>

      <div class="keypoints" id="k:server">
        <h3>Summary</h3>
        <ul>
          <li>It is hard to make dynamic web applications secure.</li>
          <li>An alternative is to dynamically generate static web pages.</li>
          <li>Every collection of data should provide a machine-readable index.</li>
          <li>URLs should be embedded in the index to keep clients simple.</li>
          <li>Information about what data has been seen can be stored on the server or on the client.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

      <p>
        The web has changed in many ways over the last 20 years,
        not all of them for the better.
        An HTML page on a modern commercial site
        is likely to include dozens or hundreds of lines of Javascript
        that depend on several large, complicated libraries,
        and which generate the page's content on the fly inside the browser.
        Such a "page" is really a small (or not-so-small) program
        rather than a document in the classical sense of the word,
        and while that may produce a better experience for human users,
        it makes life more difficult for programs
        (and for people with disabilities,
        whose assistive aids are all too easy to confuse).
        And while XML is widely used for representing data,
        many people believe that
        younger alternatives like <a href="glossary.html#json">JSON</a>
        do a better job of balancing the needs of human and computer readers.
      </p>

      <p>
        Regardless of the technology used,
        though,
        the web's <a href="http://blog.jonudell.net/2011/01/24/seven-ways-to-think-like-the-web/">basic design principles</a>
        are both simple and stable:
        tell people where data is, rather than giving them a copy;
        make the data itself and your names for it
        easy for both human beings and computers to understand;
        remix other people's data,
        and allow them to remix yours.
      </p>

    </section>