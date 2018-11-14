# Creators: Eric Mahoney & Anuruddha Karunaratne 
# Course: IT 209 
# Assignment: 8 [Cash Register Project]
# Description: Cash register game using object oriented programming. Users are prompted with a customer's transaction and must provide the correct amount of change for that transaction. Users get one point for a correct answer and lose 1 point if incorrect.

# imports the random library that we will use to generate random customers and monetary values
import random

# creates a class called Player that keeps track of the names and scores of the players
class Player:
	def __init__(self,name=None,score=0):
		self.name = input("What is your name: ")
		self.score = score

	# sets the player's name
	def setName(self):
		self.name = input("What is your name: ")

	# returns the player's name
	def returnName(self):
		return self.name

# creates a class called Customer that defines methods to randomly generator different customers
class Customer:
	def __init__(self):

		# list of different names for our customers
		self.name = ['John', 'Bob', 'Linda', 'Tom', 'Richard', 'Hubert', 'Alison', 'Maddison', 'Eric', 'Candice', 'Tiffany', 'Sydney', 'Adam', 'William', 'Patricia']
		
		# list of different amounts of money that our customers will buy food with.
		self.money = [9.25, 5.00, 10.00, 7.50, 10.00, 20.00, 5.50, 15.25, 12.75, 35.70]
		
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

	# NOT WORKING YET # 
	def randGroceries(self):	
		
		#empty shopping cart that will hold 5 different items of different prices
		cart_items = []
		item_prices = []
		# for loop that loops through the dictionary and pulls different groceries
		for i in range(0,5):
			cart_items.append(random.choice(list(self.groceries)),)
		
		for item in cart_items:
			price = self.groceries.get(items)
			item_prices.append(price)
			print("ADDED: " + item + " TO CART")


		# returns the completed shopping cart 
		return shopping_cart
	

	# COMPLETELY WORKING #
	def randCustomer(self): 
		
		# gets random name from the list above using the random library
		randomName = self.name[random.randint(0,14)]
		
		# gets random money from the list above using the random library
		randomMoney = self.money[random.randint(0,9)]
		
		# empty dictionary that will hold information about the customer
		customer = {randomName: randomMoney}
		
		# returns the dictionary of the customer
		return customer

	def getCustomer(self):
		customer = randCustomer()
		return customer

# defines a Register class that will hold different values of money
class Register:
	def __init__(self,one,five,ten,twenty,fifty,oneHundred):
		self.one = one
		self.five = five
		self.ten = ten
		self.twenty = twenty
		self.fifty = fifty
		self.oneHundred = oneHundred

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
	def __init__(self):
		self.price = price

	def calcTax(self):
		va_sales_tax = 0.043
		tax = price * va_sales_tax
		return tax


# sets up the player
new_player = Player()
new_player.setName()

# creates a new customer:
customer = Customer()
