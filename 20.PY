



question=[["what is the capital of india?"],["who founded microsoft?"],["how many students are there?"],["Who is the disco in NavGurukul?"]]
answer=[["delhi","manipur","pune","mumbai"],["jeff","bill gates","mark","poop"],["90","120","77","130"]]
i=0
while i<len(question):
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
            while l<len(soluton_list[i]):
               print(l+1,soluton_list[i][l])
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
            while l<len(soluton_list[i]):
               print(l+1,soluton_list[i][l])
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