from tkinter import *
from PIL import ImageTk,Image
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition
import threading

bot=ChatBot('Bot')
trainer=ListTrainer(bot)
# for files in os.listdir('data/english/'):
#      data=open('data/english/'+files,'r',encoding='utf-8').readlines()
#      trainer.train(data)
def bot_reply():
    question=questionField.get()
    question=question.capitalize()
    ans=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(ans)+'\n\n')
    pyttsx3.speak(ans)
    questionField.delete(0,END)

def audio_to_text():
    while True:
        sr=speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone()as m:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio=sr.listen(m)
                query=sr.recognize_google(audio)
                #=query.capitalize()
                questionField.delete(0,END)
                questionField.insert(0,query)
                bot_reply()
        except Exception as e:
                print(e)



root=Tk()
root.geometry('400x570+100+30')
root.title('Chatbot')
root.resizable (0,0)
bgImage = ImageTk.PhotoImage(file='chat1.png')
bgLabel = Label(root , image=bgImage)
bgLabel.place(x= 0 , y=0)
image=Image.open('hello.jpg')
img=image.resize((120,120))
my_img=ImageTk.PhotoImage(img)
label=Label(root,image=my_img,bg='slate blue')
label.pack(pady=1)
centreframe=Frame(root)
centreframe.pack()
scrollbar=Scrollbar(centreframe)
scrollbar.pack(side=RIGHT)
#textarea=Text(centreframe)
textarea=Text(centreframe,height=14,width=48,bg='white',font=('times new roman',15,'bold'),yscrollcommand=scrollbar.set,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)
#scrollbar=Scrollbar(root,command=textarea.yview)
#scrollbar.pack(side=RIGHT,fill=Y)
questionField=Entry(root,font=('Verdana',15,'bold'))
questionField.pack(pady=19,fill=X)
image1=Image.open('ask_copy.jpg')
img=image1.resize((35,35))
my_img1=ImageTk.PhotoImage(img)
askbutton=Button(root,image=my_img1,bg='slate blue3',bd=5,command=bot_reply)
askbutton.place(x=175,y=510)
#askbutton.pack()
def click(event):
    askbutton.invoke()

root.bind('<Return>',click)

thread=threading.Thread(target=audio_to_text)
thread.setDaemon(True)
thread.start()

root.mainloop()