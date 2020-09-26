tile = ['.', '_', '\\', '-', '/', '|', '*']

class Lawn:
	def __init__(self, flowers):
		self.lines = flowers.split('\n')

		self.width = len(self.lines[0])
		self.height = len(self.lines)

	def count(self, tile_type='*'):
		amount = 0

		for w in range(self.width):
			for h in range(self.height):
				value = tile.index(self.lines[h][w]) - 2

				if value > 0:
					value += self.width - w - 1

					if value >= 6:
						value = 6
				else:
					value = 0

				if tile[value] == tile_type:
					amount += 1

		return amount

with open("lawn.txt", 'r') as file:
	lawn_data = file.read()

lawn = Lawn(lawn_data)
print(lawn.count())