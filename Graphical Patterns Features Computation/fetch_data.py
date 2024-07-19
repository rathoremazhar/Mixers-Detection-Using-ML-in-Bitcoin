import requests
import fetch_api as fa
from jsonmerge import merge
import json
import pandas as pd
import numpy
import time
import os

'''
    Get Transaction details
    Save to file
'''

def fetch_data(addresses):
    x = numpy.array(addresses)
    jsons = []
    tokens = ['e286ac6826364af0a105574c5e6d2c0c','036fb999fba44934bb6231457e1facaa','07162c1e4f38413cbbca62b356415acf','a76de49b0cfd46bc8dd094513b17209c','0647ea1fa2e4469cb38c035bf3b4b6f2','965971a8b054410ebd31947ce81c8072','54cfa2aaff3c45d6b275236bd94a192e','1096ead613874bcd888fe8141dee5c9a','1b9e02d69bca4b629b11f4a7885adc69','bc31eddffb6d4c509e6c4ee54f654079','1bcb8387d44440fb8dd3b7cd7cd54779','3a4c47f36fc645b28c08300d64ce23bb','a1d49679ff9d46cfb2303c014cdab2be','bd544c4c553246b8b65a2f212c150e69', 'be06a644b1f946ff82d3c2f6b9d4f46e', 'a30a98c54f3c477f80440935a6f7dc37', 'fc2f27ba393c4f939b6e27549bb05a9f', 'b78fdb97553e48c0a542233d6995fe41', 'c140de712bb3483893be4b1bde5674f0', '1f88431ffc6e43439840f1ebd84eb806', 'a8eecf88ad9343d9ba92f0ee5b9bb331', 'ae17a4d7b6374ab6961a713c0304df2c', '70bb474dd22d490c9e5adf27f88ab822', '777ba260dabd44579aa3523bf5faf779', '1d77d12295854b56813c3426c621d5ba', '84e515c419a5404293ba8ac6600b6740', 'b10d384210514464b59825667e8f9737', '6d84f97a9f1d4d119d22547c36a20a8c']
    
    

    token_valid = 0
    '''
        Save the transactions from api
    '''

    for i in range(len(x)):
        transaction_id = x[i]
        # print(i, transaction_id)
        try:
            response = fa.get_transaction_data_50_first(transaction_id, tokens[token_valid])
            # print(response.status_code)
            while response.status_code == 429:
                print("token index " + str(token_valid) + " excedded due to error 429")
                token_valid+=1     
                response = fa.get_transaction_data_50_first(transaction_id, tokens[token_valid])
            json_data = response.json()
            data = json_data.get("txs")
        except:
            print("token index " + str(token_valid) + " excedded")
            token_valid+=1
            if token_valid >= len(tokens):
                print("cycling again")
                token_valid=0
            data = fa.get_transaction_data_50_first(transaction_id, tokens[token_valid]).json()['txs']
        before_id = data[-1]['block_height']
        # print(len(data))
        if len(data) >= 50:
            print("got into")
            try:
                data1 = fa.get_transaction_data_50_next(transaction_id,before_id, tokens[token_valid]).json()['txs']
            except:
                print("token index " + str(token_valid) + " excedded")
                token_valid+=1
                if token_valid >= len(tokens):
                    print("cycling again")
                    token_valid=0
                data1 = fa.get_transaction_data_50_next(transaction_id,before_id, tokens[token_valid]).json()['txs']
            for y in data1:
                data.append(y)
        jsons.append(data)
    return jsons