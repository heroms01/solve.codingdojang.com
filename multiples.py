#!/usr/bin/python
# -*- coding: utf8 -*-

# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

# for문을 이용한 방법
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

# 파이썬 다운 방법
# limit = 1000
# x = (n for n in xrange(limit) if n % 3== 0 or n % 5== 0)

# # 리스트 합계 더하기
# print(sum(x))


# 수학적 방법
"""
Let’s look at the details of our function and take as example n=3.
We would have to add:
3+6+9+12+......+999=3*(1+2+3+4+...+333)
For n=5 we would get:
5+10+15+...+995=5*(1+2+....+199)
Now note that 199=995/5 but also 999/5 rounded down to the nearest integer.
In many programming languages there exists a separate operator for that: div or \.
If we now also note that 1+2+3+...+p=½*p*(p+1) our program becomes:
"""
def mul(n):
	p = limit / n
	return n*(p*(p+1)) / 2

limit = 999
print(mul(3)+mul(5)-mul(15))
