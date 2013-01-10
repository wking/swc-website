Title: Databases
Directory: book

<span class="comment"> AB: In the text the section are numbered, I would number them here as well. </span>
<span class="comment"> AB: It might be nice to have the commands explained in a section either in the section title or listed right under it in the text. </span>
    <ol class="toc">
      <li><a href="#s:select">Selecting</a></li>
      <li><a href="#s:distinct">Removing Duplicates</a></li>
      <li><a href="#s:calc">Calculating New Values</a></li>
      <li><a href="#s:filter">Filtering</a></li>
      <li><a href="#s:sort">Sorting</a></li>
      <li><a href="#s:aggregate">Aggregation</a></li>
      <li><a href="#s:design">Database Design</a></li>
      <li><a href="#s:join">Combining Data</a></li>
      <li><a href="#s:selfjoin">Self Join</a></li>
      <li><a href="#s:null">Missing Data</a></li>
      <li><a href="#s:nested">Nested Queries</a></li>
      <li><a href="#s:create">Creating and Modifying Tables</a></li>
      <li><a href="#s:transactions">Transactions</a></li>
      <li><a href="#s:programming">Programming With Databases</a></li>
      <li><a href="#s:provenance">Provenance Once More</a></li>
      <li><a href="#s:summary">Summing Up</a></li>
    </ol>

    <blockquote>
      We're here to do research,
      they pay us to teach,
      we spend our time on administration.
      <br/>
      &mdash; Eleni Stroulia
    </blockquote>
<span class="comment"> AB: I'd like to see some kind of motivation other than administration. </span>
<span class="comment"> AB: Databases are used to store information about HST data which I would not call administrative. </span>
<span class="comment"> AB: It's more about organzing large quantities of data in an easily searchable way. Maybe there is another word. </span>
    <p>
      As many scientists have found out the hard way,
      the real challenges in research have nothing to do with quantum mechanics,
      protein folding,
      or the rate at which vulgar toads reproduce in the absence of natural predators.
      No,
      the real challenges are all about accounting and administration.
      In this chapter,
      we'll see how to use a database to keep track of
      what our graduate students have worked on.
      The techniques we'll explore apply directly to other kinds of databases as well,
      and as we'll see,
      knowing how to get information <em>out</em> of a database is essential to
      figuring out how to put data <em>in</em>.
    </p>

    <section id="s:select">

      <h2>Selecting</h2>

      <div class="understand" id="u:select">
        <h3>Understand:</h3>
        <ul>
          <li>That relational databases store data in tables with fields and records.</li>
          <li>How to select fields from a table.</li>
        </ul>
      </div>

      <p>
        A <a href="glossary.html#relational-database">relational database</a>
        is a way to store and manipulate information
        that is arranged as <a href="glossary.html#table">tables</a>.
        Each table has columns (also known as <a href="glossary.html#field-database">fields</a>) which describe the data,
        and rows (also known as <a href="glossary.html#record-database">records</a>) which contain the data.
      </p>

      <p id="a:dbms">
        When we are using a spreadsheet,
        we put formulas into cells to calculate new values based on old ones.
        When we are using a database,
        we send commands
        (usually called <a href="glossary.html#query">queries</a>)
        to a <a href="glossary.html#database-manager">database manager</a>:
        a program that manipulates the database for us.
        The database manager does whatever lookups and calculations the query specifies,
        returning the results in a tabular form
        that we can then use as a starting point for further queries.
      </p>

      <p>
        Queries are written in a language called <a href="glossary.html#sql">SQL</a>,
        which stands for "Structured Query Language".
        SQL provides hundreds of different ways to analyze and recombine data;
        we will only look at a handful,
        but that handful accounts for most of what scientists do.
      </p>

      <p>
        Here's a simple database that records how many hours scientists have spent
        on various projects in a research lab.
        It consists of a single table called <code>Experiments</code>
        with three fields&mdash;scientists, experiment, and hours&mdash;and eight records.
        Each record stores a scientist's hours on one project.
      </p>

      <table class="outlined" src="db/create_single_table_experiments.sql">
        <tr><td colspan="3" align="center"><strong>Experiments</strong></td></tr>
        <tr>
          <td><strong>Scientist</strong></td>
          <td><strong>Project</strong></td>
          <td><strong>Hours</strong></td>
        </tr>
        <tr>
          <td>Sofia Kovalevskaya</td>
          <td>Antigravity</td>
          <td>6.5</td>
        </tr>
        <tr>
          <td>Sofia Kovalevskaya</td>
          <td>Teleportation</td>
          <td>11.0</td>
        </tr>
        <tr>
          <td>Sofia Kovalevskaya</td>
          <td>Teleportation</td>
          <td>5.0</td>
        </tr>
        <tr>
          <td>Mikhail Lomonosov</td>
          <td>Antigravity</td>
          <td>4.0</td>
        </tr>
        <tr>
          <td>Mikhail Lomonosov</td>
          <td>Time Travel</td>
          <td>-2.0</td>
        </tr>
        <tr>
          <td>Dmitri Mendeleev</td>
          <td>Antigravity</td>
          <td>9.0</td>
        </tr>
        <tr>
          <td>Ivan Pavlov</td>
          <td>Teleportation</td>
          <td>9.0</td>
        </tr>
        <tr>
          <td>Ivan Pavlov</td>
          <td>Time Travel</td>
          <td>-7.0</td>
        </tr>
      </table>

      <p class="continue">
        Notice that there are two entries for Sofia Kovalevskaya's work on
        the Teleportation project.
        This could mean that she worked on it at two different times,
        or it could be a data entry error.
        We'll come back to this question <a href="#a:keys">later</a>.
      </p>

      <p>
        For now,
        let's write an SQL query that gets people's names and hours.
        We do this using the SQL command <code>SELECT</code>,
        giving it the names of the columns we want to read and the table to read them from.
        (We have to provide the table name because most databases contain more than one table.)
        Our query looks like this:
      </p>
<span class="comment"> AB: I would indent the command line text </span>
<pre src="src/db/select_scientist_hours.sql">
SELECT Scientist, Hours FROM Experiments;
</pre>

      <p>
        We have capitalized the words <code>SELECT</code> and <code>FROM</code> because they are SQL keywords.
        SQL is actually case insensitive&mdash;we could write <code>select</code>
        or <code>sElEcT</code>&mdash;but
        we will stick to upper case so that it is clear what is a keyword and what is not.
        The semi-colon at the end tells the database manager that the command is complete.
        <span class="comment"> AB: You can still write commands without the semi-colon. However, after you hit enter, you will have to type </span>
        <span class="comment"> AB: go to tell the database manager that the command is complete. </span>
        When it runs,
        it shows us the two columns of the <code>Experiments</code> table that we asked for:
      </p>
<span class="comment"> AB: Put in a little more cell padding in all of your tables. </span>
      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>6.5</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>11.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>5.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>4.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>-2.0</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>-7.0</td></tr>
      </table>

      <p class="continue">
        Exactly <em>how</em> the database displays the query's results
        depends on what kind of interface we are using.
        If we are running <code>sqlite</code> from the shell,
        its default output looks like this:
      </p>

<pre>
<span class="out">Sofia Kovalevskaya|6.5
Sofia Kovalevskaya|11.0
Sofia Kovalevskaya|5.0
Mikhail Lomonosov|4.0
Mikhail Lomonosov|-2.0
Dmitri Mendeleev|9.0
Ivan Pavlov|9.0
Ivan Pavlov|-7.0</span>
</pre>

      <p class="continue">
        If we are using a graphical interface,
        such as the <a href="https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/">SQLite Manager</a>
        plugin for Firefox,
        our output will be displayed more readably
        (<a href="#f:firefox_plugin">Figure XXX</a>).
        We'll use a simple table-based display for now.
      </p>

      <figure id="f:firefox_plugin">
        <img src="img/db/firefox_plugin.png" alt="SQLite Manager Plugin for Firefox" />
      </figure>

      <p>
        If we want the project name to our output,
        we can just add that to the list of fields:
      </p>

<pre src="src/db/select_scientist_hours_project.sql">
SELECT Scientist, Hours, Project FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>6.5</td><td>Antigravity</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>11.0</td><td>Teleportation</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>5.0</td><td>Teleportation</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>4.0</td><td>Antigravity</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>-2.0</td><td>Time Travel</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>9.0</td><td>Antigravity</td></tr>
        <tr><td>Ivan Pavlov</td><td>9.0</td><td>Teleportation</td></tr>
        <tr><td>Ivan Pavlov</td><td>-7.0</td><td>Time Travel</td></tr>
      </table>

      <p>
        It's important to understand that
        the rows and columns in a database table aren't actually stored in any particular order.
        They will always be <em>displayed</em> in some order,
        but we can control that in various ways.
        For example,
        we could rearrange the columns in the output by writing our query as:
      </p>

<pre src="src/db/select_project_scientist_hours.sql">
SELECT Project, Scientist, Hours FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>Antigravity</td><td>Sofia Kovalevskaya</td><td>6.5</td></tr>
        <tr><td>Teleportation</td><td>Sofia Kovalevskaya</td><td>11.0</td></tr>
        <tr><td>Teleportation</td><td>Sofia Kovalevskaya</td><td>5.0</td></tr>
        <tr><td>Antigravity</td><td>Mikhail Lomonosov</td><td>4.0</td></tr>
        <tr><td>Time Travel</td><td>Mikhail Lomonosov</td><td>-2.0</td></tr>
        <tr><td>Antigravity</td><td>Dmitri Mendeleev</td><td>9.0</td></tr>
        <tr><td>Teleportation</td><td>Ivan Pavlov</td><td>9.0</td></tr>
        <tr><td>Time Travel</td><td>Ivan Pavlov</td><td>-7.0</td></tr>
      </table>

      <p class="continue">
        or even repeat columns:
      </p>

<pre make="select_project_project">
SELECT Project, Project FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>Antigravity</td><td>Antigravity</td></tr>
        <tr><td>Teleportation</td><td>Teleportation</td></tr>
        <tr><td>Teleportation</td><td>Teleportation</td></tr>
        <tr><td>Antigravity</td><td>Antigravity</td></tr>
        <tr><td>Time Travel</td><td>Time Travel</td></tr>
        <tr><td>Antigravity</td><td>Antigravity</td></tr>
        <tr><td>Teleportation</td><td>Teleportation</td></tr>
        <tr><td>Time Travel</td><td>Time Travel</td></tr>
      </table>

      <p class="continue">
        We will see ways to rearrange the rows <a href="#s:sort">later</a>.
      </p>

      <p>
        As a shortcut, we can select all of the columns in a table
        using the wildcard <code>*</code>.
        For example:
      </p>

<pre src="src/db/select_star">
SELECT * FROM Experiments;
</pre>

      <p class="continue">
        selects all of the data in the <code>Experiments</code> table:
      </p>

      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <div class="keypoints" id="k:select">
        <h3>Summary</h3>
        <ul>
          <li idea="modelview">A relational database stores information in tables with fields and records.</li>
          <li>A database manager is a program that manipulates a database.</li>
          <li>The commands or queries given to a database manager are usually written in a specialized language called SQL.</li>
          <li>SQL is case insensitive.</li>
          <li>The rows and columns of a database table aren't stored in any particular order.</li>
          <li>Use <code>SELECT <em>fields</em> FROM <em>table</em></code> to get all the values for specific fields from a single table.</li>
          <li>Use <code>SELECT * FROM <em>table</em></code> to select everything from a table.</li>
        </ul>
      </div>

    </section>

    <section id="s:distinct">

      <h2>Removing Duplicates</h2>

      <div class="understand" id="u:distinct">
        <h3>Understand:</h3>
        <ul>
          <li>How to eliminate duplicate results from queries.</li>
        </ul>
      </div>

      <p>
        Queries often return redundant information.
        For example:
      </p>

<pre src="src/db/select_project.sql">
SELECT Project FROM Experiments;
</pre>

      <p class="continue">
        displays some project names multiple times (once for each occurrence):
      </p>

      <table class="outlined">
        <tr><td>Antigravity</td></tr>
        <tr><td>Teleportation</td></tr>
        <tr><td>Teleportation</td></tr>
        <tr><td>Antigravity</td></tr>
        <tr><td>Time Travel</td></tr>
        <tr><td>Antigravity</td></tr>
        <tr><td>Teleportation</td></tr>
        <tr><td>Time Travel</td></tr>
      </table>

      <p class="continue">
        We can eliminate the redundant copies by adding the <code>DISTINCT</code> keyword
        to our query:
      </p>

