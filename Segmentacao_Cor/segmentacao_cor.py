import cv2
import numpy as np
from matplotlib import pyplot as plt

class SegmentadorCor:
    def __init__(self, caminho_imagem):
        self.imagem = cv2.imread(caminho_imagem)
        self.imagem_rgb = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2RGB)
        self.imagem_hsv = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2HSV)
    
    def detectar_cor(self, cor_nome, lower_hsv, upper_hsv):
        """Detecta objetos de uma cor específica"""
        mascara = cv2.inRange(self.imagem_hsv, lower_hsv, upper_hsv)
        resultado = cv2.bitwise_and(self.imagem_rgb, self.imagem_rgb, mask=mascara)
        return mascara, resultado
    
    def contar_objetos(self, mascara):
        """Conta objetos na máscara"""
        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return len(contornos), contornos
    
    def mostrar_resultados(self, cor_nome, mascara, resultado, contornos):
        """Exibe os resultados"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Imagem original
        axes[0,0].imshow(self.imagem_rgb)
        axes[0,0].set_title('Imagem Original')
        axes[0,0].axis('off')
        
        # Máscara
        axes[0,1].imshow(mascara, cmap='gray')
        axes[0,1].set_title(f'Máscara - {cor_nome}')
        axes[0,1].axis('off')
        
        # Resultado segmentado
        axes[1,0].imshow(resultado)
        axes[1,0].set_title(f'Objetos {cor_nome}')
        axes[1,0].axis('off')
        
        # Contornos
        img_contornos = self.imagem_rgb.copy()
        cv2.drawContours(img_contornos, contornos, -1, (255, 0, 0), 2)
        axes[1,1].imshow(img_contornos)
        axes[1,1].set_title(f'Contornos ({len(contornos)} objetos)')
        axes[1,1].axis('off')
        
        plt.tight_layout()
        plt.show()

def main():
    # Faixas das cores primárias da luz (RGB) em HSV
    cores = {
        'vermelho': (np.array([0, 50, 50]), np.array([10, 255, 255])),
        'verde': (np.array([40, 50, 50]), np.array([80, 255, 255])),
        'azul': (np.array([100, 50, 50]), np.array([130, 255, 255]))
    }
    
    # Carregue sua imagem aqui
    caminho = input("Digite o caminho da imagem: ")
    
    try:
        segmentador = SegmentadorCor(caminho)
        
        print("Cores disponíveis:", list(cores.keys()))
        cor_escolhida = input("Escolha uma cor: ").lower()
        
        if cor_escolhida in cores:
            lower, upper = cores[cor_escolhida]
            mascara, resultado = segmentador.detectar_cor(cor_escolhida, lower, upper)
            num_objetos, contornos = segmentador.contar_objetos(mascara)
            
            print(f"Objetos {cor_escolhida} encontrados: {num_objetos}")
            segmentador.mostrar_resultados(cor_escolhida, mascara, resultado, contornos)
        else:
            print("Cor não disponível!")
            
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()