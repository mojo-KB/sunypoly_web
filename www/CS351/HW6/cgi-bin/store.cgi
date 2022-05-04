#!/usr/bin/perl

  use strict;
  use warnings;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS2/Class-Accessor-0.34/blib/lib';
  use base 'Class::Accessor::Fast';
  use Class::Accessor::Fast;
  use Class::Accessor;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-Ajax-0.697/blib/lib';
  use CGI::Ajax;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-4.35/lib';
  use CGI;

BEGIN{
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
}



   open (MYOUT, ">MYOUT");
   print MYOUT $ENV{'QUERY_STRING'};
   print MYOUT "\n";


  print "Content-type: text/html\n\n";

    # create a CGI object (query) for use
    my $q = CGI->new;
    my $myFunc   = $q->param('myfunc');
    print MYOUT "myFunc=$myFunc";
    # get the category of merchandise

    # get the list of items for the category
    my $thelist, my $line, my $cat;
    if ($myFunc eq "category") {
        my $category = $q->param('category');
        #my @values  = $q->param('testcase');
        print MYOUT "category is: $category";

   	open(myprods, "<cgi-bin/products") || die "Can't open products: $!\n";
   	#@newarray = <myprods>;
   	#print "NEWARRAY @newarray";
	foreach $line (<myprods>) {
    		chomp $line;
		($cat, $thelist) = split(/:/,$line);
    		if($cat eq $category){
		 	print "$thelist";
   	 		close (myprods);
		 	exit;
		}
	}
        print "Category $category not found";
    }
    if ($myFunc eq "items") {
	# my @items  = $q->multi_param('items');
        # print MYOUT "MY ITEMS: @items";
	# print @items;
	my $items  = $q->param('items');
        print MYOUT "MY ITEMS: $items";
	#print $items;
	my @itemsOrdered = split(/;/,$items);
	my $cnt=1;
 	my $thisItem;
	foreach $thisItem (@itemsOrdered) {
		print "invoice$cnt: $thisItem <br>";
		$cnt++;
	}
      
    }

