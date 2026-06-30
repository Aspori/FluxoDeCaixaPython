# 💰 Fluxo de Caixa em Python

Aplicação simples em **Python** para controle de fluxo de caixa via terminal, permitindo registrar receitas e despesas e visualizar o saldo final em conta.

---

## ✨ Funcionalidades

- ➕ **Cadastro de receitas** — nome e valor
- ➖ **Cadastro de despesas** — nome e valor (convertido automaticamente para negativo no fluxo)
- 📋 **Relatório final** com a listagem de todas as movimentações
- 💵 **Cálculo automático do saldo total** em conta

---

## ▶️ Como executar

Pré-requisito: ter o **Python 3** instalado.

```bash
python fluxo_de_caixa.py
```

> No Windows, o terminal é limpo automaticamente ao iniciar (`cls`). Em sistemas Linux/macOS, ajuste o comando para `clear` se necessário.

---

## 🧭 Como usar

Ao rodar o programa, um menu é exibido:

```
______________
@ Fluxo de caixa
______________
1- Adicionar receita
2- Adicionar despesa
______________

# Digite outro número para encerrar #
```

- Digite **1** para adicionar uma receita (nome e valor)
- Digite **2** para adicionar uma despesa (nome e valor)
- Digite **qualquer outro número** para encerrar o cadastro e visualizar o relatório final

### Exemplo de uso

```
Digite a opção: 1
Nome: Venda de produto
Valor: R$500

Digite a opção: 2
Nome: Aluguel
Valor: R$200

Digite a opção: 0

Nome: Venda de produto Valor: R$ 500.0
Nome: Aluguel Valor: R$ -200.0

Valor em conta é: R$ 300.0
```

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Lógica e execução do programa |
| Listas e dicionários | Armazenamento das movimentações |
| `os.system` | Limpeza do terminal |

---

## 📚 Aprendizados

Projeto desenvolvido para praticar lógica de programação em Python, com foco em:
- Estruturas de repetição e condicionais
- Manipulação de listas de dicionários
- Entrada e validação básica de dados via terminal
- Organização de código em funções

---

## 🚀 Possíveis melhorias futuras

- [ ] Validação de entradas (evitar erros com valores não numéricos)
- [ ] Persistência dos dados em arquivo (CSV/JSON) ou banco de dados
- [ ] Formatação monetária mais precisa (2 casas decimais)
- [ ] Exportação do relatório final
- [ ] Interface gráfica ou web

---

## 👨‍💻 Autor

Desenvolvido por **Vinicius Amorim Cataldi** ([@Aspori](https://github.com/Aspori))
