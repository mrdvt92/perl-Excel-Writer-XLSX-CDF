use strict;
use warnings;
use File::Temp qw{tempfile};

use Test::More tests => 5;
BEGIN { use_ok('Excel::Writer::XLSX::CDF') };

my @data     = map {
                    [ one   => rand            ],
                    [ two   => int(10*rand)/10 ],
                    [ three => int(50*rand)/50 ],
                   } (1 .. 1000);

{
  my $e        = Excel::Writer::XLSX::CDF->new(chart_title => "", chart_x_label => "", chart_y_label => "", chart_legend_display=>0);
  my $filename = $e->generate_file(\@data);
  ok(-r $filename, 'generate_file');
  ok(-s $filename, 'generate_file');
  diag("Created: $filename");
}

{
  my $e        = Excel::Writer::XLSX::CDF->new(
                                               chart_title          => "My Title",
                                               chart_x_label        => "My X Axis",
                                               chart_y_label        => "My Y Axis",
                                               chart_legend_display => 1,
                                               chart_colors         => ['#EE1111', '#11EE11', '#1111EE'],
                                               group_names_sort     => 1,
                                              );
  my $filename = $e->generate_file(\@data);
  ok(-r $filename, 'generate_file');
  ok(-s $filename, 'generate_file');
  diag("Created: $filename");
}
