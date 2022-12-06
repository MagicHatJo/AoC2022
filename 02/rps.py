
def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = fd.read().split("\n")
		return data

def selection_score(player):
	return {
		"X" : 1,
		"Y" : 2,
		"Z" : 3
	}[player]

def outcome_score(opponent, player):
	if (opponent, player) in set([("A", "Y"), ("B", "Z"), ("C", "X")]):
		return 6
	elif (opponent, player) in set([("A", "X"), ("B", "Y"), ("C", "Z")]):
		return 3
	return 0

def get_selection(opponent, outcome):
	return {
		"A" : {
			"X" : "Z",
			"Y" : "X",
			"Z" : "Y"
		},
		"B" : {
			"X" : "X",
			"Y" : "Y",
			"Z" : "Z"
		},
		"C" : {
			"X" : "Y",
			"Y" : "Z",
			"Z" : "X"
		}
	}[opponent][outcome]

def solution_one(data):
	return sum([selection_score(n[-1]) + outcome_score(n[0], n[-1]) for n in data])

def solution_two(data):
	return sum([selection_score(get_selection(n[0], n[-1])) + outcome_score(n[0], get_selection(n[0], n[-1])) for n in data])

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()