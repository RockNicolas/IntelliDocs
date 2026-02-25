import pdfplumber

def extrair_dados_pdf(caminho):
    texto_total = ""

    with pdfplumber.open(caminho) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                texto_total += texto + "\n"

    return texto_total