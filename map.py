import sys

for line in sys.stdin:

	data = line.strip().split("\t")
	if len(data) == 3:
		url, name, detail = data
		print "{0}\t{1}".format(name, detail)