<pre src="src/db/select_distinct_project.sql">
SELECT DISTINCT Project FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>Antigravity</td></tr>
        <tr><td>Teleportation</td></tr>
        <tr><td>Time Travel</td></tr>
      </table>

      <p>
        If we select more than one column&mdash;for example,
        both the project name and the hours&mdash;then
        the distinct pairs of values are returned.
        For example,
        the query below only displays Sofia Kovalevskaya and the Teleportation project once,
        even though there are two entries in the database for
        the hours she spent on it:
      </p>

<pre src="src/db/select_distinct_project_hours.sql">
SELECT DISTINCT Project, Scientist FROM Experiment;
</pre>

      <table class="outlined">
        <tr><td>Antigravity</td><td>Dmitri Mendeleev</td></tr>
        <tr><td>Antigravity</td><td>Mikhail Lomonosov</td></tr>
        <tr><td>Antigravity</td><td>Sofia Kovalevskaya</td></tr>
        <tr><td>Teleportation</td><td>Ivan Pavlov</td></tr>
        <tr><td>Teleportation</td><td>Sofia Kovalevskaya</td></tr>
        <tr><td>Time Travel</td><td>Ivan Pavlov</td></tr>
        <tr><td>Time Travel</td><td>Mikhail Lomonosov</td></tr>
      </table>

      <p>
        Notice in both cases that duplicates are removed
        even if they didn't appear to be adjacent in the database.
        Once again,
        it's important to remember that rows aren't actually ordered:
        they're just displayed that way.
      </p>

      <div class="keypoints" id="k:distinct">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>SELECT DISTINCT</code> to eliminate duplicates from a query's output.</li>
        </ul>
      </div>

    </section>

    <section id="s:calc">

      <h2>Calculating New Values</h2>

      <div class="understand" id="u:calc">
        <h3>Understand:</h3>
        <ul>
          <li>How to calculate new values based on the results of queries.</li>
        </ul>
      </div>

      <p>
        Suppose that 10% of the time spent on each experiment was prep work
        that needs to be accounted for separately.
        We can add an expression to our <code>SELECT</code> statement
        to do the required computation for each row like this:
      </p>

<pre src="src/db/select_simple_formula.sql">
SELECT *, 0.1 * Hours FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>Antigravity</td><td>6.5</td><td>0.65</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>11.0</td><td>1.1</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>5.0</td><td>0.5</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td><td>0.4</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Time Travel</td><td>-2.0</td><td>-0.2</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>Antigravity</td><td>9.0</td><td>0.9</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td><td>0.9</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td><td>-0.7</td></tr>
      </table>

      <p>
        When we run the query, the expression <code>0.1 * Hours</code> is evaluated for each row
        and appended to that row.
        Expressions can use any of the fields,
        all of usual arithmetic operators,
        and a variety of built-in functions
        (the most commonly used of which are summarized in <a href="ref.html#s:db">the appendix</a>).
        For example,
        we could round values to a single decimal place using the <code>ROUND</code> function,
        and pair that value with the scientist's name:
      </p>

<pre src="src/db/select_scientist_formula.sql">
SELECT Scientist, ROUND(0.1 * Hours, 1) FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>0.7</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>1.1</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>0.5</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>0.4</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>-0.2</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>0.9</td></tr>
        <tr><td>Ivan Pavlov</td><td>0.9</td></tr>
        <tr><td>Ivan Pavlov</td><td>-0.7</td></tr>
      </table>

      <div class="keypoints" id="k:calc">
        <h3>Summary</h3>
        <ul>
          <li>Use expressions in place of field names to calculate per-record values.</li>
        </ul>
      </div>

    </section>

    <section id="s:filter">

      <h2>Filtering</h2>

      <div class="understand" id="u:filter">
        <h3>Understand:</h3>
        <ul>
          <li>How to select records based on their values.</li>
          <li>How to combine tests on records.</li>
          <li>How to build up complex queries in steps.</li>
        </ul>
      </div>

      <p>
        One of the most powerful features of a database is
        the ability to <a href="glossary.html#filter">filter</a> data,
        i.e.,
        to select only those records that match certain criteria.
        For example,
        suppose we want to see all of the experiments that took more than two hours to complete.
        We can select these by adding a <code>WHERE</code> clause to our query:
      </p>

<pre src="src/db/select_where_hours.sql">
SELECT * FROM Experiments WHERE Hours &gt; 2.0;
</pre>

      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
      </table>

      <p>
        We can understand how this query works by imagining that the database executes it in two stages
        (<a href="#f:pipeline_where">Figure XXX</a>).
        First, the database looks at each row in the <code>Experiments</code> table
        to see which ones satisfy the <code>WHERE</code> condition.
        It then uses the column names immediately following the <code>SELECT</code> keyword
        to determine what columns to keep
        (or, if there are expressions, what new values to calculate).
      </p>

      <figure id="f:pipeline_where">
        <img src="img/db/pipeline_where.png" alt="Two-Stage Query Processing Pipeline" />
      </figure>

      <p>
        We can use many other operators to filter our data.
        For example, we could ask for all of the experiments that were done by Ivan Pavlov:
      </p>

<pre src="src/db/select_where_pavlov.sql">
SELECT * FROM Experiment WHERE Scientist = "Ivan Pavlov";
</pre>

      <table class="outlined">
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <p>
        We can also make our <code>WHERE</code> conditions more sophisticated
        by combining tests with <code>AND</code> and <code>OR</code>.
        For example, suppose we want to know which project Mikhail Lomonosov
        spent more than three hours working on.
        We're only interested in rows that satisfy <em>both</em> criteria,
        so we combine the two tests with <code>AND</code>:
      </p>

<pre src="src/db/select_where_lomonosov_three_hours.sql">
SELECT * FROM Experiments WHERE (Hours &gt; 3) AND (Scientist = "Mikhail Lomonosov");
</pre>

      <table class="outlined">
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
      </table>

      <p class="continue">
        (The parentheses around each test aren't strictly required,
        but they help make the query easier to read.)
      </p>

      <p>
        If we wanted experiments that either Ivan or Mikhail had worked on,
        we would combine the tests on their names like this:
      </p>

<pre src="src/db/select_where_lomonosov_or_pavlov.sql">
SELECT * FROM Experiments WHERE (Scientist = "Mikhail Lomonosov") OR (Scientist = "Ivan Pavlov");
</pre>

      <table class="outlined">
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <p>
        And if we wanted project that either scientist had spent more than three hours on,
        we would combine our tests:
      </p>

<pre src="src/db/select_where_lomonosov_or_pavlov_three_hours.sql">
SELECT * FROM Experiments WHERE (Hours > 3) AND ((Scientist = "Mikhail Lomonosov") OR (Scientist = "Ivan Pavlov"));
</pre>

      <table class="outlined">
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
      </table>

      <p>
        The extra parentheses around the checks on the scientists' names
        ensure that the <code>AND</code> and <code>OR</code> are combined the way we want.
        Without them, the computer might decide that we meant:
      </p>

<pre src="src/db/select_where_badly_grouped.sql">
SELECT * FROM Experiments WHERE ((Hours > 3) AND (Scientist = "Mikhail Lomonosov")) OR (Scientist = "Ivan Pavlov");
</pre>

      <p class="continue">
        i.e., that we want projects where Mikhail spent a lot of time,
        or any projects that Ivan worked on, regardless of hours.
        Since this is actually a different query,
        it gives a different (and wrong) answer:
      </p>

      <table class="outlined">
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <p>
        Instead of using <code>OR</code> to match one of several values,
        we can use the <code>IN</code> operator
        along with a list of values we would like to match.
        For example, we could rewrite our query as:
      </p>

<pre src="src/db/select_where_using_in.sql">
SELECT * FROM Experiments WHERE (Hours > 3) AND (Scientist IN ("Mikhail Lomonosov", "Ivan Pavlov"));
</pre>

      <p class="continue">
        This produces the same two rows as the correctly-parenthesized query,
        but is easier to understand,
        particularly as the number of options grows.
      </p>

      <p>
        Knowing how to translate what we want into appropriate <code>WHERE</code> clauses
        When in doubt,
        refer to the earlier discussion of <a href="python.html#s:bool">Boolean logic</a>.
      </p>

      <div class="box">

        <h3>Growing Queries</h3>

        <p>
          What we have just done is how most people "grow" their SQL queries.
          We started with something simple that did part of what we wanted,
          then added more clauses one by one,
          testing their effects as we went.
          This is a good strategy&mdash;in fact,
          for complex queries it's often the <em>only</em> strategy&mdash;but
          it depends on quick turnaround,
          and on us recognizing the right answer when we get it.
        </p>

        <p>
          The best way to achieve quick turnaround is often
          to put a subset of data in a temporary database
          and run our queries against that,
          or to fill a small database with synthesized records.
          For example,
          instead of trying our queries against an actual database of 20 million Australians,
          we could run it against a sample of ten thousand,
          or write a small program to generate ten thousand random (but plausible) records
          and use that.
        </p>

      </div>

      <div class="keypoints" id="k:filter">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>WHERE <em>test</em></code> in a query to filter records based on logical tests.</li>
          <li>Use <code>AND</code> and <code>OR</code> to combine tests in filters.</li>
          <li>Use <code>IN</code> to test whether a value is in a set.</li>
          <li idea="perf">Build up queries a bit at a time, and test them against small data sets.</li>
        </ul>
      </div>

    </section>

    <section id="s:sort">

      <h2>Sorting</h2>

      <div class="understand" id="u:sort">
        <h3>Understand:</h3>
        <ul>
          <li>How to sort the results of queries.</li>
        </ul>
      </div>

      <p>
        As we mentioned earlier,
        database records are not stored in any particular order.
        This means that query results aren't necessarily sorted,
        and even if they are,
        we often want to sort them in a different way,
        e.g., by the name of the project instead of by the name of the scientist.
        We can do this in SQL by adding an <code>ORDER BY</code> clause to our query
        as shown here:
      </p>

<pre src="src/db/select_order_project_asc.sql">
SELECT * FROM Experiments ORDER BY Project ASC;
</pre>

      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <p>
        The keyword <code>ASC</code> at the end is short for "ascending",
        and means "smallest first".
        We can sort in the opposite order using <code>DESC</code> (for "descending") instead:
      </p>

<pre src="src/db/select_order_project_desc.sql">
SELECT * FROM Experiments ORDER BY Project DESC;
</pre>

      <table class="outlined">
        <tr><td>Mikhail Lomonosov</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>Antigravity</td><td>9.0</td></tr>
      </table>

      <p>
        We can also sort on several fields at once.
        For example,
        this query sorts results in ascending order by project name,
        and then sorts the results for each project in descending order by name:
      </p>

<pre src="src/db/select_order_multiple.sql">
SELECT * FROM Experiments ORDER BY Project ASC, Scientist DESC;
</pre>

      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <p>
        We can even sort the results by the value of an expression.
        In SQLite,
        for example,
        the <code>RANDOM</code> function returns a pseudo-random integer:
      </p>

<pre src="src/db/select_random.sql">
SELECT RANDOM() FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>-4333583529515760313</td></tr>
        <tr><td>3661398752594229354</td></tr>
        <tr><td>-1239522849593007459</td></tr>
        <tr><td>5085104577194332809</td></tr>
        <tr><td>7406392079669228295</td></tr>
        <tr><td>8157275644606127629</td></tr>
        <tr><td>4936669514230061450</td></tr>
        <tr><td>3027346145930117288</td></tr>
      </table>

      <p class="continue">
        (Try running the query twice and watch the random values change.)
        So to randomize the order of our query results,
        we can sort them by the value of this function:
      </p>

<pre src="src/db/select_order_random.sql">
SELECT * FROM Experiments ORDER BY RANDOM();
</pre>

      <table class="outlined">
        <tr><td>Mikhail Lomonosov</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Antigravity</td><td>6.5</td></tr>
      </table>

      <p>
        We don't actually have to display a column in order to sort by it.
        For example, the query below sorts by the project name,
        but only displays the scientist's name and hours.
        (It is also split across several lines to make it easier to read,
        which is a good practice for complicated queries).
      </p>

