#!/usr/bin/perl

# input files for WebGL
# https://people.sc.fsu.edu/~jburkardt/data/tec/tec.html

  use strict;
  use warnings;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/Class-Accessor-0.34/blib/lib';
  use base 'Class::Accessor::Fast';
  use Class::Accessor::Fast;
  use Class::Accessor;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-Ajax-0.697/blib/lib';
  use CGI::Ajax;
  use lib '/home/f/csci/scott/www/cgi-bin/PMS/CGI-4.35/lib';
  use CGI;

  my %values;
   open (STDERR, ">&STDOUT");
   select(STDERR); $| = 1;
   select(STDOUT); $| = 1;
  #my $q = new CGI;
  my $q = CGI->new ;

  print "Content-type: text/html\n\n";
  #print $q->header('text/html'),
  #print "hello\n\n";
  #my @values  = $q->multi_param('QUERY_STRING');
   #$q->CGI::ReadParse(*values);

   my $myPickType = $q->CGI::param('mypicktype');

   my $myFunc = $q->CGI::param('myfunc');
   my $myRunid = $q->CGI::param('myrunid');



if ($myFunc eq "getpicks") {
if ( ( $myPickType eq "run" ) || ( $myPickType eq "display" )) {
  chdir("RUN351");
  my @picknames;
  $picknames[0] = $myPickType; # handler will use first name in the array as type for Picker List
  my $mycnt2 = 1;
  my $inputName2 = "";
  my $somedir2 = ".";
  opendir(DIR, $somedir2) || die "Can't open directory $somedir2: $!";
  my @tmpdat2 = readdir(DIR);

  foreach $inputName2 (@tmpdat2) {
#print "match $mycnt2 $inputName\n";
  #if ($inputName2 =~ m/\./ ) {
  if (!($inputName2 eq ".") && !($inputName2 eq "..") && !($inputName2 eq "files")){
        $picknames[$mycnt2++] = $inputName2;
  }
#print "found $inputName\n";
#print "\n";
  #
  }
  my $utf8_encoded_json_picknames = JSON::encode_json (\@picknames);
  print $utf8_encoded_json_picknames;
  exit;
}
}


if ( $myFunc eq "pickResults") {
}

# Process sendRequest1: 
# Code from exampleWebGL.cgi
# myfunc=execexample&exampleTestCase=' + theTestCase

if ( $myFunc eq "execexample") {

  #require File::Temp;
  #use File::Temp ();
  #$dir = File::Temp->newdir('tempXXXXX');

  # Make a temporary directory for this run
  my $myTestCase = $q->CGI::param('exampleTestCase');
  chomp $myTestCase;

  my $range = 100000;
  my $dirname = int(rand($range));
  #$dirname =  "CS351_tmp" . $dirname . int(rand($range));
  $dirname =  $myTestCase . "/CS351_tmp" . $dirname ;
  mkdir $dirname, 0755;
  #print $dirname . "\n";

  chdir $dirname;

  # Link the data files to this directory
  `ln -s /home/f/csci/scott/www/cgi-bin/DATA/mydata.dat .`;
  `ln -s /home/f/csci/scott/www/cgi-bin/DATA/mydata.dat mydata2.dat`;
  `ln -s /home/f/csci/scott/www/cgi-bin/DATA/mydata.dat mydata3.dat`;

   #`/home/f/csci/scott/www/cgi-bin/TEC360/prog TEC360_inputs.inp >& myOutput`;

  my @dirnames;
  $dirnames[0] = $dirname; # RunID tells browser where the result is
  #$dirnames[1] = "SCOTT";
  my $mycnt1 = 1;
  my $inputName = "";
my $somedir = ".";
opendir(DIR, $somedir) || die "Can't open directory $somedir: $!";
my @tmpdats = readdir(DIR);

foreach $inputName (@tmpdats) {
#print "match $mycnt1 $inputName\n";
if ($inputName =~ m/.*dat$/ ) {
	$dirnames[$mycnt1++] = $inputName;
#print "found $inputName\n";
#print "\n";
}
}


  #my @myNames = exec("ls *.dat");
  #foreach $inputName (@myNames) {
  #foreach $inputName (`ls *.dat`) {
	#chomp $inputName;
 	#$dirnames[0] += "++" + $inputName;
	#$dirnames[$mycnt1++] = $inputName;
  #}
  #print @dirnames;
  #exit;

  my $utf8_encoded_json_dirname = JSON::encode_json (\@dirnames);
  #my $utf8_encoded_json_dirname = JSON::encode_json (\@myNames);
  print $utf8_encoded_json_dirname;
  #my $json_text   = $JSON::json->encode( $dirname );
  #print $json_text ;
  exit;
}


