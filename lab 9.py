import pandas as pd

raw = {
    "age": ["25", "30", "unknown"],
    "income": ["$50,000", "$60,000", None],
    "signup": ["2024-01-01", "01/05/2024", "not a date"],
}

df = pd.DataFrame(raw)


def normalize_schema(df):
    df_normalized = df.copy()

    for col in df_normalized.columns:
        if df_normalized[col].astype(str).str.replace(r'[\$,]', '', regex=True).str.isnumeric().any():
            df_normalized[col] = pd.to_numeric(df_normalized[col].astype(str).str.replace(r'[\$,]', '', regex=True),
                                               errors='coerce')
        else:
            df_normalized[col] = pd.to_datetime(df_normalized[col], errors='coerce')

    print("NaN counts after conversion:")
    print(df_normalized.isna().sum())

    return df_normalized


df_clean = normalize_schema(df)
print("\nNormalized DataFrame:")
print(df_clean)
