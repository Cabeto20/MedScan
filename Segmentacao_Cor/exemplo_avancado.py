import cv2
import numpy as np
from matplotlib import pyplot as plt

def detectar_multiplas_cores(caminho_imagem):
    """Detecta múltiplas cores em uma única imagem"""
    img = cv2.imread(caminho_imagem)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Cores primárias da luz (RGB)
    cores = {
        'Vermelho': ([0, 50, 50], [10, 255, 255]),
        'Verde': ([40, 50, 50], [80, 255, 255]),
        'Azul': ([100, 50, 50], [130, 255, 255])
    }
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Imagem original
    axes[0,0].imshow(img_rgb)
    axes[0,0].set_title('Original')
    axes[0,0].axis('off')
    
    # Máscara combinada
    mascara_total = np.zeros(img_hsv.shape[:2], dtype=np.uint8)
    
    i = 1
    for nome, (lower, upper) in cores.items():
        lower = np.array(lower)
        upper = np.array(upper)
        
        mascara = cv2.inRange(img_hsv, lower, upper)
        mascara_total = cv2.bitwise_or(mascara_total, mascara)
        
        # Contar objetos
        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Mostrar resultado
        row = i // 3
        col = i % 3
        axes[row, col].imshow(mascara, cmap='gray')
        axes[row, col].set_title(f'{nome} ({len(contornos)} obj)')
        axes[row, col].axis('off')
        
        print(f"{nome}: {len(contornos)} objetos")
        i += 1
    
    # Resultado final
    axes[1,2].imshow(mascara_total, cmap='gray')
    axes[1,2].set_title('Todas as Cores')
    axes[1,2].axis('off')
    
    plt.tight_layout()
    plt.show()

def ajustar_limiar_interativo(caminho_imagem):
    """Permite ajustar os limiares de cor interativamente"""
    img = cv2.imread(caminho_imagem)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    def nada(val):
        pass
    
    # Criar janela com trackbars
    cv2.namedWindow('Controles')
    cv2.createTrackbar('H Min', 'Controles', 0, 179, nada)
    cv2.createTrackbar('S Min', 'Controles', 0, 255, nada)
    cv2.createTrackbar('V Min', 'Controles', 0, 255, nada)
    cv2.createTrackbar('H Max', 'Controles', 179, 179, nada)
    cv2.createTrackbar('S Max', 'Controles', 255, 255, nada)
    cv2.createTrackbar('V Max', 'Controles', 255, 255, nada)
    
    while True:
        # Obter valores dos trackbars
        h_min = cv2.getTrackbarPos('H Min', 'Controles')
        s_min = cv2.getTrackbarPos('S Min', 'Controles')
        v_min = cv2.getTrackbarPos('V Min', 'Controles')
        h_max = cv2.getTrackbarPos('H Max', 'Controles')
        s_max = cv2.getTrackbarPos('S Max', 'Controles')
        v_max = cv2.getTrackbarPos('V Max', 'Controles')
        
        # Criar máscara
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mascara = cv2.inRange(img_hsv, lower, upper)
        
        # Mostrar resultado
        cv2.imshow('Original', img)
        cv2.imshow('Mascara', mascara)
        
        print(f"Lower: [{h_min}, {s_min}, {v_min}] Upper: [{h_max}, {s_max}, {v_max}]")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    caminho = input("Digite o caminho da imagem: ")
    
    print("1 - Detectar múltiplas cores")
    print("2 - Ajustar limiares interativo")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        detectar_multiplas_cores(caminho)
    elif opcao == "2":
        ajustar_limiar_interativo(caminho)