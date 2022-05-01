__author__ = 'ave-_-avertino'
import random as rdm
import hashlib as hsl

simbolos = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-=,./;[]`~!@$%^&*()_+{}:<>qwertyuiop[]asdfghjkl;zxcvbnm,./' \
                '><MNBVCXZ:LKJHGFDSA}{POIUYTREWQ+_)(*&^%$@!1234567890-='
a_0 =  '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '1234567890'
a_z = 'abcdefghijklmnopqrstuvwxyz'
A_Z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a0_z = '1234567890abcdefghijklmnopqrstuvwxyz'
A0_Z = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a_Z = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
class Mistura(object):

    def mistura_altera(self):
        misturado = ''.join(rdm.sample(simbolos, len(simbolos)))
        codigo = hsl.sha512(misturado.encode())
        codificado = codigo.hexdigest()
        return [misturado, codificado]

    def mistura(self):
        misturado = ''.join(rdm.sample(simbolos, len(simbolos)))
        return misturado

class Referencias(object):

    def z_5(self):
        arranjos = []; q = 0; w = 0; e = 0; r = 0
        for i in a_0:
            for j in a_0:
                for k in a_0:
                    for z in a_0:
                        for y in a_0:
                            arranjos.append(i+j+k+z+y)
    '''recebe a_0'''
    def codigo(self, valor):
        casas = valor // 4
        resto = valor % 4
        print('casas=', casas, ' and resto=', resto)
        a = 0; b = 0; c = 0; d = 0; e = 0
        if (casas > 0):
            for i in range(casas):
                if (b == 3):
                    a = a + 1; b = 0; c = 0; d = 0; e = 3
                elif (c == 3):
                    b = b + 1; c = 0; d = 0; e = 3
                elif (d == 3):
                    c = c+1; d = 0; e = 3
                elif(e == 3):
                    d = d+1; e = 3
                else:
                    e = 3
        if (resto > 0):
            if (b == 3):
                a = a + 1;b = 0; c = 0; d = 0; e = resto-1
            elif (c == 3):
                b = b + 1; c = 0; d = 0; e = resto-1
            elif (d == 3):
                c = c + 1;d = 0; e = resto-1
            elif (e == 3):
                d = d + 1; e = resto-1
            else:
                e = resto-1
        print(str(a) + str(b) + str(c) + str(d) + str(e))
        retorno = a_0[a]+a_0[b]+a_0[c]+a_0[d]+a_0[e]
        return retorno