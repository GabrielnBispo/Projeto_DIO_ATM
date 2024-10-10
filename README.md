# 🏧 ATM Simulator

Este é um projeto simples de um **Caixa Eletrônico (ATM)** implementado em Python. O sistema permite que os usuários façam depósitos, saques e verifiquem o extrato da conta, respeitando limites de saldo, saques e número de operações diárias.

## 🚀 Funcionalidades

- **💵 Depósito**: O usuário pode depositar valores na conta, desde que sejam números válidos e positivos.
- **💸 Saque**: O usuário pode sacar valores da conta, respeitando o saldo disponível, o limite de saque por operação e o número máximo de saques diários.
- **📄 Extrato**: O usuário pode visualizar o extrato com todas as operações realizadas e o saldo atual.
- **Limites**:
  - 🏦 **Limite de saque por operação**: R$ 500,00.
  - 🕒 **Máximo de 3 saques por dia**.

## 🛠 Tecnologias

- **Python 3.x**

## 📦 Como Executar

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/GabrielnBispo/Projeto_DIO_ATM.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd atm-simulator
   ```
3. Execute o script principal:
   ```bash
   python atm.py
   ```

## 📝 Uso

Ao iniciar o programa, um menu com as seguintes opções será exibido:

```
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
```

Selecione a operação desejada digitando a letra correspondente e siga as instruções exibidas na tela.

Para sair do sistema, basta selecionar a opção `[q] Sair`.

## 💡 Exemplo de Uso

Selecione a opção que deseja:

```
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
```

=> `d`  
Informe o valor do depósito: 150.00  

Selecione a opção que deseja:

```
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
```

=> `e`  

================ EXTRATO ================  
Depósito de R$ 150.00  

Saldo: R$ 150.00  

=========================================  

## 🙏 Agradecimentos

Gostaria de agradecer ao **Professor Guilherme Carvalho**, Python Consultant na Oak Solutions, pela orientação durante o desenvolvimento deste projeto.

<a href="https://www.linkedin.com/in/guilherme-arthur-de-carvalho/" target="_blank" style="display: inline-block; padding: 10px 20px; margin: 5px; background-color: #0077B5; color: white; text-align: center; text-decoration: none; border-radius: 5px;">LinkedIn</a>
<a href="https://github.com/guicarvalho" target="_blank" style="display: inline-block; padding: 10px 20px; margin: 5px; background-color: #333; color: white; text-align: center; text-decoration: none; border-radius: 5px;">GitHub</a>
