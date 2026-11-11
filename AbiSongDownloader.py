#try: 
if True:
  print('------------------------------------------------------')
  print('Abi Song Downloader by Mika Schäfer (TonTechnik - THG)')
  print('------------------------------------------------------\n\n')
  print('In den Ordner "uncutsongs" kommen die songs rein, welche noch nicht zugeschnitten wurden und bei Sekunde 0 starten.')
  print('In den Ordner "songs" kommen die fertig geschnitteten Songs rein, welche bei der angegeben Zeit starten.')
  print('Da das Programm keine Updates bekommt, kann es sein, dass es irgendwann nicht mehr funktioniert und Fehlermeldungen aufkommen, da YouTube was an ihrem System ändern könnte.')
  import os 
  import time
  from pydub import AudioSegment 
  from pytube import YouTube 
  from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip 
  songlen = 120
  while True: 
    print ('---------------------------------Nächster Schüler---------------------------------') 
    name = input('Namen eingeben:') 
    URL = input('YouTube URL eingeben:') 
    startMin = int(input('Start-Minute eingeben:')) 
    startSec = int(input('Start-Sekunde eingeben:')) 
    endMin = startMin
    endSec = startSec + songlen 
    #--------------------------------Download and Save 
    video = YouTube(URL) 
    while True:
      try:
        title = video.title
        break
      except:
        print('Failed to get name. Retrying...')
        time.sleep(1)
        video = YouTube(URL)
        continue
    print('\nSong "'+video.title+'" für "'+name+'" runterladen...') 
    video = video.streams.get_lowest_resolution() 
    if not os.path.exists('uncutsongs'): 
      os.makedirs('uncutsongs') 
    while True:
      try:
        video.download(filename='uncutsongs\\UC-'+name+'.mp4') 
        break
      except Exception as e:
        print('Song konnte nicht runtergeladen werden.')
        print(f"Unexpected {e=}, {type(e)=}")
        print('Versuche erneut')
        time.sleep(1)
        video = YouTube(URL) 
        video = video.streams.get_lowest_resolution() 
        continue
    print('\nSong "'+video.title+'" für "'+name+'" runtergeladen.') 
    #--------------------------------Cutting and saving 
    print('Datei zuschneiden...') 
    if not os.path.exists('songs'): 
      os.makedirs('songs') 
    ffmpeg_extract_subclip('uncutsongs\\UC-'+name+'.mp4', startMin*60+startSec, endMin*60+endSec, targetname='songs\\'+name+'.mp4') 
    print('Datei zugeschnitten - Schüler fertig.') 
#except BaseException as e: 
  print('Ein Fehler ist aufgetreten.') 
  print('Typische Fehler:') 
  print('- YouTube-Link falsch angegeben.') 
  print('- Zeitangabe ist falsch bzw. keine reine ganze Zahl') 
  print('- Keine Internetverbindung') 
  print('Sollten immernoch Fehlermeldungen auftreten, wende dich gerne an mich.')
  print('Die Fehlermeldung: '+str(e)) 
  input('Drücke Enter, um das Programm zu schließen\n')
