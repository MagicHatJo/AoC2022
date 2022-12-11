from functools import reduce

class Tree:
	def __init__(self, height):
		self.height = height
		self.visited = False
		self.visible = False
		self.scenic_score = 0
	
	def __repr__(self):
		return "\033[32m" + str(self.height) + "\033[0m" if self.visible else " "#str(self.height)
	
	def __gt__(self, other):
		match other:
			case Tree():
				return self.height > other.height
			case int():
				return self.height > other
	
	def __ge__(self, other):
		match other:
			case Tree():
				return self.height >= other.height
			case int():
				return self.height >= other

def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = [list(row) for row in fd.read().split("\n")]
		return [[Tree(int(n)) for n in row] for row in data]

def comb_left(data):
	for row in data:
		max_height = -1
		for tree in row:
			if tree > max_height:
				tree.visible = True
				max_height = tree.height

def rotate_matrix(data):
	return list(zip(*data[::-1]))

def count_visible(data):
	return len(list(filter(lambda x : x.visible, reduce(lambda x , y : x + y, data))))

def get_scenic(data, x, y, dx, dy):
	origin_tree = data[y][x]
	x += dx
	y += dy
	count = 0
	while ( 0 <= x < len(data[0]) and
			0 <= y < len(data)):
		count += 1
		if data[y][x] >= origin_tree:
			return count
		x += dx
		y += dy
	return count

def print_forest(data):
	for row in data:
		for tree in row:
			print(tree, end="")
		print()

def solution_one(data):
	for _ in range(4):
		comb_left(data)
		data = rotate_matrix(data)
	print_forest(data)
	return count_visible(data)

def solution_two(data):
	high_score = 0
	for y, row in enumerate(data):
		for x, tree in enumerate(row):
			tree.scenic_score = (
				get_scenic(data, x, y, -1,  0) *
				get_scenic(data, x, y,  1,  0) *
				get_scenic(data, x, y,  0, -1) *
				get_scenic(data, x, y,  0,  1)
			)
			if high_score < tree.scenic_score:
				high_score = tree.scenic_score
	return high_score

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()