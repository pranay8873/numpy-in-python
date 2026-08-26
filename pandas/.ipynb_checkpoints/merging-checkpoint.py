import pandas as pd

jan = pd.DataFrame({
    "Order_ID": ["O101","O102"],
    "Revenue": [1200,800]
})

feb = pd.DataFrame({
    "Order_ID": ["O103","O104"],
    "Revenue": [2100,600]
})

combined=pd.concat([jan,feb],axis=0)#rows
print(combined)
combined=pd.concat([jan,feb],axis=1)#columns
print(f"combined {combined}")
a=pd.DataFrame({"class":['1st','2nd']})
b=pd.DataFrame({"roll_no":[66,99,90,92]})
com=pd.concat([a,b])
print(com)
b=pd.DataFrame({"roll_no":[66,99,90,92],"sec":['a','b','c','d']})

com=pd.concat([a,b],axis=1)
print(com)
sales = pd.DataFrame({
    "Order_ID": ["O101","O102","O103","O104",'0105'],
    "Customer_ID": ["C01","C02","C01","C04",'c06'],
    "Product_ID": ["P01","P02","P03","P01",'p01'],
    "Quantity": [2,1,3,1,5],
    "Revenue": [1200,800,2100,600,3000]
})

customers = pd.DataFrame({
    "Customer_ID": ["C01","C02","C03","C04","C05"],
    "Customer_Name": ["Arun","Priya","Rahul","Sneha","pranay"],
    "City": ["Hyderabad","Chennai","Bengaluru","Hyderabad","Hyderabad"],
    "Segment": ["Retail","Corporate","Retail","Corporate","Delliote"]
})

products = pd.DataFrame({
    "Product_ID": ["P01","P02","P03"],
    "Product": ["Laptop","Monitor","Phone"],
    "Category": ["Electronics","Electronics","Mobile"]
})
mer=pd.merge(sales,customers,on="Customer_ID",how='left')
print(mer)
# print(customers)
mer=pd.merge(sales,customers,on="Customer_ID",how='right')
print(mer)