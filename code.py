import pandas as p
import csv
import plotly.express as px 

df = p.read_csv("data.csv")
studentdf=df.loc[df["student_id"] == "TRL_abc"]
finalResult = studentdf.groupby("level")["attempt"].mean()
print(finalResult)

graph = px.scatter(x=finalResult,y=['level 1','level 2','level 3','level 4'])
graph.show()
