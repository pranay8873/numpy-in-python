import numpy as np
import pandas as pd
data=pd.read_csv("./raw_employee_data.csv")
print(data.info())
print(data["Phone"].dtype)
data["Gender"]=data["Gender"].replace({
    "M":"Male",
    "m":"Male",
    "F":"Female",
    "f":"Female"
})
data["Gender"]=data["Gender"].astype("category")
print(data["Gender"].dtype)
print(data["Department"])
print(data)
data["Age"]=pd.to_numeric(data["Age"],errors="coerce").astype("Int32")
print(data["Age"])
print(data["Age"].dtype)
data["Department"]=data["Department"].str.upper()
print(data["Department"])
data["Salary"]=pd.to_numeric(data["Salary"],errors="coerce").astype("float64")
print(data["Salary"])
print(data["Salary"].dtype)
data["Joining_Date"]=pd.to_datetime(data["Joining_Date"],format="mixed",errors="coerce")
print(data["Joining_Date"])
print(data["Joining_Date"].dtype)
data["City"]=data["City"].str.title()
print(data["City"])
print(data["City"].dtype)
print(data["Email"].dtype)
data["Phone"] = data["Phone"].str.replace(" ", "", regex=False)
print(data["Phone"])
data["Performance_Score"]=data["Performance_Score"].astype("float32")
print(data["Performance_Score"])
print(data["Performance_Score"].dtype)
print(data)
print(data.info())