import requests

print("key = ")
key = raw_input()
print("id = ")
yt = raw_input()

r = requests.get('https://www.googleapis.com/youtube/v3/videos?id=' + yt + '&key=' + key + '&part=statistics').json()

like = int(r['items'][0]['statistics']['likeCount'])
dislike = int(r['items'][0]['statistics']['dislikeCount'])

print("like = %d" % like)
print("dislike = %d" % dislike)
