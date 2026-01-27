import pandas as pd

raw = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}

df = pd.DataFrame(raw)


df["price"] = df["price"].apply(
    lambda x: float(x.replace("$", "").replace(",", ""))
)

df["quantity"] = df["quantity"].apply(
    lambda x: 0 if pd.isna(x) else x
)

df["total"] = df["price"].apply(
    lambda x: x
) * df["quantity"].apply(
    lambda x: x
)

df["price_category"] = df["price"].apply(
    lambda x: "low" if x < 600 else "med" if x < 1500 else "high"
)

print(df)
