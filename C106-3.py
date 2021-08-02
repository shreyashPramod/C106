import csv
import numpy as np
import plotly.express as py

def getDataSource(data_path):
    size_tv=[]
    tv_average=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            size_tv.append(float(row["Size of TV"]))
            tv_average.append(float(row["Averagetime"]))
    return{"x":size_tv,"y":tv_average}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between Size of Tv and Average time spent watching TV in a week :",correlation[0,1])

def setup():
    data_path="TvAverage.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setup()
   
    

