import os
# from typing import Optional
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import time

if os.path.isfile(".env"):
    print(".env file found. loading....")
    load_dotenv(".env")

from db import engine, Base
from bookstore.routes.item import item_router, items_router

app = FastAPI()
app.include_router(item_router)
app.include_router(items_router)
Base.metadata.create_all(bind=engine)


@app.get("/test")
def home_for_test():
    return {"message": "able to reach out to the test method"}


@app.middleware(middleware_type="http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/admin")
def home_for_test():
    return {"db": os.getenv("SQLALCHEMY_DATABASE_URL")}
# def common_parameters(mandatory_q: int = None, optional_q: Optional[int] = None, skip: int = 0, limit: int = 100):
#     return {"mandatory_q": mandatory_q, "optional_q": optional_q, "skip": skip, "limit": limit}
#
#
# class CommonQueryParams:
#     """ Common Query Parameters that can be associated with any request"""
#
#     def __init__(self, q: Optional[str], skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit
#
#     def __str__(self):
#         return str({"q": self.q, "skip": self.skip, "limit": self.limit})
#
#
# @app.get("/")
# def test_query_parameters(query_params: CommonQueryParams = Depends(CommonQueryParams)):
#     return {"message": f"my first fastapi app with common query parameters = {query_params}"}
