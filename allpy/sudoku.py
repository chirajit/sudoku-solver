class Sudoku:
	def __init__(self, dikt):
		self.grid = []
		self.given = []
		for i in range (9):
			row = []
			for j in range (9):
				if (dikt[i*9+j]) :
					row.append(int(dikt[i*9+j]))
				else :
					row.append(0)
			self.grid.append(row)

		for i in range(9):
			for j in range (9):
				if(self.grid[i][j]):
					self.given.append([i, j])
		self.solutions = []


	def valid(self, row, col, n):
		if (n in self.grid[row]):
			return False
		for i in range(9):
			if self.grid[i][col] == n :
				return False
		sr, sc = row - row%3, col - col%3

		for i in range(sr, sr+3):
			for j in range(sc, sc+3):
				if (self.grid[i][j] == n):
					return False
		return True

	def solve(self, row, col):
		if (len(self.solutions) < 10):
			if (row == 8 and col ==8):
				if (self.grid[row][col] != 0):
					ans = [self.grid[i].copy() for i in range(9)]
					self.solutions.append(ans)
				else:
					for i in range(1, 10):
						if (self.valid(8, 8, i)):
							self.grid[8][8] = i
							ans = [self.grid[i].copy() for i in range(9)]
							self.solutions.append(ans)
							self.grid[8][8] = 0
							if (len(self.solutions) >=10) :
								break
			else:
				if (col > 8) :
					row, col = row+1, 0
				if (self.grid[row][col] == 0):
					for i in range (1, 10):
						if (self.valid(row, col, i)):
							self.grid[row][col] = i
							self.solve(row, col+1)
							self.grid[row][col] = 0
				else:
					self.solve(row, col+1)
