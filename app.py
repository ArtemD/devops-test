from fastapi import FastAPI
#uuden branchin vaihdettu kommentti
app = FastAPI()

@app.get('/api')
async def api():
    return {'message': 'I am API response, hello...'}

@app.get("/")
async def index():
    return {'message': 'Greetings from FastAPI'}

@app.get('/new')
async def new():
    return {'message': 'new stuff'}