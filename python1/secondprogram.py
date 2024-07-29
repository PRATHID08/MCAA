
import setoperation

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

setoperation.add_element(set1, 5)
print("Set1 after adding 5:", set1)

setoperation.remove_element(set1, 5)
print("Set1 after removing 5:", set1)

union, intersection = setoperation.union_and_intersection(set1, set2)
print("Union of Set1 and Set2:", union)
print("Intersection of Set1 and Set2:", intersection)

difference = setoperation.difference(set1, set2)
print("Difference Set1 - Set2:", difference)

is_subset = setoperation.is_subset(set1, set2)
print("Is Set1 a subset of Set2?", is_subset)

length = setoperation.set_length(set1)
print("Length of Set1:", length)

sym_diff = setoperation.symmetric_difference(set1, set2)
print("Symmetric Difference of Set1 and Set2:", sym_diff)

power_set = setoperation.power_set(set1)
print("Power Set of Set1:", power_set)

unique_subsets = setoperation.unique_subsets(set1)
print("Unique Subsets of Set1:", unique_subsets)

