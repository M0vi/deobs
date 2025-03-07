import re

def limpar_texto(texto):
    """
    Limpa um texto removendo caracteres indesejados e formatando-o.
    Baseado na lógica do código Lua fornecido.
    """
    # 1. Remover caracteres não imprimíveis e de controle, substituindo por espaços
    cleaned = re.sub(r"[^\x20-\x7E\s]", " ", texto)

    # 2. Remover palavras isoladas (uma letra) cercadas por espaços
    cleaned = re.sub(r"\s\w\s", " ", cleaned)

    # 3. Remover sequências "@" seguidas ou precedidas por caracteres não-espaço
    cleaned = re.sub(r"\S@|\@\S", " ", cleaned)

    # 4. Remover "@" cercado por espaços
    cleaned = re.sub(r"\s@\s", " ", cleaned)

    # 5. Remover caracteres de controle
    cleaned = re.sub(r"[\x00-\x1F\x7F]", " ", cleaned)

    # 6. Remover espaços duplicados, substituindo por um único espaço
    cleaned = re.sub(r"\s+", " ", cleaned)

    # 7. Remover espaços no início e no fim da string
    cleaned = cleaned.strip()

    # 8. Substituir espaços por quebras de linha
    cleaned = cleaned.replace(" ", "\n")

    return cleaned

def processar_arquivo(input_file, output_file):
    """
    Lê o texto sujo de um arquivo, limpa o texto e salva em outro arquivo.
    
    Args:
        input_file (str): Caminho para o arquivo de entrada com texto sujo.
        output_file (str): Caminho para o arquivo de saída onde o texto limpo será salvo.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            texto_sujo = f.read()

        texto_limpo = limpar_texto(texto_sujo)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(texto_limpo)

        print(f"Texto limpo salvo em: {output_file}")

    except Exception as e:
        print(f"Erro ao processar arquivos: {e}")

# Exemplo de uso
if __name__ == "__main__":
    input_file = 'texto_sujo.txt'  # Nome do arquivo com texto sujo
    output_file = 'texto_limpo.txt'  # Nome do arquivo onde o texto limpo será salvo

    processar_arquivo(input_file, output_file)
