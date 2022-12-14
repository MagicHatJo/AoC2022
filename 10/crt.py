class CPU:
	def __init__(self):
		self.x = 1
		self.cycle = 0
		self.queued = None
		self.save = []
		self.table = {}
	
	def step(self):
		self.cycle += 1
		if self.cycle in self.save:
			self.table[self.cycle] = self.x

	def execute(self, cmd, *args):
		if cmd == "addx":
			self.queued = args[0]
			
	def resolve(self):
		self.x += self.queued
		self.queued = None
	
	@property
	def signal_strength(self):
		return sum([k * v for k, v in self.table.items()])

class CRT:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = [["." for _ in range(width)] for _ in range(height)]
	
	def update(self, cycle, x):
		overlap = abs(cycle % self.width - x) <= 1
		self.screen[cycle // self.width][cycle % self.width] = "#" if overlap else "."
	
	def display(self):
		for row in self.screen:
			for sprite in row:
				print(sprite, end="")
			print()

def parse_data(file_name):
	def cut(row):
		row = row.split(" ")
		return (row[0], int(row[1]) if len(row) == 2 else "")

	with open(file_name, "r") as fd:
		data = list(map(cut, fd.read().split("\n")))
		return data

def solution_one(data):
	cpu = CPU()
	cpu.save = [i for i in range(20, 221, 40)]
	total_cycles = 220
	for cycle in range(total_cycles):
		cpu.step()
		if cpu.queued is None:
			cpu.execute(*data.pop(0))
		else:
			cpu.resolve()
	return cpu.signal_strength

def solution_two(data):
	cpu = CPU()
	crt = CRT(40, 6)
	total_cycles = 240
	for cycle in range(total_cycles):
		crt.update(cycle, cpu.x)
		cpu.step()
		if cpu.queued is None:
			cpu.execute(*data.pop(0))
		else:
			cpu.resolve()
	crt.display()
	return None

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()