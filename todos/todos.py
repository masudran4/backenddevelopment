from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException, Path
from starlette import status
from database import engine, db_dependency, auth_dependency
from . import models
from .models import Todos

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


class TodoReq(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3)
    completed: bool = Field(default=False)
    priority: int = Field(default=0)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_record(db: db_dependency):
    return db.query(Todos).limit(20).all()


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def get_record(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")


@router.post("/todo/create", status_code=status.HTTP_201_CREATED)
async def create_record(db: db_dependency, new_todo: TodoReq, user: auth_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    item = Todos(**new_todo.model_dump(), owner=user.get('id'))
    db.add(item)
    db.commit()
    db.refresh(item)
    return {"todo_id": item.id}


@router.put("/todo/{todo_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_record(user: auth_dependency, db: db_dependency, new_todo: TodoReq, todo_id: int = Path(gt=0), ):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    item = db.query(Todos).filter(Todos.id == todo_id).first()
    if item:
        item.title = new_todo.title
        item.description = new_todo.description
        item.completed = new_todo.completed
        item.priority = new_todo.priority
        db.add(item)
        db.commit()
        return {"todo_id": item.id}
    else:
        raise HTTPException(status_code=404, detail="Todo not found")


@router.delete("/todo/{todo_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_record(user: auth_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    item = db.query(Todos).filter(Todos.id == todo_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"info": "Successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Todo not found")
