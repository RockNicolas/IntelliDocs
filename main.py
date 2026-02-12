from pdf_reader import extrair_dados_pdf
from excel_reader import ler_planilha
from report_generator import gerar_relatorio

PDF_PATH = ""
EXCEL_PATH = ""
SAIDA = ""

def main():
    print("📄 Lendo PDF...")
    texto_pdf = extrair_dados_pdf(PDF_PATH)

    print("📊 Lendo planilha...")
    planilha = ler_planilha(EXCEL_PATH)

    resulmo_planilha = planilha.describe().to_string()

    relatorio = f""

    {texto_pdf}

    {resulmo_planilha}
    ""

    print("📝 Gerando relatório...")
    gerar_relatorio(relatorio, SAIDA)
    
    print("✅ Relatório criado com sucesso!")

if __name__ == "__main__":
    main()