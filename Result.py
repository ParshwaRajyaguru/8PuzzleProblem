from Node import Node
from IdDFS_Search import IDDFS_Search
import time
from BFS_Search import BFS_Search
from Astar_MisplacedTileHeuristic import Astar_Search
from Astar_manhattanDistanceHeuristic import Astar_SearchManhattan


def print_result():
	printResultIDDFS()
	printResultAstarMisplacedTile()
	printResultAstarManhattan()
	printResultBFS()



def printResultIDDFS():
	averageStep = 0
	averageIterator = 0
	averageTime = 0.0

	puzzleArrList = [[4,1,5,2,8,7,3,0,6], [6,3,5,7,2,8,0,1,4], [1,2,5,3,4,8,6,7,0], [1,4,2,6,5,8,7,3,0], [3,1,2,4,7,0,6,8,5], [1,2,5,0,3,8,6,4,7], [3,2,5,4,0,8,6,1,7], [0,2,5,1,4,8,3,6,7], [4,3,5,0,2,8,6,1,7], [1,0,7,3,5,2,6,8,4]]

	it = 1
	for listPuzzle in puzzleArrList:
		print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print ("Solution of Scenario", it, ":")
		it = it+1
		
		start_time = time.time()
	
		root = Node(listPuzzle)
		
		BFSObj = IDDFS_Search()	
		i = BFSObj.IDDFS(root)

		averageStep = averageStep + i[0]
		averageIterator = averageIterator + i[1]	
		averageTime = averageTime + (time.time() - start_time)


	print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print ("Test Result for 10 Input:")
	print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print ()
	print ("\t\t\t\tAverage_Steps\t\t\tAverage_Time\t\t\tAverage_Iterations")
	print ()
	print ("IDDFS\t\t\t\t", (averageStep/(len(puzzleArrList))), "\t\t  ", (averageTime/(len(puzzleArrList))), "\t\t\t", (averageIterator/(len(puzzleArrList))))
	print ()



def printResultBFS():
	averageStep = 0
	averageIterator = 0
	averageTime = 0.0

	puzzleArrList = [[1,2,5,3,4,8,6,7,0], [1,4,2,6,5,8,7,3,0], [3,1,2,4,7,0,6,8,5], [1,2,5,0,3,8,6,4,7], [3,2,5,4,0,8,6,1,7], [0,2,5,1,4,8,3,6,7], [4,3,5,0,2,8,6,1,7], [1,0,7,3,5,2,6,8,4]]

	for listPuzzle in puzzleArrList:
		start_time = time.time()
	
		root = Node(listPuzzle)

		BFSObj = BFS_Search()	
		i = BFSObj.BFS(root)

		averageStep = averageStep + i[0]
		averageIterator = averageIterator + i[1]	
		averageTime = averageTime + (time.time() - start_time)
		
	print ("BFS\t\t\t\t", (averageStep/(len(puzzleArrList))), "\t\t  ", (averageTime/(len(puzzleArrList))), "\t\t\t", (averageIterator/(len(puzzleArrList))))



def printResultAstarManhattan():
	averageStep = 0
	averageIterator = 0
	averageTime = 0.0

	puzzleArrList = [[1,2,5,3,4,8,6,7,0], [1,4,2,6,5,8,7,3,0], [3,1,2,4,7,0,6,8,5], [1,2,5,0,3,8,6,4,7], [3,2,5,4,0,8,6,1,7], [0,2,5,1,4,8,3,6,7], [4,3,5,0,2,8,6,1,7], [1,0,7,3,5,2,6,8,4]]
	
	for listPuzzle in puzzleArrList:
		start_time = time.time()
	
		root = Node(listPuzzle)

		AstarObj = Astar_SearchManhattan()	
		i = AstarObj.AstarSearchManhattan(root)

		averageStep = averageStep + i[0]
		averageIterator = averageIterator + i[1]	
		averageTime = averageTime + (time.time() - start_time)
		
	print ("A*(Manhattan)\t\t\t", (averageStep/(len(puzzleArrList))), "\t\t", (averageTime/(len(puzzleArrList))), "\t\t\t", (averageIterator/(len(puzzleArrList))))
	print ()




def printResultAstarMisplacedTile():
	averageStep = 0
	averageIterator = 0
	averageTime = 0.0

	
	puzzleArrList = [[1,2,5,3,4,8,6,7,0], [1,4,2,6,5,8,7,3,0], [3,1,2,4,7,0,6,8,5], [1,2,5,0,3,8,6,4,7], [3,2,5,4,0,8,6,1,7], [0,2,5,1,4,8,3,6,7], [4,3,5,0,2,8,6,1,7], [1,0,7,3,5,2,6,8,4]]
	
	for listPuzzle in puzzleArrList:
		start_time = time.time()
	
		root = Node(listPuzzle)

		AstarObj = Astar_Search()	
		i = AstarObj.AstarSearchMisplacedTile(root)

		averageStep = averageStep + i[0]
		averageIterator = averageIterator + i[1]	
		averageTime = averageTime + (time.time() - start_time)
		
	print ("A*(Misplaced)\t\t\t", (averageStep/(len(puzzleArrList))), "\t\t", (averageTime/(len(puzzleArrList))), "\t\t\t", (averageIterator/(len(puzzleArrList))))
	print ()
	



print_result()