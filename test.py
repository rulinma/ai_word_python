__author__ = 'rollin'

# import os
# import time
import datetime

print('Hello World!')
print('Time is ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A'))
print('__name__ value: ', __name__)


def main():
    print('this message is from main function')

list = []

def parse():
	print('parse txt')
	# read lines
	with open('/Users/rollin/word/git/parse_txt/classify3000.txt','r') as f:
		for line in f.readlines():
			data = line.split('\n\t')
			for str in data:
				sub_str = str.split(" ")
			for splitStr in sub_str:
				list.append(splitStr)
			# print(line)

	print(list)

	# TODO: for list 数字开头的保存 去除所有非字符串组成的数据（保留所有字符串单词)
	# 根据数字进行）

	# write 2 file classify1.txt - classifyN.txt
    # add 2 db

	# wordlist

if __name__ == '__main__':
    # main()
    # print(__name__)
    parse()