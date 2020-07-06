import os
from six.moves import  urllib

import tarfile
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT +HOUSING_PATH+"/housing.tgz"

import pandas as pd
import matplotlib.pyplot as plt

def fetch_housing_data(housing_url=HOUSING_URL,housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path,"housing.tgz")
    urllib.request.urlretrieve(housing_url,tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(hoursing_path=HOUSING_PATH):
    csv_path = os.path.join(hoursing_path,"housing.csv")
    return pd.read_csv(csv_path)
if __name__=="__main__":
    housing=load_housing_data()
    print(housing.head())
    print(housing.info())
    housing.hist(bins=50,figsize=(20,15))
    housing.plot(kind="scatter",x='longitude',y='latitude',alpha=0.1)
    plt.show()
