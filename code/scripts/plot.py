#import libraries
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import randint


if len(sys.argv)!=2:
   print("ERROR: Invalid number of arguments..")
   print("USAGE: python plot.py /path/to/output/data_file")
else:
   #read in data from CDMS output file
   f = open(sys.argv[1])
   data = []
   #split data into array of arrays
   for line in f:
      data.append(line.strip().split())
   #close CDMS output file
   f.close()

   #split data up by columns
   filename = [row[0] for row in data]
   section = [row[1] for row in data]
   end_time = [row[2] for row in data]
   points_to_average = [row[3] for row in data]
   freq_avg = [row[4] for row in data]
   frequency_slope = [row[5] for row in data]
   frequency_relative_slope = [row[6] for row in data]
   frequency_sum_sq = [row[7] for row in data]
   mass_to_charge = [row[8] for row in data]
   mass_to_charge_std_dev = [row[9] for row in data]
   charge = [row[10] for row in data]
   charge_std_dev = [row[11] for row in data]
   mass = [row[12] for row in data]
   harm2_rel_mag_avg = [row[13] for row in data]
   harm2_rel_mag_std_dev = [row[14] for row in data]
      
   #available colors for scatter plot
   colors = ['b', 'c', 'g', 'm', 'r']
   #available markers for scatter plot
   markers = ['+', 'o', 'x', '*', '^']
   #data to plot
   data = [points_to_average, freq_avg, frequency_slope, frequency_sum_sq, mass_to_charge, mass_to_charge_std_dev, charge, charge_std_dev, mass, harm2_rel_mag_avg, harm2_rel_mag_std_dev]
   #labels for data
   labels = ["points_to_average", "freq_avg", "frequency_slope", "frequency_sum_sq", "mass_to_charge", "mass_to_charge_std_dev", "charge", "charge_std_dev", "mass", "harm2_rel_mag_avg", "harm2_rel_mag_std_dev"]
      
   #create all possible scatter plots
   for x in range(len(data)):
      for y in range(x+1, len(data)):
         fig, ax = plt.subplots()
         ax.scatter(data[x], data[y], color=colors[randint(0, len(colors)-1)], marker=markers[randint(0, len(markers)-1)])
         ax.ticklabel_format(axis='y', style='sci', scilimits=(-2,3))
         ax.ticklabel_format(axis='x', style='sci', scilimits=(-2,3))
         fig.suptitle('CDMS Hadoop Results (Test Dataset)', fontsize=12)
         plt.xlabel(labels[x], fontsize=10)
         plt.ylabel(labels[y], fontsize=10)
         fig.savefig("plot"+str(x)+"-"+str(y)+".png")
         plt.close(fig)            
