from fastapi import FastAPI, Body
from contextlib import asynccontextmanager
from app.db.config import create_tables
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
@app.post("/task")
def task_create(new_task: dict = Body(...)):
    task = create_task(title=new_task["title"], content=new_task["content"])
    return task

# ✅ READ ALL
@app.get("/tasks")
def all_tasks():
    tasks = get_all_task()
    return tasks

# ✅ READ ONE
@app.get("/task/{task_id}")
def get_tasks(task_id: int):
    task = get_task_by_id(task_id)
    return task

# ✅ PUT (Full Update)
@app.put("/task/{task_id}")
def put_task(task_id: int, new_task: dict = Body(...)):
    task = update_task(task_id, title=new_task["title"], content=new_task["content"])
    return task

# ✅ PATCH (Partial Update)
@app.patch("/task/{task_id}")
def patch_task_api(task_id: int, new_task: dict = Body(...)):
    task = patch_task(
        task_id,
        title=new_task.get("title"),  # ✅ FIXED - get() is a function, not attribute
        content=new_task.get("content")
    )
    return task

# ✅ DELETE
@app.delete("/task/{task_id}")
def delete_task_api(task_id: int):
    task = delete_task(task_id)
    return task
