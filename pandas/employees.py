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