<pre src="src/db/select_order_project_display_scientist_hours.sql">
SELECT   Scientist, Hours
FROM     Experiments
ORDER BY Project;
</pre>

      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>6.5</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>4.0</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>9.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>11.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>5.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>9.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>-2.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>-7.0</td></tr>
      </table>

      <p>
        We can sort on fields that aren't displayed because
        sorting happens earlier in the processing pipeline than field selection
        (<a href="#f:pipeline_sort">Figure XXX</a>).
        Once we include sorting,
        our pipeline:
      </p>

      <ul>

        <li>
          filters rows according to the <code>WHERE</code> clause (if any);
        </li>

        <li>
          sorts the results according to the <code>ORDER BY</code> clause (if there is one);
          and
        </li>

        <li>
          displays the specified columns and/or expressions.
        </li>

      </ul>

      <figure id="f:pipeline_sort">
        <img src="img/db/pipeline_sort.png" alt="Three-Stage Query Processing Pipeline" />
      </figure>

      <p>
        Let's put everything we've seen so far together in a single query:
      </p>

<pre src="src/db/select_all_options.sql">
SELECT   *, ROUND(0.1 * Hours, 1)
FROM     Experiments
WHERE    Hours > 3
ORDER BY Project DESC;
</pre>

      <table class="outlined">
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>11.0</td><td>1.1</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>5.0</td><td>0.5</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td><td>0.9</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Antigravity</td><td>6.5</td><td>0.7</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td><td>0.4</td></tr>
        <tr><td>Dmitri Mendeleev</td><td>Antigravity</td><td>9.0</td><td>0.9</td></tr>
      </table>

      <p class="continue">
        The order of the clauses is required by <code>SQL</code>:
        the <code>SELECT</code> must come before the <code>FROM</code>,
        the <code>WHERE </code> clause must come next,
        and the <code>ORDER BY </code> clause must come last.
      </p>

      <div class="keypoints" id="k:sort">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>ORDER BY <em>field</em> ASC</code> (or <code>DESC</code>) to order a query's results in ascending (or descending) order.</li>
        </ul>
      </div>

    </section>

    <section id="s:aggregate">

      <h2>Aggregation</h2>

      <div class="understand" id="u:aggregate">
        <h3>Understand:</h3>
        <ul>
          <li>How to combine query results to create a single value.</li>
          <li>How to group records based on their values.</li>
          <li>How to combine the values in groups.</li>
        </ul>
      </div>

      <p>
        Now suppose we want to know how many our grad students have spent on all projects combined.
        We know how to fetch the hours:
      </p>

<pre src="src/db/select_hours.sql">
SELECT Hours FROM Experiment;
</pre>

      <p class="continue">
        but how can we add them together?
        The solution is to use the <code>SUM</code> function:
      </p>

<pre src="src/db/agg_sum_hours.sql">
SELECT SUM(Hours) FROM Experiments;
</pre>

      <p class="continue">
        The output is a table containing a single row and column:
      </p>

      <table class="outlined">
        <tr><td>35.5</td></tr>
      </table>

      <p>
        <code>SUM</code> is just one of the
        <a href="glossary.html#aggregate">aggregation</a> functions built into SQL.
        In their simplest form,
        aggregation functions reduce all the rows returned by a query
        to a single row.
        <code>MAX</code>, <code>MIN</code>, and <code>AVG</code> are also aggregation functions,
        and do what their names suggest:
      </p>

<pre src="src/db/agg_functions_hours.sql">
SELECT SUM(Hours), MAX(Hours), MIN(Hours), AVG(Hours) FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>35.5</td><td>11.0</td><td>-7.0</td><td>4.4375</td></tr>
      </table>

      <p>
        Another handy aggregation function is <code>COUNT</code>,
        which counts how many records there are in a set:
      </p>

<pre src="src/db/agg_count_hours.sql">
SELECT COUNT(Hours) FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>8</td></tr>
      </table>

      <p class="continue">
         We used <code>COUNT(Hours)</code> here,
         but we could just as easily have counted <code>Project</code>
         or any other field in the table,
         or even used <code>COUNT(*)</code>,
         since the function doesn't care about the values themselves,
         just how many values there are.
      </p>

      <p>
        Aggregation is very useful,
        but there are a few traps for the unwary.
        For example,
        what if we want the total number of hours each scientist has worked so far?
        We can find out how much time a <em>particular</em> scientist has spent in the lab like this:
      </p>

<pre src="src/db/agg_hours_mendeleev.sql">
SELECT SUM(Hours) FROM Experiments WHERE Scientist = "Dmitri Mendeleev";
</pre>

      <table class="outlined">
        <tr><td>9</td></tr>
      </table>

      <p class="continue">
        but we would have to write a separate query for each scientist,
        and remember to add a new query each time someone joined the lab.
        What we want is a query that gives us one row per scientist
        with the scientist's name and the total of his or her hours.
        Our first attempt look like this:
      </p>

<pre src="src/db/agg_per_scientist_wrong.sql">
SELECT Scientist, SUM(Hours) FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>Ivan Pavlov</td><td>35.5</td></tr>
      </table>

      <p class="continue">
        Why does this query return only one row, rather than one per scientist?
        And why does that row have Ivan Pavlov's name,
        but the total hours for <em>all</em> the scientists?
      </p>

      <p>
        The answer lies in the fact that when we used <code>SUM</code>,
        the database combined the rows in the table by summing the <code>Hours</code> column,
        but since we didn't specify a aggregation function for <code>Scientist</code>,
        the database picked an arbitrary value from that column and returned it
        (<a href="#f:bad_aggregation">Figure XXX</a>).
        In general,
        if your query selects fields directly from a table and aggregates at the same time,
        the values for unaggregated fields can be any value from the records being aggregated.
      </p>

      <figure id="f:bad_aggregation">
        <img src="img/db/bad_aggregation.png" alt="Incorrect Aggregation" />
      </figure>

      <p>
        If we really do want each scientist's hours,
        we need to tell the database to aggregate the hours for each scientist separately
        using a <code>GROUP BY</code> clause:
      </p>

<pre src="src/db/group_by_scientist.sql">
SELECT   Scientist, Hours
FROM     Experiments
GROUP BY Scientist;
</pre>

      <table class="outlined">
        <tr><td>Dmitri Mendeleev</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>-7.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>-2.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>5.0</td></tr>
      </table>

      <p class="continue">
        Here,
        the database has grouped all the records with the same value for <code>Scientist</code> together,
        then selected one row from each group to display
        (<a href="#f:correct_aggregation">Figure XXX</a>).
        Since all the rows in each group have the same scientist's name,
        we get that name;
        the value for <code>Hours</code> is just one of the values for that scientist,
        chosen randomly for the same reason that the scientist's name was chosen randomly
        when we used <code>SUM(Hours)</code> a couple of queries ago.
      </p>

      <figure id="f:correct_aggregation">
        <img src="img/db/correct_aggregation.png" alt="Correct Aggregation" />
      </figure>

      <p>
        But look what happens when we put the call to <code>SUM</code> back in our query:
      </p>

<pre src="src/db/agg_sum_by_scientist.sql">
SELECT   Scientist, SUM(Hours)
FROM     Experiments
GROUP BY Scientist;
</pre>

      <table class="outlined">
        <tr><td>Dmitri Mendeleev</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>2.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>2.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>22.5</td></tr>
      </table>

      <p class="continue">
        This is the total number of hours for each scientist,
        which is what we wanted.
        And just as we can sort by multiple criteria at once,
        we can also group by multiple criteria.
        To get the number of hours each scientist has spent on each project,
        for example,
        we would group by both columns:
      </p>

<pre src="src/db/agg_sum_by_scientist_project.sql">
SELECT   Scientist, Project, SUM(Hours)
FROM     Experiments
GROUP BY Scientist, Project;
</pre>

      <table class="outlined">
        <tr><td>Dmitri Mendeleev</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>Ivan Pavlov</td><td>Time Travel</td><td>-7.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>Teleportation</td><td>16.0</td></tr>
      </table>

      <p class="continue">
        Note that we have added <code>Project</code> to the list of columns we display,
        since the results wouldn't make much sense otherwise.
      </p>

      <p>
        The other aggregation functions work in the same way.
        For example,
        we can calculate the number of records for each scientist:
      </p>

<pre src="src/db/agg_count_scientist.sql">
SELECT   Scientist, COUNT(*)
FROM     Experiments
GROUP BY Scientist;
</pre>

      <table class="outlined">
        <tr><td>Dmitri Mendeleev</td><td>1</td></tr>
        <tr><td>Ivan Pavlov</td><td>2</td></tr>
        <tr><td>Mikhail Lomonosov</td><td>2</td></tr>
        <tr><td>Sofia Kovalevskaya</td><td>3</td></tr>
      </table>

      <p>
        We can also sort and aggregate based on grouped and aggregated values.
        For example,
        if we want the total time spent on each project sorted by project name, we would use:
      </p>

<pre src="src/db/agg_hours_project_ordered.sql">
SELECT   Project, SUM(Hours) FROM Experiments
GROUP BY Project
ORDER BY Project ASC;
</pre>

      <table class="outlined">
        <tr><td>Antigravity</td><td>19.5</td></tr>
        <tr><td>Teleportation</td><td>25.0</td></tr>
        <tr><td>Time Travel</td><td>-9.0</td></tr>
      </table>

      <p>
        The <code>ORDER BY</code> clause always goes after the <code>GROUP BY</code> clause
        because we are ordering the results of aggregation.
        Putting it another way,
        ordering the results before doing the <code>GROUP BY</code>
        wouldn't make any difference to the final answer,
        so that's not what SQL does.
      </p>

      <p>
        What if we want to sort the results by the total number of hours spent?
        Instead of using a plain field to sort on,
        like <code>Project</code>,
        we can use an aggregation function as our sorting criterion:
      </p>

<pre src="src/db/agg_hours_order_agg.sql">
SELECT   Project, SUM(Hours) FROM Experiments
GROUP BY Project
ORDER BY SUM(Hours) ASC;
</pre>

      <table class="outlined">
        <tr><td>Time Travel</td><td>-9.0</td></tr>
        <tr><td>Antigravity</td><td>19.5</td></tr>
        <tr><td>Teleportation</td><td>25.0</td></tr>
      </table>

      <p class="continue">
        This query doesn't sort the results based on a field from the table,
        but by the results of aggregating values from that table.
      </p>

      <p>
        Let's keep going and remove the negative hours for the Time Travel project
        before adding things up
        (since negative times confuse the payroll department).
        We can do this by adding a <code>WHERE</code> clause to our query
        to filter out values we don't want <em>before</em> they are grouped and aggregated:
        </p>

<pre src="src/db/agg_hours_positive.sql">
SELECT   Project, SUM(Hours) FROM Experiments
WHERE    Hours >= 0
GROUP BY Project
ORDER BY SUM(Hours) ASC;
</pre>

      <table class="outlined">
        <tr><td>Antigravity</td><td>19.5</td></tr>
        <tr><td>Teleportation</td><td>25.0</td></tr>
      </table>

      <p class="continue">
        Notice that there isn't a row in the result at all for the Time Travel project:
        all of the hours recorded for it were negative,
        so none of those records got past the <code>WHERE</code>
        to be summed.
        Looking more closely, this query:
      </p>

      <ol>

        <li>
          selected rows from the table where the <code>Hours</code> are non-negative;
        </li>

        <li>
          grouped those rows into sets that have the same values for <code>Project</code>;
        </li>

        <li>
          replaced each group with a single row whose values are
          the sum of the hours in the group,
          and the project name of the group; and
        </li>

        <li>
          ordered those rows according to the total hours.
        </li>

      </ol>

      <p class="continue">
        Aggregation is therefore a fourth stage in our query processing pipeline
        (<a href="#f:pipeline_aggregate">Figure XXX</a>).
      </p>

      <figure id="f:pipeline_aggregate">
        <img src="img/db/pipeline_aggregate.png" alt="Four-Stage Query Processing Pipeline" />
      </figure>

      <div class="keypoints" id="k:aggregate">
        <h3>Summary</h3>
        <ul>
          <li>Use aggregation functions like <code>SUM</code> <code>MAX</code> to combine many query results into a single value.</li>
          <li>Use the <code>COUNT</code> function to count the number of results.</li>
          <li>If some fields are aggregated, and others are not, the database manager displays an arbitrary result for the unaggregated field.</li>
          <li>Use <code>GROUP BY</code> to group values before aggregation.</li>
        </ul>
      </div>

    </section>

    <section id="s:design">

      <h2>Database Design</h2>

      <div class="understand" id="u:design">
        <h3>Understand:</h3>
        <ul>
          <li>That each field in a database should store a single value.</li>
          <li>That information should not be duplicated in a database.</li>
        </ul>
      </div>

      <p>
        Let's go back to sorting for a moment,
        and see if we can produce a list of scientists
        ordered by family name.
        We want our output to look like this:
      </p>

      <table class="outlined">
        <tr><td>Kovalevskaya, Sofia</td></tr>
        <tr><td>Lomonosov, Mikhail</td></tr>
        <tr><td>Mendeleev, Dmitri</td></tr>
        <tr><td>Pavlov, Ivan</td></tr>
      </table>

      <p>
        This is easy to do in a programming language like Python:
        we just split the names on the space character,
        then join the two parts using a comma and a space.
      </p>

