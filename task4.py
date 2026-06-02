import pandas as pd

df = pd.read_csv("C:\\Users\\terli\\OneDrive\\Desktop\\internship\\Dataset .csv")
df.columns = df.columns.str.strip()
total_restaurants = len(df)

delivery_counts = df['Has Online delivery'].value_counts()

yes_percentage = (delivery_counts.get('Yes', 0) / total_restaurants) * 100
print("Online Delivery Analysis\n")
print(f"Restaurants with Online Delivery: {yes_percentage:.2f}%")

avg_rating_yes = df[df['Has Online delivery'] == 'Yes']['Aggregate rating'].mean()
avg_rating_no = df[df['Has Online delivery'] == 'No']['Aggregate rating'].mean()
print("\nAverage Ratings Comparison\n")
print(f"Average Rating (With Online Delivery): {avg_rating_yes:.2f}")
print(f"Average Rating (Without Online Delivery): {avg_rating_no:.2f}")