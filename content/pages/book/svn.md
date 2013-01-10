Title: Version Control With Subversion
Directory: book

    <ol class="toc">
      <li><a href="#s:basics">Basic Use</a></li>
      <li><a href="#s:merge">Merging Conflicts</a></li>
      <li><a href="#s:rollback">Recovering Old Versions</a></li>
      <li><a href="#s:setup">Setting up a Repository</a></li>
      <li><a href="#s:provenance">Provenance</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <p>
      Suppose that Wolfman and Dracula have been hired by Universal Monsters Inc.
      to figure out where the company should put its next secret lair.
      They want to be able to work on the plans at the same time,
      but they have run into problems doing this in the past.
      If they take turns,
      each one will spend a lot of time waiting for the other to finish.
      On the other hand,
      if they work on their own copies and email changes back and forth
      they know that things will be lost, overwritten, or duplicated.
    </p>

    <p>
      The right solution is to use a <a href="glossary.html#version-control-system">version control system</a>
      to manage their work.
      Version control is better than mailing files back and forth because:
    </p>

    <ol>

      <li>
        It's hard (but not impossible) to accidentally overlook or overwrite someone's changes,
        because the version control system highlights them automatically.
      </li>

      <li>
        There are no arguments about whose copy is the most up to date.
      </li>

      <li>
        Nothing that is committed to version control is ever lost.
        This means it can be used like the "undo" feature in an editor,
        and since all old versions of files are saved
        it's always possible to go back in time to see exactly who wrote what on a particular day,
        or what version of a program was used to generate a particular set of results.
      </li>

    </ol>

    <p>
      Version control systems do have one important shortcoming.
      While it is easy for them to find, display, and merge differences in text files,
      images, MP3s, PDFs, or Microsoft Word or Excel files aren't stored as text&mdash;they
      use specialized binary data formats.
      Most version control systems don't know how to deal with these formats,
      so all they can say is, "These files differ."
      The rest is up to you.
    </p>

    <p>
      Even with this limitation,
      version control is one of the most important concepts in this book.
      The rest of this chapter will explore how to use Subversion,
      a popular open source version control system.
    </p>

    <section id="s:basics">

      <h2>Basic Use</h2>

      <div class="understand" id="u:basics">
        <h3>Understand:</h3>
        <ul>
          <li>Where version control stores information.</li>
          <li>How to check out a working copy of a repository.</li>
          <li>How to view the history of changes to a project.</li>
          <li>Why working copies of different projects should not overlap.</li>
          <li>How to add files to a project.</li>
          <li>How to submit changes made locally to a project's master copy.</li>
          <li>How to update a working copy to get changes made to the master.</li>
          <li>How to check the status of a working copy.</li>
        </ul>
      </div>

      <p>
        A version control system keeps the master copy of a file
        in a <a href="glossary.html#repository">repository</a>
        located on a <a href="glossary.html#server">server</a>&mdash;a computer
        that is never used directly by people,
        but only by their programs
        (<a href="#f:repository">Figure XXX</a>).
        No-one ever edits the master copy directly.
        Instead,
        Wolfman and Dracula each have a <a href="glossary.html#working-copy">working copy</a>
        on their own computer.
        This lets them make whatever changes they want whenever they want.
      </p>

      <figure id="f:repository">
        <img src="img/svn/repository.png" alt="A Version Control Repository" />
      </figure>

      <p id="a:commit">
        As soon Wolfman is ready to share his changes,
        he <a href="glossary.html#commit">commits</a> his work to the repository
        (<a href="#f:workflow">Figure XXX</a>).
        Dracula can then <a href="glossary.html#update">update</a> his working copy to get those changes.
        And of course,
        when Dracula finishes working on something,
        he can commit and then Wolfman can update.
      </p>

      <figure id="f:workflow">
        <img src="img/svn/workflow.png" alt="Version Control Workflow" />
      </figure>

      <p>
        But what if Dracula and Wolfman make changes to the same part of their working copies?
        Old-fashioned version control systems prevented this from happening
        by <a href="glossary.html#lock">locking</a> the master copy
        whenever someone was working on it.
        This <a href="glossary.html#pessimistic-concurrency">pessimistic</a> strategy
        guaranteed that a second person (or monster)
        could never make changes to the same file at the same time,
        but it also meant that people had to take turns.
      </p>

      <p>
        Most of today's version control systems use
        an <a href="glossary.html#optimistic-concurrency">optimistic</a> strategy instead.
        Nothing is ever locked&mdash;everyone is always allowed to edit their working copy.
        This means that people can make changes to the same part of the paper,
        but that's actually fairly uncommon in a well-run project,
        and when it <em>does</em> happen,
        the version control system helps people reconcile their changes.
      </p>

      <p>
        For example,
        if Wolfman and Dracula are making changes at the same time,
        and Wolfman commits first,
        his changes are simply copied to the repository
        (<a href="#f:merge_first_commit">Figure XXX</a>):
      </p>

      <figure id="f:merge_first_commit">
        <img src="img/svn/merge_first_commit.png" alt="Wolfman Commits First" />
      </figure>

      <p class="continue">
        If Dracula now tries to commit something that would overwrite Wolfman's changes
        the version control system stops him
        and points out the <a href="glossary.html#conflict">conflict</a>
        (<a href="#f:merge_second_commit">Figure XXX</a>):
      </p>

      <figure id="f:merge_second_commit">
        <img src="img/svn/merge_second_commit.png" alt="Dracula Has a Conflict" />
      </figure>

      <p class="continue">
        Dracula must <a href="glossary.html#resolve">resolve</a> that conflict
        before the version control system will allow him to commit his work.
        He can accept what Wolfman did,
        replace it with what he has done,
        or write something new that combines the two&mdash;that's up to him.
        Once he has fixed things, he can go ahead and commit.
      </p>

      <p>
        Let's start by looking at the basic workflow we use
        when working with a version control system.
        To keep things simple,
        we'll assume that the Mummy has already put some notes in a version control repository
        on the <code>universal.software-carpentry.org</code> server.
        The full URL for this repository is <code>https://universal.software-carpentry.org/monsters</code>.
        Every repository has an address like this that uniquely identifies the location of the master copy.
      </p>

      <p>
        It's Monday night.
        In order to get a working copy on his computer,
        Dracula has to <a href="glossary.html#check-out">check out</a> a copy of the repository.
        He only has to do this once per project:
        once he has a working copy,
        he can update it over and over again to get other people's work:
      </p>

      <div class="box">
        <h3>There's More Than One Way To Do It</h3>

        <p>
          We will drive Subversion from the command line in our examples,
          but if you prefer using a GUI,
          there are many for you to choose from:
        </p>

        <ul>

          <li>
            <a href="http://tortoisesvn.net/">TortoiseSVN</a>
            is integrated into the Windows desktop,
            so there's no separate GUI as such.
          </li>

          <li>
            <a href="http://rapidsvn.tigris.org/">RapidSVN</a> is free,
            and runs on many platforms,
            but some users report difficulties installing it.
          </li>

          <li>
            Syntevo's <a href="http://www.syntevo.com/smartsvn/index.html">SmartSVN</a> isn't free,
            but it costs less than most textbooks,
            and is more stable (and has a friendlier interface) than RapidSVN.
          </li>

        </ul>

      </div>

      <p>
        While in his home directory,
        Dracula types the command:
      </p>

