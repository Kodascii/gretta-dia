from itertools import combinations

def gen_freq(data, min_sup):
    item_counts = {}
    total_trans = len(data)

    for trans in data:
        for item in trans:
            item_counts[item] = item_counts.get(item, 0) + 1

    freq_1_itemsets = {item for item, count in item_counts.items() if count / total_trans >= min_sup}
    return freq_1_itemsets


def self_join(freq_itemsets_k_minus_1):
    candidates_k = set()
    freq_list = list(freq_itemsets_k_minus_1)

    for i in range(len(freq_list)):
        for j in range(i + 1, len(freq_list)):
            itemset_i, itemset_j = freq_list[i], freq_list[j]

            if itemset_i[:-1] == itemset_j[:-1]:
                candidates_k.add(tuple(sorted(set(itemset_i) | set(itemset_j))))

    return candidates_k


def prune(C_i, L_1):
    pruned_k = set()

    for c in C_i:
        if all(tuple(sorted(subset)) in L_1 for subset in combinations(c, len(c) - 1)):
            pruned_k.add(c)

    return pruned_k


def apriori(data, min_sup):
    L = {}
    L[1] = gen_freq(data, min_sup)

    i = 2
    while L[i - 1]:
        C_i = self_join(L[i - 1])
        L_i = prune(C_i, L[i - 1])

        sup_counts = {}
        for trans in data:
            for itemset in L_i:
                if set(itemset).issubset(set(trans)):
                    sup_counts[itemset] = sup_counts.get(itemset, 0) + 1

        L[i] = {itemset for itemset, count in sup_counts.items() if count / len(data) >= min_sup}
        i += 1

    return L

# Example usage:
dataset = [
    ['A', 'B', 'C'],
    ['A', 'B'],
    ['A', 'C'],
    ['B', 'C'],
    ['A', 'B', 'C', 'D'],
]

min_support = 0.0
result = apriori(dataset, min_support)

# Display the frequent itemsets
for k, itemsets in result.items():
    print(f"Frequent {k}-itemsets:", itemsets)

X = {}
X[0] = {'Hi'}
print(X)