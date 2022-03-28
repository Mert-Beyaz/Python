menuu = (
    "-----------------------------MENU-----------------------------\n*     *     *     *     *     *     *     *     "
    "*     *     *\nPress 1 to query the name by entering an ID.\n*     *     *     *     *     *     *     *     *   "
    "  *     *\nPress 2 to see the University with the highest score.\n*     *     *     *     *     *     *     *    "
    " *     *     *\nPress 3 to create result.txt\n*     *     *     *     *     *     *     *     *     *     "
    "*\nPress 4 to rank the points.\n*     *     *     *     *     *     *     *     *     *     *\n"
    "Press 5 to list the students who have settled.\n*     *     *     *     *     *     *     *     *     *     *\n"
    "Press 6 to list students who cannot settle.\n*     *     *     *     *     *     *     *     *     *     *\n"
    "Press 7 to see University departments.\n*     *     *     *     *     *     *     *     *     *     *\n"
    "Press 0 to exit the program.\n*     *     *     *     *     *     *     *     *     *     *")


class Student():
    def __init__(self, ID, name, surname):
        self.ID = ID
        self.name = name
        self.surname = surname


file = open("student.txt", "r", encoding="utf-8")
student_list = []
for line in file.readlines():
    line = line.split()
    student = Student(line[0], line[1], line[2])  # We print the information in the student.txt to class.
    student_list.append(student)
file.close()


def find_student(ID):
    for student in student_list:
        if ID == student.ID:
            print(student.name, student.surname)


