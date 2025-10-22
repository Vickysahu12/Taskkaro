from fastapi import FastAPI

app = FastAPI()

@app.get("/me")
async def mine():
    return {"response":"hey this is me vicky"}

# restart again sry for the day
# again.....again and again we will gonna make it for sure