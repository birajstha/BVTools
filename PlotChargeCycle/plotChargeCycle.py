import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import os

cwd = os.getcwd()

x_values = []
y_values = []

p = os.path.join(cwd, 'actiCHamp.log')

f = open(p, 'r')
for row in f:
    row = row.split(';')
    #print(row)
    x_values.append(row[0])
    y_values.append(float(row[5]))
  
plt.plot(x_values, y_values, color = 'g', label = '- Charge Cycle -')
  
plt.xlabel('Date/Time', fontsize = 12)
plt.ylabel('Voltage', fontsize = 12)

plt.xticks(x_values[::10],  rotation='vertical')
plt.margins(0.02)

plt.title('Charge Cycle', fontsize = 20)
plt.legend()
plt.tight_layout()
plt.show()