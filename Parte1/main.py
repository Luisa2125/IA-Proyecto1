from nodo import node 
from Solucionador import solucionador
from PIL import Image
import numpy as np
class main(object):
    nodes = []
    def __init__(self,matrix):
        n = 0
        for x in range(len(matrix)):
            nodos = []
            for y in range(len(matrix)):
                if int(matrix[x][y][0]) == 255 and int(matrix[x][y][1]) == 0 and int(matrix[x][y][2]) == 0 and n == 0:
                    nodos.append(node(True,x,y,(int(matrix[x][y][0]),int(matrix[x][y][1]),int(matrix[x][y][2]))))
                    n = 1
                else:
                    nodos.append(node(False,x,y,(int(matrix[x][y][0]),int(matrix[x][y][1]),int(matrix[x][y][2]))))
            self.nodes.append(nodos)




import proyecto as p
from Framework import Framework as fw
n = 10
mat = p.discretizar(p.im,n)

nodos =main(mat)

initial = ()
for row in nodos.nodes:
    for item in row:
        if item.initial:
            initial = (item.x,item.y)
#print(initial)
problem1 = fw(nodos.nodes,initial,1)
problem2 = fw(nodos.nodes,initial,2)
problem3 = fw(nodos.nodes,initial,3)
problem4 = fw(nodos.nodes,initial,4)

#print(nodos.nodes[175][375].color)
#res = problem1.actions((0,1))
#print(res)
#print(problem1.goal)
solucion1 = solucionador(problem1)
#solucion2 = solucionador(problem2)
#solucion3 = solucionador(problem3)
#solucion4 = solucionador(problem4)
#print(solucion1.final_path)
if solucion1.final_path == False: 
    print ('No hay solucion')
else:
    for pix in solucion1.final_path:
        if pix == problem1.initial or pix in problem1.goal:
            pass
        else:
            mat[pix[0]][pix[1]] = (0,0,255)
    

new_im = Image.fromarray(mat.astype(np.uint8))
new_im.save("solucion1.bmp")

