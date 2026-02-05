import numpy as np
import pandas as pd

raw = {
    "age": [25, "N/A", 40, 33, "?"],
    "income": [50000, 60000, None, "unknown", 80000],
    "churned": [0, 1, 0, 1, 0],
}

df_raw = pd.DataFrame(raw)
df = df_raw.replace(
    ["N/A", "NA", "not reported", "unknown", "?"],
    np.nan
).infer_objects(copy=False)

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["income"] = pd.to_numeric(df["income"], errors="coerce")


def missing_summary(df):
    per_col = df.isna().mean() * 100
    per_row = df.isna().mean(axis=1) * 100
    return per_col, per_row

col_missing, row_missing = missing_summary(df)

print("Per-column missing %:\n", col_missing)
print("\nPer-row missing %:\n", row_missing)


key_cols = ["age", "income"]
df_A = df.dropna(subset=key_cols)
df_B = df.copy()

for col in ["age", "income"]:
    df_B[f"{col}_missing"] = df_B[col].isna().astype(int)
    df_B[col] = df_B[col].fillna(df_B[col].median())

print("\nVersion A row count:", len(df_A))
print("Version B row count:", len(df_B))

print("\nVersion A means:\n", df_A[["age", "income"]].mean())
print("\nVersion B means:\n", df_B[["age", "income"]].mean())

print("\nVersion A churn distribution:\n", df_A["churned"].value_counts())
print("\nVersion B churn distribution:\n", df_B["churned"].value_counts())
