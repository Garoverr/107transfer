set terminal pngcairo size 800,600 enhanced font 'Verdana,10'
set output 'output.png'
set xlabel 'x'
set ylabel 'y'
set title 'Ma courbe'
set key outside
plot 'output.txt' using 1:2 with lines title 'Courbe 1', \
     'output.txt' using 1:3 with lines title 'Courbe 2'
