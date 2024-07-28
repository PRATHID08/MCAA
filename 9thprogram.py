

test_tuple = ('python', 'learn', 'includehelp')

print("The original tuple : " + str(test_tuple))


res = []
for sub in test_tuple:
	N = len(sub) - 1
	res.append(sub[N])


print("The rear index string character list : " + str(res))
