class Coordinate:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
	
	def move(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f"({self.x}, {self.y})"
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __eq__(self, other):
		return (self.x, self.y) == (other.x, other.y)
	
	def __hash__(self):
		return hash((self.x, self.y))

def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = fd.read().split("\n")
		return data

def step(current, next):
	if current.x > next.x:
		return Coordinate(current.x - 1, current.y)
	elif current.x < next.x:
		return Coordinate(current.x + 1, current.y)
	elif current.y > next.y:
		return Coordinate(current.x, current.y - 1)
	elif current.y < next.y:
		return Coordinate(current.x, current.y + 1)
	return next

def generate_paths(data):
	cave = {}
	for path in data:
		coord_list = [Coordinate(*pair.split(",")) for pair in path.split(" -> ")]
		for current, next in zip(coord_list[:-1], coord_list[1:]):
			while current != next:
				cave[current] = "#"
				current = step(current, next)
			cave[current] = "#"	
	return cave

def get_abyss(cave):
	return max([c.y for c in cave])

def get_next(grain, cave):
	x, y = grain.x, grain.y + 1
	if Coordinate(x, y) not in cave:
		return (x, y)
	if Coordinate(x - 1, y) not in cave:
		return (x - 1, y)
	if Coordinate(x + 1, y) not in cave:
		return (x + 1, y)
	return None

def drop(grain, cave, y_limit):
	next = get_next(grain, cave)
	while grain.y < y_limit and next:
		grain.move(*next)
		next = get_next(grain, cave)

	if grain.y < y_limit:
		cave[grain] = "o"
		return False
	cave[Coordinate(grain.x, grain.y)]     = "#"
	cave[Coordinate(grain.x - 1, grain.y)] = "#"
	cave[Coordinate(grain.x + 1, grain.y)] = "#"
	return True

def solution_one(data):
	cave = generate_paths(data)
	origin = Coordinate(500, 0)
	y_limit = get_abyss(cave)

	abyss = False
	while not abyss:
		grain = Coordinate(origin.x, origin.y)
		abyss = drop(grain, cave, y_limit)

	return len(list(filter(lambda x: cave[x] == "o", cave)))

def solution_two(data):
	cave = generate_paths(data)
	origin = Coordinate(500, 0)
	floor = get_abyss(cave) + 2

	while origin not in cave:
		grain = Coordinate(origin.x, origin.y)
		drop(grain, cave, floor)

	return len(list(filter(lambda x: cave[x] == "o", cave)))

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()