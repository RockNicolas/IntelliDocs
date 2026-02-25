import os
from dotenv import load_dotenv

from pdf_reader import extrair_dados_pdf
from excel_reader import ler_planilha
from report_generator import gerar_relatorio

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
EXCEL_PATH = os.getenv("EXCEL_PATH")
SAIDA = os.getenv("SAIDA_RELATORIO")

def main():
    print("🔎 Verificando arquivos...")

    texto_pdf = ""
    encontrou_pdf = False

    if os.path.isdir(PDF_PATH):
        for arquivo in os.listdir(PDF_PATH):
            if arquivo.lower().endswith(".pdf"):
                encontrou_pdf = True
                caminho_completo = os.path.join(PDF_PATH, arquivo)
                print(f"📄 Processando PDF: {arquivo}")
                texto_pdf += extrair_dados_pdf(caminho_completo) + "\n"
    else:
        print("❌ Caminho de PDF inválido.")
        return

    import pandas as pd
    planilhas_consolidadas = pd.DataFrame()
    encontrou_excel = False

    if os.path.isdir(EXCEL_PATH):
        for arquivo in os.listdir(EXCEL_PATH):
            if arquivo.lower().endswith((".xlsx", ".xls")):
                encontrou_excel = True
                caminho_completo = os.path.join(EXCEL_PATH, arquivo)
                print(f"📊 Processando Planilha: {arquivo}")
                df = ler_planilha(caminho_completo)
                planilhas_consolidadas = pd.concat(
                    [planilhas_consolidadas, df],
                    ignore_index=True
                )
    else:
        print("❌ Caminho de planilhas inválido.")
        return

    if not encontrou_pdf and not encontrou_excel:
        print("⚠️ Nenhum PDF ou planilha encontrado. Relatório não gerado.")
        return

    resumo_planilha = ""
    if not planilhas_consolidadas.empty:
        resumo_planilha = planilhas_consolidadas.describe().to_string()

    from datetime import datetime

    nome_arquivo = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    caminho_saida = os.path.join(SAIDA, nome_arquivo)

    relatorio = f"""
================= RELATÓRIO AUTOMÁTICO =================

📄 DADOS DOS PDFs:
{texto_pdf}

📊 RESUMO DAS PLANILHAS:
{resumo_planilha}
"""

    print("📝 Gerando relatório...")
    gerar_relatorio(relatorio, caminho_saida)

    print(f"✅ Relatório criado com sucesso em:\n{caminho_saida}")

if __name__ == "__main__":
    main()