#Predication of tips by comparing  bill amount and service rating
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Data set 
data = pd.DataFrame({ "bill_amount" : [500,800,1200,1500,2000,600,100,1800],
                     "service_rating" :[3,3.5,4,4.5,4.8,3.2,4.2,4.6],
                     "tip_percentage" :[5,8,12,15,18,6,12,16]
})

print("~~~~~~~~DATA SET ~~~~~~~~~")
print(data)


X = data[["bill_amount","service_rating"]]
Y = data ["tip_percentage"]


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#MODEL
model = LinearRegression()
model.fit(X_train ,Y_train)
print("~~~~~~~ACCURACY CHECK~~~~~~~~~")
#ACCURACY CHECK
Accuarcy = model.score(X_test,Y_test)
print(" model accuarcy is{Accuarcy*100:.1f}")

#INPUTS
bill_amount = (int(input("Enter your bill amount :")))
service_rating =(float(input("enter your service_rating:")))

Predication = model.predict([[bill_amount,service_rating]])

print("-----tip percentage----")
print("TIP == ",Predication)

