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
     
main()
