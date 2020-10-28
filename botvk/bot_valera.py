from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import random
from datetime import datetime

login, password = "79876369801", "frecher654456"
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)

# token = "6c0b511aaa0901bd514da8a04862e6055e3efa1fd1cb4d71dd6f267cd0013ff61e1586e4df636d6599088"
# vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        id = event.user_id
        user_get = session_api.users.get(user_ids=(id))
        user_get = user_get[0]
        first_name = user_get['first_name']
        last_name = user_get['last_name']
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        stop = "!"
        stop2 = "1"
        stop3 = stop + stop2
        if event.from_user and not (event.from_me):
            if response == "пидр":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': "Ты тоже, пидр)", 'random_id': 0})
            if response == "доброе утро":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': "И тебе, доброе утро)", 'random_id': 0})
            if response == "мыш":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': "гашиш", 'random_id': 0})
            if response == "иди нахуй":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': "Нахуй ты пойдешь, " +str(first_name) + ")", 'random_id': 0})
            if response == "иди в пизду":
                vk_session.method('messages.send', {'user_id': event.user_id,
                                                    'message': "В пизду ты пойдешь, " + str(first_name) + ")",
                                                    'random_id': 0})
            if response == "привет":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': "Приветик, " +str(first_name) + ")", 'random_id': 0})
            if response == "кто ты?":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': "Я бот Валера, пока что в моей базе не так много команд, но со временем я буду улучшен", 'random_id': 0})


