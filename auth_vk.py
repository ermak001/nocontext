import vk_api
import requests as r
import schedule
import time
import os
import random
import index
import settings as s

session = vk_api.VkApi(s.login, s.password, scope='messages, wall, groups, photos, offline')
session.auth()
vk = session.get_api()

def load_post():
    upload_url = vk.photos.getWallUploadServer(group_id='194375042')['upload_url']
    DIR = r"memes_pars"
    post_photo = '\\' + random.choice(os.listdir(DIR))
    request = r.post(upload_url, files={'file': open(DIR + post_photo, "rb")})
    save_wall_photo = vk.photos.saveWallPhoto(group_id='194375042', photo=request.json()['photo'],
                                              server=request.json()['server'], hash=request.json()['hash'])
    saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
    check_posting(saved_photo, post_photo)

def check_posting(saved_photo, post_photo):
    file_open = open('post_up', 'r')
    old_post = file_open.readlines()
    for data in old_post:
        data_post = data.split(' ')
        if post_photo not in data_post:
            posting(saved_photo)
            print('Check Post: Ok')
        else:
            index.main()
            load_post()
            print('Error')
    file_open.close()

def posting(saved_photo):
    vk.wall.post(owner_id='-194375042', attachments = saved_photo)
    save_post(saved_photo)
    print('Posting: ok')

def save_post(post_photo):
    file_open = open('post_up', 'a')
    file_open.write(post_photo + ' ')
    file_open.close()
    print('Save post: ok')




schedule.every(60).minutes.do(load_post)

while True:
    schedule.run_pending()
    time.sleep(120)






