#subjests
telugu_marks = int(input("enter the telugu number"))
hindi_marks = int(input("enter the hindi marks"))
english_marks = int(input("enter the english marks"))
maths_marks = int(input("enter the maths marks"))
science_marks = int(input("enter the science marks"))
social_marks = int(input("enter the socail marks"))
#calculating the results
total_marks = (telugu_marks+hindi_marks+english_marks+maths_marks+science_marks+social_marks)/600*100
#overal grading
if total_marks >= 80:
    print("A+ grade")
    if telugu_marks <=34:
        print("fail")
        if hindi_marks <= 34:
            print("fail")
            if english_marks <= 34:
                print("fail")
                if maths_marks <=34:
                    print("fail")
                    if science_marks <= 34:
                        print("fail")
                        if social_marks <=34:
                            print("fail")
elif total_marks >= 70:
    print("A grade")
    if telugu_marks <=34:
        print("fail")
        if telugu_marks <= 34:
            print("fail")
            if hindi_marks <= 34:
                print("fail")
                if english_marks <= 34:
                    print("fail")
                    if maths_marks <= 34:
                        print("fail")
                        if science_marks <= 34:
                            print("fail")
                            if social_marks <= 34:
                                print("fail")
elif total_marks >= 60:
    print("B grade")
    if telugu_marks <=34:
        print("fail")
        if telugu_marks <= 34:
            print("fail")
            if hindi_marks <= 34:
                print("fail")
                if english_marks <= 34:
                    print("fail")
                    if maths_marks <= 34:
                        print("fail")
                        if science_marks <= 34:
                            print("fail")
                            if social_marks <= 34:
                                print("fail")
elif total_marks >= 50:
    print("C grade")
    if telugu_marks <=34:
        print("fail")
        if telugu_marks <= 34:
            print("fail")
            if hindi_marks <= 34:
                print("fail")
                if english_marks <= 34:
                    print("fail")
                    if maths_marks <= 34:
                        print("fail")
                        if science_marks <= 34:
                            print("fail")
                            if social_marks <= 34:
                                print("fail")
else:
    print("fail")