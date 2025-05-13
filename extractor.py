import pytesseract
from pdf2image import convert_from_path
import os
import sys
from tqdm import tqdm
import zipfile

def extrair_texto_de_pdfs(pdfs):
    todas_imagens = []

    # Converter cada PDF em imagens
    for pdf in sorted(pdfs):
        caminho_completo = os.path.join(os.getcwd(), pdf)
        print(f"Convertendo PDF em imagens: {pdf}")
        paginas = convert_from_path(caminho_completo, dpi=300)
        todas_imagens.extend(paginas)

    arquivos_txt = []

    # Aplicar OCR em cada imagem
    for i, img in enumerate(tqdm(todas_imagens, desc="   ➤ OCR em texto", unit="página")):
        texto = pytesseract.image_to_string(img, lang='por')
        nome_arquivo = f"pagina_{i+1}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(texto)
        arquivos_txt.append(nome_arquivo)
        print(f"Texto da página {i+1} salvo em '{nome_arquivo}'")

    # Compactar arquivos .txt em um .zip
    with zipfile.ZipFile('ocr_files.zip', 'w') as zipf:
        for arquivo in arquivos_txt:
            zipf.write(arquivo)
            os.remove(arquivo)  # Remove o arquivo .txt depois de zipar

    print("OCR finalizado e arquivos compactados em 'ocr_files.zip'.")

def main():
    if len(sys.argv) < 2:
        print("Uso: python extractor.py arquivo1.pdf [arquivo2.pdf ...]")
        sys.exit(1)
    
    if len(sys.argv) > 1:
        arquivos_pdf = [arg for arg in sys.argv[1:] if arg.lower().endswith(".pdf")]
        if not arquivos_pdf:
            print("Nenhum arquivo PDF válido foi informado.")
            sys.exit(1)
    else:
        # Sem argumentos: buscar PDFs no diretório atual
        arquivos_pdf = [f for f in os.listdir(os.getcwd()) if f.lower().endswith(".pdf")]
        if not arquivos_pdf:
            print("Nenhum arquivo PDF encontrado no diretório atual.")
            sys.exit(1)

    print(f"📄 Arquivos PDF encontrados: {arquivos_pdf}")
    extrair_texto_de_pdfs(arquivos_pdf)

if __name__ == "__main__":
    main()
