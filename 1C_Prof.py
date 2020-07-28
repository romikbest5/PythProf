import random
import numpy as np
class question():
    def __init__(self,quest,answers):
        self.quest = quest
        self.answers = answers

    def print_quest(self):
        print(self.quest)
        for i in self.answers:
            print(i[0])

    def get_answer(self,number):
        if self.answers[int(number)-1][1] == True:
            print("Правильно")
            return 0
        else:
            print("Неправильно")
            global quest_list_errors
            quest_list_errors.append(self)
            for i in self.answers:
                if i[1] == True:
                    print("Правильный ответ: \n" +i[0])
            return 1




def random_quests(quest_list):
    counter_error = 0
    success_counter = 0
    while(1):
        num = random.randint(1,len(quest_list)-1)
        quest_list[num].print_quest()
        ans = -1
        while ans not in ['1','2','3','4','5','6','7','8','9','0']:
            ans = input()
        if int(ans) == 0:
            break
        #quest_list[num].get_answer(ans)
        if quest_list[num].get_answer(ans) == 0:
            success_counter +=1
        else:
            counter_error +=1
        print("\n\n")
        print(" Ошибок: "+str(counter_error)+" Правильных: "+str(success_counter))
        print("\n\n")
    
    print("\n\n\n\n\n\n Ошибок: "+str(counter_error))
    print("Повторим вопросы с ошибками")
    global quest_list_errors
    for que in quest_list_errors:
        que.print_quest()
        ans = -1
        while ans not in ['1','2','3','4','5','6','7','8','9','0']:
            ans = input()
        counter_error+=que.get_answer(ans) 
        print("\n\n")





def random_all(quest_list):
    counter_error = 0
    success_counter = 0
    counter_of_quest = len(quest_list)
    random_quest_list = np.random.choice(quest_list,size=len(quest_list),replace=False)
    for i in random_quest_list:
        i.print_quest()
        ans = -1
        while ans not in ['1','2','3','4','5','6','7','8','9','0']:
            ans = input()
        if int(ans) == 0:
            break
        #counter_error+=i.get_answer(ans)
        if i.get_answer(ans) == 0:
            success_counter +=1
        else:
            counter_error +=1
        print("\n\n")
        counter_of_quest -=1
        print("Осталось вопросов: "+str(counter_of_quest)+" Ошибок: "+str(counter_error)+" Правильных: "+str(success_counter))
    print("Повторим вопросы с ошибками")
    print("\n\n\n\n\n\n Ошибок: "+str(counter_error))
    global quest_list_errors
    for que in quest_list_errors:
        que.print_quest()
        ans = -1
        while ans not in ['1','2','3','4','5','6','7','8','9','0']:
            ans = input()
        counter_error+=que.get_answer(ans) 
        print("\n\n")
        
quest_list = []

global quest_list_errors
quest_list_errors = []

global counter_error
counter_error = 0

files = []

#a = open("test1.txt",encoding='utf-8', mode='r')
#files.append(a.read())

#b = open("test2.txt",encoding='utf-8', mode='r')
#files.append(b.read())

#c = open("test3.txt",encoding='utf-8', mode='r')
#files.append(c.read())

#d = open("test4.txt",encoding='utf-8', mode='r')
#files.append(d.read())

#e = open("test5.txt",encoding = "utf-8", mode='r')
#files.append(e.read())

#f = open("test6.txt",encoding = "utf-8", mode='r')
#files.append(f.read())

g = open("test7.txt", encoding = "utf-8", mode = "r")
files.append(g.read())

h = open("test8.txt", encoding = "utf-8", mode = "r")
files.append(h.read())

j = open("test9.txt", encoding = "utf-8", mode = "r")
files.append(j.read())

#h = open("test10.txt", encoding = "utf-8", mode = "r")
#files.append(h.read())

for file in files:
    questions_not_parsed = file.split("\n\n\n")
    for q in questions_not_parsed:
        text = q.split("\n")
        quest = text[0]
        ans = []
        for i in range(1,len(text)):
            if i == 0:
                continue
            if "(TRUE_FLAG)" in text[i]:
                ans.append([text[i][:text[i].find("(TRUE_FLAG)")],True])
            else:
                ans.append([text[i],False])
        quest_list.append(question(quest,ans))


#random_quests(quest_list)
random_all(quest_list)
#all_quests(quest_list)
#print(counter_error)
