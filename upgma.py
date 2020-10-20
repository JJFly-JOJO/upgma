import numpy as np
labels = ['A','B','C','D','E','F','G']
table = [
		[1000,1000,1000,1000,1000,10000,1000],                       
		[19,1000,1000,1000,1000,1000,1000],                    #B 
		[27,31,1000,1000,1000,1000,1000],                #C 
		[8, 18, 26,1000,1000,1000,1000],             #D 
		[33, 36, 41, 31,1000,1000,1000],        #E 
		[18, 1, 32, 17, 35,1000,1000],     #F 
		[13, 13, 29, 14, 28, 12, 1000] #G 
		]
count = [1,1,1,1,1,1,1]
def UPGMA( table, labels, count):
	
	a, b = 0, 0  #a行，b列,a>b
	for i in range(len(labels)):
		for j in range(len(labels)):
			if table[a][b]>table[i][j]:
				a = i
				b = j
	w = len(count)
	for k in range(0,b):#更新行
		table[b][k] = (table[b][k] * count[b] * count[k] + table[a][k] * count[a] * count[k])/((count[a]+count[b])*count[k])
	for j in range(b+1,w):#更新列
		if j>a:
			table[j][b] = (table[j][b]*count[j]*count[b]+table[j][a]*count[a]*count[j]) / ((count[a]+count[b])*count[j])
		else:
			table[j][b] = (table[j][b]*count[j]*count[b]+table[a][j]*count[a]*count[j]) / ((count[a]+count[b])*count[j])
	count[b] = count[a] + count[b]
	count.pop(a)
	table = np.delete(table, a, axis = 1)#删除行列
	table = np.delete(table, a, axis = 0)
	labels[b] = (labels[b],labels[a])
	labels.pop(a)
	print(labels)
	print(table)
	print(count)
	if w > 1:
		UPGMA( table, labels, count )
	else:
		print("it's done")
UPGMA( table, labels, count )
		
	


