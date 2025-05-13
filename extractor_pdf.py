import os
import sys
import pytesseract
from pdf2image import convert_from_path
import fitz  # PyMuPDF
from tqdm import tqdm

# Diretório atual
actual_folder = os.getcwd()

# Lista de todos os arquivos PDF na pasta
pdf_list = [f for f in os.listdir(actual_folder) if f.lower().endswith('.pdf')]

# Inicializar o documento final
final_doc = fitz.open()

# Processar cada PDF
for nome_arquivo in sorted(pdf_list):
    caminho_pdf = os.path.join(actual_folder, nome_arquivo)
    paginas = convert_from_path(caminho_pdf, dpi=300)
    print(f"📄 Processando: {nome_arquivo} ({len(paginas)} páginas)")

    for img in tqdm(paginas, desc=f"   ➤ OCR", unit="página"):
        ocr_texto = pytesseract.image_to_pdf_or_hocr(img, extension='pdf', lang='por')

        # Criar página com OCR embutido
        pagina_ocr = fitz.open("pdf", ocr_texto)
        final_doc.insert_pdf(pagina_ocr)

# Salvar o PDF final
pasta_saida = os.path.join(os.getcwd(), "output_ocr")
os.makedirs(pasta_saida, exist_ok=True)

saida_pdf = os.path.join(pasta_saida, "pdf_pesquisavel.pdf")

if os.path.exists(saida_pdf):
    resposta = input(f"O arquivo '{saida_pdf}' já existe. Deseja sobrescrevê-lo? (s/N): ").strip().lower()
    if resposta != 's':
        print("Operação cancelada pelo usuário.")
        exit(0)  # Encerra o script com sucesso

final_doc.save(saida_pdf)
final_doc.close()

print(f"\nPDF final salvo como: {saida_pdf}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python extractor_pdf.py arquivo1.pdf [arquivo2.pdf ...]")
        sys.exit(1)
    
    arquivos_pdf = sys.argv[1:]  # Ignora o nome do script
    print(f"Arquivos recebidos: {arquivos_pdf}")

    # Aqui você continua o processamento normalmente...

if __name__ == "__main__":
    main()