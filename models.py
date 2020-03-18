from typing import Optional

from pydantic import BaseModel

from data import StatusOptions


class ItemModel(BaseModel):
    title: str
    status: Optional[StatusOptions]


class AnswerItemModel(ItemModel):
    id: int
