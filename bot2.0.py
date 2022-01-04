import telebot
import requests
from telebot import custom_filters
from  bs4 import BeautifulSoup as BS

r=requests.get("http://uevi.firat.edu.tr/")

soup = BS(r.content,"html.parser")
soup.prettify()
food_name=soup.find_all('div',{'class':'field-content'})

info=food_name[7].text.strip()

API_KEY="key"
bot =telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message,"Günün yemeği seni bekliyor {name}, şimdiden afiyet olsun".format(name=message.from_user.first_name))

@bot.message_handler(text=['yemek','yeme','yem','ye','y','food','foo','fo','f','fod','ymk'])
def say_hello(message):  
	bot.send_message(message.chat.id, info)


bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.infinity_polling()