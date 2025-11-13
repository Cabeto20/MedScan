import subprocess
import sys

def instalar_biblioteca(nome):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", nome])
        print(f"✓ {nome} instalado com sucesso")
    except subprocess.CalledProcessError:
        print(f"✗ Erro ao instalar {nome}")

if __name__ == "__main__":
    bibliotecas = [
        "opencv-python",
        "numpy", 
        "matplotlib"
    ]
    
    print("Instalando bibliotecas necessárias...")
    for lib in bibliotecas:
        instalar_biblioteca(lib)
    
    print("\nTentando importar para verificar...")
    try:
        import cv2
        import numpy as np
        import matplotlib.pyplot as plt
        print("✓ Todas as bibliotecas funcionando!")
    except ImportError as e:
        print(f"✗ Erro de importação: {e}")