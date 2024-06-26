import pandas as pd

# import all as type string
df = pd.read_csv("text.txt", dtype=str)
# or define the data type by Column Name
df = pd.read_csv("text.txt", dtype={"zipcode": str})

# View the data types of your dataframe with dtypes
print(df.dtypes)

# Use the na_values to set custom missing values
print(df[df.zipcode.isna()])

# see errors
df = pd.read_csv('text.txt', error_bad_lines=False, warn_bad_lines=True)
