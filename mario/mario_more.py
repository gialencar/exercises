height = int(input("Height: "))


for line in range(1, height + 1):
	print(' ' * (height - line), end='')
	print('#' * line, end='')
	
	print(' ', end='')

	print('#' * line)