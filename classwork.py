#!/usr/bin/env python
#coding=utf-8
def isPrime(N):
	true=1 #����N�����
	for x in range(2,N):#x��2~N-1������
		if N%x==0:
			true=0	#�@�㰣�N�P�wN�������
	return true
	
ans=0
for num in range(2,1000):
	if isPrime(num)==1:
		ans=ans+num
print "2~1000����ƩM��%d"%ans