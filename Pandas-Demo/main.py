import pandas as pd

dataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

# Pandas dataframe (2-D array) table with rows and columns
data = pd.DataFrame(dataset)
# Instead of indexs from 0-n, we add names
df = pd.DataFrame(dataset, index = ["day1", "day2", "day3"]) 
print(df, "\n")

# Locating row name to get data 
print(df.loc["day2"], "\n")

# Create Panda Series (table)
a = [1, 7, 2]
data = pd.Series(a)
print(data, "\n")

# Get data from CSV file
df = pd.read_csv('data.csv')
print(df) 

print(df.head(10)) # First 10 rows
print(df.tail(10)) # Last 10 rows
