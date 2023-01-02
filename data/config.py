import json

# Подгружаем токен
with open('data/config.ini', 'r') as file:
        tg_data = json.load(file)
# и админов
admins  = []
for adm in tg_data["admins"].split():
    admins.append(adm)

# Bot token
BOT_TOKEN = tg_data["token"] 
# admins
ADMINS = admins 
