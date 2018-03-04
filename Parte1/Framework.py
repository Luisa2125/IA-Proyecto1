import proyecto as p
import numpy as np
class Framework(object):
	initial = ()
	matrix = []
	goal = ()
	met = 0
	def __init__(self, matrix, initial,met):
		self.matrix = matrix
		self.dim = len(matrix)
		self.initial = initial
		self.goal = self.get_goal()
		self.met = met

	
	def actions(self,s):
		actions = []
		try:
		
			if self.matrix[s[1]][s[0]+1].color == (255,255,255) and s[1] < 500:
				actions.append('derecha')
			if self.matrix[s[1]][s[0]-1].color ==(255,255,255) and s[1] >0: 
				actions.append('izquierda') 
			if self.matrix[s[1]+1][s[0]].color ==(255,255,255) and s[0] < 500:
				actions.append('abajo') 
			if self.matrix[s[1]-1][s[0]].color ==(255,255,255) and s[0] > 0:
				actions.append('arriba') 
		except:
			#print (s)
			pass
		return actions
	def result(self,s,a):
		#print ('result',s,a)
		result = self.matrix[s[1]][s[0]+1] if a == 'derecha' else ( self.matrix[s[1]][s[0]-1] if a == 'izquierda' else ( self.matrix[s[1]-1][s[0]] if a == 'arriba' else ( self.matrix[s[1]+1][s[0]] if a == 'abajo' else 'nada')))
		#print('result adentro', result)
		return result.y,result.x
	def goal_test(self,s):
		#print('goal test',s,'color',self.matrix[s[0]][s[1]].color)
		if self.matrix[s[0]][s[1]].color == (0,255,0):
			return True
		else:
			return False

	def step_cost(self,s0,a,s1):
		return 1

	def path_cost(self,estados):
		return len(estados)

	def get_goal(self):
		goals = []
		for row in self.matrix:
			#print row
			for item in row:
				#print item
				if item.color == (0,255,0):
					if len(goals):
						#print('try')
						#print ('goal',goals)
						
						#print(((goal[0]-item.x)> 150 or (goal[1]-item.y)> 150),goal not in goals)
						#print ((goal[0]-item.x) or (goal[1]-item.y))
						if (item.x,item.y) not in goals:
							if (np.abs(goals[len(goals)-1][0]-item.x)> 150 or np.abs(goals[len(goals)-1][1]-item.y)> 150) :
								goals.append((item.x , item.y))
					else:
						#print('se agrego')
						goals.append((item.x , item.y))
		return goals

'''
mat = p.discretizar(p.im,20)
for i in range(len(mat)):
	for y in range(len(mat[0])):
		#print(int(mat[i][s[1]][0]),int(mat[i][s[1]][1]),int(mat[i][s[1]][2]))
		if int(mat[i][y][0]) == 255 and int(mat[i][y][1]) == 0 and int(mat[i][y][2]) == 0:
			#print mat[i][y]
			init = (i,y)
			break
f = Framework(mat,init)
print('initial',f.initial)
print('goal',f.goalTest((224,375)))
print(mat[224][375])
print(f.getGoal())'''
