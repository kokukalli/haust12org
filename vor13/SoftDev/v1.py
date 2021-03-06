
def maxdiff(list):
	md = 0
	last = list.pop(0)
	for i in list:
		if (abs(i - last) > md):
			md = abs(i - last)
		last = i
	return md

def linecount(cfile):
	infile = file(cfile, 'r')
	content = infile.read()
	n = content.count('\n')
	return n


ciph = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

def pycha(str1):
	new = ''
	for i in range(len(str1)):
		num = ord(str1[i])
		num += 2
		if str1[i].isalpha():
	#		new+=(chr(ord(str1[i])+2))
			if str1[i].isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif str1[i].islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			new += chr(num)
		else:
			new+=str1[i]
	return new


def maxseq(str1):
	bmax = 0
	localmax = 0
	for i in range(len(str1)):
		if str1[i-1]==str1[i]:
			localmax += 1
			if localmax > bmax:
				bmax = localmax
		elif str1[i-1]!=str1[i]:
			localmax = 1

	return bmax

'''


def pump(str1):
	arr = list(str1)
	for i in range(len(arr)):
		if arr[i].isdigit() and i <= len(arr):
			n = int(arr[i])
			l = arr[i+1]
			arr[i] = arr[i+1]
			for x in range(n-1):
				arr.insert(i,l)

	return ''.join(arr)

'''



def pump(str1):
	arr = list(str1)
	inc = 0
	for i in arr:
		if i.isdigit():
			n = int(i)
			l = arr[inc+1]
			arr[inc] = arr[inc+1]
			for x in range(n-1):
				arr.insert(inc,l)
		inc += 1

	return ''.join(arr)



Xlist = ['kex', 'xylofonn', 'epli','xenos','asni']

def xsort(str1):
	
	p2 = str1
	p2.sort()
	# str.startswith('x')
	new = []
	delList = []
	for x in range(len(p2)):
		if p2[x].startswith('x') or p2[x].startswith('X'):
			new.append(p2[x])
			delList.append(x)
			
	for i in range(len(delList)):
		del p2[delList[i]]
		p2.reverse()
		p2.append(new[i])
		p2.reverse()
	return new + p2



def wordcount(file1):
	infile = file(file1, 'r')
	content = infile.read()
	c2 = content.split()
	count = len(c2)
	dic = []
	for i in c2:
		if i not in dic:
			dic.append(i)

	return (count, len(dic))






