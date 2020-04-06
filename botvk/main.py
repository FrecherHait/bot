from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
from datetime import datetime

login, password = "79176394637", "frecher3271"
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)

# token = "6585bfc8ca94c2989d0a5cafc3d70b3e9a4c0921bb4096ad46a9189b13e6b1a1e2c6848756f048709e558"
# vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        if event.from_user and not (event.from_me):
            if response == "1":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': "Приветик)", 'random_id': 0})
            if response == "привет":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': "Приветик)", 'random_id': 0})

