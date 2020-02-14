import sys
import requests


def get_info(method, id, token):
    try:
        return requests.get('https://api.vk.com/method/' + method + id + '&access_token=' + token + '&v=5.95').json()
    except:
        print("Check your internet connection")
        sys.exit()


def get_friend(token, id):
    friends = get_info('users.get?user_ids=', id, token)['response']
    print(friends)


def get_albums(token, id):
    try:
        albums = get_info('photos.getAlbums?owner_id=', str(id), token)['response']['items']
    except:
        print('get new token')
        sys.exit()
    print('Список альбомов пользователя')
    for i in albums:
        print(i['title'])


if __name__ == '__main__':
    with open('token.txt', 'r') as file:
        token = file.read()
    get_friend(token, sys.argv[1])
    get_albums(token, sys.argv[1])
