import numpy as np

def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = fd.read().split()
		return data

def get_shared(line):
	return "".join(set(line[:len(line)//2]).intersection(line[len(line)//2:])) 

def get_priority(c):
	result = ord(c) - ord('a') + 1
	if result < 0:
		result += ord('a') - ord('A') + 26
	return result

def get_badge(group):
	return "".join(set(group[0]).intersection(group[1]).intersection(group[2]))

def solution_one(data):
	return sum([get_priority(get_shared(line)) for line in data])

def solution_two(data):
	return sum([get_priority(get_badge(group)) for group in np.array(data).reshape(len(data) // 3, 3)])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()