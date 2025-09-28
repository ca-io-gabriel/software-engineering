"""
    Este código e um modelo de Machine Learning que classifica
    espécies de flores Iris com base em características
    como comprimento e largura das sépalas e pétalas.
"""

# Importando as libs que serao usadas
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Carregando os dados das flores

iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Normalizando e pré-processando os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Construindo e compilando o modelo
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train_scaled.shape[1],)), # Camada de entrada
    tf.keras.layers.Dense(16, activation='relu'), # Camada escondida com ativação ReLU
    tf.keras.layers.Dense(12, activation='relu'), # Camada escondida com ativação ReLU
    tf.keras.layers.Dense(3, activation='softmax') # Camada escondida com ativação SoftMax
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Treinando o modelo
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', patience=10, restore_best_weights=True
)

history = model.fit(
    X_train_scaled, y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=16,
    callbacks=[early_stop],
    verbose=2
)

# Avaliando o modelo
loss, acc = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f'\nAvaliação no conjunto de teste: loss = {loss:.4f}, accuracy = {acc:.4f}')

# Testando o modelo
novas_amostras = np.array([
    [5.1, 3.5, 1.4, 0.2],  # Setosa
    [6.0, 2.9, 4.5, 1.5],  # Versicolor
    [6.9, 3.1, 5.4, 2.1]  # Virginica
])

new_samples_scaled = scaler.transform(novas_amostras)
probs = model.predict(new_samples_scaled)
pred_classes = np.argmax(probs, axis=1)

print("Saídas esperadas: "
      "\n Amostra 1: Iris Setosa"
      "\n Amostra 2: Iris Versicolor"
      "\n Amostra 3: Iris Virginica"
      )

for i, sample in enumerate(novas_amostras):
    print(f"\nAmostra {i + 1}: {sample}")
    print(f"Iris: {target_names[pred_classes[i]]} (probabilidades: {probs[i]})")
