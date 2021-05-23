from collections import deque   #import deque libry to add / remove 

jug1=int(input("Enter jug 01 value:"))  #set input values
jug2=int(input("Enter jug 02 value:"))
result=int(input("Enter result value:"))

def waterJug(jug1, jug2, result):
 #initializing requied variables
	dic = {}
	isTargetReach = False
	jugPath = []
	jugQueue = deque() #assign imported ;library to maintaine the queue
	
	
	jugQueue.append((0, 0))

	while (len(jugQueue) > 0):
		jugCurrent = jugQueue.popleft()   #asign current state to variable
        if ((jugCurrent[0], jugCurrent[1]) in dic):
			continue

		
		if ((jugCurrent[0] > jug1 or jugCurrent[1] > jug2 or
			jugCurrent[0] < 0 or jugCurrent[1] < 0)):
			continue

		
		jugPath.append([jugCurrent[0], jugCurrent[1]])
        dic[(jugCurrent[0], jugCurrent[1])] = 1         # Marking current state as visited

		
		if (jugCurrent[0] == target or jugCurrent[1] == target):
			isTargetReach = True
			if (jugCurrent[0] == target):
				if (jugCurrent[1] != 0):
					
					
					jugPath.append([jugCurrent[0], 0])
			else:
				if (jugCurrent[0] != 0):

					
					jugPath.append([0, jugCurrent[1]])   # Fill final state

		# Print the solution path
			lenPath = len(jugPath)
			for i in range(lenPath):
				print("(", jugPath[i][0], ",",
						jugPath[i][1], ")")
			break

	
		jugQueue.append([jugCurrent[0], jug2]) 
		jugQueue.append([jug1, jugCurrent[1]]) 
        for pour in range(max(jug1, jug2) + 1):

			
			jugFil1 = jugCurrent[0] + pour
			jugFil2 = jugCurrent[1] - pour

			# Check if this state is possible or not
			if (jugFil1 == jug1 or (jugFil2 == 0 and jugFil2 >= 0)):
				jugQueue.append([jugFil1, jugFil2])

			
			jugFil1 = jugCurrent[0] - pour
			jugFil2 = jugCurrent[1] + pour

			
			if ((jugFil1 == 0 and jugFil1 >= 0) or jugFil2 == jug2):
				jugQueue.append([jugFil1, jugFil2])
		
	
		jugQueue.append([jug1, 0])  #empty jug1
		jugQueue.append([0, jug2])  #empty jug2


	if (not isTargetReach):
		print ("Can not give solution for this")


if __name__ == '__main__':    #calling the function
	
	#jug1, jug2, result = 4, 3, 2
	print("Solution For Given Numbers:")
	waterJug(jug1, jug2, result)
