doc1 = "Breakthrough drug for Schizophernia"
doc2 = "New Schizophernia drug"
doc3 = "New approach for treatment of Schizophernia"
doc4 = "New hopes for Schizophernia patients"
doc = [doc1,doc2,doc3,doc4]

data1 = []
data2 = []
data3 = []
data4 = []
data1 = doc1.split()
data2 = doc2.split()
data3 = doc3.split()
data4 = doc4.split()

allData = data1 + data2 + data3 + data4
test_list = list(set(allData))
	print(test_list)
	n = len(test_list)
	k=[]

for x in test_list:
for i in range(len(doc)):

	if x in doc[i]:
		k.append(1)
	else:
		k.append(0)

	matrix = [ k[i:i+4] for i in range(0,len(k),4) ]

for l in matrix:
print(l)
