import threading
from wxpy import *
import requests
import configparser
cf = configparser.ConfigParser()
cf.read('key.ini',encoding='UTF-8')
my_lady_name = cf.get('params','wechat_name')
my_friend_name = cf.get('params','friend_name')

bot = Bot()

def get_news():
    url = ' http://open.iciba.com/dsapi'
    r = requests.get(url)
    content = r.json()['content']
    note  = r.json()['note']
    return content,note

def log_wechat():
    global  bot
    bot = Bot()
def send_news():
    try:
        my_girle = bot.friends().search(my_lady_name)[0]
        my_friend = bot.friends().search(my_friend_name)[0]
        my_girle.send('(•‾̑⌣‾̑•)已经过去5分钟了————来自老严的关怀')
        my_friend.send('(•‾̑⌣‾̑•)已经过去5分钟————来自老严的关怀')
        # my_girle.send(get_news()[0])
        # my_girle.send(get_news()[1])
        # my_friend.send(get_news()[0])
        # my_friend.send(get_news()[1])
        t = threading.Timer(300,send_news)  #3600 是秒数
        t.start()
    except:
        bot.file_helper.send('FALSE')
        print('false')

if __name__ == '__main__':
    t = threading.Timer(300, send_news)
    t.start()
