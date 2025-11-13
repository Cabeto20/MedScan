import cv2
import numpy as np
import os

def criar_amostra_eritrocitos():
    """Simula lâmina com eritrócitos (hemácias)"""
    img = np.ones((600, 800, 3), dtype=np.uint8) * 240  # Fundo claro
    
    # Adicionar eritrócitos (círculos vermelhos)
    np.random.seed(42)
    for i in range(25):
        x = np.random.randint(50, 750)
        y = np.random.randint(50, 550)
        raio = np.random.randint(15, 30)
        cv2.circle(img, (x, y), raio, (180, 30, 30), -1)  # Vermelho escuro
    
    cv2.imwrite('imagens/amostra_eritrocitos.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("✅ Criada: amostra_eritrocitos.jpg")

def criar_amostra_tecido():
    """Simula tecido corado em verde"""
    img = np.ones((600, 800, 3), dtype=np.uint8) * 230
    
    # Adicionar áreas de tecido saudável (verde)
    for i in range(15):
        x = np.random.randint(100, 700)
        y = np.random.randint(100, 500)
        w = np.random.randint(40, 80)
        h = np.random.randint(40, 80)
        cv2.rectangle(img, (x, y), (x+w, y+h), (40, 180, 40), -1)
    
    cv2.imwrite('imagens/amostra_tecido.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("✅ Criada: amostra_tecido.jpg")

def criar_amostra_vascular():
    """Simula estruturas vasculares (azul)"""
    img = np.ones((600, 800, 3), dtype=np.uint8) * 245
    
    # Adicionar vasos sanguíneos (linhas azuis)
    for i in range(8):
        x1 = np.random.randint(0, 800)
        y1 = np.random.randint(0, 600)
        x2 = np.random.randint(0, 800)
        y2 = np.random.randint(0, 600)
        cv2.line(img, (x1, y1), (x2, y2), (30, 30, 200), np.random.randint(10, 25))
    
    # Adicionar alguns círculos azuis (cortes transversais)
    for i in range(10):
        x = np.random.randint(50, 750)
        y = np.random.randint(50, 550)
        raio = np.random.randint(20, 40)
        cv2.circle(img, (x, y), raio, (40, 40, 180), -1)
    
    cv2.imwrite('imagens/amostra_vascular.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("✅ Criada: amostra_vascular.jpg")

def criar_amostra_mista():
    """Simula exame com múltiplos marcadores"""
    img = np.ones((600, 800, 3), dtype=np.uint8) * 235
    
    # Eritrócitos
    for i in range(12):
        x = np.random.randint(50, 350)
        y = np.random.randint(50, 550)
        cv2.circle(img, (x, y), np.random.randint(15, 25), (180, 30, 30), -1)
    
    # Tecido
    for i in range(8):
        x = np.random.randint(300, 500)
        y = np.random.randint(100, 500)
        cv2.rectangle(img, (x, y), (x+50, y+50), (40, 180, 40), -1)
    
    # Vasos
    for i in range(5):
        x = np.random.randint(500, 750)
        y = np.random.randint(50, 550)
        cv2.circle(img, (x, y), np.random.randint(20, 35), (40, 40, 180), -1)
    
    cv2.imwrite('imagens/amostra_mista.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("✅ Criada: amostra_mista.jpg")

def criar_amostra_alta_densidade():
    """Simula exame com alta concentração de eritrócitos"""
    img = np.ones((600, 800, 3), dtype=np.uint8) * 240
    
    # Muitos eritrócitos
    for i in range(80):
        x = np.random.randint(30, 770)
        y = np.random.randint(30, 570)
        raio = np.random.randint(12, 22)
        cv2.circle(img, (x, y), raio, (190, 25, 25), -1)
    
    cv2.imwrite('imagens/amostra_alta_densidade.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("✅ Criada: amostra_alta_densidade.jpg")

if __name__ == "__main__":
    print("🔬 Gerando imagens médicas simuladas...\n")
    
    # Criar diretório se não existir
    os.makedirs('imagens', exist_ok=True)
    
    criar_amostra_eritrocitos()
    criar_amostra_tecido()
    criar_amostra_vascular()
    criar_amostra_mista()
    criar_amostra_alta_densidade()
    
    print("\n✅ Todas as amostras foram criadas na pasta 'imagens/'")
    print("\n📋 Amostras disponíveis:")
    print("   1. amostra_eritrocitos.jpg - Detecção de hemácias")
    print("   2. amostra_tecido.jpg - Análise de tecido saudável")
    print("   3. amostra_vascular.jpg - Mapeamento vascular")
    print("   4. amostra_mista.jpg - Múltiplos marcadores")
    print("   5. amostra_alta_densidade.jpg - Alta concentração")