<pre>
result = []
for name in list_of_names:
    personal_name, family_name = name.split(' ')
    new_name = family_name + ', ' + personal_name
    result.append(new_name)
result.sort()
</pre>

      <p>
        We can do something like this in some dialects of SQL, but not all,
        and even when we can, it's harder to read.
        For example, if we're using Microsoft SQL Server, the query we need is:
      </p>

<pre>
SELECT SUBSTRING(Scientist, 1, CHARINDEX(Scientist, " ")-1)
       || ", "
       || SUBSTRING(Scientist, CHARINDEX(Scientist, " ")+1, LEN(Scientist))
       FROM Experiments;
</pre>

      <p class="continue">
        Here,
        <code>CHARINDEX</code> and <code>SUBSTRING</code> are built-in functions
        that find the locations of characters and take substrings respectively,
        and <code>||</code> concatenates strings.
        This won't work as written with other databases,
        though,
        since their equivalents of <code>CHARINDEX</code> have different names
        (or, in the case of SQLite, may not exist at all).
        And even when it does work, it's still not a complete solution,
        since it doesn't sort the names.
      </p>

      <p>
        We could get further by using <a href="#s:nested">nested queries</a>,
        which we will discuss later in this chapter,
        but the right solution is to reformulate the problem.
        What we're trying to do is difficult because
        we have violated one of the fundamental rules of database design.
        The values in the <code>Scientist</code> field have several parts that we care about;
        in technical terms,
        they are not <a href="glossary.html#atomic-value">atomic values</a>.
        In a well-designed database,
        every value <em>is</em> atomic,
        so that it can be accessed directly.
      </p>

      <p>
        Here's what our table looks like when we split names into their component parts:
      </p>

      <table class="outlined" src="db/create_single_table_experiments.sql">
        <tr><td colspan="4" align="center"><strong>Experiments</strong></td></tr>
        <tr>
          <td><strong>PersonalName</strong></td>
          <td><strong>FamilyName</strong></td>
          <td><strong>Project</strong></td>
          <td><strong>Hours</strong></td>
        </tr>
        <tr>
          <td>Sofia</td>
          <td>Kovalevskaya</td>
          <td>Antigravity</td>
          <td>6.5</td>
        </tr>
        <tr>
          <td>Sofia</td>
          <td>Kovalevskaya</td>
          <td>Teleportation</td>
          <td>11.0</td>
        </tr>
        <tr>
          <td>Sofia</td>
          <td>Kovalevskaya</td>
          <td>Teleportation</td>
          <td>5.0</td>
        </tr>
        <tr>
          <td>Mikhail</td>
          <td>Lomonosov</td>
          <td>Antigravity</td>
          <td>4.0</td>
        </tr>
        <tr>
          <td>Mikhail</td>
          <td>Lomonosov</td>
          <td>Time Travel</td>
          <td>-2.0</td>
        </tr>
        <tr>
          <td>Dmitri</td>
          <td>Mendeleev</td>
          <td>Antigravity</td>
          <td>9.0</td>
        </tr>
        <tr>
          <td>Ivan</td>
          <td>Pavlov</td>
          <td>Teleportation</td>
          <td>9.0</td>
        </tr>
        <tr>
          <td>Ivan</td>
          <td>Pavlov</td>
          <td>Time Travel</td>
          <td>-7.0</td>
        </tr>
      </table>

      <p class="continue">
        It looks like a small change, but it has major implications.
        First, it makes the SQL simpler,
        since we no longer have to do substring operations to get values:
      </p>

<pre make="select-distinct-names">
SELECT DISTINCT FamilyName || ", " || PersonalName FROM Experiments;
</pre>

      <p class="continue">
        Second,
        this SQL will be much more efficient,
        since repeatedly finding substrings takes more time than simply matching values directly.
      </p>

      <div class="box">
        <h3>Why Personal and Family Names?</h3>

        <p>
          <code>PersonalName</code> and <code>FamilyName</code> may seem like odd labels for database fields:
          <code>FirstName</code> and <code>LastName</code> would be shorter.
          However, the latter pair of labels assume a cultural convention that isn't true for many people.
          In China, Japan, and other East Asian countries, for example,
          the family name is usually written first.
          This may sound like a small thing,
          but it's a good habit to get into:
          when we're designing a database,
          we should always think about the meaning of data,
          rather than how it is presented.
        </p>

      </div>

      <p>
        Our redesigned table still violates an important rule of database design.
        To see how,
        let's look at what happens if we want to store people's email addresses:
      </p>

      <table class="outlined" src="db/create_single_table_experiments.sql">
        <tr><td colspan="5" align="center"><strong>Experiments</strong></td></tr>
        <tr>
          <td><strong>PersonalName</strong></td>
          <td><strong>FamilyName</strong></td>
          <td><strong>Email</strong></td>
          <td><strong>Project</strong></td>
          <td><strong>Hours</strong></td>
        </tr>
        <tr>
          <td>Sofia</td>
          <td>Kovalevskaya</td>
          <td>skol@euphoric.edu</td>
          <td>Antigravity</td>
          <td>6.5</td>
        </tr>
        <tr>
          <td>Sofia</td>
          <td>Kovalevskaya</td>
          <td>skol@euphoric.edu</td>
          <td>Teleportation</td>
          <td>11.0</td>
        </tr>
        <tr>
          <td>Sofia</td>
          <td>Kovalevskaya</td>
          <td>skol@euphoric.edu</td>
          <td>Teleportation</td>
          <td>5.0</td>
        </tr>
        <tr>
          <td>Mikhail</td>
          <td>Lomonosov</td>
          <td>mikki@freesci.org</td>
          <td>Antigravity</td>
          <td>4.0</td>
        </tr>
        <tr>
          <td>Mikhail</td>
          <td>Lomonosov</td>
          <td>mikki@freesci.org</td>
          <td>Time Travel</td>
          <td>-2.0</td>
        </tr>
        <tr>
          <td>Dmitri</td>
          <td>Mendeleev</td>
          <td>mendeleev@euphoric.edu</td>
          <td>Antigravity</td>
          <td>9.0</td>
        </tr>
        <tr>
          <td>Ivan</td>
          <td>Pavlov</td>
          <td>pablum@euphoric.edu</td>
          <td>Teleportation</td>
          <td>9.0</td>
        </tr>
        <tr>
          <td>Ivan</td>
          <td>Pavlov</td>
          <td>pablum@euphoric.edu</td>
          <td>Time Travel</td>
          <td>-7.0</td>
        </tr>
      </table>

      <p>
        There's a lot of redundancy in this table:
        every time "Sofia" appears as a personal name,
        the family name is always "Kovalevskaya",
        and the email address is always "skol@euphoric.edu".
        If we use this design,
        we will have to eliminate duplicates almost every time we run a query,
        and if Sofia changes her email address,
        we will have to update several rows of the database.
      </p>

      <p>
        The right way to store this data is
        to separate information about scientists
        from information about experiments,
        so that no fact is ever duplicated.
        We can do this by splitting our table in two:
      </p>

      <table class="outlined">
        <tr><td colspan="3" align="center"><strong>Experiments</strong></td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <table class="outlined">
        <tr><td colspan="4" align="center"><strong>Scientists</strong></td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td></tr>
      </table>

      <p>
        Facts about our scientists now appear exactly once,
        as do the entries for experiments.
        The only exception is the two entries for Sofia Kovalevskaya's hours on the Teleportation project,
        which was in the original data.
        At this point,
        we should either insist that
        all the hours each scientist has spent on a particular project appear in a single database entry,
        or document the reasons for having multiple entries
        (e.g., because each entry is the hours worked in a single week or month).
      </p>

      <div class="keypoints" id="k:design">
        <h3>Summary</h3>
        <ul>
          <li idea="modelview">Each field in a database table should store a single atomic value.</li>
          <li idea="modelview">No fact in a database should ever be duplicated.</li>
        </ul>
      </div>

    </section>

    <section id="s:join">

      <h2>Combining Data</h2>

      <div class="understand" id="u:join">
        <h3>Understand:</h3>
        <ul>
          <li>How to combine information from several tables.</li>
          <li>How to create an alias for a table to clarify or simplify a query.</li>
          <li>What primary keys and foreign keys are.</li>
        </ul>
      </div>

      <p>
        If we divide our data between several tables,
        we must have some way to bring it back together again.
        The key to doing this is
        the fact that both tables have a <code>PersonID</code> field,
        and that the values in these columns are shared.
      </p>

      <p>
        Suppose we want to combine all the data
        from the <code>Experiments</code> and <code>Scientists</code> tables.
        The SQL command to join the two tables is <code>JOIN</code>:
      </p>

<pre src="src/db/join_scientists_experiments.sql">
SELECT * FROM Scientists JOIN Experiments;
</pre>

      <p class="continue">
        which means,
        "Combine the rows of the <code>Scientists</code> table
        with the rows of the <code>Experiments</code> table
        and return all of the columns in the result."
        The result isn't quite what we want:
      </p>

      <table class="outlined">
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <p>
        When a database does a join,
        it combines every row of one table with every row of the other:
        in mathematical terms,
        it creates the <a href="glossary.html#cross-product">cross product</a> of the sets of rows.
        It doesn't try to figure out if those rows have anything to do with each other
        because it has no way of knowing whether they do or not&mdash;we have to tell it.
      </p>

      <p>
        What we want is combinations of rows from the <code>Scientists</code> and <code>Experiments</code> tables
        that refer to the same person,
        i.e.,
        that have the same <code>PersonID</code> values.
        To express this in SQL we need to add an <code>ON</code> clause to our query:
      </p>

<pre make="join-scientists-experiments-on">
SELECT *
FROM   Scientists JOIN Experiments
ON     Scientists.PersonID = Experiments.PersonID;
</pre>

      <table class="outlined">
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>skol</td><td>Kovalevskaya</td><td>Sofia</td><td>skol@euphoric.edu</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>mlom</td><td>Lomonosov</td><td>Mikhail</td><td>mikki@freesci.org</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>dmen</td><td>Mendeleev</td><td>Dmitri</td><td>mendeleev@euphoric.edu</td><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Pavlov</td><td>Ivan</td><td>pablum@euphoric.edu</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <p>
        <code>ON</code> is like <code>WHERE</code>:
        it filters things according to some test condition.
        More specifically,
        it filters rows as they are being joined
        and only keeps the ones that pass some test.
      </p>

      <p>
        Note how in the query above we used <code>TableName.FieldName</code> to remove any ambiguity
        on what is being compared to what.
        We could do this just as well <em>after</em> joining rows
        using a <code>WHERE</code> clause as a filter:
      </p>

<pre src="src/db/join_scientists_experiments_where.sql">
SELECT *
FROM   Scientists JOIN Experiments
WHERE  Scientists.PersonID = Experiments.PersonID;
</pre>

      <p class="continue">
        but using <code>ON</code> makes it clear that the relationship is being used in the join.
        It may also be more efficient,
        since the database won't construct rows during the join
        just to throw them away during the <code>WHERE</code>.
        However,
        a good database manager will do that particular optimization automatically.
      </p>

      <p>
        We can use the <code>TableName.FieldName</code> notation
        to specify the columns we want returned by our query.
        For example,
        the query below returns the email addresses of the scientists
        who have worked on particular projects:
      </p>

