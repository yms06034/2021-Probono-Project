from tensorflow import keras

#MachineLeanring Engine

def engine(x_train, x_val, y_train, y_val):
    model = keras.Sequential()
    model.add(keras.layers.Embedding(500, 16, input_length=500))
    model.add(keras.layers.LSTM(8, dropout=0.3, return_sequences=True)) 
    model.add(keras.layers.LSTM(8, dropout=0.3))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)

    model.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])
    checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5')
    early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)
    history = model.fit(x_train, y_train, epochs=100, batch_size=64, validation_data=(x_val, y_val), callbacks=[checkpoint_cb, early_stopping_cb])

    rnn_model = keras.models.load_model('best-model.h5')

    return rnn_model
