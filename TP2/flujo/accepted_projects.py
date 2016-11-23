#!/usr/bin/env python

from Ford_Fulkerson import*
from digraph import*
import sys

if len(sys.argv)<2:
	print sys.argv[0]+': falta ruta de archivo fuente'
	quit(-1)

file=open(sys.argv[1])
n=int(file.readline().strip())
m=int(file.readline().strip())
digraph=Digraph(2+n+m)
s=0
t=1
#rango de los nodos que representan los proyectos
projects_range=(2,m+1)
#rango de los nodos que representan los profesionales
c_range=(m+2,m+n+1)

for i in range(c_range[0],c_range[1]+1):
	c=int(file.readline().strip())
	digraph.add_edge(i,t,c)

#guardo las aristas que unen los projectos con los capacitados
edges_p_to_c=[]
source_capacity=0
for j in range(projects_range[0],projects_range[1]+1):
	campos=file.readline().strip().split()
	digraph.add_edge(s,j,int(campos[0].strip()))
	source_capacity+=int(campos[0].strip())
	for i in range(1,len(campos)):
		edges_p_to_c.append((j,c_range[0]-1+int(campos[i].strip())))
for e in edges_p_to_c:
	digraph.add_edge(e[0],e[1],source_capacity+1)

min_cut=Ford_Fulkerson(digraph,s,t).get_min_cut()
min_cut.sort()
i=1
print 'proyectos a realizar:'
while i<len(min_cut) and min_cut[i]<=projects_range[1]:
	print '\t'+str(min_cut[i])
	i+=1
print '-----\n'
print 'expertos a contratar:'
if i<len(min_cut):
	for j in range(i,len(min_cut)):
		print '\t'+str(min_cut[i])
			

