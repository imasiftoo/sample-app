from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Simple FastAPI App")

# include routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI app!"}

