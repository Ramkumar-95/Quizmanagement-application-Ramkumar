from main import quizman
def quiz_home():
    chk_val=False
    while(chk_val==False):
        print("Edyoda quiz management application running by Ram:")
        print("Please choose an option ")
        print("1 Super user login")
        print("2 User login")
        print("3 New user registration")
        print("4 Exit the application")
        chk_val1=False
        while(chk_val1==False):
            func_quizchk=input("Enter the option:")
            if func_quizchk not in ["1","2","3","4"]:
                print("Enter the correct option")
            else:
                chk_val1=True
                if func_quizchk=="1":
                    quizman.superusersdata()
                elif func_quizchk=="2":
                    quizman.user()
                elif func_quizchk=="3":
                    quizman.registration()
                else:
                    chk_val=True
def main():
    evaluate=quiz_home()

if __name__=="__main__":
    main()