#-*- coding: utf-8 -*-

a=5000
draw=input("請輸入欲提款之金額：")

if draw < 5000:
	print"提款成功!您的存款尚餘%d元" %(a-draw)

elif draw == 5000:
	print"提款成功!目前您的存款已無餘額，請盡快儲蓄"

else:
	
	print"您的存款不足!"
#   P y t h o n  
 