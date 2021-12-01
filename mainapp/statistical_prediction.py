

from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
# check for stationarity 

def ad_test(dataset):
     dftest = adfuller(dataset, autolag = 'AIC')
     dicti = {}
     dicti["1. ADF : "] = dftest[0]
     dicti["2. P-Value : "] = dftest[1]
     dicti["3. Num Of Lags : "] = dftest[2]
     dicti ["4. Num Of Observations Used For ADF Regression:"] = dftest[3]


     print("1. ADF : ",dftest[0])
     print("2. P-Value : ", dftest[1])
     print("3. Num Of Lags : ", dftest[2])
     print("4. Num Of Observations Used For ADF Regression:",      dftest[3])
     print("5. Critical Values :")
     for key, val in dftest[4].items():
         print("\t",key, ": ", val)

     return dicti

    