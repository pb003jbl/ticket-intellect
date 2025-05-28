import pandas as pd

data = {
 'priority': ['1 - Critical', '2 - High', '4 - Low', '3 - Moderate']
}

df = pd.DataFrame(data)
print(df)


def standardize_priority(df, column_name='priority'):
 priority_mapping = {
 '1-critical':1, '1':1, 'critical':1,
 '2-high':2, '2':2, 'high':2,
 '3-moderate':3, '3':3, 'moderate':3,
 '4-low':4, '4':4, 'low':4
 }

 df[column_name] = df[column_name].astype(str).str.replace(' ','').str.strip().str.lower()
 df[column_name] = df[column_name].apply(lambda x: priority_mapping.get(x, x))
 
 # try to convert to numeric
 df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
 
 return df

df = standardize_priority(df)
print(df)