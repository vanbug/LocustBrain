#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# decalarations
my @buglist;
my $infile = "/tmp/sessions.txt";
my $line;
my $everyline;
my $i=0;
my $session;
my @session;
my @ecVoltage;
my @show;
my $start;
my @start;
my @start1;
my $match;
my @module;
#my $start1;
system("bugsess list >/tmp/sessions.txt");
# basic html starts for outputting



print "Content-Type: text/html\n\n";
print "<html>";
print "<title>";
print "Flexible spreadsheet";
print "</title>";
# Adding Elements to html form dynamically
print <<END_HTML;
<HTML>
<HEAD>
<TITLE>Dynamically add Textbox, Radio, Button in html Form using JavaScript</TITLE>
<SCRIPT language="javascript">
function add(type) {
//Create an input type dynamically.
var element = document.createElement("input");
//Assign different attributes to the element.
element.setAttribute("type",type);
element.setAttribute("value", type);
element.setAttribute("name", type);
var foo = document.getElementById("fooBar");
//Append the element in page (in span).
foo.appendChild(element);
}
</SCRIPT>
</HEAD>
<BODY>
<FORM>
<H2>Dynamically add element in form.</H2>
Select the element and hit Add to add it in form.
<BR/>
<SELECT name="element">
<OPTION value="button">Button</OPTION>
<OPTION value="text">Textbox</OPTION>
<OPTION value="radio">Radio</OPTION>
</SELECT>
<INPUT type="button" value="Add" onclick="add(document.forms[0].element.value)"/>
<span id="fooBar">&nbsp;</span>
</FORM>
</BODY>
</HTML>
END_HTML

print "<body>";

print '<form action="ask.cgi" method="post">';


#print <<END_HTML;
#<input type="text" name="query" value="Query" id="queryString">
#<input type="button" name="ask" value="Ask" onclick="askQuery()">
#</form>
#<div id="showSession"></div>
#<div id="showQuery"></div>
#</body>
#</html>
#END_HTML

print '<table border="1">';
print "<tr>";
print "<td>";
print "Session Name</td>";
print "<td>Start Time</td>";
print "<td>";
print "Modules Run</td>";
print "</tr>";
@buglist = `bugsess list -m`;

foreach $line (@buglist)
{
$line =~ /(\w{1,6})/;
$session[$i]=$1;

@show = `bugsess show $1`;
system("bugsess show $1 >>/tmp/show.txt");
foreach $everyline (@show)
{
if($everyline =~ /^Start\stime:\s\w+\s(\w+\s+\d+\s+)\d+\W+\d+\W\d+\s+\w+(\s+\d+.+)/mgis) {
  $start[$i]=$1;
  $start1[$i]=$2;
}
if($everyline =~ /^Modules\s\w+\W(.+)/) {
     $module[$i]=$1;
}

#print $3;
}

print "<tr>";
print '<td id="sessNm'.$i.'">'.$session[$i].'</td>';
print '<td id="sessDt'.$i.'">'.$start[$i].$start1[$i].'</td>';
print '<td id="sessMd'.$i.'">'.$module[$i].'</td>';
print "</tr>";
$i++;
}

print "</table>";
print "</body>";
print "</html>";