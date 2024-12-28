from fastapi import APIRouter
from app.models import Task

router = APIRouter()
#api for tasks
@router.post("/tasks")
def create_task(task: Task):
    return {"task": task}
