import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\terli\\OneDrive\\Desktop\\internship\\Dataset .csv")
df.columns = df.columns.str.strip()

price_counts = df['Price range'].value_counts().sort_index()
percentages = (price_counts / len(df)) * 100
print("Price Range Distribution:\n")

result = pd.DataFrame({
    'Price Range': price_counts.index,
    'Restaurant Count': price_counts.values,
    'Percentage (%)': percentages.values
})

print(result)
#Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(price_counts.index, price_counts.values)
plt.title("Distribution of Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.xticks(price_counts.index)
plt.show()