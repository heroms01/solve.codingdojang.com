#!/usr/bin/python
# -*- coding: utf8 -*-

#입력된 파일의 탭을 공백 4개로 변경
import sys

# 시스템 매개변수로 파일명 받아서 처리
args = sys.argv[1:]
filename = args[0]

try:
	with open(filename, 'rb') as tab_file:
		source = tab_file.readlines()			# 파일내 글 모두 읽는다.
		target = "".join(source)				# 읽어온 데이터는 list 타입이라 스트링으로 변환
		target = target.replace("\t", "    ")		# 탭을 공백으로 변환

		with open('space4.txt','wb') as space_file:
			space_file.write(target)			# 새로운 파일에 저장
except IOError as err:
	print('File error: ' + str(err))