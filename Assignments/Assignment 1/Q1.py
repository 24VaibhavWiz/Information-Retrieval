Documents = ["Antony and Cleopatra","Julius Caesar","The Tempest","Hamlet","Othello","Macbeth"]

Antony = [1,1,0,0,1,1]
Brutus = [1,1,0,1,0,0]
Caesar = [1,1,0,1,1,1]
Calpurnia = [0,1,0,0,0,0]
Cleopatra = [1,0,0,0,0,0]
Mercy = [1,0,1,1,1,1]
Worser = [1,0,1,1,1,0]

c1 = [x and y for (x, y) in zip(Brutus,Caesar)]
ncalpurnia = [1,0,1,1,1,1]

c2 = [x and y for (x, y) in zip(c1,ncalpurnia)]

for i in range(len(Documents)):
	if c2[i]==1:
		print(Documents[i])
