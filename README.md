# 🏥 MediScan - Sistema de Análise de Imagens Médicas

Sistema de processamento e análise de imagens médicas baseado em colorimetria, desenvolvido para auxiliar profissionais de saúde na detecção e quantificação de áreas de interesse em exames.

## 📋 Descrição

O **MediScan** é um sistema de visão computacional aplicado à área médica que utiliza análise colorimétrica para identificar, segmentar e quantificar regiões específicas em imagens de exames. O sistema emprega o espaço de cores HSV para detecção precisa de marcadores coloridos comumente usados em análises laboratoriais e histológicas.

### 🔬 Aplicações Clínicas

Este sistema pode ser utilizado para:
- **Análise de lâminas histológicas** coradas
- **Detecção de eritrócitos** em amostras sanguíneas
- **Identificação de tecidos** com marcadores colorimétricos
- **Quantificação de áreas vasculares** em exames
- **Análise de culturas celulares** com corantes específicos

### 🌈 Por que Análise Colorimétrica?

A colorimetria é fundamental em diagnósticos médicos pois:
- **Marcadores específicos** permitem identificar estruturas celulares
- **Corantes histológicos** (Hematoxilina-Eosina, Giemsa) usam cores primárias
- **Quantificação objetiva** reduz variabilidade entre observadores
- **Processamento automatizado** aumenta eficiência diagnóstica

## ✨ Funcionalidades

- **Análise colorimétrica**: Detecta regiões baseadas em marcadores de cor
- **Quantificação automática**: Conta e mede áreas de interesse
- **Interface médica profissional**: GUI adaptada para ambiente hospitalar
- **Geração de laudos**: Relatórios técnicos com métricas quantitativas
- **Classificação de risco**: Níveis de concentração (Baixo/Moderado/Alto)
- **Registro de pacientes**: Identificação e rastreabilidade
- **Visualização completa**: Múltiplas vistas do processamento

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **OpenCV** - Processamento de imagens médicas
- **NumPy** - Cálculos matemáticos e estatísticos
- **Matplotlib** - Visualização científica
- **Tkinter** - Interface gráfica profissional
- **PIL** - Manipulação de imagens

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd "Projeto AlgProcImg"
```

### 2. Instale as dependências

**Opção A - Automática:**
```bash
cd Segmentacao_Cor
python instalar_libs.py
```

**Opção B - Manual:**
```bash
pip install -r Segmentacao_Cor/requirements.txt
```

### 3. Teste a instalação
```bash
python Segmentacao_Cor/testar_libs.py
```

## 🚀 Como Usar

### Interface Médica (Recomendado)
```bash
python Segmentacao_Cor/interface_gui.py
```

**Fluxo de trabalho:**
1. Insira o ID do paciente
2. Clique em "📁 Importar Exame"
3. Selecione o tipo de análise desejada
4. Clique em "🔬 Analisar"
5. Visualize o laudo completo gerado

### Linha de Comando
```bash
python Segmentacao_Cor/segmentacao_cor.py
```

### Análises Avançadas
```bash
# Detectar múltiplas regiões
python Segmentacao_Cor/exemplo_avancado.py

# Teste automatizado
python Segmentacao_Cor/teste_automatico.py
```

## 📁 Estrutura do Projeto

```
Projeto AlgProcImg/
├── Segmentacao_Cor/
│   ├── imagens/                    # Imagens de exames
│   │   ├── amostra_eritrocitos.jpg
│   │   ├── amostra_tecido.jpg
│   │   ├── amostra_vascular.jpg
│   │   ├── amostra_mista.jpg
│   │   └── amostra_alta_densidade.jpg
│   ├── resultados/                 # Laudos salvos
│   ├── interface_gui.py           # Interface médica principal
│   ├── segmentacao_cor.py         # Módulo de processamento
│   ├── exemplo_avancado.py        # Análises avançadas
│   ├── teste_automatico.py        # Testes automatizados
│   ├── gerar_imagens_medicas.py   # Gerador de amostras médicas
│   ├── instalar_libs.py           # Instalador automático
│   ├── testar_libs.py            # Verificador de dependências
│   └── requirements.txt           # Lista de dependências
├── README.md                      # Documentação principal
└── GUIA_DE_TESTES.md              # Guia completo de testes
```

## 🎯 Tipos de Análise Disponíveis

O sistema detecta marcadores colorimétricos baseados nas cores primárias da luz:

| Análise | Faixa HSV (Lower) | Faixa HSV (Upper) | Aplicação Clínica |
|---------|-------------------|-------------------|-------------------|
| 🔴 Eritrócitos (Vermelho) | [0, 50, 50] | [10, 255, 255] | Detecção de hemácias, áreas hemorrágicas |
| 🟢 Tecido Saudável (Verde) | [40, 50, 50] | [80, 255, 255] | Identificação de tecidos normais corados |
| 🔵 Vasos/Veias (Azul) | [100, 50, 50] | [130, 255, 255] | Mapeamento vascular, núcleos celulares |

## 📊 Exemplo de Laudo Gerado

```
LAUDO DE ANÁLISE COLORIMÉTRICA
═══════════════════════════════════════════

