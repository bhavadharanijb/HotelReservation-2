# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 23:09:52 2022

@author: bhava
"""

import random
import datetime

# Global List Declaration
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

# Global Variable Declaration

i = 0

# home Function
def home():
	
	print("\t\t\t\t\t\t WELCOME TO HOTEL ANCASA\n")
	print("\t\t\t 1 Booking\n")
	print("\t\t\t 2 Rooms Info\n")
	print("\t\t\t 3 Room Service(Menu Card)\n")
	print("\t\t\t 4 Payment\n")
	print("\t\t\t 5 record\n")
	print("\t\t\t 0 Exit\n")

	ch=int(input("->"))
	
	if ch == 1:
		print(" ")
		booking()
	
	elif ch == 2:
		print(" ")
		Rooms_Info()
	
	elif ch == 3:
		print(" ")
		restaurant()
	
	elif ch == 4:
		print(" ")
		payment()
	
	elif ch == 5:
		print(" ")
		record()
	
	else:
		exit()

# Function used in booking

def date(c):
    print("date")
	
	


def booking():
    print("booking")

# ROOMS INFO
def rooms_info():
	print("		 ------ HOTEL ROOMS INFO ------")
	print("")
	print("STANDARD NON-AC")
	print("---------------------------------------------------------------")
	print("Room amenities include: 1 Double Bed, Television, Telephone,")
	print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
	print("an attached washroom with hot/cold water.\n")
	print("STANDARD NON-AC")
	print("---------------------------------------------------------------")
	print("Room amenities include: 1 Double Bed, Television, Telephone,")
	print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
	print("an attached washroom with hot/cold water + Window/Split AC.\n")
	print("3-Bed NON-AC")
	print("---------------------------------------------------------------")
	print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
	print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
	print("Side table, Balcony with an Accent table with 2 Chair and an")
	print("attached washroom with hot/cold water.\n")
	print("3-Bed AC")
	print("---------------------------------------------------------------")
	print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
	print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
	print("1 Side table, Balcony with an Accent table with 2 Chair and an")
	print("attached washroom with hot/cold water + Window/Split AC.\n\n")
	print()
	n=int(input())
	if n==0:
		home()
	else:
		exit()

# RESTAURANT FUNCTION
def restaurant():
	
			
			# updates restaurant charges and then
			# appends in 'rc' list
			r=r+rc.pop(n)
			rc.append(r)	
		
	if f == 0:
		print("Invalid Customer Id")
	n=int(input())
	if n==0:
		home()
	else:
		exit()
	
				
# PAYMENT FUNCTION			
def payment():
	
	ph=str(input("Phone Number: "))
	global i
	f=0
	dash="--------------------------------"
	for n in range(0,i):
		
			
			# checks if payment is
			# not already done
			
				f=1
				print(" Payment")
				print("")
				print(" MODE OF PAYMENT")
				
				print(" 1- Credit/Debit Card")
				print(" 2- Paytm/PhonePe")
				print(" 3- Using UPI")
				print(" 4- Cash")
				print("\n Amount: ",(price[n]*day[n])+rc[n])
				print("\n		 Pay For AnCasa")
				print(" (y/n)")
				ch=str(input("->"))
				
				
					print("\n\ndash")
					print("		 Hotel AnCasa")
					print(dash)
					print("			 Bill")
					print(dash)
					print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
					print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
					print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
					print(" Restaurant Charges: \t",rc[n])
					print(dash)
					print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
					print(dash)
					print("		 Thank You")
					print("		 Visit Again :)")
					print(dash+"/n")
					p.pop(n)
					p.insert(n,1)
					
					# pops room no. and customer id from list and
					# later assigns zero at same position
					roomno.pop(n)
					custid.pop(n)
					roomno.insert(n,0)
					custid.insert(n,0)
					
			
				
				for j in range(n+1,i):
					if ph==phno[j] :
						if p[j]!=0:
							f=1
							print("\n\tPayment has been Made :)\n\n")
						
						
		
		print("Invalid Customer Id")
		
	

# record FUNCTION
def record():
	
	# checks if any record exists or not
	if phno!=[]:
		print("	 *** HOTEL record ***\n")
		print("| Name	 | Phone No. | Address	 | Check-In | Check-Out	 | Room Type	 | Price	 |")
		print("----------------------------------------------------------------------------------------------------------------------")
		
		for n in range(0,i):
			print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n])
		
		print("----------------------------------------------------------------------------------------------------------------------")
	
	else:
		print("No records Found")
	n = int(input())
	if n == 0:
		home()
		
	else:
		exit()

# Driver Code
home()