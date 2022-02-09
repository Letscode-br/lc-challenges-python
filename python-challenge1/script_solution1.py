################ Funções Twist ################

def converte_char_int(caractere):
    """Converte um caractere para um inteiro segundo a tabela ASCII
    com correção do valor segundo enunciado e uso da função ord(), para que:

    '_' = 0, 'a' = 1, 'b' = 2, ..., 'z' = 26 e '.' = 27

    Args:
        caractere (str): caractere a ser convertido em inteiro

    Returns:
        [int]: inteiro correspondente ao caractere
    """
    if caractere == '.':
        return 27

    elif caractere == '_':
        return 0

    return ord(caractere) - 96


def converte_int_char(inteiro):

    """Converte um inteiro para um caractere segundo a tabela ASCII
    com correção do valor do inteiro, segundo enunciado e uso da função chr(), para que:

    0 = '_' = , 1 = 'a' = , 2 = 'b', ..., 26 = 'z' e 27 = '.'

    Args:
        inteiro (int): inteiro a ser convertido em caractere

    Returns:
        [str]: caractere correspondente ao inteiro 
    """
    if inteiro == 27:
        return '.'

    elif inteiro == 0:
        return '_'

    return chr(inteiro + 96) 


def codifica(lista_codigoplano, chave_k):
    """A partir de codigoplano aplica a função de codificação segundo
    Método Twist

    Args:
        lista_codigoplano (list): lista com os códigos que representam codigoplano
        chave_k (int): chave para codificação

    Returns:
        [list]: lista que representa cifradocodigo
    """
    n_tam_msg = len(lista_codigoplano)
    lista_cifradocodigo = monta_lista_base(lista_codigoplano)

    for i in range(n_tam_msg):
        lista_cifradocodigo[i] = (lista_codigoplano[(chave_k * i) % n_tam_msg] - i) % 28
    return lista_cifradocodigo


def decodifica(lista_cifradocodigo,  chave_k):
    """A partir de lista_cifradocodigo aplica a função de decodificação segundo
    Método Twist

    Args:
        lista_cifradocodigo (list): lista com elementos de cifradocodigo
        chave_k (int): chave para decoficação

    Returns:
        [list]: lista com elementos que representam codigoplano
    """
    n_tam_msg = len(lista_cifradocodigo)
    lista_codigoplano = monta_lista_base(lista_cifradocodigo)

    for i in range(n_tam_msg):
        lista_codigoplano[(chave_k * i) % n_tam_msg] = (lista_cifradocodigo[i] + i) % 28
    
    return lista_codigoplano


################ Funções auxiliares ################

def aplica_conversao(funcao, lista_ref):
    """Aplica uma função de conversão em cada elemento da lista_ref
    construindo uma nova lista com os valores convertidos

    Args:
        funcao (function): função de conversão a ser aplicada
        lista_ref ([type]): lista de referência com os valores a serem convertidos pela funcao

    Returns:
        [list]: lista com elementos convertidos
    """
    return [funcao(i) for i in lista_ref]


def to_string(lista_ref):
    """ Constrói uma string a partir dos elementos de uma lista

    Args:
        lista_ref (list): lista de referência para construção da string

    Returns:
        [str]: string formada pelos elementos da lista_ref
    """
    return ''.join(lista_ref)


def monta_lista_base(lista_ref):

    """A partir de uma lista_ref constrói uma nova lista
    de mesmo tamanho e elementos None

    Args:
        lista_ref (list): lista de referência para o tamanho da nova lista

    Returns:
        [list]: lista com elementos None com mesmo tamanho de lista_ref
    """
    return [None]*len(lista_ref)

################ MAIN ################

def main():
    """Interface com o usuário para receber o texto a ser convertido,
    chave de conversão e opção selecionada    
    """

    opcao = input('Digite 0 para codificar e 1 para decodificar: ')
    chave_k = int(input('Digite a chave: '))
    texto = input('Digite a mensagem: ')

    if opcao == '0':
        lista_textoplano = list(texto)
        codigoplano = aplica_conversao(converte_char_int, lista_textoplano)
        cifradocodigo = codifica(codigoplano, chave_k)
        lista_textocifrado = aplica_conversao(converte_int_char, cifradocodigo)
        textocifrado = to_string(lista_textocifrado)
        print(f'Frase final: {textocifrado}')

    else:
        lista_textocifrado = list(texto)
        cifradocodigo = aplica_conversao(converte_char_int, lista_textocifrado)
        codigoplano = decodifica(cifradocodigo, chave_k)
        lista_textoplano = aplica_conversao(converte_int_char, codigoplano)
        textoplano = to_string(lista_textoplano)
        print(f'Frase final: {textoplano}')

if __name__ == '__main__':
    main()