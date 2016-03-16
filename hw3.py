#-*- coding: utf-8 -*-
x=input("請輸入一個整數：")
sum=0
for i in range(1,x+1):

	if x%i==0:
		sum = sum+1


if sum == 2:
	print "This is 質數。"

else:
	print "This is not 質數。"		