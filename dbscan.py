'''
		-------		Abhishek Raushan
				CSE Department
		Indian Institute of Information Technology, Guwahati
'''

#!/usr/bin/python

import os,sys
from math import sqrt,pow

# to measure the distance betweer x and y
def EucledianDistance( x , y ):
	temp=sqrt(pow((y[0] - x[0]), 2) + pow((y[1] - x[1]),2) )
	return temp
	
# To recognise the neighours of a point
def addNeighours(points, i):
	neighours=[]
	for j in range(len(points)):
		dist=EucledianDistance(points[i],points[j])
		if dist <= epsilon:
			neighours.append(points[j])
	return neighours
	
	
#return specific point belong to which cluster...
def addConnected(neighours,points,epsilon,min_pts,current_cluster,debug):
	clusters = []
	#print "neighours",neighours
    	for i in range(len(neighours)):
        	#if debug[i] == "notVisited" :
        	for k in range(len(points)):
        		if neighours[i] == points[k] and debug[k]=="notVisited":
        			debug[k]= "visited"
				new_points = addNeighours(points, i)
				#print "new: ",new_points
				if len(new_points) >= min_pts:                                
					for p in new_points:
						if p not in neighours:
							neighours.append(p)
						#print "neighours",neighours
				#print "clusters",clusters
				if points[i] not in clusters:
					clusters.append(points[i])
			
    	return clusters

def dbscan(epsilon, min_pts, points):
	debug=[]
	cluster=[]
	current_cluster=-1
	#cluster[-1]=[]
	noise=[]
	count = 0
	for i in range(len(points)):
		debug.append("notVisited")
	for i in range(len(points)):
		#print points[i]
		if debug[i] == "notVisited":
			#print points[i]
			debug[i] = "visited"
			#print debug
			neighours = addNeighours(points,i)
			
					
			if len(neighours) >= min_pts:
				print neighours
				current_cluster += 1 
				print '\nCreating new cluster %d' % (current_cluster)
				#point.cluster = current_cluster                
				cluster = [points[i],]
				#print cluster
				cluster.extend(addConnected(neighours,points,epsilon,min_pts,current_cluster,debug))
				
			else: 
				noise.append(points[i])
				print "noisy points",noise
				print '----------no new cluster %d' % (current_cluster)
				
# To find points belongs to which cluster , we require epilson, minimum pts and datas
# datas stored in list of lists
# epsilon can integers, float anything
# minimum_point is integer 

if __name__ == '__main__':
	
	import csv
	points=[]
	epsilon = 2
	min_pts = 2
	
	f = open('points.csv' , 'r')
	reader = csv.reader(f, delimiter=",")
	for line in reader:
		points.append([float(line[0]) , float(line[1])])
	#print points
	
	dbscan(epsilon, min_pts, points)