<pre src="src/db/join_email_project.sql">
SELECT DISTINCT Experiments.Project, Scientists.Email
FROM            Scientists JOIN Experiments
ON              Scientists.PersonID = Experiments.PersonID;
</pre>

      <table class="outlined">
        <tr><td>Antigravity</td><td>mendeleev@euphoric.edu</td></tr>
        <tr><td>Antigravity</td><td>mikki@freesci.org</td></tr>
        <tr><td>Antigravity</td><td>skol@euphoric.edu</td></tr>
        <tr><td>Teleportation</td><td>pablum@euphoric.edu</td></tr>
        <tr><td>Teleportation</td><td>skol@euphoric.edu</td></tr>
        <tr><td>Time Travel</td><td>mikki@freesci.org</td></tr>
        <tr><td>Time Travel</td><td>pablum@euphoric.edu</td></tr>
      </table>

      <p>
        We can sometimes make long queries more readable
        by creating <a href="glossary.html#alias">aliases</a>
        for the tables we are joining:
      </p>

<pre src="src/db/join_using_alias.sql">
SELECT DISTINCT e.Project, s.Email
FROM            Experiments e JOIN Scientists s
ON              e.PersonID = s.PersonID;
</pre>

      <p class="continue">
        Here,
        we're temporarily using the names <code>e</code> and <code>s</code>
        for the <code>Experiments</code> and <code>Scientists</code> tables.
        This produces the same set of results as before.
        However,
        since the database may display rows in any order it likes,
        the output from this query and the previous one may not be textually identical.
        If we sort them,
        though,
        they are guaranteed to match:
      </p>

<pre src="src/db/join_and_order.sql">
SELECT DISTINCT e.Project, s.Email
FROM            Experiments e JOIN Scientists s
ON              e.PersonID = s.PersonID
ORDER BY        e.Project, s.Email;
</pre>

      <p>
        If joining two tables is good,
        joining multiple tables must be better.
        In fact,
        we can join any number of tables simply by adding more <code>JOIN</code> clauses.
        To see how this works,
        let's add two more tables to our database called <code>Papers</code>
        that keeps track of who co-authored the papers our group has produced so far:
      </p>

      <table class="outlined">
        <tr><td colspan="2" align="center"><strong>Authors</strong></td></tr>
        <tr>
          <td>skol</td>
          <td>antigrav-lit-survey</td>
        </tr>
        <tr>
          <td>skol</td>
          <td>teleport-quantum</td>
        </tr>
        <tr>
          <td>mlom</td>
          <td>antigrav-lit-survey</td>
        </tr>
        <tr>
          <td>ipav</td>
          <td>teleport-quantum</td>
        </tr>
      </table>
      <table class="outlined">
        <tr><td colspan="3" align="center"><strong>Papers</strong></td></tr>
        <tr>
          <td><strong>CiteKey</strong></td>
          <td><strong>Title</strong></td>
          <td><strong>Journal</strong></td>
        </tr>
        <tr>
          <td>antigrav-lit-survey</td>
          <td>Antigravity: A Survey</td>
          <td>J. Improb. Physics</td>
        </tr>
        <tr>
          <td>teleport-quantum</td>
          <td>Quantum Teleportation and Why Not</td>
          <td>Quantum Rev. Let.</td>
        </tr>
      </table>

      <p>
        Why two tables?
        Because putting all the information into one would break
        the rules we described in the previous section&mdash;for example,
        the paper's title and journal would appear together in multiple records.
        What we have done instead is give each paper a unique citation key
        (which we would use in BibTeX or some kind of reference manager),
        and then combine it once,
        and once only,
        with each author,
        and with the paper's details.
      </p>

      <p>
        Let's construct a query to get the full name of the experimenter
        and the title of every paper he or she has co-authored.
        We'll start by writing down the fields we want:
      </p>

<pre>
SELECT Scientists.PersonalName, Scientists.FamilyName, Papers.Title
&hellip;
</pre>

      <p class="continue">
        These fields are coming from the <code>Scientists</code> and <code>Papers</code> tables,
        so we have to combine those tables with <code>JOIN</code>.
        But how?
        None of the values in <code>Scientists</code> appear in <code>Papers</code>,
        or vice versa.
        How can we match records up?
      </p>

      <p>
        The solution is to add the <code>Authors</code> table to our query.
        <code>Scientists.PersonID</code> is supposed to match <code>Authors.PersonID</code>,
        and <code>Authors.CiteKey</code> matches <code>Papers.CiteKey</code>,
        so that extra stage lets us combine people and papers.
        Our query now looks like this:
      </p>

<pre src="src/db/join_three.sql">
SELECT Scientists.PersonalName, Scientists.FamilyName, Papers.Title
FROM   Scientists JOIN Authors JOIN Papers
ON     (Scientists.PersonID = Authors.PersonID) AND (Authors.CiteKey = Papers.CiteKey);
</pre>

      <table class="outlined">
        <tr><td>Sofia</td><td>Kovalevskaya</td><td>Antigravity: A Survey</td></tr>
        <tr><td>Sofia</td><td>Kovalevskaya</td><td>Quantum Teleportation and Why Not</td></tr>
        <tr><td>Mikhail</td><td>Lomonosov</td><td>Antigravity: A Survey</td></tr>
        <tr><td>Ivan</td><td>Pavlov</td><td>Quantum Teleportation and Why Not</td></tr>
      </table>

      <p id="a:keys">
        The technical terms for the concepts we have been using in this section are
        <a href="glossary.html#primary-key">primary key</a>
        and <a href="glossary.html#foreign-key">foreign key</a>.
        A primary key is a value, or combination of values,
        that uniquely identifies each row in a table.
        For example,
        the primary key for the <code>Scientists</code> table is <code>PersonID</code>:
        if two records ever have the same value for this,
        something has probably gone wrong.
      </p>

      <p>
        A foreign key is a value (or combination of values) from one table
        that identifies a unique record in another table.
        Another way of saying this is that
        a foreign key is the primary key of one table
        that appears in some other table.
        In our database,
        <code>Experiments.PersonID</code> is a foreign key into the <code>Scientists</code> table.
      </p>

      <p>
        What is the primary key for the <code>Experiments</code> table?
        If there was only one entry pairing <code>skol</code> with <code>Teleportation</code>,
        then that pair would be the primary key.
        As it is,
        we can't even be sure that using all three fields will be unique,
        since there could,
        for example,
        be two entries saying that <code>dmen</code> spent 6.5 hours working on antigravity.
      </p>

      <p>
        Most database designers believe that every table should have a well-defined primary key.
        (If nothing else,
        this allows us to print or delete specific records.)
        If the entries in <code>Experiments</code> are monthly totals,
        we should include the month in the table
        (and the year as well,
        so that we don't wind up with multiple entries for each month
        after a few years running the lab).
      </p>

      <p>
        Alternatively,
        we could create an arbitrary, unique ID for each record
        as we add it to the database.
        This is actually very common:
        those IDs have names like "student numbers" and "patient numbers",
        and they almost always turn out to have originally been
        a unique record identifier in some database system or other.
        As the query below demonstrates,
        SQLite automatically numbers records as they're added to tables,
        and we can use those record numbers in queries:
      </p>

<pre src="src/db/select_rowid.sql">
SELECT ROWID, * FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>1</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>2</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>3</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>4</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>5</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>6</td><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>7</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>8</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <div class="keypoints" id="k:join">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>JOIN</code> to create all possible combinations of records from two or more tables.</li>
          <li>Use <code>JOIN <em>tables</em> ON <em>test</em></code> to keep only those combinations that pass some test.</li>
          <li>Use <code><em>table</em>.<em>field</em></code> to specify a particular field of a particular table.</li>
          <li>Use aliases to make queries more readable.</li>
          <li idea="modelview">Every record in a table should be uniquely identified by the value of its primary key.</li>
        </ul>
      </div>

    </section>

    <section id="s:selfjoin">

      <h2>Self Join</h2>

      <div class="understand" id="u:selfjoin">
        <h3>Understand:</h3>
        <ul>
          <li>How and why to combine a table with itself.</li>
        </ul>
      </div>

      <p>
        One special case of joining tables comes up so often that it has its own name: <a href="glossary.html#self-join">self join</a>.
        As the name suggests,
        this means joining a table with itself.
        To see why this is useful,
        let's try to find out how many scientists have worked on two or more projects.
        Our first guess looks like this:
      </p>

<pre src="src/db/self_join_incorrect.sql">
SELECT PersonID, COUNT(*) FROM Experiments GROUP BY PersonID WHERE COUNT(*) > 1;
</pre>

      <p class="continue">
        but that's not legal SQL&mdash;we can't use
        an aggregated value in our <code>WHERE</code> clause,
        because <code>WHERE</code> is applied row-by-row before aggregation happens.
      </p>

      <p>
        Instead, let's join the <code>Experiments</code> table to itself.
        We will give each copy of the table an alias,
        so that we can tell which values came from which copy:
      </p>

<pre src="src/db/self_join_all.sql">
SELECT * FROM Experiments a JOIN Experiments b;
</pre>

      <p>
        The result has 64 rows, a few of which are shown below:
      </p>

      <table class="outlined">
        <tr>
          <td><strong>a.PersonID</strong></td>
          <td><strong>a.Project</strong></td>
          <td><strong>a.Hours</strong></td>
          <td><strong>b.PersonID</strong></td>
          <td><strong>b.Project</strong></td>
          <td><strong>b.Hours</strong></td>
        </tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>11.0</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>11.0</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td align="center">&hellip;</td><td align="center">&hellip;</td><td align="center">&hellip;</td><td align="center">&hellip;</td><td align="center">&hellip;</td><td align="center">&hellip;</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td align="center">&hellip;</td><td align="center">&hellip;</td><td align="center">&hellip;</td><td align="center">&hellip;</td><td align="center">&hellip;</td><td align="center">&hellip;</td></tr>
      </table>

      <p>
        Now let's add a <code>WHERE</code> clause to filter out rows
        that have different <code>PersonID</code> values,
        i.e.,
        where we have joined information about one person with information about another:
      </p>

<pre src="src/db/self_join_personid.sql">
SELECT * FROM Experiments a JOIN Experiments b WHERE a.PersonID = b.PersonID;
</pre>

      <table class="outlined">
        <tr>
          <td><strong>a.PersonID</strong></td>
          <td><strong>a.Project</strong></td>
          <td><strong>a.Hours</strong></td>
          <td><strong>b.PersonID</strong></td>
          <td><strong>b.Project</strong></td>
          <td><strong>b.Hours</strong></td>
        </tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>11.0</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>11.0</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>11.0</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>5.0</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>5.0</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>5.0</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>mlom</td><td>Time Travel</td><td>-2.0</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>mlom</td><td>Time Travel</td><td>-2.0</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>dmen</td><td>Antigravity</td><td>9.0</td><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Teleportation</td><td>9.0</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Teleportation</td><td>9.0</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
        <tr><td>ipav</td><td>Time Travel</td><td>-7.0</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Time Travel</td><td>-7.0</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
      </table>

      <p>
        Now let's add another clause to our <code>WHERE</code>
        to get rid of records where the two project names are the same:
      </p>

