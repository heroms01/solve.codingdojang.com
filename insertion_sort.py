#!/usr/bin/python
# -*- coding: utf8 -*-

# INSERTION SORT

target = [5,2,4,6,1,3]

# 하나 작은 만큼 리스트를 반복함
for index in xrange(len(target)-1):
	# print(index)
	# print(target)
	# 현재 인덱스 값과 다음 값을 비교하기 위한 인덱스
	add_index = index+1
	# 다음값과 비교해서 다음값이 작을때
	# if (target[index] > target[add_index]):
	# 지나온 이전 인젝스를 다시 반복하면서
	for inner_index in xrange(add_index):
		# print('target[inner_index] = '+str(target[inner_index]) + ' target[index] = '+str(target[add_index]))
		# 값이 작으면 swap
		if (target[inner_index] > target[add_index]):
			temp = target[add_index]
			target[add_index] = target[inner_index]
			target[inner_index] = temp
			continue

print(target)
