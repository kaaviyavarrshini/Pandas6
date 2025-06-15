import pandas as pd

#Soln1 Using group by
def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store['maxvalue']=store.groupby('customer_id')['amount'].transform('max')
    df=store[store['maxvalue']>500]['customer_id'].unique()
    rich_count=len(df)
    return pd.DataFrame({'rich_count':[rich_count]})

#Soln 2 using nunique
    rich_customers=store[store['amount']>500]
    count=rich_customers['customer_id'].nunique()
    return pd.DataFrame({'rich_count':[count]})