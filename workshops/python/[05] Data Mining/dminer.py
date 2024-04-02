from typing import List, Tuple, Set
from itertools import combinations
import pandas as pd

def power_set(S:Set) -> Set:
    cardinal = len(S)
    masks = [1 << i for i in range(cardinal)]
    for i in range(1, 1 << cardinal):
        yield {ss for mask, ss in zip(masks, S) if i & mask}

def is_valid(value):
    if value is None or pd.isna(value):
        return False
    return True

class Miner:
    def __init__(self, data:pd.DataFrame, min_support=0.0, min_confidence=0.0):
        self.data = data
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.__header = data.columns.equals(pd.RangeIndex(start=0, stop=len(data.columns)))

    def __normalized(self, value):
        if value == 0 or value == False:
            return 0
        if value == 1 or value == True:
            return 1

    def __contains(self, X:Set, i:int) -> bool:
        if self.__header == None or self.__header == False:
            return X.issubset(self.data.iloc[i])
        else:
            r, s = self.data[list(X)].iloc[i], 0
            for j in range(len(r)):
                s += self.__normalized(r[j])

            return s == len(X)

    def __count(self, X:Set) -> int:
        count = 0
        for i in range(len(self.data)):
            if (self.__contains(X, i)):
                count += 1

        return count
    
    def frequents(self) -> Set:
        if self.__header == False:
            return set(self.data.columns)
        
        freqs = set()
        for i in range(len(self.data)):
            record = self.data.iloc[i]
            for j in range(len(record)):
                item = record[j]
                if is_valid(item):
                    freqs.add(item)

        return freqs

    def support(self, X:Set) -> float:
        return self.__count(X) / (len(self.data))
    
    def confidence(self, X:Set, Y:Set) -> float:
        return self.support(X | Y) / self.support(Y)
    
    def lift(self, X:Set, Y:Set) -> float:
        return self.support(X | Y) / (self.support(X) * self.support(Y))
    
    def association_rules(self, X:Set) -> pd.DataFrame:
        rules = power_set(X)
        frequent_items = { 'itemsets': [], 'support' : [] }

        for r in rules:
            r_support = self.support(r)
            if (r_support >= self.min_support):
                frequent_items['itemsets'].append(r)
                frequent_items['support'].append(r_support)

        return pd.DataFrame(frequent_items)