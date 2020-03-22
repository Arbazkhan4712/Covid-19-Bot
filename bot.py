import telepot, time


def covidbot(msg):

	userName = msg['from']['first_name']+" "+msg['from']['last_name']

	content_type, chat_type, chat_id = telepot.glance(msg)

	if (content_type == 'text'):
		command = msg['text']
		print ('Got command: %s' % command)

		if  '/start' in command:
			bot.sendMessage(chat_id, "Hello , This is Covid-19 chatbot created by ARBAZ KHAN. You can use this bot for Updates on Covid-19.\n commands \n cases - to get all the cases of covid - 19\n deaths - to get number of deathsdue to covid - 19\n recovered - to get all the  recoverd cases of covid - 19 \n news  - to get all the lastest news of covid - 19\n top - to get an image of the top effected countries")

		if 'cases' in command:
			bot.sendMessage(chat_id, " Total cases of covid-19 Around the Globe = 308,609")


		if 'deaths' in command:
			bot.sendMessage(chat_id, "Total Deaths of covid-19 Around the Globe = 13,069 ")

		if 'recovered' in command:
			bot.sendMessage(chat_id, "Total Recovered of covid-19 Around the Globe = 95,834")

		if 'news' in command:
			bot.sendMessage(chat_id, "1. Concerns have been raised that a national 'state of emergency' is on the cards following a high powered meeting on Saturday between Treasury, the SA Reserve Bank and the SA Revenue Service.\n \n2. “Contain, contain, contain!” That is the message from National Treasury to the government, warning that the state should do “whatever it takes” to contain the spread of the Covid-19 coronavirus.\n \n3 Two coronavirus deaths were reported from Maharashtra's Mumbai and Bihar today, taking the total number of deaths linked to COVID-19 in India to six.\n \n4 The Delhi CM called for citizens to remain strong and united.")

		if 'precautions' in command:
			bot.sendMessage(chat_id,"1.Regular hand washing. \n 2. Covering mouth and nose when coughing and sneezing \n 3. If you are taking care of someone who is sick, try to stay 6 feet away – this is the distance virus-containing droplets can travel through a sneeze or cough \n 4. Avoid close contact with anyone showing symptoms of respiratory illness such as coughing and sneezing. \n 5. Avoid touching your eyes, nose, and mouth \n 6. Clean and disinfect frequently touched objects and surfaces using a regular household cleaning spray or wipe.")
			bot.sendPhoto(chat_id, open("un.png", 'rb'))
			bot.sendPhoto(chat_id, open("pre.png", 'rb'))

		if 'symptoms' in command:
			bot.sendMessage(chat_id, "Reported illnesses have ranged from mild symptoms to severe illness and death for confirmed coronavirus disease 2019 (COVID-19) cases.These symptoms may appear 2-14 days after exposure (based on the incubation period of MERS-CoV viruses).\n1.Fever\n2.Cough\n3.Shortness of breath\n4.Trouble breathing\n5.Persistent pain or pressure in the chest\n6.New confusion or inability to arouse\n7.Bluish lips or face")
			bot.sendPhoto(chat_id, open("sy.png", 'rb'))


		if 'top' in command:
			bot.sendPhoto(chat_id, open("covid-1.png", 'rb'))

bot = telepot.Bot('APi_key')


bot.message_loop(covidbot)


while 1:
	time.sleep(20)