<pre>
$ <span class="in">svn checkout https://universal.software-carpentry.org/monsters</span>
</pre>

      <p class="continue">
        This creates a new directory called <code>monsters</code>
        and fills it with a copy of the repository's contents
        (<a href="#f:example_repo">Figure XXX</a>).
      </p>

<pre>
<span class="out">A    monsters/jupiter
A    monsters/mars
A    monsters/mars/mons-olympus.txt
A    monsters/mars/cydonia.txt
A    monsters/earth
A    monsters/earth/himalayas.txt
A    monsters/earth/antarctica.txt
A    monsters/earth/carlsbad.txt
Checked out revision 6.</span>
</pre>

      <figure id="f:example_repo">
        <img src="img/svn/example_repo.png" alt="Example Repository" />
      </figure>

      <p class="continue">
        Dracula can then go into this directory
        and use regular shell commands to view the files:
      </p>

<pre>
$ <span class="in">cd monsters</span>
$ <span class="in">ls</span>
<span class="out">earth   jupiter mars</span>
$ <span class="in">ls *</span>
<span class="out">earth:
antarctica.txt  carlsbad.txt  himalayas.txt

jupiter:

mars:
cydonia.txt  mons-olympus.txt</span>
</pre>

      <div class="box">

        <h3>Don't Let the Working Copies Overlap</h3>

        <p>
          It's very important that the working copies of different project do not overlap;
          in particular,
          we should never try to check out one project inside a working copy of another project.
          The reason is that Subversion stories information about
          the current state of a working copy
          in special sub-directories called <code>.svn</code>:
        </p>

<pre>
$ <span class="in">pwd</span>
<span class="out">/home/vlad/monsters</span>
$ <span class="in">ls -a</span>
<span class="out">.    ..    .svn    earth    jupiter    mars</span>
$ <span class="in">ls -F .svn</span>
<span class="out">entries    prop-base/    props/    text-base/    tmp/</span>
</pre>

        <p class="continue">
          If two working copies overlap,
          the files in the <code>.svn</code> directories for one repository
          will be clobbered by the other repository's <code>.svn</code> files,
          and Subversion will become hopelessly confused.
        </p>

      </div>

      <p>
        Dracula can find out more about the history of the project
        using Subversion's <code>log</code> command:
      </p>

<pre>
$ <span class="in">svn log</span>
<span class="out">------------------------------------------------------------------------
r6 | mummy | 2010-07-26 09:21:10 -0400 (Mon, 26 Jul 2010) | 1 line

Damn the budget---the Jovian moons would be a _perfect_ place for a lair.
------------------------------------------------------------------------
r5 | mummy | 2010-07-26 09:19:39 -0400 (Mon, 26 Jul 2010) | 1 line

