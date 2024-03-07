real_password = 'a123456'
chance = 3 # 剩餘機會
while chance > 0:
	password = input('請輸入密碼: ')
	if password == real_password:
		print('登入成功!')
		break   # 逃出迴圈
	else:
		chance = chance - 1
		print('密碼錯誤!還有', chance, '次機會')