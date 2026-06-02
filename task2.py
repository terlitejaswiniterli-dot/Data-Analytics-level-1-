import pandas as pd

df = pd.read_csv("C:\\Users\\terli\\OneDrive\\Desktop\\internship\\Dataset .csv")
df.columns = df.columns.str.strip()
city_counts = df['City'].value_counts()

top_city = city_counts.idxmax()
restaurant_count = city_counts.max()

print("City with the Most Restaurants:")
print(f"{top_city} : {restaurant_count} restaurants")
avg_ratings = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
print("\nAverage Rating by City:")
print(avg_ratings)
highest_rated_city = avg_ratings.idxmax()
highest_rating = avg_ratings.max()

print("\nCity with Highest Average Rating:")
print(f"{highest_rated_city} : {highest_rating:.2f}")