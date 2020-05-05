#coded by nimsith
import pyfiglet
import os

os.system("clear")
print('''
░░░░░▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄░░░░░░░░░
░░░▄▀░░░░░░░░░░░░░░░▀▀▄▄░░░░░
░░▄▀░░░░░░░░░░░░░░░░░░░░▀▄░░░
░▄▀░░░░░░░░░░░░░░░░░░░░░░░█░░
░█░░░░░░░░░░░░░░░░░░░░░░░░░█░
▐░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░▀▀█▄▄▄░░░▄▌░░░░░░░░░░░░▐
▌░░░░░▌░██▀█▀▀░░░▄▄▄▄▄░░░░▌░▐
▌░░░░░▀▄▄▄▀░░░░░░▌░▀███▄▄▀░░▐
▌░░░░░░░░░░░░░░░░░▀▄▄▄▄▀░░░▄▌
▐░░░░▐▀░░░░░░░░░░░░░░░░░░░▄▀░
░█░░░▌░░▄▀▀▀▄▄▄░░░░░░░░░░▄▀░░
░░█░░▀░░░░▄▄▄▄░▀▀▌░░▌░░░█░░░░
░░░▀▄░░░░░░░░░▀░░░▄▀░░▄▀░░░░░
░░░░░▀▄▄▄░░░░░░░░░▄▄▀▀░░░░░░░
░░░░░░░░▐▀▀▀▀▀▀▀▀▀░░░░░░░░░░░
░░░░░░░░█░░░░░░░░░░░░░░░░░░░░
█▀▀█ █▀▀█ █▀▀ 　 █░░█ █▀▀█ █░░█
█▄▄█ █▄▄▀ █▀▀ 　 █▄▄█ █░░█ █░░█
▀░░▀ ▀░▀▀ ▀▀▀ 　 ▄▄▄█ ▀▀▀▀ ░▀▀▀
▒█░▄▀ ▀█▀ ▒█▀▀▄ ▒█▀▀▄ ▀█▀ ▒█▄░▒█ ▒█▀▀█
▒█▀▄░ ▒█░ ▒█░▒█ ▒█░▒█ ▒█░ ▒█▒█▒█ ▒█░▄▄
▒█░▒█ ▄█▄ ▒█▄▄▀ ▒█▄▄▀ ▄█▄ ▒█░░▀█ ▒█▄▄█
▒█▀▄▀█ ▒█▀▀▀ ▀█
▒█▒█▒█ ▒█▀▀▀ █▀
▒█░░▒█ ▒█▄▄▄ ▄░
''')
print("\033[1;31;40m        ~ a tool by nimsith  \n")
print()
a=(input("do you wanna continue ? [y/n] :"))
os.system("clear")
print()
if a=="y":
    print("\033[1;30;40m Enter your O/L marks :  \n")
    s1=int(input("maths       :"))
    print()
    s2=int(input("science     :"))
    print()
    s3=int(input("ICT         :"))
    print()
    s4=int(input("sinhala     :"))
    print()
    s5=int(input("religion    :"))
    print()
    s6=int(input("english     :"))
    print()
    s7=int(input("commerce    :"))
    print()
    s8=int(input("history     :"))
    print()
    s9=int(input("ART         :"))
    #this is maths marks
    if s1>0:
        r1="F"
    if s1>39:
        r1="S"
    if s1>54:
        r1="C"
    if s1>64:
        r1="B"
    if s1>74:
        r1="A"
    #this is science marks
    if s2>0:
        r2="F"
    if s2>39:
        r2="S"
    if s2>54:
        r2="C"
    if s2>64:
        r2="B"
    if s2>74:
        r2="A"
    #this is ICT marks
    if s3>0:
        r3="F"
    if s3>39:
        r3="S"
    if s3>54:
        r3="C"
    if s3>64:
        r3="B"
    if s3>74:
        r3="A"
    #this is sinhala marks
    if s4>0:
        r4="F"
    if s4>39:
        r4="S"
    if s4>54:
        r4="C"
    if s4>64:
        r4="B"
    if s4>74:
        r4="A"
    #this is religion marks
    if s5>0:
        r5="F"
    if s5>39:
        r5="S"
    if s5>54:
        r5="C"
    if s5>64:
        r5="B"
    if s5>74:
        r5="A"
    #this is english marks
    if s6>0:
        r6="F"
    if s6>39:
        r6="S"
    if s6>54:
        r6="C"
    if s6>64:
        r6="B"
    if s6>74:
        r6="A"
    #this is commerce marks
    if s7>0:
        r7="F"
    if s7>39:
        r7="S"
    if s7>54:
        r7="C"
    if s7>64:
        r7="B"
    if s7>74:
        r7="A"
    #this is history marks
    if s8>0:
        r8="F"
    if s8>39:
        r8="S"
    if s8>54:
        r8="C"
    if s8>64:
        r8="B"
    if s8>74:
        r8="A"
    #this is art marks
    if s9>0:
        r9="F"
    if s9>39:
        r9="S"
    if s9>54:
        r9="C"
    if s9>64:
        r9="B"
    if s9>74:
        r9="A"
    if s1>39:
        m1=1
    else:
        m1=0
    if s4>39:
        m2=1
    else:
        m2=0
    if m1+m2>1:
        x=1
    else:
        x=0
    os.system("clear")
    print()
    print("\033[1;31;40m Here is your resluts :  \n")
    print("\033[1;30;40m \n")
    print("maths       :",r1)
    print()
    print("science     :",r2)
    print()
    print("ICT         :",r3)
    print()
    print("sinhala     :",r4)
    print()
    print("religion    :",r5)
    print()
    print("english     :",r6)
    print()
    print("commerce    :",r7)
    print()
    print("history     :",r8)
    print()
    print("ART         :",r9)
    print()
    y=input("press any to see whether you pass or fail :")
    os.system("clear")
    print()
    if x>0:
        print("\033[1;32;40m \n")
        ascii_banner = pyfiglet.figlet_format("pass")
        print(ascii_banner)
        print("your total   :",(s1+s2+s3+s4+s5+s6+s7+s8+s9))
        print()
        print("your avarage :",(s1+s2+s3+s4+s5+s6+s7+s8+s9)/3)
        print()
        print("congratulations ! you have passed the O/L exam ")
        print()
    else:
        print("\033[1;31;40m \n")
        ascii_banner2 = pyfiglet.figlet_format("fail")
        print(ascii_banner2)
        print("you have failed the current subjects :")
        print()
        if m1<1:
            print("maths")
        print()
        if m2<1:
            print("sinhala")
            print()
        print("sorry ! you have failed your O/L exam ")
        print()
else:
    print("\033[1;30;40m okay will be in second shy !  \n")
    print()
    #tool by nimsith
    #pyfiglet have to be installed to run this


