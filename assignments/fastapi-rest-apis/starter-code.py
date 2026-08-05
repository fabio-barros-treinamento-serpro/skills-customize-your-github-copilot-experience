from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel


app = FastAPI(title="Tasks API")


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    done: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    done: bool


tasks: list[TaskResponse] = []
next_id = 1


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> TaskResponse:
    global next_id
    task = TaskResponse(id=next_id, title=payload.title, done=False)
    tasks.append(task)
    next_id += 1
    return task


@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks() -> list[TaskResponse]:
    return tasks


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int) -> TaskResponse:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, payload: TaskUpdate) -> TaskResponse:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated = TaskResponse(id=task.id, title=payload.title, done=payload.done)
            tasks[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="Task not found")