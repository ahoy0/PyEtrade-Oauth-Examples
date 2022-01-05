# -*- coding: utf-8 -*-
import datetime as dt
import pandas as pd
import math as m
import pyetrade as et
import webbrowser
import matplotlib.pyplot as plt
import time

from dateutil.relativedelta import relativedelta as rd, MO
from datetime import datetime
 
class option_analysis():
    
    pd.set_option("expand_frame_repr", False)
    
    global _key, _secret, consumer_key, consumer_secret, dateshift
    
    _key = 'my_consumer_key'

    _secret = 'my_secret'
    
    consumer_key = _key
    
    consumer_secret = _secret
    
    def login():
        
        global tokens
        
        file_ref = "tokens.txt"     # insert file path
        
        oauth = et.ETradeOAuth(consumer_key, consumer_secret)
        
        webbrowser.open(oauth.get_request_token())
        
        time.sleep(10)
        
        with open(file_ref, 'r') as f:
            r = f.read()
            f.close()
        
        verifier_code = str(r[-6:-1])
        
        tokens = oauth.get_access_token(verifier_code)
        
        return tokens
 
if __name__ == "__main__":
    option_analysis.login()