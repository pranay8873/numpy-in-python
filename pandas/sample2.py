import pandas as pd
data=pd.read_csv("./Pandas_Day_4_Real_World_Sales_Data.csv")
print(data)
print(data.dtypes)
print(data["Order_Date"].dtype)
print(data["Price"].dtype)
print(data["Order_Date"].map(type).value_counts())
