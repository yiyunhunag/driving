country = input('請輸入您的國家: ')
age = input('請輸入您的年齡: ')
age = int(age)
if country == '台灣':
	if age > 18:
		print('你可以考駕照')
	else:
		print('滾')
