#!/usr/bin/perl -T

BEGIN {
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
   print "Content-type: text/html\n\n";
}
print "<h1> HELLO WORLD </h1>\n"
print "<font color=green>Done!</font>\n";
print "<font color=red>Done!</font>\n";
print "<font color=green>Done!</font>\n";
