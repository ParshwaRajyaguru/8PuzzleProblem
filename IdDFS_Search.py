from Node import Node
import time

class IDDFS_Search:

	def __init__(self):
		pass


	def printResult(self, treeNode, root):
		l = []
		i = treeNode

		l.append(i)
		while i.parent != root:
			l.append(i.parent)
			i = i.parent

		l.append(root)
		l.reverse()
		loopCount = 0;
	
		for n in l:
			n.printPuzzle()
			if loopCount != len(l)-1:
				print ("to")
			loopCount += 1

		print()
		print()



	def IDDFS(self, nodeObj):
		currentList = []
		expandedList = []
		visitedList = []

		step  =1
		iterator = 0

		visitedList.append(nodeObj)

		if (nodeObj.goalTest()):
			self.printResult(nodeObj, nodeObj)
			return (step, iterator)


		goalFound = False

		while ((len(expandedList) < 362880) & (goalFound != True)):
			while len(visitedList) != 0:
				iterator = iterator + 1
				currentNode = visitedList[0]
				expandedList.append(currentNode)
				visitedList.pop(0)

				currentNode.expandNode()

			
				for i in currentNode.children:
					if i.parent == currentNode:
						step = step + 1
						currentChild = i
				
						if (currentChild.goalTest()):
							self.printResult(currentChild, nodeObj)
							return (step, iterator)

					
						if ((currentChild not in currentList) & (currentChild not in visitedList) & (currentChild not in expandedList)):
							currentList.append(currentChild)

			while len(currentList) != 0:
				visitedList.append(currentList[0])
				currentList.pop(0)
		
		print ("Goal is not found.")
		return (step, iterator)
				