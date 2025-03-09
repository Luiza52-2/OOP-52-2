import requests  # Библиотека requests используется для отправки HTTP-запросов

response = requests.get("https://api.github.com")  # Отправляем GET-запрос
print(response.status_code)  # Выводим статус-код ответа
print(response.json())  # Выводим JSON-ответ