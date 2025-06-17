from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Hello, FastAPI"}

@app.get("/ping")
def ping():
    return {"status": "pong"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=1000)
