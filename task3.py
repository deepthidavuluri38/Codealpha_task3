import pandas as pd
import matplotlib.pyplot as plt

# Sample Sales Dataset
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Sales': [50000, 30000, 20000, 55000, 35000],
    'Quantity': [5, 10, 4, 6, 12]
}

df = pd.DataFrame(data)

# Bar Chart
plt.bar(df['Product'], df['Sales'])
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Pie Chart
plt.pie(df['Sales'], labels=df['Product'], autopct='%1.1f%%')
plt.title("Sales Distribution")
plt.show()

# Line Chart
plt.plot(df['Product'], df['Sales'], marker='o')
plt.title("Product Sales Trend")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Histogram
plt.hist(df['Sales'])
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
