#-*- coding: utf-8 -*-

def isPrime(N):
	prime=0
	for j in range(1,N+1):
		
		if N%j==0:
			prime=prime+1
			
	if prime == 2:		
		return 1
	else:
		return 0

sum=0
for i in range(1,1001):
	if isPrime(i)==1:
		sum=sum+i

print "2~1000����ƩM:%d\n" %sum#   h e l l o   p y t h o n  
 