from youtube_transcript_api import YouTubeTranscriptApi
import math
import sys
my_file = open("Youtube_links.txt", "r")
data = my_file.read()
my_file.close()
data_list = data.splitlines()
z = len(data_list)
L = []
for j in range(0,z):
    q = data_list[j].split("=")
    L = L+q
y = ""
r = len(L)
p = 0
for i in range(1,r,2):
    y = y + L[i]
    y = y + " "
links_list = y.split()
for t in range(0,len(links_list)):
    g=""
    yt = YouTubeTranscriptApi.get_transcript(links_list[t])


    for i in range(0,len(yt)):
        a = (yt[i])['text']
        g = g + a
        g = g + " "

    with open('output18.txt', 'a') as f:
        sys.stdout = f
        j = 1
        print(g)
        print(f"BITS Pilani")