import pyowm  # type: ignore
from datetime import datetime

owm = pyowm.OWM('ea95d7be6facb880f812da37738353fc')  # Ви повинні надати дійсний API-ключ
mgr = owm.weather_manager()

place = input('Введіть назву міста: ')

# Пошук поточної погоди
observation = mgr.weather_at_place(place)
w = observation.weather

print("Погода в " + place + ":")
print("Температура: " + str(w.temperature('celsius')['temp']) + "°C")
print("Вологість: " + str(w.humidity) + "%")
print("Швидкість вітру: " + str(w.wind()['speed']) + " м/с")
print("Статус погоди: " + w.status)
print("Деталі погоди: " + w.detailed_status)
print("Хмарність: " + str(w.clouds) + "%")
print("Видимість: " + str(w.visibility_distance) + " м")
print("Тиск: " + str(w.pressure['press']) + " гПа")
print("Захід сонця: " + str(w.sunset_time))