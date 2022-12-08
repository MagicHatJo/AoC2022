
def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = fd.read().split()
		data = [line.split(",") for line in data]
		data = [(line[0].split("-"), line[1].split("-")) for line in data]
		data = [((int(line[0][0]), int(line[0][1])), ((int(line[1][0]), int(line[1][1])))) for line in data]
		return data

def check_containment(pair):
	return ((pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or
			(pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]))

def check_overlap(pair):
	return ((pair[0][0] <= pair[1][1] and pair[0][1] >= pair[1][0]) or
			(pair[1][0] <= pair[0][1] and pair[1][1] >= pair[0][0]))

def solution_one(data):
	return len(list(filter(check_containment, data)))

def solution_two(data):
	return len(list(filter(check_overlap, data)))

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()