<pre src="src/db/self_join_project.sql">
SELECT * FROM Experiments a JOIN Experiments b
WHERE (a.PersonID = b.PersonID) AND (a.Project != b.Project);
</pre>

      <table class="outlined">
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td><td>skol</td><td>Teleportation</td><td>11.0</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>11.0</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>5.0</td><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
        <tr><td>mlom</td><td>Time Travel</td><td>-2.0</td><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>ipav</td><td>Teleportation</td><td>9.0</td><td>ipav</td><td>Time Travel</td><td>-7.0</td></tr>
        <tr><td>ipav</td><td>Time Travel</td><td>-7.0</td><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
      </table>

      <p>
        This may not seem like progress,
        but we have almost answered our original question.
        Each of these records represents the fact that some person has worked on two different projects.
        Putting it another way,
        if someone has only ever worked on one project (or hasn't worked on any projects at all),
        their ID will not appear in any record in this set.
        To get the list of names of people who have worked on two or more projects,
        therefore,
        all we have to do is display either <code>a.PersonID</code> or <code>b.PersonID</code>
        (and eliminate duplicates using <code>DISTINCT</code>).
        We will split our final query across several lines to make it easier to read,
        and use an <code>ORDER BY</code> to ensure that our results are sorted:
      </p>

<pre src="src/db/self_join_final.sql">
SELECT DISTINCT a.PersonID
FROM            Experiments a JOIN Experiments b
WHERE           (a.PersonID = b.PersonID) AND (a.Project != b.Project)
ORDER BY        a.PersonID ASC;
</pre>

      <table class="outlined">
        <tr>
          <td>ipav</td>
        </tr>
        <tr>
          <td>mlom</td>
        </tr>
        <tr>
          <td>skol</td>
        </tr>
      </table>

      <p>
        If you hang around programmers long enough,
        you will eventually hear someone call this trick "intuitive".
        They are using that word the way certain mathematicians use "obvious":
        it means,
        "You only have to read the proof a couple of times to get it."
        There actually is a rich mathematical theory underneath SQL,
        and if you immerse yourself in that theory,
        tricks like joining a table to itself do eventually seem obvious.
        For the rest of us, though,
        it's enough to learn this pattern
        and recognize when it should be used.
      </p>

      <div class="keypoints" id="k:selfjoin">
        <h3>Summary</h3>
        <ul>
          <li>Use a self join to combine a table with itself.</li>
        </ul>
      </div>

    </section>

    <section id="s:null">

      <h2>Missing Data</h2>

      <div class="understand" id="u:null">
        <h3>Understand:</h3>
        <ul>
          <li>That databases use a special value to indicate missing data.</li>
          <li>That arithmetic and logical tests on this special value produce special results.</li>
          <li>That operations which combine many values usually ignore this special value.</li>
          <li>How to handle records that contain this special value.</li>
        </ul>
      </div>

      <p>
        In the real world data is not always complete&mdash;there are always holes.
        A database uses a special value for these holes: <code>NULL</code>.
        <code>NULL</code> is not zero, <code>False</code>, or the empty string:
        it is a one-of-a-kind value that means "nothing here".
        Dealing with <code>NULL</code> requires a few special tricks,
        and sometimes some careful thinking.
      </p>

      <p>
        As an example,
        here is our <code>Experiments</code> table with a few times replaced by <code>NULL</code>:
      </p>

      <table class="outlined">
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>NULL</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>mlom</td><td>Time Travel</td><td>NULL</td></tr>
        <tr><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Time Travel</td><td>NULL</td></tr>
      </table>

      <p class="continue">
        These <code>NULL</code>s might represent values that were missing,
        that haven't been entered yet,
        or that someone erased them because they looked suspicious.
        We can't tell just by looking at the data,
        but we <em>do</em> have to take these missing values into account when writing queries.
      </p>

      <div class="box">

        <h3>Displaying NULL</h3>

        <p>
          Different databases display NULL values differently.
          For example,
          SQLite's default is to print a blank,
          so that the data above is actually shown as:
        </p>

<pre>
|skol|Antigravity|6.5|
|skol|Teleportation||
|skol|Teleportation|5.0|
|mlom|Antigravity|4.0|
|mlom|Time Travel||
|dmen|Antigravity|9.0|
|ipav|Teleportation|9.0|
|ipav|Time Travel||
</pre>

        <p>
          This format makes it easy to overlook NULLs,
          particularly if they're in the middle of a long row.
        </p>

      </div>

      <p>
        Let's start by finding out which experiments are missing <code>Hours</code> data.
        The natural thing to try is:
      </p>

<pre src="src/db/select_null_equal_error.sql">
SELECT * FROM Experiments WHERE Hours = NULL;
</pre>

      <p class="continue">
        but it produces no results.
        The reason is that <code>NULL</code> cannot be compared to anything else.
        It cannot be added to anything, either;
        in fact,
        anything combined with NULL,
        using any operator,
        is NULL.
        This means that our <code>WHERE</code> is always false,
        so no records are selected.
      </p>

      <p>
        Notice that the opposite test also fails:
        if we select rows where <code>Hours</code> is <em>not</em> equal to <code>NULL</code>,
        we still don't get any rows
        because once again the comparison always fails:
      </p>

<pre src="src/db/select_null_not_equal_error.sql">
SELECT * FROM Experiments WHERE Hours != NULL;
</pre>

      <p>
        To check whether a value is <code>NULL</code> or not,
        we must use the special <code>IS&nbsp;NULL</code> operator:
      </p>

<pre src="src/db/select_null.sql">
SELECT * FROM Experiments WHERE Hours IS NULL;
</pre>

      <table class="outlined">
        <tr><td>skol</td><td>Teleportation</td><td>NULL</td></tr>
        <tr><td>mlom</td><td>Time Travel</td><td>NULL</td></tr>
        <tr><td>ipav</td><td>Time Travel</td><td>NULL</td></tr>
      </table>

      <p>
        To find all of the rows that do <em>not</em> have a <code>NULL</code>,
        we use <code>IS&nbsp;NOT&nbsp;NULL</code>:
      </p>

<pre src="src/db/select_not_null.sql">
SELECT * FROM Experiments WHERE Hours IS NOT NULL;
</pre>

      <table class="outlined">
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
        <tr><td>ipav</td><td>Teleportation</td><td>9.0</td></tr>
      </table>

      <p>
        <code>NULL</code> causes headaches wherever it appears.
        For example,
        suppose we want to find the all of the experiments
        that didn't take exactly nine hours to do.
        It is natural to write:
      </p>

<pre src="src/db/select_not_nine_hours.sql">
SELECT * FROM Experiments WHERE Hours != 9.0;
</pre>

      <table class="outlined">
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
      </table>

    <p class="continue">
      but this query filters out all the records that have <code>NULL</code> hours
      as well as those that took something other than one hour.
      Once again,
      the reason is that when <code>Hours</code> is <code>NULL</code>,
      the <code>!=</code> comparison fails.
      If we want to keep the rows that have <code>NULL</code> <code>Hours</code>,
      we need to add an explicit check using <code>IS</code>:
    </p>

<pre src="src/db/select_not_nine_hours_keep_null.sql">
SELECT * FROM Experiments WHERE (Hours != 9.0) OR (Hours IS NULL);
</pre>

      <table class="outlined">
        <tr><td>skol</td><td>Antigravity</td><td>6.5</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>&nbsp;</td></tr>
        <tr><td>skol</td><td>Teleportation</td><td>5.0</td></tr>
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>mlom</td><td>Time Travel</td><td>&nbsp;</td></tr>
        <tr><td>ipav</td><td>Time Travel</td><td>&nbsp;</td></tr>
      </table>

      <p class="continue">
        This query really does exclude only those records marked as taking one hour.
        It's up to use to decide if this is the right thing to do or not
        based on how we're going to use the query's results,
        but this technique gives us the choice.
      </p>

      <p>
        <code>NULL</code> also needs careful handling when we are aggregating.
        Most aggregation functions skip <code>NULL</code> values in their calculations.
        For example, the query:
      </p>

<pre src="src/db/select_sum_hours_null.sql">
SELECT SUM(Hours) FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>33.5</td></tr>
      </table>

      <p class="continue">
        adds up everyone's hours,
        skipping the <code>NULL</code>s.
        This might seem like a sensible default behavior,
        but consider what happens when we calculate an average with:
      </p>

<pre src="src/db/select_avg_hours_null.sql">
SELECT AVG(Hours) FROM Experiments;
</pre>

      <table class="outlined">
        <tr><td>6.7</td></tr>
      </table>
<span class="comment"> AB: I didn't understand this next paragraph. </span>
      <p class="continue">
        Once again,
        <code>NULL</code> values have not been included,
        so this average is the sum of the five actual values we have,
        divided by five,
        rather than the sum divided by the number of experiments&mdash;i.e.,
        it does <em>not</em> treat the <code>NULL</code> values as contributing zero to the total.
        Again,
        it's up to us to decide whether this is the right behavior or not.
      </p>

      <div class="keypoints" id="k:null">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>NULL</code> in place of missing information.</li>
          <li>Almost every operation involving <code>NULL</code> produces <code>NULL</code> as a result.</li>
          <li>Test for nulls using <code>IS NULL</code> and <code>IS NOT NULL</code>.</li>
          <li>Most aggregation functions skip nulls when combining values.</li>
        </ul>
      </div>

    </section>

    <section id="s:nested">

      <h2>Nested Queries</h2>

      <div class="understand" id="u:nested">
        <h3>Understand:</h3>
        <ul>
          <li>How to use the results of one query in the condition of another query.</li>
          <li>How to find desired results by subtracting undesired results from all possibilities.</li>
        </ul>
      </div>

      <p>
        Let's switch back to the <code>Experiments</code> table that doesn't contain <code>NULL</code>s.
        How do we find scientists who have <em>not</em> been working on time travel?
        Our first guess might be:
      </p>

<pre src="src/db/select_not_time_travel_flawed.sql">
SELECT DISTINCT PersonID FROM Experiments WHERE Project != "Time Travel";
</pre>

      <p>
        Unfortunately, this doesn't give us what we want.
        <code>ivan</code> and <code>skol</code> have both worked both on Time Travel,
        but show up in the results:
      </p>

      <table class="outlined">
        <tr><td>dmen</td></tr>
        <tr><td>ipav</td></tr>
        <tr><td>mlom</td></tr>
        <tr><td>skol</td></tr>
      </table>

      <p>
        Let's think this through.
        There are scientists who have worked on Time Travel,
        scientists who have only worked on other projects,
        and scientists who have done both.
        Our query returns all of the scientists who have worked on projects other than Time Travel,
        but that includes ones who have worked on Time Travel <em>and</em> other projects
        (<a href="#f:venn_time_travel">Figure XXX</a>).
      </p>

      <figure id="f:venn_time_travel">
        <img src="img/db/venn_time_travel.png" alt="Scientists and Time Travel" />
      </figure>

      <p>
        The trick to answering this question&mdash;and it <em>is</em> a trick&mdash;is
        to subtract those scientists who <em>have</em> worked on Time Travel
        (i.e., the ones we <em>don't</em> want)
        from the set of all scientists.
        To do this,
        we will need to use a <a href="glossary.html#nested-query">nested query</a>
        (also called a <a href="glossary.html#subquery">subquery</a>).
      </p>

      <p>
        Let's work up to it in stages.
        Finding all of the scientists is easy:
      </p>

<pre>
SELECT DISTINCT PersonID FROM Experiments;
</pre>

      <p class="continue">
        If we knew in advance which scientists we didn't want,
        we could use <code>NOT IN</code> to subtract a fixed set,
        like this:
      </p>

<pre>
SELECT DISTINCT PersonID FROM Experiment WHERE PersonID NOT IN ('ivan', 'skol');
</pre>

      <p class="continue">
        We don't actually know which scientists who have worked on Time Travel,
        but we can generate it with this query:
      </p>

<pre src="src/db/time_travel_subquery.sql">
SELECT DISTINCT PersonID FROM Experiment WHERE Project = "Time Travel";
</pre>

      <p>
        What we want to do is somehow use the result of the second query in the first.
        SQL allows us to do exactly this,
        i.e.,
        to nest one query inside another so that we can use the results of the nested query
        in the filter conditions of the main query.
        Here's what it looks like:
      </p>

<pre src="src/db/select_nested_subtract.sql">
SELECT DISTINCT PersonID FROM Experiments WHERE PersonID NOT IN
       (SELECT DISTINCT PersonID FROM Experiments WHERE Project = "Time Travel");
</pre>

      <table class="outlined">
        <tr><td>dmen</td></tr>
        <tr><td>skol</td></tr>
      </table>

      <p>
        We can read this query as saying,
        "Fetch all of the scientists who have done experiments,
        except for the ones that appear in the list of scientists who have worked on Time Travel".
        It isn't intuitive,
        but the pattern is easy to learn,
        and very useful.
      </p>

      <p>
        Nested queries can also be used as if they were tables in their own right.
        For example,
        suppose we want to know how many different projects each scientist has worked on.
        We can begin by finding the distinct list of projects for scientist like this:
      </p>

<pre>
SELECT DISTINCT PersonID, Project FROM Experiments;
</pre>

      <p>
        Now we want to count how many results there are for each scientist.
        Since counting is an aggregation,
        we need to use the results of this query as input for another query that does the aggregation.
        We can do this by wrapping the first query in parentheses
        and putting it in the <code>FROM</code> clause of the second query:
      </p>

<pre>
&hellip;
FROM (SELECT DISTINCT PersonID, Project FROM Experiments);
</pre>

      <p class="continue">
        The next step is to write the outer query.
        We want the scientist, and count of their projects:
      </p>

<pre>
SELECT PersonID, COUNT(*)
FROM   (SELECT DISTINCT PersonID, Project FROM Experiments);
</pre>

      <p class="continue">
        and since we want the count for each scientists,
        we have to add a <code>GROUP&nbsp;BY</code> for the outer query.
        The whole thing is therefore:
      </p>

<pre src="src/db/nested_query_group_by.sql">
SELECT   PersonID, COUNT(*)
FROM     (SELECT DISTINCT PersonID, Project FROM Experiments)
GROUP BY PersonID;
</pre>

      <table class="outlined">
        <tr><td>dmen</td><td>1</td></tr>
        <tr><td>ipav</td><td>2</td></tr>
        <tr><td>mlom</td><td>2</td></tr>
        <tr><td>skol</td><td>2</td></tr>
      </table>

      <p>
        Nesting queries like this is really useful
        if the data we want isn't present in exactly the right form in the database.
        We can use one query to get the data in the form we need it in,
        and then wrap another query around it to get the answer we originally wanted.
      </p>

      <div class="keypoints" id="k:nested">
        <h3>Summary</h3>
        <ul>
          <li>Use nested queries to create temporary sets of results for further querying.</li>
          <li>Use nested queries to subtract unwanted results from all results to leave desired results.</li>
        </ul>
      </div>

    </section>

    <section id="s:create">

      <h2>Creating and Modifying Tables</h2>

      <div class="understand" id="u:create">
        <h3>Understand:</h3>
        <ul>
          <li>How to create database tables.</li>
          <li>How to define the fields in a database table.</li>
          <li>How to specify the properties and constraints of a table's fields.</li>
          <li>How to erase database tables.</li>
          <li>How to insert and delete records in tables.</li>
          <li>The importance of keeping relationships consistent as information is added or deleted.</li>
        </ul>
      </div>

      <p>
        We have only looked at how to get information out of a database so far,
        both because that is more frequent than adding information,
        and because most other operations only make sense
        once queries are understood.
        If we want to create and modify data,
        we need to know two other pairs of commands.
      </p>

      <p>
        The first pair are <code>CREATE&nbsp;TABLE</code> and <code>DROP&nbsp;TABLE</code>.
        While they are written as two words,
        they are actually single commands.
        The first one creates a new table;
        its arguments are the names and types of the table's columns.
        For example,
        the following statements create the four tables in our experiments database:
      </p>

<pre src="src/db/create_tables.sql">
CREATE TABLE Experiments(PersonID TEXT, Project TEXT, Hours REAL);
CREATE TABLE Scientists(PersonID TEXT, FamilyName TEXT, PersonalName TEXT, Email TEXT);
CREATE TABLE Authors(PersonID TEXT, CiteKey TEXT);
CREATE TABLE Papers(CiteKey TEXT, Title TEXT, Journal TEXT);
</pre>

      <p class="continue">
        and we can get rid of one of our tables using:
      </p>

<pre src="src/db/drop_tables.sql">
DROP TABLE Experiments;
</pre>

      <p class="continue">
        Be very careful when doing this:
        most databases have some support for undoing changes,
        but it's better not to have to rely on it.
      </p>

      <p>
        Different database systems support different data types for table columns,
        but most provide the following:
      </p>

      <table>
        <tr>
          <td>
            <code>INTEGER</code>
          </td>
          <td>
            A signed integer.
          </td>
        </tr>
        <tr>
          <td>
            <code>REAL</code>
          </td>
          <td>
            A floating point value.
          </td>
        </tr>
        <tr>
          <td>
            <code>TEXT</code>
          </td>
          <td>
            A string.
          </td>
        </tr>
        <tr>
          <td>
            <code>BLOB</code>
          </td>
          <td>
            Any "binary large object"
            such as an image or audio file.
          </td>
        </tr>
      </table>

      <p>
        Most databases also support Booleans and date/time values;
        SQLite uses the integers 0 and 1 for the former,
        and represents the latter either as numbers
        or as strings in the format YYYY-MM-DD&nbsp;HH:MM:SS.SSS.
        An increasing number of databases also support geographic data types,
        such as latitude and longitude.
        Keeping track of what particular systems do or do not offer,
        and what names they give different data types,
        is yet another portability headache.
      </p>

      <p>
        What may be more interesting is the fact that
        we can specify properties and constraints for columns when creating a table.
        For example,
        a better definition for the <code>Scientists</code> table would be:
      </p>

<pre src="src/db/create_constraints.sql">
CREATE TABLE Scientists(
    PersonID     TEXT PRIMARY KEY,        -- uniquely identifies entries
    FamilyName   TEXT NOT NULL,           -- must have value
    PersonalName TEXT NOT NULL,           -- ditto
    Email        TEXT UNIQUE              -- no duplicates
);
</pre>

      <p class="continue">
        Constraints are declared after the type name;
        once again,
        exactly which ones are available,
        and what they're called,
        depends on which database manager we are using.
        (And note that we are finally commenting our SQL using <code>--</code>,
        which we should have been doing all along.)
      </p>

      <p>
        Once tables have been created,
        we can add and remove records using our other pair of commands,
        <code>INSERT</code> and <code>DELETE</code>.
        The simplest form of <code>INSERT</code> statement lists values in order:
      </p>

<pre src="src/db/simple_insert.sql">
INSERT INTO Scientists VALUES("skol", "Kovalevskaya", "Sofia", "skol@euphoric.edu");
INSERT INTO Scientists VALUES("mlom", "Lomonosov", "Mikhail", "mikki@freesci.org");
INSERT INTO Scientists VALUES("dmen", "Mendeleev", "Dmitri", "mendeleev@euphoric.edu");
INSERT INTO Scientists VALUES("ipav", "Pavlov", "Ivan", "pablum@euphoric.edu");
</pre>

      <p>
        We can also insert values into one table directly from another:
      </p>

<pre src="src/db/insert_from_query.sql">
CREATE TABLE JustEmail(PersonID TEXT, Email TEXT);
INSERT INTO JustEmail SELECT PersonId, Email FROM Scientists;
</pre>

      <p>
        Deleting records can be a bit trickier,
        because we have to ensure that the database remains internally consistent.
        If all we care about is a single table,
        we can use the <code>DELETE</code> command with a <code>WHERE</code> clause
        that matches the records we want to discard.
        For example,
        if Dmitri Mendeleev leaves our lab,
        we can remove him from the <code>Scientists</code> table like this:
      </p>

<pre src="src/db/simple_delete.sql">
DELETE FROM Scientists WHERE PersonID = "dmen";
</pre>

      <p>
        But now we have a problem&mdash;a potentially catastrophic one.
        Our <code>Experiments</code> table still contains a record
        recording the fact that Dmitri spent nine hours working on the Antigravity project:
      </p>

<pre>
SELECT * FROM Experiments WHERE PersonID = "dmen";
</pre>

      <table class="outlined">
        <tr><td>dmen</td><td>Antigravity</td><td>9.0</td></tr>
      </table>

      <p>
        That's never supposed to happen:
        <code>Experiments.PersonID</code> is a foreign key into the <code>Scientists</code> table,
        and all our queries assume there will be a row in the latter
        matching every value in the former.
      </p>

      <p>
        This problem is called <a href="glossary.html#referential-integrity">referential integrity</a>:
        we need to ensure that all references between tables can always be resolved correctly.
        One solution, if our database supports it,
        is to use a <a href="glossary.html#cascading-delete">cascading delete</a>,
        so that when a record in one table is deleted,
        the database automatically deletes other records that refer to it.
        However,
        this technique is outside the scope of this chapter.
      </p>

      <div class="keypoints" id="k:create">
        <h3>Summary</h3>
        <ul>
          <li>Use <code>CREATE TABlE <em>name</em>(...)</code> to create a table.</li>
          <li>Use <code>DROP TABLE <em>name</em></code> to erase a table.</li>
          <li>Specify field names and types when creating tables.</li>
          <li>Specify <code>PRIMARY KEY</code>, <code>NOT NULL</code>, and other constraints when creating tables.</li>
          <li>Use <code>INSERT INTO <em>table</em> VALUES(...)</code> to add records to a table.</li>
          <li>Use <code>DELETE FROM <em>table</em> WHERE <em>test</em></code> to erase records from a table.</li>
          <li>Maintain referential integrity when creating or deleting information.</li>
        </ul>
      </div>

    </section>

    <section id="s:transactions">

      <h2>Transactions</h2>

      <div class="understand" id="u:transactions">
        <h3>Understand:</h3>
        <ul>
          <li>How to group operations to ensure predictable behavior.</li>
          <li>That grouped operations only take effect when told to.</li>
        </ul>
      </div>

      <p>
        Let's look at another problem.
        Suppose we have another table that shows which pieces of equipment
        have been borrowed by which scientists:
      </p>

      <table class="outlined">
        <tr><td colspan="2" align="center"><strong>Equipment</strong></td></tr>
        <tr><td><strong>PersonID</strong></td><td><strong>EquipmentID</strong></td></tr>
        <tr><td>skol</td><td>CX-211 oscilloscope</td></tr>
        <tr><td>skol</td><td>Greenworth balance</td></tr>
        <tr><td>mlom</td><td>Cavorite damping plates</td></tr>
      </table>

      <p class="continue">
        (We should actually give each piece of equipment a unique ID,
        and use that ID here instead of the full name,
        just as we created a separate table for scientists earlier in this chapter,
        but we will bend the rules for now.)
        If Sofia Kovalevskaya gives the oscilloscope to Ivan Pavlov,
        we need to execute two statements to update this table:
      </p>

<pre>
DELETE FROM Equipment WHERE PersonID = "skol" and EquipmentID = "CX-211 oscilloscope";
INSERT INTO Equipment VALUES("ipav", "CX-211 oscilloscope");
</pre>

      <p>
        This is all fine&mdash;unless our program or our database happen to crash
        between the first statement and the second.
        If that happens,
        the <code>Equipment</code> table won't have a record for the oscilloscope at all.
        Such a crash may seem unlikely,
        but remember:
        if a computer can do two billion operations per second,
        that means there are two billion opportunities every second for something to go wrong.
        And if our operations take a long time to complete&mdash;as they will
        when we are working with large datasets,
        or when the database is being heavily used&mdash;the odds of failure increase.
      </p>

      <p>
        What we really want is a way to ensure that every operation is <a href="glossary.html#acid">ACID</a>:
        <a href="glossary.html#atomic-operation">atomic</a> (i.e. indivisible),
        consistent, isolated, and durable.
        The precise meanings of these terms doesn't matter;
        what does is the notion that
        every logical operation on the database should either run to completion
        as if nothing else was going on at the same time,
        or fail without having any effect at all.
      </p>

      <p>
        The tool we use to ensure that this happens is called
        a <a href="glossary.html#transaction">transaction</a>.
        Here's how we should actually write the statements
        to move the oscilloscope from one person to another:
      </p>

<pre src="src/db/simple_transaction.sql">
BEGIN TRANSACTION;
DELETE FROM Equipment WHERE PersonID = "skol" and EquipmentID = "CX-211 oscilloscope";
INSERT INTO Equipment VALUES("ipav", "CX-211 oscilloscope");
END TRANSACTION;
</pre>

      <p class="continue">
        When we do this,
        the database manager treats everything in the transaction as one large statement.
        If anything goes wrong inside,
        then none of the changes made in the transaction will actually be written to the database&mdash;it
        will be as if the transaction had never happened.
        Changes are only stored permanently
        when we <a href="glossary.html#commit">commit</a> them at the end of the transaction.
      </p>

      <div class="box">

        <h3>Transactions and Commits</h3>

        <p>
          We first used the term "transaction" in
          <a href="svn.html#a:transaction">our discussion of version control</a>.
          That's not a coincidence:
          behind the scenes,
          tools like Subversion are using many of the same algorithms as database managers
          to ensure that either everything happens consistently
          or nothing happens at all.
          We <a href="svn.html#a:commit">use the term "commit"</a> for the same reason:
          just as our changes to local files aren't written back to the version control repository
          until we commit them,
          our (apparent) changes to a database aren't written to disk
          until we say so.
        </p>

      </div>

      <p>
        Transactions serve another purpose as well.
        Suppose we have decided that the <code>Experiments</code> table will store
        the total number of hours that each scientist has worked on each project.
        At one point in time,
        there are two records for Mikhail Lomonosov:
      </p>

      <table class="outlined">
        <tr><td>mlom</td><td>Antigravity</td><td>4.0</td></tr>
        <tr><td>mlom</td><td>Time Travel</td><td>-2.0</td></tr>
      </table>

      <p>
        Late one Friday afternoon,
        Mikhail remembers that he forgot to add three hours to his time on the Antigravity project.
        He uses these two statements:
      </p>

<pre src="src/db/update_mlom_hours.sql">
UPDATE Experiments
  SET Hours = 3.0 + (SELECT Hours FROM Experiments WHERE PersonID = "mlom" and Project = "Antigravity")
WHERE PersonID = "mlom" and Project = "Antigravity";
</pre>

      <p class="continue">
        The inner select gets the old value for Mikhail's hours;
        the outer <code>UPDATE</code> adds 3.0 to that
        and writes the result back to the database.
      </p>

      <p>
        At the same moment as Mikhail runs his command,
        though,
        Dmitri Mendeleev decides to add six hours to Mikhail's time on the project
        in recognition of the work he did putting a poster together for a conference.
        His command looks exactly the same as the one above,
        except he adds 6.0 instead of 3.0.
      </p>

      <p>
        After both operations have completed,
        the database should show that Mikhail has spent 13 hours working on antigravity
        (the 4.0 we started with, plus the 3.0 that he added, plus 6.0 more that Dmitry added).
        However,
        there is a small chance that it won't.
        To see why,
        let's break the two queries into their respective read and write steps
        and place them side by side:
      </p>

      <table border="1">
        <tr>
          <td><code>X = read Experiments("mlom", "Antigravity")</code></td>
          <td><code>Y = read Experiments("mlom", "Antigravity")</code></td>
        </tr>
        <tr>
          <td><code>write Experiments("mlom", "Antigravity", X+3.0)</code></td>
          <td><code>write Experiments("mlom", "Antigravity", Y+6.0)</code></td>
        </tr>
      </table>

      <p>
        The database can only actually do one thing at once,
        so it must put these four operations into some sequential order.
        That order has to respect the original order within each column,
        but the database can interleave the two columns any way it wants.
        If it orders them like this:
      </p>

      <table border="1">
        <tr>
          <td><code>X = read Experiments("mlom", "Antigravity")</code></td>
        </tr>
        <tr>
          <td><code>write Experiments("mlom", "Antigravity", X+3.0)</code></td>
        </tr>
        <tr>
          <td><code>Y = read Experiments("mlom", "Antigravity")</code></td>
        </tr>
        <tr>
          <td><code>write Experiments("mlom", "Antigravity", Y+6.0)</code></td>
        </tr>
      </table>

      <p class="continue">
        then all is well:
        the final value in the database is 13.0.
        But what if it interleaves the operations like this:
      </p>

      <table border="1">
        <tr>
          <td><code>X = read Experiments("mlom", "Antigravity")</code></td>
        </tr>
        <tr>
          <td><code>Y = read Experiments("mlom", "Antigravity")</code></td>
        </tr>
        <tr>
          <td><code>write Experiments("mlom", "Antigravity", X+3.0)</code></td>
        </tr>
        <tr>
          <td><code>write Experiments("mlom", "Antigravity", Y+6.0)</code></td>
        </tr>
      </table>

      <p>
        This ordering puts the initial value, 4.0, into both <code>X</code> and <code>Y</code>.
        It then writes 7.0 back to the database (the third statement),
        and then writes 10.0,
        since <code>Y</code> holds 4.0 and we're adding 6.0 to it.
      </p>

      <p>
        This is called a <a href="glossary.html#race-condition">race condition</a>,
        since the final result depends on a race between the two operations.
        Race conditions are part of what makes parallel programming such a nightmare:
        they are difficult to spot in advance
        (since they are caused by the interactions between components,
        rather than by anything in any one of those components),
        and can be almost impossible to debug
        (since they usually occur intermittently and infrequently).
      </p>

      <p>
        Transactions come to our rescue once again.
        If both users put their statements in transactions,
        the database will act as if it executed all of one and then all of the other.
        Whether or not it actually does this is up to whoever wrote the database program itself:
        modern databases use very sophisticated algorithms to determine
        which operations actually have to be run sequentially,
        and which can safely be run in parallel to improve performance.
      </p>

      <div class="keypoints" id="k:transactions">
        <h3>Summary</h3>
        <ul>
          <li>Place operations in a transaction to ensure that they appear to be atomic, consistent, isolated, and durable.</li>
        </ul>
      </div>

    </section>

    <section id="s:programming">

      <h2>Programming With Databases</h2>

      <div class="understand" id="u:programming">
        <h3>Understand:</h3>
        <ul>
          <li>That database queries can and should be placed inside programs written in general-purpose languages.</li>
          <li>How to connect to a database, run a query, and gather results.</li>
          <li>How villains can try to insert their own code into database queries.</li>
          <li>How to insert values into a query safely.</li>
        </ul>
      </div>

      <p>
        To end this chapter,
        let's have a look at how to access a database from
        a general-purpose programming language like Python.
        Other languages use almost exactly the same model:
        library and function names may differ,
        but the concepts are the same.
      </p>

      <p>
        Here's a short Python program that selects scientists' IDs and email addresses
        from an SQLite database stored in a file called <code>lab.db</code>:
      </p>

<pre>
import sqlite3                                                  # 0
                                                                # 1
connection = sqlite3.connect("lab.db")                          # 2
cursor = connection.cursor()                                    # 3
cursor.execute("SELECT PersonID, Email FROM Scientists;")       # 4
results = cursor.fetchall();                                    # 5
for r in results:                                               # 6
    print r                                                     # 7
cursor.close();                                                 # 8
connection.close();                                             # 9
<span class="out">(u'skol', u'skol@euphoric.edu')
(u'mlom', u'mikki@freesci.org')
(u'dmen', u'mendeleev@euphoric.edu')
(u'ipav', u'pablum@euphoric.edu')</span>
</pre>

      <p>
        The program starts by importing the <code>sqlite3</code> library.
        If we were connecting to MySQL, DB2, or some other database,
        we would import a different library,
        but all of them provide the same functions,
        so that the rest of our program does not have to change
        (at least, not much)
        if we switch from one database to another.
      </p>

      <p>
        Line 2 establishes a connection to the database.
        Since we're using SQLite,
        all we need to specify is the name of the database file.
        Other systems may require us to provide a username and password as well.
        Line 3 then uses this connection to create a <a href="glossary.html#cursor">cursor</a>.
        Just like the cursor in an editor,
        its role is to keep track of where we are in the database.
      </p>

      <p>
        On line 4, we use that cursor to ask the database to execute a query for us.
        The query is written in SQL,
        and passed to <code>cursor.execute</code> as a string.
        It's our job to make sure that SQL is properly formatted;
        if it isn't,
        or if something goes wrong when it is being executed,
        the database will report an error.
      </p>

      <p>
        The database returns the results of the query to us
        in response to the <code>cursor.fetchall</code> call on line 5.
        This result is a list with one entry for each record in the result set;
        if we loop over that list (line 6) and print those list entries (line 7),
        we can see that each one is a tuple
        with one element for each field we asked for.
      </p>

      <p>
        Finally, lines 8 and 9 close our cursor and our connection,
        since the database can only keep a limited number of these open at one time.
        Since establishing a connection takes time,
        though,
        we shouldn't open a connection,
        do one operation,
        then close the connection,
        only to reopen it a few microseconds later to do another operation.
        Instead,
        it's normal to create one connection that stays open for the lifetime of the program.
      </p>

      <div class="box">
        <h3>What Are The u's For?</h3>

        <p>
          You may have noticed that
          each of the strings in our output has a lower-case 'u' in front of it.
          That is Python's way of telling us that the string is stored in
          <a href="glossary.html#unicode">Unicode</a>,
          which is used to handle characters beyond the A-Z and 0-9 used in most English words.
        </p>

      </div>

      <p>
        Let's have another look at the query on line 4.
        In real life,
        queries will often depend on values from a program's user.
        For example,
        our program might read a list of user IDs and project names
        and display the hours those people have spent on those projects.
        It is tempting to write that program like this:
      </p>

<pre>
import sys, sqlite3

statement = '''SELECT PersonID, Project, Hours
FROM Experiments
WHERE PersonID = "%s" and Project = "%s";
'''

connection = sqlite3.connect("lab.db")
cursor = connection.cursor()
for line in sys.stdin:
    person, project = line.split(' ', 1)
    s = statement % (person, project)
    cursor.execute(s)
    results = cursor.fetchall();
    for r in results:
        print r
cursor.close()
connection.close()
</pre>

      <p>
        The variable <code>statement</code> holds the statement we want to execute,
        with <code>%s</code> format strings where we want to insert
        the hours, the person's ID, and the name of the project.
        Each time we read a line from standard input,
        we split it into two pieces at the first space,
        then create a new string based on <code>statement</code> that includes them.
        For example,
        if we read in the line:
      </p>

<pre>
mlom Antigravity
</pre>

      <p class="continue">
        we use these two values to fill in our query, which becomes:
      </p>

<pre>
SELECT PersonID, Project, Hours
FROM Experiments
WHERE PersonID = "mlom" and Project = "Antigravity";
</pre>

      <p>
        But what happens if someone gives the program this input?
      </p>

<pre>
mlom Antigravity&quot;; DROP TABLE Scientists;
</pre>

      <p class="continue">
        It looks like there's garbage after the name of the project,
        but it is very carefully chosen garbage.
        Everything from the word "Antigravity" to the end of the line
        will be inserted into our query,
        making it:
      </p>

<pre>
SELECT PersonID, Project, Hours
FROM Experiments
WHERE PersonID = "mlom" and Project = "Antigravity"; DROP TABLE  Scientists;
</pre>

      <p class="continue">
        The double quote and semicolon at the end of the input
        end the <code>SELECT</code> statement;
        the rest of the input then puts a <code>DROP TABLE</code> statement in our query.
        If we run this,
        it will erase one of the tables in our database.
      </p>

      <p>
        This technique is called <a href="glossary.html#sql-injection">SQL injection</a>,
        and it has been used to attack thousands of programs over the years.
        In particular,
        many web sites that take data from users insert values directly into queries
        without checking them carefully first.
      </p>

      <p>
        Since a villain might try to smuggle commands into our queries in many different ways,
        the safest way to deal with this threat is
        to replace characters like quotes with their escaped equivalents,
        so that we can safely put whatever the user gives us inside a string.
        We can do this by using a <a href="glossary.html#prepared-statement">prepared statement</a>
        instead of formatting our statements as strings.
        Here's what our example program looks like if we do this:
      </p>

<pre>
import sys, sqlite3

statement = '''
SELECT PersonID, Project, Hours
FROM Experiments
WHERE PersonID = ? and Project = ?;
'''

connection = sqlite3.connect("lab.db")
cursor = connection.cursor()
for line in sys.stdin:
    person, project = line.strip().split(' ', 1)
    cursor.execute(statement, (person, project))
    results = cursor.fetchall();
    for r in results:
        print r
cursor.close()
connection.close()
</pre>

      <p>
        The key changes are in the query template string <code>statement</code>,
        and the <code>execute</code> call inside the loop.
        Instead of formatting the query ourselves,
        we put question marks in the query template where we want to insert values.
        When we call <code>execute</code>,
        we provide a tuple as a second argument
        that contains exactly as many values as there are question marks in the template.
        The library matches values to question marks in order,
        and translates any special characters in the values
        into their escaped equivalents
        so that they are safe to use.
      </p>

      <div class="keypoints" id="k:programming">
        <h3>Summary</h3>
        <ul>
          <li>Most applications that use databases embed SQL in a general-purpose programming language.</li>
          <li>Database libraries use connections and cursors to manage interactions.</li>
          <li>Programs can fetch all results at once, or a few results at a time.</li>
          <li>If queries are constructed dynamically using input from users, malicious users may be able to inject their own commands into the queries.</li>
          <li>Dynamically-constructed queries can use SQL's native formatting to safeguard against such attacks.</li>
        </ul>
      </div>

    </section>

    <section id="s:summary">

      <h2>Summing Up</h2>

      <p>
        A database is the right tool for managing complex and structured data.
        Thousands of programmer-years have gone into their design and implementation
        so that they can handle very large datasets&mdash;terabytes or more&mdash;quickly and reliably.
        Queries allow for great flexibility in how you are able to analyze your data,
        which makes databases a good choice when you are exploring data.
        On the other hand,
        there are lots of things databases <em>can't</em> do,
        or can't do well:
        that's why we have general-purpose programming languages like Python.
      </p>

    </section>