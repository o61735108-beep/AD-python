import pandas as pd


rows = [
    {"user": "U1", "day": "2024-01-01", "product": "A", "clicked": 1},
    {"user": "U1", "day": "2024-01-01", "product": "A", "clicked": 1},
    {"user": "U1", "day": "2024-01-01", "product": "B", "clicked": 0},
    {"user": "U2", "day": "2024-01-02", "product": "A", "clicked": 1},
]

df = pd.DataFrame(rows)
df_no_duplicates = df.drop_duplicates()
print("After removing full duplicates:\n", df_no_duplicates)

df_unique = df_no_duplicates.drop_duplicates(subset=["user", "day", "product"])
print("\nAfter applying uniqueness rule (user, day, product):\n", df_unique)

user_features = df_unique.groupby("user").agg(
    total_clicks=pd.NamedAgg(column="clicked", aggfunc="sum"),
    unique_products=pd.NamedAgg(column="product", aggfunc="nunique")
).reset_index()

print("\nAggregated user-level features:\n", user_features)
