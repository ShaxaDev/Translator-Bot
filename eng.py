import telebot
from telebot import types
import os
from gtts import gTTS


from googletrans import Translator





token = os.environ.get("tg", "1112656267:AAGzzEYPmt4vv16xE97g_9Q2_5czJnUWe3M")
bot = telebot.TeleBot(token)

translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.kr',
])
savol = "*Assalomu alaykum @{} bot imkoniyatlari bilan tanishing\nBot google translate bilan deyarli bir xil ishlaydi matnni audio shaklida ham tinglashingiz mumkin\n✅Ingliz tili\n✅Rus tili\n✅Koreys tili\n✅Nemis tili\n✅Fransuz tili\n✅Arab tili\n✅Turk tili\nYuqorida keltirilgan tillarda yozilgan matnni\nO'ZBEK tilidagi tarjimasini va \nmatn qaysi tilda bo'lsa o'sha tildagi o'qilishini ya'ni audiosini olishingiz mumkin\nQo'shimcha agar o'zbekcha matn kiritsangiz 7 tildagi tarjimasini olishingiz mumkin\n\nDasturchi👨🏻‍💻: Luco Zayn*"
    

#suz = '*Assalomu alaykum @{} men tarjimon botman\nsiz menga ingliz,rus va koreys tilidagi suz yoki matn shaklidagi xabar jo\'natasiz\nMen sizga matnni o\'zbek tilidagi  tarjimasini🇺🇿 va siz bergan matn qaysi tilda bo\'lsa xuddi o\'sha tildagi audiosini yuboraman🇬🇧🇰🇷🇷🇺 qani boshladik!\n\nAgar sizga o\'zbek tilidagi so\'zlar tarjimasi kerak bo\'lsa\nso\'zni yozib yuboring va men sizga 3 tildagi tarjimasini yuboraman *'

       

@bot.message_handler(commands=['start'])
def m(message):
   
        
    k = open('image.jpg', 'rb')

    bot.send_photo(message.chat.id, k,savol.format(
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
        bot.send_audio(txt.chat.id,f,"*Siz yozgan matn audiosi ingliz tilida 🇬🇧 tinglang🔊*",parse_mode='markdown')
        print(a.lang)
        f.close()
        
    elif a.lang=='ru':
        
        bot.reply_to(txt,k.text)
        bot.send_chat_action(txt.from_user.id,'record_audio')
        out=gTTS(text=s,lang='ru',slow=False)
        out.save('audio.mp3')
        f=open('audio.mp3','rb')
        bot.send_audio(txt.chat.id,f,"*Siz yozgan matn audiosi rus tilida 🇷🇺 tinglang🔊*",parse_mode='markdown')
        print(a.lang)
        f.close()
    elif a.lang=='ko':
        bot.reply_to(txt,k.text)
        bot.send_chat_action(txt.from_user.id,'record_audio')
        out=gTTS(text=s,lang='ko',slow=False)
        out.save('audio.mp3')
        f=open('audio.mp3','rb')
        bot.send_audio(txt.chat.id,f,"*Siz yozgan matn audiosi koreys tilida 🇰🇷 tinglang🔊*",parse_mode='markdown')
        print(a.lang)
        f.close()
    elif a.lang=='uz':
        e=txt.text
        p=translator.translate(e, dest='en')
        q=translator.translate(e, dest='ru')
        r=translator.translate(e, dest='ko')
        r1=translator.translate(e,dest='fr')
        r2=translator.translate(e,dest='tr')
        r4=translator.translate(e,dest='de')
        r5=translator.translate(e,dest='ar')
        bot.reply_to(txt, '*Ingliz tilida 🇬🇧 ➡️ {}\nRus tilida 🇷🇺 ➡️ {}\nKoreys tilida 🇰🇷 ➡️ {}\nFransuz tilida 🇫🇷 ➡️ {}\nNemis tilida 🇩🇪 ➡️ {}\nTurk tilida 🇹🇷 ➡️ {}\nArab tilida 🇸🇦 ➡️ {} *'.format(
            p.text, q.text, r.text,r1.text,r4.text,r2.text,r5.text), parse_mode='markdown')
        
    elif a.lang=='fr':
        bot.reply_to(txt,k.text)
        bot.send_chat_action(txt.from_user.id,'record_audio')
        out=gTTS(text=s,lang='fr',slow=False)
        out.save('audio.mp3')
        f=open('audio.mp3','rb')
        bot.send_audio(
            txt.chat.id, f, "*Siz yozgan matn audiosi fransuz tilida 🇫🇷 tinglang🔊*", parse_mode='markdown')
        print(a.lang)
        f.close()
    elif a.lang=='ar':
        bot.reply_to(txt,k.text)
        bot.send_chat_action(txt.from_user.id,'record_audio')
        out=gTTS(text=s,lang='ar',slow=False)
        out.save('audio.mp3')
        f=open('audio.mp3','rb')
        bot.send_audio(txt.chat.id,f,"*Siz yozgan matn audiosi arab tiida 🇸🇦 tilida tinglang🔊*",parse_mode='markdown')
        print(a.lang)
        f.close()
    elif a.lang=='de':
        bot.reply_to(txt, k.text)
        bot.send_chat_action(txt.from_user.id, 'record_audio')
        out = gTTS(text=s, lang='de', slow=False)
        out.save('audio.mp3')
        f = open('audio.mp3', 'rb')
        bot.send_audio(
            txt.chat.id, f, "*Siz yozgan matn audiosi nemis tilida 🇩🇪 tinglang🔊*", parse_mode='markdown')
        print(a.lang)
        f.close()
    elif a.lang=='tr':
        bot.reply_to(txt,k.text)
        bot.send_chat_action(txt.from_user.id,'record_audio')
        out=gTTS(text=s,lang='tr',slow=False)
        out.save('audio.mp3')
        f=open('audio.mp3','rb')
        bot.send_audio(
            txt.chat.id, f, "*Siz yozgan matn audiosi turk tilida 🇹🇷 tinglang🔊*", parse_mode='markdown')
        print(a.lang)
        f.close()

        

    
    
    
    else:
        bot.reply_to(txt,'*Iltimos,ro\'yxatdagi tillardan birida yozing siz yozgan so`z bazada mavjud bo`lmasligi mumkin\nBot google translate bilan ishlaydi!*',parse_mode='markdown')

        


    



bot.polling()



























