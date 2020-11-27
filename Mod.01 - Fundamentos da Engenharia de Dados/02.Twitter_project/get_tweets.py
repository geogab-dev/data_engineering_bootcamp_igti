# Import Libraries
import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime


# Definindo as chaves de acesso da API
CONSUMER_KEY = "your_key_here"
CONSUMER_SECRET = "your_key_here"

ACCESS_TOKEN = "your_key_here"
ACCESS_TOKEN_SECRET = "your_key_here"


# Arquivo de saida para armazenar os tweets coletados
now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
output = open(f"collected_tweets_{now}.txt", "w")

# implementação da classe para conexão com a API do Twitter
class MyListener(StreamListener):

    def on_data(self, data):
        str_item = json.dumps(data)
        output.write(str_item + "\n")
        return True

    def on_error(self, status):
        print(status)

        
# Main function
if __name__ == '__main__':
    listener_instance = MyListener()
    auth = OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)

    stream = Stream(auth=auth, listener=listener_instance)
    stream.filter(track=["Trump"])
