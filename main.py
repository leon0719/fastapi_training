from typing import Union
from models.model import User
from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.post("/users")
def create_user(user: User):
    # 在這裡可以使用驗證過的 user 物件
    # 例如，儲存到資料庫或進行其他操作
    return {"message": "User created successfully"}


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
