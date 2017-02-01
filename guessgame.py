#! /usr/bin/env python
import math
import random

myfile=open("yourscore.txt","r")


content = myfile.read()

print content

myfile.close()


myfile=open("yourscore.txt","a")

list=[]
count=0
i=0
noofplay=1
x=random.randint(1,100)
while (i<10):
	
	print x
	
	num= raw_input("enter your number: ")

	flag= num.isdigit()
	if flag :
		num= eval(num)
		#list.append(num)
	if num in list:
		print "you are entered this num before"
		i=i-1

 	if num > x and num <= 100 :
 		print "your num is grather than the value please enter small num "
 		
	elif num < x:

		print "your num is less than the value please enter grather num "
	elif num >100 :

		print"out of range "
		i=i-1	
	else:
		print "you win"

		count+=1
		print "you hava a ",10-(i+1),"trial "


	i+=1
	list.append(num)
	if(i==10):

		list=[]
		print "do you want to play agine"
		confirm= raw_input("play agine enter y or n: ")
		if confirm == "y" :
			noofplay+=1
			#list=[]
			#count=count
			i=0

		else :
			myfile.write(repr(count))
			myfile.write(repr(noofplay))
			break
print "your score is ",count 

print "you played ",noofplay,"times"





myfile.close()




#only 10 trial
#num out of rang not count in trial
#echo message if num > or < or = num 
#echo  finalscore
#echo message if num is insert before
#if value insert before not count in trial
#playagine
#count how many time you played this game





