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

import cv2


#print(initial)

    



#print(nodos.nodes[175][375].color)
#res = problem1.actions((0,1))
#print(res)
#print(problem1.goal)

#print(solucion1.final_path)

def image_solution(solucion,problem,matrix,n):
    color = (93,173,226) if n == 1 else (186,74,0) if n == 2 else (66,0,50) if n == 3 else (247,220,111)
    sol = matrix
    if solucion.final_path == False: 
        print ('No hay solucion')
    else:
        for pix in solucion.final_path:
            if pix == problem.initial or pix in problem.goal:
                pass
            else:
                sol[pix[0]][pix[1]] = color
        

    new_im = Image.fromarray(matrix.astype(np.uint8))
    new_image = new_im.resize((1000, 1000))
    new_image.show()
    new_image.save("solucion"+str(n)+".bmp")

n = int(input("Ingrese n:\n"))
mat = p.discretizar(p.im,n)

nodos =main(mat)

initial = ()
x = 0
for row in nodos.nodes:
    for item in row:
        if item.initial and x == 1:
            initial = (item.x,item.y)
        x+=1
discret_matrix = Image.fromarray(mat.astype(np.uint8))
final_matrix = discret_matrix.resize((1000, 1000))
final_matrix.show()
final_matrix.save("discretizada.bmp")

while True:
    print ("{}\n{}\n{}\n{}\n{}\n{}".format("Elija que algoritmo desea utilizar:","1.Breadth First Search (BFS)","2.Depth First Search (DFS)","3.A* con Euristica Euclidiana","4.A* con Euristica Chebyshev","5.salir"))
    option = input()
    if option == 1:
        problem1 = fw(nodos.nodes,initial,1)
        solucion1 = solucionador(problem1)
        image_solution(solucion1,problem1,mat,1)
    elif option == 2:
        problem2 = fw(nodos.nodes,initial,2)
        solucion2 = solucionador(problem2)
        image_solution(solucion2,problem2,mat,2)
    elif option == 3:
        problem3 = fw(nodos.nodes,initial,3)
        solucion3 = solucionador(problem3)
        image_solution(solucion3,problem3,mat,3)
    elif option == 4:
        problem4 = fw(nodos.nodes,initial,4)
        solucion4 = solucionador(problem4)
        image_solution(solucion4,problem4,mat,4)
    elif option == 5:
        break
    else:
        print("elija una de las siguientes opciones")



