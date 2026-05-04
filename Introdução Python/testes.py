# 2. Receba um valor em Reais e converta para Dólares (considere a cotação de 5.00).

def correcao_moeda(real):
    dolar = real * 5.00
    print(f"R${real}(reais) são ${dolar}(dólares)")

print("Conversão de moeda, Real(R$) para Dólar($)")
real = float(input("Digite o valor a ser convertido: "))
conversao = correcao_moeda(real)
