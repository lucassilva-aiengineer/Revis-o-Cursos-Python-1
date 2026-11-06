# Geradores 

# O que são?
# Geradores são uma forma muito interessante, inteligente, de gerar iterações, 
# ao fim de trabalharmos com conjuntos de dados mais extensos. 


def geradores_parte_1():

    def meu_gerador():

        yield 1
        yield 2 
        yield 3 


    # Estes números apenas passam a existir na memória quando utilizados. 
    # geradores = meu_gerador()

    def situacao():
        for a in geradores:
            print(a)

        print(geradores)

    # Outra forma 

    def situacao_2():
        valor_1 = next(geradores)
        print(valor_1)

        valor_2 = next(geradores)
        print(valor_2)


    def situacao_3():
        total = sum(geradores)
        print("Soma dos geradores: " + str(total))

    # print(sorted(geradores))
    # print(sorted(geradores))


    def situacao_4(): 

        def countdown(num):
            print('Starting')

            while num > 0:
                yield num 
                num -= 1 

        cd = countdown(4)

        valor = next(cd)
        print(valor)

        print(next(cd))
        print(next(cd))
        print(next(cd))


    # situacao_4()

    def exemplos():

        import sys 

        def exemplo_1(n):

            nums = []
            num = 0

            while num < n:
                nums.append(num)
                num += 1 

            return nums 

        # print(sum(exemplo_1(10)))


        def exemplo_1_geradores(n): # Utilizando geradores 

            num = 0 
            while num < n:
                yield num 
                num += 1 
            

        # print(sum(exemplo_1_geradores(10)))

        # Verificando a econômia de memória 

            print(sys.getsizeof(exemplo_1(1000)))
            print(sys.getsizeof(exemplo_1_geradores(1000)))


        def exemplo_2(limite):

            """
                Implementando uma sequência de fibonacci
            """
            # 0 1 1 2 3 5 8 13 21...

            a, b = 0, 1
            while a < limite: 
                yield a 
                a, b = b, a + b 

        
            fib = exemplo_2(30)
            for a in fib: 
                print(fib)

        
        def exemplo_3():
            import sys 


            alvo = 10000
            meu_gerador_1 = (i for i in range(alvo) if i % 2 == 0)
            print(sys.getsizeof(meu_gerador_1))

            meu_gerador_2 = [i for i in range(alvo) if i  % 2 == 0]
            print(sys.getsizeof(meu_gerador_2))


        exemplo_3()


    exemplos()
    



def main():
    geradores_parte_1()


if __name__ == '__main__':
    main()