#!/usr/bin/perl -w

# Who:	Javed A. Aslam
#
# What:	parse.pl
#
# When: 05/15/05
#
# Why:	parse.pl takes a text file as input and parses that file,
#       returning the words contained in that file, one word per line.

if (@ARGV != 1) {
  die "Usage:  parse.pl <filename>\n\n";
  }

$file = shift;                            # Shift implicitly acts on @ARGV.

open(FILE, $file) or
  die "Failed to open $file: $!\n\n";

while(<FILE>) {
  while (/([a-zA-Z]+(?:'[a-zA-Z]+)*)/g) {
    $word = lc $1;
    print "$word\n";
    }
  }

close(FILE) or
  die "Couldn't close $file: $!\n\n";
