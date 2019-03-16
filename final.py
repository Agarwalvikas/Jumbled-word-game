from tkinter import *
from tkinter import ttk
import random
import re
def to():
    global t
    global e
    global score
    if(len(l)<=0):
        return()
    q=len(l)
    t=random.randint(0,q-1)
    f=''
    s=l[t]
    y=s.split(' ')
    for j in range (len(y)):
        for i in range(len(y[j])):
            v=random.randint(0,len(y[j])-1)
            f+=y[j][v]
            y[j]=y[j][:v]+y[j][v+1:]
        f+=' '
    print(f)
    label.config(text=f)
    e=Entry(root)
    e.grid(row=4,column=0)
    answer=Button(root,text="check",command=jumb).grid(row=6,column=0,sticky=W)

    
    
def jumb():
    global co
    global t
    global e
    global score
    if(len(l)<=0):
        return()
    em=e.get()
    em.lower()
    if(em==l[t]):
        print("You are right")
        score+=1
        lll.config(text=str(score)+'/10')
        o.config(text=" ")
        Label(root,text="Your previous answer is correct").grid(row=7,column=0,sticky=W)
    else:
        print("Wrong")
        Label(root,text="Correct answer-").grid(row=8,column=0,sticky=W)
        o.config(text=l[t])
        Label(root,text="Your previous answer is wrong").grid(row=7,column=0,sticky=W)
    del l[t]
    if(len(l)>0):
        co+=1
        que.config(text="Jumbled word "+str(co)+"-")
    if(len(l)==0):
        Label(root,text="Game over").grid(row=10,column=0,sticky=W)
    to()
    return()
root=Tk()
root.title('GDG Project')
score=0
lo=["life","deathnote","vikings","house of cards","altered carbon","dexter","madmen","dark","el chapo","blacklist","game of thrones","friends","breaking bad","modern family","big bang theory","2 and a half man","joey","better call saul","stranger things","narcos","how i met your mother","13 reasons why","silicon valley","flash","suits","arrow","prison break","sherlock","gotham","daredevil",]
l=set(lo)
l=list(l)
l=l[:10]
print(l)
co=1
Label(root,text="                         Welcome to the game                         ").grid(row=0,column=0,sticky=W)
que=Label(root,text="Jumbled word "+str(co)+"-")
que.grid(row=1,column=0,sticky=W)
Label(root,text="Enter your answer").grid(row=3,column=0,sticky=W)
e=Entry(root)
e.grid(row=4,column=0)
q=len(l)
t=random.randint(0,q-1)
f=''
s=l[t]
y=s.split(' ')
print(y)
for j in range (len(y)):
    for i in range(len(y[j])):
        v=random.randint(0,len(y[j])-1)
        f+=y[j][v]
        y[j]=y[j][:v]+y[j][v+1:]
    f+=' '
print(f)
o=Label(root,text="")
o.grid(row=8,column=0,sticky=E)
label=Label(root,text=f)
label.grid(row=1,column=0,sticky=E)
answer=Button(root,text="check",command=jumb).grid(row=6,column=0,sticky=W)
Label(root,text="your score-").grid(row=9,column=0,sticky=W)
lll=Label(root,text=str(score)+'/10')
lll.grid(row=9,column=1,sticky=W)
mainloop()
