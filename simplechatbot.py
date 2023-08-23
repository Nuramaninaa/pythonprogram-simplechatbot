from tkinter import *                       
from random import choice                       
 
#ask list contains the greetings that the chatbot will respond to                                                                      
ask   = ["hi", "hello", "good morning", "good evening", "how are you?"]  
#hi list contains the chatbot's possible responses to greetings
hi    = ["hi", "hello", "Hello too"]     
#error list contains the chatbot's possible responses to questions that it does not understand
error = ["sorry, i don't know", "what u said?","yes","i am a chatbot only" ]            

                                                                                                                                        
root = Tk()                             
user = StringVar()                          
bot  = StringVar()                          
  
                                                                      
root.title(" Simple ChatBot ")                  
Label(root, text=" user : ").pack(side=LEFT)                
Entry(root, textvariable=user).pack(side=LEFT)          
Label(root, text=" Bot  : ").pack(side=LEFT)                
Entry(root, textvariable=bot).pack(side=LEFT)               
                            
                                
def main():                             
       question = user.get()                        
       if question in ask:                      
             bot.set(choice(hi))                    
       else:                                
             bot.set(choice(error))                 
                                
Button(root, text="speak", command=main).pack(side=LEFT)        
                                    
mainloop()                              
