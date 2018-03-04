class solucionador(object):
	final_path = []
	def __init__(self,problem):
		self.problem = problem
		self.final_path = self.graph_search(problem)

	def breadth_first(self,frontier):
		path = frontier[0]
		for index in range(len(frontier)-1):
			if len(frontier[index+1]) > len(path):
				path = frontier[index+1]
		return path

	def depth_first(self,frontier):
		path = frontier[0]
		for index in range(len(frontier)-1):
			if len(frontier[index+1]) < len(path):
				path = frontier[index+1]
		return path
	def euclidea(self,punto1,punto2):
		return (((punto2[0]-punto1[0])**2)+((punto2[1]-punto1[1])**2))**(1/2)
		def euristica2():
			pass

	def A_estrella_Eu(self,frontier):
		func = []
		for goal in (self.problem.goal):
			for path in frontier:
				#print path ,len(path) , (path[len(path)-1][0],path[len(path)-1][1]),goal
				func.append((len(path) + self.euclidea((path[len(path)-1][0],path[len(path)-1][1]),goal),path))
		#print func
		#print min(func)
		return min(func)[1]

	def A_estrella_(self):
		pass

	def remove_choice(self,frontier):
		if self.problem.met == 1:
			path = self.breadth_first(frontier)
		elif self.problem.met == 2:
			path = self.depth_first(frontier)
		elif self.problem.met == 3:
			path = self.A_estrella_Eu(frontier)
		else:
			path = self.A_estrella_()
		return path

	def graph_search(self, problem):
	    frontier = [[problem.initial]]
	    explored = []
	    final_path = []
	    while True:
	    	if len(frontier):
	    		print 'frontera',frontier
	    		print 'explorados', explored
	    		path = self.remove_choice(frontier)
	    		frontier.remove(path)
	    		s = path[-1]
	    		explored.append(s)
	    		if problem.goal_test(s):
	    			return path
	    		#print('actions',problem.actions(s))
	    		for a in problem.actions(s):
	    			#print('action',a)
	    			result = problem.result(s,a)
	    			#print ('result',result)

	    			if result not in explored:
	    				new_path = []
	    				new_path.extend(path)
	    				new_path.extend([result])
	    				frontier.extend([new_path])
	    				#print 'frontier',frontier
	    	else:
	    		return False
	
	

#print(A_estrella_Eu([[(1,2),(1,3),(1,5)],[(1,2),(1,3)],[(1,3),(1,5)],[(1,2),(1,3),(1,5),(2,1)]]))
#print(depth_first([[(1,2),(1,3),(1,5)],[(1,2),(1,3)],[(1,3),(1,5)],[(1,2),(1,3),(1,5),(2,1)]]))
'''
path = self.remove_choice(frontier)
	        	print 'path',path,'\nfrontera:',frontier
	        	frontier.remove(path)
	        	s = path[-1]
	        	print('s',s)
	        	explored.append(s)
	        	print('explored',explored)
	        	print('actions',problem.actions(s))
	        	print('goal',problem.goal_test(s))
	        	if problem.goal_test(s):
	        		final_path = path
	        	else:
					for a in problem.actions(s):
						print('action',a)
						result = problem.result(s, a)
						print('result',result)

						if result not in explored:
							new_path = []
							new_path.extend(path)
							new_path.extend(problem.result(s, a))
							frontier.append(new_path)
'''