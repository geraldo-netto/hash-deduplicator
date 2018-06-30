#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


if len(sys.argv) < 2:
	print("Usage: %s <hash-file>" % (sys.argv[0]))
	sys.exit(0)


duplicates = []
file = None

try:
	file_equal = 0
	file_curr = ''
	file = open(sys.argv[1], 'r')
    # TODO implement mmap
	file_lines = file.readlines()
	file_total_lines = len(file_lines)

    # TODO improve loop
	for line in range(0, file_total_lines -1):
		if file_lines[line +1]:
			file_curr = file_lines[line].replace('\n', '')
			file_next = file_lines[line +1].replace('\n', '')
			if file_curr.split(' ')[0] == file_next.split(' ')[0]:
				file_equal += 1
				if file_curr not in duplicates:
					duplicates.append(file_curr[26:])
				if file_next not in duplicates:
					duplicates.append(file_next[26:])

	file.close()

	for duplicate in duplicates:
		print(duplicate)

	print("equal files: %d / %d" % (file_equal, file_total_lines))


except Exception, ex:
    if file:
    	# file lock may raise exception
    	# if it's streaming data and the process is killed
    	# eg: control + c during deduplication
        file.close()
    else:
    	print(ex)

