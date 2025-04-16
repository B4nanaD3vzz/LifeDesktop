# LifeDesktop

---

```markdown
# 🎯 PulseMonitor — Sistema de Monitoramento Avançado (Overlay + Logs)

> Monitoramento em tempo real de **CPU, GPU, RAM, Rede, FPS**, temperatura e muito mais — com overlay transparente, logging em CSV e análise de métricas.

---

## 🧩 Sobre o Projeto

O **Life Desktop** é uma aplicação desenvolvida em Python com uma interface leve e sobreposta (`overlay`) que coleta dados em tempo real do sistema e jogos. Ideal para análise de desempenho, amostragem técnica, testes de stress ou uso pessoal.

O sistema inclui:

- Monitoramento ao vivo de hardware
- Gravação de logs em `.csv`
- Interface gráfica com `customtkinter`
- Overlay transparente que permanece acima de todas as janelas
- Geração de métricas de uso ao final da sessão

---

## 📊 O que a aplicação monitora

| Recurso              | Detalhes coletados                                       |
|----------------------|-----------------------------------------------------------|
| **CPU**             | Uso (%) e temperatura                                     |
| **RAM**             | Uso (%), usada e livre em MB                              |
| **GPU (NVIDIA)**    | Uso (%) e temperatura                                     |
| **Internet**        | Upload e download em KB/s                                 |


---

## 🧰 Tecnologias e Bibliotecas Utilizadas

| Biblioteca           | Função principal                                  |
|----------------------|---------------------------------------------------|
| `psutil`             | Coleta dados de CPU, RAM, disco e rede            |
| `GPUtil`             | Coleta dados da GPU (NVIDIA)                      |
| `customtkinter`      | Interface gráfica moderna e personalizável        |
| `tkinter`            | Base para a GUI e overlay                         |
| `pandas`             | Geração de métricas com base nos logs             |
| `datetime` / `os`    | Manipulação de arquivos, diretórios e tempo       |

---

## 🖥️ Interface (Overlay)

- Caixa flutuante sobre todas as janelas
- Transparente com borda verde fina
- Texto em **verde limão** sobre fundo escuro (estilo HUD)
- Pode ser arrastada pela tela
- Exibe: CPU, RAM, GPU, Net.

---

## 📁 Estrutura de Arquivos

```
PulseMonitor/
├── main.py               # Inicia a aplicação e gera métricas finais
├── monitor.py            # Coleta e grava dados em tempo real
├── overlay.py            # Interface HUD sobreposta com informações ao vivo
├── logs/                 # Pasta onde os arquivos CSV são salvos
├── README.md             # Este documento
└── requirements.txt      # Bibliotecas necessárias
```

---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/B4nanaD3vzz/LifeDesktop.git
cd LifeDesktop
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. (Opcional) Instale o **RTSS** para monitorar FPS:
   - [Download RTSS (RivaTuner)](https://www.guru3d.com/files-details/rtss-rivatuner-statistics-server-download.html)

4. Execute a aplicação:

```bash
python main.py
```

---

## 📝 Como usar

- A interface HUD será aberta.
- Os dados começam a ser coletados automaticamente.
- Ao encerrar a aplicação (`Ctrl+C` ou fechar), os dados serão salvos em `logs/`.
- As métricas finais serão exibidas no terminal.

---

## 📈 Exemplo de saída

```
Métricas finais:
-----------------
CPU médio: 27.4%
RAM média: 58.3%
Upload médio: 32.1 KB/s
Download médio: 220.4 KB/s
...
```

---


## 🤝 Contribuições

Sinta-se livre para abrir issues, enviar PRs ou sugerir melhorias!

### Ideias futuras:
- Gráficos ao vivo com `matplotlib` ou `plotly`
- Amostrador de FPS
- Geração automática de relatórios em PDF
- Suporte a múltiplas GPUs
- Notificações de temperatura crítica

---

## 🧠 Autor

Desenvolvido por **[B4nanaD3vzz]**  
Se curtir, ⭐ no repo é sempre bem-vindo!

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```
