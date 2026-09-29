import matplotlib.pyplot as plt
import seaborn as sns

from main import load_and_clean_data

df = load_and_clean_data()

# Task1: Top 10 localities by average property price

locality_price = df.groupby('locality')['price'].mean()
top_10_localities = locality_price.sort_values(ascending=False).head(10)

# sns.barplot(x=top_10_localities.index, y=top_10_localities.values)
# plt.title('Top 10 Localities by Average Property Price')
# plt.xlabel('Locality')
# plt.ylabel('Average Price')
# plt.xticks(rotation=45)
# plt.show()

# Task 2: Flat Type ke according average rate per sqft
# property_rate= df.groupby('flat_type')['rate_per_sqft'].mean()
# flat_type_avg_per_sqft = property_rate.sort_values(ascending=False)

# sns.barplot(x=flat_type_avg_per_sqft.index, y=flat_type_avg_per_sqft.values)
# plt.title('Flat Type ke according average rate per sqft')
# plt.xlabel("Flat Type")
# plt.ylabel("Average Rate per Sqft")
# plt.show()

# Task 3: Area vs Price

# sns.scatterplot(x='area', y='price', data=df)
# plt.title('Area Vs Price')
# plt.xlabel('Area')
# plt.ylabel("Price")
# plt.show()

# Task4: Area vs Rate per Sqft
sns.scatterplot(x='area', y='rate_per_sqft', data=df)
plt.title('Area Vs Rate per Sqft')
plt.xlabel('Area')
plt.ylabel("Rate per Sqft")
plt.show()