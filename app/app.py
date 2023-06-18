from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException, Response, status
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from fastapi import Depends

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="leon",
            password="a0908116100",
            port=5432,
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Database connection failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite foods", "content": "I like pizza", "id": 2},
]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "success"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(
        """INSERT INTO posts (title, content, published) VALUES(%s,%s,%s) RETURNING *""",
        (post.title, post.content, post.published))

    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", str(id))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post {id} not found"
        )
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", str(id))
    deleted_post = cursor.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post {id} not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(
        """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
        (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post {id} not found"
        )
    return {"data": updated_post}
