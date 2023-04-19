from datetime import datetime

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class NotaFiscal:
    def __init__(self, numero, data_emissao, produtos):
        self.numero = numero
        self.data_emissao = data_emissao
        self.produtos = produtos

    def calcular_valor_total(self):
        valor_total = 0
        for produto in self.produtos:
            valor_total += produto.preco * produto.quantidade
        return valor_total

    def imprimir_nota_fiscal(self):
        print(f"NOTA FISCAL - Número: {self.numero}")
        print(f"Data de Emissão: {self.data_emissao}")
        print("PRODUTOS:")
        for produto in self.produtos:
            print(f"{produto.quantidade}x {produto.nome} - R${produto.preco:.2f} cada")
        print(f"VALOR TOTAL: R${self.calcular_valor_total():.2f}")

# Exemplo de uso
produtos = [
    Produto("Camisa", 32.9, 2),
    Produto("Calça", 130.0, 1),
    Produto("Tênis", 289.9, 1),
]
nota_fiscal = NotaFiscal(123, datetime.now(), produtos)
nota_fiscal.imprimir_nota_fiscal()
