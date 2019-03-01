import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.DataFrame()
df = pd.read_csv("/Users/jjoergens/Desktop/Chicago_Energy_Benchmarking.csv", thousands=',')

x = df['Data Year'].unique()

# y = df.groupby(['Data Year']).groupby(['Primary Property Type']).mean()

y = df.groupby('Primary Property Type')['Electricity Use (kBtu)'].mean()

n = df['Primary Property Type'].nunique()
fig, ax = plt.subplots()

new_x = [10*i for i in np.arange(n)]

ax.barh(new_x,y, tick_label=df['Primary Property Type'].unique(), height=1, log=True, align='center')
plt.ylabel('Property Type')
ax.yaxis.set_label_position("right")
plt.xlabel('Electricity Use (kBtu)(log)')
plt.title("Average Energy Use by Building Type")

plt.savefig("energy_by_type")


