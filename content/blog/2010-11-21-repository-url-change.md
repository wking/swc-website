Post_Id: 3769
Author: Jon Pipitone
Title: Repository URL Change
Tags: tooling

<p>We've been having problems hosting the course's Subversion repository at its current URL (http://software-carpentry.org/swc), and so we've moved it to:</p>
<p>http://svn.software-carpentry.org/swc</p>
<p>This URL points to the same repository as before. If you already have a working copy checked out you can switch it to use the new URL by running the following shell command in the top-level folder of your working copy:</p>
<p><code>svn switch --relocate http://software-carpentry.org/swc http://svn.software-carpentry.org/swc</code></p>

