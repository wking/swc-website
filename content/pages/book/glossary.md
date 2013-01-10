Title: Glossary
Directory: book


<p>
  <a href="#A">A</a>
  <a href="#B">B</a>
  <a href="#C">C</a>
  <a href="#D">D</a>
  <a href="#E">E</a>
  <a href="#F">F</a>
  <a href="#G">G</a>
  <a href="#H">H</a>
  <a href="#I">I</a>
  <a href="#J">J</a>
  <a href="#K">K</a>
  <a href="#L">L</a>
  <a href="#M">M</a>
  <a href="#N">N</a>
  <a href="#O">O</a>
  <a href="#P">P</a>
  <a href="#Q">Q</a>
  <a href="#R">R</a>
  <a href="#S">S</a>
  <a href="#T">T</a>
  <a href="#U">U</a>
  <a href="#V">V</a>
  <a href="#W">W</a>
  <a href="#X">X</a>
  <a href="#Y">Y</a>
  <a href="#Z">Z</a>
</p>

    <section id="A">

      <h2>A</h2>

      <dl class="gloss">

        <dt id="absolute-path">absolute path</dt>
        <dd>
          A <a href="#path">path</a> that refers to a particular location in a file system.  Absolute paths are usually written with respect to the file system's <a href="#root-directory">root directory</a>, and begin with either "/" (on Unix) or "\" (on Microsoft Windows). See also: <a href="#relative-path">relative path</a>.
        </dd>

        <dt id="access-control">access control</dt>
        <dd>
          A way to specify who has permission to view, edit, delete, run, or otherwise interact with something, by explicitly listing what rights each individual or group has.  This is in contrast with the standard Unix <a href="#authorization">authorization</a> mechanism, which only allows a fixed set of privileges to be listed for owner, one group, and everyone else.
        </dd>

        <dt id="access-control-list">access control list (ACL)</dt>
        <dd>
          A way to specify who has permission to view, edit, delete, run, or otherwise interact with something, by explicitly listing what rights each individual or group has.  This is in contrast with the standard Unix <a href="#authorization">authorization</a> mechanism, which only allows a fixed set of privileges to be listed for owner, one group, and everyone else.
        </dd>

        <dt id="acid">ACID</dt>
        <dd>
          An acronym for atomic, consistent, isolated, and durable, which are the properties that a <a href="#transaction">database transaction</a> must guarantee.
        </dd>

        <dt id="acquire-lock">acquire a lock</dt>
        <dd>
          To claim a <a href="#lock">lock</a> in order to establish exclusive access to some resource. See also: <a href="#release-lock">release a lock</a>.
        </dd>

        <dt id="actual-result">actual result</dt>
        <dd>
          The actual result of a <a href="#unit-test">unit test</a>. If this matches the <a href="#expected-result">expected result</a>, the test passes.
        </dd>

        <dt id="aggregate">aggregate</dt>
        <dd>
          To create a single value by combining multiple values, e.g. by adding or averaging.
        </dd>

        <dt id="alias">alias</dt>
        <dd>
          A second (or subsequent) reference to a single piece of data. Aliasing can make programs more difficult to understand, since changes made through one reference "magically" affect the other.
        </dd>

        <dt id="amdahls-law">Amdahl's Law</dt>
        <dd>
          A rule first stated by Gene Amdahl that explains why adding more hardware can't keep making programs faster indefinitely.  For example, if 90% of the program can take advantage of the extra hardware, but 10% cannot, the greatest possible speedup is a factor of ten.
        </dd>

        <dt id="anchor">anchor</dt>
        <dd>
          An element of a <a href="#regular-expression">regular expression</a> that matches a location, rather than a sequence of characters.      <code>^</code> matches the beginning of a line, <code>\b</code> matches the break between word and non-word characters, and <code>$</code> matches the end of a line.
        </dd>

        <dt id="assertion">assertion</dt>
        <dd>
          An expression which is supposed to be true at a particular point in a program.  Programmers typically put assertions in their code to check for errors; if the assertion fails (i.e., if the expression evaluates as false), the program halts and produces an error message.
        </dd>

        <dt id="asymmetric-cipher">asymmetric cipher</dt>
        <dd>
          A <a href="#cipher">cipher</a> which has two <a href="#key">keys</a>, each of which undoes the other's effects. See also: <a href="#symmetric-cipher">symmetric cipher</a>.
        </dd>

        <dt id="atomic-operation">atomic operation</dt>
        <dd>
          Not interruptible.  An atomic operation is one that always takes effect as a whole, no matter what else the system is doing.
        </dd>

        <dt id="atomic-value">atomic value</dt>
        <dd>
          A value that cannot be decomposed into smaller pieces.  For example, the number 12 is usually considered atomic (unless we are teaching addition to school children, in which case we might decompose it into tens and ones).
        </dd>

        <dt id="attribute">attribute</dt>
        <dd>
          An extra property added to an XML <a href="#element">element</a>.  Attributes are represented as name/value pairs; a given name may appear at most once for any particular element.
        </dd>

        <dt id="authentication">authentication</dt>
        <dd>
          The act of establishing someone's identity.  This is almost always done by requiring them to produce some credentials, such as a password. See also: <a href="#authorization">authorization</a>, <a href="#access-control">access control</a>.
        </dd>

        <dt id="authorization">authorization</dt>
        <dd>
          The part of a computer security system that keeps track of who's allowed to do what. See also: <a href="#authentication">authentication</a>, <a href="#access-control">access control</a>.
        </dd>

      </dl>

    </section>

    <section id="B">

      <h2>B</h2>

      <dl class="gloss">

        <dt id="boundary-case">boundary case</dt>
        <dd>
          In testing, an input that is just at, or just beyond, some extreme value.  A database containing no records, or a list whose length is the greatest possible integer, are both examples of boundary cases.
        </dd>

        <dt id="branch">branch</dt>
        <dd>
          A separate line of development managed by a <a href="#version-control-system">version control system</a>. Branches help projects manage incompatible sets of changes that are being made concurrently. See also: <a href="#merge">merge</a>.
        </dd>

        <dt id="breakpoint">breakpoint</dt>
        <dd>
          A marker put in a program by a <a href="#debugger">debugger</a> that causes it to pause so that the program's internal state can be inspected (and possibly modified).
        </dd>

      </dl>

    </section>

    <section id="C">

      <h2>C</h2>

      <dl class="gloss">

        <dt id="call-stack">call stack</dt>
        <dd>
          A data structure used to keep track of functions that are currently being executed.  Each time a function is called, a new <a href="#stack-frame">stack frame</a> is put on the top of the stack to hold that function's local variables.  When the function returns, the stack frame is discarded. See also: <a href="#heap">heap</a>, <a href="#static-space">static space</a>.
        </dd>

        <dt id="cascading-delete">cascading delete</dt>
        <dd>
          In a database, the practice of automatically deleting things that depend on, or refer to, a record when that record is deleted.  See also: <a href="#referential-integrity">referential integrity</a>.
        </dd>

        <dt id="case-insensitive">case insensitive</dt>
        <dd>
          Treating text as if upper and lower case characters were the same.  See also: <a href="#case-sensitive">case sensitive</a>.
        </dd>

        <dt id="case-sensitive">case sensitive</dt>
        <dd>
          Treating upper and lower case characters as different.  See also: <a href="#case-insensitive">case insensitive</a>.
        </dd>

        <dt id="catch-exception">catch exception</dt>
        <dd>
          To handle an <a href="#exception">exception</a>. See also: <a href="#raise-exception">raise exception</a>.
        </dd>

        <dt id="check-out">check out</dt>
        <dd>
          To obtain an initial copy of a project from a version control system.
        </dd>

        <dt id="cipher">cipher</dt>
        <dd>
          An algorithm used to <a href="#encryption">encrypt</a> and <a href="#decryption">decrypt</a> data.
        </dd>

        <dt id="ciphertext">ciphertext</dt>
        <dd>
          The <a href="#encryption">encrypted</a> form of a message. Ciphertext is usually produced from <a href="#plaintext">plaintext</a> by a combination of a <a href="#cipher">cipher</a> algorithm and a <a href="#key">key</a>.
        </dd>

        <dt id="chunk">chunk</dt>
        <dd>
          A group of objects that are stored together in short-term memory, such as the seven digits in a North American phone number.
        </dd>

        <dt id="class">class</dt>
        <dd>
          A definition that specifies the properties of a set of <a href="#object">objects</a>.
        </dd>

        <dt id="client">client</dt>
        <dd>
          A software application that accesses data over a network.  The provider is called a <a href="#server">server</a>.
        </dd>

        <dt id="client-server-architecture">client-server architecture</dt>
        <dd>
          An asymmetric system in which many <a href="#client">clients</a> communicate with a single centralized <a href="#server">server</a>.
        </dd>

        <dt id="clui">CLUI</dt>
        <dd>
          A command-line user interface.  See also: <a href="#gui">GUI</a>.
        </dd>

        <dt id="code-coverage">code coverage</dt>
        <dd>
          The proportion of a program which has been exercised by tests. Code coverage is typically expressed as "percentage of lines tested". However, even 100% coverage does not guarantee that all possible conditions and paths have been tested.
        </dd>

        <dt id="column-major-order">column major order</dt>
        <dd>
          Storing matrix values by columns, and then by rows.  See also: <a href="#row-major-order">row major order</a>.
        </dd>

        <dt id="command-completion">command completion</dt>
        <dd>
          Completing the rest of a command when the user presses a shortcut key (typically tab).
        </dd>

        <dt id="command-line-arguments">command-line arguments</dt>
        <dd>
          Values passed to a program on the command line.  In Unix, the name of the program itself is always the first command-line argument to a program.
        </dd>

        <dt id="command-line-flag">command-line flag</dt>
        <dd>
          A terse way to specify an option or setting to a command-line program.  By convention, Unix applications use a dash followed by a single letter, such as <code>-v</code>, or two dashes followed by a word, such as <code>--verbose</code>, while DOS applications use a slash, such as <code>/V</code>.  Depending on the application, a flag may be followed by a single argument, as in <code>-o /tmp/output.txt</code>.
        </dd>

        <dt id="commit">commit</dt>
        <dd>
          To send changes from a <a href="#working-copy">working copy</a> to a <a href="#version-control-system">version control</a>'s <a href="#repository">repository</a> to create a new <a href="#revision">revision</a> of the affected file(s).  Changes must be committed in order for other users to see them. See also: <a href="#update">update</a>.
        </dd>

        <dt id="compiler">compiler</dt>
        <dd>
          A program that transforms the source of a program into something that can be executed.  That "something" can be saved for later use, or (in an <a href="#interpreter">interpreter</a>) executed immediately.
        </dd>

        <dt id="concurrency">concurrency</dt>
        <dd>
          The situation in which two or more things are going on at once. See also: <a href="#serialization">serialization</a>.
        </dd>

        <dt id="conditional-breakpoint">conditional breakpoint</dt>
        <dd>
          A <a href="#breakpoint">breakpoint</a> that only causes the program to pause under certain conditions.  For example, a <a href="#debugger">debugger</a> may specify that the program is to pause only when a certain function parameter is an empty string, or when a loop index is greater than a specified value.
        </dd>

        <dt id="conflict">conflict</dt>
        <dd>
          A change made by one user of a <a href="#version-control-system">version control system</a> that is incompatible with changes made by other users.  Helping users <a href="#resolve">resolve</a> conflicts is one of the <a href="#version-control-system">version control system</a>'s major tasks.
        </dd>

        <dt id="conflict-marker">conflict marker</dt>
        <dd>
          A string such as <code>&lt;&lt;&lt;&lt;&lt;&lt;</code>, <code>======</code>, or <code>&gt;&gt;&gt;&gt;&gt;&gt;</code> put into a local copy of a file by a <a href="#version-control-system">version control system</a> to indicate where local changes overlap with incompatible changes made by someone else.  The <a href="#version-control-system">version control system</a> will typically not allow the user to <a href="#commit">commit</a> changes until all conflicts have been <a href="#resolve">resolved</a>.
        </dd>

        <dt id="contract">contract</dt>
        <dd>
          The "agreement" between a function and its caller, usually expressed in terms of <a href="#precondition">preconditions</a> that must be true when the function is called in order for it to execute correctly, and <a href="#postcondition">postconditions</a> that the function guarantees will be true after the call completes.
        </dd>

        <dt id="core-dump">core dump</dt>
        <dd>
          A file containing a byte-for-byte representation of the contents of a program's memory.  On some <a href="#operating-system">operating systems</a>, programs produce core dumps whenever they terminate abnormally (e.g., try to divide by zero, or access memory that is out of bounds).  Core dumps are often used as the basis for <a href="#post-mortem-debugging">post mortem debugging</a>.
        </dd>

        <dt id="cross-product">cross product</dt>
        <dd>
          A pairing of all elements of one set with all elements of another. The cross product of two <em>N</em>-element vectors <em>L</em> and <em>R</em> is an <em>N&times;N</em> matrix <em>M</em>, in which <em>M<sub>i,j</sub>=L<sub>i</sub>R<sub>j</sub></em>.
        </dd>

        <dt id="css">Cascading Style Sheets (CSS)</dt>
        <dd>
          A language used to describe how HTML pages should be formatted for display.
        </dd>

        <dt id="current-working-directory">current working directory</dt>
        <dd>
          The directory that <a href="#relative-path">relative paths</a> are calculated from; equivalently, the place where files referenced by name only are searched for.  Every <a href="#process">process</a> has a current working directory.  The current working directory is usually referred to using the shorthand notation <code>.</code> (pronounced "dot").
        </dd>

        <dt id="cursor">cursor</dt>
        <dd>
          A pointer into a database that keeps track of outstanding transactions and other operations.
        </dd>

      </dl>

    </section>

    <section id="D">

      <h2>D</h2>

      <dl class="gloss">

        <dt id="data-parallel">data parallelism</dt>
        <dd>
          Applying the same operation to many data values at once.  This is the programming model that whole-array languages such as MATLAB use.
        </dd>

        <dt id="database-manager">database manager</dt>
        <dd>
          A set of values in a <a href="#relational-database">relational database</a> that are organized into <a href="#field-database">fields</a> and <a href="#record-database">records</a>.
        </dd>

        <dt id="database-table">database table</dt>
        <dd>
          A set of values in a <a href="#relational-database">relational database</a> that are organized into <a href="#field-database">fields</a> and <a href="#record-database">records</a>.
        </dd>

        <dt id="deadlock">deadlock</dt>
        <dd>
          Any situation in which no one can proceed unless someone else does first (analogous to having two locked boxes, each of which holds the key to the other). See also: <a href="#race-condition">race condition</a>.
        </dd>

        <dt id="debuggee">debuggee</dt>
        <dd>
          See <a href="#target-program">target program</a>.
        </dd>

        <dt id="debugger">debugger</dt>
        <dd>
          A computer program that is used to control and inspect another program (called the <a href="#target-program">target program</a>).  Most debuggers are <em>symbolic</em> debuggers that show the target program's state in terms of the variables that the programmer created, rather than showing the raw contents of memory.
        </dd>

        <dt id="decryption">decryption</dt>
        <dd>
          The process of translating <a href="#encryption">encrypted</a> <a href="#ciphertext">ciphertext</a> back into the original <a href="#plaintext">plaintext</a>. See also: <a href="#cipher">cipher</a>, <a href="#key">key</a>.
        </dd>

        <dt id="defensive-programming">defensive programming</dt>
        <dd>
          The practice of checking input values, <a href="#invariant">invariants</a>, and other aspects of a program in order to catch errors as early as possible.
        </dd>

        <dt id="default-value">default value</dt>
        <dd>
          A value to use if nothing else is specified explicitly.
        </dd>

        <dt id="design-pattern">design pattern</dt>
        <dd>
          A standard solution to a commonly-occurring problem.
        </dd>

        <dt id="deterministic-profiler">deterministic profiler</dt>
        <dd>
          A <a href="#profiler">profiler</a> that records events as they happen to produce an exact trace of a program's behavior.  See also: <a href="#statistical-profiler">statistical profiler</a>.
        </dd>

        <dt id="directory-tree">directory tree</dt>
        <dd>
          File system directories are normally organized hierarchically: each directory except the <a href="#root-directory">root</a> has a single parent, and each may have zero or more children.  This means that directories may be viewed as a tree.  Since files may not contain directories or other files, they are always leaf nodes of this tree.
        </dd>

        <dt id="dictionary">dictionary</dt>
        <dd>
          A mutable unordered collection that pairs each <a href="#key">key</a> with a single value.  Dictionaries are also known as maps, hashes, or associative arrays, and are typically implemented using <a href="#hash-table">hash tables</a>.
        </dd>

        <dt id="docstring">docstring</dt>
        <dd>
          Short for "documentation string", this refers to textual documentation embedded in Python programs.  Unlike comments, docstrings are preserved in the running program, and can be examined in interactive sessions.
        </dd>

        <dt id="document">document</dt>
        <dd>
          A well-formed instance of <a href="#xml">XML</a>.  Documents can be represented as trees (using <a href="#document-object-model">DOM</a>), stored as files on disk, etc.
        </dd>

        <dt id="document-object-model">Document Object Model (DOM)</dt>
        <dd>
          A cross-language standard for representing XML documents as trees.
        </dd>

        <dt id="domain-decomposition">domain decomposition</dt>
        <dd>
          Dividing the data used in a program into pieces, and having a separate processor operate on each piece.
        </dd>

        <dt id="dns">Domain Name System (DNS)</dt>
        <dd>
          A system which maps numeric <a href="#internet-protocol">Internet Protocol</a> addresses, such as <code>128.100.171.16</code>, to human-readable names, such as <code>third-bit.com</code>.
        </dd>

        <dt id="drive-letter">drive letter</dt>
        <dd>
          In Windows, a single character that identifies a specific <a href="#file-system">file system</a>.  Drive letters originally referred to actual (physical) disk drives.
        </dd>

      </dl>

    </section>

    <section id="E">

      <h2>E</h2>

      <dl class="gloss">

        <dt id="element">element</dt>
        <dd>
          A named item in an <a href="#xml">XML</a> <a href="#document">document</a>, which has a unique parent, and may contain <a href="#attribute">attributes</a>, text, and other elements. See also: <a href="#tag-xml">tag (in XML)</a>.
        </dd>

        <dt id="empty-list">empty list</dt>
        <dd>
          A list containing no values.
        </dd>

        <dt id="encryption">encryption</dt>
        <dd>
          The process of translating <a href="#plaintext">plaintext</a> that anyone can understand into <a href="#ciphertext">ciphertext</a> that can only be understood by someone possessing the correct <a href="#cipher">cipher</a> and <a href="#key">key</a>.
        </dd>

        <dt id="escape-sequence">escape sequence</dt>
        <dd>
          A sequence of characters that represents some other character or special entity.      <code>\t</code> and <code>\n</code> are escape sequences in normal Python strings that represent tab and newline characters respectively; <code>&amp;lt;</code> and <code>&amp;amp;</code> are escape sequences in HTML and XML that represents the less than sign and ampersand.
        </dd>

        <dt id="exception">exception</dt>
        <dd>
          An object that represents an error condition.  As a program executes, it creates a stack of <a href="#exception-handler">exception handlers</a>.  When an exception is <a href="#raise-exception">raised</a>, the program searches this stack for the top-most handler, which <a href="#catch-exception">catches</a> and handles the exception. Exceptions typically contain information such as the file and line where the error occurred, the type of the error, and an error message.
        </dd>

        <dt id="exception-handler">exception handler</dt>
        <dd>
          A block of code that deals with the error signalled by an <a href="#exception">exception</a>. See also: <a href="#catch-exception">catch exception</a>, <a href="#raise-exception">raise exception</a>.
        </dd>

        <dt id="exclusive-or">exclusive or</dt>
        <dd>
          A logical operator that is true if one or other of its arguments is true, but not both.  See also: <a href="#inclusive-or">inclusive or</a>.
        </dd>

        <dt id="expected-result">expected result</dt>
        <dd>
          The outcome a test must produce in order to pass.  If the <a href="#actual-result">actual result</a> is different, the test fails.
        </dd>

        <dt id="expression">expression</dt>
        <dd>
          Something in a program that has a value. "5" has the value 5, "len('abc')" has the value 3, and so on.  Expressions may be used in <a href="#statement">statements</a>, but not vice versa.
        </dd>

      </dl>

    </section>

    <section id="F">

      <h2>F</h2>

      <dl class="gloss">

        <dt id="faded-example">faded example</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="fall-through">fall-through</dt>
        <dd>
          In a program, the code we execute by default if we do not choose some other path explicitly.
        </dd>

        <dt id="field-database">field (in database)</dt>
        <dd>
          A set of data values of a particular type, one for each record in a <a href="#database-table">table</a>, typically shown as a column. See also: <a href="#record-database">record</a>.
        </dd>

        <dt id="file-system">file system</dt>
        <dd>
          A set of files, directories, and I/O devices (such as keyboards, screens, printers, and so on).  A file system may be spread across many physical devices, or many file systems may be stored on a single physical device.  The <a href="#operating-system">operating system</a> will only allow some file operations (such as copying, or creating symbolic links or shortcuts) within a file system.
        </dd>

        <dt id="filename-extension">filename extension</dt>
        <dd>
          The portion of a file's name that comes after the final "." character.  By convention, this identifies the file's type: <code>.txt</code> means "text file", <code>.png</code> means "Portable Network Graphics file", and so on.  These conventions are <em>not</em> enforced by most operating systems: it is perfectly possible to name an MP3 sound file <code>homepage.html</code>.  Since many applications use filename extensions to identify the <a href="#mime">MIME type</a> of the file, misnaming files may cause those applications to fail.
        </dd>

        <dt id="filter">filter</dt>
        <dd>
          A program that transforms a stream of data.  Many Unix command-line tools are written as filters: they read data from <a href="#standard-input">standard input</a>, process it, and write the result to <a href="#standard-output">standard output</a>.  Image processing applications are often constructed by connecting filters to one another.
        </dd>

        <dt id="fixture">fixture</dt>
        <dd>
          The particular configuration of a system that is the subject of a <a href="#unit-test">unit test</a>.  It is a good practice to create a fresh fixture for each test, so that the actions and outcomes of early tests cannot affect later ones.
        </dd>

        <dt id="flag">flag</dt>
        <dd>
          A variable used to track the current state of processing.  For example, a flag can be used to show whether a negative number has previously been seen in a list of numbers.
        </dd>

        <dt id="float">floating point number</dt>
        <dd>
          A number containing a fractional part and an exponent.
        </dd>

        <dt id="for-loop">for loop</dt>
        <dd>
          A loop that is executed once for each value in some kind of set, list, or range.
        </dd>

        <dt id="foreign-key">foreign key</dt>
        <dd>
          One or more values in a <a href="#database-table">database table</a> that identify a <a href="#record-database">records</a> in another table.
        </dd>

        <dt id="function">function</dt>
        <dd>
          A portion of a program with an independent identity that can be invoked by other parts of the program.
        </dd>

      </dl>

    </section>

    <section id="G">

      <h2>G</h2>

      <dl class="gloss">

        <dt id="global-scope">global scope</dt>
        <dd>
          The top-level <a href="#variable-scope">variable scope</a> that includes the entire program.
        </dd>

        <dt id="gui">GUI</dt>
        <dd>
          A graphical user interface.  See also: <a href="#clui">CLUI</a>.
        </dd>

      </dl>

    </section>

    <section id="H">

      <h2>H</h2>

      <dl class="gloss">

        <dt id="hash-function">hash function</dt>
        <dd>
          A function which takes an object as its input, and produces an integer value as its output.  Good hash functions produce outputs that are as random as possible, i.e., they have the property that different inputs are likely to produce different outputs.
        </dd>

        <dt id="hash-table">hash table</dt>
        <dd>
          A data structure which allows programs to look up objects by value, rather than by location.  Hash tables do this by using a <a href="#hash-function">hash function</a> to calculate seemingly-random identifiers for values, and using those as indices into an array.  Under normal conditions, it takes constant time to find a value in a hash table.
        </dd>

        <dt id="handle">handle</dt>
        <dd>
          A variable that refers to some external resource, such as an open file.
        </dd>

        <dt id="head">head</dt>
        <dd>
          The most recent revision in a version control repository.
        </dd>

        <dt id="heap">heap</dt>
        <dd>
          An area of memory out of which a program can dynamically allocate blocks of various sizes in order to store values. See also: <a href="#call-stack">call stack</a>, <a href="#static-space">static space</a>.
        </dd>

        <dt id="heisenbug">heisenbug</dt>
        <dd>
          A bug that hides when you are looking for it. Bugs can arise in sequential programs (for example, adding a <code>printf</code> call to a C program may move things around in memory so that the bug is no longer triggered), but are much more common in <a href="#concurrency">concurrent</a> programs.
        </dd>

        <dt id="higher-order-functions">higher order functions</dt>
        <dd>
          A function which operates on other functions.
        </dd>

        <dt id="home-directory">home directory</dt>
        <dd>
          The default directory associated with an account on a computer system.  By convention, all of a user's files are stored in or below her home directory.
        </dd>

        <dt id="host-address">host address</dt>
        <dd>
          A computer's Internet address.
        </dd>

        <dt id="html">HTML</dt>
        <dd>
          The HyperText Markup Language used to format web pages.
        </dd>

        <dt id="http">Hypertext Transfer Protocol (HTTP)</dt>
        <dd>
          A set of rules for exchanging data (especially files) on the World Wide Web.
        </dd>

        <dt id="http-header">HTTP header</dt>
        <dd>
          A name/value pair at the start of an HTTP request or response. Unlike dictionary keys, names are not required to be unique.
        </dd>

      </dl>

    </section>

    <section id="I">

      <h2>I</h2>

      <dl class="gloss">

        <dt id="idiom">idiom</dt>
        <dd>
          definition
        </dd>

        <dt id="immutable">immutable</dt>
        <dd>
          Unchangeable.  The value of immutable data cannot be altered after it has been created. See also: <a href="#mutable">mutable</a>.
        </dd>

        <dt id="implementation">implementation</dt>
        <dd>
          How a function, class, or other program element is constructed.  The term is usually used in contrast with <a href="#interface">interface</a>.
        </dd>

        <dt id="inclusive-or">inclusive or</dt>
        <dd>
          A logical operator that is true if either or both of its arguments is true.  See also: <a href="#exclusive-or">exclusive or</a>.
        </dd>

        <dt id="infinite-loop">infinite loop</dt>
        <dd>
          A loop which would never terminate without outside intervention, such as <code>while True: pass</code> in Python. In practice, all "infinite" loops are eventually terminated, if only by the computer being switched off.
        </dd>

        <dt id="inner-loop">inner loop</dt>
        <dd>
          A loop that is inside another loop.  See also: <a href="#outer-loop">outer loop</a>.
        </dd>

        <dt id="integration-test">integration test</dt>
        <dd>
          A test that checks whether the parts of a program work together. See also: <a href="#unit-test">unit test</a>.
        </dd>

        <dt id="interface">interface</dt>
        <dd>
          A specification of the behavior of a function, class, or other unit of software.  The term is usually used in contrast with <a href="#implementation">implementation</a>.
        </dd>

        <dt id="invasion-percolation">invasion percolation</dt>
        <dd>
          A physical process in which a fluid seeps into a porous material, displacing anything that might already be there.
        </dd>

        <dt id="internet-protocol">Internet Protocol (IP)</dt>
        <dd>
          A family of communication protocols, the most widely used of which are <a href="#udp">UDP</a> and <a href="#tcp">TCP</a>.
        </dd>

        <dt id="invariant">invariant</dt>
        <dd>
          An expression whose value doesn't change during the execution of a program.  For example, an invariant property of a loop indexed by a variable <code>i</code> might be that the value of the variable <code>M</code> is always greater than or equal to the values of the array elements whose indices are less than <code>i</code>. See also: <a href="#precondition">precondition</a>, <a href="#postcondition">postcondition</a>.
        </dd>

        <dt id="ip-address">IP address</dt>
        <dd>
          A numerical identifier associated with a particular device on a network that uses the <a href="#internet-protocol">Internet Protocol</a> for communication.
        </dd>

      </dl>

    </section>

    <section id="J">

      <h2>J</h2>

    </section>

    <section id="K">

      <h2>K</h2>

      <dl class="gloss">

        <dt id="key">key</dt>
        <dd>
          The data that is used to index a particular entry in a <a href="#dictionary">dictionary</a>.  In a phone book, for example, people's names are keys.
        </dd>

        <dt id="key-pair">key pair</dt>
        <dd>
          definition
        </dd>

      </dl>

    </section>

    <section id="L">

      <h2>L</h2>

      <dl class="gloss">

        <dt id="library">library</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="list">list</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="list-indexing">list indexing</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="loader">loader</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="local-scope">local scope</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="lock">lock</dt>
        <dd>
          A mechanism used to control access to resources in <a href="#concurrency">concurrent systems</a>.  If a <a href="#process">process</a> A tries to <a href="#acquire-lock">acquire</a> a lock held by some other <a href="#process">process</a> B, A is forced to wait until B releases it.
        </dd>

        <dt id="loop-body">loop body</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="loop-variable">loop variable</dt>
        <dd class="fixme">FIXME</dd>

      </dl>

    </section>

    <section id="M">

      <h2>M</h2>

      <dl class="gloss">

        <dt id="main-line">main line</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="markup-language">markup language</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="mask">mask</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="mental-model">mental model</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="merge">merge</dt>
        <dd>
          To combine the contents of two or more versions of a file in order to <a href="#resolve">resolve</a> overlapping edits; also, to combine material from two or more <a href="#branch">branches</a>.
        </dd>

        <dt id="metadata">metadata</dt>
        <dd>
          Literally, "data about data", i.e., data such as a format descriptor, which describes other data.
        </dd>

        <dt id="method">method</dt>
        <dd>
          In object-oriented programming, a function which is tied to a particular <a href="#object">object</a>.  Typically, each of an object's methods implements one of the things it can do, or one of the questions it can answer.
        </dd>

        <dt id="mime">Multipurpose Internet Mail Extensions (MIME)</dt>
        <dd>
          An Internet standard for the format of email that also specifies which filename suffixes should be used to identify particular types of content (such as <code>.png</code> for a PNG-format image).
        </dd>

        <dt id="model">model</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="module">module</dt>
        <dd>
          A set of functions and variables that are grouped together to make them more manageable.  In Python, every source file is automatically a module; in other languages, source files may contain many modules, or a single module may span several files.
        </dd>

        <dt id="multi-valued-assignment">multi-valued assignment</dt>
        <dd>
          An assignment statement which changes several values at once. For example, <code>a,b = 2,3</code> sets <code>a</code> to 2 and <code>b</code> to 3, while <code>a,b = b,a</code> swaps those variables' values.
        </dd>

        <dt id="mutable">mutable</dt>
        <dd>
          Changeable.  The value of mutable data can be updated in place. See also: <a href="#immutable">immutable</a>.
        </dd>

      </dl>

    </section>

    <section id="N">

      <h2>N</h2>

      <dl class="gloss">

        <dt id="namespace">namespace</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="nested-list">nested list</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="nested-loop">nested loop</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="nested-query">nested query</dt>
        <dd>
          A <a href="#query">query</a> whose results are used as input by some other query.
        </dd>

        <dt id="notional-machine">notional machine</dt>
        <dd class="fixme">FIXME</dd>

      </dl>

    </section>

    <section id="O">

      <h2>O</h2>

      <dl class="gloss">

        <dt id="object">object</dt>
        <dd>
          A combination of data and functions (called <a href="#method">methods</a>) that are meant to work together. In most programming languages, objects are instances of <a href="#class">classes</a>; each object represents one "thing" that the program can operate on.
        </dd>

        <dt id="operating-system">operating system</dt>
        <dd>
          The software responsible for managing a computer's hardware and other processes.  Operating systems are also responsible for making different computers present the same interface to other programs, so that applications like word processors and compilers don't have to be re-written each time a new generation of chips comes out.  Popular desktop operating systems include Microsoft Windows, Linux, and Mac OS X.
        </dd>

        <dt id="optimistic-concurrency">optimistic concurrency</dt>
        <dd>
          Any scheme in which different processes are allowed to make changes that may prove incompatible, so long as they <a href="#resolve">resolve</a> them later. See also: <a href="#pessimistic-concurrency">pessimistic concurrency</a>.
        </dd>

        <dt id="oracle">oracle</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="outer-loop">outer loop</dt>
        <dd class="fixme">FIXME</dd>

      </dl>

    </section>

    <section id="P">

      <h2>P</h2>

      <dl class="gloss">

        <dt id="pair-programming">pair programming</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="parameter">parameter</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="parent-directory">parent directory</dt>
        <dd>
          The directory "above" a particular directory; equivalently, the directory that "contains" the one in question.  Every directory in a file system except the <a href="#root-directory">root</a> must a unique parent.  A directory's parent is usually referred to using the shorthand notation <code>..</code> (pronounced "dot dot").
        </dd>

        <dt id="path">path</dt>
        <dd>
          A non-empty string specifying a single file or directory. Paths consist of zero or more directory names, optionally followed by a filename.  Directory and file names are separated by "/" (on Unix) or "\" (on Microsoft Windows).  If the path begins with this character, it is an <a href="#absolute-path">absolute path</a>; otherwise, it is a <a href="#relative-path">relative path</a>. On Microsoft Windows, a path may optionally begin with a <a href="#drive-letter">drive letter</a>.
        </dd>

        <dt id="path-coverage">path coverage</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="peer-instruction">peer instruction</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="peer-to-peer-architecture">peer-to-peer architecture</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="pessimistic-concurrency">pessimistic concurrency</dt>
        <dd>
          Any scheme which prevents different processes from ever making conflicting changes to a shared resource. See also: <a href="#optimistic-concurrency">optimistic concurrency</a>.
        </dd>

        <dt id="pipe">pipe</dt>
        <dd>
          A connection from the output of one program to the input of another.  When two or more programs are connected in this way, they are called a "pipeline".
        </dd>

        <dt id="pipe-and-filter">pipe and filter</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="pipeline">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="plaintext">plaintext</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="port">port</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="post-mortem-debugging">post mortem debugging</dt>
        <dd>
          The act of debugging a program after it has terminated, typically by inspecting a <a href="#core-dump">core dump</a>.
        </dd>

        <dt id="postcondition">postcondition</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="precondition">precondition</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="prepared-statement">prepared statement</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="primary-key">primary key</dt>
        <dd>
          One or more <a href="#field-database">fields</a> in a <a href="#database-table">database table</a> whose values are guaranteed to be unique for each <a href="#record-database">record</a>, i.e., whose values uniquely identify the entry.
        </dd>

        <dt id="priority-queue">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="private-key">private key</dt>
        <dd>
          One of the two <a href="#key">keys</a> used in an <a href="#asymmetric-cipher">asymmetric cipher</a>.  The private key is kept secret, while the <a href="#public-key">public key</a> is shared with anyone the key's owner wishes to communicate with.
        </dd>

        <dt id="process">process</dt>
        <dd>
          A running instance of a program, containing code, variable values, open files and network connections, and so on.  Processes are the "actors" that the <a href="#operating-system">operating system</a> manages; typically, the OS runs each process for a few milliseconds at a time to give the impression that they are executing simultaneously.
        </dd>

        <dt id="profiler">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="prompt">prompt</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="property-subversion">property (Subversion)</dt>
        <dd>
          definition
        </dd>

        <dt id="protocol">protocol</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="provenance">provenance</dt>
        <dd>
          in art, the history of the ownership and location of an object; in computing, the record of how a particular data value was created.  Computational provenance is intended to provide an audit trail allowing every result to be traced back to the program or programs that produced it, the settings or parameters used by those programs, the raw input values that were processed, etc.
        </dd>

        <dt id="public-key">public key</dt>
        <dd>
          One of the two <a href="#key">keys</a> used in an <a href="#asymmetric-cipher">asymmetric cipher</a>.  The public key is shared with anyone the key's owner wishes to communicate with, while the <a href="#private-key">private key</a> is kept secret.
        </dd>

        <dt id="public-key-cryptography">public key cryptography</dt>
        <dd>
          A cryptographic system based on an <a href="#asymmetric-cipher">asymmetric cipher</a>, in which the keys used for <a href="#encryption">encryption</a> and <a href="#decryption">decryption</a> are different, and one cannot be guessed or calculated from the other. See also: <a href="#private-key">private key</a>, <a href="#public-key">public key</a>.
        </dd>

      </dl>

    </section>

    <section id="Q">

      <h2>Q</h2>

      <dl class="gloss">

        <dt id="query">query</dt>
        <dd>
          A database operation that reads values, but does not modify anything.  Queries are expressed in a special-purpose language called <a href="#sql">SQL</a>.
        </dd>

      </dl>

    </section>

    <section id="R">

      <h2>R</h2>

      <dl class="gloss">

        <dt id="race-condition">race condition</dt>
        <dd>
          A situation in which the final state of a system depends on the order in which two or more competing processes modifies the state last.  For example, if two people make changes to a shared file, the final contents of the file depends on who saves their changes last.  Race conditions are usually bugs, and are notoriously hard to track down.
        </dd>

        <dt id="raise-exception">raise exception</dt>
        <dd>
          To signal an error by creating an <a href="#exception">exception</a>, and triggering the process by which the program searches for a matching <a href="#exception-handler">handler</a>. See also: <a href="#catch-exception">catch exception</a>.
        </dd>

        <dt id="record-database">record (in database)</dt>
        <dd>
          A set of related values making up a single entry in a <a href="#database-table">database table</a>, typically shown as a row. See also: <a href="#field-database">field (database)</a>.
        </dd>

        <dt id="redirection">redirection</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="refactor">refactor</dt>
        <dd>
          To rewrite or reorganize software in order to improve its structure or readability.
        </dd>

        <dt id="referential-integrity">referential integrity</dt>
        <dd>
          The internal consistency of values in a database.  If an entry in one table contains a <a href="#foreign-key">foreign key</a>, but the <a href="#record-database">record</a> that key is supposed to identify doesn't exist, referential integrity has been violated.
        </dd>

        <dt id="regular-expression">regular expression (RE)</dt>
        <dd>
          A pattern that specifies a set of character strings.  In programs, regular expressions are most often used to find sequences of characters in strings.
        </dd>

        <dt id="relational-database">relational database</dt>
        <dd>
          A collection of data organized into <a href="#database-table">tables</a>.
        </dd>

        <dt id="relative-path">relative path</dt>
        <dd>
          A <a href="#path">path</a> that specifies the location of a file or directory with respect to the <a href="#current-working-directory">current working directory</a>.  Any <a href="#path">path</a> that does <em>not</em> begin with a separator character ("/" or "\") is a relative path. See also: <a href="#absolute-path">absolute path</a>.
        </dd>

        <dt id="release-lock">release a lock</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="remote-login">remote login</dt>
        <dd>
          definition
        </dd>

        <dt id="repository">repository</dt>
        <dd>
          A central storage area where a <a href="#version-control-system">version control system</a> stores old <a href="#revision">revisions</a> of files, along with information about who created them and when.
        </dd>

        <dt id="resolve">resolve</dt>
        <dd>
          To eliminate the <a href="#conflict">conflicts</a> between two or more incompatible changes to a file or set of files being managed by a <a href="#version-control-system">version control system</a>.
        </dd>

        <dt id="response-time">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="reverse-merge">reverse merge</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="revert">revert</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="revision">revision</dt>
        <dd>
          A particular state of a file, or a set of files, being managed by a <a href="#version-control-system">version control system</a>.
        </dd>

        <dt id="revision-number">revision number</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="root-directory">root directory</dt>
        <dd>
          The top-most directory in a <a href="#file-system">file system</a>'s <a href="#directory-tree">directory tree</a>.  Its name is the <a href="#operating-system">operating system</a>'s separator character, i.e., "/" on Unix (including Linux and Mac OS X), and "\" on Microsoft Windows.
        </dd>

        <dt id="root-element">root element</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="row-major-order">row major order</dt>
        <dd>
          Storing matrix values by row, and then by column.  See also: <a href="#column-major-order">column major order</a>.
        </dd>

      </dl>

    </section>

    <section id="S">

      <h2>S</h2>

      <dl class="gloss">

        <dt id="scope">scope</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="screen-scraping">screen scraping</dt>
        <dd>
          Using a program to extract information from an HTML page intended for human viewing.  Screen scraping is a quick way to solve simple problems, but breaks down when the pages are complex, or their format changes frequently. See also: <a href="#web-services">web services</a>, <a href="#web-spider">web spider</a>.
        </dd>

        <dt id="secure-shell">secure shell (SSH)</dt>
        <dd>
          definition
        </dd>

        <dt id="self-join">self-join</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="sequence">sequence</dt>
        <dd>
          A set of objects arranged in a dense, linear fashion, so that they may be referred to by their index.  In Python, strings, lists, and tuples are built-in sequence types, since the elements of each may be referred to as <code>s[0]</code>, <code>s[1]</code>, and so on up to <code>s[N-1]</code>, where <code>N</code> is the sequence's length.
        </dd>

        <dt id="serial-fraction">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="serialization">serialization</dt>
        <dd>
          The act of forcing operations to execute one at a time, instead of <a href="#concurrency">concurrently</a>.
        </dd>

        <dt id="server">server</dt>
        <dd>
          A software application that provides data to other programs.  The consumer is called a <a href="#client">client</a>. See also: <a href="#web-server">web server</a>.
        </dd>

        <dt id="set">set</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="sgml">SGML</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="shell">shell</dt>
        <dd>
          A command-line user interface program, such as Bash (the Bourne-Again Shell) or the Microsoft Windows DOS shell.  Shells commonly execute a read-evaluate-print cycle: when the user enters a command in response to a <a href="#prompt">prompt</a>, the shell either executes the command itself, or runs the program that the command has specified.  In either case, output is sent to the shell window, and the user is prompted to enter another command.  Most shells include commands for looping, conditionals, and defining functions, so that small (and sometimes large) programs can be written by putting a sequence of shell commands in a file.
        </dd>

        <dt id="shell-script">shell script</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="short-circuit-evaluation">short-circuit evaluation</dt>
        <dd>
          Evaluation of an expression from left to right that stops as soon as the expression's final value is known.  For example, if <code>x</code> is false, the computer does not call the function <code>f</code> in the expression <code>x and f(x)</code>.  Similarly, if <code>x</code> is true, <code>f</code> does not have to be called in <code>x or f(x)</code>.
        </dd>

        <dt id="side-effect">side effect</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="single-step">single-step</dt>
        <dd>
          To advance a program by one instruction, or one line, while debugging. See also: <a href="#step-into">step into</a>, <a href="#step-over">step over</a>.
        </dd>

        <dt id="socket">socket</dt>
        <dd>
          One end of an <a href="#internet-protocol">IP</a> communication channel.
        </dd>

        <dt id="sparse">sparse</dt>
        <dd>
          Being mostly empty.  A sparse vector or matrix is one in which most values are zero.
        </dd>

        <dt id="sql">SQL</dt>
        <dd>
          A special-purpose language for describing operations on <a href="#relational-database">relational databases</a>.  SQL is <em>not</em> actually an acronym for "Structured Query Language".
        </dd>

        <dt id="sql-injection">SQL injection</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="stack-frame">stack frame</dt>
        <dd>
          A data structure that provides storage for a function's local variables.  Each time a function is called, a new stack frame is created and put on the top of the <a href="#call-stack">call stack</a>.  When the function returns, the stack frame is discarded.
        </dd>

        <dt id="standard-error">standard error</dt>
        <dd>
          A process's "other" default output stream, typically used for error messages. See also: <a href="#standard-output">standard output</a>.
        </dd>

        <dt id="standard-input">standard input</dt>
        <dd>
          A process's default input stream.  In interactive command-line applications, it is typically connected to the keyboard; in a <a href="#pipe">pipeline</a>, it receives data from the <a href="#standard-output">standard output</a> of the preceding process.
        </dd>

        <dt id="standard-output">standard output</dt>
        <dd>
          A process's default output stream.  In interactive command-line applications, data sent to standard output is displayed on the screen; in a <a href="#pipe">pipeline</a>, it is passed to the <a href="#standard-input">standard input</a> of the next process.
        </dd>

        <dt id="stateless-protocol">stateless protocol</dt>
        <dd>
          A communication protocol in which each basic operation is independent of each other. <a href="#http">HTTP</a> is the best-known example: <a href="#server">servers</a> do not remember anything about <a href="#client">clients</a> between requests.
        </dd>

        <dt id="statement">statement</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="static-space">static space</dt>
        <dd>
          A portion of a program's memory reserved for storing values that are allocated even before the program starts to run, such as constant strings. See also: <a href="#call-stack">call stack</a>, <a href="#heap">heap</a>.
        </dd>

        <dt id="statistical-profiler">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="stdin">stdin</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="stdout">stdout</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="step-into">step into</dt>
        <dd>
          To go into a function call when debugging. See also: <a href="#single-step">single-step</a>, <a href="#step-over">step over</a>.
        </dd>

        <dt id="step-over">step over</dt>
        <dd>
          To execute a function without going into it when debugging. See also: <a href="#single-step">single-step</a>, <a href="#step-into">step into</a>.
        </dd>

        <dt id="stereotype-threat">stereotype-threat</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="string">string</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="strong-scalability">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="subquery">subquery</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="symmetric-cipher">symmetric cipher</dt>
        <dd>
          A <a href="#cipher">cipher</a> in which a single key is used for both <a href="#encryption">encryption</a> and <a href="#decryption">decryption</a>.  Symmetric ciphers are less secure than <a href="#asymmetric-cipher">asymmetric</a> ones, but are typically much faster.
        </dd>

      </dl>

    </section>

    <section id="T">

      <h2>T</h2>

      <dl class="gloss">

        <dt id="table">table</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="tag-xml">tag (in XML)</dt>
        <dd>
          A textual representation of an <a href="#xml">XML</a> <a href="#element">element</a>.  Tags come in matched opening and closing pairs, such as <code>&lt;x&gt;</code> and <code>&lt;/x&gt;</code>; if the element the tag pair represents does not contain text or other elements, the short form <code>&lt;x/&gt;</code> may be used. See also: <a href="#branch">branch</a>.
        </dd>

        <dt id="target-program">target program</dt>
        <dd>
          The program being controlled by a <a href="#debugger">debugger</a>; also called the <a href="#debuggee">debuggee</a>.
        </dd>

        <dt id="task-farm">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="tcp">Transmission Control Protocol (TCP)</dt>
        <dd>
          A communication protocol in the <a href="#internet-protocol">IP</a> family that provides reliable in-order delivery of data.  Programs communicating via TCP can read and write as they would with files (at least, until something goes wrong). See also: <a href="#socket">socket</a>, <a href="#udp">User Datagram Protocol (UDP)</a>.
        </dd>

        <dt id="test-action">test action</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="test-report">test report</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="test-result">test result</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="text">text</dt>
        <dd>
          The non-<a href="#element">element</a> content of an <a href="#xml">XML</a> <a href="#document">document</a>; in an HTML page, the text is what is displayed, while the <a href="#tag-xml">tags</a> control its formatting.
        </dd>

        <dt id="throughput">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="transaction">transaction</dt>
        <dd>
          A set of operations which take effect in a reliable, consistent manner.  If a transaction cannot be completed (e.g., because of a system failure), it is guaranteed to have no effect.
        </dd>

        <dt id="tree">tree</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="tuple">tuple</dt>
        <dd>
          An immutable <a href="#sequence">sequence</a>.
        </dd>

        <dt id="type">type</dt>
        <dd class="fixme">FIXME</dd>

      </dl>

    </section>

    <section id="U">

      <h2>U</h2>

      <dl class="gloss">

        <dt id="unicode">Unicode</dt>
        <dd>
          An international standard for representing characters and other symbols.  Each symbol is assigned a unique number; those numbers are then encoded in any of several standard ways (such as <a href="#utf-8">UTF-8</a>).
        </dd>

        <dt id="unit-test">unit test</dt>
        <dd>
          A test that exercises a single basic element of a program, such as a particular function or method. See also: <a href="#integration-test">integration test</a>.
        </dd>

        <dt id="update">update</dt>
        <dd>
          To update a <a href="#working-copy">working copy</a> with the most recent changes in a <a href="#version-control-system">version control system</a> <a href="#repository">repository</a>. See also: <a href="#commit">commit</a>.
        </dd>

        <dt id="url-encoding">URL encoding</dt>
        <dd>
          A translation standard that replaces characters that are meaningful in URLs (such as <code>&amp;</code> and <code>?</code>) with their hexadecimal encodings.
        </dd>

        <dt id="user-group">user group</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="user-group-id">user group ID</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="user-group-name">user group name</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="user-id">user ID</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="user-name">username</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="utf-8">UTF-8</dt>
        <dd>
          A standard for encoding character data; the acronym is short for "<a href="#unicode">Unicode</a> Transformation Format, 8-bit encoding form".
        </dd>

      </dl>

    </section>

    <section id="V">

      <h2>V</h2>

      <dl class="gloss">

        <dt id="variable">variable</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="variable-scope">variable scope</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="version-control-system">version control system</dt>
        <dd>
          A tool for managing changes to a set of files.  Each set of changes creates a new <a href="#revision">revision</a> of the files; the version control system allows users to recover old <a href="#revision">revisions</a> reliably, and helps manage conflicting changes made by different users.
        </dd>

        <dt id="view">view</dt>
        <dd class="fixme">FIXME</dd>

      </dl>

    </section>

    <section id="W">

      <h2>W</h2>

      <dl class="gloss">

        <dt id="weak-scalability">FIXME</dt>
        <dd>
          definition
        </dd>

        <dt id="web-server">web server</dt>
        <dd>
          A <a href="#server">server</a> that handles <a href="#http">HTTP</a> requests.
        </dd>

        <dt id="web-services">web services</dt>
        <dd>
          A software application that exchanges data with others by sending <a href="#xml">XML</a> data via the <a href="#http">HTTP</a> protocol.  Most modern web services encode data using the <a href="#soap">SOAP</a> standard. See also: <a href="#screen-scraping">screen scraping</a>.
        </dd>

        <dt id="while-loop">while loop</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="whitespace">whitespace</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="wildcard">wildcard</dt>
        <dd>
          A character used in pattern matching.  In the Unix shell, the wildcard "*" matches zero or more characters, so that <code>*.txt</code> matches all files whose names end in <code>.txt</code>.
        </dd>

        <dt id="working-copy">working copy</dt>
        <dd>
          A personal copy of the files being managed by a <a href="#version-control-system">version control system</a>. Changes the user makes to the working copy do not affect other users until they are <a href="#commit">committed</a> to the <a href="#repository">repository</a>.
        </dd>

        <dt id="wrapper-function">wrapper function</dt>
        <dd class="fixme">FIXME</dd>

        <dt id="wysiwyg">WYSIWYG</dt>
        <dd class="fixme">FIXME</dd>

      </dl>

    </section>

    <section id="X">

      <h2>X</h2>

      <dl class="gloss">

        <dt id="xml">XML</dt>
        <dd>
          The Extensible Markup Language; a standard for defining application-specific markup languages. See also: <a href="#attribute">attribute</a>, <a href="#document">document</a>, <a href="#document-object-model">Document Object Model (DOM)</a>, <a href="#element">element</a>.
        </dd>

        <dt id="xpath">XPath</dt>
        <dd class="fixme">FIXME</dd>

      </dl>

    </section>

    <section id="Y">

      <h2>Y</h2>

    </section>

    <section id="Z">

      <h2>Z</h2>

    </section>