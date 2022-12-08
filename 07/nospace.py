DIR_LIMIT        = 100000
TOTAL_DISK_SPACE = 70000000
REQUIRED_SPACE   = 30000000

class Directory:
	def __init__(self, parent_path, name):
		self.name = name
		self.parent_path = parent_path
		self.total_size = 0
		self.directories = []
		self.files = {}
	
	def add_file(self, file_name, file_size):
		self.files[file_name] = file_size
	
	def get_total(self):
		if self.total_size != 0:
			return self.total_size
		
		for dir in self.directories:
			self.total_size += dir.get_total()
		
		for file in self.files:
			self.total_size += self.files[file]
		
		return self.total_size
	
	def __add__(self, other):
		if type(other) == Directory:
			return self.total_size + other.total_size
		if type(other) == int:
			return self.total_size + other

def parse_data(file_name):
	with open(file_name, "r") as fd:
		data = fd.read().split("\n")
		return data

def execute_cd(current_path, target_path, dir_table):
	if target_path == "/":
		current_path = "/"
		dir_table["/"] = Directory("", "/")
	elif target_path == "..":
		current_path = current_path.rsplit("/", 1)[0]
	else:
		dir_table[current_path + "/" + target_path] = Directory(current_path, target_path)
		dir_table[current_path].directories.append(dir_table[current_path + "/" + target_path])
		current_path += "/" + target_path
	return current_path

def execute_ls(current_path, data, i, dir_table):
	while i < len(data) and data[i][0] != "$":
		cmd = data[i].split()
		if cmd[0] == "dir":
			dir_table[current_path + "/" + cmd[1]] = Directory(current_path, cmd[1])
		elif cmd[0].isdigit():
			dir_table[current_path].add_file(cmd[1], int(cmd[0]))
		i += 1

def create_table(data):
	dir_table = {}
	current_path = "/"
	i = 0
	while i < len(data):
		cmd = data[i].split()
		if cmd[0] == "$":
			if cmd[1] == "cd":
				current_path = execute_cd(current_path, cmd[2], dir_table)
			elif cmd[1] == "ls":
				execute_ls(current_path, data, i + 1, dir_table)
		i += 1
	return dir_table

def solution_one(data):
	dir_table = create_table(data)
	return sum(dir.total_size for dir in filter(lambda x: x.get_total() <= DIR_LIMIT, dir_table.values()))

def solution_two(data):
	dir_table = create_table(data)
	to_clear = REQUIRED_SPACE - (TOTAL_DISK_SPACE - dir_table["/"].get_total())
	candidates = [dir for dir in dir_table.values() if dir.get_total() >= to_clear]
	candidates.sort(key = lambda x : x.total_size)
	return candidates[0].total_size

def main():
	print(f"Example 1 : {solution_one(parse_data('example.txt'))}")
	print(f"Output  1 : {solution_one(parse_data('input.txt'))}")

	print("--------------------")
	print(f"Example 2 : {solution_two(parse_data('example.txt'))}")
	print(f"Output  2 : {solution_two(parse_data('input.txt'))}")

if __name__ == "__main__":
	main()