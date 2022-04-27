#!/usr/bin/perl 
BEGIN {
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
   print "Content-type: text/html\n\n";
}
print "content-type: text/html\n\n";
print "<h1> Hello World </h1>\n";
print "<font color=green>Done!</font>\n";
print "<font color=red>Done!</font>\n";
print "<font color=green>Done!</font>\n";
