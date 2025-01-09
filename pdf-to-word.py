from pdf2docx import Converter

import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

def converter_pdf_para_word(pdf_file, word_file):
    """
    Converte um arquivo PDF para um arquivo Word (.docx).

    Parâmetros:
    pdf_file (str): caminho do arquivo PDF a ser convertido.
    word_file (str): caminho do arquivo Word a ser gerado.
    """
    
    cv = Converter(pdf_file)
    cv.convert(word_file, start=0, end=None)
    cv.close()

def selecionar_arquivo():

    pdf_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_file:
        word_file = pdf_file.replace('.pdf', '.docx')
        converter_pdf_para_word(pdf_file, word_file)
        label_status.config(text=f"Conversão concluída: {word_file}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversor PDF para Word")

label_instrucoes = tk.Label(root, text="Selecione um arquivo PDF para converter para Word")
label_instrucoes.pack(pady=10)

botao_selecionar = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
botao_selecionar.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=10)

root.mainloop()

