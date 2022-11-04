from fastapi import FastAPI
#nopea muutos tänne väliin
#ja vielä toinki rivi että rivit muuttuu
app = FastAPI()


@app.get('/api')
async def api():
    return {'message': 'I am API response, hello...'}

@app.get("/")
async def index():
        return {'message': 'Greetings from FastAPI'}

        # Tässä jotain muutos kommenttia
