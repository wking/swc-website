Title: The Bash Shell
Directory: book

    <ol class="toc">
      <li><a href="#s:what">What and Why</a></li>
      <li><a href="#s:filedir">Files and Directories</a></li>
      <li><a href="#s:create">Creating Things</a></li>
      <li><a href="#s:pipefilter">Pipes, Filters, and Wildcards</a></li>
      <li><a href="#s:loop">Loops</a></li>
      <li><a href="#s:scripts">Shell Scripts</a></li>
      <li><a href="#s:find">Finding Things</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <p>
      Nelle Nemo,
      a marine biologist,
      has just returned from a six-month survey of the
      <a href="http://en.wikipedia.org/wiki/North_Pacific_Gyre">North Pacific Gyre</a>,
      where she has been collecting samples of gelatinous marine life
      from the <a href="http://en.wikipedia.org/wiki/Great_Pacific_Garbage_Patch">Great Pacific Garbage Patch</a>.
      She has 1520 samples in all,
      and now needs to:
    </p>

    <ol>
      <li>
        Run each sample through an assay machine that will measure the relative abundance of 300 different proteins.
        The machine's output for a single sample is one file with one line for each protein.
      </li>
      <li>
        Calculate statistics for each of the proteins separately
        using a program her supervisor wrote called <code>goostat</code>.
      </li>
      <li>
        Compare the statistics for each protein with corresponding statistics for each other protein
        using a program one of the other graduate students wrote called <code>goodiff</code>.
      </li>
      <li>
        Write up.
        Her supervisor would really like her to do this by the end of the month
        so that her paper can appear in
        an upcoming special issue of <cite>Aquatic Goo Letters</cite>.
      </li>
    </ol>

    <p>
      It takes about half an hour for the assay machine to process each sample.
      The good news is,
      it only takes two minutes to set each one up.
      Since her lab has eight assay machines that she can use in parallel,
      this step will "only" take about two weeks.
    </p>

    <p>
      The bad news is,
      if she has to run <code>goostat</code> and <code>goodiff</code> by hand,
      she'll have to enter filenames and click "OK" roughly 300<sup>2</sup> times
      (300 runs of <code>goostat</code>, plus 300&times;299 runs of <code>goodiff</code>).
      At 30 seconds each,
      that's 750 hours, or 18 weeks, of mindless, repetitive, soul-destroying work.
      Not only would she miss her paper deadline,
      the chances of her getting all 90,000 commands right are approximately zero.
    </p>

    <p>
      This chapter is about what she should do instead.
      More specifically,
      it's about how she can use a command shell
      to automate all the repetitive steps in her processing pipeline,
      so that her computer can work 24 hours a day
      while she catches up on her reading.
      As a bonus,
      once she has put a processing pipeline together,
      she will be able to use it again in the future
      whenever she, or someone else,
      collects more data of this kind.
    </p>

    <section id="s:intro">

      <h2>What and Why</h2>

      <div class="understand" id="u:intro">
        <h3>Understand:</h3>
        <ul>
          <li>Where the shell lies between the computer, the operating system, and the user's programs.</li>
          <li>When and why command-line interfaces should be used instead of graphical interfaces.</li>
        </ul>
      </div>

      <p>
        At a high level, computers really do four things:
      </p>

      <ul>
        <li>run programs;</li>
        <li>store data;</li>
        <li>communicate with each other; and</li>
        <li>interact with us.</li>
      </ul>

      <p>
        They can do the last of these in many different ways.
        For example, they can use direct brain-computer links.
        This technology is still in its infancy,
        but I for one look forward to being assimilated as it matures&hellip;
        Another way is to talk to them.
        No, <em>talk to them</em>, not <em>dock the pen</em>.
        This technology is also still somewhat immature.
      </p>

      <p>
        What most of us use for interacting with computers is a WIMP interface:
        windows, icons, mice, and pointers.
        These technologies didn't become widespread until the 1980s,
        but their roots go back to Doug Engelbart's work in the 1960s,
        which you can see in what has been called
        "<a href="http://video.google.com/videoplay?docid=-8734787622017763097#">The Mother of All Demos</a>".
      </p>

      <p>
        Going back even further,
        the only way to interact with early computers was to rewire them.
        But in between,
        from the 1950s to the 1980s and into the present day,
        people used a technology that's based on the old-fashioned typewriter,
        and that technology is what we're going to explore in this lecture.
      </p>

      <figure id="f:decwriter">
        <img src="img/shell/decwriter.jpg" alt="DECWriter LA-36" />
      </figure>

      <p>
        When I say "typewriter", I actually mean a line printer connected to a keyboard
        (<a href="#f:decwriter">Figure 1</a>).
        These devices only allowed input and output of the letters, numbers, and punctuation found on a standard keyboard,
        so programming languages and interfaces had to be designed around that constraint&mdash;although
        if you were clever enough, you could draw simple pictures using just those characters
        (<a href="#f:ascii_art">Figure 2</a>).
      </p>

      <figure id="f:ascii_art">
<pre>
                    ,-.             __
                  ,'   `---.___.---'  `.
                ,'   ,-                 `-._
              ,'    /                       \
           ,\/     /                        \\
       )`._)>)     |                         \\
       `>,'    _   \                  /       ||
         )      \   |   |            |        |\\
