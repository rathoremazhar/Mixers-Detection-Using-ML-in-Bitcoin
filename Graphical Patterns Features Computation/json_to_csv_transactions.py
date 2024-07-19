import numpy
import json
import pandas as pd
import datetime
from datetime import timezone
import pytz
import csv
import fetch_api as fa


def json_to_csv(json_data, addresses):

    output_file = open('PatternFeatures.csv', "a") #Change the file location as per requirement.
    output_file.write('Address, No of fan-in, fan-out,scatter-gathered' + "\n")
    
 


    x_addresses = numpy.array(addresses)


    all_transactions = []
    for index_address in range(len(x_addresses)):

        j_transactions = json_data[index_address]
        # print(index_address, x_addresses[index_address])
        # print("j_transactions : ",j_transactions)

     
     
        total_fan_in = 0
        total_fan_out = 0
        total_scatter_gather = 0
        for j in j_transactions:
            
      

            block_height = j['block_height']
            no_of_inputs = j['vin_sz']
            no_of_outputs = j['vout_sz']
            preference = j['preference']
            if no_of_inputs == 1 and no_of_outputs > 1:
                total_fan_out+=1
            elif no_of_outputs == 1 and no_of_inputs > 1:
                total_fan_in+=1
            elif no_of_outputs > 1 and no_of_inputs > 1:
                total_scatter_gather+=1
        output_file.write(x_addresses[index_address] + ',' + str(total_fan_in) + ',' + str(total_fan_out) + ',' + str(total_scatter_gather) + '\n')

    output_file.close()    
    return all_transactions