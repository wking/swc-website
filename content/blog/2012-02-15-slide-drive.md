Journal: True
Post_Id: 4557
Author: Greg Wilson
Title: Slide Drive
Tags: content, education, versions/version-5-0

<p>Speaking of new kinds of content (which I've <a href="|filename|2012-01-26-never-mind-the-content-what-about-the-format.md">been</a> <a href="|filename|2012-02-13-formatting-revisited.md">doing</a> <a href="|filename|2012-02-14-new-kinds-of-content.md">a lot</a>), <a href="http://dseifried.wordpress.com/">David Seifreid</a> has built a working prototype of a new slideshow tool that combines <a href="http://imakewebthings.github.com/deck.js/">deck.js</a> with an HTML5 audio player.  You can check out a demo or grab the source from <a href="https://github.com/dseif/slide-drive">https://github.com/dseif/slide-drive</a>. Slides are pure HTML like this:</p>
<pre>&lt;section popcorn-slideshow="24"&gt;
  &lt;h2&gt;Solution&lt;/h2&gt;
  &lt;p&gt;Short intensive workshops&lt;/p&gt;
  &lt;div&gt;
    Our solution combines short, intensive workshops...
  &lt;/div&gt;
  &lt;div popcorn-slideshow="27"&gt;
    &lt;p&gt;Plus self-paced online instruction&lt;/p&gt;
    &lt;div&gt;
      ...with self-paced online instruction.
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/section&gt;</pre>
<p>which combines slide pages and transcripts in a single file suitable for diffing and merging. (Images are still in external files, but I can live with that.) You can pause the slideshow at any point to select and copy the content (something you definitely <em>can't</em> do with a video), and we'll add support for translations into other languages and so on.</p>
<p>Many thanks to David for pulling this together; please let us know what you think.</p>