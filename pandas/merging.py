import pandas as pd

sales = pd.DataFrame({
    "Order_ID": ["O101","O102","O103","O104"],
    "Customer_ID": ["C01","C02","C01","C04"],
    "Product_ID": ["P01","P02","P03","P01"],
    "Quantity": [2,1,3,1],
    "Revenue": [1200,800,2100,600]
})

customers = pd.DataFrame({
    "Customer_ID": ["C01","C02","C03","C04"],
    "Customer_Name": ["Arun","Priya","Rahul","Sneha"],
    "City": ["Hyderabad","Chennai","Bengaluru","Hyderabad"],
    "Segment": ["Retail","Corporate","Retail","Corporate"]
})

products = pd.DataFrame({
    "Product_ID": ["P01","P02","P03"],
    "Product": ["Laptop","Monitor","Phone"],
    "Category": ["Electronics","Electronics","Mobile"]
})
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