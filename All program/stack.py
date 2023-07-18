l=[]
while True:
    c=int(input('''
    
        1 push element
        2 pop element
        3 peek element
        4 display stack
        5 exit`
    
    '''))
    if c==1:
        n=input("enetr the value:-");
        l.append(n)
        print(n)
    elif c==2:
        if len(l)==0:
            print("Enpty stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty stack")
        else:
            print("Last stack value:-",l[-1])
    elif c==4:
        print("display stack:-",l)
    elif c==5:
        break;
    else:
        print("Invalid choice....")