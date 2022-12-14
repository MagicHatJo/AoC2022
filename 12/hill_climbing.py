def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = [[c for c in line] for line in fd.read().split("\n")]
		return data

def find(data, target):
	out = []
	for y, row in enumerate(data):
		for x, val in enumerate(row):
			if val == target:
				out.append((x, y))
	return out

def traverse(data, start_x, start_y, end_x, end_y):
	queue = [[[start_x, start_y]]]
	visited = set((start_x, start_y))
	while queue:
		path = queue.pop(0)
		x, y = path[-1]
		if (x, y) == (end_x, end_y):
			return path
		for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
			if (0 <= dx < len(data[0])  and
				0 <= dy < len(data)     and
				(dx, dy) not in visited and
				ord(data[dy][dx]) <= ord(data[y][x]) + 1):
				queue.append(path + [[dx, dy]])
				visited.add((dx, dy))
	return []

def solution_one(data):
	sx, sy = find(data, "S")[0]
	ex, ey = find(data, "E")[0]
	data[sy][sx] = 'a'
	data[ey][ex] = 'z'
	path = traverse(data, sx, sy, ex, ey)
	return len(path) - 1

def solution_two(data):
	sx, sy = find(data, "S")[0]
	ex, ey = find(data, "E")[0]
	data[sy][sx] = 'a'
	data[ey][ex] = 'z'
	start_list = find(data, "a")
	short_list = []
	for x, y in start_list:
		distance = len(traverse(data, x, y, ex, ey)) - 1
		if distance > 0:
			short_list.append(distance)
	return min(short_list)

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()