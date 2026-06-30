from fastapi import FastAPI

app = FastAPI(
    title="DevOps Platform CachoDev",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "DevOps Platform API"
    }

@app.get("/health")
def health():
    return {
        "status": "UP"
    }