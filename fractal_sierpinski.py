#!/usr/bin/env python3
##DEVTEST###
###pl7ofit###

from PIL import Image, ImageDraw
from random import randint as r

def gen_fractal(w,h,attractors,iterations,colored,coef, output):
	start_point = 0,0
	colors = [(r(0,255),r(0,255),r(0,255)) for color in range(0,len(attractors))]
	image = Image.new('RGB', (w, h), (255,255,255))
	draw = ImageDraw.Draw(image)
	get_distance = lambda c,t,co : ( ((c[0]-t[0])//co)+t[0], ((c[1]-t[1])//co)+t[1] )
	for i in range(iterations):
		attr_index = r(0, len( attractors ) - 1 )
		attr = attractors[ attr_index ]
		start_point = get_distance(start_point, attr, coef)
		if colored: color = colors[ attr_index ]
		else: color = (0,0,0)
		draw.point( start_point , fill=color )
	image.save( output )

#attractors = [ (1000,0),(2000,2000),(0,2000)]
attractors = [ ( r(0,2000), r(0,2000) ) for cord in range(0,r(3,10)) ]
name_postfix = ''
for cord in attractors: name_postfix+='_'+str(cord[0])+'.'+str(cord[1])+'_'
h,w = 2000,2000
iterations = 500000
colored = True
coef = r(2,4)
coeff = r(1,9)/10
coef+=coeff
output = 'fractals/fractal_triangle'+str(coef)+name_postfix+'.png'


gen_fractal(h,w,attractors,iterations, colored, coef, output)
