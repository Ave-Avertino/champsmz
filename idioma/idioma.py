

def geral(lingua):

    if(lingua=='en-US'):
        pass
    else:
        from idioma.pt_PT import geral
        return [geral.palavras]

def contas(lingua):
    if(lingua=='en-US'):
        pass
    else:
        from idioma.pt_PT import geral, contas
        return [geral.palavras, contas.palavras]

def laboratorio(lingua):

    if(lingua=='en-US'):
        pass
    else:
        from idioma.pt_PT import geral, laboratorio
        return [geral.palavras, laboratorio.palavras]

def farmacia(lingua):

    if(lingua=='en-US'):
        pass
    else:
        from idioma.pt_PT import geral, farmacia
        return [geral.palavras, farmacia.palavras]

def qc(lingua):

    if(lingua=='en-US'):
        pass
    else:
        from idioma.pt_PT import geral, qc
        return [geral.palavras, qc.palavras]