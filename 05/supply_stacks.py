import re

def make_stacks(stack_data):
	stack_list = [[] for _ in range(10)]
	stack_data = stack_data.split("\n")
	for row in stack_data[:-1]:
		for i in range(1, len(row), 4):
			if row[i] != " ":
				stack_list[i // 4 + 1].insert(0, row[i])
	return stack_list

def parse_data(file_name):
	with open(file_name, "r") as fd:
		stack_data, move_data = fd.read().split("\n\n")
		return make_stacks(stack_data), [re.findall(r'\d+', line) for line in move_data.split("\n")]

def solution_one(data):
	stacks, moves = data
	for move in moves:
		stacks[int(move[2])] += stacks[int(move[1])][-1 * int(move[0]):][::-1]
		stacks[int(move[1])] = stacks[int(move[1])][:-1 * int(move[0])]
	return "".join([row[-1] for row in stacks if row])

def solution_two(data):
	stacks, moves = data
	for move in moves:
		stacks[int(move[2])] += stacks[int(move[1])][-1 * int(move[0]):]
		stacks[int(move[1])] = stacks[int(move[1])][:-1 * int(move[0])]
	return "".join([row[-1] for row in stacks if row])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()