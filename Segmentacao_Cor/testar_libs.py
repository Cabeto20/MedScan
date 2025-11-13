print("Testando importacao das bibliotecas...")

try:
    import cv2
    print("OK - OpenCV importado")
    print(f"Versao OpenCV: {cv2.__version__}")
except ImportError as e:
    print(f"ERRO - OpenCV: {e}")

try:
    import numpy as np
    print("OK - NumPy importado")
    print(f"Versao NumPy: {np.__version__}")
except ImportError as e:
    print(f"ERRO - NumPy: {e}")

try:
    import matplotlib.pyplot as plt
    print("OK - Matplotlib importado")
except ImportError as e:
    print(f"ERRO - Matplotlib: {e}")
    print("Instalando matplotlib...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    print("Matplotlib instalado!")

print("\nTodas as bibliotecas estao prontas para uso!")