import requests
import os
import main
from fastapi import HTTPException

def get_data(data:str='wine'):
    if data=='wine' or data=='house_price':
        if not os.path.isfile(data+'.csv'):
            url = main.url_wine if data == 'wine' else main.url_house_price
            r = requests.get(url, allow_redirects=True)
            open(data+'.csv', 'wb').write(r.content)
    else:
        raise HTTPException(status_code=500, detail="Unkown dataset: "+ data)