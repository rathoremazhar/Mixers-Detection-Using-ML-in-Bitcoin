import fetch_data as fd
import json_to_csv_transactions as jtcsv
import numpy
import pandas
import joblib 
import json
import sys
import time


def get_features(addresses):
    # Get Json Data
    s=time.time()
    json_data = fd.fetch_data(addresses)
    print("Fatch time",time.time()-s)

    # Json Data to List
    s=time.time()
    csv_data = jtcsv.json_to_csv(json_data, addresses)# This function also stored pattern statistics in a file. 
    print("param compute",time.time()-s)

 
    return pandas.DataFrame() ##Not required


def get_prediction(addresses):
    X = get_features(addresses).values[:, 1:].astype(float)


if __name__ == "__main__":
            
    addresses = []
    with open("SampleAddresses.txt", "r") as data:
         addresses = data.read().splitlines()
    print("lenght of addresses send", len(addresses))
    get_prediction(addresses)
    
