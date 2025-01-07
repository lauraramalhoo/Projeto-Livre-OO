# Projeto-Livre-OO

# 🐍 **Jogo da Cobrinha - Python** 🐍

Esse é o **Jogo da Cobrinha**! Um um dos meus jogos preferidos de infância recriado com Python e Pygame. Controla-se uma cobrinha para que ela coma aa comida (quadrado amarelo) para crescer e ganhar pontos. Se a cobrinha bater nas paredes ou nela mesma, o jogo acaba.

## 🎮 **Objetivo do Jogo**

O objetivo é simples: controle a cobra e faça ela comer a comida (quadrado amarelo) para crescer. Cada pedaço de comida comido aumenta a pontuação e o tamanho da cobra, mas também aumenta a dificuldade, pois a cobra vai ficando maior. O jogo termina quando a cobra bate na parede ou em seu próprio corpo.

## 🕹️ **Como Jogar**

1. **Movimentação**: Use as setas do teclado para mover a cobra.
   - **Seta para cima**: move a cobra para cima.
   - **Seta para baixo**: move a cobra para baixo.
   - **Seta para esquerda**: move a cobra para a esquerda.
   - **Seta para direita**: move a cobra para a direita.

2. **Coma a comida**: A cobra cresce e a pontuação aumenta cada vez que ela come a comida (quadrado amarelo).

3. **Evite as colisões**: Não bata nas paredes ou em você mesma, caso contrário, você perderá o jogo.

4. **Objetivo**: Tentar alcançar a maior pontuação possível. 

## 💻 **Requisitos**

Para rodar o jogo, você precisará do **Python** e do **Pygame** instalados em seu sistema:


### Instalação do Pygame

Caso não tenha o Pygame instalado, você pode instalar facilmente usando o pip:

```bash
pip install pygame
```
-----

# 🔐 **Gerador de Senha Aleatória - Python** 🔐

Esse é o **Gerador de Senha Aleatória**! Um projeto simples, mas poderoso, para ajudar a criar senhas seguras e difíceis de adivinhar. 🔑

Este gerador permite que você configure o comprimento da senha e escolha se deseja incluir maiúsculas, minúsculas, números e até mesmo símbolos. 💻



## 🎯 **Objetivo**

O objetivo deste projeto é fornecer uma maneira simples e flexível de gerar senhas fortes. Com tantas contas online hoje em dia, é fundamental usar senhas únicas e seguras. Com ele, você pode criar senhas que atendem às suas necessidades de segurança, seja para uma conta de e-mail, redes sociais, ou até mesmo para seus sistemas internos.



## 🚀 **Como Usar**

1. **Instale o Python**: 
   
2. **Configuração do Gerador**:
   - **Tamanho da Senha**: Defina o tamanho desejado para a senha gerada. O padrão é 8 caracteres, mas você pode ajustar conforme necessário.
   - **Opções de Caracteres**:
     - **Maiúsculas**: Ative para incluir letras maiúsculas.
     - **Minúsculas**: Ative para incluir letras minúsculas.
     - **Números**: Ative para incluir números.
     - **Símbolos**: Ative para incluir símbolos especiais (como `@`, `#`, `!`).

3. **Execute o Código**: Execute o script Python para gerar sua senha personalizada e segura.

### Exemplo de código para rodar:
```python
from gerador_de_senha import GeradorDeSenha

# Criando um gerador de senhas com tamanho 12 e incluindo símbolos
gerador = GeradorDeSenha(tamanho=16, usar_simbolos=True, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True)

# Gerando a senha
senha_gerada = gerador.gerar_senha()

# Exibindo a senha gerada
print(f"Senha gerada: {senha_gerada}")
