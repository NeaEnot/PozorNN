import vk_api
import httplib2
import json
import time
import random

group_id = '71729358'

dump_path = 'oldest_off.json'
oldest_off = None

try:
    with open(dump_path, 'r') as dump:
        oldest_off = json.loads(dump.read())
except Exception as e:
    None

vk_session = vk_api.VkApi('+79278275685', 'Jastinbiber123')
vk_session.auth()
vk = vk_session.get_api()

if oldest_off == None:
    off = 0
else:
    off = oldest_off

while True:
    try:
        posts = vk.wall.get(owner_id=int(f"-{group_id}"), count=100, offset=off, extended=1)

        i = 0
        count = posts['count']

        for post in posts['items']:
            i += 1

            if ('text' in post) and (post['text'] != ''):
                text = post['text']
                id = post['id']

                try:
                    print(f'{off+i}/{count}: {id}')
                    
                    with open(f'Dataset\\{id}.txt', 'wb') as out:
                        out.write(bytearray(text, 'utf8'))
                except Exception as e:
                    print(e)
        
        if i < 100:
            break
        
        off += 100

        with open(dump_path, 'w') as dump:
            dump.write(json.dumps(off))
    except Exception as e:
        print(e)
        time.sleep(10)