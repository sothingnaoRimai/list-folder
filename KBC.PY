question_list=["How many council post are there in navgurukul?","What is the capital of bangalore?","who is the T&P of navgurukul?","what's my full name?"]
options_list =[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "karnataka", "Chennai", "Delhi"],["Shikha", "moni", "anisha", "worrin"],["soso","sothingnao","akoney","athing"]]
life=[["nine","seven"],["Delhi","karnataka"],["shikha","anisha"],["soso","sothingnao"]]
life_solution=[2, 2, 2,2]
solution_list = [3, 2, 3,2]
i=0
count=0 
while i<len(question_list):
   print(i+1,question_list[i])
   j=0
   while j<len(options_list[i]):
      print(j+1,options_list[i][j])
      j+=1
   user=("without live line","with live line")
   print("choose your choice:")
   print("1.without lifline")
   print("2.with lifeline")
   choice=int(input("your choice:"))
   if choice==1:
      user1=int(input("enter your ans:"))
      if user1==solution_list[i]: 
         print("WOW!! CNGRATULATIONS","\n","Go Ahead")
      
      else:
         print("wrong answer!!!","\n","you can't move furthur","\n","restart the game")
         
         break
   elif choice==2:
      if count==0:
         k=0
         while k<len(life[i]):
            print(k+1,life[i][k])
            k+=1
         count+=1
         user2=int(input("enter your ans:")) 
         if user2==life_solution[i]:
            print("WOW!! COGRATULATIONS","\n","You Did It ")
            
               
         else:
            print("wrong answer","\n","sorry..please restart")
           
            break
      elif choice==1:
         print("you have used your lifeline")
         if count==1:
            l=0
            while l<len(solution_list[i]):
               print(l+1,solution_list[i][l])
               l=l+1
            count=count+1
            
            user3=input("enter your choice")
            if user3==solution_list[i]:
               print("wowowow...","\n","just left one question")
               
            else:
               print("SORRY...","\n","PLEASE RETRY..")
               
               break
         

      else:
         print("you have used your lifeline")
         user4=int(input("enter your answer:"))
         if user4==solution_list[i]:
            print("BRAVOO.. YOU'RE AWESOME")
            
         else:
            print("wrong answer","\n","almost clear.. restart")
            
            break
      
   else:
      print("we're so sorry for the inconvinience")
      break
   i+=1