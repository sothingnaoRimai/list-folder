print("Welcome to my computer")
s=0
playing=input("Do you want to play?")
if playing !="yes":
    quit()
print("ok, let's play")
ans=input("moni is the disco")
if ans=="No":
    print("correct")
    s=s+1
else:
    print("incorrect")
ans=input("which city is a pink city?")
if ans=="Jaipur":
    print("correct")
    s=s+1
else:
    print("incorrect")
ans=input("who is the father of the nation?")
if ans=="mahatma gandhi":
    print("correct")
    s=s+1
else:
    print("incorrect")
ans=input("how many paglu are there in navgurukul?")
if ans=="5":
    print("correct")
    s=s+1
else:
    print("incorrect")

print("You got"+str(s)+"question correct")
# print("you got"+str(s/4)*5+"%")