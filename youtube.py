from pytube import YouTube
while 1:
    videoname=input("輸入youtube網址:\n")
    yt = YouTube(videoname)
    stream = yt.streams.first()
    stream.download("/home/dio/Music/")
    print('下載完成')
    #print("輸入網址錯誤")
