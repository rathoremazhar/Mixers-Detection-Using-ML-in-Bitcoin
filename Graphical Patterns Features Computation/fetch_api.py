import json
import requests

def get_transaction_data_50_first(address, token):
   return requests.get("https://api.blockcypher.com/v1/btc/main/addrs/" + str(address) + "/full?limit=50&token=" + str(token)) 

def get_transaction_data_50_next(id, before, token):
   return requests.get("https://api.blockcypher.com/v1/btc/main/addrs/" + id + "/full?limit=50&before=" + str(before) + "&token=" + str(token)) 


def get_transaction_coinBaseData(id):
   return requests.get("https://api.blockchain.info/haskoin-store/btc/address/" + id + "/transactions/full?limit=5&offset=0")
