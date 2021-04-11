import csv
import numpy

temparature = []
ice_cream_sale = []

with open('data,csv') as summer:
    df = csv.DictReader(summer)
    for info in df:
        temparature.append(info["Temperature"])
        ice_cream_sale.append(info["Ice-cream-Sales"])
    
data = {"x": temparature, "y" : ice_cream_sale }
correlation = numpy.corrcoef(data["x"],data["y"])
print(correlation[0,1])