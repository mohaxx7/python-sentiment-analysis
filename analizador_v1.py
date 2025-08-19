from transformers import pipeline
classifier = pipeline("sentiment-analysis")
milista = ["wow this is so cool I love it", "This is disgusting!", "I neither like it nor dislike it"]

for frase in milista:
    resultado=classifier(frase)
     # 2. Imprimir la frase original para saber a qué resultado corresponde
    print("Frase analizada:")
    print(frase)

    # 3. Imprimir el resultado que te ha devuelto el modelo
    print("Resultado del modelo:")
    print(resultado)
    
    # 4. Añadir un separador para que la salida sea más limpia
    print("-------------------------")

print("--- Análisis finalizado ---")
