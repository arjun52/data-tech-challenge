import pandas as pd


df = pd.read_csv('data/AeroConnectData.csv')
#find non-missing values
df.info()

# find missing values
print(f"\n# of missing values:\n{df.isnull().sum()}")



# check total of freight and passengers match. account for floating point error in freights
df['Passengers_Check'] = df['Passengers_In'] + df['Passengers_Out'] - df['Passengers_Total']
df['Freight_Check'] = df['Freight_In_(tonnes)'] + df['Freight_Out_(tonnes)'] - df['Freight_Total_(tonnes)']

print(f"\nPassenger calculation check: {df['Passengers_Check'].ne(0).sum()} errors")
print(f"Freight calculation check): {(abs(df['Freight_Check']) > 0.001).sum()} errors")



# create joint routes column and get uniqueness numbers
df['Route'] = df['AustralianPort'] + ' <-> ' + df['ForeignPort'] + ' (' + df['Country'] + ')'
print(f"\nTotal routes: {df['Route'].nunique()}")
print(f"Unique Australian ports: {df['AustralianPort'].nunique()}")
print(f"Unique foreign ports: {df['ForeignPort'].nunique()}")
print(f"Unique countries: {df['Country'].nunique()}")

# top 5 busiest routes overall
top_routes = df.groupby('Route')['Passengers_Total'].sum().sort_values(ascending=False).head(5)
print(f"\nTop 5 routes with total passengers:")
print(top_routes)


# bottom 5 busiest routes overall
top_routes = df.groupby('Route')['Passengers_Total'].sum().sort_values(ascending=True).head(5)
print(f"\nBottom 5 routes with total passengers:")
print(top_routes)