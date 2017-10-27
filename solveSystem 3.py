
#
# so elimination?
# 
# matrix based approach
#

class GaussianElimination:

	def __init__(self,unknowns,equations=None):
		self.matrix = []
		if equations == None:
			self.dim1 = unknowns # rows
		else:
			self.dim1 = equations # rows
		self.dim2 = unknowns + 1 # columns

		#self.abc = "abcdefghijklmnopqrstuvwxyz"

		self.matrix = \
		[
			[0.5, 1, 1, 128],
			[2, 2, 1, 80],
			[4.5, 3, 1, 0]

		]
		'''self.matrix = \
                [
                        [3,-1,9],
                        [1,-2,-2]
                ]'''
		#self.parseEquation()
		try:
			self.gaussElimate()
		except ValueError:
			pass
		#print(self)

	def __repr__(self):
		s = ""
		for row in self.matrix:
			for i in range(len(row)):
				if len(str(row[i])) > 5:
					row[i] = float(str(row[i])[:6])
				if i != len(row) - 1:
					s += "{0}\t".format(row[i])
				else:
					s += ": {0}\n".format(row[i])

		return s

	def parseEquation(self):
		print("Example: 1x + 0y + -2z = 3 -> 1 0 -2 : 3")
		for i in range(self.dim1):
			tmp = [0 for j in range(self.dim2)]
			s1 = input("Equation {0} => ".format(i+1))
			assert ":" in s1
			s2 = s1.split(":")
			s2 = [j.strip() for j in s2]

			s3 = s2[0].split(" ")
			s3.append(s2[1])
			#s3 = [j.strip() for j in s3]

			#print(s3)
			for j in range(self.dim2):
				tmp[j] = int(s3[j])

			self.matrix.append(tmp)

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
		tmp = self.matrix[a]
		self.matrix[a] = self.matrix[b]
		self.matrix[b] = tmp

	def matrixDivide(self,row,divisor):
		self.matrix[row] = [value / divisor for value in self.matrix[row]]

	def matrixAdd(self, column, row):
		coeff = self.matrix[row][column]
		tmp = [i * -coeff for i in self.matrix[column]]
		self.matrix[row] = [i + j for i, j in zip(self.matrix[row],tmp)]
		# check for inf / no solution

	def cleanup(self):
		for row in range(self.dim1):
			for column in range(self.dim2):
				if self.matrix[row][column] == 0:
					self.matrix[row][column] = 0

	def gaussElimate(self):
		# Gaussion elimination to obtain row-echelon form
		for columnNum in range(self.dim2 - 1):
			row = self.getFirstNotZeroFirstCoeffRow()
			print("Switching rows\n" + repr(self))
			if row != 0:
				self.matrixSwitch(columnNum, row)
			coeff = self.getFirstNotZeroCoeff(columnNum)
			self.matrixDivide(columnNum, coeff)
			self.cleanup()
			print("Dividing rows\n" + repr(self))
			for rowNum in range(columnNum + 1, self.dim1):
				if self.matrix[rowNum][columnNum] != 0:
					self.matrixAdd(columnNum,rowNum)
					print("Adding rows\n" + repr(self))
					self.getFirstNotZeroCoeff(rowNum)
		print("Achieved row-echelon form")
		# Gauss-Jordan elimination to obtain the solution
		for columnNum in range(1, self.dim2 - 1):
			for rowNum in range(0,columnNum):
				self.matrixAdd(columnNum, rowNum)
				print(self)





		

GaussianElimination(3)






