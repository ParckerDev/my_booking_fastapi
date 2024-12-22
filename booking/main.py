from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello on main page!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
