import pyfiglet

ascii_banner = pyfiglet.figlet_format("tool by")
a=ascii_banner.center(20)
ascii_banner2 = pyfiglet.figlet_format("MRAK")
b=ascii_banner2.center(20)
print(a)
print(b)
print(" ")
c="GCE RESULTS CALCULATOR"
d=c.center(30)
f="please enter your GCE O/L marks"
g=f.center(30)
print(d)
print(" ")
print("options:")
print("   1) GCE O/L")
print("   2) GCE A/L")
print(" ")
e=int(input("choose an option (1/2) :"))
print(" ")
print(" ")
if e==1:
    print(g)
    print(" ")
    s1=int(input("maths :"))
    s2=int(input("science :"))
    s3=int(input("sinhala :"))
    s4=int(input("commerce :"))
    s5=int(input("history :"))
    s6=int(input("english :"))
    s7=int(input("ICT :"))
    s8=int(input("religion :"))
    s9=int(input("arts :"))
    if s1>39:
        r1="pass"
    else:
        r1="fail"
    if s2>39:
        r2="pass"
    else:
        r2="fail"
    if s3>39:
        r3="pass"
    else:
        r3="fail"
    if s4>39:
        r4="pass"
    else:
        r4="fail"
    if s5>39:
        r5="pass"
    else:
        r5="fail"
    if s6>39:
        r6="pass"
    else:
        r6="fail"
    if s7>39:
        r7="pass"
    else:
        r7="fail"
    if s8>39:
        r8="pass"
    else:
        r8="fail"
    if s9>39:
        r9="pass"
    else:
        r9="fail"
    if s1>39:
        l=1
    else:
        l=0
    if s3>39:
        m=1
    else:
        m=0
    if m+l>1:
        j="congratulations you have passed your exam"
    else:
        j="sorry you have failed your exam"
    print(" ")
    print(" ")
    total=s1+s2+s3+s4+s5+s6+s7+s8+s9
    avg=total/9
    h="here is your results"
    i=h.center(30)
    print(i)
    print(" ")
    print("maths         ",r1)
    print("science       ",r2)
    print("sinhala       ",r3)
    print("commerce      ",r4)
    print("history       ",r5)
    print("english       ",r6)
    print("ICT           ",r7)
    print("religion      ",r8)
    print("arts          ",r9)
    print(" ")
    print("here is your total :",total)
    print("here is your avarage :",avg)
    print(" ")
    print(j)
elif e==2:
    j="please select your GCE A/L stream"
    k=j.center(30)
    print(k)
    print(" ")
    print("   1) maths")
    print("   2) bio")
    print("   3) commerce")
    print("   4) arts")
    print(" ")
    n=int(input("choose your stream (1/2/3/4) :"))
    if n==1:
        print(" ")
        print("please enter your GCE A/L marks")
        print(" ")
        s1=int(input("maths :"))
        s2=int(input("ICT :"))
        s3=int(input("pysics :"))
        if s1>39:
            r1="pass"
        else:
            r1="fail"
        if s2>39:
            r2="pass"
        else:
            r2="fail"
        if s3>39:
            r3="pass"
        else:
            r3="fail"
        if s1>39:
            o=1
        else:
            o=0
        if s2>39:
            p=1
        else:
            p=0
        if s3>39:
            q=1
        else:
            q=0
        if o+p+q>2:
            r="congratulation you have passed the A/L exam"
        else:
            r="sorry you have failed your A/L exam"
        print(" ")
        print(" ")
        s="here is your results"
        t=s.center(30)
        print(t)
        print(" ")
        print("maths         ",r1)
        print("ICT           ",r2)
        print("pysics.       ",r3)
        print(" ")
        print("here is your total",s1+s2+s3)
        print("here is your avarage",(s1+s2+s3)/3)
        print(" ")
        print(r)
    if n==2:
        print(" ")
        print("please enter your GCE A/L marks")
        print(" ")
        s1=int(input("bio :"))
        s2=int(input("chemistry :"))
        s3=int(input("pysics :"))
        if s1>39:
            r1="pass"
        else:
            r1="fail"
        if s2>39:
            r2="pass"
        else:
            r2="fail"
        if s3>39:
            r3="pass"
        else:
            r3="fail"
        if s1>39:
            o=1
        else:
            o=0
        if s2>39:
            p=1
        else:
            p=0
        if s3>39:
            q=1
        else:
            q=0
        if o+p+q>2:
            r="congratulation you have passed the A/L exam"
        else:
            r="sorry you have failed your A/L exam"
        print(" ")
        print(" ")
        s="here is your results"
        t=s.center(30)
        print(t)
        print(" ")
        print("bio           ",r1)
        print("chemistry     ",r2)
        print("pysics        ",r3)
        print(" ")
        print("here is your total",s1+s2+s3)
        print("here is your avarage",(s1+s2+s3)/3)
        print(" ")
        print(r)
    if n==3:
        print(" ")
        print("please enter your GCE A/L marks")
        print(" ")
        s1=int(input("accounting :"))
        s2=int(input("ICT :"))
        s3=int(input("business studies :"))
        if s1>39:
            r1="pass"
        else:
            r1="fail"
        if s2>39:
            r2="pass"
        else:
            r2="fail"
        if s3>39:
            r3="pass"
        else:
            r3="fail"
        if s1>39:
            o=1
        else:
            o=0
        if s2>39:
            p=1
        else:
            p=0
        if s3>39:
            q=1
        else:
            q=0
        if o+p+q>2:
            r="congratulation you have passed the A/L exam"
        else:
            r="sorry you have failed your A/L exam"
        print(" ")
        print(" ")
        s="here is your results"
        t=s.center(30)
        print(t)
        print(" ")
        print("accounting         ",r1)
        print("ICT                ",r2)
        print("business studies   ",r3)
        print(" ")
        print("here is your total",s1+s2+s3)
        print("here is your avarage",(s1+s2+s3)/3)
        print(" ")
        print(r)
    if n==4:
        print(" ")
        print("please enter your GCE A/L marks")
        print(" ")
        s1=int(input("logic :"))
        s2=int(input("ICT :"))
        s3=int(input("religion :"))
        if s1>39:
            r1="pass"
        else:
            r1="fail"
        if s2>39:
            r2="pass"
        else:
            r2="fail"
        if s3>39:
            r3="pass"
        else:
            r3="fail"
        if s1>39:
            o=1
        else:
            o=0
        if s2>39:
            p=1
        else:
            p=0
        if s3>39:
            q=1
        else:
            q=0
        if o+p+q>2:
            r="congratulation you have passed the A/L exam"
        else:
            r="sorry you have failed your A/L exam"
        print(" ")
        print(" ")
        s="here is your results"
        t=s.center(30)
        print(t)
        print(" ")
        print("logic         ",r1)
        print("ICT          ",r2)
        print("religion     ",r3)
        print(" ")
        print("here is your total",s1+s2+s3)
        print("here is your avarage",(s1+s2+s3)/3)
        print(" ")
        print(r)
    if n>4:
        print("sorry we dont have tec subjects")
else:
    print("sorry wrong option !")

