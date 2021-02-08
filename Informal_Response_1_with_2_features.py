# code for model with bedrooms and square footage

import tensorflow as tf
import numpy as np
from tensorflow import keras
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[2])])
model.compile(optimizer='sgd', loss='mean_squared_error')
x1 = np.array([3,4,2,5,4,3], dtype=float) # number of bedrooms
x2 = np.array([2840,3680, 1479, 3051,3524,1238]) #square footage
x2 = x2/1000
xs = np.stack([x1,x2], axis=1)

ys = np.array([229000,399000,250000,347500,289000,97000],dtype=float) #price
ys = ys/100000 #price divided by 100000

model.fit(xs, ys, epochs=2000)

model.predict([xs])

# code for model with total rooms and square footage

import tensorflow as tf
import numpy as np
from tensorflow import keras
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[2])])
model.compile(optimizer='sgd', loss='mean_squared_error')
x1 = np.array([5,7,3,7,6,4], dtype=float) # number of rooms
x2 = np.array([2840,3680, 1479, 3051,3524,1238]) #square footage
x2 = x2/1000
xs = np.stack([x1,x2], axis=1)

ys = np.array([229000,399000,250000,347500,289000,97000],dtype=float) #price
ys = ys/100000 #price divided by 100000

model.fit(xs, ys, epochs=2000)

model.predict([xs])
