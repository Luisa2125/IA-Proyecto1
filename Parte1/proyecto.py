from numpy import asarray
import numpy as np
from PIL import Image
import itertools
im = asarray(Image.open('lab1.bmp'))
def discretizar(im,n):

	#print (len(im),len(im[0]))
	x = len(im)/(n)
	particiones = list(np.arange(0,len(im),x))
	particiones.append(len(im))
	intervalos = []
	i = 0
	#print (particiones)
	#print len(particiones)
	while i < len(particiones)-1:
		intervalos.append(range(particiones[i],particiones[i+1]))
		i+=1

	#intervalos = [(0,1,2,3,4),(5,6,7,8,9)]
	#print(intervalos)
	discret_squares= []
	#print( len(intervalos))

	for intervalo in intervalos:
		for intervalo2 in intervalos:
			producto = list(itertools.product(intervalo,intervalo2))
			#print(producto)
			discret_squares.append(producto)
	#print(len(discret_squares),len(discret_squares[0]))
	#448-464
	#48-64
	return pintar(discret_squares,im)

def determinate(discret_square):
	colors = []
	#print len(discret_square)
	for x,y in discret_square:
		colors.append((im[y][x][0],im[y][x][1],im[y][x][2]))
		#if 48<x<64 and 448<y<464:
		#	print((im[y][x][0],im[y][x][1],im[y][x][2]))
			
	if (254,0,0) in colors or (255,0,0) in colors:
		return [255,0,0]
	elif (0,255,0) in colors:
		return [0,255,0]
	elif (255,255,255) in colors:
		return [255,255,255]
	elif (0.,0.,25.5) in colors:
		return [0,0,255]
	elif (0,0,0) in colors:
		return [0,0,0]
	else:
		return [255,255,255]

def pintar(discret_squares,im):
	discret_matrix = np.empty([len(im), len(im[0]),3])
	for discret_square in discret_squares:
		color = determinate(discret_square)
		#print(color)
		for x,y in discret_square:
			discret_matrix[y][x] = color

		
	discret_array = asarray(discret_matrix)
	print (len(discret_array),len(discret_array[0]))


	new_im = Image.fromarray(discret_array.astype(np.uint8))
	new_im.save("discretI.bmp")
	return discret_array

matriz = discretizar(im,10)
#print(matriz[425][25])
#print matriz


#print (discret_square)
#print(len(im))