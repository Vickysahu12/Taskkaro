from fastapi import FastAPI, Body
from contextlib import asynccontextmanager
from app.db.config import create_tables, sessionDep
from app.task.models import *
from app.task.services import (
    create_task,
    get_all_task,
    get_task_by_id,
    update_task,
    patch_task,
    delete_task,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

# ✅ CREATE
@app.post("/task", response_model=TaskOut)
def task_create(new_task: TaskCreate):
    # use dot notation instead of []
    task = create_task(title=new_task.title, content=new_task.content)
    return task

# ✅ READ ALL
@app.get("/tasks", response_model=list[TaskOut])
def all_tasks():
    return get_all_task()

# ✅ READ ONE
@app.get("/task/{task_id}", response_model=TaskOut)
def get_tasks(task_id: int):
    return get_task_by_id(task_id)

# ✅ PUT (Full Update)
@app.put("/task/{task_id}", response_model=TaskOut)
def put_task(task_id: int, new_task: TaskUpdate):
    task = update_task(task_id, title=new_task.title, content=new_task.content)
    return task

# ✅ PATCH (Partial Update)
@app.patch("/task/{task_id}", response_model=TaskOut)
def patch_task_api(task_id: int, new_task: TaskPatch):
    task = patch_task(
        task_id,
        title=new_task.title,
        content=new_task.content
    )
    return task

# ✅ DELETE
@app.delete("/task/{task_id}")
def delete_task_api(task_id: int):
    deleted_task = delete_task(task_id)
    return {"message": "Task deleted successfully", "task": deleted_task}
