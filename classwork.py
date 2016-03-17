#!/usr/bin/env python
#coding=utf-8
def isPrime(N):
	true=1 #先視N為質數
	for x in range(2,N):#x為2~N-1之除數
		if N%x==0:
			true=0	#一整除就判定N不為質數
	return true
	
ans=0
for num in range(2,1000):
	if isPrime(num)==1:
		ans=ans+num
print "2~1000的質數和為%d"%ans