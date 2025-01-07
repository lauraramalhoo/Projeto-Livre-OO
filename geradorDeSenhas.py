import random
import string

class GeradorDeSenha:
    def __init__(self, tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=False):
        self.tamanho = tamanho
        self.usar_maiusculas = usar_maiusculas
        self.usar_minusculas = usar_minusculas
        self.usar_numeros = usar_numeros
        self.usar_simbolos = usar_simbolos

    def _gerar_conjunto_caracteres(self):
        """Método privado que gera o conjunto de caracteres permitidos para a senha."""
        caracteres = ""
        if self.usar_maiusculas:
            caracteres += string.ascii_uppercase
        if self.usar_minusculas:
            caracteres += string.ascii_lowercase
        if self.usar_numeros:
            caracteres += string.digits
        if self.usar_simbolos:
            caracteres += string.punctuation
        
        return caracteres

    def gerar_senha(self):
        """Método público que gera a senha aleatória de acordo com as configurações do objeto."""
        caracteres_permitidos = self._gerar_conjunto_caracteres()
        
        if not caracteres_permitidos:
            raise ValueError("Deve-se permitir pelo menos um tipo de caractere (maiúsculas, minúsculas, números ou símbolos).")
        
        senha = ''.join(random.choice(caracteres_permitidos) for _ in range(self.tamanho))
        return senha


if __name__ == "__main__":
    # Criando um gerador de senhas com tamanho 16 e incluindo símbolos
    gerador = GeradorDeSenha(tamanho=8, usar_simbolos=True)

    senha_gerada = gerador.gerar_senha()
    print(f"Senha gerada: {senha_gerada}")
