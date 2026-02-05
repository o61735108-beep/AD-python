import pandas as pd

def fit_imputer(train_df, num_cols, cat_cols):
    params = {
        "num": {col: train_df[col].median() for col in num_cols},
        "cat": {col: train_df[col].mode()[0] for col in cat_cols},
    }
    return params

def transform_imputer(df, params, add_indicators=True):
    df = df.copy()

    for col, value in params["num"].items():
        if add_indicators:
            df[col + "_missing"] = df[col].isna().astype(int)
        df[col] = df[col].fillna(value)

    for col, value in params["cat"].items():
        if add_indicators:
            df[col + "_missing"] = df[col].isna().astype(int)
        df[col] = df[col].fillna(value)

    return df

train = pd.DataFrame({
    "age": [25, None, 40, 33],
    "city": ["NY", "SF", None, "NY"],
})

test = pd.DataFrame({
    "age": [None, 50],
    "city": ["SF", None],
})

num_cols = ["age"]
cat_cols = ["city"]

params = fit_imputer(train, num_cols, cat_cols)

test_with_ind = transform_imputer(test, params, add_indicators=True)
test_no_ind = transform_imputer(test, params, add_indicators=False)

print(test_with_ind)
print(test_no_ind)
