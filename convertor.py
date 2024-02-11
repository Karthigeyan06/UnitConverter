
print('Convertion program')
print()
print("1. millimeter to centimeter")
print('2. centimeter to meter')
print('3. meter to kilometer')
print('4. gram to kilogram')
print('5. centi meter to inch')
print('6. meter to yard')
print('7. kilometer to mile')
print('8. gram to pound')
print('9. acre to hectere')
print('10. cent to acre')
print('11. INR to dollars')
print('12. INR to pounds')
print('13. feet to centimeter')
print('14. hours to seconds')


def mmtocm():
    print('YOU HAVE SELECTED MILLIMETER TO CENTIMETER CONVERTOR')
    print('CATEGORIES :')
    print('1. centimeter to millimeter')
    print('2. millimeter to centimeter')
    
    t= int(input('Kindly enter the category 1 or 2 :'))
    if t==2:
        mm=int(input('Enter millimeter:'))
        ans=mm/10
        print(mm, 'millimeters =', ans, 'centimeters')
    elif t==1:
        cm=int(input('Enter centimeter:'))
        ans=cm*10
        print(cm, 'centimeters =', ans, 'millmeters')
    return''

def cmtom():
    print('YOU HAVE SELECTED CENTIMETER TO METER CONVERTOR')
    print('CATEGORIES :')
    print('1. centimeter to meter')
    print('2. meter to centimeter')
    
    t= int(input('Kindly enter the category 1 or 2 :'))
    if t==2:
        mm=int(input('Enter meter:'))
        ans=mm*100
        print(mm, 'meters =', ans, 'centimeters')
    elif t==1:
        cm=int(input('Enter centimeter:'))
        ans=cm/100
        print(cm, 'centimeters =', ans, 'meters')
    
    
    return '   '

def mtokm():
    print('YOU HAVE SELECTED METER TO KILOMETER CONVERTOR')
    print('CATEGORIES :')
    print('1. meter to kilometer')
    print('2. kilometer to meter')
    
    t= int(input('Kindly enter the category 1 or 2 :'))
    if t==2:
        mm=int(input('Enter kilometer:'))
        ans=mm*1000
        print(mm, 'kilometers =', ans, 'meters')
    elif t==1:
        cm=int(input('Enter meter:'))
        ans=cm/1000
        print(cm, 'meters =', ans, 'kilometers')
    
    
    return '   '

def gtokg():
    print('YOU HAVE SELECTED GRAM TO KILOGRAM CONVERTOR')
    print('CATEGORIES :')
    print('1. gram to kilogram')
    print('2. kilogram to gram')
    
    t= int(input('Kindly enter the category 1 or 2 :'))
    if t==2:
        mm=int(input('Enter kilogram:'))
        ans=mm*1000
        print(mm, 'kilograms =', ans, 'grams')
    elif t==1:
        cm=int(input('Enter grams:'))
        ans=cm/1000
        print(cm, 'grams =', ans, 'kilograms')
    
    
    return '   '

def gtokg():
    print('YOU HAVE SELECTED GRAM TO KILOGRAM CONVERTOR')
    print('CATEGORIES :')
    print('1. gram to kilogram')
    print('2. kilogram to gram')
    
    t= int(input('Kindly enter the category 1 or 2 :'))
    if t==2:
        mm=int(input('Enter kilogram:'))
        ans=mm*1000
        print(mm, 'kilograms =', ans, 'grams')
    elif t==1:
        cm=int(input('Enter grams:'))
        ans=cm/1000
        print(cm, 'grams =', ans, 'kilograms')
    
    
    return '   '



a=int(input('Enter a convertion program from 1 to 14:'))
if a==1:
    print(mmtocm())
elif a==2:
    print(cmtom())
elif a==3:
    print(mtokm())
elif a==4:
    print(gtokg())


