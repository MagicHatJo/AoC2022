
def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = fd.read()
		return data

def get_unique(data, size):
	i = 0
	while i < len(data) - size:
		if len(set(data[i:i + size])) == size:
			return i + size
		i += 1
	return 0

def solution_one(data):
	return get_unique(data, 4)

def solution_two(data):
	return get_unique(data, 14)

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()