from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


locjson = {}
budget = ""
emo = ""


#Registering the updater and dispatcher
updater = Updater(token='768461777:AAFE5txqPI7Rh5bkt7a5l4VndmA1LmosVbk')
dispatcher = updater.dispatcher


#For the start command
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm Alcobot, please send your budget, location and picture to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()


#For handling the budget
def echo(bot, update):
	budget = update.message.text
	textmess = "Your budget is £" + str(update.message.text)
	bot.send_message(chat_id=update.message.chat_id, text=textmess)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

#For photos
def photo(bot, update):
    file_id = update.message.photo[-1].file_id
    newFile = bot.getFile(file_id)
    newFile.download('test.jpg')
    bot.sendMessage(chat_id=update.message.chat_id, text="Got your picture mate!")
    imagerec()

def imagerec():
	url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"
	querystring = {"returnFaceId":"true","returnFaceLandmarks":"false","returnFaceAttributes":"emotion,age,gender"}

	image_path = "/Users/AkshayC/Desktop/test.jpg"
	image_data = open(image_path, "rb").read()

	headers = {
		'Ocp-Apim-Subscription-Key': "9495f13ff2764d0f87daec1d820257e8",
		'Content-Type': "application/octet-stream",
		'cache-control': "no-cache",
		'Postman-Token': "67ac9f11-e73a-430f-aca3-eb71b7dcc0a5"
		}	

	response = requests.request("POST", url, data=image_data, headers=headers, params=querystring)

	age = int(response.json()[0]["faceAttributes"]["age"])
	emotion = response.json()[0]["faceAttributes"]["emotion"]

	maxint = -0.5

	for key in emotion:
		if (emotion[key] > maxint):
			maxint = emotion[key]
			emo = key
	
	#print(maxint)
	print(emo)
	print(age)

photo_handler = MessageHandler(Filters.photo, photo)
dispatcher.add_handler(photo_handler)

#For the Location
def location(bot, update):

	print(update.message.location)
	bot.sendMessage(chat_id=update.message.chat_id, text=str(update.message.location))


location_handler = MessageHandler(Filters.location, location, edited_updates=True)
dispatcher.add_handler(location_handler)