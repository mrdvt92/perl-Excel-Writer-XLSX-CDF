# NAME

Excel::Writer::XLSX::CDF - Generates Excel Document with Continuous Distribution Function Chart

# SYNOPSIS

    use Excel::Writer::XLSX::CDF;
    my $writer   = Excel::Writer::XLSX::CDF->new(
                                                 chart_title      => "My Title",
                                                 group_names_sort => 1,
                                                );
    my @data     = (
                    [group_name_A => 0.11], #group name is used to label the chart series
                    [group_name_A => 0.21],
                    [group_name_A => 0.31],
                    [group_name_A => 0.41],
                    [group_name_B => 0.07],
                    [group_name_B => 0.13],
                    [group_name_Z => 0.10],
                   );
    my $blob     = $writer->generate(\@data);      #returns Excel File in memory
    my $filename = $writer->generate_file(\@data); #returns Excel File in tmp folder

# DESCRIPTION

Generates Excel Document with Continuous Distribution Function Chart from the supplied data.

# CONSTRUCTOR

## new

    my $writer    = Excel::Writer::XLSX::CDF->new(
                                             chart_title      => "Continuous Distribution Function (CDF)",
                                             chart_y_label    => "Probability",
                                             chart_x_label    => "",
                                             chart_x_min      => "auto", #defalut: undef => calculated by this package
                                             chart_x_max      => "auto", #default: undef => calculated by this package
                                             group_names_sort => 0,      #default: 0     => order of appearance in data
                                            );

# PROPERTIES

## chart\_title

Set and returns the title of the Excel chart

    $writer->chart_title("My Chart Title");

Default: Continuous Distribution Function (CDF)

## chart\_y\_label

Set and returns the Y axis label of the Excel chart

    $writer->chart_y_label("Y Axis Label");

Default: Probability

## chart\_x\_label

Set and returns the X axis label of the Excel chart

    $writer->chart_x_label("X Axis Label");

Default: ""

## chart\_x\_max

Set and returns the X axis max value of the Excel chart

    $writer->chart_x_max(undef);  #calculated by this package
    $writer->chart_x_max(123);    #set set_x_axis max to number
    $writer->chart_x_max("auto"); #set to auto for Excel to estimate

Default: undef

## chart\_x\_min

Set and returns the X axis min value of the Excel chart

    $writer->chart_x_min(undef);  #calculated by this package
    $writer->chart_x_min(123);    #set set_x_axis min to number
    $writer->chart_x_min("auto"); #set to auto for Excel to estimate

Default: undef

## chart\_legend\_display

Set and returns the legend display property for the Excel chart

    $writer->chart_legend_display(0);

Default: 1

## chart\_colors

Set and returns an array reference of Excel color codes to use for each CDF in group order.  The default color once all colors are used is black.

    $writer->chart_colors([]); #set to all black
    $writer->chart_colors([reverse map {"#$_$_$_$_$_$_"} 1 .. 9, 'A' .. 'E']); #gray scale

Default: \['#FF0000', '#800000', '#FFFF00', '#808000', '#00FF00', '#008000', '#00FFFF', '#008080', '#0000FF', '#000080', '#FF00FF', '#800080'\]

## group\_names\_sort

Set and returns the alphabetical sort option for the group names.  A true value Perl-wise will sort the group names before generating the Excel Workbook and a false value will use the order in which the groups were discovered in the data to generate the group names order.

    $writer->group_names_sort(1);

Default: 0

# METHODS

## generate

Generates an Excel Workbook in memory and returns the Workbook as a data blob stored in the returned scalar variable.

    my $blob = $writer->generate(\@data);

## generate\_file

Returns Excel file name in temp folder

    use File::Copy qw{move};
    my $filename = $writer->generate_file(\@data);
    move $filename, '.';

# SEE ALSO

[Excel::Writer::XLSX](https://metacpan.org/pod/Excel::Writer::XLSX)

# AUTHOR

Michael R. Davis

# COPYRIGHT AND LICENSE

MIT License

Copyright (c) 2022 Michael R. Davis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
