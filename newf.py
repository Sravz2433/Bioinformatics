

# Step 1: Load and preprocess the MNIST dataset
(x_train_full, y_train_full), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train_full, x_test = x_train_full / 255.0, x_test / 255.0  # Normalize pixel values

# Step 2: Split into training, validation, and test sets
x_train, x_val, y_train, y_val = train_test_split(x_train_full, y_train_full, test_size=0.15, random_state=42)
x_train, x_val, x_test = x_train.reshape(-1, 784), x_val.reshape(-1, 784), x_test.reshape(-1, 784)  # Flatten images

# Define potential hyperparameters (can adjust these during experimentation)
input_dim = 784  # 28x28 flattened images
hidden_units = 128  # number of units in hidden layers
output_dim = 10  # number of classes
dropout_rate = 0.2  # dropout to prevent overfitting
learning_rate = 0.001  # learning rate for optimizer
batch_size = 64  # batch size for training
epochs = 30  # maximum epochs for training

# Step 3: Build the MLP model
model = Sequential([
    Dense(hidden_units, activation='relu', input_shape=(input_dim,)),
    Dropout(dropout_rate),
    Dense(hidden_units, activation='relu'),
    Dropout(dropout_rate),
    Dense(output_dim, activation='softmax')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=learning_rate), 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# Step 4: Train the model with early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
history = model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, 
                    validation_data=(x_val, y_val), callbacks=[early_stopping])

# Step 5: Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy:.4f}")

# Report optimal hyperparameters
print(f"Optimal Hyperparameters:\n"
      f"- Hidden Units: {hidden_units}\n"
      f"- Dropout Rate: {dropout_rate}\n"
      f"- Learning Rate: {learning_rate}\n"
      f"- Batch Size: {batch_size}\n"
      f"- Epochs: {len(history.history['loss'])} (based on early stopping)")