.   ,   /        \  |    `.          |        | ))
\`. \`-'          )-|      `.        |        /((
 \ `-`   .`     _/  \ _     )`-.___.--\      /  `'
  `._         ,'     `j`.__/           `.    \
    / ,    ,'         \   /`             \   /
    \__   /           _) (               _) (
      `--'           /____\             /____\
</pre>
        <caption>ASCII Art</caption>
      </figure>

      <p>
        This kind of interface is called a command-line user interface,
        or <a href="glossary.html#clui">CLUI</a>,
        to distinguish it from the graphical user interface,
        or <a href="glossary.html#gui">GUI</a>,
        that most of us now use.
        The heart of a CLUI is a read-evaluate-print loop:
        when the user types a command,
        the computer executes it and prints its output.
        (In the case of old teletype terminals, it literally printed the output onto paper, a line at a time.)
        The user then types another command,
        and so on until the user logs off.
      </p>

      <p>
        From this description, you'd think that the user was sending commands directly to the computer,
        and that the computer was sending output directly to the user.
        In fact,
        there's a program in between called a <a href="glossary.html#shell">command shell</a>
        (<a href="#f:command_shell">Figure 3</a>).
        What the user types goes into the shell;
        it figures out what commands to run and orders the computer to execute them.
        The computer then sends the output of those programs back to the shell,
        which takes care of displaying things to the user.
      </p>

      <figure id="f:command_shell">
        <img src="img/shell/command_shell.svg" alt="The Command Shell" />
      </figure>

      <p>
        A shell is just a program like any other.
        The only thing that's special about it is that its job is to run other programs,
        rather than to do calculations itself.
        The most popular Unix shell is Bash, the Bourne Again SHell
        (so-called because it's derived from a shell written by Stephen Bourne&mdash;this
        is what passes for wit among programmers).
        Bash is the default shell on most modern implementations of Unix,
        and also comes with <a href="http://www.cygwin.org">Cygwin</a>,
        a popular Unix-on-Windows toolkit.
      </p>

      <p>
        Using Bash,
        or any other shell,
        feels more like programming that like using a mouse.
        Commands are terse (often only a couple of characters long),
        their names are often cryptic,
        and their only output is lines of text rather than a graph or diagram.
        On the other hand,
        the shell allows us to combine existing tools in powerful ways with only a few keystrokes,
        and to set up pipelines to handle large volumes of data automatically.
        In addition,
        the command line is often the easiest way to interact with remote machines.
        As clusters and cloud computing become more popular for scientific data crunching,
        being able to drive them is becoming a necessary skill.
      </p>

      <div class="keypoints" id="k:intro">
        <h3>Summary</h3>
        <ul>
          <li>The shell is a program whose primary purpose is to read commands, run programs, and display results.</li>
        </ul>
      </div>

    </section>

    <section id="s:filedir">

      <h2>Files and Directories</h2>

      <div class="understand" id="u:filedir">
        <h3>Understand:</h3>
        <ul>
          <li>The difference between a file and a directory.</li>
          <li>The hierarchical organization of directories.</li>
          <li>The difference between absolute and relative paths.</li>
          <li>How to navigate the hierarchy.</li>
          <li>That file suffixes are used to suggest file type.</li>
          <li>The shell's read-run-print cycle.</li>
          <li>That commands have options indicated by flags.</li>
          <li>That tab completion saves time and reduces errors.</li>
        </ul>
      </div>

      <p>
        Some of the shell commands we will use most often are related to storing data on disk.
        The subsystem responsible for this is called the <a href="glossary.html#file-system">file system</a>.
        It organizes our data into files, which hold information, and directories, which hold files or other directories.
      </p>

      <p>
        To start,
        let's log in to the computer by typing our user ID and password.
        (We'll show user input like <span class="in">this</span>.)
        Most systems will print stars to obscure the password,
        or nothing at all,
        in case some evildoer is shoulder surfing behind us.
      </p>

<pre>
login: <span class="in">vlad</span>
password: <span class="in">********</span>
$
</pre>

      <p>
        Once we have logged in we'll see a <a href="glossary.html#prompt">prompt</a>,
        which is the computer's way of telling us that it's waiting for input.
        This is usually just a dollar sign,
        but which may show extra information such as our user ID.
        Type <code class="in">whoami</code>, followed by <span class="in">enter</span>.
        This command prints out the ID of the current user,
        i.e., shows us who the shell thinks we are:
      </p>

<pre>
$ <span class="in">whoami</span>
<span class="out">vlad</span>
$
</pre>

      <p class="continue">
        More specifically,
        when we type <code>whoami</code>
        the shell finds a program called <code>whoami</code>,
        runs it,
        displays its output,
        and then displays a new prompt to tell us that it's ready for more commands.
      </p>

      <p>
        Now that we know <em>who</em> we are,
        we can find out <em>where</em> we are using <code>pwd</code>,
        which stands for "print working directory".
        This is our current default directory,
        i.e., the directory (or folder) that the computer assumes we want to run commands on
        unless we specify something else explicitly.
        Here, the computer's response is <code class="out">/users/vlad</code>,
        which is Vlad's <a href="glossary.html#home-directory">home directory</a>:
      </p>

<pre>
$ <span class="in">pwd</span>
<span class="out">/users/vlad</span>
$
</pre>

      <p class="continue">
        To understand what this means,
        let's have a look at how the file system as a whole is organized
        (<a href="#f:filesystem">Figure 4</a>):
      </p>

      <figure id="f:filesystem">
        <img src="img/shell/filesystem.png" alt="File System" />
      </figure>

      <p class="continue">
        The very top of the file system is a directory called the <a href="glossary.html#root-directory">root directory</a>
        that holds everything else the computer is storing.
        When we want to refer to it, we just use a slash character <code>/</code>.
        This is the leading slash in <code>/users/vlad</code>.
      </p>

      <p>
        Inside that directory (or underneath it, if you're drawing a tree) are several other directories,
        such as <code>bin</code> (which is where some built-in programs are stored),
        <code>data</code>,
        <code>users</code> (where users' personal directories are located),
        <code>tmp</code> (for temporary files that don't need to be stored long-term),
        and so on.
        We know that our current working directory <code>/users/vlad</code> is stored inside <code>/users</code>
        because <code>/users</code> is the first part of its name.
        Similarly, we know that <code>/users</code> is stored inside the root directory <code>/</code> because its name begins with <code>/</code>.
      </p>

      <p>
        Underneath <code>/users</code>, we find one directory for each user with an account on this machine:
      </p>

      <figure id="f:home_directories">
        <img src="img/shell/home_directories.png" alt="Home Directories" />
      </figure>

      <p class="continue">
        The Mummy's files are stored in <code>/users/imhotep</code>,
        Wolfman's in <code>/users/larry</code>,
        and ours in <code>/users/vlad</code>,
        which is why <code>vlad</code> is the last part of the directory's name.
        Notice, by the way, that there are two meanings for the <code>/</code> character.
        When it appears at the front of a file or directory name, it refers to the root directory.
        When it appears <em>inside</em> a name, it's just a separator.
      </p>

      <p>
        Let's see what's in Vlad's home directory by running <code>ls</code>, which stands for "listing".
        (It's not a particularly memorable name, but as we'll see, many others are unfortunately even more cryptic.)
      </p>

<pre>
$ <span class="in">ls</span>
<span class="out">bin          data      mail       music
notes.txt    papers    pizza.cfg  solar
solar.pdf    swc</span>
$
</pre>

      <p class="continue">
        <code>ls</code> prints the names of all the files and directories in the current directory in alphabetical order,
        arranged neatly into columns.
        To make its output more comprehensible,
        we can give it the <a href="glossary.html#command-line-flag">flag</a> <code>-F</code> by typing <code>ls -F</code>.
        This tells <code>ls</code> to add a trailing <code>/</code> to the names of directories:
      </p>

<pre>
$ <span class="in">ls -F</span>
<span class="out">bin/         data/     mail/      music/
notes.txt    papers/   pizza.cfg  solar/
solar.pdf    swc/</span>
$
</pre>

      <p class="continue">
        As you can see, there are seven of these.
        The names <code>notes.txt</code>, <code>pizza.cfg</code>, and <code>solar.pdf</code> that don't have trailing slashes are plain old files.
      </p>

      <figure id="f:vlad_homedir">
        <img src="img/shell/vlad_homedir.png" alt="Vlad's Home Directory" />
      </figure>

      <div class="box">

        <h3>What's In A Name?</h3>

        <p>
          You may have noticed that files' names are all something dot something.
          By convention, the second part, called the <a href="glossary.html#filename-extension">filename extension</a>,
          indicates what type of data the file holds:
          <code>.txt</code> signals a plain text file,
          <code>.pdf</code> indicates a PDF document,
          <code>.cfg</code> is a configuration file full of parameters for some program or other,
          and so on.
          However, this is only a convention, and not a guarantee.
          Files contain bytes, nothing more.
          It's up to us and our programs to interpret those bytes according to the rules for PDF documents, images, and so on.
        </p>

      </div>

      <p>
        Now let's run the command <code>ls -F data</code>,
        which tells <code>ls</code> to give us a listing of what's in our <code>data</code> directory:
      </p>

<pre>
$ <span class="in">ls -F data</span>
<span class="out">amino_acids.txt   elements/     morse.txt
pdb/              planets.txt   sunspot.txt</span>
$
</pre>

      <p class="continue">
        The output shows us that there are four text files and two directories.
        This hierarchical organization helps us keep our work organized.
        Notice how we spelled the directory name <code>data</code>.
        Since it doesn't begin with a slash,
        it's a <a href="glossary.html#relative-path">relative path</a>,
        i.e., it's interpreted relative to the current working directory:
      </p>

      <figure id="f:relative_path">
        <img src="img/shell/relative_path.png" alt="Relative Paths" />
      </figure>

      <p class="continue">
        If we run <code>ls -F /data</code>,
        we get a different answer,
        because <code>/data</code> is an <a href="glossary.html#absolute-path">absolute path</a>:
      </p>

<pre>
$ <span class="in">ls -F /data</span>
<span class="out">access.log    backup/    hardware.cfg
network.cfg</span>
$
</pre>

      <p class="continue">
        The leading <code>/</code> tells the computer to follow the path from the root of the filesystem,
        so it always refers to exactly one directory,
        no matter where we are when we run the command.
      </p>

      <figure id="f:absolute_path">
        <img src="img/shell/absolute_path.png" alt="Absolute Paths" />
      </figure>

      <p>
        What if we want to change our current working directory?
        <code>pwd</code> shows us that we're still in <code>/users/vlad</code>,
        and <code>ls</code> without any arguments shows us its contents:
      </p>

<pre>
$ <span class="in">pwd</span>
<span class="out">/users/vlad</span>
$ <span class="in">ls</span>
<span class="out">bin/         data/     mail/      music/
notes.txt    papers/   pizza.cfg  solar/
solar.pdf    swc/</span>
$
</pre>

      <p class="continue">
        We can use <code>cd</code> followed by a directory name to change our working directory.
        <code>cd</code> stands for "change directory", which is a bit misleading:
        the command doesn't change the directory,
        it changes the shell's idea of what directory we are in.
      </p>

<pre>
$ <span class="in">cd data</span>
$
</pre>

      <p class="continue">
        <code>cd</code> doesn't print anything,
        but if we run <code>pwd</code> after it,
        we can see that we are now in <code>/users/vlad/data</code>.
        If we run <code>ls</code> without arguments now,
        it lists the contents of <code>/users/vlad/data</code>,
        because that's where we now are:
      </p>

<pre>
$ <span class="in">pwd</span>
<span class="out">/users/vlad/data</span>
$ <span class="in">ls</span>
<span class="out">amino_acids.txt   elements/     morse.txt
pdb/              planets.txt   sunspot.txt</span>
$
</pre>

      <p>
        OK, we can go down the directory tree: how do we go up?
        If we're still in <code>/users/vlad/data</code>,
        we can use <code>cd&nbsp;..</code> to go up one level:
      </p>

<pre>
$ <span class="in">pwd</span>
<span class="out">/users/vlad/data</span>
$ <span class="in">cd ..</span>
</pre>

      <p class="continue">
        <code>..</code> is a special directory name meaning "the directory containing this one",
        or, more succinctly,
        the <a href="glossary.html#parent-directory">parent</a> of the current directory.
        Sure enough, if we run <code>pwd</code> after running <code>cd&nbsp;..</code>,
        we're back in <code>/users/vlad</code>:
      </p>

<pre>
$ <span class="in">pwd</span>
<span class="out">/users/vlad</span>
$
</pre>

      <p>
        The special directory <code>..</code> doesn't usually show up when we run <code>ls</code>.
        If we add the <code>-a</code> flag to our <code>-F</code>, though, it will be displayed:
      </p>

<pre>
$ <span class="in">ls -F -a</span>
<span class="out">./           ../       bin/       data/
mail/        music/    notes.txt  papers/
pizza.cfg    solar/    solar.pdf    swc/</span>
</pre>

      <p class="continue" id="a:dot-directory">
        <code>-a</code> stands for "show all".
        It forces <code>ls</code> to show us directory names that begin with <code>.</code>, such as <code>..</code>
        (which, if we're in <code>/users/vlad</code>, means the <code>/users</code> directory).
        As you can see,
        it also displays another special directory that's just called <code>.</code>.
        This means "the directory we're currently in".
        It may seem redundant to have a name for it,
        but we'll see some uses for it soon.
      </p>

      <p>
        Everything we have seen so far works on Unix and its descendents,
        such as Linux and Mac OS X.
        Things are a bit different on Windows.
        A typical directory path on a Windows 7 machine might be <code>C:\Users\vlad</code>.
        The first part, <code>C:</code>, is a <a href="glossary.html#drive-letter">drive letter</a>
        that identifies which disk we're talking about.
        This notation dates back to the days of floppy drives,
        and even today,
        each drive is a completely separate filesystem.
      </p>

      <p>
        Instead of a forward slash,
        Windows uses a backslash to separate the names in a path.
        This causes headaches because Unix uses backslash to allow input of special characters.
        For example,
        if we want to put a space in a filename on Unix,
        we would write the filename as <code>my\&nbsp;results.txt</code>.
        Please don't ever do this, though:
        if you put spaces,
        question marks,
        and other special characters in filenames on Unix,
        you can confuse the shell for reasons that we'll see shortly.
      </p>

      <p>
        Finally, Windows filenames and directory names are <a href="glossary.html#case-insensitive">case insensitive</a>:
        upper and lower case letters mean the same thing.
        This means that the path name <code>C:\Users\vlad</code> could be spelled
        <code>c:\users\VLAD</code>,
        <code>C:\Users\Vlad</code>,
        and so on.
        Some people argue that this is more natural:
        after all, "VLAD" in all upper case and "Vlad" spelled normally refer to the same person.
        However,
        it causes headaches for programmers,
        and can be difficult for people to understand
        if their first language doesn't use a cased alphabet.
      </p>

      <div class="box">

        <h3>For Cygwin Users</h3>

        <p>
          <a href="http://www.cygwin.org">Cygwin</a> tries to make Windows paths look more like Unix paths
          by allowing us to use a forward slash instead of a backslash as a separator.
          It also allows us to refer to the C drive as <code>/cygdrive/c/</code> instead of as <code>C:</code>.
          (The latter usually works too, but not always.)
          Paths are still case insensitive,
          though,
          which means that if you try to put files called <code>backup.txt</code> (in all lower case)
          and <code>Backup.txt</code> (with a capital 'B') into the same directory,
          the second will overwrite the first.
        </p>
      </div>

      <section>

        <h3>Nelle's Pipeline: Organizing Files</h3>

        <p>
          Knowing just this much about files and directories,
          Nelle is ready to organize the files that the protein assay machine will create.
          First,
          she creates a directory called <code>north-pacific-gyre</code>
          (to remind herself where the data came from).
          Inside that, she creates a directory called <code>2012-07-03</code>,
          which is the date she started processing the samples.
          She used to use names like <code>conference-paper</code> and <code>revised-results</code>,
          but she found them hard to understand after a couple of years.
          (The final straw was when she found herself creating a directory called
          <code>revised-revised-results-3</code>.)
        </p>

        <p>
          Each of her physical samples is labelled
          according to her lab's convention
          with a unique ten-character ID,
          such as "NENE01729A".
          This is what she used in her collection log to record the location,
          time, depth, and other characteristics of the sample,
          so she decides to use it as part of each data file's name.
          Since the assay machine's output is plain text,
          she will call her files <code>NENE01729A.txt</code>,
          <code>NENE01812A.txt</code>,
          and so on.
          All 1520 files will go into the same directory
          (<a href="#f:pipeline_source_file_layout">Figure 9</a>).
        </p>

        <figure id="f:pipeline_source_file_layout">
          <img src="img/shell/pipeline_source_file_layout.png" alt="Source Files Layout" />
        </figure>

        <p>
          If she is in her home directory,
          Nelle can see what files she has using the command:
        </p>

<pre>
$ <span class="in">ls north-pacific-gyre/2012-07-03/</span>
</pre>

        <p>
          Since this is a lot to type,
          she can take advantage of Bash's
          <a href="glossary.html#command-completion">command completion</a>.
          If she types:
        </p>

<pre>
$ <span class="in">ls no</span>
</pre>

        <p class="continue">
          and then presses <span class="in">tab</span>,
          Bash will automatically complete the directory name for her:
        </p>

<pre>
$ <span class="in">ls north-pacific-gyre/</span>
</pre>

        <p class="continue">
          If she presses tab again,
          Bash will add <code>2012-07-03/</code> to the command,
          since it's the only possible completion.
          Pressing tab again does nothing,
          since there are 1520 possibilities;
          pressing tab twice brings up a list of all the files,
          and so on.
        </p>

      </section>

      <div class="keypoints" id="k:filedir">
        <h3>Summary</h3>
        <ul>
          <li>The file system is responsible for managing information on disk.</li>
          <li>Information is stored in files, which are stored in directories (folders).</li>
          <li>Directories can also store other directories, which forms a directory tree.</li>
          <li><code>/</code> on its own is the root directory of the whole filesystem.</li>
          <li>A relative path specifies a location starting from the current location.</li>
          <li>An absolute path specifies a location from the root of the filesystem.</li>
          <li>Directory names in a path are separated with '/' on Unix, but '\' on Windows.</li>
          <li>'..' means "the directory above the current one"; '.' on its own means "the current directory".</li>
          <li idea="meaning">Most files' names are <code>something.extension</code>; the extension isn't required, and doesn't guarantee anything, but is normally used to indicate the type of data in the file.</li>
          <li><code>cd <em>path</em></code> changes the current working directory.</li>
          <li><code>ls <em>path</em></code> prints a listing of a specific file or directory; <code>ls</code> on its own lists the current working directory.</li>
          <li><code>pwd</code> prints the user's current working directory (current default location in the filesystem).</li>
          <li><code>whoami</code> shows the user's current identity.</li>
          <li>Most commands take options (flags) which begin with a '-'.</li>
        </ul>
      </div>

    </section>

    <section id="s:create">

      <h2>Creating Things</h2>

      <div class="understand" id="u:create">
        <h3>Understand:</h3>
        <ul>
          <li>How to create new files and directories.</li>
          <li>How to delete files and directories.</li>
          <li>How to copy and rename files and directories.</li>
          <li>That deleting really does erase things.</li>
        </ul>
      </div>

      <p>
        We now know how to look at files and directories,
        but how do we create them in the first place?
        Let's go back to Vlad's home directory,
        <code>/users/vlad</code>,
        and use <code>ls -F</code> to see what files and directories it contains:
      </p>

<pre>
$ <span class="in">pwd</span>
<span class="out">/users/vlad</span>
$ <span class="in">ls -F</span>
<span class="out">bin/         data/     mail/      music/
notes.txt    papers/   pizza.cfg  solar/
solar.pdf    swc/</span>
$
</pre>

      <p>
        Let's create a new directory called <code>tmp</code>
        using the command <code>mkdir tmp</code>
        (which has no output):
      </p>

<pre>
$ <span class="in">mkdir tmp</span>
$
</pre>

      <p class="continue">
        As you might (or might not) guess from its name,
        <code>mkdir</code> means "make directory".
        Since <code>tmp</code> is a relative path
        (i.e., doesn't have a leading slash),
        the new directory is made below the current one:
      </p>

<pre>
$ <span class="in">ls -F</span>
<span class="out">bin/         data/     mail/      music/
notes.txt    papers/   pizza.cfg  solar/
solar.pdf    swc/      tmp/</span>
$
</pre>

      <p class="continue">
        However, there's nothing in it yet&mdash;<code>tmp</code> is empty:
      </p>

<pre>
$ <span class="in">ls -F tmp</span>
$
</pre>

      <p>
        Let's change our working directory to <code>tmp</code> using <code>cd</code>,
        then run the command <code>nano junk</code>:
      </p>

<pre>
$ <span class="in">cd tmp</span>
$ <span class="in">nano junk</span>
</pre>

      <p class="continue">
        <code>nano</code> is a very simple text editor that only a programmer could really love.
        <a href="#f:nano">Figure 10</a>
        shows what it looks like when it runs:
      </p>

      <figure id="f:nano">
        <img src="img/shell/nano.png" alt="The Nano Editor" />
      </figure>

      <p class="continue">
        The cursor is the blinking square in the upper left;
        it shows us where what we type will be inserted.
        Let's type in a short quotation:
      </p>

      <figure id="f:nano_quotation">
        <img src="img/shell/nano_quotation.png" alt="Nano in Action" />
      </figure>

      <p class="continue">
        then use <span class="in">Control-O</span> to write our data to disk.
        (By convention,
        Unix documentation uses the caret <code>^</code> followed by a letter
        to mean "control plus that letter".)
        Once our quotation is saved,
        we can use <span class="in">Control-X</span> to quit the editor and return to the shell.
      </p>

      <div class="box">

        <h3>Why Nano?</h3>

        <p>
          When we say, "<code>nano</code> is a text editor,"
          we really do mean "text":
          it can only work with plain character data,
          not tables,
          images,
          or any other human-friendly media.
          We'll use it in this chapter because
          almost anyone can use it anywhere without training,
          but we'll use more powerful tools for programming,
          editing HTML,
          and so on.
        </p>

      </div>

      <p>
        <code>nano</code> doesn't leave any output on the screen after it exits.
        But <code>ls</code> now shows that we have created a file called <code>junk</code>:
      </p>

<pre>
$ <span class="in">ls</span>
<span class="out">junk</span>
$
</pre>

      <p>
        We can run <code>ls</code> with the <code>-s</code> flag
        to show us how big the file we just created is:
      </p>

<pre>
$ <span class="in">ls -s</span>
<span class="out">   1  junk</span>
$
</pre>

      <p class="continue">
        Unfortunately,
        by default Unix reports sizes in disk blocks,
        which just might be the least helpful default imaginable.
        If we add the <code>-h</code> flag,
        <code>ls</code> switches to more human-friendly units:
      </p>

<pre>
$ <span class="in">ls -s -h</span>
<span class="out"> 512  junk</span>
$
</pre>

      <p class="continue">
        Here, 512 is the number of bytes the file takes up.
        This is more than we actually typed in because
        the smallest unit of storage on the disk is typically a block of 512 bytes.
      </p>

      <p>
        Let's tidy up by running <code>rm junk</code>:
      </p>

<pre>
$ <span class="in">rm junk</span>
$
</pre>

      <p class="continue">
        This command removes files ("rm" is short for "remove").
        If we now run <code>ls</code> again,
        its output is empty once more,
        which tells us that our file is gone:
      </p>

<pre>
$ <span class="in">ls</span>
$
</pre>

      <div class="box">

        <h3>Deleting Is Forever</h3>

        <p>
          It's important to remember that Unix doesn't have a trash bin:
          when we delete files,
          they are unhooked from the file system
          so that their storage space on disk can be recycled.
          Tools for finding and recovering deleted files do exist,
          but there's no guarantee they'll work in any particular situation,
          since the computer may recycle the file's disk space right away.
        </p>

      </div>

      <p>
        Let's re-create that file
        and then move up one directory to <code>/users/vlad</code> using <code>cd ..</code>:
      </p>

<pre>
$ <span class="in">pwd</span>
<span class="out">/users/vlad/tmp</span>
$ <span class="in">nano junk</span>
$ <span class="in">ls</span>
<span class="out">junk</span>
$ <span class="in">cd ..</span>
$
</pre>

      <p class="continue">
        If we try to remove the <code>tmp</code> directory using <code>rm tmp</code>,
        we get an error message:
      </p>

<pre>
$ <span class="in">rm tmp</span>
<span class="err">rm: cannot remove `tmp': Is a directory</span>
$
</pre>

      <p class="continue">
        This happens because <code>rm</code> only works on files, not directories.
        The right command is <code>rmdir</code>, which is short for "remove directory":
        It doesn't work yet either, though,
        because the directory we're trying to remove isn't empty:
      </p>

<pre>
$ <span class="in">rmdir tmp</span>
<span class="err">rmdir: failed to remove `tmp': Directory not empty</span>
$
</pre>

      <p class="continue">
        (This little safety feature can save you a lot of grief,
        particularly if you are a bad typist.)
        If we want to get rid of <code>tmp</code> we must first delete the file <code>junk</code>:
      </p>

<pre>
$ <span class="in">rm tmp/junk</span>
$
</pre>

      <p class="continue">
        The directory is now empty,
        so <code>rmdir</code> can delete it:
      </p>

<pre>
$ <span class="in">rmdir tmp</span>
$
</pre>

      <p>
        Let's create that directory and file one more time.
        (Note that this time we're running <code>nano</code> with the path <code>tmp/junk</code>,
        rather than going into the <code>tmp</code> directory
        and running <code>nano</code> on <code>junk</code> there.)
      </p>

<pre>
$ <span class="in">pwd</span>
<span class="out">/users/vlad/tmp</span>
$ <span class="in">mkdir tmp</span>
$ <span class="in">nano tmp/junk</span>
$ <span class="in">ls tmp</span>
<span class="out">junk</span>
$
</pre>

      <p class="continue">
        <code>junk</code> isn't a particularly informative name,
        so let's change the file's name using <code>mv</code>,
        which is short for "move":
      </p>

<pre>
$ <span class="in">mv tmp/junk tmp/quotes.txt</span>
$
</pre>

      <p class="continue">
        The first argument tells <code>mv</code> what we're moving,
        while the second is where it's to go.
        In this case,
        we're moving <code>tmp/junk</code> to <code>tmp/quotes.txt</code>,
        which has the same effect as renaming the file.
        Sure enough,
        <code>ls</code> shows us that <code>tmp</code> now contains one file called <code>quotes.txt</code>:
      </p>

<pre>
$ <span class="in">ls tmp</span>
<span class="out">quotes.txt</span>
$
</pre>

      <p class="continue">
        Just for the sake of inconsistency,
        <code>mv</code> also works on directories&mdash;there
        is no separate <code>mvdir</code> command.
      </p>

      <p>
        Let's move that file into the current working directory.
        We use <code>mv</code> once again,
        but this time,
        the second argument is the name of a directory,
        which is the directory we want that file to put in.
        In this case,
        the special directory name <code>.</code> that we <a href="#a:dot-directory">mentioned earlier</a>):
      </p>

<pre>
$ <span class="in">mv tmp/quotes.txt .</span>
$
</pre>

      <p class="continue">
        The effect is to move the file from the directory it was in
        to the current directory.
        <code>ls</code> now shows us that <code>tmp</code> is now empty,
        and that <code>quotes.txt</code> is in our current directory.
        Notice that <code>ls</code> with a filename or directory name as an argument
        only lists that file or directory:
      </p>

<pre>
$ <span class="in">ls tmp</span>
$ <span class="in">ls quotes.txt</span>
<span class="out">quotes.txt</span>
$
</pre>

      <p>
        The <code>cp</code> command works very much like <code>mv</code>,
        except it copies a file instead of moving it.
        We can check that it did the right thing
        using <code>ls</code> with two paths as arguments&mdash;like many other Unix commands,
        <code>ls</code> can process thousands of paths at once:
      </p>

<pre>
$ <span class="in">cp quotes.txt tmp/quotations.txt</span>
$ <span class="in">ls quotes.txt tmp/quotations.txt</span>
<span class="out">quotes.txt   tmp/quotations.txt</span>
$
</pre>

      <p>
        To prove that we made a copy,
        let's delete the <code>quotes.txt</code> file in the current directory,
        and then run that same <code>ls</code> again.
        This time,
        it tells us that it can't find <code>quotes.txt</code> in the current directory,
        but it does find the copy in <code>tmp</code> that we didn't delete:
      </p>

<pre>
$ <span class="in">ls quotes.txt tmp/quotations.txt</span>
<span class="err">ls: cannot access quotes.txt: No such file or directory</span>
<span class="out">tmp/quotations.txt</span>
$
</pre>

      <p>
        Let's make one more copy.
        This time,
        though,
        we don't specify the destination filename,
        just a directory, so the copy will keep the original's filename:
      </p>

<pre>
$ <span class="in">cp tmp/quotations.txt .</span>
$ <span class="in">ls quotations.txt</span>
<span class="out">quotations.txt</span>
$
</pre>

      <div class="box">

        <h3>Alphabet Soup</h3>

        <p>
          <code>mv</code> probably isn't the first thing that springs to mind
          when you want to rename a file.
          And why is it <code>cp</code> instead of plain old <code>copy</code>?
          The usual answer is that in the early 1970s,
          when Unix was first being developed,
          every keystroke counted:
          the devices of the day were slow,
          and backspacing on a teletype was so painful
          that cutting the number of keystrokes
          in order to cut the number of typing mistakes
          was actually a win for usability.
        </p>

        <p>
          Ever since,
          people have complained about how cryptic Unix commands are,
          and about how hard they are to learn and remember.
          In 1983,
          <a href="bib.html#deleon-trouble-with-unix">De Leon and colleagues</a>
          found that while Unix commands weren't harder for novice users to learn,
          they were probably more difficult for them to use.
          We're stuck with them now,
          though,
          just as we're stuck with the roolz uv Inglish speling.
        </p>

      </div>

      <div class="keypoints" id="k:create">
        <h3>Summary</h3>
        <ul>
          <li>Unix documentation uses '^A' to mean "control-A".</li>
          <li>The shell does <em>not</em> have a trash bin: once something is deleted, it's really gone.</li>
          <li><code>mkdir <em>path</em></code> creates a new directory.</li>
          <li><code>cp <em>old</em> <em>new</em></code> copies a file.</li>
          <li><code>mv <em>old</em> <em>new</em></code> moves (renames) a file or directory.</li>
          <li><code>nano</code> is a very simple text editor&mdash;please use something else for real work.</li>
          <li><code>rm <em>path</em></code> removes (deletes) a file.</li>
          <li><code>rmdir <em>path</em></code> removes (deletes) an empty directory.</li>
        </ul>
      </div>

    </section>

    <section id="s:pipefilter">

      <h2>Pipes and Filters</h2>

      <div class="understand" id="u:pipefilter">
        <h3>Understand:</h3>
        <ul>
          <li>How to use wildcards to match filenames.</li>
          <li>That wildcards are expanded by the shell before commands are run.</li>
          <li>How to redirect a command's output to a file.</li>
          <li>How to redirect a command's input from a file.</li>
          <li>How to use the output of one command as the input to another with a pipe.</li>
          <li>That combining single-purpose filters with pipes is the most productive way to use the shell.</li>
          <li>That if a program conforms to Unix conventions, it can easily be combined with others.</li>
        </ul>
      </div>

      <p>
        Now that we know a few basic commands,
        we can finally look at its most powerful feature:
        the ease with which it lets you combine existing programs in new ways.
        We'll start with a directory called <code>molecules</code>
        that contains six files describing some simple organic molecules.
        The <code>.pdb</code> extension indicates that these files are in Protein Data Bank format,
        a simple text format that specifies the type and position of each atom in the molecule.
      </p>

<pre>
$ <span class="in">ls molecules</span>
<span class="out">cubane.pdb    ethane.pdb    methane.pdb
octane.pdb    pentane.pdb   propane.pdb</span>
$
</pre>

      <p>
        Let's go into that directory with <code>cd</code>
        and run the command <code>wc *.pdb</code>.
        <code>wc</code> is the "word count" command:
        it counts the number of lines, words, and characters in files.
        The <code>*</code> in <code>*.pdb</code> matches zero or more characters,
        so the shell turns <code>*.pdb</code> into a complete list of <code>.pdb</code> files:
      </p>

<pre>
$ <span class="in">cd molecules</span>
$ <span class="in">wc *.pdb</span>
<span class="out">  20  156 1158 cubane.pdb
  12   84  622 ethane.pdb
   9   57  422 methane.pdb
  30  246 1828 octane.pdb
  21  165 1226 pentane.pdb
  15  111  825 propane.pdb
 107  819 6081 total</span>
$
</pre>

      <div class="box">

        <h3>Wildcards</h3>

        <p>
          <code>*</code> is a <a href="glossary.html#wildcard">wildcard</a>.
          It matches zero or more characters,
          so <code>*.pdb</code> matches <code>ethane.pdb</code>,
          <code>propane.pdb</code>,
          and so on.
          On the other hand,
          <code>p*.pdb</code> only matches <code>pentane.pdb</code> and <code>propane.pdb</code>,
          because the 'p' at the front only matches itself.
        </p>

        <p>
          <code>?</code> is also a wildcard,
          but it only matches a single character.
          This means that <code>p?.pdb</code> matches <code>pi.pdb</code> or <code>p5.pdb</code>,
          but not <code>propane.pdb</code>.
          We can use any number of wildcards at a time:
          for example,
          <code>p*.p?*</code> matches anything that starts with a 'p'
          and ends with '.', 'p', and at least one more character
          (since the '?' has to match one character,
          and the final '*' can match any number of characters).
          Thus,
          <code>p*.p?*</code> would match
          <code>preferred.practice</code>,
          and even <code>p.pi</code>
          (since the first '*' can match no characters at all),
          but not <code>quality.practice</code> (doesn't start with 'p')
          or <code>preferred.p</code> (there isn't at least one character after the '.p').
        </p>

        <p>
          When the shell sees a wildcard,
          it expands it to create a list of filenames
          <em>before</em> passing those names to whatever command is being run
          (<a href="#f:wildcard_expansion">Figure 12</a>).
          This means that commands like <code>wc</code> and <code>ls</code> never actually see the wildcards:
          all they see are what those wildcards matched.
        </p>

        <figure id="f:wildcard_expansion">
          <img src="img/shell/wildcard_expansion.png" alt="Wildcard Expansion" />
        </figure>

      </div>

      <p>
        If we run <code>wc -l</code> instead of just <code>wc</code>,
        the output shows only the number of lines per file:
      </p>

<pre>
$ <span class="in">wc -l *.pdb</span>
<span class="out">  20  cubane.pdb
  12  ethane.pdb
   9  methane.pdb
  30  octane.pdb
  21  pentane.pdb
  15  propane.pdb
 107  total</span>
$
</pre>

      <p class="continue">
        We can use <code>-w</code> to get only the number of words,
        or <code>-c</code> to get only the number of characters.
      </p>

      <p>
        Now, which of these files is shortest?
        It's an easy question to answer when there are only six files, but what if there were 6000?
        That's the kind of job we want a computer to do.
      </p>

      <p>
        Our first step toward a solution is to run the command:
      </p>

<pre>
$ <span class="in">wc -l *.pdb > lengths</span>
</pre>

      <p class="continue">
        The <code>&gt;</code> tells the shell to <a href="glossary.html#redirection">redirect</a>
        the command's output to a file
        instead of printing it to the screen.
        The shell will create the file if it doesn't exist,
        or overwrite the contents of that file if it does:
      </p>

<pre>
$ <span class="in">wc -l *.pdb > lengths</span>
$
</pre>

      <p>
        Notice that there is no screen output:
        everything that <code>wc</code> would have printed has gone into the file <code>lengths</code> instead.
        <code>ls lengths</code> confirms that the file exists:
      </p>

<pre>
$ <span class="in">ls lengths</span>
<span class="out">lengths</span>
$
</pre>

      <p class="continue">
        We can print the content of <code>lengths</code> to the screen using <code>cat lengths</code>.
        <code>cat</code> stands for "concatenate": it prints the contents of files one after another.
        In this case, there's only one file, so <code>cat</code> just shows us what's in it:
      </p>

<pre>
$ <span class="in">cat lengths</span>
<span class="out">  20  cubane.pdb
  12  ethane.pdb
   9  methane.pdb
  30  octane.pdb
  21  pentane.pdb
  15  propane.pdb
 107  total</span>
$
</pre>

      <p>
        Now let's use the <code>sort</code> command to sort its contents.
        This does <em>not</em> change the file.
        Instead, it prints the sorted result to the screen:
      </p>

<pre>
$ <span class="in">sort lengths</span>
<span class="out">  9  methane.pdb
 12  ethane.pdb
 15  propane.pdb
 20  cubane.pdb
 21  pentane.pdb
 30  octane.pdb
107  total</span>
$
</pre>

      <p>
        We can put the sorted list of lines in another temporary file called <code>sorted-lengths</code>
        by putting <code>&gt; sorted-lengths</code> after the command,
        just as we used <code>&gt; lengths</code> to put the output of <code>wc</code> into <code>lengths</code>.
        Once we've done that,
        we can run another command called <code>head</code> to get the first few lines in <code>sorted-lengths</code>:
      </p>

<pre>
$ <span class="in">sort lengths > sorted-lengths</span>
$ <span class="in">head -1 sorted-lengths</span>
<span class="out">  9  methane.pdb</span>
$
</pre>

      <p class="continue">
        Giving <code>head</code> the argument <code>-1</code> tells us we only want the first line of the file;
        <code>-20</code> would get the first 20, and so on.
        The output must be the file with the fewest lines,
        since <code>sorted-lengths</code> the lengths of our files
        ordered from least to greatest.
      </p>

      <p>
        If you think this is confusing, you're in good company:
        even once you understand what <code>wc</code>, <code>sort</code>, and <code>head</code> do,
        all those intermediate files make it hard to follow what's going on.
        How can we make it easier to understand?
      </p>

      <p>
        Let's start by getting rid of the <code>sorted-lengths</code> file
        by running <code>sort</code> and <code>head</code> together:
      </p>

<pre>
$ <span class="in">sort lengths | head -1</span>
<span class="out">  9  methane.pdb</span>
$
</pre>

      <p class="continue">
        The vertical bar between the two commands
        is called a <a href="glossary.html#pipe">pipe</a>.
        It tells the shell that we want to use the output of the command on the left
        as the input to the command on the right
        without creating a temporary file.
        The computer might create such a file itself if it wants to,
        run the two programs simultaneously and pass data from one to the other through memory,
        or do something else entirely:
        we don't have to know or care.
      </p>

      <p>
        Well, if we don't need to create the temporary file <code>sorted-lengths</code>,
        can we get rid of the <code>lengths</code> file too?
        The answer is "yes":
        we can use another pipe to send the output of <code>wc</code> directly to <code>sort</code>,
        which then sends its output to <code>head</code>:
      </p>

<pre>
$ <span class="in">wc -l *.pdb | sort | head -1</span>
<span class="out">  9  methane.pdb</span>
$
</pre>

      <p class="continue">
        This is exactly like a mathematician nesting functions like <em>sin(&pi;x)<sup>2</sup></em>
        and saying "the square of the sine of <em>x</em> times &pi;":
        in our case, the calculation is "head of sort of word count of <code>*.pdb</code>".
      </p>

      <p>
        This simple idea is why Unix has been so successful.
        Instead of creating enormous programs that try to do many different things,
        Unix programmers focus on creating lots of simple tools that each do one job well,
        and work well with each other.
        Ten such tools can be combined in 100 ways, and that's only looking at pairings:
        when we start to look at pipes with multiple stages,
        the possibilities are almost uncountable.
      </p>

      <div class="box" id="s:pipefilter:pipes">

        <h3>Inside Pipes</h3>

        <p>
          Here's what actually happens behind the scenes when we create a pipe.
          In order to run a program&mdash;any program&mdash;the computer creates a <a href="glossary.html#process">process</a>,
          which we'll represent as an octagon.
          Every process has an input channel called <a href="glossary.html#standard-input">standard input</a>.
          (By this point, you may be surprised that the name is so memorable, but don't worry:
          most Unix programmers call it <a href="glossary.html#stdin">stdin</a>.)
          Every process also has a default output channel called <a href="glossary.html#standard-output">standard output</a>,
          or <a href="glossary.html#stdout">stdout</a>
          (<a href="#f:process_stdin_stdout">Figure 13</a>).
        </p>

        <figure id="f:process_stdin_stdout">
          <img src="img/shell/process_stdin_stdout.png" alt="A Process with Standard Input and Output" />
        </figure>

        <p>
          The shell is just another program, and runs in a process like any other.
          Under normal circumstances,
          whatever we type on the keyboard is sent to the shell on its standard input,
          and whatever it produces on standard output is displayed on our screen
          (<a href="#f:shell_as_process">Figure 14</a>):
        </p>

        <figure id="f:shell_as_process">
          <img src="img/shell/shell_as_process.png" alt="The Shell as a Process" />
        </figure>

        <p>
          When we run a program,
          the shell creates a new process.
          It then temporarily sends whatever we type on our keyboard to that process's standard input,
          and copies whatever the process prints to standard output to the screen
          (<a href="#f:running_a_process">Figure 15</a>):
        </p>

        <figure id="f:running_a_process">
          <img src="img/shell/running_a_process.png" alt="Running a Process" />
        </figure>

        <p>
          Here's what happens when we run <code>wc -l *.pdb &gt; lengths</code>.
          The shell starts by telling the computer to create a new process to run the <code>wc</code> program.
          Since we've provided some filenames as arguments,
          <code>wc</code> reads from them instead of from standard input.
          And since we've used <code>&gt;</code> to redirect output to a file,
          the shell connects the process's standard output to that file
          (<a href="#f:running_wc">Figure 16</a>):
        </p>

        <figure id="f:running_wc">
          <img src="img/shell/running_wc.png" alt="Running One Program with Redirection" />
        </figure>

        <p>
          If we run <code>wc -l *.pdb | sort</code> instead,
          the shell creates two processes,
          one for each component of the pipe,
          so that <code>wc</code> and <code>sort</code> run simultaneously.
          The standard output of <code>wc</code> is fed directly to the standard input of <code>sort</code>;
          since there's no redirection with <code>&gt;</code>, <code>sort</code>'s output goes to the screen
          (<a href="#f:running_wc_sort">Figure 17</a>):
        </p>

        <figure id="f:running_wc_sort">
          <img src="img/shell/running_wc_sort.png" alt="Running Two Programs in a Pipe" />
        </figure>

        <p>
          And if we run <code>wc -l *.pdb | sort | head -1</code>,
          we get the three processes shown here,
          with data flowing from the files,
          through <code>wc</code> to <code>sort</code>,
          and from <code>sort</code> through <code>head</code> to the screen
          (<a href="#f:running_wc_sort_head">Figure 18</a>):
        </p>

        <figure id="f:running_wc_sort_head">
          <img src="img/shell/running_wc_sort_head.png" alt="Running the Full Pipeline" />
        </figure>

      </div>

      <p>
        This programming model is called <a href="glossary.html#pipe-and-filter">pipes and filters</a>.
        We've already seen pipes;
        a <a href="glossary.html#filter">filter</a> is
        a program that transforms a stream of input into a stream of output.
        Almost all of the standard Unix tools can work this way:
        unless told to do otherwise,
        they read from standard input,
        do something with what they've read,
        and write to standard output.
      </p>

      <p>
        The key is that any program that reads lines of text from standard input,
        and writes lines of text to standard output,
        can be combined with every other program that behaves this way as well.
        You can <em>and should</em> write your programs this way,
        so that you and other people can put those programs into pipes to multiply their power.
      </p>

      <div class="box">

        <h3>Redirecting Input</h3>

        <p>
          As well as using <code>&gt;</code> to redirect a program's output,
          we can use <code>&lt;</code> to redirect its input,
          i.e.,
          to read from a file instead of from standard input.
          For example, instead of writing <code>wc ammonia.pdb</code>,
          we could write <code>wc &lt; ammonia.pdb</code>.
          In the first case,
          <code>wc</code> gets a command line argument telling it what file to open.
          In the second,
          <code>wc</code> doesn't have any command line arguments,
          so it reads from standard input,
          but we have told the shell to send the contents of <code>ammonia.pdb</code> to <code>wc</code>'s standard input.
        </p>

      </div>

      <section>

        <h3>Nelle's Pipeline: Checking Files</h3>

        <p>
          Nelle has run her samples through the assay machines
          and created 1520 files in the <code>north-pacific-gyre/2012-07-03</code> directory
          described earlier.
          As a quick sanity check,
          she types:
        </p>

<pre>
$ <span class="in">cd north-pacific-gyre/2012-07-03</span>
$ <span class="in">wc -l *.txt</span>
</pre>

        <p class="continue">
          The output is 1520 lines that look like this:
        </p>

<pre>
 300 NENE01729A.txt
 300 NENE01729B.txt
 300 NENE01736A.txt
 300 NENE01751A.txt
 300 NENE01751B.txt
 300 NENE01812A.txt
 ... ...
</pre>

        <p>
          Now she types this:
        </p>

<pre>
$ <span class="in">wc -l *.txt | sort | head -5</span>
 240 NENE02018B.txt
 300 NENE01729A.txt
 300 NENE01729B.txt
 300 NENE01736A.txt
 300 NENE01751A.txt
</pre>

        <p class="continue">
          Whoops:
          one of the files is 60 lines shorter than the others.
          When she goes back and checks it,
          she sees that she did that assay at 8:00 on a Monday morning&mdash;someone
          was probably in using the machine on the weekend,
          and she forgot to reset it.
          Before re-running that sample,
          she checks to see if any files have too much data:
        </p>

<pre>
$ <span class="in">wc -l *.txt | sort | <span class="highlight">tail</span> -5</span>
 300 NENE02040A.txt
 300 NENE02040B.txt
 300 NENE02040Z.txt
 300 NENE02043A.txt
 300 NENE02043B.txt
</pre>

        <p>
          Those numbers look good&mdash;but what's that 'C' doing there in the third-to-last line?
          All of her samples should be marked 'A' or 'B';
          by convention,
          her lab uses 'Z' to indicate samples with missing information.
          To find others like it,
          she does this:
        </p>
<pre>
$ <span class="in">ls *Z.txt</span>
NENE01971Z.txt    NENE02040Z.txt
</pre>

        <p class="continue">
          Sure enough,
          when she checks the log on her laptop,
          there's no depth recorded for either of those samples.
          Since it's too late to get the information any other way,
          she must exclude those two files from her analysis.
          She could just delete them using <code>rm</code>,
          but there are actually some analyses she might do later
          where depth doesn't matter,
          so instead,
          she'll just be careful later on to select files using the wildcard expression
          <code>*[AB].txt</code>.
          As always, the '*' matches any number of characters;
          the new expression <code>[AB]</code>
          matches either an 'A' or a 'B',
          so this matches all the valid data files she has.
        </p>

      </section>

      <div class="keypoints" id="k:pipefilter">
        <h3>Summary</h3>
        <ul>
          <li idea="perf">Use wildcards to match filenames.</li>
          <li>'*' is a wildcard pattern that matches zero or more characters in a pathname.</li>
          <li>'?' is a wildcard pattern that matches any single character.</li>
          <li>The shell matches wildcards before running commands.</li>
          <li><code><em>command</em> &gt; <em>file</em></code> redirects a command's output to a file.</li>
          <li><code><em>first</em> | <em>second</em></code> is a pipeline: the output of the first command is used as the input to the second.</li>
          <li idea="tools">The best way to use the shell is to use pipes to combine simple single-purpose programs (filters).</li>
          <li><code>cat</code> displays the contents of its inputs.</li>
          <li><code>head</code> displays the first few lines of its input.</li>
          <li><code>sort</code> sorts its inputs.</li>
          <li><code>tail</code> displays the last few lines of its input.</li>
          <li><code>wc</code> counts lines, words, and characters in its inputs.</li>
        </ul>
      </div>

    </section>

    <section id="s:loop">

      <h2>Loops</h2>

      <div class="understand" id="u:loop">
        <h3>Understand:</h3>
        <ul>
          <li>How to repeat operations using a loop.</li>
          <li>That the loop variable takes on a different value each time through the loop.</li>
          <li>The difference between a variable's name and its value.</li>
          <li>Why spaces and some punctuation characters shouldn't be used in files' names.</li>
          <li>How to display history and re-use commands.</li>
        </ul>
      </div>

      <p>
        Wildcards and tabs are one way to save on typing.
        Another,
        which is much more powerful,
        is to tell the shell to do something over and over again.
        Suppose we have several hundred genome data files in a directory
        with names like <code>genome-unicorn.dat</code>,
        <code>genome-basilisk.dat</code>,
        and so on.
        Some new files have just arrived,
        so we'd like to rename all the existing ones to
        <code>original-genome-unicorn.dat</code>,
        <code>original-genome-basilisk.dat</code>,
        etc.
        We can't use:
      </p>

<pre>
mv *.dat original-*.dat
</pre>

      <p class="continue">
        because that would expand (in the two-file case) to:
      </p>

<pre>
mv basilisk.dat unicorn.dat
</pre>

      <p class="continue">
        (<code>original-*.dat</code> would expand to nothing,
        because there aren't any files with names like that yet.)
        This wouldn't back up our files:
        it would replace the content of <code>unicorn.dat</code>
        with whatever's in <code>basilisk.dat</code>.
      </p>

      <p>
        Here's what we can do instead:
      </p>

<pre>
for filename in *.dat; do mv $filename original-$filename; done
</pre>

      <p class="continue">
        If we're typing interactively,
        we can make this easier to read using carriage returns:
      </p>

<pre>
for filename in *.dat
do
  mv $filename original-$filename
done
</pre>

      <p>
        This is called a <a href="glossary.html#for-loop">for loop</a>,
        because it does something <em>for</em> each thing in a list.
        The shell starts by expanding the wildcard pattern <code>*.dat</code> to a list of files,
        so that this loop is equivalent to:
      </p>

<pre>
for filename in genome-basilisk.dat genome-unicorn.dat
do
  mv $filename original-$filename
done
</pre>

      <p class="continue">
        It then runs the command inside the loop&mdash;the <code>mv</code>&mdash;once
        for each name in that list.
        Each time through the loop,
        a different filename is assigned to the variable <code>filename</code>.
        We get the variable's value by putting a <code>$</code> in front of it,
        so <code>original-$filename</code> is
        <code>original-basilisk.dat</code> when <code>filename</code> is <code>basilisk.dat</code>,
        <code>original-unicorn.dat</code> when <code>filename</code> is <code>unicorn.dat</code>,
        and so on.
      </p>

      <p>
        Here's another, more complicated, loop:
      </p>

<pre>
for filename in *.dat
do
  head -100 $filename | tail -20
done
</pre>

      <p>
        Again,
        the loop is executed once for each file.
        The <a href="glossary.html#loop-body">loop body</a> then selects
        lines 80-100 from each of those files.
        It doesn't tell us which file each group of lines is from, though;
        if we wanted that,
        we could change the loop to:
      </p>

<pre>
for filename in *.dat
do
  echo $filename
  head -100 $filename | tail -20
done
</pre>

      <p class="continue">
        The <code>echo</code> command just prints its command-line arguments to standard output,
        so in this case,
        it just displays the filename.
        We can't just write:
      </p>

<pre>
for filename in *.dat
do
  <span class="highlight">$filename</span>
  head -100 $filename | tail -20
done
</pre>

      <p class="continue">
        because then the first time through the loop,
        when <code>$filename</code> expanded to <code>genome-basilisk.dat</code>,
        the shell would try to run that file as a program.
      </p>

      <div class="box">

        <h3>Spaces in Names</h3>

        <p>
          Loops like these are why you should <em>not</em> use spaces in filenames.
          Suppose our data files are named:
        </p>

<pre>
basilisk.dat
red dragon.dat
unicorn.dat
</pre>

        <p class="continue">
          If we try to process them using:
        </p>

<pre>
for filename in *.dat
do
  head -100 $filename | tail -20
done
</pre>

        <p class="continue">
          then <code>*.dat</code> will expand to:
        </p>

<pre>
basilisk.dat red dragon.dat unicorn.dat
</pre>

        <p class="continue">
          which means that <code>filename</code> will be assigned
          each of the following values in turn:
        </p>

<pre>
basilisk.dat
<span class="highlight">red
dragon.dat</span>
unicorn.dat
</pre>

        <p>
          The highlighted lands show the problem:
          instead of getting one name <code>red&nbsp;dragon.dat</code>,
          the commands in the loop will get <code>red</code> and <code>dragon.dat</code> separately.
          To make matters worse,
          the file <code>red&nbsp;dragon.dat</code> won't be processed at all.
          There are ways to get around this,
          but the safest thing is to use dashes,
          underscores,
          or some other printable character instead.
        </p>

      </div>

      <section>

        <h3>Nelle's Pipeline: Processing Files</h3>

        <p>
          Nelle is now ready to process her data files.
          Since she's still learning how to use the shell,
          she decides to build up the required commands in stages.
          Her first step is to make sure that she can select the right files&mdash;remember,
          these are ones whose names end in 'A' or 'B', rather than 'Z':
        </p>

<pre>
$ <span class="in">cd north-pacific-gyre/2012-07-03</span>
$ <span class="in">for datafile in *[AB].txt
do
  echo $datafile
done</span>
<span class="out">NENE01729A.txt
NENE01729B.txt
NENE01736A.txt
...
NENE02043A.txt
NENE02043B.txt</span>
$
</pre>

        <p>
          Her next step is to figure out what to call the files
          that the <code>goostat</code> analysis program will create.
          Prefixing each input file's name with "stats" seems simple,
          so she modifies her loop to do that:
        </p>

<pre>
$ <span class="in">for datafile in *[AB].txt
do
  echo $datafile stats-$datafile
done</span>
<span class="out">NENE01729A.txt stats-NENE01729A.txt
NENE01729B.txt stats-NENE01729B.txt
NENE01736A.txt stats-NENE01736A.txt
...
NENE02043A.txt stats-NENE02043A.txt
NENE02043B.txt stats-NENE02043B.txt</span>
$
</pre>

        <p class="continue">
          She hasn't actually run <code>goostats</code> yet,
          but now she's sure she can select the right files
          and generate the right output filenames.
        </p>

        <p id="a:repeat">
          Typing in commands over and over again is becoming tedious,
          though,
          and Nelle is worried about making mistakes,
          so instead of re-entering her loop,
          she presses the up arrow.
          In response,
          Bash redisplays the whole loop on one line
          (using semi-colons to separate the pieces):
        </p>

<pre>
$ <span class="in">for datafile in *[AB].txt; do echo $datafile stats-$datafile; done</span>
</pre>

        <p class="continue">
          Using the left arrow key,
          Nelle backs up and changes the command <code>echo</code> to <code>goostats</code>:
        </p>

<pre>
$ <span class="in">for datafile in *[AB].txt; do <span class="highlight">goostats</span> $datafile stats-$datafile; done</span>
</pre>

        <p>
          When she presses enter,
          Bash runs the modified command.
          However,
          nothing appears to happen&mdash;there is no output.
          After a moment,
          Nelle realizes that since her script doesn't print anything to the screen any longer,
          she has no idea whether it is running,
          much less how quickly.
          She kills the job by typing Control-C,
          uses up-arrow to repeat the command,
          and edits it to read:
        </p>

<pre>
$ <span class="in">for datafile in *[AB].txt; do <span class="highlight">echo $datafile;</span> goostats $datafile stats-$datafile; done</span>
</pre>

        <p class="continue">
          When she runs her program now,
          it produces one line of output every five seconds or so:
        </p>

<pre>
<span class="out">NENE01729A.txt
NENE01729B.txt
NENE01736A.txt
...</span>
$
</pre>

        <p class="continue">
          1518 times 5 seconds, divided by 60,
          tells her that her script will take about two hours to run.
          As a final check,
          she opens another terminal window,
          goes into <code>north-pacific-gyre/2012-07-03</code>,
          and uses <code>cat NENE01729B.txt</code> to examine
          one of the output files.
          It looks good,
          so she decides to get some coffee and catch up on her reading.
        </p>

        <div class="box">

          <h3>Those Who Know History Can Choose to Repeat It</h3>

          <p>
            Another way to repeat previous work is to use the <code>history</code> command
            to get a list of the last few hundred commands that have been executed,
            and then to use <code>!123</code> (where "123" is replaced by the command number)
            to repeat one of those commands.
            For example,
            if Nelle types this:
          </p>

<pre>
$ <span class="in">$ history | tail -5</span>
<span class="out">  456  ls -l NENE0*.txt
  457  rm stats-NENE01729B.txt.txt
  458  goostats NENE01729B.txt stats-NENE01729B.txt
  459  ls -l NENE0*.txt
  460  history</span>
</pre>

          <p class="continue">
            then she can re-run <code>goostats</code> on <code>NENE01729B.txt</code>
            simply by typing <code>!458</code>.
          </p>

        </div>

      </section>

      <div class="keypoints" id="k:loop">
        <h3>Summary</h3>
        <ul>
          <li idea="perf">Use a <code>for</code> loop to repeat commands once for every thing in a list.</li>
          <li>Every <code>for</code> loop needs a variable to refer to the current "thing".</li>
          <li>Use <code>$<em>name</em></code> to expand a variable (i.e., get its value).</li>
          <li>Do not use spaces, quotes, or wildcard characters such as '*' or '?' in filenames, as it complicates variable expansion.</li>
          <li idea="paranoia">Give files consistent names that are easy to match with wildcard patterns to make it easy to select them for looping.</li>
          <li idea="perf;paranoia">Use the up-arrow key to scroll up through previous commands to edit and repeat them.</li>
          <li idea="perf;paranoia">Use <code>history</code> to display recent commands, and <code>!<em>number</em></code> to repeat a command by number.</li>
          <li>Use ^C (control-C) to terminate a running command.</li>
        </ul>
      </div>

    </section>

    <section id="s:scripts">

      <h2>Shell Scripts</h2>

      <div class="understand" id="u:scripts">
        <h3>Understand:</h3>
        <ul>
          <li>How to store shell commands in a file for re-use.</li>
          <li>How to run a shell script.</li>
          <li>How to pass filenames into a shell script.</li>
        </ul>
      </div>

      <p>
        We can now start creating "programs" using nothing but shell commands.
        Let's start by putting the following line in the file <code>smallest</code>:
      </p>

<pre>
<span class="in">wc -l *.pdb | sort -n</span>
</pre>

      <p class="continue">
        This is a variation on the pipe we constructed <a href="#s:pipefilter">earlier</a>:
        it displays all of the files sorted by the number of lines
        (the <code>-n</code> flag to <code>sort</code> means "sort numerically").
        Remember, we are <em>not</em> running it as a command just yet:
        we are putting the commands in a file.
        Once we're done,
        let's ask the shell (which is called <code>bash</code>) to run those saved commands:
      </p>

<pre>
$ <span class="in">bash smallest</span>
<span class="out">  9  methane.pdb
 12  ethane.pdb
 15  propane.pdb
 20  cubane.pdb
 21  pentane.pdb
 30  octane.pdb
107  total</span>
</pre>

      <p>
        Sure enough, our little program's output is exactly what we'd get if we ran that pipeline ourselves.
      </p>

      <p>
        We can make this script a little more flexible by changing <code>*.pdb</code> to <code>$*</code>,
        a shortcut which means "all of the command-line arguments".
        The new <code>smallest</code> looks like this:
      </p>

<pre>
$ <span class="in">cat smallest</span>
<span class="out">wc -l $* | sort -n</span>
$
</pre>

      <p class="continue">
        Once we have done this,
        we can use our program&mdash;usually called a <a href="glossary.html#shell-script">shell script</a>&mdash;to sort
        any set of files by size:
      </p>

<pre>
$ <span class="in">bash smallest *.txt</span>
<span class="out">419  paper.txt
2718 thesis.txt</span>
$
</pre>

      <p>
        If we want,
        we can use <code>$1</code>, <code>$2</code>, and so on to select particular arguments
        instead of always running on all the arguments.
        Together,
        these facilities let us write some very complicated programs
        using only the commands we would type interactively.
      </p>

      <p>
        In practice,
        most people develop shell scripts by running commands at the shell prompt a few times
        to make sure they are doing what we want,
        then copying them into a file so that we can re-use them in a single step.
        If we follow the Unix convention of reading data from standard input when we're not given filenames,
        and writing results to standard output,
        we can combine those programs with others using pipes and redirection
        to create even more powerful programs.
        Trying doing <em>that</em> with a bunch of GUIs&hellip;
      </p>

      <div class="box">

        <h3>Text vs. Whatever</h3>

        <p>
          We usually call programs like Microsoft Word or LibreOffice Writer "text editors",
          but we need to be a bit more careful when it comes to programming.
          By default,
          Microsoft Word uses <code>.doc</code> files to store not only text,
          but also formatting information about fonts,
          headings,
          and so on.
          This extra information isn't stored as characters,
          and doesn't mean anything to the Python interpreter:
          it expects input files to contain nothing but the letters, digits, and punctuation
          on a standard computer keyboard.
          When editing programs,
          therefore,
          you must either use a plain text editor,
          or be careful to save files as plain text.
        </p>

      </div>

      <section>

        <h3>Nelle's Pipeline: Creating a Script</h3>

        <p>
          An off-hand comment from her supervisor has made Nelle realize that
          she should have provided a couple of extra parameters to <code>goostats</code>
          when she processed her files.
          This might have been a disaster if she had done all the analysis by hand,
          but thanks to for loops,
          it will only take a couple of hours to re-do.
        </p>

        <p>
          Experience has taught her,
          though,
          that if something needs to be done twice,
          it will probably need to be done a third or fourth time as well.
          She runs the editor and writes the following:
        </p>

<pre>
for datafile in $*
do
    echo $datafile
    goostats -J 100 -r $datafile stats-$datafile
done
</pre>

        <p class="continue">
          (The parameters <code>-J&nbsp;100</code> and <code>-r</code>
          are the ones her supervisor said she should have used.)
          She saves this in a file called <code>do-stats.sh</code>,
          so that she can now re-do the first stage of her analysis by typing:
        </p>

<pre>
$ <span class="in">bash do-stats.sh *[AB].txt</span>
</pre>

        <p>
          She can also do this:
        </p>

<pre>
$ <span class="in">bash do-stats.sh *[AB].txt | wc -l</span>
</pre>

        <p class="continue">
          so that the output is just the number of files processed,
          rather than the names of the files that were processed.
        </p>

        <p>
          One thing to note about Nelle's script is
          her choice to let the person running it decide what files to process.
          She could have written the script as:
        </p>

<pre>
for datafile in <span class="highlight">*[AB].txt</span>
do
    echo $datafile
    goostats -J 100 -r $datafile stats-$datafile
done
</pre>

        <p>
          The advantage is that this always selects the right files:
          she doesn't have to remember to exclude the 'Z' files.
          The disadvantage is that it <em>always</em> selects just those files&mdash;she
          can't run it on all files (including the 'Z' files),
          or on the 'G' or 'H' files her colleagues in Antarctica are producing,
          without editing the script.
          If she wanted to be more adventurous,
          she could modify her script to check for command-line arguments,
          and use <code>*[AB].txt</code> if none were provided.
          Of course,
          this introduces another tradeoff between flexibility and complexity;
          we'll explore this <a href="quality.html">later</a>.
        </p>

      </section>

      <div class="keypoints" id="k:scripts">
        <h3>Summary</h3>
        <ul>
          <li idea="perf;paranoia">Save commands in files (usually called shell scripts) for re-use.</li>
          <li>Use <code>bash <em>filename</em></code> to run saved commands.</li>
          <li><code>$*</code> refers to all of a shell script's command-line arguments.</li>
          <li><code>$1</code>, <code>$2</code>, etc., refer to specified command-line arguments.</li>
          <li idea="tools">Letting users decide what files to process is more flexible and more consistent with built-in Unix commands.</li>
        </ul>
      </div>

    </section>

    <section id="s:find">

      <h2>Finding Things</h2>

      <div class="understand" id="u:find">
        <h3>Understand:</h3>
        <ul>
          <li>How to select lines matching patterns in text files.</li>
          <li>How to find files with certain properties.</li>
          <li>How to use one command's output as arguments to another command.</li>
          <li>The difference between text files and binary files.</li>
        </ul>
      </div>

      <figure id="f:google_vs_grep">
        <img src="img/shell/google_vs_grep.png" alt="Google vs. Grep" />
      </figure>

      <p>
        You can often guess someone's age by listening to how people talk about search.
        Just as young people use "Google" as a verb,
        crusty old Unix programmers use "grep".
        The word is a contraction of "global/regular expression/print",
        a common sequence of operations in early Unix text editors.
        It is also the name of a very useful command-line program.
      </p>

      <p>
        <code>grep</code> finds and prints lines in files that match a pattern.
        For our examples,
        we will use a file that contains three haikus
        taken from a <a href="http://www.salonmagazine.com/21st/chal/1998/01/26chal.html">1998 competition in Salon magazine</a>:
      </p>

<pre>
The Tao that is seen
Is not the true Tao, until
You bring fresh toner.

With searching comes loss
and the presence of absence:
"My Thesis" not found.

Yesterday it worked
Today it is not working
Software is like that.
</pre>

      <p>
        Let's find lines that contain the word "not":
      </p>

<pre>
$ <span class="in">grep not haiku.txt</span>
<span class="out">Is not the true Tao, until
"My Thesis" not found
Today it is not working</span>
$
</pre>

      <p class="continue">
        Here, <code>not</code> is the pattern we're searching for.
        It's pretty simple: every alphanumeric character matches against itself.
        After the pattern comes the name or names of the files we're searching in.
        The output is the three lines in the file that contain the letters "not".
      </p>

      <p>
        Let's try a different pattern: "day".
      </p>

<pre>
$ <span class="in">grep day haiku.txt</span>
<span class="out">Yesterday it worked
Today it is not working</span>
$
</pre>

      <p class="continue">
        This time,
        the output is lines containing the words "Yesterday" and "Today",
        which both have the letters "day".
        If we give <code>grep</code> the <code>-w</code> flag,
        it restricts matches to word boundaries,
        so that only lines with the word "day" will be printed:
      </p>

<pre>
$ <span class="in">grep -w day haiku.txt</span>
$
</pre>

      <p class="continue">
        In this case, there aren't any, so <code>grep</code>'s output is empty.
      </p>

      <p>
        Another useful option is <code>-n</code>, which numbers the lines that match:
      </p>

<pre>
$ <span class="in">grep -n it haiku.txt</span>
<span class="out">5:With searching comes loss
9:Yesterday it worked
10:Today it is not working</span>
$
</pre>

      <p class="continue">
        Here, we can see that lines 5, 9, and 10 contain the letters "it".
      </p>

      <p>
        As with other Unix commands, we can combine flags.
        For example,
        since <code>-i</code> makes matching case-insensitive,
        and <code>-v</code> inverts the match,
        using them both only prints lines that <em>don't</em> match the pattern
        in any mix of upper and lower case:
      </p>

<pre>
$ <span class="in">grep -i -v the haiku.txt</span>
<span class="out">You bring fresh toner.

With searching comes loss

Yesterday it worked
Today it is not working
Software is like that.</span>
$
</pre>

      <p>
        <code>grep</code> has lots of other options.
        To find out what they are, we can type <code>man grep</code>.
        <code>man</code> is the Unix "manual" command.
        It prints a description of a command and its options,
        and (if you're lucky) provides a few examples of how to use it:
      </p>

<pre>
$ <span class="in">man grep</span>
<span class="out">GREP(1)                                                                                              GREP(1)

NAME
       grep, egrep, fgrep - print lines matching a pattern

SYNOPSIS
       grep [OPTIONS] PATTERN [FILE...]
       grep [OPTIONS] [-e PATTERN | -f FILE] [FILE...]

DESCRIPTION
       grep  searches the named input FILEs (or standard input if no files are named, or if a single hyphen-
       minus (-) is given as file name) for lines containing a match to the given PATTERN.  By default, grep
       prints the matching lines.
       &hellip;        &hellip;        &hellip;

OPTIONS
   Generic Program Information
       --help Print  a  usage  message  briefly summarizing these command-line options and the bug-reporting
              address, then exit.

       -V, --version
              Print the version number of grep to the standard output stream.  This version number should be
              included in all bug reports (see below).

   Matcher Selection
       -E, --extended-regexp
              Interpret  PATTERN  as  an  extended regular expression (ERE, see below).  (-E is specified by
              POSIX.)

       -F, --fixed-strings
              Interpret PATTERN as a list of fixed strings, separated by newlines, any of  which  is  to  be
              matched.  (-F is specified by POSIX.)
    &hellip;        &hellip;        &hellip;</span>
</pre>

      <div class="box">

        <h3>Wildcards</h3>

        <p>
          <code>grep</code>'s real power doesn't come from its options, though;
          it comes from the fact that patterns can include wildcards.
          (The technical name for these is
          <a href="glossary.html#regular-expression">regular expressions</a>,
          which is what the "re" in "grep" stands for.)
          Regular expressions are complex enough that
          we devotedan entire section of the website to them;
          if you want to do complex searches,
          please check it out.
          As a taster,
          we can find lines that have an 'o' in the second position like this:
        </p>

<pre>
$ <span class="in">grep -E '^.o' haiku.txt</span>
You bring fresh toner.
Today it is not working
Software is like that.
</pre>

        <p class="continue">
          We use the <code>-E</code> flag and put the pattern in quotes to prevent the shell from trying to interpret it.
          (If the pattern contained a '*', for example, the shell would try to expand it before running <code>grep</code>.)
          The '^' in the pattern anchors the match to the start of the line.
          The '.' matches a single character
          (just like '?' in the shell),
          while the 'o' matches an actual 'o'.
        </p>

      </div>

      <p>
        While <code>grep</code> finds lines in files,
        the <code>find</code> command finds files themselves.
        Again, it has a lot of options;
        to show how the simplest ones work, we'll use the directory tree in
        <a href="#f:find_file_tree">Figure 24</a>:
      </p>

      <figure id="f:find_file_tree">
        <img src="img/shell/find_file_tree.png" alt="Sample Files and Directories" />
      </figure>

      <p class="continue">
        Vlad's home directory contains one file called <code>notes.txt</code> and four subdirectories:
        <code>thesis</code> (which is sadly empty),
        <code>data</code> (which contains two files <code>first.txt</code> and <code>second.txt</code>),
        a <code>tools</code> directory that contains the programs <code>format</code> and <code>stats</code>,
        and an empty subdirectory called <code>old</code>.
      </p>

      <p>
        For our first command, let's run <code>find . -type d</code>.
        <code>.</code> is the directory where we want our search to start;
        <code>-type&nbsp;d</code> means "things that are directories".
        Sure enough, <code>find</code>'s output is the names of the five directories in our little tree
        (including <code>.</code>, the current working directory):
      </p>

<pre>
$ <span class="in">find . -type d</span>
<span class="out">./
./data
./thesis
./tools
./tools/old</span>
$
</pre>

      <p>
        If we change <code>-type&nbsp;d</code> to <code>-type&nbsp;f</code>,
        we get a listing of all the files instead:
      </p>

<pre>
$ <span class="in">find . -type f</span>
<span class="out">./data/first.txt
./data/second.txt
./notes.txt
./tools/format
./tools/stats</span>
$
</pre>

      <p class="continue">
        <code>find</code> automatically goes into subdirectories,
        their subdirectories,
        and so on to find everything that matches the pattern we've given it.
        If we don't want it to,
        we can use <code>-maxdepth</code> to restrict the depth of search:
      </p>

<pre>
$ <span class="in">find . -maxdepth 1 -type f</span>
<span class="out">./notes.txt</span>
$
</pre>

      <p>
        The opposite of <code>-maxdepth</code> is <code>-mindepth</code>,
        which tells <code>find</code> to only report things that are at or below a certain depth.
        <code>-mindepth&nbsp;2</code> therefore finds all the files that are two or more levels below us:
      </p>

<pre>
$ <span class="in">find . -mindepth 2 -type f</span>
<span class="out">./data/first.txt
./data/second.txt
./tools/format
./tools/stats</span>
$
</pre>

      <p>
        Another option is <code>-empty</code>.
        It restricts matches to empty files and directories, of which we have two:
      </p>

<pre>
$ <span class="in">find . -empty</span>
<span class="out">./thesis
./tools/old</span>
$
</pre>

      <p>
        Let's try matching by name:
      </p>

<pre>
$ <span class="in">find . -name *.txt</span>
<span class="out">./notes.txt</span>
$
</pre>

      <p class="continue">
        We expected it to find all the text files,
        but it only prints out <code>./notes.txt</code>:
        what's gone wrong?
      </p>

      <p>
        The problem is that the shell expands wildcard characters like <code>*</code> <em>before</em> commands run.
        Since <code>*.txt</code> in the current directory expands to <code>notes.txt</code>,
        the command we actually ran was:
      </p>

<pre>
$ <span class="in">find . -name notes.txt</span>
</pre>

      <p class="continue">
        <code>find</code> did what we asked; we just asked for the wrong thing.
      </p>

      <p>
        To get what we want,
        let's do what we did with <code>grep</code>:
        put <code>*.txt</code> in single quotes to prevent the shell from expanding the <code>*</code> wildcard.
        This way,
        <code>find</code> actually gets the pattern <code>*.txt</code>,
        not the expanded filename <code>notes.txt</code>:
      </p>

<pre>
$ <span class="in">find . -name '*.txt'</span>
<span class="out">./data/first.txt
./data/second.txt
./notes.txt</span>
$
</pre>

      <p>
        As we said <a href="#s:pipefilter">earlier</a>,
        the command line's power lies in combining tools.
        We've seen how to do that with pipes; let's look at another technique.
        As we just saw, <code>find . -name '*.txt'</code> gives us a list of all text files in or below the current directory.
        How can we combine that with <code>wc -l</code> to count the lines in all those files?
      </p>

      <p>
        One way is to put the <code>find</code> command inside <code>$()</code>:
      </p>

<pre>
$ <span class="in">wc -l $(find . -name '*.txt')</span>
<span class="out">  70  ./data/first.txt
 420  ./data/second.txt
  30  ./notes.txt
 520  total</span>
$
</pre>

      <p class="continue">
        When the shell executes this command,
        the first thing it does is run whatever is inside the <code>$()</code>.
        It then replaces the <code>$()</code> expression with that command's output.
        Since the output of <code>find</code> is the three filenames
        <code>./data/first.txt</code>, <code>./data/second.txt</code>, and <code>./notes.txt</code>,
        the shell constructs the command:
      </p>

<pre>
$ <span class="in">wc -l ./data/first.txt ./data/second.txt ./notes.txt</span>
</pre>

      <p class="continue">
        which is what we wanted.
        This expansion is exactly what the shell does when it expands wildcards like <code>*</code> and <code>?</code>,
        but lets us use any command we want as our own "wildcard".
      </p>

      <p>
        It's very common to use <code>find</code> and <code>grep</code> together.
        The first finds files that match a pattern;
        the second looks for lines inside those files that match another pattern.
        Here, for example, we can find PDB files that contain iron atoms
        by looking for the string "FE" in all the <code>.pdb</code> files below the current directory:
      </p>

<pre>
$ <span class="in">grep FE $(find . -name '*.pdb')</span>
<span class="out">./human/heme.pdb:ATOM  25  FE  1  -0.924  0.535  -0.518</span>
$
</pre>

      <div class="box">

        <h3>Binary Files</h3>

        <p>
          We have focused exclusively on finding things in text files.
          What if your data is stored as images, in databases, or in some other format?
          One option would be to extend tools like <code>grep</code> to handle those formats.
          This hasn't happened, and probably won't, because there are too many formats to support.
        </p>

        <p>
          The second option is to convert the data to text,
          or extract the text-ish bits from the data.
          This is probably the most common approach,
          since it only requires people to build one tool per data format (to extract information).
          On the one hand, it makes simple things easy to do.
          On the negative side, complex things are usually impossible.
          For example,
          it's easy enough to write a program that will extract X and Y dimensions from image files for <code>grep</code> to play with,
          but how would you write something to find values in a spreadsheet whose cells contained formulas?
        </p>

        <p>
          The third choice is to recognize that the shell and text processing have their limits,
          and to use a programming language such as Python instead.
          When the time comes to do this, don't be too hard on the shell:
          many modern programming languages, Python included, have borrowed a lot of ideas from it,
          and imitation is also the sincerest form of praise.
        </p>

      </div>

      <section>

        <h3>Nelle's Pipeline: The Second Stage</h3>

        <p>
          Nelle now has a directory called <code>north-pacific-gyre/2012-07-03</code>
          containing 1518 data files,
          and needs to compare each one against all of the others
          to find the hundred pairs with the highest pairwise scores.
          Armed with what she has learned so far,
          she writes the following script
        </p>

<pre>
for left in $*
do
    for right in $*
    do
        echo $left $right $(goodiff $left $right)
    done
done
</pre>

        <p>
          The outermost loop assigns the name of each file to the variable <code>left</code> in turn.
          The inner loop does the same thing for the variable <code>right</code>
          each time the outer loop executes,
          so inside the inner loop,
          <code>left</code> and <code>right</code> are given
          each pair of filenames
          (<a href="#f:nested_loops">Figure 25</a>).
        </p>

        <figure id="f:nested_loops">
          <img src="img/shell/nested_loops.png" alt="Nested Loops" />
        </figure>

        <p>
          Each time it runs the command inside the inner loop,
          the shell starts by running <code>goodiff</code> on the two files
          in order to expand the <code>$()</code> expression.
          Once it's done that,
          it passes the output,
          along with the names of the files,
          to <code>echo</code>.
          Thus,
          if Nelle saves this script as <code>pairwise.sh</code>
          and runs it as:
        </p>

<pre>
$ <span class="in">bash pairwise.sh stats-*.txt</span>
</pre>

        <p class="continue">
          the shell runs:
        </p>

<pre>
echo stats-NENE01729A.txt stats-NENE01729A.txt $(goodiff stats-NENE01729A.txt stats-NENE01729A.txt)
echo stats-NENE01729A.txt stats-NENE01729B.txt $(goodiff stats-NENE01729A.txt stats-NENE01729B.txt)
echo stats-NENE01729A.txt stats-NENE01736A.txt $(goodiff stats-NENE01729A.txt stats-NENE01736A.txt)
...
</pre>

        <p class="continue">
          which turns into:
        </p>

<pre>
echo stats-NENE01729A.txt stats-NENE01729A.txt files are identical
echo stats-NENE01729A.txt stats-NENE01729B.txt 0.97182
echo stats-NENE01729A.txt stats-NENE01736A.txt 0.45223
...
</pre>

        <p class="continue">
          which in turn prints:
        </p>

<pre>
stats-NENE01729A.txt stats-NENE01729A.txt files are identical
stats-NENE01729A.txt stats-NENE01729B.txt 0.97182
stats-NENE01729A.txt stats-NENE01736A.txt 0.45223
...
</pre>

        <p>
          That's a good start,
          but Nelle can do better.
          First,
          she notices that when the two input files are the same,
          the output is the words "files are identical"
          instead of a numerical score.
          She can remove these lines like this:
        </p>

<pre>
$ <span class="in">bash pairwise.sh stats-*.txt | grep -v 'files are identical'</span>
</pre>

        <p class="continue">
          or put the call to <code>grep</code> inside the shell script
          (which will be less error-prone):
        </p>

<pre>
for left in $*
do
    for right in $*
    do
        echo $left $right $(goodiff $left $right)
    done
done <span class="highlight">| grep -v 'files are identical'</span>
</pre>

        <p>
          This works because <code>do</code>&hellip;<code>done</code>
          counts as a single command in Bash.
          If Nelle wanted to make this clearer,
          she could put parentheses around the loop:
        </p>

<pre>
<span class="highlight">(</span>for left in $*
do
    for right in $*
    do
        echo $left $right $(goodiff $left $right)
    done
done<span class="highlight">)</span> | grep -v 'files are identical'
</pre>

        <p class="continue">
          or move the <code>grep</code> to a line of its own:
        </p>

<pre>
for left in $*
do
    for right in $*
    do
        echo $left $right $(goodiff $left $right)
    done
done <span class="highlight">\
| grep -v 'files are identical'</span>
</pre>

        <p class="continue">
          The backslash tells the shell
          that the line doesn't really end after the outer <code>done</code>.
          Without it,
          the shell would see two commands:
          the outer loop
          (which would print to standard output),
          and then a call to <code>grep</code> without any filenames
          (which would wait forever waiting for the user to type something at the keyboard).
        </p>

        <p>
          The last thing Nelle needs to do before writing up
          is find the 100 best pairwise matches.
          She has seen this before:
          sort the lines numerically,
          then use <code>head</code> to select the top lines.
          However,
          the numbers she wants to sort by are at the end of the line,
          rather than beginning.
          Reading the output of <code>man&nbsp;sort</code> tells her
          that the <code>-k</code> flag will let her specify
          which column of input she wants to use as a sort key,
          but the syntax looks a little complicated.
          Instead,
          she moves the score to the front of each line:
        </p>

<pre>
for left in $*
do
    for right in $*
    do
        <span class="highlight">echo $(goodiff $left $right) $left $right</span>
    done
done \
| grep -v 'files are identical'
</pre>

        <p class="continue">
          and then adds two more commands to the pipeline:
        </p>

<pre>
for left in $*
do
    for right in $*
    do
        <span class="highlight">echo $(goodiff $left $right) $left $right</span>
    done
done \
| grep -v 'files are identical' \
| sort -n -r
| head -100
</pre>

        <p>
          She then runs:
        </p>

<pre>
$ <span class="in">bash pairwise.sh stats-*.txt > top100.txt</span>
</pre>

        <p class="continue">
          and heads off to a seminar,
          confident that by the time she comes back tomorrow,
          <code>top100.txt</code> will contain
          the results she needs for her paper.
        </p>

      </section>

      <div class="keypoints" id="k:find">
        <h3>Summary</h3>
        <ul>
          <li idea="meaning">Everything is stored as bytes, but the bytes in binary files do not represent characters.</li>
          <li>Use nested loops to run commands for every combination of two lists of things.</li>
          <li>Use '\' to break one logical line into several physical lines.</li>
          <li>Use parentheses '()' to keep things combined.</li>
          <li>Use <code>$(<em>command</em>)</code> to insert a command's output in place.</li>
          <li><code>find</code> finds files with specific properties that match patterns.</li>
          <li><code>grep</code> selects lines in files that match patterns.</li>
          <li><code>man <em>command</em></code> displays the manual page for a given command.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

      <p>
        The Unix shell is older than most of the people who use it.
        It has survived so long because it is
        one of the most productive programming environments ever created&mdash;maybe even
        <em>the</em> most productive.
        Its syntax may be cryptic,
        but as Nelle's story shows,
        people who have mastered it can experiment with different commands interactively,
        then use what they have learned to automate their work.
        Here's how it relates to the questions that motivate Software Carpentry:
      </p>

    </section>