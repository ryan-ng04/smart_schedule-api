from fastapi import FastAPI
#serves as the main entry point
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Scheduler API"}