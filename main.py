from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app=FastAPI()

class Task(BaseModel):
    
    task_name:str
    description:str
    statu:str
    priority:str
    due_date:str
    created_at:str
class Taskupdate(BaseModel):
    description:str
    statu:str
    priority:str    


tasks=[]
@app.post("/info")
def insert_data(task:Task):
    new_task={
        "task_id":len(tasks)+1,
        "task_name":task.task_name,
        "description":task.description,
        "statu":task.priority,
        "priority":task.priority,
        "due_date":task.due_date,
        "created_at":task.created_at

    }

    tasks.append(new_task)
    return new_task
 


@app.get("/show")
def show_data():
    return tasks


#get by id
@app.get("/id/{id}")
def get_id(id:int):
    for no in tasks:
        if no["task_id"]==id:
            return no
    return {
        "messge":"no data"
    }  


@app.put("/id/{id}")
def get_id(id:int):
    for no in tasks:
        if no["task_id"]==id:
            no["description"]="done"
            return no
    return {
        "messge":"not found"
    }
@app.patch("/d/{id}")
def update_task(id:int,task_update:Taskupdate):
    for task in tasks:
        if task["task_id"]==id:

            updatetask=task_update.model_dump(exclude_unset=True)
            task.update(updatetask)
            return tasks
    raise  HTTPException(status_code=404, detail="Task not found") 
                
@app.delete("/dele/{id}")
def delete_data(id:int):
    for task in tasks:
        if task["task_id"]==id:
            tasks.remove(task)     
            return tasks
    raise HTTPException(status_code=404,detail="not found")     


        

    
    


    









