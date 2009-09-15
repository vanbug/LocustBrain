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
<TITLE> Add/Remove dynamic rows in HTML table </TITLE>
<SCRIPT language="javascript">
function addRow(tableID) {
       var table = document.getElementById(tableID);
       var rowCount = table.rows.length;
       var row = table.insertRow(rowCount);
       var cell1 = row.insertCell(0);
      	  var element1 = document.createElement("input");
           element1.type = "checkbox";
			  cell1.appendChild(element1);
           var cell2 = row.insertCell(1);
           cell2.innerHTML = rowCount + 1;
           var cell3 = row.insertCell(2);
           var element2 = document.createElement("input");
           element2.type = "text";
           cell3.appendChild(element2);
                  }
function deleteRow(tableID) {
          try {
          var table = document.getElementById(tableID);
          var rowCount = table.rows.length;
          for(var i=0; i<rowCount; i++) {
          var row = table.rows[i];
          var chkbox = row.cells[0].childNodes[0];
               if(null != chkbox && true == chkbox.checked) {
                   table.deleteRow(i);
                   rowCount--;
                   i--;
               }

          }
          }catch(e) {
              alert(e);
           }
        }
 
   </SCRIPT>
</HEAD>
<BODY>
   <INPUT type="button" value="Add Row" onclick="addRow('sessTable')" />

   <INPUT type="button" value="Delete Row" onclick="deleteRow('sessTable')" />
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

print '<table id="sessTable" border="1">';
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

print '<tr id="sessCh'.$i.'">';
print '<td id="sessNm'.$i.'">'.$session[$i].'</td>';
print '<td id="sessDt'.$i.'">'.$start[$i].$start1[$i].'</td>';
print '<td id="sessMd'.$i.'">'.$module[$i].'</td>';
print "</tr>";
$i++;
}

print "</table>";
print "</body>";
print "</html>";