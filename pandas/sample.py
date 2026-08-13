import pandas as pd
import numpy as np
arr=np.array([1,2,3,4,5], dtype=np.int32)
s=pd.Series(arr)
print(s)
arr=pd.Series((1,2,3,4,5),dtype=np.int32)
print(arr)
dict={'a':1,'b':2,'c':3}
s=pd.Series(dict)
print(s)
df=pd.DataFrame(np.array([[1,2,3],[4,5,6]]),columns=['A','B','C'])
print(df)
employees = pd.DataFrame({
    "EmpID": ["E101", "E102", "E103", "E104", "E105"],
    "Name": ["Rahul", "Priya", "Arun", "Meena", "Kiran"],
    "Age": [25, 29, 24, 32, 27],
    "Department": ["IT", "HR", "IT", "Sales", "Finance"],
    "Salary": [45000, 55000, 48000, 70000, 85000]
})

print("Employees DataFrame:")
print(employees)
