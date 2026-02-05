import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(10)
values = np.concatenate([np.random.lognormal(10, 0.5, 1000), [1e7, 2e7]])
df = pd.DataFrame({"income": values})

def iqr_bounds(series, factor=1.5):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR
    return lower, upper

def detect_outliers_iqr(series, factor=1.5):
    lower, upper = iqr_bounds(series, factor)
    return (series < lower) | (series > upper)

df['outlier_iqr'] = detect_outliers_iqr(df['income'])
print("Number of IQR outliers:", df['outlier_iqr'].sum())

def detect_outliers_zscore(series, threshold=3):
    z_scores = np.abs(stats.zscore(series))
    return z_scores > threshold

df['outlier_zscore'] = detect_outliers_zscore(df['income'])
print("Number of z-score outliers:", df['outlier_zscore'].sum())

df['income_no_handling'] = df['income']

lower, upper = iqr_bounds(df['income'])
df['income_iqr_capped'] = df['income'].clip(lower, upper)

df['income_log1p'] = np.log1p(df['income'])

print(df[['income_no_handling', 'income_iqr_capped', 'income_log1p']].describe())
