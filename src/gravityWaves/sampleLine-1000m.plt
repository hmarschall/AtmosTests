set style data lines
set key outside top center
set xlabel 'theta'
set x2label 'exner'
set ylabel 'height'
#set xrange [288:298]
#set x2range [0.90:1]
#set yrange [0:3000]
set x2tics

plot 'build/gravityWaves-btf-1000m/18000/exnerTheta-sampleLine.dat' using 3:1 lc 1 title 'BTF theta', \
 'build/gravityWaves-btf-1000m/18000/exnerTheta-sampleLine.dat' using 2:1 axes x2y1 lc 1 dt 2 title 'BTF exner', \
 'build/gravityWaves-sleve-1000m/18000/exnerTheta-sampleLine.dat' using 3:1 lc 2 title 'SLEVE theta', \
 'build/gravityWaves-sleve-1000m/18000/exnerTheta-sampleLine.dat' using 2:1 axes x2y1 lc 2 dt 2 title 'SLEVE exner', \
 'build/gravityWaves-cutCell-1000m/18000/exnerTheta-sampleLine.dat' using 3:1 lc 3 title 'cut cell theta', \
 'build/gravityWaves-cutCell-1000m/18000/exnerTheta-sampleLine.dat' using 2:1 axes x2y1 lc 3 dt 2 title 'cut cell exner'
