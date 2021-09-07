import plotly.express as px
import csv
import numpy as np

def getData(datapath):
    cupsofCoffee=[]
    horsofSleep=[]
    with open (datapath)as cvs_file:
        df=csv.DictReader(cvs_file)
        for row in df:
           cupsofCoffee.append(float(row["sleep in hours"])) 
           horsofSleep.append(float(row["Coffee in ml"]))
        return{"x":cupsofCoffee,"y":horsofSleep}
def findCorre(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    data_path="cofvsslee.csv"   
    datasource=getData(data_path)            
    findCorre(datasource)

setup()    