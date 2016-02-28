use warnings;
use strict;
use 5.22.0;

sub is_nice {
    (my $str) = @_;
    my $retval = 0;
    my @vowels = $str =~ /([aeiou])/g;
    my @repeated_letters = ();
    my @repeated_letters = $str =~ /([a-zA-Z])\1/g;

    my $n = scalar(@vowels);
    my $m = scalar(@repeated_letters);

    $retval = 1 if ($n >= 3 and $m >= 1);
    $retval = 0 if ($str =~ /(ab|cd|pq|xy)/g);
    return $retval;
}

if (@ARGV) {
    my @nice_strings = ();
    open my $fh, '<', $ARGV[0];
    while (my $line = <$fh>) {
        next if (!$line);
        chomp $line;
        say $line;
        push @nice_strings, $line if is_nice $line;
    }
    say scalar(@nice_strings);
} else {
    say "Please specify a filename."
}
