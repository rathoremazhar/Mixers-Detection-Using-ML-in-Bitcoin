# graywolf-api

## Install Dependencies 
pip3 install -r requirements.txt

## Run application for features collection
python3 aws_main.py


## Workflow of the app in aws_main.py
- Given a address, it will fetch 100 transactions from blockcypher platform using fetch_data.py
- It will convert the json to readable list format using json_to_csv.py
- It will preprocess the list format to get features using csv_to_features.py
- Store the calculated features on file-result (Otherthan graphical pattern related featues)

## Updated market prices csv for current bitcoin price
python3 market_price.py
