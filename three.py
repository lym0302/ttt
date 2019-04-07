# coding=utf-8
### find the minimize
def findmin(n,minn):
	aa = n[0]-minn
	for i in range(1,len(n)):
		n[i] = n[i] - minn
		if(aa == 0):
			aa = n[i]
		elif(n[i] < aa):
			aa = n[i]
		else:
			aa = aa
	return aa


def main():
	### input paras
	paras = raw_input()
	n = int(paras.split()[0])
	k = int(paras.split()[1])
	#print(n,k)
	#print(paras)
	#print(type(paras))

	numbers = raw_input()
	nums = []
	for i in numbers.split(' '):
		nums.append(int(i))
	minnum = 0
	for i in range(k):
		minnum = findmin(nums,minnum)
		print(minnum)


if __name__ == "__main__":
	main()
			
