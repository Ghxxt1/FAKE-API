# Arthur Melquiades de Freitas, Brenno Santiago e Marco Antônio Souza - 3° Periodo - TADS.
# MOSTRANDO UMA FAKE API COM O TEMA: LOJA DE PESCA.

class Pesca:
    def __init__(self): 
        self.items = []

    def menu(self):
        print("\n=== Loja de Pesca ===")
        print("1. Cadastrar item")
        print("2. Deletar item")
        print("3. Listar itens")
        print("4. Mostrar valor total dos itens")
        print("5. Sair")

    def cadastrar_item(self):
        nome = input("Nome do produto: ").strip()
        if nome == "":
            print("Nome inválido.")
            return
        preco = input("Preço do produto (ex: 29.90): ").replace(',', '.').strip()
        if not self.numero_valido(preco):
            print("Preço inválido.")
            return
        preco = float(preco)
        if preco <= 0:
            print("Preço deve ser maior que zero.")
            return
        self.items.append({'nome': nome, 'preco': preco})
        print(f'Produto "{nome}" adicionado!')

    def deletar_item(self):
        if len(self.items) == 0:
            print("Nenhum produto para deletar.")
            return
        self.listar_itens()
        indice = input("Número do item para deletar: ").strip()
        if not indice.isdigit():
            print("Entrada inválida.")
            return
        indice = int(indice)
        if 1 <= indice <= len(self.items):
            item = self.items.pop(indice -1)
            print(f'Produto "{item["nome"]}" removido.')
        else:
            print("Número inválido.")

    def listar_itens(self):
        if len(self.items) == 0:
            print("Nenhum produto cadastrado.")
            return
        print("\nItens cadastrados:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item['nome']} - R$ {item['preco']:.2f}")

    def valor_total(self):
        if len(self.items) == 0:
            print("Nenhum produto cadastrado.")
            return
        total = 0
        for item in self.items:
            total += item['preco']
        print(f"\nTotal: R$ {total:.2f}")

    def numero_valido(self, valor):
        pontos = 0
        if valor == "" or valor == ".":
            return False
        for c in valor:
            if c == ".":
                pontos += 1
                if pontos > 1:
                    return False
            elif c < "0" or c > "9":
                return False
        return True

    def iniciar(self):
        while True:
            self.menu()
            op = input("Escolha uma opção: ").strip()
            if op == "1":
                self.cadastrar_item()
            elif op == "2":
                self.deletar_item()
            elif op == "3":
                self.listar_itens()
            elif op == "4":
                self.valor_total()
            elif op == "5":
                print("Até mais... Agradecemos a preferência. Tenha um Ótimo Dia!!")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    Pesca().iniciar()