The budget might not even stretch to a deep-sea lair... :-(
------------------------------------------------------------------------
r4 | mummy | 2010-07-26 09:17:46 -0400 (Mon, 26 Jul 2010) | 1 line

Budget cuts may force us to reconsider Earth as a base.
------------------------------------------------------------------------
r3 | mummy | 2010-07-26 09:14:14 -0400 (Mon, 26 Jul 2010) | 1 line

Converting to wiki-formatted text.
------------------------------------------------------------------------
r2 | mummy | 2010-07-26 09:11:55 -0400 (Mon, 26 Jul 2010) | 1 line

Hide near the face in Cydonia, perhaps?
------------------------------------------------------------------------
r1 | mummy | 2010-07-26 09:08:23 -0400 (Mon, 26 Jul 2010) | 1 line

Thoughts on Mons Olympus (probably too obvious)
------------------------------------------------------------------------</span>
</pre>

      <p class="continue">
        Subversion displays a summary of all the changes made to the project so far.
        This list includes the
        <a href="glossary.html#revision-number">revision number</a>,
        the name of the person who made the change,
        the date the change was made,
        and whatever comment the user provided when the change was submitted.
        As we can see,
        the <code>monsters</code> project is currently at revision 6,
        and all changes so far have been made by the Mummy.
      </p>

      <p>
        Notice how detailed the comments on the updates are.
        Good comments are as important in version control as they are in coding.
        Without them, it can be very difficult to figure out who did what, when, and why.
        We can use comments like "Changed things" and "Fixed it" if we want,
        or even no comments at all,
        but we'll only be making more work for our future selves.
      </p>

      <p>
        Another thing to notice is that the revision number applies to the whole repository,
        not to a particular file.
        When we talk about "version 61" we mean
        "the state of all files and directories at that point."
        Older version control systems like CVS gave each file a new version number when it was updated,
        which meant that version 38 of one file could correspond in time to version 17 of another
        (<a href="#f:version_numbering">Figure XXX</a>).
        Experience shows that
        global version numbers that apply to everything in the repository
        are easier to manage than
        per-file version numbers,
        so that's what Subversion uses.
      </p>

      <figure id="f:version_numbering">
        <img src="img/svn/version_numbering.png" alt="Version Numbering in CVS and Subversion" />
      </figure>

      <p>
        A couple of cubicles away,
        Wolfman also runs <code>svn checkout</code>
        to get a working copy of the repository.
        He also gets version 6,
        so the files on his machine are the same as the files on Dracula's.
        While he is looking through the files,
        Dracula decides to add some information to the repository about Jupiter's moons.
        Using his favorite editor,
        he creates a file in the <code>jupiter</code> directory called <code>moons.txt</code>,
        and fills it with information about Io, Europa, Ganymede, and Callisto:
      </p>

<pre src="src/svn/moons_initial.txt">
Name            Orbital Radius  Orbital Period  Mass            Radius
Io              421.6           1.769138        893.2           1821.6
Europa          670.9           3.551181        480.0           1560.8
Ganymede        1070.4          7.154553        1481.9          2631.2
Calisto         1882.7          16.689018       1075.9          2410.3
</pre>

      <p>
        After double-checking his data,
        he wants to commit the file to the repository so that everyone else on the project can see it.
        The first step is to add the file to his working copy using <code>svn add</code>:
      </p>

<pre>
$ <span class="in">svn add jupiter/moons.txt</span>
<span class="out">A         jupiter/moons.txt</span>
</pre>

      <p>
        Adding a file is not the same as creating it&mdash;he has already done that.
        Instead,
        the <code>svn add</code> command tells Subversion to add the file to
        the list of things it's supposed to manage.
        It's quite common,
        particularly in programming projects,
        to have backup files or intermediate files in a directory
        that aren't worth storing in the repository.
        This is why version control requires us to explicitly tell it which files are to be managed.
      </p>

      <p>
        Once he has told Subversion to add the file,
        Dracula can go ahead and commit his changes to the repository.
        He uses the <code>-m</code> flag to provide a one-line message explaining what he's doing;
        if he didn't,
        Subversion would open his default editor
        so that he could type in something longer.
      </p>

<pre>
$ <span class="in">svn commit -m "Some basic facts about the Galilean moons of Jupiter." jupiter/moons.txt</span>
<span class="out">Adding         jupiter/moons.txt
Transmitting file data .
Committed revision 7.</span>
</pre>

      <p class="continue">
        When Dracula runs this command,
        Subversion establishes a connection to the server,
        copies over his changes,
        and updates the revision number from 6 to 7
        (<a href="#f:updated_repo">Figure XXX</a>).
        Again,
        this version number applies to the <em>whole</em> repository,
        not just to files that have changed.
      </p>

      <figure id="f:updated_repo">
        <img src="img/svn/updated_repo.png" alt="Updated Repository" />
      </figure>

      <p id="a:define-head">
        Back in his cubicle,
        Wolfman uses <code>svn update</code> to update his working copy.
        It tells him that a new file has been added
        and brings his working copy up to date with version 7 of the repository,
        because this is now the most recent revision
        (also called the <a href="glossary.html#head">head</a>).
        <code>svn update</code> updates an existing working copy,
        rather than checking out a new one.
        While <code>svn checkout</code> is usually only run once per project per machine,
        <code>svn update</code> may be run many times a day.
      </p>

      <p>
        Looking in the new file <code>jupiter/moons.txt</code>,
        Wolfman notices that Dracula has misspelled "Callisto"
        (it is supposed to have two L's.)
        Wolfman edits that line of the file:
      </p>

<pre src="src/svn/moons_spelling.txt">
Name            Orbital Radius  Orbital Period  Mass            Radius
Io              421.6           1.769138        893.2           1821.6
Europa          670.9           3.551181        480.0           1560.8
Ganymede        1070.4          7.154553        1481.9          2631.2
<span class="highlight">Callisto        1882.7          16.689018       1075.9          2410.3</span>
</pre>

      <p class="continue">
        He also adds a line about Amalthea,
        which he thinks might be a good site for a secret lair despite its small size:
      </p>

<pre src="src/svn/moons_amalthea.txt">
Name            Orbital Radius  Orbital Period  Mass            Radius
<span class="highlight">Amalthea        181.4           0.498179        0.075           125.0</span>
Io              421.6           1.769138        893.2           1821.6
Europa          670.9           3.551181        480.0           1560.8
Ganymede        1070.4          7.154553        1481.9          2631.2
Callisto        1882.7          16.689018       1075.9          2410.3
</pre>

      <p class="continue">
        uses the <code>svn status</code> command to check that he hasn't accidentally changed anything else:
      </p>

<pre>
$ <span class="in">svn status</span>
<span class="out">M       jupiter/moons.txt</span>
</pre>

      <p class="continue">
        and then runs <code>svn commit</code>.
        Since has hasn't used the <code>-m</code> flag to provide a message on the command line,
        Subversion launches his default editor and shows him:
      </p>

<pre>

--This line, and those below, will be ignored--

M    jupiter/moons.txt
</pre>

      <p>
        He changes this to be
      </p>

<pre>
1. Fixed typo in moon's name: 'Calisto' -> 'Callisto'.
2. Added information about Amalthea.
--This line, and those below, will be ignored--

M    jupiter/moons.txt
</pre>

      <p class="continue">
        When he saves this temporary file and exits the editor,
        Subversion commits his changes:
      </p>

<pre>
<span class="out">Sending        jupiter/moons.txt
Transmitting file data .
Committed revision 8.</span>
</pre>

      <p class="continue">
        Note that since Wolfman didn't specify a particular file to commit,
        Subversion commits <em>all</em> of his changes.
        This is why he ran the <code>svn status</code> command first.
      </p>

      <div class="box" id="a:transaction">

        <h3>Working With Multiple Files</h3>

        <p>
          Our example only includes one file,
          but version control can work on any number of files at once.
          For example,
          if Wolfman noticed that a dozen data files had the same incorrect header,
          he could change it in all 12 files,
          then commit all those changes at once.
          This is actually the best way to work:
          every logical change to the project should be a single commit,
          and every commit should include everything involved in one logical change.
        </p>

      </div>

      <p>
        That night,
        when Dracula rises from his coffin to start work,
        the first thing he wants to do is get Wolfman's changes.
        Before updating his working copy with <code>svn update</code>,
        though,
        he wants to see the differences between what he has
        and what he <em>will</em> have if he updates.
        To do this,
        Dracula uses <code>svn diff</code>.
        When run without arguments,
        it compares what's in his working copy to what he started with,
        and shows no differences:
      </p>

<pre>
$ <span class="in">svn diff</span>
$
</pre>

      <p class="continue">
        To compare his working copy to the master,
        Dracula uses <code>svn diff -r HEAD</code>.
        The <code>-r</code> flag is used to specify a revision,
        while <code>HEAD</code> means
        "<a href="#a:define-head">the latest version of the master</a>".
      </p>

<pre>
$ <span class="in">svn diff -r HEAD</span>
<span class="out">--- moons.txt(revision 8)
+++ moons.txt(working copy)
@@ -1,5 +1,6 @@
 Name            Orbital Radius  Orbital Period  Mass            Radius
+Amalthea        181.4           0.498179        0.075           125.0
 Io              421.6           1.769138        893.2           1821.6
 Europa          670.9           3.551181        480.0           1560.8
 Ganymede        1070.4          7.154553        1481.9          2631.2
-Calisto         1882.7          16.689018       1075.9          2410.3
+Callisto        1882.7          16.689018       1075.9          2410.3
</span>
</pre>

      <p class="continue">
        After looking over the changes,
        Dracula goes ahead and does the update.
      </p>

      <div class="box">
        <h3>Reading a Diff</h3>

        <p>
          The output of <code>diff</code> isn't particularly user-friendly,
          but actually isn't that hard to figure out.
          The first two lines:
        </p>

<pre>
--- moons.txt(revision 9)
+++ moons.txt(working copy)
</pre>

        <p class="continue">
          signal that '-' will be used to show content from revision 9
          and '+' to show content from the user's working copy.
          The next line, with the '@' markers,
          indicates where lines were inserted or removed.
          This isn't really intended for human consumption:
          a variety of other software tools will use this information.
        </p>

        <p>
          The most important parts of what follows are the lines marked with '+' and '-',
          which show insertions and deletions respectively.
          Here,
          we can see that the line for Amalthea was inserted,
          and that the line for Callisto was changed
          (which is indicated by an add and a delete right next to one another).
          Many editors and other tools can display diffs like this in a two-column display,
          highlighting changes.
        </p>

      </div>

      <p>
        This is a very common workflow,
        and is the basic heartbeat of most developers' days.
        To recap,
        the steps are:
      </p>

      <ol>

        <li>
          Check to see if there are changes in the repository to download.
        </li>

        <li>
          Update our working copy with those changes.
        </li>

        <li>
          Do our own work.
        </li>

        <li>
          Commit our changes to the repository so that other people can get them.
        </li>

      </ol>

      <p>
        It's worth noticing here how important Wolfman's comments about his changes were.
        It's hard to see the difference between "Calisto" with one 'L' and "Callisto" with two,
        even if the line containing the difference has been highlighted.
        Without Wolfman's comments,
        Dracula might have wasted time wondering what the difference was.
      </p>

      <p>
        In fact,
        Wolfman should probably have committed his two changes separately,
        since there's no logical connection between
        fixing a typo in Callisto's name
        and adding information about Amalthea to the same file.
        Just as a function or program should do one job and one job only,
        a single commit to version control should have a single logical purpose so that it's easier to find,
        understand,
        and if necessary undo later on.
      </p>

      <div class="keypoints" id="k:basics">
        <h3>Summary</h3>
        <ul>
          <li>Version control is a better way to manage shared files than email or shared folders.</li>
          <li>The master copy is stored in a repository.</li>
          <li>Nobody ever edits the master directory: instead, each person edits a local working copy.</li>
          <li>People share changes by committing them to the master or updating their local copy from the master.</li>
          <li idea="paranoia">The version control system prevents people from overwriting each other's work by forcing them to merge concurrent changes before committing.</li>
          <li idea="perf">It also keeps a complete history of changes made to the master so that old versions can be recovered reliably.</li>
          <li>Version control systems work best with text files, but can also handle binary files such as images and Word documents.</li>
          <li>Every repository is identified by a URL.</li>
          <li>Working copies of different repositories may not overlap.</li>
          <li>Each changed to the master copy is identified by a unique revision number.</li>
          <li>Revisions identify snapshots of the entire repository, not changes to individual files.</li>
          <li idea="perf">Each change should be commented to make the history more readable.</li>
          <li>Commits are transactions: either all changes are successfully committed, or none are.</li>
          <li>The basic workflow for version control is update-change-commit.</li>
          <li><code>svn add <em>things</em></code> tells Subversion to start managing particular files or directories.</li>
          <li><code>svn checkout <em>url</em></code> checks out a working copy of a repository.</li>
          <li><code>svn commit -m "<em>message</em>" <em>things</em></code> sends changes to the repository.</li>
          <li><code>svn diff</code> compares the current state of a working copy to the state after the most recent update.</li>
          <li><code>svn diff -r HEAD</code> compares the current state of a working copy to the state of the master copy.</li>
          <li><code>svn history</code> shows the history of a working copy.</li>
          <li><code>svn status</code> shows the status of a working copy.</li>
          <li><code>svn update</code> updates a working copy from the repository.</li>
        </ul>
      </div>

    </section>

    <section id="s:merge">

      <h2>Merging Conflicts</h2>

      <div class="understand" id="u:merge">
        <h3>Understand:</h3>
        <ul>
          <li>What a conflict in an update is.</li>
          <li>How to resolve conflicts when updating.</li>
        </ul>
      </div>

      <p>
        Dracula and Wolfman have both synchronized their working copies of <code>monsters</code>
        with version 8 of the repository.
        Dracula now edits his copy to change Amalthea's radius
        from a single number to a triple to reflect its irregular shape:
      </p>

<pre src="src/svn/moons_dracula_triple.txt">
Name            Orbital Radius  Orbital Period  Mass            Radius
<span class="highlight">Amalthea        181.4           0.498179        0.075           131 x 73 x 67</span>
Io              421.6           1.769138        893.2           1821.6
Europa          670.9           3.551181        480.0           1560.8
Ganymede        1070.4          7.154553        1481.9          2631.2
Callisto        1882.7          16.689018       1075.9          2410.3
</pre>

      <p class="continue">
        He then commits his work,
        creating revision 9 of the repository
        (<a href="#f:after_dracula_commits">Figure XXX</a>).
      </p>

      <figure id="f:after_dracula_commits">
        <img src="img/svn/after_dracula_commits.png" alt="After Dracula Commits" />
      </figure>

      <p>
        But while he is doing this,
        Wolfman is editing <em>his</em> copy
        to add information about two other minor moons,
        Himalia and Elara:
      </p>

<pre src="src/svn/moons_wolfman_extras.txt">
Name            Orbital Radius  Orbital Period  Mass            Radius
Amalthea        181.4           0.498179        0.075           131
Io              421.6           1.769138        893.2           1821.6
Europa          670.9           3.551181        480.0           1560.8
Ganymede        1070.4          7.154553        1481.9          2631.2
Callisto        1882.7          16.689018       1075.9          2410.3
<span class="highlight">Himalia         11460           250.5662        0.095           85.0
Elara           11740           259.6528        0.008           40.0</span>
</pre>

      <p>
        When Wolfman tries to commit his changes to the repository,
        Subversion won't let him:
      </p>

<pre>
$ <span class="in">svn commit -m "Added data for Himalia, Elara"</span>
<span class="out">Sending        jupiter/moons.txt
svn: Commit failed (details follow):
svn: File or directory 'moons.txt' is out of date; try updating
svn: resource out of date; try updating</span>
</pre>

      <p class="continue">
        The reason is that
        Wolfman's changes were based on revision 8,
        but the repository is now at revision 9,
        and the file that Wolfman is trying to overwrite
        is different in the later revision.
        (Remember,
        one of version control's main jobs is to make sure that
        people don't trample on each other's work.)
        Wolfman has to update his working copy to get Dracula's changes before he can commit.
        Luckily,
        Dracula edited a line that Wolfman didn't change,
        so Subversion can merge the differences automatically.
      </p>

      <p>
        This does <em>not</em> mean that Wolfman's changes have been committed to the repository:
        Subversion only does that when it's ordered to.
        Wolfman's changes are still in his working copy,
        and <em>only</em> in his working copy.
        But since Wolfman's version of the file now includes
        the lines that Dracula added,
        Wolfman can go ahead and commit them as usual to create revision 10.
      </p>

      <p>
        Wolfman's working copy is now in sync with the master,
        but Dracula's is one behind at revision 9.
        At this point,
        they independently decide to add measurement units
        to the columns in <code>moons.txt</code>.
        Wolfman is quicker off the mark this time;
        he adds a line to the file:
      </p>

<pre src="src/svn/moons_wolfman_units.txt">
Name            Orbital Radius  Orbital Period  Mass            Radius
<span class="highlight">                (10**3 km)      (days)          (10**20 kg)     (km)</span>
Amalthea        181.4           0.498179        0.075           131 x 73 x 67
Io              421.6           1.769138        893.2           1821.6
Europa          670.9           3.551181        480.0           1560.8
Ganymede        1070.4          7.154553        1481.9          2631.2
Callisto        1882.7          16.689018       1075.9          2410.3
Himalia         11460           250.5662        0.095           85.0
Elara           11740           259.6528        0.008           40.0
</pre>

      <p class="continue">
        and commits it to create revision 11.
        While he is doing this,
        though,
        Dracula inserts a different line at the top of the file:
      </p>

<pre src="src/svn/moons_dracula_units.txt">
Name            Orbital Radius  Orbital Period  Mass            Radius
<span class="highlight">                * 10^3 km       * days          * 10^20 kg      * km</span>
Amalthea        181.4           0.498179        0.075           131 x 73 x 67
Io              421.6           1.769138        893.2           1821.6
Europa          670.9           3.551181        480.0           1560.8
Ganymede        1070.4          7.154553        1481.9          2631.2
Callisto        1882.7          16.689018       1075.9          2410.3
Himalia         11460           250.5662        0.095           85.0
Elara           11740           259.6528        0.008           40.0
</pre>

      <p>
        Once again,
        when Dracula tries to commit,
        Subversion tells him he can't.
        But this time,
        when Dracula does updates his working copy,
        he doesn't just get the line Wolfman added to create revision 11.
        There is an actual conflict in the file,
        so Subversion asks Dracula what he wants to do:
      </p>

<pre src="src/svn/moons_dracula_conflict.txt">
$ <span class="in">svn update</span>
<span class="out">Conflict discovered in 'jupiter/moons.txt'.
Select: (p) postpone, (df) diff-full, (e) edit,
        (mc) mine-conflict, (tc) theirs-conflict,
        (s) show all options:</span>
</pre>

      <p>
        Dracula choose <code>p</code> for "postpone",
        which tells Subversion that he'll deal with the problem later.
        Once the update is finished,
        he opens <code>moons.txt</code> in his editor and sees:
      </p>

<pre>
 Name            Orbital Radius  Orbital Period  Mass
+&lt;&lt;&lt;&lt;&lt;&lt;&lt; .mine
         +                * 10^3 km       * days         * 10^20 kg
+=======
+                (10**3 km)      (days)         (10**20 kg)
+&gt;&gt;&gt;&gt;&gt;&gt;&gt; .r11
 Amalthea        181.4           0.498179        0.074
 Io              421.6           1.769138        893.2
 Europa          670.9           3.551181        480.0
 Ganymede        1070.4          7.154553        1481.9
 Callisto        1882.7          16.689018       1075.9
</pre>

      <p class="continue">
        As we can see,
        Subversion has inserted
        <a href="glossary.html#conflict-marker">conflict markers</a>
        in <code>moons.txt</code>
        wherever there is a conflict.
        The line <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt; .mine</code> shows the start of the conflict,
        and is followed by the lines from the local copy of the file.
        The separator <code>=======</code> is then
        followed by the lines from the repository's file that are in conflict with that section,
        while <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt; .r11</code> marks the end of the conflict.
      </p>

      <p>
        Before he can commit,
        Dracula has to edit his copy of the file to get rid of those markers.
        He changes it to:
      </p>

<pre src="src/svn/moons_dracula_resolved.txt">
Name            Orbital Radius  Orbital Period  Mass            Radius
<span class="highlight">                (10^3 km)       (days)          (10^20 kg)      (km)</span>
Amalthea        181.4           0.498179        0.075           131 x 73 x 67
Io              421.6           1.769138        893.2           1821.6
Europa          670.9           3.551181        480.0           1560.8
Ganymede        1070.4          7.154553        1481.9          2631.2
Callisto        1882.7          16.689018       1075.9          2410.3
Himalia         11460           250.5662        0.095           85.0
Elara           11740           259.6528        0.008           40.0
</pre>

      <p class="continue">
        then uses the <code>svn resolved</code> command to tell Subversion that
        he has fixed the problem.
        Subversion will now let him commit to create revision 12.
      </p>

      <div class="box">

        <h3>Auxiliary Files</h3>

        <p>
          When Dracula did his update and Subversion detected the conflict in <code>moons.txt</code>,
          it created three temporary files to help Dracula resolve it.
          The first is called <code>moons.txt.r9</code>;
          it is the file as it was in Dracula's local copy
          before he started making changes,
          i.e., the common ancestor for his work
          and whatever he is in conflict with.
        </p>

        <p>
          The second file is <code>moons.txt.r11</code>.
          This is the most up-to-date revision from the repository&mdash;the
          file as it is including Wolfman's changes.
          The third temporary file, <code>moons.txt.mine</code>,
          is the file as it was in Dracula's working copy before he did the Subversion update.
        </p>

        <p>
          Subversion creates these auxiliary files primarily
          to help people merge conflicts in binary files.
          It wouldn't make sense to insert <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code>
          and <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> characters into an image file
          (it would almost certainly result in a corrupted image).
          The <code>svn resolved</code> command deletes these three extra files
          as well as telling Subversion that the conflict has been taken care of.
        </p>

      </div>

      <p>
        Some power users prefer to work with interpolated conflict markers directly,
        but for the rest of us,
        there are several tools for displaying differences and helping to merge them,
        including <a href="http://diffuse.sourceforge.net/">Diffuse</a> and <a href="http://winmerge.org/">WinMerge</a>.
        If Dracula launches Diffuse,
        it displays his file,
        the common base that he and Wolfman were working from,
        and Wolfman's file in a three-pane view
        (<a href="#f:diff_viewer">Figure XXX</a>):
      </p>

      <figure id="f:diff_viewer">
        <img src="img/svn/diff_viewer.png" alt="A Difference Viewer" />
      </figure>

      <p class="continue">
        Dracula can use the buttons to merge changes from either of the edited versions
        into the common ancestor,
        or edit the central pane directly.
        Again,
        once he is done,
        he uses <code>svn resolved</code> and <code>svn commit</code>
        to create revision 12 of the repository.
      </p>

      <p>
        In this case, the conflict was small and easy to fix.
        However, if two or more people on a team are repeatedly creating conflicts for one another,
        it's usually a signal of deeper communication problems:
        either they aren't talking as often as they should, or their responsibilities overlap.
        If used properly,
        the version control system can help the team find and fix these issues
        so that it will be more productive in future.
      </p>

      <div class="box">

        <h3>Working With Multiple Files</h3>

        <p>
          As mentioned <a href="#a:transaction">earlier</a>,
          every logical change to a project should result in a single commit,
          and every commit should represent one logical change.
          This is especially true when resolving conflicts:
          the work done to reconcile one person's changes with another are often complicated,
          so it should be a single entry in the project's history,
          with other, later, changes coming after it.
        </p>

      </div>

      <div class="keypoints" id="k:merge">
        <h3>Summary</h3>
        <ul>
          <li>Conflicts must be resolved before a commit can be completed.</li>
          <li>Subversion puts markers in text files to show regions of conflict.</li>
          <li>For each conflicted file, Subversion creates auxiliary files containing the common parent, the master version, and the local version.</li>
          <li><code>svn resolve <em>files</em></code> tells Subversion that conflicts have been resolved.</li>
        </ul>
      </div>

    </section>

    <section id="s:rollback">

      <h2>Recovering Old Versions</h2>

      <div class="understand" id="u:rollback">
        <h3>Understand:</h3>
        <ul>
          <li>How to undo changes to a working copy.</li>
          <li>How to recover old versions of files.</li>
          <li>What a branch is.</li>
        </ul>
      </div>

      <p>
        Now that we have seen how to merge files and resolve conflicts,
        we can look at how to use version control as an "infinite undo".
        Suppose that when Wolfman starts work late one night,
        his copy of <code>monsters</code> is in sync with the head at revision 12.
        He decides to edit the file <code>moons.txt</code>;
        unfortunately, he forgot that there was a full moon,
        so his changes don't make a lot of sense:
      </p>

<pre src="src/svn/poetry.txt">
Just one moon can make me growl
Four would make me want to howl
...
</pre>

      <p>
        When he's back in human form the next day,
        he wants to undo his changes.
        Without version control, his choices would be grim:
        he could try to edit them back into their original state by hand
        (which for some reason hardly ever seems to work),
        or ask his colleagues to send him their copies of the files
        (which is almost as embarrassing as chasing the neighbor's cat when in wolf form).
      </p>

      <p>
        Since he's using Subversion, though,
        and hasn't committed his work to the repository,
        all he has to do is <a href="glossary.html#revert">revert</a> his local changes.
        <code>svn revert</code> simply throws away local changes to files
        and puts things back the way they were before those changes were made.
        This is a purely local operation:
        since Subversion stores the history of the project inside every working copy,
        Wolfman doesn't need to be connected to the network to do this.
      </p>

      <p>
        To start,
        Wolfman uses <code>svn diff</code> <em>without</em> the <code>-r HEAD</code> flag
        to take a look at the differences between his file
        and the master copy in the repository.
        Since he doesn't want to keep his changes,
        his next command is <code>svn revert moons.txt</code>.
      </p>

<pre>
$ <span class="in">cd jupiter</span>
$ <span class="in">svn revert moons.txt</span>
<span class="out">Reverted   moons.txt</span>
</pre>

      <p>
        What if someone <em>has</em> committed their changes,
        but still wants to undo them?
        For example,
        suppose Dracula decides that the numbers in <code>moons.txt</code> would look better with commas.
        He edits the file to put them in:
      </p>

<pre src="src/svn/moons_commas.txt">
Name            Orbital Radius  Orbital Period  Mass            Radius
                (10^3 km)       (days)          (10^20 kg)      (km)
Amalthea        181.4           0.498179          0.075      131 x 73 x 67
Io              421.6           1.769138        893.2          1<span class="highlight">,</span>821.6
Europa          670.9           3.551181        480.0          1<span class="highlight">,</span>560.8
Ganymede      1<span class="highlight">,</span>070.4           7.154553      1<span class="highlight">,</span>481.9          2<span class="highlight">,</span>631.2
Callisto      1<span class="highlight">,</span>882.7          16.689018      1<span class="highlight">,</span>075.9          2<span class="highlight">,</span>410.3
Himalia      11<span class="highlight">,</span>460           250.5662            0.095           85.0
Elara        11<span class="highlight">,</span>740           259.6528            0.008           40.0
</pre>

      <p class="continue">
        then commits his changes to create revision 13.
        A little while later,
        the Mummy sees the change and orders Dracula to put things back the way they were.
        What should Dracula do?
      </p>

      <p>
        We can draw the sequence of events leading up to revision 13
        as shown in <a href="#f:before_undoing">Fixture XXX</a>:
      </p>

      <figure id="f:before_undoing">
        <img src="img/svn/before_undoing.png" alt="Before Undoing" />
      </figure>

      <p class="continue">
        Dracula wants to erase revision 13 from the repository,
        but he can't actually do that:
        once a change is in the repository,
        it's there forever.
        What he can do instead is merge the old revision with the current revision
        to create a new revision
        (<a href="#f:merging_history">Fixture XXX</a>).
      </p>

      <figure id="f:merging_history">
        <img src="img/svn/merging_history.png" alt="Merging History" />
      </figure>

      <p class="continue">
        This is exactly like merging changes made by two different people;
        the only difference is that the "other person" is his past self.
      </p>

      <p>
        To undo his commas,
        Dracula must merge revision 12 (the one before his change)
        with revision 13 (the current head revision)
        using <code>svn merge</code>:
      </p>

<pre>
$ <span class="in">svn merge -r HEAD:12 moons.txt</span>
<span class="out">-- Reverse-merging r13 into 'moons.txt'
U  moons.txt</span>
</pre>

      <p class="continue">
        The <code>-r</code> flag specifies the range of revisions to merge:
        to undo the changes from revision 12 to revision 13,
        he uses either <code>13:12</code> or <code>HEAD:12</code>
        (since he is going backward in time from the most recent revision to revision 12).
        This is called a <a href="glossary.html#reverse-merge">reverse</a> merge
        because he's going backward in time.
      </p>

      <p>
        After he runs this command,
        he must run <code>svn commit</code> to save the changes to the repository.
        This creates a new revision, number 14,
        rather than erasing revision 13.
        That way,
        the changes he made to create revision 13 are still there
        if he can ever convince the Mummy that numbers should have commas.
      </p>

      <p>
        Merging can be used to recover older revisions of files,
        not just the most recent,
        and to recover many files or directories at a time.
        The most frequent use, though,
        is to manage parallel streams of development in large projects.
        This is outside the scope of this chapter,
        but the basic idea is simple.
      </p>

      <p>
        Suppose that Universal Monsters has just released a new program for designing secret lairs.
        Dracula and Wolfman are supposed to start adding a few features
        that had to be left out of the first release because time ran short.
        At the same time,
        Frankenstein and the Mummy are doing technical support:
        their job is to fix any bugs that users find.
        All sorts of things could go wrong if both teams tried to work on the same code at the same time.
        For example,
        if Frankenstein fixed a bug and sent a new copy of the program to a user in Greenland,
        it would be all too easy for him to accidentally include
        the half-completed shark tank control feature that Wolfman was working on.
      </p>

      <p>
        The usual way to handle this situation is
        to create a <a href="glossary.html#branch">branch</a>
        in the repository for each major sub-project
        (<a href="#f:branch_merge">Figure XXX</a>).
        While Wolfman and Dracula work on
        the <a href="glossary.html#main-line">main line</a>,
        Frankenstein and the Mummy create a branch,
        which is just another copy of the repository's files and directories
        that is also under version control.
        They can work in their branch without disturbing Wolfman and Dracula and vice versa:
      </p>

      <figure id="f:branch_merge">
        <img src="img/svn/branch_merge.png" alt="Branching and Merging" />
      </figure>

      <p>
        Branches in version control repositories are often described as "parallel universes".
        Each branch starts off as a clone of the project at some moment in time
        (typically each time the software is released,
        or whenever work starts on a major new feature).
        Changes made to a branch only affect that branch,
        just as changes made to the files in one directory don't affect files in other directories.
        However,
        the branch and the main line are both stored in the same repository,
        so their revision numbers are always in step.
      </p>

      <p>
        If someone decides that a bug fix in one branch should also be made in another,
        all they have to do is merge the files in question.
        This is exactly like merging an old version of a file with the current one,
        but instead of going backward in time,
        the change is brought sideways from one branch to another.
      </p>

      <p>
        Branching helps projects scale up by letting sub-teams work independently,
        but too many branches can cause as many problems as they solve.
        Karl Fogel's excellent book
        <a href="bib.html#fogel-producing-oss"><cite>Producing Open Source Software</cite></a>,
        and Laura Wingerd and Christopher Seiwald's paper
        "<a href="bib.html#wingerd-seiwald-scm">High-level Best Practices in Software Configuration Management</a>",
        talk about branches in much more detail.
        Projects usually don't need to do this until they have a dozen or more developers,
        or until several versions of their software are in simultaneous use,
        but using branches is a key part of switching from software carpentry to software engineering.
      </p>

      <div class="keypoints" id="k:rollback">
        <h3>Summary</h3>
        <ul>
          <li>Old versions of files can be recovered by merging their old state with their current state.</li>
          <li>Recovering an old version of a file does not erase the intervening changes.</li>
          <li>Use branches to support parallel independent development.</li>
          <li><code>svn merge</code> merges two revisions of a file.</li>
          <li><code>svn revert</code> undoes local changes to files.</li>
        </ul>
      </div>

    </section>

    <section id="s:setup">

      <h2>Setting up a Repository</h2>

      <div class="understand" id="u:setup">
        <h3>Understand:</h3>
        <ul>
          <li>How to create a repository.</li>
        </ul>
      </div>

      <p>
        It is finally time to see how to create a repository.
        As a quick recap,
        we will keep the master copy of our work in a repository
        on a server that we can access from other machines on the internet.
        That master copy consists of files and directories that no-one ever edits directly.
        Instead, a copy of Subversion running on that machine
        manages updates for us and watches for conflicts.
        Our working copy is a mirror image of the master sitting on our computer.
        When our Subversion client needs to communicate with the master,
        it exchanges data with the copy of Subversion running on the server.
      </p>

      <figure id="f:repo_four_things">
        <img src="img/svn/repo_four_things.png" alt="What's Needed for a Repository" />
      </figure>

      <p>
        To make this to work, we need four things
        (<a href="#f:repo_four_things">Figure XXX</a>):
      </p>

      <ol>

        <li>
          The repository itself.
          It's not enough to create an empty directory and start filling it with files:
          Subversion needs to create a lot of other structure
          in order to keep track of old revisions, who made what changes, and so on.
        </li>

        <li>
          The full URL of the repository.
          This includes the URL of the server
          and the path to the repository on that machine.
          (The second part is needed because a single server can,
          and usually will,
          host many repositories.)
        </li>

        <li>
          Permission to read or write the master copy.
          Many open source projects give the whole world permission to read from their repository,
          but very few allow strangers to write to it:
          there are just too many possibilities for abuse.
          Somehow, we have to set up a password or something like it
          so that users can prove who they are.
        </li>

        <li>
          A working copy of the repository on our computer.
          Once the first three things are in place,
          this just means running the <code>checkout</code> command.
        </li>

      </ol>

      <p>
        To keep things simple,
        we will start by creating a repository on the machine that we're working on.
        This won't let us share our work with other people,
        but it <em>will</em> allow us to save the history of our work as we go along.
      </p>

      <p>
        The command to create a repository is <code>svnadmin create</code>,
        followed by the path to the repository.
        If we want to create a repository called <code>lair_repo</code>
        directly under our home directory,
        we just <code>cd</code> to get home
        and run <code>svnadmin create lair_repo</code>.
        This command creates a directory called <code>lair_repo</code> to hold our repository,
        and fills it with various files that Subversion uses
        to keep track of the project's history:
      </p>

<pre>
$ <span class="in">cd</span>
$ <span class="in">svnadmin create lair_repo</span>
$ <span class="in">ls -F lair_repo</span>
<span class="out">README.txt    conf/    db/    format    hooks/    locks/</span>
</pre>

      <p class="continue">
        We should <em>never</em> edit anything in this repository directly.
        Doing so probably won't shred our sanity and leave us gibbering in mindless horror,
        but it will almost certainly make the repository unusable.
      </p>

      <p>
        To get a working copy of this repository,
        we use Subversion's <code>checkout</code> command.
        If our home directory is <code>/users/mummy</code>,
        then the full path to the repository we just created is <code>/users/mummy/lair_repo</code>,
        so we run <code>svn checkout file:///users/mummy/lair lair_working</code>.
      </p>

      <p>
        Working backward,
        the second argument,
        <code>lair_working</code>,
        specifies where the working copy is to be put.
        The first argument is the URL of our repository,
        and it has two parts.
        <code>/users/mummy/lair_repo</code> is the path to repository directory.
        <code>file://</code> specifies the <a href="glossary.html#protocol">protocol</a>
        that Subversion will use to communicate with the repository&mdash;in this case,
        it says that the repository is part of the local machine's filesystem.
        Notice that the protocol ends in two slashes,
        while the absolute path to the repository starts with a slash,
        making three in total.
        A very common mistake is to type only two, since that's what web URLs normally have.
      </p>

      <p>
        When we're doing a checkout,
        it is <em>very</em> important that we provide the second argument,
        which specifies the name of the directory we want the working copy to be put in.
        Without it,
        Subversion will try to use the name of the repository,
        <code>lair_repo</code>,
        as the name of the working copy.
        Since we're in the directory that contains the repository,
        this means that Subversion will try to overwrite the repository with a working copy.
        Again,
        there isn't much risk of our sanity being torn to shreds,
        but this could ruin our repository.
      </p>

      <p>
        To avoid this problem,
        most people create a sub-directory in their account called something like <code>repos</code>,
        and then create their repositories in that.
        For example,
        we could create our repository in <code>/users/mummy/repos/lair</code>,
        then check out a working copy as <code>/users/mummy/lair</code>.
        This practice makes both names easier to read.
      </p>

      <p>
        The obvious next steps are
        to put our repository on a server,
        rather than on our personal machine,
        and to give other people access to the repository we have just created
        so that they can work with us.
        We'll discuss the first in <a href="web.html#s:svn">a later chapter</a>,
        but unfortunately,
        the second really does require things that we are not going to cover in this course.
        If you want to do this, you can:
      </p>

      <ul>

        <li>
          ask your system administrator to set it up for you;
        </li>

        <li>
          use an open source hosting service like <a href="http://www.sf.net">SourceForge</a>,
          <a href="http://code.google.com">Google Code</a>,
          <a href="https://github.com/">GitHub</a>,
          or <a href="https://bitbucket.org/">BitBucket</a>; or
        </li>

        <li>
          spend a few dollars a month on a commercial hosting service like <a href="http://dreamhost.com">DreamHost</a>
          that provides web-based GUIs for creating and managing repositories.
        </li>

      </ul>

      <p>
        If you choose the second or third option,
        please check with whoever handles intellectual property at your institution
        to make sure that putting your work on a commercially-operated machine
        that is probably in some other legal jurisdiction
        isn't going to cause trouble.
        Many people assume that it's "just OK",
        while others act as if not having asked will be an acceptable defence later on.
        Unfortunately,
        neither is true&hellip;
      </p>

      <div class="keypoints" id="k:setup">
        <h3>Summary</h3>
        <ul>
          <li>Repositories can be hosted locally, on local (departmental) servers, on hosting services, or on their owners' own domains.</li>
          <li><code>svnadmin create <em>name</em></code> creates a new repository.</li>
        </ul>
      </div>

    </section>

    <section id="s:provenance">

      <h2>Provenance</h2>

      <div class="understand" id="u:provenance">
        <h3>Understand:</h3>
        <ul>
          <li>What data provenance is.</li>
          <li>How to embed version numbers and other information in files managed by version control.</li>
          <li>How to record version information about a program in its output.</li>
        </ul>
      </div>

      <p>
        In art,
        the <a href="glossary.html#provenance">provenance</a> of a work
        is the history of who owned it, when, and where.
        In science,
        it's the record of how a particular result came to be:
        what raw data was processed by what version of what program to create which intermediate files,
        what was used to turn those files into which figures of which papers,
        and so on.
      </p>

      <p>
        One of the central ideas of this course is that
        wen can automatically track the provenance of scientific data.
        To start,
        suppose we have a text file <code>combustion.dat</code> in a Subversion repository.
        Run the following two commands:
      </p>

<pre>
$ svn propset svn:keywords Revision combustion.dat
$ svn commit -m "Turning on the 'Revision' keyword" combustion.dat
</pre>

      <p>
        Now open the file in an editor
        and add the following line somewhere near the top:
      </p>

<pre>
# $Revision:$
</pre>

      <p>
        The '#' sign isn't important:
        it's just what <code>.dat</code> files use to show comments.
        The <code>$Revision:$</code> string,
        on the other hand,
        means something special to Subversion.
        Save the file, and commit the change:
      </p>

<pre>
$ svn commit -m "Inserting the 'Revision' keyword" combustion.dat
</pre>

      <p>
        When we open the file again,
        we'll see that Subversion has changed that line to something like:
      </p>

<pre>
# $Revision: 143$
</pre>

      <p class="continue">
        i.e., Subversion has inserted the version number
        after the colon and before the closing <code>$</code>.
      </p>

      <p>
        Here's what just happened.
        First, Subversion allows you to set
        <a href="glossary.html#property-subversion">properties</a>
        for files and and directories.
        These properties aren't in the files or directories themselves,
        but live in Subversion's database.
        One of those properties,
        <code>svn:keywords</code>,
        tells Subversion to look in files that are being changed
        for strings of the form <code>$propertyname: &hellip;$</code>,
        where <code>propertyname</code> is a string like <code>Revision</code> or <code>Author</code>.
        (About half a dozen such strings are supported.)
      </p>

      <p>
        If it sees such a string,
        Subversion rewrites it as the commit is taking place to replace <code>&hellip;</code>
        with the current version number,
        the name of the person making the change,
        or whatever else the property's name tells it to do.
        You only have to add the string to the file once;
        after that,
        Subversion updates it for you every time the file changes.
      </p>

      <p>
        Putting the version number in the file this way can be pretty handy.
        If you copy the file to another machine,
        for example,
        it carries its version number with it,
        so you can tell which version you have even if it's outside version control.
        We'll see some more useful things we can do with this information in
        <a href="python.html">the next chapter</a>.
      </p>

      <div class="box">

        <h3>When <em>Not</em> to Use Version Control</h3>

        <p>
          Despite the rapidly decreasing cost of storage,
          it is still possible to run out of disk space.
          In some labs,
          people can easy go through 2 TB/month if they're not careful.
          Since version control tools usually store revisions in terms of lines,
          with binary data files,
          they end up essentially storing every revision separately.
          This isn't that bad
          (it's what we'd be doing anyway),
          but it means version control isn't doing what it likes to do,
          and the repository can get very large very quickly.
          Another concern is that if very old data will no longer be used,
          it can be nice to archive or delete old data files.
          This is not possible if our data is version controlled:
          information can only be added to a repository,
          so it can only ever increase in size.
        </p>

      </div>

      <p>
        We can use this trick with shell scripts too,
        or with almost any other kind of program.
        Going back to Nelle Nemo's data processing from the previous chapter,
        for example,
        suppose she writes a shell script that uses <code>gooclean</code>
        to tidy up data files.
        Her first version looks like this:
      </p>

<pre>
for filename in $*
do
    gooclean -b 0 100 &lt; $filename &gt; cleaned-$filename
done
</pre>

      <p class="continue">
        i.e., it runs <code>gooclean</code> with bounding values of 0 and 100
        for each specified file,
        putting the result in a temporary file with a well-defined name.
        Assuming that '#' is the comment character for those kinds of data files,
        she could instead write:
      </p>

<pre>
for filename in $*
do
    <span class="highlight">echo "gooclean $Revision: 901$ -b 0 100" &gt; $filename</span>
    gooclean -b 0 100 &lt; $filename <span class="highlight">&gt;&gt;</span> cleaned-$filename
done
</pre>

      <p>
        The first change puts a line in the output file
        that describes how that file was created.
        The second change is to use <code>&gt;&gt;</code> instead of <code>&gt;</code>
        to redirect <code>gooclean</code>'s output to the file.
        <code>&gt;&gt;</code> means "append to":
        instead of overwriting whatever is in the file,
        it adds more content to it.
        This ensures that the first line of the file is the provenance record,
        with the actual output of <code>gooclean</code> after it.
      </p>

      <div class="keypoints" id="k:provenance">
        <h3>Summary</h3>
        <ul>
          <li><code>$Keyword:$</code> in a file can be filled in with a property value each time the file is committed.</li>
          <li idea="paranoia">Put version numbers in programs' output to establish provenance for data.</li>
          <li><code>svn propset svn:keywords <em>property</em> <em>files</em></code> tells Subversion to start filling in property values.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

      <p>
        Correlation does not imply causality,
        but there is a very strong correlation between
        using version control
        and doing good computational science.
        There's an equally strong correlation
        between <em>not</em> using it and wasting effort,
        so today (the middle of 2012),
        I will not review a paper if the software used in it
        is not under version control.
        Its authors' work might be interesting,
        but without the kind of record-keeping that version control provides,
        there's no way to know exactly what they did and when.
        Just as importantly,
        if someone doesn't know enough about computing to use version control,
        the odds are good that they don't know enough
        to do the programming right either.
      </p>

    </section>