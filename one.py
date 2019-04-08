# coding=utf-8

import random

def operation(n,k,tt):
	news = []
	flag = 0
	if(tt<=k):
		### Randomly select a number from [0,1]
		flag = random.sample([0,1], 1)[0]
	#print(flag)
	
	### flag=0  --> Each number minus 1
	if(flag==0):
		for ii in range(len(n)):
			if(n[ii]==0):
				news.append(n[ii])
			else:
				news.append(n[ii] - 1)
		
	
	### flag=1 --> Each number is split into two numbers
	else:
		for jj in range(len(n)):
			if(n[jj]==0 or n[jj]==1):
				news.append(n[jj])
			else:
				a = random.sample(range(1,n[jj]), 1)[0]
				#print(a,type(a))
				#print(n[jj],type(n[jj]))
				b = n[jj] - a
				news.append(a)
				news.append(b)
	
	return news



def main():
	paras = raw_input()
	n = int(paras.split(" ")[0])
	k = int(paras.split(" ")[1])
	nums = []
	nums.append(n)
	#print(nums)
	
	for ii in range(1,n+1):
		nums = operation(nums,k,ii)
		#print(nums)
		summ = 0
		for jj in range(len(nums)):
			summ += nums[jj]
		if(summ==0):
			break

	print(ii)
	
	#print(n)
	#print(k)



if __name__ == "__main__":
	main()
	
