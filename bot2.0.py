import telebot
import requests
from telebot import custom_filters
from  bs4 import BeautifulSoup as BS

r=requests.get("http://uevi.mdr.firat.edu.tr/")

soup = BS(r.content,"html.parser")
soup.prettify()
food_name=soup.find_all('div',{'class':'contain-text'})

foods=""
for i in range(len(food_name)):
    foods +=food_name[i].text

API_KEY="your key"
bot =telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message,"Günün yemeği seni bekliyor {name}, şimdiden afiyet olsun".format(name=message.from_user.first_name))

@bot.message_handler(text=['yemek','yeme','yem','ye','y','food','foo','fo','f','fod','ymk'])
def say_hello(message):  
	bot.send_message(message.chat.id, foods)


bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.infinity_polling()