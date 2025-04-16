import customtkinter as ctk
import threading
from monitor import iniciar_monitoramento, log_file
import pandas as pd
from overlay import Overlay


"""
global overlay
    if not executando["executando"]:
        executando["executando"] = True
        resultado.configure(text="Monitoramento em execução...")
        thread_monitor = threading.Thread(target=iniciar_monitoramento, args=(executando,))
        thread_monitor.start()
        overlay = Overlay(app)  # Inicia HUD flutuante

def parar():
    if executando["executando"]:
        executando["executando"] = False
        resultado.configure(text="Monitoramento finalizado.")
        gerar_metricas()
"""

# Flag de controle
executando = {"executando": False}
thread_monitor = None

def iniciar():
    global overlay
    if not executando["executando"]:
        executando["executando"] = True
        resultado.configure(text="Monitoramento em execução...")
        thread_monitor = threading.Thread(target=iniciar_monitoramento, args=(executando,))
        thread_monitor.start()
        overlay = Overlay(app)  # Inicia HUD flutuante

def parar():
    global overlay
    if executando["executando"]:
        executando["executando"] = False
        resultado.configure(text="Monitoramento finalizado.")
        gerar_metricas()
        if overlay:
            overlay.fechar()
            overlay = None

def gerar_metricas():
    df = pd.read_csv(log_file)

    metricas = {
        "CPU (%) média": df["cpu_percent"].mean(),
        "Temp. CPU (°C) média": df["cpu_temp"].dropna().mean(),
        "RAM usada (MB) média": df["ram_used_mb"].mean(),
        "RAM livre (MB) média": df["ram_free_mb"].mean(),
        "RAM (%) média": df["ram_percent"].mean(),
        "GPU (%) média": df["gpu_load"].dropna().mean(),
        "Temp. GPU (°C) média": df["gpu_temp"].dropna().mean()
    }

    texto = "\n".join([f"{k}: {round(v, 2)}" for k, v in metricas.items() if not pd.isna(v)])
    resultado.configure(text="Métricas:\n" + texto)

# UI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Monitoramento de Sistema")
app.geometry("500x400")

titulo = ctk.CTkLabel(app, text="Monitor de Uso do Sistema", font=("Arial", 20))
titulo.pack(pady=20)

btn_iniciar = ctk.CTkButton(app, text="Iniciar Monitoramento", command=iniciar)
btn_iniciar.pack(pady=10)

btn_parar = ctk.CTkButton(app, text="Parar e Exibir Métricas", command=parar)
btn_parar.pack(pady=10)

resultado = ctk.CTkLabel(app, text="", wraplength=400, justify="left")
resultado.pack(pady=20)

app.mainloop()
