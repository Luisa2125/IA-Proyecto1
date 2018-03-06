from numpy import asarray
import numpy as np
from PIL import Image
import itertools
im = asarray(Image.open('1.bmp'))
def discretizar(im,n):

	#print (len(im),len(im[0]))
	x = int(round(len(im)/float(n)))
	particiones = list(np.arange(0,len(im),x))
	particiones.append(len(im))
	intervalos = []
	i = 0
	#print (particiones)
	#print len(particiones),x,n
	while i < len(particiones)-1:
		intervalos.append(range(particiones[i],particiones[i+1]))
		i+=1

	#intervalos = [(0,1,2,3,4),(5,6,7,8,9)]
	#print 'len int',len(intervalos)
	discret_squares= []
	#print( len(intervalos))
	#print len(list(itertools.product(intervalos[0],intervalos[0])))
	for intervalo in intervalos:
		for intervalo2 in intervalos:
			producto = list(itertools.product(intervalo,intervalo2))
			discret_squares.append(producto)

	#print len(list(itertools.product(intervalo,intervalo2)))

	#print('discret_squares',len(discret_squares),(discret_squares[0]))
	#448-464
	#48-64
	#print(discret_squares)
	return pintar(discret_squares,im,n)

def determinate(discret_square):
	colors = []
	#print len(discret_square)
	for x,y in discret_square:
		colors.append((im[y][x][0],im[y][x][1],im[y][x][2]))

		#if 48<x<64 and 448<y<464:
		#	print((im[y][x][0],im[y][x][1],im[y][x][2]))

	r = round(colors.count((254,0,0))/529.0,2)
	r1 = round(colors.count((254,0,0))/529.0,2)
	g = round(colors.count((0,255,0))/529.0,2)
	w = round(colors.count((255,255,255))/529.0,2)
	b = round(colors.count((0,0,0))/529.0,2)

	if r+r1 > 0.00:
		return [255,0,0]
	elif g > 0.00:
		return [0,255,0]
	elif w > 0.00:
		return [255,255,255]
	else:
		return [0,0,0]
'''
	print r,r1,g,w,b
	if (254,0,0) in colors or (255,0,0) in colors:
		return [255,0,0]
	elif (0,255,0) in colors:
		return [0,255,0]
	elif (255,255,255) in colors:
		return [255,255,255]
	elif (0.,0.,25.5) in colors:
		return [0,0,255]
	else:
		return [0,0,0]
'''
def pintar(discret_squares,im,n):
	discret_matrix = np.empty([len(im), len(im[0]),3])
	discret_new = []
	square = []
	#print len(discret_squares), len(discret_squares[0]), len(im)**2, len(im)**2/n
	
	#print(determinate(discret_squares[0]))
	for discret_square in discret_squares:
		color = determinate(discret_square)
	
		#print count, color
		square.append(color)
			
	#print len(square)
	count = 0
	for i in range(n):
		row = []
		for it in range(n):
			#print it+(i*10)
			row.append(square[count])
			count+=1
		#print row
		discret_new.append(row)

	discret_new = [list(i) for i in zip(*discret_new)] 
	#discret_new = np.array(square).reshape(len(im)/n,len(im)/n)
	#print (discret_new)
	discret_array = asarray(discret_new)
	print (len(discret_array),len(discret_array[0]))


	new_im = Image.fromarray(discret_array.astype(np.uint8))
	new_im.save("discret2.bmp")
	return discret_array

#matriz = discretizar(im,50)
#print(matriz[425][25])
#print matriz


#print (discret_square)
#print(len(im))