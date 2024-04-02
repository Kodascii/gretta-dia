from typing import List, Tuple, Set
import pandas as pd
import numpy as np
from dminer import *

def self_join(S:Set) -> Set:
    candidates = set()
    frequent = list(S)

    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            candidates.add(tuple(sorted(set(frequent[i]) | set(frequent[j]))))
        #candidates.add(builder_set)

    return candidates

def is_valid(value):
    if value is None or pd.isna(value):
        return False
    return True

def frequents(df:pd.DataFrame):
    _frequents = set()
    for i in range(len(df)):
        record = df.iloc[i]
        for j in range(len(record)):
            item = record[j]
            if is_valid(item):
                _frequents.add(item)

    return _frequents

df_store = pd.read_csv('./store_data.csv', header=None)
df_movies = pd.read_csv('./movies.csv')

products = {
    'Onion':[1,0,0,1,1,1],
    'Potato':[1,1,0,1,1,1],
    'Burger':[1,1,0,0,1,1],
    'Milk':[0,1,1,1,0,1],
    'Beer':[0,0,1,0,1,0]
}
df_products = pd.DataFrame(products)
miner_products = Miner(df_products)

print(miner_products.frequents())