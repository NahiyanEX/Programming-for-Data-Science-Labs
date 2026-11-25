import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("train.csv")


print("First Five Rows:")
print(df.head())


print("\nDataset Information:")
df.info()


print("\nStatistical Summary:")
print(df.describe())

print("\nColumn Names:")
print(df.columns)


numerical = df.select_dtypes(include='number').columns


categorical = df.select_dtypes(include='object').columns

print("\nNumerical Attributes:")

print(numerical)

print("\nCategorical Attributes:")
print(categorical)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
