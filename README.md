# Controle Remoto de Slides via Navegador

Este projeto permite **controlar slides remotamente através de um navegador web** acessando um servidor local. O sistema possui uma interface simples com dois botões (seta para cima e para baixo) que disparam comandos de teclado no computador que hospeda o servidor, simulando o avanço ou retrocesso de slides (como no PowerPoint ou LibreOffice Impress).

## Visão Geral

- **Frontend (HTML + JS)**: Interface com dois botões (ícones de setas), estilizados com CSS e ícones do Font Awesome.
- **Backend (Flask + PyAutoGUI)**: Servidor que escuta comandos e dispara teclas usando `pyautogui`.
- **Comunicação**: A interface envia requisições HTTP para o servidor Flask, que simula pressionamento de teclas com `pyautogui`.

## Requisitos

- Python 3.x
- Flask
- PyAutoGUI
- Tkinter

## Execução

> É necessário ter o tkinter (tk) instalado globalmente.

**1 - Clone o repositório e abra a pasta:**
```bash
git clone https://github.com/albertojbe/remote-slide.git
cd remote-slide
```
\
**2 - Crie um ambiente virtual para o Python e execute-o:**
```bash
python -m venv venv
source venv/bin/activate (Para Linux e Mac)
.\venv\Scripts\activate (para Windows)
```
\
**3 - Instale as dependências:**
```bash
pip install -r requirements.txt
```
\
**4 - Execute o código:**
```bash
flask --app app run --host=0.0.0.0
```

Será retornado o IP da máquina na rede local, basta acessar esse IP na porta 5000 (`http://<IP-LOCAL>:5000`) para controlar o slide que esteja sendo apresentado.
