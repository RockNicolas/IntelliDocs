from reportlab.pdfgen import canvas

def gerar_relatorio(texto, caminho_saida):
    c = canvas.Canvas(caminho_saida)

    largura_max = 90
    linhas = []

    for linha in texto.split("\n"):
        while len(linha) > largura_max:
            linhas.append(linha[:largura_max])
            linha = linha[largura_max]
        linhas.append(linha)

    y = 800

    for linha in linhas:
        c.drawString(40, y, linha)
        y -= 15

        if y < 50:
            c.showPage()
            y = 800
        
    c.save()