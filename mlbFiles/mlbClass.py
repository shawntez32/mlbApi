import sqlite3
import pandas as pd
import datetime as dt

now = dt.datetime.now()
today = dt.date(now.year,now.month,now.day)

class MlbTeam:
    def __init__(self,abr,name,Date,box,Tm,Home,Opp,WL,R,RA,Inn,W_L,Rank,GB,Win,Loss,Save,DN,Attendance,cLI,Streak,Orig,Schedule):
        self.abr = abr
        self.name = name
        self.date = Date
        self.box = box
        self.tm = Tm
        self.home = Home
        self.opp = Opp
        self.wl = WL
        self.r = R
        self.ra = RA
        self.inn = Inn
        self.record = W_L
        self.rank = Rank
        self.gb = GB
        self.win = Win
        self.loss = Loss
        self.save = Save
        self.dn = DN
        self.att = Attendance
        self.cli = cLI
        self.streak = Streak
        self.orig = Orig
        self.sched = Schedule

    def get_stats(self,team,year):
        team = team
        year = year
        db_path = sqlite3.connect(f'{team}-{year}-mlb.db')
        conn = db_path
        cur = conn.cursor()
        cur.execute('SELECT * FROM Statz2')
        row = cur.fetchall()
        team_stats = pd.DataFrame(row, columns=['Date','box','Tm','Home','Opp','WL','R','RA','Inn','W_L','Rank','GB','Win','Loss','Save','DN','Attendance','cLI','Streak','Orig','Schedule'])
        date = team_stats['Date']
        self.date = today
        self.r = sum(team_stats['R'].astype(int) / len(team_stats['R']))
        self.ra = sum(team_stats['RA'].astype(int) / len(team_stats['RA']))
        self.record = team_stats['W_L'].tail(1)
        self.rank = team_stats['Rank'].tail(1)
        self.gb = team_stats['GB'].tail(1)

    def last5(self,team,year):
        team = team
        year = year
        db_path = sqlite3.connect(f'{team}-{year}-mlb.db')
        conn = db_path
        cur = conn.cursor()
        cur.execute('SELECT * FROM Statz2')
        row = cur.fetchall()
        team_stats = pd.DataFrame(row, columns=['Date','box','Tm','Home','Opp','WL','R','RA','Inn','W_L','Rank','GB','Win','Loss','Save','DN','Attendance','cLI','Streak','Orig','Schedule'])
        date = team_stats['Date']
        self.date = today
        self.r = sum(team_stats['R'].astype(int) / 5)
        self.ra = sum(team_stats['RA'].astype(int) / 5)
        self.record = team_stats['W_L'].tail(1)
        self.rank = team_stats['Rank'].tail(1)
        self.gb = team_stats['GB'].tail(1)

    def last10(self,team,year):
        team = team
        year = year
        db_path = sqlite3.connect(f'{team}-{year}-mlb.db')
        conn = db_path
        cur = conn.cursor()
        cur.execute('SELECT * FROM Statz2')
        row = cur.fetchall()
        team_stats = pd.DataFrame(row, columns=['Date','box','Tm','Home','Opp','WL','R','RA','Inn','W_L','Rank','GB','Win','Loss','Save','DN','Attendance','cLI','Streak','Orig','Schedule'])
        date = team_stats['Date']
        self.date = today
        self.r = sum(team_stats['R'].astype(int) / 10)
        self.ra = sum(team_stats['RA'].astype(int) / 10)
        self.record = team_stats['W_L'].tail(1)
        self.rank = team_stats['Rank'].tail(1)
        self.gb = team_stats['GB'].tail(1)

    def last20(self,team,year):
        team = team
        year = year
        db_path = sqlite3.connect(f'{team}-{year}-mlb.db')
        conn = db_path
        cur = conn.cursor()
        cur.execute('SELECT * FROM Statz2')
        row = cur.fetchall()
        team_stats = pd.DataFrame(row, columns=['Date','box','Tm','Home','Opp','WL','R','RA','Inn','W_L','Rank','GB','Win','Loss','Save','DN','Attendance','cLI','Streak','Orig','Schedule'])
        date = team_stats['Date']
        self.date = today
        self.r = sum(team_stats['R'].astype(int) / 20)
        self.ra = sum(team_stats['RA'].astype(int) / 20)
        self.record = team_stats['W_L'].tail(1)
        self.rank = team_stats['Rank'].tail(1)
        self.gb = team_stats['GB'].tail(1)
