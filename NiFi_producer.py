# Import de la librairie
import json, ast
from kafka import KafkaProducer

f = open('./data.json')
data = json.load(f)
f.close()

producer = KafkaProducer(bootstrap_servers='20.126.103.217:9092')

for message in data:
    jdata = ast.literal_eval(str(message))
    jd = json.dumps(jdata)
    producer.send("KPE_streaming", bytes(jd,'UTF-8'))

producer.flush()
