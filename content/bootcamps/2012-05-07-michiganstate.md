Venue: Michigan State University
Enddate: 2012-05-08
Latlng: 42.7272884,-84.482106

<p><strong>Database file</strong>: experiments.db</p>
<p><strong>Querying a Database with Python</strong></p>
<pre>import sqlite3
connection = sqlite3.connect("experiments.db")
cursor = connection.cursor()
cursor.execute("SELECT FirstName, LastName FROM Person;")
results = cursor.fetchall();
for r in results:
    print r[0], r[1]
cursor.close();
connection.close();</pre>
<p><strong>Starting point for Monday night exercise</strong></p>
<pre>import sys

def count_birds(reader):
    reader.readline() # first line is header, so ignore
    total = 0
    for line in reader:
        date, breed, count = line.split(',')
        count = int(count)
        total += count
    return total

grand_total = 0
for filename in sys.argv[1:]:
    source = open(filename, 'r')
    total = count_birds(source)
    grand_total += total
    print total, filename
    source.close()
print grand_total, 'total'</pre>
<p><strong>When:</strong> May 7-9, 2012.</p>
<p><strong>Where:</strong>Michigan State University.</p>