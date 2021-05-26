import requests
import shutil

local_filename = 'music.m4a'
"""url = "http://catchup.hosting.thisisdax.com/045981f8-79a9-4036-813e-56da49b0fd5f/e553f299-e273-4498-a728-428df5e5e38a.m4a?aw_0_1st.channelid=d2bf085f-d4e0-4a6b-80d6-75d92bf0fcae&aw_0_1st.showid=045981f8-79a9-4036-813e-56da49b0fd5f&aw_0_1st.episodeid=55494584-b60b-4fd6-b105-988822872aa6&isLoggedIn=false&dax_version=release_2237&dax_player=GlobalPlayer&dax_platform=Web&aisDelivery=streaming&dax_listenerid=C235A5654319E4D04CBBE1D244F157F2&listenerid=250d62a811e06fdf77a9b385f55c98db&aw_0_1st.playerid=GlobalPlayer&aw_0_1st.skey=1621971946&aw_0_req.userConsentV2="
with requests.get(url, stream = True) as r:
    with open(local_filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)"""

"""from pydub import AudioSegment

sound = AudioSegment.from_file('clip.mp3')
sound.export('clip.wav', format='wav')

sound = AudioSegment.from_file('ad_start.mp3')
sound.export('ad_start.wav', format='wav')
sound = AudioSegment.from_file('ad_end.mp3')
sound.export('ad_end.wav', format='wav')"""

"""sound = AudioSegment.from_file(local_filename)

start = 1000 * 60 * 25
end = 1000 * 60 * 35
snippet = sound[start:end]

snippet.export("clip.mp3", format='mp3')"""

"""sound = AudioSegment.from_file('snippet.mp3', format='mp3')
start = 1000 * 89
end = 1000 * 91
snippet = sound[start:end]
snippet.export("snippet2.mp3", format='mp3')"""

"""start = 1000 * 60 * 4 + 1000 * 31
end = 1000 * 60 * 4 + 1000 * 37
snippet = sound[start:end]
snippet.export("snippet2.mp3", format='mp3')"""

import librosa
import numpy

clip, sr = librosa.load('music.m4a')

matcher, _ = librosa.load('ad_end.mp3')

frames = librosa.util.frame(clip, len(matcher), 45, axis=0)

print(len(matcher))
print(len(clip))
print(len(frames))

scores = []
for x, frame in enumerate(frames):
    num = numpy.correlate(frame, matcher)
    scores.append(num[0])

import soundfile as sf

for x, num in enumerate(scores):
    if num > 200:
        print(x)
        print(num)
        way_through = x/(len(scores)-(len(matcher)/45))
        mins = numpy.floor(way_through * 10)
        secs = ((way_through * 10) - mins)*60
        print('It is ' + str(mins) + ' mins and ' + str(secs) + ' secs.')
        sf.write(str(num)+'.wav', frames[x], sr)

#print(scores)