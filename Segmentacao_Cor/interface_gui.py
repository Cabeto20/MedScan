import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

class InterfaceSegmentacao:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MediScan - Sistema de Análise de Imagens Médicas")
        self.root.geometry("900x650")
        self.root.configure(bg="#f5f5f5")
        
        self.imagem = None
        self.imagem_rgb = None
        self.imagem_hsv = None
        self.paciente_id = ""
        
        # Marcadores colorimétricos usados em análises médicas
        self.cores = {
            'Eritrócitos (Vermelho)': ([0, 50, 50], [10, 255, 255]),
            'Tecido Saudável (Verde)': ([40, 50, 50], [80, 255, 255]),
            'Vasos/Veias (Azul)': ([100, 50, 50], [130, 255, 255])
        }
        
        self.criar_interface()
    
    def criar_interface(self):
        # Cabeçalho
        header = tk.Frame(self.root, bg="#1976D2", height=80)
        header.pack(fill=tk.X)
        tk.Label(header, text="🏥 MediScan", font=("Arial", 20, "bold"), bg="#1976D2", fg="white").pack(pady=5)
        tk.Label(header, text="Sistema de Análise de Imagens Médicas por Colorimetria", font=("Arial", 11), bg="#1976D2", fg="white").pack()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Frame de dados do paciente
        patient_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.RAISED, bd=1)
        patient_frame.pack(fill=tk.X, pady=(0, 10))
        tk.Label(patient_frame, text="ID do Paciente:", font=("Arial", 10), bg="#ffffff").pack(side=tk.LEFT, padx=10, pady=8)
        self.entry_paciente = tk.Entry(patient_frame, font=("Arial", 10), width=20)
        self.entry_paciente.pack(side=tk.LEFT, pady=8)
        
        # Frame de controles
        control_frame = tk.Frame(main_frame, bg="#f5f5f5")
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Botão importar imagem
        btn_importar = tk.Button(control_frame, text="📁 Importar Exame", 
                                command=self.importar_imagem, bg="#4CAF50", 
                                fg="white", font=("Arial", 11, "bold"), cursor="hand2")
        btn_importar.pack(side=tk.LEFT, padx=(0, 10))
        
        # Combobox para escolher análise
        tk.Label(control_frame, text="Tipo de Análise:", font=("Arial", 10, "bold"), bg="#f5f5f5").pack(side=tk.LEFT, padx=(0, 5))
        self.combo_cor = ttk.Combobox(control_frame, values=list(self.cores.keys()), 
                                     state="readonly", font=("Arial", 10), width=25)
        self.combo_cor.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botão processar
        btn_processar = tk.Button(control_frame, text="🔬 Analisar", 
                                 command=self.processar_imagem, bg="#1976D2", 
                                 fg="white", font=("Arial", 11, "bold"), cursor="hand2")
        btn_processar.pack(side=tk.LEFT, padx=(0, 10))
        
        # Label para mostrar resultado
        self.label_resultado = tk.Label(control_frame, text="", font=("Arial", 10, "bold"), bg="#f5f5f5", fg="#1976D2")
        self.label_resultado.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botão fechar
        btn_fechar = tk.Button(control_frame, text="❌ Fechar Sistema", 
                              command=self.root.quit, bg="#F44336", 
                              fg="white", font=("Arial", 11, "bold"), cursor="hand2")
        btn_fechar.pack(side=tk.RIGHT)
        
        # Frame para imagem original
        img_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.RAISED, bd=1)
        img_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(img_frame, text="Visualização do Exame", font=("Arial", 11, "bold"), bg="#ffffff").pack(pady=5)
        
        # Canvas para mostrar imagem
        self.canvas = tk.Canvas(img_frame, bg="#fafafa", relief=tk.SUNKEN, bd=1)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Texto inicial
        self.canvas.create_text(450, 300, text="🏥 Importe uma imagem médica para análise", 
                               font=("Arial", 14), fill="#666")
    
    def importar_imagem(self):
        arquivo = filedialog.askopenfilename(
            title="Selecionar Imagem Médica",
            filetypes=[
                ("Imagens Médicas", "*.jpg *.jpeg *.png *.bmp *.tiff *.dcm"),
                ("Todos os arquivos", "*.*")
            ]
        )
        
        if arquivo:
            try:
                self.imagem = cv2.imread(arquivo)
                self.imagem_rgb = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2RGB)
                self.imagem_hsv = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2HSV)
                
                self.mostrar_imagem_original()
                self.label_resultado.config(text="✅ Exame carregado! Selecione o tipo de análise.")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar imagem: {e}")
    
    def mostrar_imagem_original(self):
        # Redimensionar imagem para caber no canvas
        h, w = self.imagem_rgb.shape[:2]
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        
        if canvas_w > 1 and canvas_h > 1:  # Canvas já foi renderizado
            scale = min(canvas_w/w, canvas_h/h, 1.0)
            new_w, new_h = int(w*scale), int(h*scale)
            
            img_resized = cv2.resize(self.imagem_rgb, (new_w, new_h))
            img_pil = Image.fromarray(img_resized)
            img_tk = ImageTk.PhotoImage(img_pil)
            
            self.canvas.delete("all")
            self.canvas.create_image(canvas_w//2, canvas_h//2, image=img_tk)
            self.canvas.image = img_tk  # Manter referência
    
    def processar_imagem(self):
        if self.imagem is None:
            messagebox.showwarning("Aviso", "Primeiro importe um exame médico!")
            return
        
        cor_selecionada = self.combo_cor.get()
        if not cor_selecionada:
            messagebox.showwarning("Aviso", "Selecione o tipo de análise!")
            return
        
        self.paciente_id = self.entry_paciente.get() or "Não informado"
        
        try:
            # Obter limites da cor
            lower, upper = self.cores[cor_selecionada]
            lower = np.array(lower)
            upper = np.array(upper)
            
            # Criar máscara
            mascara = cv2.inRange(self.imagem_hsv, lower, upper)
            
            # Contar objetos
            contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            num_objetos = len(contornos)
            
            # Atualizar resultado
            self.label_resultado.config(text=f"🔬 {num_objetos} região(ões) detectada(s)")
            
            # Mostrar resultados em nova janela
            self.mostrar_resultados(cor_selecionada, mascara, contornos)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar: {e}")
    
    def mostrar_resultados(self, cor_nome, mascara, contornos):
        # Criar nova janela para resultados
        janela_resultado = tk.Toplevel(self.root)
        janela_resultado.title(f"Laudo - {cor_nome}")
        janela_resultado.geometry("1100x800")
        janela_resultado.configure(bg="#f5f5f5")
        
        # Frame principal com scroll
        main_frame = tk.Frame(janela_resultado)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas com scrollbar
        canvas_scroll = tk.Canvas(main_frame)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas_scroll.yview)
        scrollable_frame = tk.Frame(canvas_scroll)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all"))
        )
        
        canvas_scroll.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas_scroll.configure(yscrollcommand=scrollbar.set)
        
        # Criar figura matplotlib
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        
        # Imagem original
        axes[0,0].imshow(self.imagem_rgb)
        axes[0,0].set_title('Exame Original', fontsize=12, fontweight='bold')
        axes[0,0].axis('off')
        
        # Máscara
        axes[0,1].imshow(mascara, cmap='gray')
        axes[0,1].set_title(f'Mapa de Detecção', fontsize=12, fontweight='bold')
        axes[0,1].axis('off')
        
        # Resultado segmentado
        resultado = cv2.bitwise_and(self.imagem_rgb, self.imagem_rgb, mask=mascara)
        axes[1,0].imshow(resultado)
        axes[1,0].set_title(f'Regiões Isoladas', fontsize=12, fontweight='bold')
        axes[1,0].axis('off')
        
        # Contornos
        img_contornos = self.imagem_rgb.copy()
        cv2.drawContours(img_contornos, contornos, -1, (255, 0, 0), 3)
        axes[1,1].imshow(img_contornos)
        axes[1,1].set_title(f'Marcação de Áreas ({len(contornos)} região(ões))', fontsize=12, fontweight='bold')
        axes[1,1].axis('off')
        
        plt.tight_layout()
        
        # Incorporar matplotlib no frame scrollável
        canvas_plot = FigureCanvasTkAgg(fig, scrollable_frame)
        canvas_plot.draw()
        canvas_plot.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Laudo médico
        laudo_frame = tk.Frame(scrollable_frame, bg="#ffffff", relief=tk.RAISED, bd=2)
        laudo_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(laudo_frame, text="📋 LAUDO DE ANÁLISE COLORIMÉTRICA", font=("Arial", 14, "bold"), bg="#ffffff", fg="#1976D2").pack(pady=8)
        
        # Calcular área total dos objetos
        area_total = sum(cv2.contourArea(c) for c in contornos)
        area_imagem = self.imagem_rgb.shape[0] * self.imagem_rgb.shape[1]
        percentual = (area_total / area_imagem) * 100
        
        # Classificação de risco
        if percentual < 5:
            nivel_risco = "BAIXO"
            cor_risco = "#4CAF50"
        elif percentual < 15:
            nivel_risco = "MODERADO"
            cor_risco = "#FF9800"
        else:
            nivel_risco = "ALTO"
            cor_risco = "#F44336"
        
        import datetime
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M")
        
        laudo = f"""Paciente: {self.paciente_id}
Data/Hora: {data_hora}
Tipo de Análise: {cor_nome}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESULTADOS QUANTITATIVOS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔬 Regiões detectadas: {len(contornos)} área(s)
📏 Área total afetada: {area_total:.0f} pixels
📊 Percentual da imagem: {percentual:.2f}%
⚠️  Nível de concentração: {nivel_risco}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MÉTODO APLICADO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Técnica: Segmentação por espaço HSV
🔍 Algoritmo: Detecção de contornos externos
💡 Processamento: OpenCV + Análise colorimétrica"""
        
        tk.Label(laudo_frame, text=laudo, font=("Courier", 10), bg="#ffffff", justify=tk.LEFT).pack(pady=5, padx=15)
        
        # Indicador de risco
        risco_frame = tk.Frame(laudo_frame, bg=cor_risco, relief=tk.RAISED, bd=2)
        risco_frame.pack(fill=tk.X, padx=15, pady=10)
        tk.Label(risco_frame, text=f"NÍVEL DE CONCENTRAÇÃO: {nivel_risco}", font=("Arial", 12, "bold"), bg=cor_risco, fg="white").pack(pady=8)
        
        # Empacotar canvas e scrollbar
        canvas_scroll.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def executar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = InterfaceSegmentacao()
    app.executar()