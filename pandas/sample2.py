import pandas as pd
data=pd.read_csv("./Pandas_Day_4_Real_World_Sales_Data.csv")
print(data)
print(data.dtypes)
print(data["Order_Date"].dtype)
print(data["Price"].dtype)
print(data["Order_Date"].map(type).value_counts())
data["Order_Date"]=data["Order_Date"].astype("datetime64[ns]")
print(data["Order_Date"].dtype)
print(data['Order_Date'])
values=pd.Series(["100","200","hello"])
print(values.dtype)
print(values)
# values=values.astype("int32")
values=pd.to_numeric(values,errors="coerce")
print(values)
data["reveunue"]=data["Price"]*data["Quantity"]
print(data["reveunue"])
print(f"high cost products : {data[data["Price"]>60000]}")
print(data["Category"].dtype)
data["Category"]=data["Category"].astype("category")
print(data["Category"].dtype)
print(data["Category"].cat.categories)
print(data["Category"].cat.codes)
print(data.memory_usage(deep=True).sum())
from pandas.api.types import (
    is_numeric_dtype,
    is_datetime64_any_dtype,
    is_bool_dtype
)

print(is_numeric_dtype(data["Price"]))
print(is_numeric_dtype(data["Order_Date"]))
data.info()
print(data["Category"].head(8))
#null values handling
import numpy as np
val=pd.Series([10,20,30,np.nan,40])
print(val)
print(data[data["Price"].isna()])
print(data[data["Price"].isnull()])
duplicate=data
print(duplicate)
duplicate.loc[2,"Price"]=np.nan
print(duplicate)
print(duplicate.isna().sum())
mean=duplicate.isna().mean()*100
print(mean)

