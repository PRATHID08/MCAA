def find_max(lst):
    if not lst:
        return None
    return max(lst)

def find_min(lst):
    if not lst:
        return None
    return min(lst)

def calculate_sum(lst):
    return sum(lst)

def compute_average(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)

def determine_median(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

if __name__ == "__main__":
    list1 = [x for x in range(10)]  
    list2 = [x**2 for x in range(10)]  
    list3 = [x for x in range(1, 21) if x % 2 == 0]  

    print("List1:", list1)
    print("Max value in List1:", find_max(list1))
    print("Min value in List1:", find_min(list1))
    print("Sum of List1:", calculate_sum(list1))
    print("Average of List1:", compute_average(list1))
    print("Median of List1:", determine_median(list1))

    print("\nList2:", list2)
    print("Max value in List2:", find_max(list2))
    print("Min value in List2:", find_min(list2))
    print("Sum of List2:", calculate_sum(list2))
    print("Average of List2:", compute_average(list2))
    print("Median of List2:", determine_median(list2))

    print("\nList3:", list3)
    print("Max value in List3:", find_max(list3))
    print("Min value in List3:", find_min(list3))
    print("Sum of List3:", calculate_sum(list3))
    print("Average of List3:", compute_average(list3))
    print("Median of List3:", determine_median(list3))
