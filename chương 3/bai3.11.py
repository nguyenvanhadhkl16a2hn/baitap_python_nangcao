import pandas as pd

stocks1 = pd.read_csv('chương 3/stocks1.csv')
print("1a. Head of stocks1:")
print(stocks1.head())
print("\n   Tail of stocks1:")
print(stocks1.tail())
print("\n   Dtype of columns in stocks1:")
print(stocks1.dtypes)
print("\n   Info of stocks1:")
print(stocks1.info())

stocks2 = pd.read_csv('chương 3/stocks2.csv')
print("\n1b. Head of stocks2:")
print(stocks2.head())
print("\n   Tail of stocks2:")
print(stocks2.tail())
print("\n   Dtype of columns in stocks2:")
print(stocks2.dtypes)
print("\n   Info of stocks2:")
print(stocks2.info())

companies = pd.read_csv('chương 3/companies.csv')
print("\n1c. Data of companies:")
print(companies)
print("\n   Dtype of columns in companies:")
print(companies.dtypes)
print("\n   Info of companies:")
print(companies.info())

stocks1['high'].fillna(stocks1.groupby('symbol')['high'].transform('max'), inplace=True)
stocks1['low'].fillna(stocks1.groupby('symbol')['low'].transform('min'), inplace=True)
print("\n2. Null values in stocks1 after replacement:")
print(stocks1.isnull().sum())

stocks = pd.concat([stocks1, stocks2], ignore_index=True)
print("\n3. Tail of merged dataframe 'stocks':")
print(stocks.tail(15))

stocks_companies = pd.merge(stocks, companies, left_on='symbol', right_on='name', how='inner')
print("\n4. Head of merged dataframe 'stocks_companies':")
print(stocks_companies.head())

average_prices = stocks_companies.groupby('name')[['open', 'high', 'low', 'close', 'volume']].mean()
print("\n5. Average prices and volumes for each company:")
print(average_prices)

close_stats = stocks_companies.groupby('name')['close'].agg(['mean', 'max', 'min'])
print("\n6. Close prices stats for each company:")
print(close_stats)

stocks_companies['parsed_time'] = pd.to_datetime(stocks_companies['date'])
print("\n7. Dtype of 'parsed_time' column:")
print(stocks_companies['parsed_time'].dtypes)
print("\n   Head of 'stocks_companies' with 'parsed_time' column:")
print(stocks_companies.head())

stocks_companies['result'] = 'up'
stocks_companies.loc[stocks_companies['close'] <= stocks_companies['open'], 'result'] = 'down'
print("\n8. Head of 'stocks_companies' with 'result' column:")
print(stocks_companies.head())