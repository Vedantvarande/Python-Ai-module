import csv
from matplotlib.pyplot import xlabel, ylabel
import plotly.express as px

rows=[]
with open('Final.csv', 'r') as f:
    csv_r = csv.reader(f)
    for star in csv_r:
        rows.append(star)

headers = rows[0]
star_data = rows[1:]

name = []
distance = []
radius = []
mass = []
gravity = []

for star in star_data:
    name.append(star[1])
    distance.append(float(star[2]))
    mass.append(float(star[3]))
    radius.append(float(star[4]))
    gravity.append(float(star[5]))

fig1 = px.bar(x=name, y=distance, labels={'x':'Star Name', 'y':'Distance in Light Years'})
fig1.show()
fig2 = px.bar(x=name, y=mass, labels={'x':'Star Name', 'y':'Mass'})
fig2.show()
fig3 = px.bar(x=name, y=radius, labels={'x':'Star Name', 'y':'Radius'})
fig3.show()
fig4 = px.bar(x=name, y=gravity, labels={'x':'Star Name', 'y':'Gravity'})
fig4.show()