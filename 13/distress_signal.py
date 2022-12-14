import ast
import itertools
import functools

def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = fd.read().split("\n\n")
		data = [[ast.literal_eval(line) for line in pair.split("\n")] for pair in data]
		return data

def is_valid(left, right):
	match (left, right):
		case (int(), int()):
			if left == right:
				return 0
			return -1 if left < right else 1
		case (int(), list()):
			return is_valid([left], right)
		case (list(), int()):
			return is_valid(left, [right])
		case (list(), list()):
			for l, r in itertools.zip_longest(left, right):
				v = is_valid(l, r)
				if v is not 0:
					return v
			return is_valid(len(left), len(right))
	return 0

def solution_one(data):
	return sum(i + 1 for i, (left, right) in enumerate(data) if is_valid(left, right) == -1)

def solution_two(data):
	divider_packets = [[[2]], [[6]]]
	data = sum(data, []) + divider_packets
	data.sort(key=functools.cmp_to_key(is_valid))
	return functools.reduce(lambda x, y: x * y, [data.index(packet) + 1 for packet in divider_packets])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()