import schedule
import time
import requests
import pafy
import os
os.add_dll_directory('C:\Program Files (x86)\VideoLAN\VLC')
import vlc

def GoodMorning():
  print("Good Morning!")
# GoodMorning()

def Weekday8():
  schedule.every().monday.at("08:00").do(GoodMorning)
  schedule.every().tuesday.at("08:00").do(GoodMorning)
  schedule.every().wednesday.at("08:00").do(GoodMorning)
  schedule.every().thursday.at("08:00").do(GoodMorning)
  schedule.every().friday.at("08:00").do(GoodMorning)
Weekday8()

r = requests.get('https://api.covid19api.com/live/country/canada')
# print(r.status_code)
jsonData = r.json()

localtime = time.asctime( time.localtime(time.time()) )
# print (time.strftime("%Y-%m-%d")) 

def ImportData():  
  # 1:Add Value for desired Provinces
  # Country = ['Ontario','Quebec','British Columbia']
  # Data = []
  # for i in jsonData: #Take out Value from jsonData
  #   if i['Date'][:-10]== time.strftime("%Y-%m-%d"): #Check if date wanted matches
  #     for x in Country: #Select Provinces
  #       if i['Province'] == x:
  #         Data.append(i)
  
  # 2:Add Value for all Provinces
  Data = []
  for i in jsonData: #Take out Value from jsonData
    if i['Date'][:-10]== time.strftime("%Y-%m-%d"): #Check if date wanted matches
      Data.append(i)
  Data = sorted(Data, key=lambda k: k['Province'])
  
  return Data
# print(ImportData())

def NationSum():
  Confirmed = 0
  for y in ImportData():
    Confirmed = Confirmed + y['Confirmed']
  Deaths = 0
  for z in ImportData():
    Deaths = Deaths + z['Deaths']
  Active = 0
  for a in ImportData():
    Active = Active + a['Active']

  NationStat = {'Confirmed':Confirmed,'Deaths':Deaths,'Active':Active}
  return NationStat
# print(NationSum())

def PrintData():
  print('COVID-19 Cases in Major Regions in Canada')
  print(time.strftime("%Y-%m-%d %H:%M:%S")) 
  print('---------------')
  for x in ImportData():
      print('Province:',x['Province'])
      print('Confirmed:',x['Confirmed'])
      print('Deaths:',x['Deaths'])
      print('Active:',x['Active'])
      # print('Date:',x['Date'][:-10])
      print('---------------')
  print('Canada National Stats')
  print('Confirmed:',NationSum()['Confirmed'])
  print('Deaths:',NationSum()['Deaths'])
  print('Active:',NationSum()['Active'])
# PrintData()

def PlayAnthem():
  url = "https://www.youtube.com/watch?v=LQAbRP1f31A"                                                                                         
  video = pafy.new(url)                                                                                                                       
  best = video.getbestaudio()                                                                                                                 
  playurl = best.url                                                                                                                          
  player = vlc.MediaPlayer(playurl)                                                                                                           
  player.play()
  while True: pass
PlayAnthem()

# schedule.every(1).hour.do(PrintData)
schedule.every(1).minutes.do(PrintData)
schedule.every(30).minutes.do(PlayAnthem)

while True:
    schedule.run_pending()
    time.sleep(1)
