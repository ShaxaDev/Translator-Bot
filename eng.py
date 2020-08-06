import telebot
from telebot import types
import os
from gtts import gTTS


from googletrans import Translator


token = os.environ.get("tg", "'985403265:AAFSOSsxtLT2FEC_Hq37mrgmRyxIWydSd4Q")
bot = telebot.TeleBot(token)

translator = Translator()
users=[977851759,1089169019]    
@bot.message_handler(commands=['admin'])
def send_(message):
    if message.from_user.id==995951832:
        for user in users:
            bot.send_message(user.id,message.text)


suz = '*Assalomu alaykum @{} men tarjimon botman\nsiz menga ingliz,rus va koreys tilidagi suz yoki matn shaklidagi xabar jo\'natasiz\nMen sizga matnni o\'zbek tilidagi  tarjimasini🇺🇿 va siz bergan matn qaysi tilda bo\'lsa xuddi o\'sha tildagi audiosini yuboraman🇬🇧🇰🇷🇷🇺 qani boshladik!\n\nAgar sizga o\'zbek tilidagi so\'zlar tarjimasi kerak bo\'lsa\nso\'zni yozib yuboring va men sizga 3 tildagi tarjimasini yuboraman *'


@bot.message_handler(commands=['start'])
def m(message):
    k = open('en.jpg', 'rb')

    bot.send_photo(message.chat.id, k,suz.format(
        message.from_user.username), parse_mode='markdown')
    
    k.close()



@bot.message_handler(func=lambda txt: True)
def send(txt):
    
    s=txt.text
    k=translator.translate(s, dest='uz')
    print(k.text)
    a=translator.detect(txt.text)
    if a.lang=='en':
       
        
        bot.reply_to(txt,k.text)
        bot.send_chat_action(txt.from_user.id,'record_audio')
        out=gTTS(text=s,lang='en',slow=False)
        out.save('audio.mp3')
        
        
        f = open('audio.mp3', 'rb')
        #f=open('audio.mp3','rb')
        bot.send_audio(txt.chat.id,f,"*siz yozgan matn audiosi ingliz tilida 🇬🇧 tinglang🔊*",parse_mode='markdown')
        print(a.lang)
        f.close()
        
    elif a.lang=='ru':
        
        bot.reply_to(txt,k.text)
        bot.send_chat_action(txt.from_user.id,'record_audio')
        out=gTTS(text=s,lang='ru',slow=False)
        out.save('audio.mp3')
        f=open('audio.mp3','rb')
        bot.send_audio(txt.chat.id,f,"*siz yozgan matn audiosi rus tilida 🇷🇺 tinglang🔊*",parse_mode='markdown')
        print(a.lang)
        f.close()
    elif a.lang=='ko':
        bot.reply_to(txt,k.text)
        bot.send_chat_action(txt.from_user.id,'record_audio')
        out=gTTS(text=s,lang='ko',slow=False)
        out.save('audio.mp3')
        f=open('audio.mp3','rb')
        bot.send_audio(txt.chat.id,f,"*siz yozgan matn audiosi koreys tilida 🇰🇷 tinglang🔊*",parse_mode='markdown')
        print(a.lang)
        f.close()
    elif a.lang=='uz':
        e=txt.text
        p=translator.translate(e, dest='en')
        q=translator.translate(e, dest='ru')
        r=translator.translate(e, dest='ko')
        bot.reply_to(txt,'*ingliz tilida 🇬🇧 ➡️ {}\nrus tilida 🇷🇺 ➡️ {}\nkoreys tilida 🇰🇷 ➡️ {}*'.format(p.text,q.text,r.text),parse_mode='markdown')
        


        

    
    
    
    else:
        bot.reply_to(txt,'*faqat ruscha,inglizcha yoki koreyscha so\'z yoki matn yozing iltimos*',parse_mode='markdown')

        


    



















bot.polling()













