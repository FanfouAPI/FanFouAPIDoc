#!/usr/bin/env perl
use strict;

my $has_table = 0;

while(<>) {
    s/\\_/_/g;
    if(/^\|/) {
	my $a = "$'";
	if($has_table == 0) {
	    print '<table>';
	}
	$has_table++;
	print '<tr>';
	while($a =~ /(.*?)\|/){
	    print '<td>' . $1 . '</td>';
	    $a = "$'";
	}
	print "</tr>\n";
    } else {
	if($has_table >0) {
	    print "</table>\n";
	    $has_table = 0;
	}
	print;
    }
}
