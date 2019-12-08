"""
Implementing skipped list (Part 2)
"""
from linkedList import LinkedList
from linkedList import Node
from random import randint

class SkippedList(LinkedList):

## Creating a new linked list with different nodes
	def __init__(self):
		super().__init__()

	def add(self, newItem):
		super().add(newItem, True)

	def main():
	
		arr1 = SkippedList()
		arr2 = SkippedList()
		makeLinkedList(arr1)
		makeLinkedList(arr2)
		skipParameter1 = arr1.length() ** 0.5
		skipParameter2 = arr2.length() ** 0.5
		setPara(arr1, skipParameter1)
		setPara(arr2, skipParameter2)	
		##Printing the linked lists

"""
print("ARR1:", arr1)
print("SKIPS of arr1:")
head = arr1._head
while head:
if head.getSkipPointer():
temp = head.getSkipPointer()
print(temp.getData(), end=" ")
else:
print("None", end=" ")
head = head.getNext()
print("\nARR2:", arr2)
print("SKIPS of arr2:")
head = arr2._head
while head:
if head.getSkipPointer():
temp = head.getSkipPointer()
print(temp.getData(), end=" ")
else:print("None", end=" ")
head = head.getNext()
print()
"""

		intersectWithSkips(arr1, arr2)

	def makeLinkedList(lyst):
	##Making a linked list with randomly (mostly) generated numbers

		number = randint(20, 30)
		for i in range(number):
			lyst.add(randint(1, number*number))
			lyst.add(3)
			lyst.add(20)
			lyst.add(23)

	def intersectWithSkips(lyst1, lyst2):
	## Finding the intersection of two linked lists by making use of skip pointers

		answer = LinkedList()
		head1 = lyst1._head
		head2 = lyst2._head

		while head1 and head2:
			if head1.getData() == head2.getData():
				answer.add(head1.getData())
				head1 = head1.getNext()
				head2 = head2.getNext()
			elif head1.getData() < head2.getData():

			if head1.hasSkip() and head1.getSkipPointer().getData() <= \
				head2.getData():

				while head1.hasSkip() and head1.getSkipPointer().getData() <= \
					head2.getData():
					head1 = head1.getSkipPointer()
			else:
				head1 = head1.getNext()
			else:

				if head2.hasSkip() and head2.getSkipPointer().getData() <= \
					head1.getData():

				while head2.hasSkip() and head2.getSkipPointer().getData() <= \
					head1.getData():
					head2 = head2.getSkipPointer()else:
					head2 = head2.getNext()

					print("Intersecting indices:", end=" ")
					head = answer._head

			while head:
				print(head.getData(), end=" ")
					head = head.getNext()

	def setPara(lyst, para):
	## Taking a previously generated linked list and setting skip pointers
	## for few nodes

		head = lyst._head
		para = int(para)
		count = 0

		while head:
			if count % para == 0:
				node = skip(head, para)
			if node != None:
				head.setSkipPointer(node)
				count += 1
				head = head.getNext()

	def skip(h, p):
	## Returns a node "p" after a current node

		count = 1

		while h and count < p:
			h = h.getNext()
			count += 1
			return h

	if __name__ == "__main__":
		main()
