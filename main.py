import pandas as pd
from fastapi import FastAPI, HTTPException, Header

df = pd.read_csv('players.csv')

app = FastAPI()

API_KEY = "testingapitokenkey1234" #testing api token key 1234

@app.get("/")
def home():
  return {"message":"Welcome to All Player API, place to get player list"}

@app.get("/players")
def getAllPlayers(api_key: str = Header(None)):
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
       return df.to_dict(orient='records')

@app.get("/players/{state}")
def getPlayerByState(state:str, api_key: str = Header(None)):
    print(state)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
       player_by_state = df[df['state'] == state]

       return player_by_state.to_dict(orient='records')
