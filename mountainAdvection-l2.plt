set xrange [0:9000]
set yrange [0:0.2]

set style data linespoints

set xlabel "Peak mountain height (m)"
set ylabel "l2 error"

set label "BTF linearUpwind" at 6200,0.08 textcolor rgb "dark-violet"
set label "BTF cubicUpwind" at 6200,0.045 textcolor rgb "dark-violet"
set label "Cut cells linearUpwind" at 6200,0.17 textcolor rgb "#009e73"
set label "Cut cells cubicUpwind" at 6200,0.07 textcolor rgb "#009e73"
set label "Slanted cells linearUpwind" at 5200,0.19 textcolor rgb "#56b4e9"
set label "Slanted cells cubicUpwind" at 6200,0.09 textcolor rgb "#56b4e9"

unset key

plot 'mountainAdvection-btf-linearUpwind-l2.dat' using 1:2 lc 1 lw 1.5 dt 2 ps 2 pt 4, \
     'mountainAdvection-btf-cubicUpwind-l2.dat' using 1:2 lc 1 lw 1.5 dt 1 ps 2 pt 5, \
     'mountainAdvection-cutCell-linearUpwind-l2.dat' using 1:2 lc 2 lw 1.5 dt 2 ps 2 pt 8, \
     'mountainAdvection-cutCell-cubicUpwind-l2.dat' using 1:2 lc 2 lw 1.5 dt 1 ps 2 pt 9, \
     'mountainAdvection-slantedCell-linearUpwind-l2.dat' using 1:2 lc 3 lw 1.5 dt 2 ps 2 pt 6, \
     'mountainAdvection-slantedCell-cubicUpwind-l2.dat' using 1:2 lc 3 lw 1.5 dt 1 ps 2 pt 7
