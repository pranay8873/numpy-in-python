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
},index=["E101", "E102", "E103", "E104", "E105"])

print("Employees DataFrame:")
print(employees)
df2=pd.DataFrame(np.array([arr,arr]),columns=['A','B','C','D','E'])
print(df2)
print(employees[['Name','Salary']])
print(employees.shape)
print(employees.size)
print(employees.ndim)
print(employees.columns)
print(employees.dtypes)
print(employees['Name'])
print(employees[['Name', 'Salary']])
print(employees.iloc[0:3])
print(employees.iloc[[-1, -2]])
print(employees.iloc[[-1,-2], [3,4]])
print(employees[employees['Department'] == 'IT'])
print(employees[employees['Department'] == 'HR'])
print(employees[employees['Salary'] > 50000])
print(employees[employees['Salary'] < 50000])
print(employees[employees['Age'] > 27])
print(employees[employees['Age'] < 25])
print(employees[(employees['Salary'] > 50000) & (employees['Age'] < 30)])
print(employees[(employees['Department'] == 'IT') | (employees['Department'] == 'HR')])
print(employees[((employees['Salary']<75000) & (employees['Salary']>45000))])
print(employees[~(employees['Salary']>50000)])
print(employees.loc['E101'])
print(employees.loc['E103'])
print(employees.loc['E103',['Salary']])
print(employees.loc['E102',['Name','Salary']])
print(employees[employees['Salary'].isin([45000, 70000])])

df3=pd.DataFrame({
    "name":["pranay","venketesh","sounik","balaganesh","sravya"],
    "Gender":["male","male","male","female","female"],
    "Age": [21, 25, 19, 30, 23],
    "Salary": [50000, 80000, 40000, 90000, 60000],
    "City": ["Hyderabad", "Mumbai", "Delhi", "Hyderabad", "Chennai"]
})
print(df3)
print(df3[df3["City"].isin(["Hyderabad","Mumbai"])])
print(df3[df3["Gender"].isin(["male","female"])])
print("between : ")
print(df3[df3["Salary"].between(50000,100000)])
print("neither : ")
print(df3[df3["Salary"].between(50000,100000,inclusive='neither')])
print("right : ")
print(df3[df3["Salary"].between(50000,100000,inclusive='right')])
print("left : ")
print(df3[df3["Salary"].between(50000,100000,inclusive='left')])
print("both : ")
print(df3[df3["Salary"].between(50000,100000,inclusive='both')])
#query
print("query in pandas")
print(df3.query("Salary>20000"))
print(df3.query("Salary>20000 &Salary<50000"))
print(df3.query("Salary>20000 &Salary<50000&Gender=='male'"))
print(df3.query("30000<=Salary<=50000"))
df4=df3[["name","City","Salary"]].where(df3["Gender"]=='male')
print(df4)
print("where filter :")
print(df3.where(df3["Salary"]>50000))
print("mask filter : ")
print(df3.mask(df3["Salary"]>50000))








