from tensorflow import keras
import tensorflow as tf

rn50model = tf.keras.applications.resnet50.ResNet50()
rn50preprocess = tf.keras.applications.resnet50.preprocess_input
rn50resolution = (224, 224, 3)

rn50cut = keras.Sequential()
for i in range(35):
    try:
        rn50cut.add(rn50model.layers[i])
    except:
        pass
rn50cut.compile()