def menu():  # We put everything in the menu.
    while True:
        print(menuu)
        number = input("Please choose a option:")
        if number == "1" or number == "2" or number == "3" or number == "4" or number == "5" or number == "6" or \
                number == "7":
            if number == "1":
                ID = input("Please enter a 6-digit number..:")
                while True:
                    if len(ID) == 6:
                        print("Student with entered ID:")
                        find_student(ID)
                        break
                    elif len(ID) < 6:
                        ID = input("You have entered the missing character. Please enter a 6-digit number..:")
                    elif len(ID) > 6:
                        ID = input("You have entered too much character. Please enter a 6-digit number..:")
                    else:
                        menu()
            elif number == "2":
                file1 = open("university.txt", "r", encoding="utf-8")
                base_point = []
                uni = []
                for i in file1:
                    uni2 = i.split(",")
                    base_point.append(uni2[2])
                    uni.append(uni2)
                base_point.sort()  # We rank base scores from small to large.
                uni_info = 0  # A variable that I use to get university information.
                while True:
                    if uni[uni_info][2] == base_point[-1]:
                        print("Highest point University:", uni[uni_info][1], "\nPoint:", uni[uni_info][2])
                        break
                    else:
                        uni_info += 1
                file1.close()
            elif number == "3":
                result_list = []
                file2 = open("key.txt", "r", encoding="utf-8")
                listt = file2.readlines()
                A = "".join(listt[0])
                B = "".join(listt[1])  # We turned each answer in the answer key into an element.
                file2.close()

                ID_of_student_file = []
                file3 = open("student.txt", "r", encoding="utf-8")
                line1 = file3.readlines()
                for i in line1:
                    elements_of_the_student_file = i.split(" ")
                    ID_of_student_file.append(elements_of_the_student_file[0])
                file3.close()
                p = 0
                while p != len(ID_of_student_file):
                    file4 = open("answers.txt", "r", encoding="utf-8")
                    for i in file4:
                        list1 = i.split()
                        if ID_of_student_file[p] == list1[0]:
                            booklet = list1[1]
                            student_answer = "".join(list1[2])

                            if booklet == "A":
                                number_of_questions = 0
                                right_question = 0
                                wrong_question = 0
                                unanswered_question = 0
                                while number_of_questions < 40:
                                    if student_answer[number_of_questions] == A[number_of_questions]:
                                        right_question += 1
                                        number_of_questions += 1
                                    else:
                                        if student_answer[number_of_questions] == "*":
                                            unanswered_question += 1
                                            number_of_questions += 1
                                        else:
                                            wrong_question += 1
                                            number_of_questions += 1
                                net = right_question - (wrong_question / 4)
                                point = net * 15
                                result_list.append("Student ID: ")
                                result_list.append(student_list[p].ID)
                                result_list.append("\nName: ")
                                result_list.append(student_list[p].name)
                                result_list.append("\nSurname: ")
                                result_list.append(student_list[p].surname)
                                result_list.append("\nBooklet: ")
                                result_list.append(booklet)
                                result_list.append("\nNumber Of Right Questions: ")
                                result_list.append(right_question)
                                result_list.append("\nNumber Of Wrong Questions: ")
                                result_list.append(wrong_question)
                                result_list.append("\nNumber Of Empty Questions: ")
                                result_list.append(unanswered_question)
                                result_list.append("\nNet: ")
                                result_list.append(net)
                                result_list.append("\nPoint: ")
                                result_list.append(point)
                            else:
                                number_of_questions = 0
                                right_question = 0
                                wrong_question = 0
                                unanswered_question = 0
                                while number_of_questions < 40:
                                    if student_answer[number_of_questions] == B[number_of_questions]:
                                        right_question += 1
                                        number_of_questions += 1
                                    else:
                                        if student_answer[number_of_questions] == "*":
                                            unanswered_question += 1
                                            number_of_questions += 1
                                        else:
                                            wrong_question += 1
                                            number_of_questions += 1
                                net = right_question - (wrong_question / 4)
                                point = net * 15
                                result_list.append("Student ID: ")
                                result_list.append(student_list[p].ID)
                                result_list.append("\nName: ")
                                result_list.append(student_list[p].name)
                                result_list.append("\nSurname: ")
                                result_list.append(student_list[p].surname)
                                result_list.append("\nBooklet: ")
                                result_list.append(booklet)
                                result_list.append("\nNumber Of Right Questions: ")
                                result_list.append(right_question)
                                result_list.append("\nNumber Of Wrong Questions: ")
                                result_list.append(wrong_question)
                                result_list.append("\nNumber Of Empty Questions: ")
                                result_list.append(unanswered_question)
                                result_list.append("\nNet: ")
                                result_list.append(net)
                                result_list.append("\nPoint: ")
                                result_list.append(point)
                            file5 = open("university.txt", "r", encoding="utf-8")
                            list2 = file5.readlines()
                            for j in list2:
                                uni_info2 = j.split(",")
                                if uni_info2[0] == list1[3]:
                                    # We compare the university number with the first choice.
                                    result_list.append("\nSelected 1. University: ")
                                    result_list.append(uni_info2[1:-2])
                            result_list.append("\n")
                            file5.close()
                            file6 = open("university.txt", "r", encoding="utf-8")
                            list3 = file6.readlines()
                            for j in list3:
                                uni_info2 = j.split(",")
                                if uni_info2[0] == list1[4]:  # We compare the university number with the second choice.
                                    result_list.append("Selected 2. University: ")
                                    result_list.append(uni_info2[1:-2])
                            result_list.append("\n")
                            file6.close()
                    p += 1
                    file4.close()

                file7 = open("result.txt", "w", encoding="utf-8")
                for i in result_list:
                    file7.write(str(i))
                file7.close()
                print("File Created.")
            elif number == "4":
                student_info = []
                student_rankings = []
                points = []
                file8 = open("result.txt", "r", encoding="utf-8")
                for i in file8.readlines():
                    student_info.append(i)
                k = 0
                while k != len(student_info):
                    y = student_info[k + 8].index(":")  # for point (k = line)
                    point_student = student_info[k + 8][y + 2:-1]  # Here we find the point.
                    points.append(float(point_student))
                    k += 11  # We add 11 for the other student to pass.
                points.sort()
                q = len(student_info)
                u = 0
                while u != q:
                    k = 0
                    while k != len(student_info):
                        y = student_info[k + 8].index(":")
                        point_student = student_info[k + 8][y + 2:-1]
                        # We're writing -1 So it doesn't write down \n on the probe.
                        if points[0] == float(point_student):
                            a = student_info[k].index(":")
                            student_IDs = student_info[k][a + 2:-1]
                            c = student_info[k + 1].index(":")
                            student_names = student_info[k + 1][c + 2:-1]
                            e = student_info[k + 2].index(":")
                            student_surnames = student_info[k + 2][e + 2:-1]
                            g = student_info[k + 8].index(":")
                            student_points = student_info[k + 8][g + 2:-1]
                            student_rankings.append(
                                student_IDs + " " + student_names + " " + student_surnames + " " + student_points)
                            for m in range(11):
                                student_info.pop(k)
                                # We're removing student information from the list so it doesn't get rewritten.
                            points.pop(0)
                            # We also remove the score from the list so that the same score is not searched.
                        else:
                            k += 11
                    u += 1
                student_rankings = student_rankings[::-1]
                for j in range(len(student_rankings)):
                    print(j + 1, ":", student_rankings[j])
                file8.close()
            elif number == "5":
                file9 = open("university.txt", "r", encoding="utf-8")
                list4 = file9.readlines()
                unis_info = []
                for i in list4:
                    line2 = i.split(",")
                    unis_info.append(line2)
                file9.close()

                student_info = []
                student_rankings = []
                points = []
                file10 = open("result.txt", "r", encoding="utf-8")
                for i in file10.readlines():
                    student_info.append(i)
                k = 0
                while k != len(student_info):
                    y = student_info[k + 8].index(":")  # for point (k = line)
                    point_student = student_info[k + 8][y + 2:-1]  # Here we find the point.
                    points.append(float(point_student))
                    k += 11  # We add 11 for the other student to pass.
                points.sort()
                q = len(student_info)
                u = 0
                while u != q:
                    k = 0
                    while k != len(student_info):
                        y = student_info[k + 8].index(":")
                        point_student = student_info[k + 8][y + 2:-1]
                        if points[0] == float(point_student):
                            a = student_info[k].index(":")
                            student_IDs = student_info[k][a + 2:-1]
                            c = student_info[k + 1].index(":")
                            student_names = student_info[k + 1][c + 2:-1]
                            e = student_info[k + 2].index(":")
                            student_surnames = student_info[k + 2][e + 2:-1]
                            g = student_info[k + 8].index(":")
                            student_points = student_info[k + 8][g + 2:-1]
                            h = student_info[k + 9].index(":")
                            choice1 = student_info[k + 9][h + 2:-1]
                            b = student_info[k + 10].index(":")
                            choice2 = student_info[k + 10][b + 2:-1]
                            student_rankings.append(
                                student_IDs + "," + student_names + "," + student_surnames + "," + student_points + ","
                                + choice1 + "," + choice2)
                            for m in range(11):
                                student_info.pop(k)
                                # We're removing student information from the list so it doesn't get rewritten.
                            points.pop(0)
                            # We also remove the score from the list so that the same score is not searched.
                        else:
                            k += 11
                    u += 1
                student_rankings = student_rankings[::-1]
                file10.close()
                earned_uni = []
                rank = 0
                while len(student_rankings) != rank:
                    student_infos = student_rankings[rank].split(",")
                    a = 0
                    p = 0
                    while a != len(unis_info):
                        the_number_of_settlers_uni = earned_uni.count(unis_info[a][1])
                        # If he has already settled in the chosen university, it is how many times he has been settled.
                        availability = int(unis_info[a][3])  # kontenjan
                        if unis_info[a][1] == student_infos[4][2:-2]:
                            if (availability - the_number_of_settlers_uni) == 0:
                                # We calculating the remaining availability.
                                break
                            else:
                                uni_base_point = float(unis_info[a][2])
                                student_point = float(student_infos[3])
                                if uni_base_point <= student_point:
                                    # Checking whether the student's score is sufficient.
                                    print("EARNED UNIVERSITY:", student_infos[4][2:-2], "\n STUDENT:",
                                          student_infos[1], student_infos[2])
                                    earned_uni.append(unis_info[a][1])
                                    p = 10  # If 1. if it settled in university because of its choice, it becomes p 10
                                    # and 2. its choice is not being questioned.
                                    break
                                else:
                                    break
                        else:
                            a += 1
                    b = 0
                    if p == 0:
                        while b != len(unis_info):
                            the_number_of_settlers_uni = earned_uni.count(unis_info[b][1])
                        # If he has already settled in the chosen university, it is how many times he has been settled.
                            availability = int(unis_info[b][3])
                            if unis_info[b][1] == student_infos[5][2:-2]:
                                if (availability - the_number_of_settlers_uni) == 0:
                                    # We calculating the remaining availability.
                                    break
                                else:
                                    uni_base_point = float(unis_info[b][2])
                                    student_point = float(student_infos[3])
                                    if uni_base_point <= student_point:
                                        # Checking whether the student's score is sufficient.
                                        print("EARNED UNIVERSITY:", student_infos[5][2:-2], "\n STUDENT:",
                                              student_infos[1], student_infos[2])
                                        earned_uni.append(unis_info[b][1])
                                        b += 1
                                    else:
                                        break
                            else:
                                b += 1
                    rank += 1
            elif number == "6":
                file9 = open("university.txt", "r", encoding="utf-8")
                list4 = file9.readlines()
                unis_info = []
                for i in list4:
                    line2 = i.split(",")
                    unis_info.append(line2)
                file9.close()

                student_info = []
                student_rankings = []
                points = []
                file10 = open("result.txt", "r", encoding="utf-8")
                for i in file10.readlines():
                    student_info.append(i)
                k = 0
                while k != len(student_info):
                    y = student_info[k + 8].index(":")  # for point (k = line)
                    point_student = student_info[k + 8][y + 2:-1]  # Here we find the point.
                    points.append(float(point_student))
                    k += 11  # We add 11 for the other student to pass.
                points.sort()
                q = len(student_info)
                u = 0
                while u != q:
                    k = 0
                    while k != len(student_info):
                        y = student_info[k + 8].index(":")
                        point_student = student_info[k + 8][y + 2:-1]
                        if points[0] == float(point_student):
                            a = student_info[k].index(":")
                            student_IDs = student_info[k][a + 2:-1]
                            c = student_info[k + 1].index(":")
                            student_names = student_info[k + 1][c + 2:-1]
                            e = student_info[k + 2].index(":")
                            student_surnames = student_info[k + 2][e + 2:-1]
                            g = student_info[k + 8].index(":")
                            student_points = student_info[k + 8][g + 2:-1]
                            h = student_info[k + 9].index(":")
                            choice1 = student_info[k + 9][h + 2:-1]
                            b = student_info[k + 10].index(":")
                            choice2 = student_info[k + 10][b + 2:-1]
                            student_rankings.append(
                                student_IDs + "," + student_names + "," + student_surnames + "," + student_points + ","
                                + choice1 + "," + choice2)
                            for m in range(0, 11):
                                student_info.pop(k)
                                # We're removing student information from the list so it doesn't get rewritten.
                            points.pop(0)
                                # We also remove the score from the list so that the same score is not searched.
                        else:
                            k += 11
                    u += 1
                student_rankings = student_rankings[::-1]
                file10.close()
                earned_uni = []
                university_student = []
                rank = 0
                while len(student_rankings) != rank:
                    student_infos = student_rankings[rank].split(",")
                    a = 0
                    p = 0
                    while a != len(unis_info):
                        the_number_of_settlers_uni = earned_uni.count(unis_info[a][1])
                        # If he has already settled in the chosen university, it is how many times he has been settled.
                        availability = int(unis_info[a][3])  # kontenjan
                        if unis_info[a][1] == student_infos[4][2:-2]:
                            if (availability - the_number_of_settlers_uni) == 0:
                                # We calculating the remaining availability.
                                break
                            else:
                                uni_base_point = float(unis_info[a][2])
                                student_point = float(student_infos[3])
                                if uni_base_point <= student_point:
                                    # Checking whether the student's score is sufficient.
                                    earned_uni.append(unis_info[a][1])
                                    university_student.append(student_rankings[rank])
                                    p = 10  # If 1. if it settled in university because of its choice, it becomes p 10
                                    # and 2. its choice is not being questioned.
                                    break
                                else:
                                    break
                        else:
                            a += 1
                    b = 0
                    if p == 0:
                        while b != len(unis_info):
                            the_number_of_settlers_uni = earned_uni.count(unis_info[b][1])
                        # If he has already settled in the chosen university, it is how many times he has been settled.
                            availability = int(unis_info[b][3])
                            if unis_info[b][1] == student_infos[5][2:-2]:
                                if (availability - the_number_of_settlers_uni) == 0:
                                    # We calculating the remaining availability.
                                    break
                                else:
                                    uni_base_point = float(unis_info[b][2])
                                    student_point = float(student_infos[3])
                                    if uni_base_point <= student_point:
                                        # Checking whether the student's score is sufficient.
                                        earned_uni.append(unis_info[b][1])
                                        university_student.append(student_rankings[rank])
                                        b += 1
                                    else:
                                        break
                            else:
                                b += 1
                    rank += 1
                for i in university_student:
                    ssss = student_rankings.index(i)
                    student_rankings.pop(ssss)
                print("LOSERS:")
                for i in student_rankings:
                    # students who stay on the student_rankings list are students who can't settle anywhere.
                    line3 = i.split(",")
                    print(" ", line3[0], line3[1], line3[2])
            elif number == "7":
                file11 = open("university.txt", "r", encoding="utf-8")
                departments = []
                for i in file11.readlines():
                    list5 = i.split(",")
                    a = list5[1].index("U")
                    if list5[1][a + 9] == "y":
                        departments.append(list5[1][a + 10:])
                        # After finding the first letter of the university,
                    # we add after the total number of characters of the university to the list to find the Department.
                k = 1
                print("DEPARTMENTS:")
                for i in departments:
                    if i not in departments[k:]:
                        print(i)
                    k += 1
                file11.close()
        elif number == "0":
            print("TERMINATING THE PROGRAM...")
            break
        else:
            continue


menu()
