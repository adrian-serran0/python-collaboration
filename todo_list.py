# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:35:02 2024

@author: adrian
"""

#to-do list
tasks = {}
Y = True
while Y == True:
    
    choice = input("Would you like to 'add', 'view', 'delete', 'sort', 'mark' a task as complete, or 'exit'? ")

    
    if choice == 'add':
        num = int(input("How many tasks would you like to add? "))
        for i in range(num):
            key = input("What is the name of the task? ")
            newtask = {key:'uncomplete'}
            tasks.update(newtask)
            print('Task added')
        
    elif choice == 'view':
        print(tasks)
        
    elif choice == 'delete':
        print(tasks)
        x = input("Enter the name of the task to delete. ")
        tasks.pop(x)
        print("Task deleted.")
        
    elif choice == 'mark':
        print(tasks)
        d = input('Which task would you like to mark as done? ')
        tasks[d] = 'complete'
        print("Marked as complete.")
        
    elif choice == 'sort':
        sortlist = sorted(tasks.items())
        sortdict = {}
        for key, value in sortlist:
            sortdict[key] = value   
        print("The tasks in alpahetical order are", sortdict)
        
    elif choice == 'exit':
        Y = False
        


