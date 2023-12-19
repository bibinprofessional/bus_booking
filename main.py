from datetime import datetime

def check_name(name):
    res=name.isalpha()
    return res

def check_gender(gender):
    if gender =='m' or gender =='f':
        res2= True
    else:
        res2 =False
    return res2

def check_date(dob,dob_format):
    res3=True
    try:
        res3=bool(datetime.strptime(dob, dob_format))
    except ValueError:
        res3 = False
    return res3

def check_phone(phone):
    res4=phone.isnumeric()
    if res4:
        if len(phone)==10:
            res5=True
        else:
            res5=False
    else:
        res5=False
    return res5

def check_password(password):
    if len(password)<8:
        res6= False
    else:
        res6= True
    return res6

def check_conpassword(conpassword,password):
    if conpassword==password:
        res7=True
    else:
        res7=False
    return res7

def check_location(location,areas):
    for i in areas:
        if i==location:
            return True
    else:
        return False


class regi:
    def __init__(self,name,gender,dob,phone,username,conpassword):
        self.__name=name
        self.__gender=gender
        self.__dob=dob
        self.__phone=phone
        self.__username=username
        self.__conpassword=conpassword

    def userlogin(self,username1):
        if self.__username==username1:
            return True
        else:
            return False

    def userpass(self,password1):
        if self.__conpassword==password1:
            return True
        else:
            return False

class passenger:
    def __init__(self,name,gender,dob,phone):
        self.__name=name
        self.__gender=gender
        self.__dob=dob
        self.__phone=phone

    def display(self):
        print('__________________________________')
        print('passenger name :',self.__name)
        print('passenger gender :',self.__gender)
        print('passenger dob :',self.__dob)
        print('passenger phone :',self.__phone)
        

#list l[] to store the registered user details
l=[] 
while True:
    choose=input('press 1 to register, anyother key to login :')
    if choose =='1':
        name=input('enter your first name :')
        while True:
            if check_name(name):
                break
            else:
                print('invalid input. please enter your correct first name ')
                name=input('enter your first name :')

        gender=input('enter your gender(m/f) :')[0]
        while True:
            if check_gender(gender):
                break
            else:
                print('invalid input. please enter the correct gender(m/f)')
                gender=input('enter your gender(m/f) :')[0]

        dob=input('enter your dob in dd/mm/yyyy format :')
        dob_format='%d/%m/%Y'
        while True:
            if check_date(dob,dob_format):
                break
            else:
                print('invalid date. please enter the correct date')
                dob=input('enter your dob in dd/mm/yyyy format :')
                dob_format='%d/%m/%Y'

        phone=input('enter your mobile number without country code :')
        while True:
            if check_phone(phone):
                break
            else:
                print('invalid input. please enter the correct number ')
                phone=input('enter your mobile number without country code :')

        username=input('enter the username to register :')

        password=input('enter password (minimum 8 characters) :')
        while True:
            if check_password(password):
                break
            else:
                print('invalid input. please enter a strong password ')
                password=input('enter password (minimum 8 characters) :')

        conpassword=input('Reenter the password to confirm :')
        while True:
            if check_conpassword(conpassword,password):
                break
            else:
                print('invalid input. enter the correct password')
                conpassword=input('Reenter the password to confirm :')
        l.append(regi(name,gender,dob,phone,username,conpassword))

    else:
        username1=input('enter your registered username :')
        password1=input('enter the registered password :')

        for i in l:
            l1=[] #list l1[] to store the passenger details

            if i.userlogin(username1):
                if i.userpass(password1):

                    print('you are logged in')
                    print('BOOKING DETAILS:')

                    travel_areas=['chennai','coimbatore','bangalore']
                    travel_price={'chennaicoimbatore':'250','coimbatorechennai':'250','chennaibangalore':'350','bangalorechennai':'350','coimbatorebangalore':'400','bangalorecoimbatore':'400'}
                    
                    print('currently we operate buses in only three locations [chennai,coimbatore,bangalore]')
                    travel_from=input('enter the starting point (use only lowercase) :')
                    while True:
                        if check_location(travel_from,travel_areas):
                            break
                        else:
                            print('invalid input. please enter correct location')
                            travel_from=input('enter the starting point :')
                            

                    travel_to=input('enter the ending point (use only lowercase) :')
                    while True:
                        if check_location(travel_to,travel_areas):
                            if travel_to != travel_from:
                                break
                        else:
                            print('invalid input. please enter correct location')
                            travel_to=input('enter the ending point :')
                    
                    travel_place=travel_from+travel_to
                    for i in travel_price:
                        if i==travel_place:
                            price=travel_price[i]

                    number=int(input('Enter number of passengers :'))
                    total_price=number*int(price)
                    print('The total price is ',total_price)

                    print('PASSENGER DETAILS')
                    for a in range(number):
                        print('enter details of passenger ',a+1)
                        pas_name=input("enter the passenger's first name :")
                        while True:
                            if check_name(pas_name):
                                break
                            else:
                                print('invalid input. please enter correct first name ')
                                name=input("enter the passenger's first name :")

                        pas_gender=input("enter passenger's gender(m/f) :")[0]
                        while True:
                            if check_gender(pas_gender):
                                break
                            else:
                                print('invalid input. please enter the correct gender(m/f)')
                                pas_gender=input("enter passenger's gender(m/f) :")[0]

                        pas_dob=input("enter passenger's dob in dd/mm/yyyy format :")
                        pas_dob_format='%d/%m/%Y'
                        while True:
                            if check_date(pas_dob,pas_dob_format):
                                break
                            else:
                                print('invalid date. please enter the correct date')
                                pas_dob=input("enter passenger's dob in dd/mm/yyyy format :")
                                pas_dob_format='%d/%m/%Y'

                        pas_phone=input("enter passenger's mobile number without country code :")
                        while True:
                            if check_phone(pas_phone):
                                break
                            else:
                                print('invalid input. please enter the correct number ')
                                pas_phone=input("enter passenger's mobile number without country code :")
                        
                        l1.append(passenger(pas_name,pas_gender,pas_dob,pas_phone))
                    
                    for i in l1:
                        i.display()

                    print('____________________________________')
                    print('The total price is ',total_price)
                    print('____________________________________')
                    choose2=input('press 1 to continue with the payment , anyother key to cancel payment :')
                    if choose2=='1':
                        print('YOUR BOOKING HAS BEEN DONE SUCCESSFULLY.ENJOY YOUR JOURNEY WITH US')
                        print('THANKYOU')
                        exit()
                    else:
                        break
                    
                else:
                    print('incorrect password')
                    break

        else:
            print('the enter username is incorrect')