Paciente: PAC-2024-001
Data/Hora: 15/01/2024 às 14:30
Tipo de Análise: Eritrócitos (Vermelho)

RESULTADOS QUANTITATIVOS:
═══════════════════════════════════════════

🔬 Regiões detectadas: 12 área(s)
📏 Área total afetada: 45230 pixels
📊 Percentual da imagem: 8.45%
⚠️  Nível de concentração: MODERADO

MÉTODO APLICADO:
═══════════════════════════════════════════

🎯 Técnica: Segmentação por espaço HSV
🔍 Algoritmo: Detecção de contornos externos
💡 Processamento: OpenCV + Análise colorimétrica
```

## 🔧 Personalização

### Adicionando Novos Marcadores

Para incluir novos corantes ou marcadores:

```python
cores = {
    # Marcadores padrão
    'Eritrócitos (Vermelho)': ([0, 50, 50], [10, 255, 255]),
    'Tecido Saudável (Verde)': ([40, 50, 50], [80, 255, 255]),
    'Vasos/Veias (Azul)': ([100, 50, 50], [130, 255, 255]),
    
    # Novos marcadores (exemplos)
    'Hematoxilina': ([100, 50, 50], [130, 255, 255]),  # Núcleos
    'Eosina': ([0, 50, 50], [10, 255, 255]),           # Citoplasma
    'Giemsa': ([140, 50, 50], [170, 255, 255])         # Parasitas
}
```

### Ajustando Sensibilidade

Use o modo interativo para calibrar valores HSV:

```bash
python Segmentacao_Cor/exemplo_avancado.py
# Escolha opção 2 para ajuste em tempo real
```

## 📈 Interpretação dos Resultados

### Níveis de Concentração

- **BAIXO** (< 5%): Concentração mínima detectada
- **MODERADO** (5-15%): Concentração significativa
- **ALTO** (> 15%): Alta concentração, requer atenção

### Métricas Fornecidas

- **Regiões detectadas**: Número de áreas identificadas
- **Área total**: Medida em pixels da região afetada
- **Percentual**: Proporção em relação à imagem total
- **Visualizações**: 4 vistas diferentes do processamento

## 🧪 Testes e Validação

### Gerar Imagens Médicas Simuladas
```bash
python Segmentacao_Cor/gerar_imagens_medicas.py
```

Isso criará 5 amostras médicas simuladas:
- `amostra_eritrocitos.jpg` - Detecção de hemácias
- `amostra_tecido.jpg` - Análise de tecido saudável
- `amostra_vascular.jpg` - Mapeamento vascular
- `amostra_mista.jpg` - Múltiplos marcadores
- `amostra_alta_densidade.jpg` - Alta concentração

### Executar Teste Automatizado
```bash
python Segmentacao_Cor/teste_automatico.py
```

### 📖 Guia Completo de Testes

Para instruções detalhadas sobre como testar o sistema, incluindo:
- Como gerar imagens de teste
- Onde encontrar imagens médicas reais
- Bancos de dados públicos (Kaggle, NIH, TCIA)
- Interpretação de resultados
- Solução de problemas

**Consulte o arquivo**: [`GUIA_DE_TESTES.md`](GUIA_DE_TESTES.md)

## ⚠️ Avisos Importantes

- Este sistema é uma **ferramenta auxiliar** de análise
- **Não substitui** avaliação de profissional qualificado
- Resultados devem ser **validados clinicamente**
- Uso recomendado para **triagem e quantificação**

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaAnalise`)
3. Commit suas mudanças (`git commit -m 'Add nova análise'`)
4. Push para a branch (`git push origin feature/NovaAnalise`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨💻 Autor

**Desenvolvedor**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)

## 🙏 Agradecimentos

- Comunidade OpenCV pela documentação em visão computacional médica
- Profissionais de saúde que forneceram feedback sobre usabilidade
- Comunidade Python pelo suporte técnico

## 📞 Suporte Técnico

Para problemas ou dúvidas:

1. Verifique se todas as dependências estão instaladas
2. Execute `python testar_libs.py` para diagnóstico
3. Consulte a documentação técnica
4. Abra uma issue no GitHub com detalhes

## 📚 Referências

- Processamento de imagens médicas com OpenCV
- Análise colorimétrica em histologia
- Padrões de coloração em laboratórios clínicos

---

⭐ **Sistema desenvolvido para auxiliar profissionais de saúde na análise quantitativa de imagens médicas**

🏥 **MediScan** - Tecnologia a serviço da saúde
