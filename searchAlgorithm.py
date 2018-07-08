from Node import Node
from IdDFS_Search import IDDFS_Search
import time
from BFS_Search import BFS_Search
from Astar_MisplacedTileHeuristic import Astar_Search
from Astar_manhattanDistanceHeuristic import Astar_SearchManhattan

puzzleArrList = [3,2,5,4,0,8,6,1,7]

print ("Uninformed Search:")
print ("Breadth-first search(BFS) Algorithm:")
root = Node(puzzleArrList)
BFSObj = BFS_Search()	
i = BFSObj.BFS(root)
step = i[0]
iteration = i[1]
print ("Total Number of Iterations in BFS Algorithm: ", iteration)
print ("Total Number of Steps in BFS Algorithm: ", step)
print ()
print ()


print ("Iterative deepening depth-first search(IDDFS) Algorithm: ")
root = Node(puzzleArrList)		
BFSObj = IDDFS_Search()	
i = BFSObj.IDDFS(root)
step = i[0]
iteration = i[1]
print ("Total Number of Iterations in IDDFS Algorithm: ", iteration)
print ("Total Number of Steps in IDDFS Algorithm: ", step)
print ()
print ()



print ("informed A* Search:")
print ("A* search Algorithm with Misplaced Tiles Heuristic:")
root = Node(puzzleArrList)
AstarObj = Astar_Search()	
i = AstarObj.AstarSearchMisplacedTile(root)
step = i[0]
iteration = i[1]
print ("Total Number of Iterations in A* search Algorithm with Misplaced Tiles Heuristic: ", iteration)
print ("Total Number of Steps in A* search Algorithm with Misplaced Tiles Heuristic: ", step)
print ()
print ()


print ("A* search Algorithm with Manhattan Distance Heuristic:")
root = Node(puzzleArrList)
AstarObj = Astar_SearchManhattan()	
i = AstarObj.AstarSearchManhattan(root)
step = i[0]
iteration = i[1]
print ("Total Number of Iterations in A* search Algorithm with Manhattan Distance Heuristic: ", iteration)
print ("Total Number of Steps in A* search Algorithm with Manhattan Distance Heuristic: ", step)
print ()
print ()