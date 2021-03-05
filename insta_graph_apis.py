import json as js
import requests as rq
import credentials as cr


def get_fb_page_id():
    response = rq.get(
        "https://graph.facebook.com/v10.0/me/accounts?access_token=" +
        cr.user_access_token)
    page_id = js.loads(response.text)['data'][0]['id']
    print(page_id)
    return page_id


def get_instagram_user_id():
    response = rq.get("https://graph.facebook.com/v10.0/105397334940653?fields=instagram_business_account&access_token="
                      + cr.user_access_token)
    user_id = js.loads(response.text)['instagram_business_account']['id']
    print(user_id)
    return user_id


def get_container_id_pic(image_url):
    headers = {
        "Authorization": "Bearer " + cr.user_access_token,

    }
    url = 'https://graph.facebook.com/' + cr.instagram_user_id + '/media?image_url=' + image_url
    data = {
        'caption': 'hello from datahunkdev #hello'
    }
    response = rq.post(url=url, headers=headers, data=data)
    print(response.text)
    return js.loads(response.text)['id']


def publish_pic(container_id):
    headers = {
        "Authorization": "Bearer " + cr.user_access_token,

    }
    url = 'https://graph.facebook.com/' + cr.instagram_user_id + '/media_publish?creation_id=' + container_id
    response = rq.post(url=url, headers=headers, )
    print(response.text)
