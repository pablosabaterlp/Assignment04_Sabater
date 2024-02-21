#To-Do List Generator

#Define the main function
def main():
    #initialize the dictionary that stores all tasks and completion status
    taskDict = {}

    #Define the addtask function, that takes a task name and the to do list to add it to
    def addTask(task, dict):
        #Initially add the task as incomplete
        dict[task] = False
        print("\nTask Added.\n=====================")

    #Define the view tasks function that takes a to do list
    def viewTasks(dict):
        #If there are no tasks in the list tell this to the user
        if not dict:
            print("\nYou have no tasks to do.\n=====================")
        #If the list has at least 1 item in it print this out to the user
        elif len(dict) >= 1:
            print("Tasks:\n")
            number = 1 #number is used to number each tasks 1->n tasks
            for task, completed in dict.items():
                print(f"{number}. {task} - Status: {completed}")
                number+=1 #For each iteration add 1 to the listing

    #Define the mark complete function that takes the task, either as a number or name, and the to do list
    def markComplete(inputTask, dict):
        #If the task is given as a number from the list, find the key that corresponds with the index and update the status to true
        if inputTask.isnumeric():
            intInput = int(inputTask)
            if 1 <= intInput <= len(dict):
                keyToUpdate = list(dict.keys())[intInput-1]
                dict[keyToUpdate] = True
            else: #if the key is not present then return this to the user
                print("\nThere is no task under this number.\n=====================")
        else: #If the task is given as a named string, then update the same if it exists
            if inputTask in dict.keys():
                dict[inputTask] = True
            else:
                print("\nThere is no task under this name.\n=====================")
        #Print the action to the user
        print(f"\nTask {inputTask} marked completed.\n=====================")

    def printHello():
        print("Hello")
    
    #Define the delete tasks function that takes the task, either as a number or name, and the to do list
    def deleteTasks(inputTask, dict):
        #If the task is given as a number from the list, find the key that corresponds with the index and pop it from the dictionary
        if inputTask.isnumeric():
            intInput = int(inputTask)
            if 1 <= int(inputTask) <= len(dict):
                keyToPop = list(dict.keys())[intInput-1]
                dict.pop(keyToPop)
            else: #if the key is not present then return this to the user
                print("\nThere is no task under this number.\n=====================")
        else:#If the task is given as a named string, then update the same if it exists
            if inputTask in dict.keys():
                dict.pop(inputTask)
            else:
                print("\nThere is no task under this name.\n=====================")
        #Print the action to the user
        print(f"\nTask {inputTask} deleted successfully.\n=====================")
    
    #Infinitely recurse as long as the user doesn't exit the program
    while True:
        #Ask the user for their choice of option
        print("\nOptions: \n1. Add task \n2. View tasks \n3. Mark task as completed \n4. Delete tasks \n5. Exit")
        userChoice = int(input("\nChoose from the previous options (input 1-5). "))

        #Run the corresponding function from above according to the input from the user.
        if userChoice == 1:
            taskName = input("Enter the name of the task: ").capitalize()
            addTask (taskName, taskDict)
        elif userChoice == 2:
            viewTasks(taskDict)
        elif userChoice == 3:
            taskNameNum = input("What task would you like to mark (input the exact name or the number from the list). ").capitalize()
            markComplete(taskNameNum, taskDict)
        elif userChoice == 4:
            taskNameNum = input("What task would you like to delete (input the exact name or the number from the list). ").capitalize()
            deleteTasks(taskNameNum, taskDict)
        elif userChoice == 5:
            print("Ending Program...")
            break
        else:
            print("This is not a valid choice, try again.\n")
#Run the main function     
main()