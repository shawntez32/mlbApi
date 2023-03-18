import datetime as dt
import requests
from bs4 import BeautifulSoup
import sqlite3
from mlbData import mlb_teams
import os

dirname = os.path.dirname(__file__)

x = 'BATTING'
y = 'PITCHING'

def mlbdb_bat(mlb_team,year):
    mlb_team = mlb_team
    year = year
    data = []
    s = 'stats'
    a = 0
    content = requests.get("https://www.baseball-reference.com/teams/tgl.cgi?team={}&t=b&year={}".format(mlb_team.upper(),year))
    soup = BeautifulSoup(content.content, 'html.parser')
    td = soup.find_all('td')
    for td1 in td:
        data.append(str(td1.text))
        Rk=data[0::31]
        Date=data[1::31]
        H_A = data[2::31]
        Opp=data[3::31] 
        Rslt=data[4::31] 
        PA=data[5::31] 
        AB=data[6::31] 
        R =data[7::31]
        H =data[8::31]
        B2=data[9::31] 
        B3 =data[10::31]
        HR =data[11::31]
        RBI=data[12::31] 
        BB=data[13::31]
        IBB=data[14::31] 
        SO=data[15::31] 
        HBP=data[16::31] 
        SH=data[17::31] 
        SF=data[18::31]
        ROE=data[19::31] 
        GDP=data[20::31]	
        SB=data[21::31] 
        CS=data[22::31] 
        BA =data[23::31]
        OBP=data[24::31] 
        SLG=data[25::31] 
        OPS=data[26::31] 
        LOB=data[27::31] 
        num=data[28::31] 
        Thr=data[29::31] 
        Opp_Starter_GmeSc=data[30::31]
        #mlb_dict = {"Rk":Rk,"Gtm":Gtm,"Date":Date,"H_A":H_A,"Opp":Opp,"Rslt":Rslt,"PA":PA,"AB":AB,"R":R,"H":H,"B2":B2,"B3":B3,"HR":HR,"RBI":RBI,"BB":BB,"IBB":IBB,"SO":SO,"HBP":HBP,"SH":SH,"SF":SF,"ROE":ROE,"GDP":GDP,"SB":SB,"CS":CS,"BA":BA,"OBP":OBP,"SLG":SLG,"OPS":OPS,"LOB":LOB,"Num":num,"Thr":Thr,"Opp_Start":Opp_Starter_GmeSc}
        conn = sqlite3.connect('{}-{}-{}.db'.format(mlb_team,year,x))
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Batting(Rk TEXT,Date TEXT,H_A TEXT,Opp TEXT,Rslt TEXT,PA TEXT,AB TEXT,R TEXT,H TEXT,B2 TEXT,B3 TEXT,HR TEXT,RBI TEXT,BB TEXT,IBB TEXT,SO TEXT,HBP TEXT,SH TEXT,SF TEXT,ROE TEXT,GDP TEXT,SB TEXT,CS TEXT,BA TEXT,OBP TEXT,SLG TEXT,OPS TEXT,LOB TEXT,num TEXT,Thr TEXT,Opp_Starter_GmeSc TEXT)''')
    for y in Rk:
        try:
            Rk1 = Rk[a]
            Date1 = Date[a]
            H_A1 = H_A[a]
            Opp1 = Opp[a]
            Rslt1 = Rslt[a]
            PA1 = PA[a]
            AB1 = AB[a]
            R1 = R[a]
            H1 = H[a]
            B21 = B2[a]
            B31 = B3[a]
            HR1 = HR[a]
            RBI1 = RBI[a]
            BB1 = BB[a]
            IBB1 = IBB[a]
            SO1 = SO[a]
            HBP1 = HBP[a]
            SH1 = SH[a]
            SF1 = SF[a]
            ROE1 = ROE[a]
            GDP1 = GDP[a]
            SB1 = SB[a]
            CS1 = CS[a]
            BA1 = BA[a]
            OBP1 = OBP[a]
            SLG1 = SLG[a]
            OPS1 = OPS[a]
            LOB1 = LOB[a]
            num1 = num[a]
            Thr1 = Thr[a]
            Opp_Starter_GmeSc1 = Opp_Starter_GmeSc[a]
            cur.execute('INSERT INTO Batting(Rk,Date,H_A,Opp,Rslt,PA,AB,R,H,B2,B3,HR,RBI,BB,IBB,SO,HBP,SH,SF,ROE,GDP,SB,CS,BA,OBP,SLG,OPS,LOB,num,Thr,Opp_Starter_GmeSc) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Rk1,Date1,H_A1,Opp1,Rslt1,PA1,AB1,R1,H1,B21,B31,HR1,RBI1,BB1,IBB1,SO1,HBP1,SH1,SF1,ROE1,GDP1,SB1,CS1,BA1,OBP1,SLG1,OPS1,LOB1,num1,Thr1,Opp_Starter_GmeSc1))
            conn.commit()
            a += 1
            print(len(data))
        except:
            pass

def mlbdb_pit(mlb_team,year):
    mlb_team = mlb_team
    year = year
    data = []
    s = 'stats'
    a = 0
    content = requests.get("https://www.baseball-reference.com/teams/tgl.cgi?team={}&t=b&year={}".format(mlb_team.upper(),year))
    soup = BeautifulSoup(content.content, 'html.parser')
    td = soup.find_all('td')
    for td1 in td:
        #IP H R ER UER BB SO HR HBP	ERA	BF Pit Str IR IS SB CS AB 2B 3B IBB SH SF ROE GDP # Umpire PitchersUsed(Rest-GameScore-Dec
        data.append(str(td1.text))
        Rk=data[0::33]
        Date=data[1::33]
        H_A = data[2::33]
        Opp=data[3::33] 
        Rslt=data[4::33] 
        IP=data[5::33] 
        H=data[6::33] 
        R=data[7::33]
        ER=data[8::33]
        UER=data[9::33] 
        BB=data[10::33]
        SO=data[11::33]
        HR=data[12::33] 
        HBP=data[13::33]
        ERA=data[14::33] 
        BF=data[15::33] 
        Pit=data[16::33] 
        Str=data[17::33] 
        IR=data[18::33]
        IS=data[19::33] 
        SB=data[20::33]	
        CS=data[21::33] 
        AB=data[22::33] 
        B2 =data[23::33]
        B3=data[24::33] 
        IBB=data[25::33] 
        SH=data[26::33] 
        SF=data[27::33] 
        ROE=data[28::33] 
        GDP=data[29::33]
        num = data[30::33]
        Ump = data[31::33]
        Oth_Pitch=data[32::33]
        #mlb_dict = {"Rk":Rk,"Gtm":Gtm,"Date":Date,"H_A":H_A,"Opp":Opp,"Rslt":Rslt,"PA":PA,"AB":AB,"R":R,"H":H,"B2":B2,"B3":B3,"HR":HR,"RBI":RBI,"BB":BB,"IBB":IBB,"SO":SO,"HBP":HBP,"SH":SH,"SF":SF,"ROE":ROE,"GDP":GDP,"SB":SB,"CS":CS,"BA":BA,"OBP":OBP,"SLG":SLG,"OPS":OPS,"LOB":LOB,"Num":num,"Thr":Thr,"Opp_Start":Opp_Starter_GmeSc}
        conn = sqlite3.connect('{}-{}-{}.db'.format(mlb_team,year,y))
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Pitching(Rk TEXT,Date TEXT,H_A TEXT,Opp TEXT,Rslt TEXT,IP TEXT, H TEXT, R TEXT, ER TEXT, UER TEXT, BB TEXT, SO TEXT, HR TEXT, HBP TEXT,ERA TEXT,BF TEXT, Pit TEXT, Str TEXT, IR TEXT, IS1 TEXT, SB TEXT, CS TEXT, AB TEXT, B2 TEXT, B3 TEXT, IBB TEXT,SH TEXT, SF TEXT, ROE TEXT, GDP,num TEXT,Ump TEXT,Oth_Pitch TEXT)''')
    for z in Rk:
        try:
            Rk1 = Rk[a]
            Date1 = Date[a]
            H_A1 = H_A[a]
            Opp1 = Opp[a]
            Rslt1 = Rslt[a]
            IP1= IP[a]
            H1= H[a]
            R1= R[a]
            ER1= ER[a]
            UER1= UER[a]
            BB1= BB[a]
            SO1= SO[a]
            HR1= HR[a]
            HBP1= HBP[a]
            ERA1= ERA[a]
            BF1= BF[a]
            Pit1= Pit[a]
            Str1= Str[a]
            IR1= IR[a]
            IS1= IS[a]
            SB1= SB[a]
            CS1= CS[a]
            AB1= AB[a]
            B21 = B2[a]
            B31= B3[a]
            IBB1= IBB[a]
            SH1= SH[a]
            SF1= SF[a]
            ROE1= ROE[a]
            GDP1= GDP[a]
            num1 = num[a]
            Ump1 = Ump[a]
            Oth_Pitch1= Oth_Pitch[a]
            cur.execute('INSERT INTO Pitching(Rk,Date,H_A,Opp,Rslt,IP,H,R,ER,UER,BB,SO,HR,HBP,ERA,BF,Pit,Str,IR,IS1,SB,CS,AB,2B,3B,IBB,SH,SF,ROE,GDP,num,Ump,Oth_Pitch) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Rk1,Date1,H_A1,Opp1,Rslt1,IP1,H1,R1,ER1,UER1,BB1,SO1,HR1,HBP1,ERA1,BF1,Pit1,Str1,IR1,IS1,SB1,CS1,AB1,B21,B31,IBB1,SH1,SF1,ROE1,GDP1,num1,Ump1,Oth_Pitch1))
            conn.commit()
            a += 1
            print(len(data))
        except:
            pass

def getBatting(team,year):
    a = 0
    for x in team:
        if a > 0:
            x = x.lower()
        a += 1
    filename = os.path.join(dirname, f'mlbDb/{team}-{year}-BATTING.db')
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Batting")
    rows = cur.fetchall()
    return rows

def getPitching(team,year):
    a = 0
    for x in team:
        if a > 0:
            x = x.lower()
        a += 1
    print(team)
    filename = os.path.join(dirname, f'mlbDb/{team}-{year}-PITCHING.db')
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Pitching")
    rows = cur.fetchall()
    return rows

getPitching("Ari",2022)