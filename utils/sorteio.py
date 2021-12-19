#-*-coding utf-8-*-
import random

TIMES=[
    'ABC/RN',
    'América/MG',
    'América/RJ',
    'América/RN',
    'Americano/RJ',
    'Atlético/GO',
    'Atlético/MG',
    'Atlético/PR',
    'Avaí/SC',
    'Bahia/BA',
    'Bangu/RJ',
    'Barueri/SP',
    'Botafogo/PB',
    'Botafogo/RJ',
    'Bragantino/SP',
    'Brasiliense/DF',
    'Ceará/CE',
    'Corinthians/SP',
    'Coritiba/PR',
    'CRB/AL',
    'Criciúma/SC',
    'Cruzeiro/MG',
    'CSA/AL',
    'Desportiva/ES',
    'Figueirense/SC',
    'Flamengo/RJ',
    'Fluminense/RJ',
    'Fortaleza/CE',
    'Gama/DF',
    'Goiás/GO',
    'Grêmio/RS',
    'Guarani/SP',
    'INTERLIMEIRA/SP',
    'Internacional/RS',
    'Ipatinga/MG',
    'Ituano/SP',
    'Ji-Paraná/RO',
    'Joinville/SC',
    'Juventude/RS',
    'Juventus/SP',
    'Londrina/PR',
    'Marília/SP',
    'Mixto/MT',
    'MotoClube/MA',
    'Nacional/AM',
    'Náutico/PE',
    'Olaria/RJ',
    'Operário/MS',
    'Palmas/TO',
    'Palmeiras/SP',
    'Paraná/PR',
    'Paulista/SP',
    'Paysandú/PA',
    'PONTEPRETA/SP',
    'PORTUGUESADESPORTOS/SP',
    'Remo/PA',
    'RIOBRANCO/AC',
    'RIOBRANCO/ES',
    'River/PI',
    'Roraima/RR',
    'SAMPAIOCORRÊA/MA',
    'SantaCruz/PE',
    'SANTOANDRE/SP',
    'Santos/SP',
    'SÃOCAETANO/SP',
    'SÃOPAULO/SP',
    'SRaimundo/AM',
    'Sergipe/SE',
    'Sport/PE',
    'Treze/PB',
    'TunaLuso/PA',
    'Uberlândia/MG',
    'UNIÃOBARBARENSE/SP',
    'UNIÃOSÃOJOÃO/SP',
    'VASCODAGAMA/RJ',
    'VILANOVA/GO',
    'VILLANOVA/MG',
    'Vitória/BA',
    'XVPIRACICABA/SP',
    'Ypiranga/AP'
]
MESES=[
    'Janeiro',
    'Fevereiro',
    'Março',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'    
]

def Sorteia(tipo,qt):
    if (tipo,qt):
        if tipo=='mega-sena':
            if qt>=6 and qt<=15:
                numeros=[]
                while len(numeros)<qt:
                    sorteado =  random.randint(1,60)
                    if sorteado not in numeros:
                        numeros.append(sorteado)
                numeros= sorted(numeros)
            else:
                return Exception("Quantidade inválida")
        elif tipo=='lotofacil':
            if qt>=15 and qt<=20:
                numeros=[]
                while len(numeros)<qt:
                    sorteado =  random.randint(1,25)
                    if sorteado not in numeros:
                        numeros.append(sorteado)
                numeros= sorted(numeros)
            else:
                return  Exception("Quantidade inválida")
        elif tipo=='lotomania':
            if qt==50:
                numeros=[]
                while len(numeros)<qt:
                    sorteado =  random.randint(0,99)
                    if sorteado not in numeros:
                        numeros.append(sorteado)
                numeros= sorted(numeros)
            else:
                return  Exception("Quantidade inválida")
        elif tipo=='super-sete':
            if qt==7:
                numeros=[]
                while len(numeros)<qt:
                    colunas=[]
                    while len(colunas)<qt:               
                        sorteado =  random.randint(0,9)
                        if sorteado not in colunas:
                            colunas.append(sorteado)
                    numeros.append(sorted(colunas))
            else:
                return  Exception("Quantidade inválida")
        elif tipo=='quina':
            if qt>=5 and qt<=15:
                numeros=[]
                while len(numeros)<qt:
                    sorteado =  random.randint(1,80)
                    if sorteado not in numeros:
                        numeros.append(sorteado)
                numeros= sorted(numeros)
            else:
                return Exception("Quantidade inválida")
        elif tipo=='dupla-sena':
            if qt>=6 and qt<=15:
                numeros=[]
                while len(numeros)<qt:
                    sorteado =  random.randint(1,50)
                    if sorteado not in numeros:
                        numeros.append(sorteado)
                numeros= sorted(numeros)
            else:
                return Exception("Quantidade inválida")
        elif tipo=='timemania':
            if qt==10 :
                numeros=[]
                while len(numeros)<qt:
                    sorteado =  random.randint(1,50)
                    if sorteado not in numeros:
                        numeros.append(sorteado)
                numeros= sorted(numeros)
                numeros.append(random.choice(TIMES))
            else:
                return Exception("Quantidade inválida")
        elif tipo=='dia-de-sorte':
            if qt>=7 and qt <=15 :
                numeros=[]
                while len(numeros)<qt:
                    sorteado =  random.randint(1,50)
                    if sorteado not in numeros:
                        numeros.append(sorteado)
                numeros= sorted(numeros)
                numeros.append(random.choice(MESES))
            else:
                return Exception("Quantidade inválida")
        
    return [str(i) for i in numeros]


