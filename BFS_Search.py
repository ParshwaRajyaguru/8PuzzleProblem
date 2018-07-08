from Node import Node
import time

class BFS_Search:

	def __init__(self):
		pass



	def BFS(self, nodeObj):
		currentList = []
		expandedList = []
		step  =1
		iterator = 0
		currentList.append(nodeObj)

		goalFound = False

		while ((len(currentList) > 0) & (goalFound != True)):
			currentNode = currentList[0];
			expandedList.append(currentNode)
			currentList.pop(0)

			if (currentNode.goalTest()):
				return (step, iterator)

			currentNode.expandNode()

			iterator = iterator+1
			
			for i in currentNode.children:
				if i.parent == currentNode:
					step = step + 1
					currentChild = i
				
					if (currentChild.goalTest()):
						return (step, iterator)
					
					# if ((self.isContain(currentList, currentChild) != True) & (self.isContain(expandedList, currentChild) != True)):
					# 	currentList.append(currentChild)
					if ((currentChild not in currentList) & (currentChild not in expandedList)):
						currentList.append(currentChild)

		print ("Goal is not found.")
		return (step, iterator)
