# python -m venv venv (cria venv se necessário)
# .\venv\Scripts\activate (ativa a venv)
# deactivate (desativa venv)
# pip install -r requirements.txt
# cd C:\Users\marcus.silva05\Desktop\PRODUÇÃO\WEB_SCRAPING
# python TESTES_SCRAPING.py

# sys
from colorama import init, Fore, Back, Style
from datetime import datetime
import os
import platform
import pkgutil
import requests
import shutil
import socket
import subprocess
import sys

# leitura
import csv
import json
import re
import unicodedata
from docx import Document

# debug
from selenium import webdriver
from selenium.webdriver.edge.options import Options

init(autoreset=True) # reseta a cor no próximo print


# Estudar:

#
#📄 ARQUIVOS
## RENOMEAR/SUBSTITUIR



# CONTINUAR A ESTUDAR OS TIPOS:
# com pip = .docx, .xlsx, .pdf, .zip, .tar.gz                .pptx, 







##############################################################################################################################
#📂 ARQUIVOS (BAIXO NÍVEL)

## LER ARQUIVO
#conteudo = os.read(fd, 1024)  # Lê 1024 bytes
#print(f"Conteúdo: {conteudo}")
#
## ESCREVER ARQUIVO
#fd_w = os.open('novo.txt', os.O_WRONLY | os.O_CREAT)  # Abre para escrita
#bytes_escritos = os.write(fd_w, b'Texto qualquer')  # Escreve
#print(f"Bytes escritos: {bytes_escritos}")
#
## MOVER PONTEIRO
#os.lseek(fd, 0, os.SEEK_SET)  # Volta para o início
#os.lseek(fd, 10, os.SEEK_CUR)  # Avança 10 bytes
#os.lseek(fd, -5, os.SEEK_END)  # Volta 5 bytes do final
#
## FECHAR ARQUIVO
#os.close(fd)  # Fecha descritor
#os.close(fd_w)
#
## CONVERTER FD PARA FILE
#fd = os.open('arquivo.txt', os.O_RDONLY)
#file = os.fdopen(fd, 'r')  # Converte para objeto file
#conteudo = file.read()  # Lê todo o conteúdo
#print(f"Conteúdo: {conteudo}")
#file.close()
#
## DUPLICAR DESCRITOR
#fd2 = os.dup(fd)  # Duplica descritor
#os.dup2(fd, 1)  # Redireciona stdout para fd
#
## VERIFICAR SE É TERMINAL
#print("É terminal?", os.isatty(0))  # True/False
#
## SINCRONIZAR COM DISCO
#os.fsync(fd)  # Garante que dados foram escritos
#
## PIPE (comunicação entre processos)
#r, w = os.pipe()  # Cria pipe (leitura, escrita)
#print(f"Pipe: leitura={r}, escrita={w}")
#
##############################################################################################################################
#🔄 PROCESSOS
## EXECUTAR COMANDO (retorna código de saída)
#codigo = os.system('dir')  # Windows
#codigo = os.system('ls -la')  # Linux
#print(f"Código de saída: {codigo}")
#
## EXECUTAR E CAPTURAR SAÍDA
#resultado = os.popen('dir').read()  # Captura a saída
#print(f"Saída: {resultado}")
#
## ID DO PROCESSO
#print(f"PID: {os.getpid()}")  # ID do processo atual
#print(f"PID do pai: {os.getppid()}")  # ID do processo pai
#
## NÚMERO DE CPUs
#print(f"CPUs: {os.cpu_count()}")  # Número de núcleos
#
## TEMPOS DO PROCESSO
#tempos = os.times()
#print(f"Tempo de usuário: {tempos.user}")
#print(f"Tempo de sistema: {tempos.system}")
#
## NOME DO USUÁRIO
#print(f"Usuário: {os.getlogin()}")  # Nome do usuário logado
#
## MATAR PROCESSO
## os.kill(1234, 9)  # Mata processo com ID 1234 (sinal 9 = SIGKILL)
#
## ESPERAR PROCESSO
## pid, status = os.waitpid(1234, 0)  # Espera processo 1234 terminar
#
## ABORTAR
## os.abort()  # Aborta o processo (cuidado!)
#
## SAIR
## os._exit(0)  # Sai imediatamente (sem cleanup)
#
##############################################################################################################################
#🌍 VARIÁVEIS DE AMBIENTE
## VARIÁVEIS DE AMBIENTE
#print("TODAS AS VARIÁVEIS:", os.environ)  # Dicionário completo
#print("PATH:", os.environ['PATH'])  # Variável PATH
#print("USUÁRIO:", os.getenv('USERNAME', 'desconhecido'))  # Obtém com default
#print("USER:", os.getenv('USER', 'desconhecido'))  # Linux
#
## DEFINIR VARIÁVEL (cuidado - pode afetar o processo)
#os.environ['MINHA_VAR'] = 'valor'  # Define variável
#print("MINHA_VAR:", os.environ['MINHA_VAR'])
#
## REMOVER VARIÁVEL
## os.unsetenv('MINHA_VAR')  # Remove variável
#
##############################################################################################################################
#📊 INFORMAÇÕES DO SISTEMA
## INFORMAÇÕES DO SISTEMA
#print(f"Sistema: {os.name}")  # 'nt' (Windows) ou 'posix' (Linux)
#print(f"Separador: {os.sep}")  # '\\' (Windows) ou '/' (Linux)
#print(f"Separador PATH: {os.pathsep}")  # ';' (Windows) ou ':' (Linux)
#print(f"Quebra de linha: {repr(os.linesep)}")  # '\\r\\n' ou '\\n'
#print(f"Diretório atual: {os.curdir}")  # '.'
#print(f"Diretório pai: {os.pardir}")  # '..'
#print(f"Dispositivo nulo: {os.devnull}")  # 'nul' ou '/dev/null'
#
## TAMANHO DO TERMINAL
#tamanho = os.get_terminal_size()
#print(f"Terminal: {tamanho.columns} colunas x {tamanho.lines} linhas")
#
## SUPORTES
#print(f"Suporta bytes no environ? {os.supports_bytes_environ}")
#print(f"Suporta dir_fd? {os.supports_dir_fd}")
#print(f"Suporta fd? {os.supports_fd}")
#
##############################################################################################################################
#🔧 FUNÇÕES UTILITÁRIAS
## MENSAGEM DE ERRO
#print("Erro 2:", os.strerror(2))  # 'No such file or directory'
#
## CODIFICAÇÃO
#caminho_bytes = os.fsencode('pasta/arquivo.txt')  # Para bytes
#print(f"Bytes: {caminho_bytes}")
#caminho_str = os.fsdecode(caminho_bytes)  # Para string
#print(f"String: {caminho_str}")
#
## ABRIR COM PROGRAMA PADRÃO (Windows)
#os.startfile('arquivo.txt')  # Abre com programa associado
#os.startfile('arquivo.txt', 'print')  # Imprime (Windows)
#
## FSPATH (converte pathlib para string)
#from pathlib import Path
#caminho = Path('pasta/arquivo.txt')
#print("FSPath:", os.fspath(caminho))  # 'pasta/arquivo.txt'
#
##############################################################################################################################
#FIM




# sys
# shutil
# pathlib
# tempfile
# glob
# filecmp
# fileinput
# linecache
# genericpath
# ntpath
# posixpath
#
# pkgutil
# subprocess
# re
# unicodedata
# 
# socket
# socketserver
# ftplib
# telnetlib
# urllib
# http
# email
# json
# xml
# xmlrpc
# ipaddress
# cgi
# cgitb
# 
# sqlite3
# pymssql
# 
# datetime
# time
# 
# unittest
# doctest
# test
# pdb
# 
# importlib
# 
# pydoc
# 
# hashlib
# ssl
# 
# argparse
# 
# cmd
# rlcompleter
# pipes
# pty
# webbrowser
# 
# pip
# setuptools
# requests
# selenium
# urllib3
# certifi
# websocket
# socks






































