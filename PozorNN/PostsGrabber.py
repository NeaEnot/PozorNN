import vk_api
import httplib2
import json
import time
import random

group_ids = [
    '89693462',
    '174296699',
    '75419495',
    '133180305',
    '71729358'
]

vk_session = vk_api.VkApi('', '')
vk_session.auth()
vk = vk_session.get_api()

group_count = 0

for id in group_ids:
    group_count += 1
    off = 0

    while True:
        try:
            posts = vk.wall.get(owner_id=int(f"-{id}"), count=100, offset=off, extended=1)

            i = 0
            count = posts['count']

            for post in posts['items']:
                i += 1

                if ('text' in post) and (post['text'] != ''):
                    text = post['text']
                    post_id = post['id']

                    try:
                        print(f'{group_count}-{id}/{off+i}/{count}: {post_id}')
                    
                        with open(f'Dataset\\{id}_{post_id}.txt', 'wb') as out:
                            out.write(bytearray(text, 'utf8'))
                    except Exception as e:
                        print(e)
        
            if i < 100:
                break
        
            off += 100
        except Exception as e:
            print(e)
            time.sleep(10)