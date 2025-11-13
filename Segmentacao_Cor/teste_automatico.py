import cv2
import numpy as np
from matplotlib import pyplot as plt

# Testar o segmentador automaticamente
def teste_segmentacao():
    # Carregar imagem de teste
    img = cv2.imread('imagens/teste_cores.jpg')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Cores primárias da luz (RGB)
    cores = {
        'Vermelho': ([0, 50, 50], [10, 255, 255]),
        'Verde': ([40, 50, 50], [80, 255, 255]),
        'Azul': ([100, 50, 50], [130, 255, 255])
    }
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    
    # Imagem original
    axes[0,0].imshow(img_rgb)
    axes[0,0].set_title('Imagem Original')
    axes[0,0].axis('off')
    
    i = 1
    for nome, (lower, upper) in cores.items():
        lower = np.array(lower)
        upper = np.array(upper)
        
        # Criar máscara
        mascara = cv2.inRange(img_hsv, lower, upper)
        
        # Contar objetos
        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Mostrar resultado
        row = (i-1) // 2
        col = (i-1) % 2 + 1
        axes[row, col].imshow(mascara, cmap='gray')
        axes[row, col].set_title(f'{nome}: {len(contornos)} objetos')
        axes[row, col].axis('off')
        
        print(f"{nome}: {len(contornos)} objetos detectados")
        i += 1
    
    # Remover subplot vazio
    axes[1,2].axis('off')
    
    plt.tight_layout()
    plt.savefig('resultados/teste_resultado.png', dpi=150, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    print("Executando teste automatico...")
    teste_segmentacao()
    print("Teste concluido! Resultado salvo em resultados/teste_resultado.png")