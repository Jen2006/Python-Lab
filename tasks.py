
tasks={}

def add_task(task_no,description,priority):
 task={
  "description":description,
  "priority":priority.lower(),
  "status":"incomplete"
  }
 tasks[task_no]=task

def remove_task():
  index=int(input("Enter the Index of the task to be removed"))
  tasks.pop(index)

def update_desc():
  index=int(input("Enter the index"))
  desc=input("Enter the description")
  tasks[index]["description"]=desc

def sort_task():
  sorted_task={}
  n=1

  for i in range(1,len(tasks)+1):
    if tasks[i]["priority"]=="high":
      sort_task[n]=tasks[i]
      n+=1
    
  for i in range(1,len(tasks)+1):  
    if tasks[i]["priority"]=="medium":
      sort_task[n]=tasks[i]
      n+=1
  for i in range(1,len(tasks)+1):
     if tasks[i]["priority"]=="low":
       sort_task[n]=tasks[i]
       n+=1

  return sorted_task 


if __name__=="__main__":
  print("1.Add a task \n2.Remove a task \n3.Update the description of the task \n4. Sort the tasks")

  choice=int(input("Enter your choice"))

  if choice==1:
     e=int(input("Enter the no of tasks you want to add") )
    
     for i in range(e+1):
      tn=int(input("Enter the task no"))
      des=input("Enter description")
      pr=input("Enter the priority")
     add_task(tn,des,pr)

  elif choice==2:
     remove_task()
  elif choice== 3:
    update_desc()
  else:
    sort_task()
  

