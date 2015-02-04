#!/usr/bin/python
# -*- coding: utf8 -*-

# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

limit = 1000

x = [n for n in xrange(limit) if n % 3== 0 or n % 5== 0]

# 리스트 합계 더하기
print(sum(x))

# for i in xrange(limit):
# 	temp = 3*i
# 	if temp >= limit:
# 		break
# 	print(temp)
# 	result += temp

# for i in xrange(limit):
# 	temp = 5*i
# 	if temp >= limit:
# 		break
# 	print(temp)	
# 	result += temp


# print(result)