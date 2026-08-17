PI_INT="1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

E_INT="7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def pi_real(n):
    '''
    dado um número natural "n" maior que 0 e menor que 100 
    retorna uma string de uma aproximação pro número pi com "n" casa decimais'''
    sts="3,"
    casas=PI_INT[:n]
    st=sts+casas
    return st

def e_real(n):
    '''
    dado um número natural "n" maior que 0 e menor que 100 
    retorna uma string de uma aproximação pro número neperiano com "n" casa decimais'''
    tst="2,"
    casa=E_INT[:n]
    ts=tst+casa
    return ts
