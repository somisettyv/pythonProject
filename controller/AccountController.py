from dao.MyTestDao import fetch_data
from fastapi import FastAPI

app = FastAPI()


@app.get("/account")
async def get_accounts():
    accounts = fetch_data()
    return accounts
