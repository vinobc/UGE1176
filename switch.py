import datetime
now = datetime.datetime.now()
# print(now)
today = now.strftime("%A")
# print(today)

# if today == 'Monday' :
# 	print('learn Java')
# elif today == 'Tuesday':
# 	print('learn Python')
# elif today == 'Wednesday':
# 	print('learn Angular')
# elif today == 'Thursday':
# 	print('learn Swift')
# elif today == 'Friday':
# 	print('learn Android')
# elif today == 'Saturday':
# 	print('learn Ruby on Rails')
# elif today == 'Sunday':
# 	print('learn Django')

languages = {'Monday' : 'Java',
	         'Tuesday' : 'C++',
	         'wednesday' : 'Angular',
	         'Thursday' : 'Swift',
	         'Friday' : 'Andrid', 
	         'Saturday' : 'Ruby on Rails',
	         'Sunday' : 'Django'
			}

def learn(day):
	# language = languages[day]
	language = languages.get(day,'invalid day specified..')
	print(language)

# try:
learn(today)
# except KeyError as e:
	# print('invalid day..:{}'.format(e))
