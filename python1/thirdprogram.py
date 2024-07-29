def merging_dict(*args):
    merged_dict = {}
    for d in args:
        if isinstance(d, dict):
            merged_dict.update(d)
        else:
            raise ValueError("All arguments must be dictionaries")
    return merged_dict

def common_keys(*args):
    if not args:
        return set()
    
    common_keys_set = set(args[0].keys())
    for d in args[1:]:
        common_keys_set.intersection_update(d.keys())
    
    return common_keys_set

def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key
    return inverted_dict

def common_key_value_pairs(*args):
    if not args:
        return {}
    
    common_pairs = set(args[0].items())
    for d in args[1:]:
        common_pairs.intersection_update(d.items())
    
    return dict(common_pairs)


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'c': 3, 'd': 5, 'e': 6}

merged = merging_dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

common_keys_result = common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys_result)

inverted = invert_dict(dict1)
print("Inverted Dictionary:", inverted)

common_pairs = common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_pairs)




