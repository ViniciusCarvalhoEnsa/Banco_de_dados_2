import threading
import random
import time
from pymongo import MongoClient

#Conexão com o banco de dados MongoDB
client = MongoClient('localhost', 27017)
db = client['bancoiot']
collection = db['sensores']

#Gera temperatura aleatória
def generate_temperature():
    return round(random.uniform(30, 40), 2)

#Verifica se o sensor está alarmado
def check_alarm(sensor_name, temperature):
    if temperature > 38:
        collection.update_one({'nomeSensor': sensor_name}, {'$set': {'sensorAlarmado': True}})
        print(f"Atenção! Temperatura muito alta! Verificar Sensor {sensor_name}!")
        return True
    return False

#Função para executar cada thread (sensor)
def sensor_thread(sensor_name):
    while True:
        temperature = generate_temperature()
        print(f"Sensor {sensor_name}: {temperature} C°")
        if check_alarm(sensor_name, temperature):
            break
        collection.update_one({'nomeSensor': sensor_name}, {'$set': {'valorSensor': temperature}})
        time.sleep(2)  # tempo de espera entre leituras

#Criar threads para cada sensor
threads = []
for i in range(3):
    sensor_name = f"Temp{i+1}"
    thread = threading.Thread(target=sensor_thread, args=(sensor_name,))
    threads.append(thread)
    thread.start()

#Aguarda threads terminarem
for thread in threads:
    thread.join()






