import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras import optimizers


Adam = optimizers.Adam

def construir_rede_neural(input_shape):
    # Carregar classes do data_loader
    from data_loader import carregar_bases_de_dados
    _, _, _, rotulos_teste, classes = carregar_bases_de_dados()
    numclasses = len(rotulos_teste[0])

    # Construção das bases de treinamento e teste
    class_index = {index: classe for index, classe in enumerate(classes)}
    print("Class Index:", class_index)

    # Compilação da rede neural
    rede_neural = Sequential()
    rede_neural.add(Conv2D(32, (3, 3), input_shape=input_shape, activation='relu'))
    rede_neural.add(MaxPooling2D(pool_size=(2, 2)))

    rede_neural.add(Conv2D(32, (3, 3), activation='relu'))
    rede_neural.add(MaxPooling2D(pool_size=(2, 2)))

    rede_neural.add(Flatten())

    # Adicione Dropout com uma taxa específica (por exemplo, 0.5)
    rede_neural.add(Dropout(0.5))

    # Ajuste o número de unidades nas camadas intermediárias conforme necessário
    rede_neural.add(Dense(units=128, activation='relu'))
    rede_neural.add(Dropout(0.5))

    rede_neural.add(Dense(units=64, activation='relu'))

    # Ajuste a camada de saída para ter o número correto de neurônios e a função de ativação softmax
    rede_neural.add(Dense(units=numclasses, activation='softmax'))

    # Use um otimizador com uma taxa de aprendizado específica (por exemplo, 0.001)
    otimizador = optimizers.Adam(learning_rate=0.001)

    # Compilação da rede neural
    rede_neural.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return rede_neural