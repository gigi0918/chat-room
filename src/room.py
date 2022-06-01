
from datetime import datetime
from kafka import KafkaConsumer
from googletrans import Translator


# Init the Google API translator
translator = Translator()
# translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.kr',


consumer = KafkaConsumer('test_topic', group_id='test_topic_group')
def our_translate(msg):
    try:    
        translation = translator.translate(msg, dest='en').text
    except Exception as e:
        return msg
        
    return translation
    

for item in consumer:
    msg = (item.value).decode("utf-8") 
    print((item.key).decode("utf-8"))
    print(our_translate(msg))
    print(datetime.fromtimestamp(item.timestamp/1000).strftime('%Y-%m-%d %H:%M:%S'))
    print('\n')