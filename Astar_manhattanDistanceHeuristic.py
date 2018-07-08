from Node import Node
import time

class Astar_SearchManhattan:

	def __init__(self):
		pass



	def AstarSearchManhattan(self, nodeObj):
		step = 0;
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
		heuristicValue = self.manhattanDistanceHeuristic(listObj)
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
						heuristicValue = self.manhattanDistanceHeuristic(listObj)
						heuristicDict[currentChild] = depthDict[currentChild] + heuristicValue

						if currentChild not in openSet:
							openSet.append(currentChild)

		print ("Goal is not found.")
		return (step, iterator)

	


	def manhattanDistanceHeuristic(self, listObject):
		k = 0
		currentList = [[0,0,0], [0,0,0], [0,0,0]]
		goal = [[0,1,2],[3,4,5],[6,7,8]]

		for i in range(3):
			for j in range(3):
				currentList[i][j] = listObject[k]
				k = k + 1

		sum = 0
		element = 0

		for i in range(3):
  			for j in range(3):
  				element = currentList[i][j]
  				for x in range(3):
  					for y in range(3):
  						if(element == goal[x][y]):
  							sum = sum + abs(i-x) + abs(j-y)

		return sum

