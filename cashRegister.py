# Creators: Eric Mahoney & Anuruddha Karunaratne 
# Course: IT 209 
# Assignment: 8 [Project]
# Description: Cash register game using object oriented programming. Users are prompted with a customer's transaction and must provide the correct amount of change for that transaction. Users get one point for a correct answer and lose 1 point if incorrect.

class Player:
	def __init__(self, name, score=0):
		self.name = name
		self.score = score

	def addScore(self):
		score += 1
		return score

	def subScore(self):
		score -= 1
		return score

	def returnScore(self):
		return score

class Customer:
	def __init__(self, money):
		self.money = money

class Register:
	def __init__(self,one,five,ten,twenty,fifty,oneHundred):
		self.one = one
		self.five = five
		self.ten = ten
		self.twenty = twenty
		self.fifty = fifty
		self.oneHundred = oneHundred

class Score:
	def __init__(self):
		self.score = score

class Purchase:
	def __init__(self):
		self.price = price

	def calcTax(self):
		va_sales_tax = 0.043
		tax = price * va_sales_tax
		return tax