# Encode Vertices and Faces to JSON
# imports encode_json, decode_json, to_json and from_json.
# imports encode_json, decode_json, to_json and from_json.
# simple and fast interfaces (expect/generate UTF-8)


 use constant { true => 1, false => 0 };

 use lib '/home/f/csci/scott/www/cgi-bin/JSON-2.90';
 use lib '/home/f/csci/scott/www/cgi-bin/JSON-2.90/lib';
 use lib::JSON; 
 use JSON::backportPP; 

my @jsonFaces;
my @jsonVertices;

sub doMyParse {

 
#print "HELLO1 \n";

open(tec360, "<mydata.dat") || die "Can't open tec360 dat: $!\n";

#print "HELLO2 \n";

my @newarray = <tec360>;
##print "NEWARRAY $newarray[0] \n";
##print "NEWARRAY $newarray[1] \n";
##print "NEWARRAY $newarray[2] \n";
##print "NEWARRAY $newarray[3] \n";
close (tec360);

my $foundtriangle = false;
my $foundvertex = false;

my $filename="myData";
my $fcnt = 0;
#foreach $line (@newarray) {
#
my $faceCnt = 0;
my $vertexCnt = 0;
my $line = 0;
my $filename2 = 0;
my @vals;

open(myOutfile, ">TEST28FEB2018") || die "Can't open $filename2 : $!\n";

my $cnt = 0;
while ($cnt <= $#newarray) {

        $line = $newarray[$cnt];
        if ( $line =~ /TITLE/ ) {
                $foundtriangle = false;
                #$line = <tec360>;
                #print "c360_surf $cnt  $newarray[$cnt++]; \n";
                $cnt++;
                #print "c360_surf $cnt  $newarray[$cnt++]; \n";
                $cnt++;
                #print "c360_surf $cnt  $newarray[$cnt++]; \n";
                $cnt++;
                $line = $newarray[$cnt++];
                #$line = <tec360>;
                #print "c360_surf $cnt  $line \n";
                #$line = <tec360>;
                #print "c360_surf $cnt  $line \n";
                if ($fcnt > 0) {
                        close($filename2);
                }
                $fcnt++;
                $filename2 = "$filename" . "$fcnt";

                #open(myOutfile, ">$filename2") || die "Can't open $filename2 : $!\n";
        }
        else {
                $cnt++;
        }

        chomp $line;
        #@vals = split(/ .+/, $line);
        $vals[4] = "ScottSpetka";
        @vals = split(/ {1,}/, $line);
        #if ($vals[4] == "") {}
        #if ($vals[4] eq "") {}
        if ( defined $vals[5] ) {
                if ($foundtriangle eq false) {
                        $foundtriangle = true;
                        print myOutfile "TRIANGLES\n";
                }
#geom.vertices.push( new THREE.Vector3( 10, -10, 0 ) );
#geom.faces.push( new THREE.Face3( 0, 1, 2 ) );

                print myOutfile " geom.vertices.push( new THREE.Vector3( $vals[1], $vals[2], $vals[3] ));\n";
		$jsonVertices[$vertexCnt++] = $vals[1] . ";" . $vals[2] . ";" . $vals[3];
        }
        else {
                print myOutfile " geom.faces.push( new THREE.Face3( $vals[1], $vals[2], $vals[3] ));\n";
		$jsonFaces[$faceCnt++] = $vals[1] . ";" . $vals[2] . ";" . $vals[3];
		if (defined $vals[4] ) {
                print myOutfile " geom.faces.push( new THREE.Face3( $vals[2], $vals[3], $vals[4] ));\n";
		$jsonFaces[$faceCnt++] = $vals[1] . ";" . $vals[3] . ";" . $vals[4];
		}
        }
}

}  # end of sub doMyParse

