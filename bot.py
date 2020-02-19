import telebot
import pyowm
import random
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru" )
bot = telebot.TeleBot("1055842149:AAEdiE2Ct01Gv3jgXlRaU2-vFSxy4mbwD0Q")

lib = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
ran = 0;


#список из игр в наличии с ценой
games = [
["Resident Evil 2", 1200, "PS4"],
["Resident Evil 6", 600, "PS3"],
["Evil Within", 1000, "PS4"],
["Evil Within 2", 1200, "PS4"],
["Evil Within 2", 1200, "Xbox One"],
["DOOM", 800, "Xbox One"],
["DOOM", 800, "PS4"],
["BioShock", 1600, "PC"]
]

platforms = [
"grsspordf", #пустой для пропуска 0 
"ps3", "playstation3", #1 & 2
'ps4', 'playstation4', #3 & 4
"xbox360", "x360", #5 & 6
"xboxone", "xone", #7 & 8
"pc" #9
]

@bot.message_handler(content_types=['text'])
def send_echo(message):
	search_name = message.text
	search_name = search_name.lower()

	name = ""
	for i in search_name:
		if i in lib:
			name += i

	platform_number = 0;
	count_platforms = 0;
	while count_platforms < len(platforms):
		if platforms[count_platforms] in name:
			name = name.replace(platforms[count_platforms],'')
			platform_number = count_platforms
			break
		count_platforms += 1

	work_name = ""
	show_name = ""
	list_len = len(games)
	count = 0;
	count_says = 0;
	awnser = ""
	while count < list_len:
		for i in games[count][0]:
			if i in lib:
				work_name += i;
			work_name = work_name.lower()
		if (name in work_name) and (name != ""):
			if platform_number == 0:
				show_name = games[count]
				if count_says == 0:
					awnser += "По вашему запросу мы нашли:\n"
					count_says += 1;
				awnser += str(show_name[0]) + " для " + str(show_name[2]) + " за " + str(show_name[1]) + " рублей. \n"
				count += 1
				work_name = ""
			elif (platform_number == 3) or (platform_number == 4):
				show_name = games[count]
				if str(show_name[2]) == str("PS4"):
					if count_says == 0:
						awnser = "По вашему запросу мы нашли:\n"
						count_says += 1;
					awnser += str(show_name[0]) + " для " + str(show_name[2]) + " за " + str(show_name[1]) + " рублей. \n"
					count += 1
					work_name = ""
				else:
					count += 1
					work_name = ""
					awnser += " "
			elif (platform_number == 1) or (platform_number == 2):
				show_name = games[count]
				if str(show_name[2]) == str("PS3"):
					if count_says == 0:
						awnser = "По вашему запросу мы нашли:\n"
						count_says += 1;
					awnser += str(show_name[0]) + " для " + str(show_name[2]) + " за " + str(show_name[1]) + " рублей. \n"
					count += 1
					work_name = ""
				else:
					count += 1
					work_name = ""
					awnser += " "
			elif (platform_number == 7) or (platform_number == 8):
				show_name = games[count]
				if str(show_name[2]) == str("Xbox One"):
					if count_says == 0:
						awnser = "По вашему запросу мы нашли:\n"
						count_says += 1;
					awnser += str(show_name[0]) + " для " + str(show_name[2]) + " за " + str(show_name[1]) + " рублей. \n"
					count += 1
					work_name = ""
				else:
					count += 1
					work_name = ""
					awnser += " "	
			elif (platform_number == 5) or (platform_number == 6):
				show_name = games[count]
				if str(show_name[2]) == str("Xbox 360"):
					if count_says == 0:
						awnser = "По вашему запросу мы нашли:\n"
						count_says += 1;
					awnser += str(show_name[0]) + " для " + str(show_name[2]) + " за " + str(show_name[1]) + " рублей. \n"
					count += 1
					work_name = ""
				else:
					count += 1
					work_name = ""
					awnser += " "
			elif platform_number == 9:
				show_name = games[count]
				if str(show_name[2]) == str("PC"):
					if count_says == 0:
						awnser = "По вашему запросу мы нашли:\n"
						count_says += 1;
					awnser += str(show_name[0]) + " для " + str(show_name[2]) + " за " + str(show_name[1]) + " рублей. \n"
					count += 1
					work_name = ""
				else:
					count += 1
					work_name = ""
					awnser += " "				
			else: 
				count += 1
				work_name = ""
		else:
			count += 1
			work_name = ""
		
	if (show_name == "") or len(awnser) < 30:
		awnser = ("Мы не смогли ничего найти по вашему запросу :с")

	if "погода" in search_name:
		observation = owm.weather_at_place('Новосибирск')
		w = observation.get_weather()
		temp = w.get_temperature('celsius')["temp"]
		awnser = "В Новосибирске сейчас " + w.get_detailed_status() + "\n"
		awnser += "Температура в районе " + str(temp) + " градусов." "\n\n"
		if temp < 5:
			awnser +=  "На улице холодно :c"
		elif temp < 15:
			awnser += "На улице нормально :)" 
		else:
			awnser +=  "На улице очень тепло :D " 

	if "спасибо" in search_name:
		ran = random.randint(1,3)
		if ran == 1:
			awnser = "Пожалуйста. Обращайся ;)"
		elif ran == 2:
			awnser = "Всегда рад помочь ;)"
		elif ran == 3:
			awnser = "Это моя работа! Не стоит благодарности ;)"

	if "благодарю" in search_name:
		ran = random.randint(1,3)
		if ran == 1:
			awnser = "Пожалуйста. Обращайся ;)"
		elif ran == 2:
			awnser = "Всегда рад помочь ;)"
		elif ran == 3:
			awnser = "Это моя работа! Не стоит благодарности ;)"

	if "я" and "люблю" and "тебя" in search_name:
		awnser = "Я тоже тебя люблю <3"

	if "привет" in search_name:
		bot.send_message(message.chat.id, 'Приветсвую тебя :) \nКак твои дела?')

	bot.send_message(message.chat.id, awnser)
bot.polling( none_stop = True )