#!/usr/bin/env python3.6
# This version uses 8byte numpy floats which increases precision
#
import numpy as np
import time

class GaussianElimination:

	def __init__(self,unknowns,equations=None):
		self.matrix = []
		if equations == None:
			self.dim1 = unknowns # rows
		else:
			self.dim1 = equations # rows
		self.dim2 = unknowns + 1 # columns
		self.matrix = []
		self.parseEquation()
		self.t = time.time()
		try:
			self.gaussElimate()
		except ValueError:
			pass

	def __repr__(self):
		return " " + str(self.matrix)[1:-1]

	def parseEquation(self):
		self.dim1 = int(input("Number of equations: "))
		self.dim2 = int(input("Number of variables: ")) + 1
		self.matrix = np.zeros((self.dim1,self.dim2),dtype=np.float64)
		print("Example: 1x + 0y + -2z = 3 -> 1 0 -2 : 3")
		for i in range(self.dim1):
			s1 = input("Equation {0} => ".format(i+1))
			assert ":" in s1
			s2 = [j.strip() for j in s1.split(":")]
			s3 = s2[0].split(" ")
			s3.append(s2[1])

			tmp = [int(s3[j]) for j in range(self.dim2)]
			self.matrix[i] = tmp

	def getFirstNotZeroCoeff(self,row):
		for i in self.matrix[row][:-1]: # last value in the matrix row is the constant
			if i != 0:
				return i
		print("Error") # this happens if all coeff == 0
		if not any(self.matrix[row]):
			print("Infinite Solutions!")
		else:
			print("No solution")
		raise ValueError

	def getFirstNotZeroFirstCoeffRow(self):
		for row in range(self.dim1):
			if self.matrix[row][0] != 0:
				return row

	def matrixSwitch(self,a,b):
		print("Switching R{0} <--> R{1}".format(a+1,b+1))
		tmp = self.matrix[a]
		self.matrix[a] = self.matrix[b]
		self.matrix[b] = tmp

	def matrixDivide(self,row,divisor):
		print("Dividing R{0} by {1}".format(row+1,divisor))
		self.matrix[row] = self.matrix[row] / divisor

	def matrixAdd(self, column, row):
		coeff = self.matrix[row][column]
		print("Adding ({0})R{1} to R{2}".format(-coeff,column+1,row+1))
		self.matrix[row] = self.matrix[row] + (-coeff * self.matrix[column])

	def cleanup(self):
		for row in range(self.dim1):
			for column in range(self.dim2):
				if self.matrix[row][column] == 0:
					self.matrix[row][column] = 0

	def gaussElimate(self):
		# Gaussion elimination to obtain row-echelon form
		for columnNum in range(self.dim2 - 1):
			row = self.getFirstNotZeroFirstCoeffRow()
			if row != 0:
				self.matrixSwitch(columnNum, row)
				print(repr(self))
			coeff = self.getFirstNotZeroCoeff(columnNum)
			self.matrixDivide(columnNum, coeff)
			self.cleanup()
			print(repr(self))
			for rowNum in range(columnNum + 1, self.dim1):
				if self.matrix[rowNum][columnNum] != 0:
					self.matrixAdd(columnNum,rowNum)
					print(repr(self))
					self.getFirstNotZeroCoeff(rowNum)
		print("Achieved row-echelon form")
		# Gauss-Jordan elimination to obtain the solution
		for columnNum in range(1, self.dim2 - 1):
			for rowNum in range(0,columnNum):
				self.matrixAdd(columnNum, rowNum)
				print(self)
