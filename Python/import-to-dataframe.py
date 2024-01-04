# Read in the multi csv files from the CustomerData_West folder and combine them into one dataframe
import pandas as pd
pd.set_option('display.max_rows', None)
try:
    path = 'C:/Users/User/Documents/pdi-mc-examples/pdi-pentaho/sample-data/customers/CustomerData_West/'
    customer_data_west = pd.concat(map(pd.read_csv, 
                       [path + 'CustomerData_West_Arizono.csv',
                       path + 'CustomerData_West_California.csv',
                       path + 'CustomerData_West_Colorado.csv',
                       path + 'CustomerData_West_Others.csv',
                       path + 'CustomerData_West_Washington.csv']))

    #info shows us the count of entires, column names, and non-null counts
    customer_data_west.info()

    #dtypes shows more info about each column and their data type (object is string and int64 is an integer)
    customer_data_west.dtypes
except Exception as e:
    print(e)

# function to get unique values and their counts for a column in a dataframe in alphabetical order  
def get_unique_values(df, column):
    unique_values = df[column].astype(str).value_counts().sort_index()
    return unique_values
get_unique_values(customer_data_east, 'Age')


# Find NULL values
customer_data_west.isnull().sum()


# Read in the multi csv files from the CustomerData_East folder and combine them into one dataframe
try:
    path = 'C:/Users/User/Documents/pdi-mc-examples/pdi-pentaho/sample-data/customers/'
    customer_data_east = pd.concat(map(pd.read_excel, 
                       [path + 'CustomerData_East.xlsx']))

    customer_data_east.info()
    customer_data_east.dtypes
except Exception as e:
    print(e)

# read tab seperated text file
try:
    path = 'C:/Users/User/Documents/pdi-mc-examples/pdi-pentaho/sample-data/customers/'
    customer_data_central = pd.concat(map(pd.read_table, 
                       [path + 'CustomerData_Central.txt']))

    customer_data_central.info()
    customer_data_central.dtypes
except Exception as e:
    print(e)

# Sort and look for unique values
country_unique_values = customer_data_west['Country'].value_counts().sort_index()
state_unique_values = customer_data_west['State'].value_counts().sort_index()

print("Unique values and their counts for 'Country' column in alphabetical order:")
print(country_unique_values)

print("\nUnique values and their counts for 'State' column in alphabetical order:")
print(state_unique_values)