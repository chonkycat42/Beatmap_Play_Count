# need to install ossapi eg. pip install ossapi
from ossapi import Ossapi, UserLookupKey, GameMode, RankingType

# OAUTH stuff get this from the webiste
client_id = 34795
client_secret = 'fp1bCuG17Pxy9TC4X2BzUOU4ugdiS0JxvwMrmspF'
def most_played(username_user,beatmap_id):
    map_id = beatmap_id

    username_user = username_user
    api = Ossapi(client_id,client_secret)
    try:
        user = api.user(username_user, key=UserLookupKey.USERNAME)
        play_count = api.user(username_user, key=UserLookupKey.USERNAME).beatmap_playcounts_count
    except:
        return "User Not Found"
    try:
        user_info = api.user_beatmaps(user_id=user.id,type="most_played",limit=100, offset=0)
    except:
        return "beatmap ID does Not Exist"
    print(user.id)
    search = True
    user_info = api.user_beatmaps(user_id=user.id,type="most_played",limit=100, offset=0)




    i = 0 
    z = 0
    while search:
        if z+i > min(play_count-1,2000):
            search = False
            return (f'In order for it to not take long, I limited it to top 2000 most played, most likely {username_user} has played this map 1 or 2 times or not at all')

        if i == 50:
            i = 0
            z += 50
            user_info = api.user_beatmaps(user_id=user.id,type="most_played",limit=100, offset=z)
        
        if user_info[i].beatmap_id == map_id:
            times_played = user_info[i].count

            title = user_info[i].beatmapset.title
            artist = user_info[i].beatmapset.artist
            
            version = api.beatmap(beatmap_id=map_id).version
            search = False
            return (f'{username_user} played {artist} - {title} [{version}] {times_played} times! ')

        else:
            i += 1
        





