while True:
    print("=================================")
    print("----STUDENT MARKS DECLARATION----")
    print("=================================")
    print("1.Enter Marks and Details.\n")
    print("2.Exit.\n")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter Student`s name: ")
        standard=input("Enter Student`s class: ")
        while True:
            roll=int(input("Enter Student`s Exam Roll number: "))
            if roll>0 and roll<=100:
             break
            else:
             print("Enter valid Roll number!!")   
        while True:
            sci=int(input("Enter the marks of Science Subject: "))
            if sci<=100 and sci>=0:
              break
            else:
               print("Enter valid marks!")
        while True:
            sst=int(input("Enter the marks of Social Science subject: "))
            if sst<=100 and sst>=0:
                break
            else:
                print("Enter valid marks!")
        while True:
            maths=int(input("Enter the marks of Mathematics Subject: "))
            if maths<=100 and maths>=0:
                break
            else:
                print("Enter valid marks!")
        while True:
            eng=int(input("Enter the marks of English Subject: "))
            if eng<=100 and eng>=0:
                break
            else:
                print("Enter valid marks!")
        while True:
            lang=int(input("Enter the marks of Language Subject: "))
            if lang<=100 and lang>=0:
                break
            else:
                print("Enter valid marks!")    

        total=sci+sst+maths+eng+lang
        per=total/5

        print("=============================")
        print("-------STUDENT RESULTS-------")
        print("=============================\n")
        print("Name of Student: ",name)
        print("Class of Student: ",standard)
        print("Student`s Roll number: ",roll)
        print("Total marks obtained: ",total ,"out of 500")
        print("Percentage acquired: ",round(per,2),"%")

        if sci>=33 and sst>=33 and maths>=33 and eng>=33 and lang>=33:
            if per>=90:
                print("Grade: A+")
                print("Congratulations,You have been promoted to next class!")
            elif per>=80:
                print("Grade: A-")
                print("Congratulations,You have been promoted to next class!")
            elif per>=70:
                print("Grade: A")
                print("Congratulations,You have been promoted to next class!")
            elif per>= 60:
                print("Grade: B")
                print("Congratulations,You have been promoted to next class!")
            elif per>=50:
                print("Grade: C")
                print("Congratulations,You have been promoted to next class!")
            elif per>=40:
                print("Grade: D")
                print("Congratulations,You have been promoted to next class!")
            elif per>=33:
                print("Grade: E")
                print("Congratulations,You have been promoted to next class!")
        else:
            print("Grade: F")
            print(f"Student Failed in class:{standard} ")
    elif choice==2:
        print("Thank you! See you again.")
        break
    else:
        print("Invalid choice!!")