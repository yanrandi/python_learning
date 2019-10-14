import threading
from wxpy import *
bot = Bot()
def send_news():
    try:
        # my_friend = bot.friends().search(my_lady_name)[0]
        # my_friend.send('(•‾̑⌣‾̑•)已经三个小时,休息一下啦')
        # my_friend.send(get_news()[0])
        # my_friend.send(get_news()[1])
        bot.file_helper.send('test1')
        t = threading.Timer(60,send_news)  #10800 是秒数
        t.start()
    except:
        print('false')
if __name__ == '__main__':

    t = threading.Timer(60, send_news)  # 10800 是秒数
    t.start()


# import threading
#
# def func1():
#     print('Do something')
#     timer = threading.Timer(3, func1)
#     timer.start()
#
# if __name__ == '__main__':
#
#     timer = threading.Timer(3, func1)
#     timer.start()




