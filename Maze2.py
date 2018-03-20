a = [[1,0,0,0],
	 [1,0,0,0],
	 [1,1,1,1],
	 [1,0,0,1]]




def track(i,j,res):
	# print "start"
	if i==3 and j==3:
		res.append([i,j])
		print res
		return

	if i < 3 and str(a[i+1][j]) == "1":
		res.append([i,j])
		track(i+1,j,res)
	
	elif j < 3 and str(a[i][j+1]) == "1":
		res.append([i,j])
		track(i,j+1,res)
	
	else:
		a[i][j] = 0
		i = res[-1][0]
		j = res[-1][1]
		res.pop()
		track(i,j,res)




arr = []		#for appending result
track(0,0,arr)
