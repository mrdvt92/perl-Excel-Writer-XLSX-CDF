use strict;
use warnings;
use File::Temp qw{tempfile};

use Test::More tests => 1;
BEGIN { use_ok('Excel::Writer::XLSX::CDF') };

my $e        = Excel::Writer::XLSX::CDF->new(chart_title => "", chart_x_label => "", chart_y_label => "", chart_legend_display=>0);
my @data     = map {
                    [ one => rand            ],
                    [ two => int(10*rand)/10 ],
                   } (1 .. 1000);
my $filename = $e->generate_file(\@data);

diag("Created: $filename");
