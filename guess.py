# 猜數字
import random
start = int(input('請決定隨機數字的初始值:'))
end = int(input('請決定隨機數字的最終值:'))

r = random.randint(start,end)
count = 0
while True:
	count = count + 1
	num = input('請猜數字:')
	num = int(num)
	if num == r:
		print('你猜中了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')	