from enum import Enum
from typing import List, Dict, Any, Union


class StatusOptions(str, Enum):
    todo = "Todo"
    doing = "Doing"
    done = "Done"


Item = Dict[str, Union[int, str, StatusOptions]]


class TodoList:
    todo_list: List[Item] = [
        {"id": 1, "title": "Fast Api", "status": StatusOptions.done},
        {"id": 2, "title": "UML", "status": StatusOptions.doing},
        {"id": 3, "title": "Use cases", "status": StatusOptions.todo},
    ]
    current_id = 3

    def listing(self):
        return self.todo_list

    def insert(self, item: Dict[str, Any]) -> Dict[str, Any]:
        self.current_id += 1
        item["id"] = self.current_id
        self.todo_list.append(item)
        return item

    def get_by_id(self, item_id: int) -> Item:
        item = filter(lambda x: x["id"] == item_id, self.todo_list)
        return list(item)[0]

    def filtering(self, status: StatusOptions) -> List[Item]:
        return list(filter(lambda x: x["status"] == status, self.todo_list))

    def delete(self, item_id: int):
        for i in self.todo_list:
            if i["id"] == item_id:
                return f"{i} deleted"
