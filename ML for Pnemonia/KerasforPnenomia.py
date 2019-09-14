# %% [code]
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.

# %% [code]
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.layers.convolutional import Conv2D # to add convolutional layers
from keras.layers.convolutional import MaxPooling2D # to add pooling layers
from keras.layers import Flatten # to flatten data for fully connected layers
import numpy as np # for linear algebra
import matplotlib.pyplot as plt #for plotting things
import os
from PIL import Image
print(os.listdir("../input"))
from keras.preprocessing.image import ImageDataGenerator, load_img

# %% [code]
train_data= '../input/chest_xray/chest_xray/train/'
val_data = '../input/chest_xray/chest_xray/val/'
test_data = '../input/chest_xray/chest_xray/test/'

# %% [code]
os.listdir(train_data)

# %% [code]
train_n = train_data+'NORMAL/'
train_p = train_data+'PNEUMONIA/'

# %% [code]
CNN_model = Sequential()
CNN_model.add(Conv2D(32, (3, 3), activation="relu", input_shape=(64, 64, 3)))
CNN_model.add(MaxPooling2D(pool_size = (2, 2)))
CNN_model.add(Conv2D(32, (3, 3), activation="relu"))
CNN_model.add(MaxPooling2D(pool_size = (2, 2)))
CNN_model.add(Flatten())
CNN_model.add(Dense(activation = 'relu', units = 128))
CNN_model.add(Dense(activation = 'sigmoid', units = 1))

# Compile the Neural network
CNN_model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# %% [code]
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('../input/chest_xray/chest_xray/train',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')
validation_generator = test_datagen.flow_from_directory('../input/chest_xray/chest_xray/val/',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')
test_set = test_datagen.flow_from_directory('../input/chest_xray/chest_xray/test',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')


# %% [code]
CNN_model.summary()

# %% [code]
cnn_model = CNN_model.fit_generator(training_set,
                         steps_per_epoch = 15,
                         epochs = 10,
                         validation_data = validation_generator,
                         validation_steps = 25)

# %% [code]
test_accu = CNN_model.evaluate_generator(test_set,steps=64)

# %% [code]
print('The testing accuracy is :',test_accu[1]*100, '%')
