import schedule
import time
import requests
import pafy
import os
os.add_dll_directory('C:\Program Files\VideoLAN\VLC')
import vlc

r = requests.get('https://api.covid19api.com/live/country/canada')
# print(r.status_code)
jsonData = r.json()

def CaseCheck():
  Data = [
    {
      'Province':'Ontario'
    },{
      'Province':'Quebec'
    },{
      'Province':'British Columbia'
    }
  ]

  for i in range(59,47,-1):
      if jsonData[i]['Province'] == 'Ontario':
          Data[0]['Confirmed'] = jsonData[i]['Confirmed']
          Data[0]['Deaths'] = jsonData[i]['Deaths']
          Data[0]['Recovered'] = jsonData[i]['Recovered']
          Data[0]['Active'] = jsonData[i]['Active']
          Date = jsonData[i]['Date']
          Date = Date[:-10]
          Data[0]['Date'] = Date
          # print(Date)
      elif jsonData[i]['Province'] == 'Quebec':
          Data[1]['Confirmed'] = jsonData[i]['Confirmed']
          Data[1]['Deaths'] = jsonData[i]['Deaths']
          Data[1]['Recovered'] = jsonData[i]['Recovered']
          Data[1]['Active'] = jsonData[i]['Active']
          Date = jsonData[i]['Date']
          Date = Date[:-10]
          Data[1]['Date'] = Date
      elif jsonData[i]['Province'] == 'British Columbia':
          Data[2]['Confirmed'] = jsonData[i]['Confirmed']
          Data[2]['Deaths'] = jsonData[i]['Deaths']
          Data[2]['Recovered'] = jsonData[i]['Recovered']
          Data[2]['Active'] = jsonData[i]['Active']
          Date = jsonData[i]['Date']
          Date = Date[:-10]
          Data[2]['Date'] = Date

  print('COVID-19 Cases in Major Regions in Canada')
  print('---------------')
  for x in range(0,3,1):
      print('Province:',Data[x]['Province'])
      print('Confirmed:',Data[x]['Confirmed'])
      print('Deaths:',Data[x]['Deaths'])
      print('Active:',Data[x]['Active'])
      print('Date:',Data[x]['Date'])
      print('---------------')
CaseCheck()

def PlayAnthem():
  url = "https://www.youtube.com/watch?v=zwDvF0NtgdU"                                                                                         
  video = pafy.new(url)                                                                                                                       
  best = video.getbestaudio()                                                                                                                 
  playurl = best.url                                                                                                                          
  player = vlc.MediaPlayer(playurl)                                                                                                           
  player.play()
  while True: pass
PlayAnthem()

def GoodMorning():
  print("Good Morning!")

def Weekday8():
  schedule.every().monday.at("08:00").do(GoodMorning)
  schedule.every().tuesday.at("08:00").do(GoodMorning)
  schedule.every().wednesday.at("08:00").do(GoodMorning)
  schedule.every().thursday.at("08:00").do(GoodMorning)
  schedule.every().friday.at("08:00").do(GoodMorning)

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)