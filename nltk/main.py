import sorting

f = open('tweets.txt', 'r')

for line in f:
	print sorting.sorter(line)
	

# sorting.anotherTest()