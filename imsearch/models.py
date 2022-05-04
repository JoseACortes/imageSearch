from classification_models.tfkeras import Classifiers
from tensorflow import keras

ResNet18, preprocess_input = Classifiers.get('resnet18')
rn18 = ResNet18((224, 224, 3), weights='imagenet')
rn18.compile()

rn18cut = keras.Sequential()
for i in range(35):
    try:
        rn18cut.add(rn18.layers[i])
    except:
        pass
rn18cut.compile()