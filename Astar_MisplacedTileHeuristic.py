from Node import Node
import time

class Astar_Search:

	def __init__(self):
		pass



	def AstarSearchMisplacedTile(self, nodeObj):
		step = 0
		iterator = 0

		openSet = []
		closeSet = []

		depthDict = {}
		heuristicDict = {}

		listObj = []

		depth = 0
		heuristicValue = 0

		openSet.append(nodeObj)

		if (nodeObj.goalTest()):
			return (step, iterator)

		listObj = nodeObj.convertNodeToList()
		heuristicValue = self.misplacedTilesHeuristic(listObj)
		depthDict = {nodeObj: depth}
		heuristicDict = {nodeObj: depth + heuristicValue}

		while (len(openSet) != 0):
			iterator = iterator + 1
			currentNode = openSet[0]

			for nodes in openSet:
				if heuristicDict[nodes] < heuristicDict[currentNode]:
					currentNode = nodes

			if (currentNode.goalTest()):
				return (step, iterator)

			openSet.remove(currentNode)
			closeSet.append(currentNode)

			currentNode.expandNode()


			for child in currentNode.children:
				if child.parent == currentNode:
					step = step + 1
					currentChild = child

					depth = depthDict[currentNode] + 1

					if currentChild in closeSet:
						continue

			
					elif currentChild not in openSet or depth < depthDict[currentChild]:
						depthDict[currentChild] = depth

						listObj = currentChild.convertNodeToList()
						heuristicValue = self.misplacedTilesHeuristic(listObj)
						heuristicDict[currentChild] = depthDict[currentChild] + heuristicValue

						if currentChild not in openSet:
							openSet.append(currentChild)

		print ("Goal is not found.")
		return (step, iterator)



	def misplacedTilesHeuristic(self, listObject):
		count = 0
		for i in range(9):
			if listObject[i] != i:
				count = count + 1
		return count


