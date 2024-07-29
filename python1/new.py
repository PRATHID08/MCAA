import module_ListFunction as mlf

list1 = [x for x in range(10)]  
list2 = [x**2 for x in range(10)]  
list3 = [x for x in range(1, 21) if x % 2 == 0]  

print("List1:", list1)
print("Max value in List1:", mlf.find_max(list1))
print("Min value in List1:", mlf.find_min(list1))
print("Sum of List1:", mlf.calculate_sum(list1))
print("Average of List1:", mlf.compute_average(list1))
print("Median of List1:", mlf.determine_median(list1))

print("\nList2:", list2)
print("Max value in List2:", mlf.find_max(list2))
print("Min value in List2:", mlf.find_min(list2))
print("Sum of List2:", mlf.calculate_sum(list2))
print("Average of List2:", mlf.compute_average(list2))
print("Median of List2:", mlf.determine_median(list2))

print("\nList3:", list3)
print("Max value in List3:", mlf.find_max(list3))
print("Min value in List3:", mlf.find_min(list3))
print("Sum of List3:", mlf.calculate_sum(list3))
print("Average of List3:", mlf.compute_average(list3))
print("Median of List3:", mlf.determine_median(list3))
