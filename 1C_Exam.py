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
            for i in self.answers:
                if i[1] == True:
                    print("Правильный ответ: \n" +i[0])
            return 1

def quest_choice(quest_list):
    for file in files:
        questions_not_parsed = file.split("\n\n\n")
        quest_list = []
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
    return np.random.choice(quest_list)
exam_list = []
files = []
f = open("test1.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test2.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test3.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test4.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test5.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test6.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test7.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test8.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test9.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test10.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test11.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test12.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test13.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))

files = []
f = open("test14.txt", encoding = "utf-8", mode = "r")
files.append(f.read())
exam_list.append(quest_choice(files[0]))


for que in exam_list:
    que.print_quest()
    ans = -1

    while str(ans) not in ['1','2','3','4','5','6','7','8','9','0']:
        ans = input()

    while True:
        try:
            a=que.get_answer(ans)
            break
        except:
            print("Некорректный ответ, try again")
            ans = -1
            while str(ans) not in ['1','2','3','4','5','6','7','8','9','0']:
                ans = input()
    print("\n\n")
