import numpy as np
import cv2 

#-- Captura do video pela camera --#
cap = cv2.VideoCapture(0)

# Verifica se a câmera abriu corretamente
if not cap.isOpened():
    print("Erro: Não foi possível acessar a webcam.")
    exit()

print("Câmera aberta com sucesso! Pressione a tecla 'q' para sair.")

while True:
    # Lê um quadro (frame) da câmera
    ret, frame = cap.read()
    
    # Se a leitura falhou, interrompe o loop
    if not ret:
        print("Erro ao capturar o frame.")
        break
    
    # Exibe o frame em uma janela chamada "Webcam Teste"
    cv2.imshow("Webcam Teste", frame)
    
    # Aguarda 1 milissegundo se a tecla 'q' foi pressionada para fechar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha todas as janelas abertas
cap.release()
cv2.destroyAllWindows()