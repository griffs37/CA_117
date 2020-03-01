#!usr/bin/env python

class BankAccount(object):

	next_account_number = 0
	total_lodgements = 0
	interest_rate = 0.043


	def __init__(self, forename, surname, balance=0.00, account_number=0):
		self.forename = forename
		self.surname = surname
		self.balance = balance
		self.account_number = account_number
		BankAccount.next_account_number = self.account_number + 1

	def lodge(self, add):
		self.balance += add
		BankAccount.total_lodgements += 1

	def apply_interest(self):
		return 

