import sys

for line in open(sys.argv[1]):
	line_list = line.strip().split('\t')
	print len(line_list)
