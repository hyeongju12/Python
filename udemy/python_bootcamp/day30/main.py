try:
	file = open('a_file.txt')
except FileNotFoundError:
	file = open('a_file.txt', 'w')
	file.write("Something")
except KeyError as e:
	print(f"That key {e} does not exist")
else:
	content = file.read()
	print(content)
finally:
	raise TypeError("This is an eeror that I made up.")