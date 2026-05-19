import pandas as pd

data= {

    "name" : ["Ahmed" , "Ali" , "Omar"], 
    "salary" : [2000, 4000 , 7000]
}

df = pd.DataFrame(data)

df["salary_after_tax"] = df["salary"] * 0.9

df.to_csv("output.csv" , index=False)

print("ETL Process Completed")