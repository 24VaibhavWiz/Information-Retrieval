Brutus = [1,2,4,11,31,45,173,174]
Calpurnia = [2,31,54,101]

k = len(Brutus)
l = len(Calpurnia)

def intersection(lst1, lst2):

	lst3 = [value for value in lst1 if value in lst2]
	return lst3

print(intersection(Brutus,Calpurnia))
