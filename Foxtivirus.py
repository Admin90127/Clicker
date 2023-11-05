import time
import random

print("Инициализация антивирусной проверки...\n")

for i in range(100):
    time.sleep(0.05)
    print(f"Сканирование: {i+1}% Завершено", end='\r')

print("\nСканирование завершено! Результаты:")

rand_number = random.randint(0, 10)
if rand_number > 7:
    print("Обнаружена вредоносная программа! Пожалуйста, примите меры.")
else:
    print("Угроз не обнаружено. Ваша система в безопасности.")
