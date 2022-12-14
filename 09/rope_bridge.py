class Coordinate():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	@property
	def value(self):
		return (self.x, self.y)
	
	def __repr__(self):
		return f"({self.x}, {self.y})"

class Head(Coordinate):
	def move(self, dir):
		self.x, self.y = {
			"L" : (self.x - 1, self.y),
			"R" : (self.x + 1, self.y),
			"U" : (self.x, self.y - 1),
			"D" : (self.x, self.y + 1)
		}[dir]

class Tail(Coordinate):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.visited = set()

	def follow(self, x, y):
		dx = x - self.x
		dy = y - self.y
		if dy == 0 and abs(dx) > 1:
			self.x += 1 if dx > 0 else -1
		elif dx == 0 and abs(dy) > 1:
			self.y += 1 if dy > 0 else -1
		elif abs(dy) > 1 or abs(dx) > 1:
			self.x += 1 if dx > 0 else -1
			self.y += 1 if dy > 0 else -1
		self.visited.add((self.x, self.y))

def parse_data(file_name):
	def cut(row):
		row = row.split(" ")
		return (row[0], int(row[1]))

	with open(file_name, "r") as fd:
		data = list(map(cut, fd.read().split("\n")))
		return data

def make_queue(data):
	move_queue = []
	for dir, times in data:
		for _ in range(times):
			move_queue.append(dir)
	return move_queue

def solution_one(data):
	move_queue = make_queue(data)
	head = Head(0, 0)
	tail = Tail(0, 0)
	for dir in move_queue:
		head.move(dir)
		tail.follow(head.x, head.y)
	return len(tail.visited)

def solution_two(data):
	move_queue = make_queue(data)
	head = Head(0, 0)
	rope = [Tail(0, 0) for _ in range(9)]
	for dir in move_queue:
		head.move(dir)
		x = head.x
		y = head.y
		for tail in rope:
			tail.follow(x, y)
			x = tail.x
			y = tail.y	
	return len(rope[-1].visited)

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Example 2 : {solution_two(parse_data('example01.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()