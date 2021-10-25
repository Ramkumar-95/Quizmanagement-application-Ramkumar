import json
import re
import time

class quizman():

    qtitle = open('quiztitle.json', 'r')
    content = qtitle.read()
    quiztitle = json.loads(content)
    #print(quiztitle) #To check the quiz question and answers
    qtitle.close()

    suser = open('superuser.json', 'r')
    content1 = suser.read()
    superuser = json.loads(content1)
    #print(superuser) #To check the quiz management admin details
    suser.close()

    user_file = open('users.json', 'r')
    content1 = user_file.read()
    user = json.loads(content1)
    #print(user) #To check the quiz management user details
    user_file.close()

    @classmethod
    def registration(cls, value="user"):
        print("====USER REGISTRATION DETAILS====")
        usertype = value
        print("Enter your email id:")
        email = input()
        pwd = input("Enter your password:")
        mobile_chk = '^[0-9]{10}$'
        chk_val = False
        while (chk_val == False):
            mobile = int(input("Enter mobile no"))
            if re.match(mobile_chk, mobile):
                chk_val = True
            else:
                print("Enter mobile number correctly")
        name = input("Enter name:")

        if usertype == "super":
            cls.superuser[email] = [pwd, name, mobile]
            print("Superuser access added successfully")
            val_data1 = json.dumps(cls.superuser)
            est = open("superuser.json", "w")
            est.write(val_data1)
            est.close()
        else:
            if email in cls.users:
                print("Email id existed already")
            else:
                cls.users[email] = [pwd, name, mobile]
                print("Users access added successfully")
                val_data2 = json.dumps(cls.users)
                est1 = open("users.json", "w")
                est1.write(val_data2)
                est1.close()
    @classmethod
    def superusersdata(cls):
        userid=input("Enter user detail:")
        if userid in cls.superuser:
            pwd=input("Enter your password")
            if cls.superuser[userid][0]==pwd:
                input_loopchk=False
                while(input_loopchk==False):
                    print("---Details of Superuser---")
                    print("Choose an option below")
                    #print("-----------------------")
                    print("1=>Create new Super user")
                    print("2=>Set up new quiz")
                    print("3=>Edit a quiz")
                    print("4=>View quizes")
                    print("5=>View Test attempters")
                    print("6=>Logout from superuser mode")
                    inp_val1=input("Enter an option:")
                    if inp_val1 not in ["1","2","3","4","5","6"]:
                        print("Your input is not valid")
                    else:
                        if inp_val1=="1":
                            value="super"
                            cls.registration(value)
                        elif inp_val1=="2":
                            topic_detail1=input("Enter the topic you need to add").lower()
                            if topic_detail1 not in cls.quiztitle.keys():
                                cls.quiztitle[topic_detail1]={"hard":[],"medium":[],"easy":[]}
                                cls.quizattempties[topic_detail1]=[]
                            else:
                                print("Topic has been existed already.Please Add new questions")

                            addques_val=False
                            while(addques_val==False):
                                qst=input("Enter the question")
                                a = input("Option a:")
                                b = input("Option b:")
                                c = input("Option c:")
                                d = input("Option d:")
                                ques_val=False
                                while (ques_val==False):
                                    answer=input("Enter the correct option:")
                                    if answer.lower() not in ["a","b","c","d"]:
                                        print("Enter the option correctly")
                                    else:
                                        ques_val=True
                                print("Enter difficulty level of quiz")
                                print("Choose an option below")
                                print("--------------------")
                                print("1: Hard")
                                print("2: Medium")
                                print("3: Easy")
                                hard_val=False
                                while(hard_val==False):
                                    difficulty=input("Enter the option:")
                                    if difficulty not in ["1","2","3"]:
                                        print("Enter the options correctly")
                                    else:
                                        hard_val=True
                                        if difficulty=="1":
                                            dif_level="hard"
                                        elif difficulty=="2":
                                            dif_level="medium"
                                        else:
                                            dif_level="easy"
                                cls.quizData[topic_detail1][dif_level].append([new_ques, {'a': a, 'b': b, 'c': c, 'd': d}, answer])
                                next_val = input("Press 1 if you need to provide another question: ")
                                if next_val!="1":
                                    addques_val=True
                        elif inp_val1=="3":
                            print("====Quiz Edit====")
                            print("Enter the topic you want to edit:")
                            for topic in cls.quiztitle:
                                print(topic.capitalize())
                            edit_val=False
                            while(edit_val==False):
                                topic_detail2=input("Enter the topic:")
                                if topic_detail2.lower() not in cls.quiztitle:
                                    print("No given topic has been exists.Please give topic correctly")
                                else:
                                    edit_val=True
                                    print(" Select option 1 to delete topic details completely from quiz")
                                    print("Select any other key")
                                    del_topic=input()
                                    if del_topic=="1":
                                        print("Given topic has been deleted successfully")
                                        cls.quiztitle.pop(topic_detail2)
                                    else:
                                        num_val=1
                                        ques_countval={}
                                        for dif_level in cls.quiztitle[topic_detail2]:
                                            num_val1=0
                                            for question in cls.quiztitle[topic_detail2][dif_level]:
                                                print(num_val,')',question[0],'Difficulty level:', dif_level)
                                                ques_countval[str(num_val)]=[dif_level,num_val1]
                                                print("a)",question[1]["a"])
                                                print("b)",question[1]["b"])
                                                print("c)",question[1]["c"])
                                                print("d)",question[1]["d"])
                                                print("Correct answer for this question:", question[2])
                                                num_val+=1
                                                num_val1+=1
                                            print("Give an option 1 to add new set of question")
                                            print("Give an option 2 to edit existing question")
                                            check_data1=False
                                            while(check_data1==False):
                                                new_val=input()
                                                if new_val not in ["1","2"]:
                                                    print("Enter the correct value")
                                                else:
                                                    check_data1=True
                                                    if new_val=="1":
                                                        check_data2=False
                                                        while(check_data2==False):
                                                            new_ques=input("Enter the question:")
                                                            a = input("Option a: ")
                                                            b = input("Option b: ")
                                                            c = input("Option c: ")
                                                            d = input("Option d: ")
                                                            hard_val=False
                                                            while(hard_val==False):
                                                                answer = input("Enter the correct option: ")
                                                                if answer.lower() not in ['a', 'b', 'c', 'd']:
                                                                    print("Enter the correct option")
                                                                else:
                                                                    hard_val=True
                                                                print("Enter difficulty level")
                                                                print("Choose an option below")
                                                                #print("--------------------")
                                                                print("1:Hard")
                                                                print("2:Medium")
                                                                print("3:Easy")
                                                                hard_val=False
                                                                while(hard_val==False):
                                                                    difficulty=input("Enter the option")
                                                                    if difficulty not in ["1","2","3"]:
                                                                        print("Enter the correct option")
                                                                    else:
                                                                        hard_val=True
                                                                        if difficulty=="1":
                                                                            dif_level="hard"
                                                                        elif difficulty=="2":
                                                                            dif_level="medium"
                                                                        else:
                                                                            dif_level="easy"
                                                                cls.quiztitle[topic_detail2][dif_level].append([new_ques,{'a':a,'b':b,'c':c,'d':d},answer])
                                                                print("Do you want to add another question in quiz. If yes, press 1")
                                                                jet_val=input()
                                                                if jet_val!="1":
                                                                    check_data2=True
                                                            pass
                                                    elif new_val=="2":
                                                        check_data3=False
                                                        while(check_data3==False):
                                                            quesinp_val=input("Enter the question number you want to edit")
                                                            if quesinp_val not in ques_countval:
                                                                print("Enter the correct question number")
                                                            else:
                                                                check_data3=True
                                                                editques_val=cls.quiztitle[topic_detail2][ques_countval[quesinp_val][0]][ques_countval[quesinp_val][1]]
                                                                print(editques_val[0])
                                                                for i in editques_val[1].items():
                                                                    print(i[0],')',i[1])
                                                                print("Answer for the given question:",editques_val[2])
                                                                #print()
                                                                check_data4=False
                                                                while(check_data4==False):
                                                                    print("Choose an option")
                                                                    print("1 Edit the question ")
                                                                    print("2 Edit an options")
                                                                    print("3 Edit an answer")
                                                                    print("4 Delete the question")
                                                                    print("5 Exit from edit window")
                                                                    inp_edit=input("Enter your option")
                                                                    if inp_edit not in ['1', '2', '3', '4', '5']:
                                                                        print("Enter correct option")
                                                                    else:
                                                                        if inp_edit=="1":
                                                                            newques_val=input("Enter the question")
                                                                            cls.quiztitle[topic_detail2][ques_countval[quesinp_val][0]][ques_countval[quesinp_val][1]][0]=newques_val
                                                                        elif inp_edit=="2":
                                                                            check_data5=False
                                                                            while(check_data5==False):
                                                                                print("Enter an option to edit [a,b,c,d]:")
                                                                                print("Enter 1 to exit option edit")
                                                                                option=input()
                                                                                if option not in ['a', 'b', 'c', 'd''1']:
                                                                                    print("Enter option correctly")
                                                                                    print("Enter 1 to exit option edit")
                                                                                else:
                                                                                    if option=="a":
                                                                                        new_inp1=input("Enter option a:")
                                                                                        cls.quiztitle[topic_detail2][ques_countval[quesinp_val][0]][ques_countval[quesinp_val][1][1]]["a"]=new_inp1
                                                                                    elif option=="b":
                                                                                        new_inp2 = input("Enter option b:")
                                                                                        cls.quiztitle[topic_detail2][ques_countval[quesinp_val][0]][ques_countval[quesinp_val][1][1]]["a"]=new_inp2
                                                                                    elif option=="c":
                                                                                        new_inp3=input("Enter option c:")
                                                                                        cls.quiztitle[topic_detail2][ques_countval[quesinp_val][0]][ques_countval[quesinp_val][1][1]]["a"]=new_inp3
                                                                                    elif option=="d":
                                                                                        new_inp4=input("Enter option d:")
                                                                                        cls.quiztitle[topic_detail2][ques_countval[quesinp_val][0]][ques_countval[quesinp_val][1][1]]["a"]=new_inp4
                                                                                    else:
                                                                                        check_data5=True
                                                                            pass
                                                                        elif inp_edit=="3":
                                                                            check_data6=False
                                                                            while(check_data6==False):
                                                                                newanswer = input("Correct answer: ")
                                                                                if newanswer.lower() not in ['a', 'b','c', 'd']:
                                                                                    print("Enter the option correctly")
                                                                                else:
                                                                                    check_data6=True
                                                                                    cls.quiztitle[topic_detail2][ques_countval[quesinp_val][0]][ques_countval[quesinp_val][1][2]] = newanswer

                                                                        elif inp_edit=="4":
                                                                            cls.quiztitle[topic_detail2][ques_countval[quesinp_val][0]].pop(ques_countval[quesinp_val][1])
                                                                            print("Given question has been deleted")

                                                                        elif inp_edit=="5":
                                                                            check_data4=True

                        elif inp_val1=="4":
                            print("--List of Quizzes --")
                            print("Quiz topics")
                            for top_val in cls.quiztitle:
                                print(top_val)
                            print()
                            check_data7=False
                            while(check_data7==False):
                                topic_view=input("Enter the topic you want to see:")
                                if topic_view.lower() not in cls.quiztitle:
                                    print("Enter the topic correctly")
                                else:
                                    check_data7=True
                                    num_val2=0
                                    for dif_level in cls.quiztitle[topic_view][dif_level]:
                                        for question in cls.quizData[topic_view][dif_level]:
                                            print(num_val2,')',question[0],"Difficulty:",dif_level)
                                            print('a)',question[1]["a"])
                                            print('b)', question[1]["b"])
                                            print('c)', question[1]["c"])
                                            print('d)', question[1]["d"])
                                            print("Correct answer:",question[2])
                                            num_val2+=1
                                    time.sleep(5)

                        elif inp_val1=="5":
                            for sec in cls.quizattempters:
                                count=1
                                print("==Topic==")
                                print("Number Email Score Percentage")
                                print(sec)
                                for att in cls.quizattempters[sec]:
                                    print(count,att[0]," ",att[1]," ",att[2])
                        elif inp_val1=="6":
                            print("Logged out from quiz successfully")
                            val_data=json.dumps(cls.quiztitle)
                            log_chk=open("quiztitle.json","w")
                            log_chk.write(val_data)
                            log_chk.close()
                            input_loopchk=True

            else:
                print("Wrong password given")
        else:
            print("No user with email exists")
    @classmethod
    def user(cls):
        print("====User access page===")
        user=input("Enter email id:")
        if user not in cls.users:
            print("No email id exists")
        else:
            password=input("Enter password")
            if cls.users[user][0]!=password:
                print("Incorrect password")
            else:
                check_data8=False
                while(check_data8==False):

                    print(" Choose the below function to operate further:")
                    print("1 To show the topics available")
                    print("2 Logout from user mode")
                    inp_quiz=input("Enter the option:")
                    if inp_quiz not in ["1","2"]:
                        print("Enter the correct option")
                    else:
                        if inp_quiz=="1":
                            print("===Show Quiz Topics===")
                            for j in cls.quiztitle:
                                print(j)
                            print()
                            check_data9=False
                            while(check_data9==False):
                                attempt=input("Enter the topic you are going to attempt:")
                                if attempt.lower() not in cls.quiztitle:
                                    print("Enter the correct topic")
                                else:
                                    check_data9=True
                                    print("===Quiz_Section===")
                                    answers=[]
                                    choosen_options=[]
                                    num_val4=1
                                    for dif_level in cls.quiztitle[attempt]:
                                        for k in cls.quiztitle[attempt][dif_level]:
                                            print(num_val4,')',k[0])
                                            print('a)',k[1]['a'])
                                            print('b)', k[1]['b'])
                                            print('c)', k[1]['c'])
                                            print('d)', k[1]['d'])
                                            print("Enter 's' to skip the question")
                                            print("Enter your option")
                                            check_data10=False
                                            while(check_data10==False):
                                                answer=input()
                                                if answer.lower() not in ['a','b','c','d','s']:
                                                    print("Invalid details")
                                                else:
                                                    if answer=="s":
                                                        choosen_options.append("Not answered")
                                                    else:
                                                        choosen_options.append(answer)
                                                    check_data10=True
                                                    if answer==k[2]:
                                                        answers.append(True)
                                                    elif answer=="s":
                                                        answers.append(0)
                                                    else:
                                                        answers.append(False)
                                            num_val4+=1

                                    # Calculation of marks
                                    correct=answers.count(True)
                                    wrong=answers.count(False)
                                    unanswered=answers.count(0)
                                    score_cal = (correct * 1) - (wrong * 0.25)
                                    total_marks = len(answers)
                                    percentage = round(((score_cal / total_marks) * 100), 2)
                                    print("Calculating final score......")
                                    time.sleep(1)
                                    print("Totalmarks: ", total_marks)
                                    print("Your score: ", score_cal)
                                    print("Percentage: ", percentage)
                                    cls.quizattempters[attempt].append([user, score_cal, percentage])
                                    print("Quiz Questions")
                                    time.sleep(3)
                                    num_val5=0
                                    for dif_level in cls.quiztitle[attempt]:
                                        for k in cls.quiztitle[attempt][dif_level]:
                                            print(num_val5+1,')',k[0])
                                            print('a)',k[1]["a"])
                                            print('b)', k[1]["b"])
                                            print('c)', k[1]["c"])
                                            print('d)', k[1]["d"])
                                            print("Correct answer:",k[2])
                                            print("Marked Option:",choosen_options[num_val5])
                                            num_val5+=1

                        elif inp_quiz=="2":
                            check_data8=True
                            print("Successfully logged out")
                            val_data3=json.dumps(cls.quizattempters)
                            log_chk1=open("quizattempters.json","w")
                            log_chk1.write(val_data3)
                            log_chk1.close()
def main():
    evaluate=quizman()
    evaluate.user()

if __name__=="__main__":
    main()






















