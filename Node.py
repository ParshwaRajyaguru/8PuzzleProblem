class Node:
	#One-Dimentional array of type list which store Node object
	puzzle = []

	#List of type Node
	children = []

	#Store index of puzzle array at which empty slot 0 is assign 
	index = 0


	def __init__(self, puzzleArray, parent=None):
		self.puzzle = puzzleArray
		self.parent = parent



	# Check whether current state id goal state
	def goalTest(self):
		m = self.puzzle[0]

		for i in range(1, 9):
			if m > self.puzzle[i]:
				return False
			m = self.puzzle[i]

		return True
	


	# Print puzzle board
	def printPuzzle(self):
		i = 0
		for x in range(3):
			for y in range(3):
				print (self.puzzle[i], end = " ")
				i = i+1
			print()
		


	# Function convert Node object to List object
	def convertNodeToList(self):
		li = []
		for i in range(9):
			li.append(self.puzzle[i])
		return li



	# def isEqualPuzzle(self, p):
	# 	for i in range(9):
	# 		if(self.puzzle[i] != p[i]):
	# 			return False

	# 	return True



	# Take Right move
	def moveRight(self, p, ind):
		if (ind%3) < 2:
			newPuzzleArray = []

			for i in p:
				newPuzzleArray.append(i)

			temp = newPuzzleArray[ind+1]
			newPuzzleArray[ind+1] = newPuzzleArray[ind]
			newPuzzleArray[ind] = temp

			child = Node(newPuzzleArray)
			self.children.append(child)
			child.parent = self

	

	# Take Left move
	def moveLeft(self, p, ind):
		if (ind%3) > 0:
			newPuzzleArray = []

			for i in p:
				newPuzzleArray.append(i)

			temp = newPuzzleArray[ind-1]
			newPuzzleArray[ind-1] = newPuzzleArray[ind]
			newPuzzleArray[ind] = temp

			child = Node(newPuzzleArray)
			self.children.append(child)
			child.parent = self



	# Take Up move
	def moveUp(self, p, ind):
		if (ind-3) >= 0:
			newPuzzleArray = []

			for i in p:
				newPuzzleArray.append(i)

			temp = newPuzzleArray[ind-3]
			newPuzzleArray[ind-3] = newPuzzleArray[ind]
			newPuzzleArray[ind] = temp

			child = Node(newPuzzleArray)
			self.children.append(child)
			child.parent = self



	# Take Down move
	def moveDown(self, p, ind):
		if (ind+3) < 9:
			newPuzzleArray = []
			for i in p:
				newPuzzleArray.append(i)

			temp = newPuzzleArray[ind+3]
			newPuzzleArray[ind+3] = newPuzzleArray[ind]
			newPuzzleArray[ind] = temp

			child = Node(newPuzzleArray)
			self.children.append(child)
			child.parent = self



	def expandNode(self):
		for i in range(9):
			if(self.puzzle[i] == 0):
				self.index = i

		Node.moveRight(self, self.puzzle, self.index)
		Node.moveLeft(self, self.puzzle, self.index)
		Node.moveUp(self, self.puzzle, self.index)
		Node.moveDown(self, self.puzzle, self.index)