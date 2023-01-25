import uvicorn
from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
async def root():
    with sqlite3.connect('db.db') as conn:
        cur = conn.cursor()

        query = 'select * from entidades'

        cur.execute(query)

        data = cur.fetchall()
        print (data)
    return {"message": "Está Funcionando"}

if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=5555)