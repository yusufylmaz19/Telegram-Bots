import telebot
from selenium import webdriver
from webdriver_manager import driver

driver = webdriver.Chrome("C:\\Users\\yy\\Downloads\\Compressed\\yandexdriver-21.11.0.1999-win\\yandexdriver.exe")
driver.implicitly_wait(0.5)

driver.minimize_window()
driver.get("http://uevi.firat.edu.tr")
l = driver.find_elements_by_css_selector(".views-row.views-row-1.views-row-odd.views-row-first>.views-field.views-field-body>.field-content>p")
info=""
for e in l:
    info +=e.text+"\n"
driver.quit()


API_KEY="key"
bot =telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message,"welcome")

@bot.message_handler(commands=['yemek'])
def say_hello(message):  
	bot.send_message(message.chat.id, info)
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()