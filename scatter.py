import plotly.express as px
import csv

with open('data.csv') as csv_file:
    df = csv.DictReader(csv_file)
    scatter = px.scatter(df,x ="Temparature", y="Ice-cream-Sales")
    scatter.show()