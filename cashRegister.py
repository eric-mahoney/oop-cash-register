# Creators: Eric Mahoney & Anuruddha Karunaratne 
# Course: IT 209 
# Assignment: 8 [Cash Register Project]
# Description: Cash register game using object oriented programming. Users are prompted with a customer's transaction and must provide the correct amount of change for that transaction. Users get one point for a correct answer and lose 1 point if incorrect.

# imports the random library that we will use to generate random customers and monetary values
import random

# creates a class called Player that keeps track of the names and scores of the players
class Player:
	def __init__(self,firstName=None,lastName=None,score=0):
		self.firstName = firstName
		self.lastName = lastName
		self.name = firstName + " " + lastName
		self.score = score

	# sets the player's name
	def setName(self):
		self.name = name

	# returns the player's name
	def returnName(self):
		return self.name

# creates a class called Customer that defines methods to randomly generator different customers
class Customer:
	def __init__(self):

		# list of different names for our customers
		self.name = ['John', 'Bob', 'Linda', 'Tom', 'Richard', 'Hubert', 'Alison', 'Maddison', 'Eric', 'Candice', 'Tiffany', 'Sydney', 'Adam', 'William', 'Patricia']
		
		# list of different amounts of money that our customers will buy food with.
		self.money = [15.00,16.00,17.00,18.00,19.00,20.00,21.00,22.00,23.00,24.00,25.00]
		
		# dictionary list of groceries prices from:
		# http://www.visualcapitalist.com/decade-grocery-prices/
		self.groceries = {
		'white bread': 1.34,
		'wheat bread': 1.99,
		'whole milk': 3.24,
		'salted butter': 3.38,
		'american cheese': 4.28,
		'eggs': 1.43,
		'apples': 1.29,
		'bananas': 0.56,
		'oranges': 1.33,
		'strawberries': 2.21,
		'lemons': 2.01,
		'tomatoes': 1.90,
		'broccoli': 1.81,
		'bacon': 5.79,
		'pasta': 1.28,
		'dried beans': 1.36,
		'ground beef': 4.12,
		'all purpose flour': 0.52,
		'creamy peanut butter': 2.56,
		'top round steak': 5.78,
		'potatoes': 0.72,
		'frozen turkey': 1.59,
		'sirloin steak': 8.07,
		'white rice': 0.72,
		'chocolate chip cookies': 3.47,
		'seedless grapes': 2.67,
		'sugar': 0.65,
		'ice cream': 4.70
		}

		self.total = []

	def randGroceries(self):	
		
		#empty shopping cart that will hold 5 different items of different prices
		cart_items = []
		# for loop that loops through the dictionary and pulls different groceries
		for i in range(0,5):
			cart_items.append(random.choice(list(self.groceries)))
		
		for item in cart_items:
			price = self.groceries.get(item)
			self.total.append(price)

		self.groceries = cart_items

		# returns the completed shopping cart 
		return self.groceries
	

	# generates a random customer from a list
	def randCustomer(self): 
		
		# gets random name from the list above using the random library
		self.name = self.name[random.randint(0,14)]
		
		# gets random money from the list above using the random library
		self.money = self.money[random.randint(0,9)]
		
		# empty dictionary that will hold information about the customer
		self.customer = {self.name: self.money}
		
		# returns the dictionary of the customer
		return self.customer

	def getCustomer(self):
		customer = randCustomer()
		return customer

	def calcTax(self):
		va_sales_tax = 0.043
		tax = sum(self.total) * va_sales_tax
		return round(tax,2)
	def getMoney(self):
		self.money = [15.00,16.00,17.00,18.00,19.00,20.00,21.00,22.00,23.00,24.00,25.00]
		self.money = self.money[random.randint(0,9)]
		return self.money

# defines a Register class that will hold different values of money
class Register:
	def __init__(self,penny=None,nickle=None,dime=None,quarter=None,one=None,five=None,ten=None,twenty=None):
		self.penny = 0.01
		self.nickle = 0.05
		self.dime = 0.1
		self.quarter = 0.25
		self.one = 1.00
		self.five = 5.00
		self.ten = 10.00
		self.twenty = 20.00


# creates a class called Score that will be run when we need to keep track of high scores
class Scores:
	def __init__(self):
		self.scores = {}

	def addScore(self,user,score):
		scores[score] = user
		return self.scores

	def removeScore(self):
		if key in scores:
			del scores[key]
		return self.scores

	def returnScore(self):
		return self.score

# creates a class for purchases
class Purchase:
	def __init__(self,price):
		self.price = price

	def calcTax(self):
		va_sales_tax = 0.043
		tax = price * va_sales_tax
		return tax

# sets up the player
def newPlayer():
	first = input('What is your first name? ')
	last = input('What is your second name? ')
	player = Player(first,last)
	print('\nHi ' + player.name)

def calcCustomer():
	tax_amount = client.calcTax()
	total = sum(client.total)
	final_total = round((total + tax_amount),2)
	print('\nThis customer: ' + str(client.name) + ' is ready to checkout.')
	print('\nTheir items include: ')
	count = 1
	for item in client.groceries:
		print(str(count) + " - " + str(item))
		count += 1
	print('\nTheir purchase amount is: ' + str(round(total,2)))
	print('+ sales tax (' + str(tax_amount) + ")")
	print("------------------------------")
	print('FINAL TOTAL: ' + str(final_total))
	
	while(client.money < final_total):
		client.getMoney()
	
	return final_total

def checkChange(total,money):
	print('\nThe customer hands you: ' + str(money))
	print('The total amount is: ' + str(total))
	rounded_money = round((money - total),2)
	print('you need: ' + str(rounded_money) + ' in change.')
	penny = float(input('how many pennies should you return in change?')) * 0.01
	nickles = float(input('how many nickles should you return in change?')) * 0.05
	dimes = float(input('how many dimes should you return in change?')) * 0.10
	quarters = float(input('how many quarters should you return in change?')) * 0.25
	ones = int(input('how many one should you return in change?')) * 1
	fives = int(input('how many fives should you return in change?')) * 5
	tens = int(input('how many tens should you return in change?')) * 10
	total_change = round((penny + nickles + dimes + quarters + ones + fives + tens),2)

	if(total_change != rounded_money):
		print('sorry, you gave the incorrect change.')
		print('you gave: ' + str(total_change))
		print('you needed: ' + str(rounded_money))
	else:
		print('successfully checked out user!')

# Global Code ---------------------------------------------

print('\t\t\t\tWelcome to Cash-Register.py!\t\t\t\t')
done = False
newPlayer()
while done != True:
	client = Customer()
	client.randCustomer()
	client.randGroceries()
	total = calcCustomer()
	money = client.money
	checkChange(total,money)
	done = input('\nWould you like to play again? yes or no: ')
	if(done == 'no'):
		done = True