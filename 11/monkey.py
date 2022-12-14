import math

class Monkey:
	def __init__(self, info):
		self.inspection_count = 0
		self.__parse(info)

	def throw(self, lcm = None):
		out_queue = []
		self.inspection_count += len(self.held_items)
		for old in self.held_items:
			old = eval(self.operation)
			old = old // 3 if lcm is None else old % lcm
			out_queue.append((self.toss[old % self.test == 0], old))
		self.held_items = []
		return out_queue
	
	def catch(self, item):
		self.held_items.append(item)

	def __parse(self, info):
		info            = info.split("\n")
		self.id         = int(info[0].split()[1][:-1])
		self.held_items = [int(num) for num in info[1].split(":")[1].split(", ")]
		self.operation  = info[2].split(" = ")[1]
		self.test       = int(info[3].split()[-1])
		self.toss       = {
			True  : int(info[4].split()[-1]),
			False : int(info[5].split()[-1])
		}

	def __repr__(self):
		return str(self.inspection_count)
	
	def __lt__(self, other):
		return self.inspection_count < other.inspection_count

def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = fd.read().split("\n\n")
		return data

def get_monkey_business(troop):
	troop.sort()
	return troop[-1].inspection_count * troop[-2].inspection_count

def solution_one(data):
	troop = [Monkey(info) for info in data]
	for _ in range(20):
		for monkey in troop:
			for reciever, item in monkey.throw():
				troop[reciever].catch(item)
	return get_monkey_business(troop)

def solution_two(data):
	troop = [Monkey(info) for info in data]
	lcm = math.prod([monkey.test for monkey in troop])
	for _ in range(10000):
		for monkey in troop:
			for reciever, item in monkey.throw(lcm):
				troop[reciever].catch(item)
	return get_monkey_business(troop)

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()