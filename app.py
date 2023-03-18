from fastapi import FastAPI
import sys, os
sys.path.append(os.path.dirname((__file__)) + "/mlbFiles/")
from mlbGameLines import *
from mlbGetData import *

app = FastAPI()

@app.get("/")
def home():
    return {"Data":"Set"}

@app.get("/mlb/gamelines")
def get_lines():
    return {"Data":mlb_game_lines}
a = 0
@app.get("/mlb/{team}/{year}/batting")
def get_stats(team,year):
    results = []
    try:
        results = getBatting(team,year)
        return {"Team_Stats":results}
    except:
        data = 'wait'
        return {"Data":data}
    print(results)

@app.get("/mlb/{team}/{year}/pitching")
def get_stats(team,year):
    results = []
    try:
        results = getPitching(team,year)
        return {"Team_Stats":results}
    except:
        data = 'wait'
        return {"Data":data}
