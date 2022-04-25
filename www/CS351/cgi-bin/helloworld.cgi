#!/usr/bin/perl
BEGIN {
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
   print "Content-type: text/html\n\n";
}

print "content-type:text/html; charset=utf-8\n\n";
print h1({-style=>'Color: red;'},'Hello world');