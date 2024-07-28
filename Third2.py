def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")


n = 5
half_pyramid(n)


my_list = ['abc', 'xyz', 'aba', '1221']

counter = 0
for i in my_list:
    if len(i) > 1:
        if i[0] == i[len(i)-1]: # or if i[0] == i[-1]:
            counter += 1
print(counter)