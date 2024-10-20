import random,time,os



def passgen(): #the part that generetes passwords!1!!1111!1!1!11!!1!!11
    pae2 = random.randint(3487323232984,348738463534894354546)
    pae3 = random.randint(232332223441,4756873538995783823)
    pae5 = random.randint(12623455498,3444533435354578438)
    pae4 = random.randint(2458896029034,597826728234343545243945)
    pae = random.randint(63463746739,49834734994243445621124557584)

    print(pae,pae5,pae3,pae2,pae4)
    


def howmanpass(): #determines how many passwords going to genereted by the users prompt
    print("                                     ")
    
    try:
        pes = int(input("How Many Passwords You Wanna Generete? "))
    except ValueError:
        print("Thats Not A Number Type A Number!")
        howmanpass()
    else:
        print(pes,"Amaount Of Passwords Genereted")
        print("                                  ")

        for i in range(pes):
            passgen()
        howmanpass()

howmanpass()
    

