from typing import List, Optional

from fastapi import APIRouter

from data import StatusOptions, TodoList
from models import ItemModel, AnswerItemModel

todo = TodoList()
router = APIRouter()


@router.get("/", response_model=List[AnswerItemModel])
def todo_listing(status: Optional[StatusOptions] = None):
    """
    Returns the to-do list
    """
    if status is not None:
        return todo.filtering(status=status)
    return todo.todo_list


@router.get("/{item_id}", response_model=AnswerItemModel)
def get_by_id(item_id: int):
    """
    View that shows an item from its id
    """
    return todo.get_by_id(item_id)


@router.post("/", response_model=AnswerItemModel)
def insert_to_do(item_to_insert: ItemModel):
    """
    Returns the to-do list insert
    """
    return todo.insert(item_to_insert.dict())


@router.delete("/", response_model=AnswerItemModel)
def delete_to_do(item_to_delete: int):
    """
    Delete the to-do
    """
    return todo.delete(item_to_delete)
