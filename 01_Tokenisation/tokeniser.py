import sys
import re
def tokenize(input_string):
	tokens = re.findall("[\w]+", input_string)
	return tokens

if __name__ == '__main__':
	while True:
		line = sys.stdin.readline()
		if line == '':
			break
		output = tokenize(line)
		print(output)
