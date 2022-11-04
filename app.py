#git kommenttia
from fastapi import FastAPI

app = FastAPI()
#lisää kommenttia

@app.get('/api')
async def api():
    return {'message': 'I am API response, hello!'}


@app.get("/")
async def index():
    return {'message': 'Hello from FastAPI'}

# Tässä jotain muutos kommenttia
