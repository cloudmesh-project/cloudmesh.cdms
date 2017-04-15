import matplotlib.pyplot as plt

f = open("part-00000")
data = []
for line in f:
   data.append(line.strip().split())


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


colors = ['b', 'c', 'g', 'm', 'r']

fig, ax = plt.subplots()
ax.scatter(points_to_average, freq_avg, color=colors[0], marker='o')
fig.suptitle('Charge Detection Mass Spectrometry', fontsize=20)
plt.xlabel('points_to_average', fontsize=16)
plt.ylabel('freq_avg', fontsize=16)
fig.savefig('test1.png')
plt.close(fig)

#good
fig, ax = plt.subplots()
ax.scatter(freq_avg, freq_avg, color=colors[1], marker='x')
fig.suptitle('Charge Detection Mass Spectrometry', fontsize=20)
plt.xlabel('freq_avg', fontsize=16)
plt.ylabel('freq_avg', fontsize=16)
fig.savefig('test2.png')
plt.close(fig)

#good 
fig, ax = plt.subplots()
ax.scatter(frequency_sum_sq, frequency_slope, color=colors[2], marker='^')
fig.suptitle('Charge Detection Mass Spectrometry', fontsize=20)
plt.xlabel('frequency_sum_sq', fontsize=16)
plt.ylabel('frequency_slope', fontsize=16)
fig.savefig('test3.png')
plt.close(fig)

fig, ax = plt.subplots()
ax.scatter(freq_avg, frequency_slope, color=colors[3], marker='o')
fig.suptitle('Charge Detection Mass Spectrometry', fontsize=20)
plt.xlabel('freq_avg', fontsize=16)
plt.ylabel('frequency_slope', fontsize=16)
fig.savefig('test4.png')
plt.close(fig)

fig, ax = plt.subplots()
ax.scatter(mass, frequency_sum_sq, color=colors[4], marker='x')
fig.suptitle('Charge Detection Mass Spectrometry', fontsize=20)
plt.xlabel('mass', fontsize=16)
plt.ylabel('frequency_sum_sq', fontsize=16)
fig.savefig('tes5.png')
plt.close(fig)
