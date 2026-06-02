import pandas as pd

df = pd.read_csv("C:\\Users\\terli\\OneDrive\\Desktop\\internship\\Dataset .csv")
df.columns = df.columns.str.strip()
cuisine_counts = df['Cuisines'].value_counts()
top_3_cuisines = cuisine_counts.head(3)
total_restaurants = len(df)
print("Top 3 Most Common Cuisines:\n")
for cuisine, count in top_3_cuisines.items():
    percentage = (count / total_restaurants) * 100
    print(f"{cuisine}: {count} restaurants ({percentage:.2f}%)")

result = pd.DataFrame({
    'Cuisine': top_3_cuisines.index,
    'Count': top_3_cuisines.values,
    'Percentage (%)': (top_3_cuisines.values / total_restaurants) * 100
})

print("\nSummary Table:")
print(result)