if ( $myFunc eq "faces") {
 #chdir $myRunid;
 chdir "/home/f/csci/scott/www/cgi-bin/DATA";
 doMyParse();
 #print "FACES: ";
 #print @jsonFaces;
 #exit;
 my $utf8_encoded_json_faces = JSON::encode_json (\@jsonFaces);
 print $utf8_encoded_json_faces;
}

if ( $myFunc eq "vertices") {
 #chdir $myRunid;
 chdir "/home/f/csci/scott/www/cgi-bin/DATA";
 doMyParse();
 my $utf8_encoded_json_vertices = JSON::encode_json (\@jsonVertices);
 #$perl_hash_or_arrayref  = decode_json $utf8_encoded_json_text;
 #print "FACES: ", $utf8_encoded_json_faces;
 #print "<br>\n";
 #print "VERTICES ", $utf8_encoded_json_vertices;
 #print "<br>\n";
 print $utf8_encoded_json_vertices;
}

  print "Content-type: text/html\n\n";
    my $q = CGI->new;
    my $value = $q->param('myfunc');
    my $dir = 'cgi-bin/post';
    if($value eq 'updateDisplay'){
        my $name = $q->param('name');
        open(POST,$dir);
        my @lines = <POST>;
        my $out = '';
        foreach my $line (@lines){
            my @everything = split(",",$line);
            if($everything[0] eq $name){
                $out .= $line .= ";" ;
            }
        }
        close(POST);
        print $out;
    }

    if($value eq "topicDisplay"){
        my $topics = $q->param('topics');
        my @topic = split(",",$topics);
        open(POST,$dir);
        my @lines = <POST>;
        my $out = '';
        foreach my $line (@lines){
            my @everything = split(",",$line);
            foreach my $topicd (@topic){
                if($topicd eq $everything[1]){
                $out .= $line .= ";" ;
                }
            }
        }
        close(POST);
        print $out;
    }
    
    if($value eq "postIdea"){
        my $name = $q->param('name');
        my $topic = $q->param('topics');
        my $stuff = $q->param('stuff');
        open(POST,">>",$dir);
	print $topic;
        my $newIdea = "\n" . $name. "," . $topic . "," . $stuff;
        print POST $newIdea;
        my $out= 1;
        print $out;
    }




#Routing
{
    package MyWebServer;

    use HTTP::Server::Simple::CGI;

    use base qw(HTTP::Server::Simple::CGI);

    my %dispatch = (
        '/index.html' => \&resp_index,
        # ...
    );

    sub handle_request {
        my $self = shift;
        my $cgi  = shift;

        my $path = $cgi->path_info();
        my $handler = $dispatch{$path};
        if (ref($handler) eq "CODE") {
            print "HTTP/1.0 200 OK\r\n";
            $handler->($cgi);
        } else {
            print "HTTP/1.0 404 Not found\r\n";
            print $cgi->header,
                $cgi->start_html('Not found'),
                $cgi->h1('Not found'),
                $cgi->end_html;
        }
    }

    sub resp_index {
        my $cgi  = shift;   # CGI.pm object
        return if !ref $cgi;

        my $who = $cgi->param('name');

        print $cgi->header,
            $cgi->start_html("index"),
            $cgi-h1("THIS IS INDEX"),
            $cgi->end_html;
    }
}

my $pid = MyWebServer->new()->background();
print "Use 'kill $pid' to stop server.\n";