#!/usr/bin/python
# -*- coding: utf8 -*-

"""
주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

1. 김씨와 이씨는 각각 몇 명 인가요?
2. "이재영"이란 이름이 몇 번 반복되나요?
3. 중복을 제거한 이름을 출력하세요.
4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
"""
names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
#리스트로 변환
list_names = names.split(',')

cnt_k=0 #김씨 카운터
cnt_l=0  #이씨 카운터
cnt_j=0  #이재영 카운터

#각각 카운터 
for name in list_names:
	if name[0:3] == '김':
		cnt_k += 1
	if name[0:3] == '이':
		cnt_l += 1
	if name == '이재영':
		cnt_j += 1

print("1. 김씨와 이씨는 각각 몇 명 인가요? 김씨: "+ str(cnt_k)+"명, 이씨: "+ str(cnt_l)+"명")
print("2. 이재영 이란 이름이 몇 번 반복되나요? "+ str(cnt_j) + "번")
#집합으로 변환하여 중복 제거
set_names = set(list_names)

print("3. 중복을 제거한 이름을 출력하세요.")
#중복제거 출력
for name in set_names:
	print(name)

print("4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.")
#오름차순 정렬 출력
for name in sorted(set_names):
	print(name)