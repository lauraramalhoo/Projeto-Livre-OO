import pygame
import random

# tela do jogo
LARGURA_TELA = 640
ALTURA_TELA = 480
TAMANHO_CELULA = 20
FPS = 15

# cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (213, 50, 80)
AZUL = (50, 153, 213)
AMARELO = (255, 255, 102)

# Classe da cobrinha
class Cobra:
    def __init__(self):
        self.corpo = [(100, 100), (80, 100), (60, 100)]  
        self.direcao = (TAMANHO_CELULA, 0)  
        self.vivo = True

    def mover(self):
        # Move a cobra 
        cabeça = self.corpo[0]
        nova_cabeça = (cabeça[0] + self.direcao[0], cabeça[1] + self.direcao[1])
        self.corpo = [nova_cabeça] + self.corpo[:-1]

    def crescer(self):
        # Adiciona uma nova célula a cobra
        cabeça = self.corpo[0]
        nova_cabeça = (cabeça[0] + self.direcao[0], cabeça[1] + self.direcao[1])
        self.corpo = [nova_cabeça] + self.corpo

    def colidiu_com_parede(self):
        cabeça = self.corpo[0]
        return cabeça[0] < 0 or cabeça[0] >= LARGURA_TELA or cabeça[1] < 0 or cabeça[1] >= ALTURA_TELA

    def colidiu_com_o_corpo(self):
        cabeça = self.corpo[0]
        return cabeça in self.corpo[1:]

# comida
class Comida:
    def __init__(self):
        self.posicao = (0, 0)
        self.nova_posicao()

    def nova_posicao(self):
        self.posicao = (random.randrange(1, (LARGURA_TELA // TAMANHO_CELULA)) * TAMANHO_CELULA,
                       random.randrange(1, (ALTURA_TELA // TAMANHO_CELULA)) * TAMANHO_CELULA)

# Classe do jogo
class JogoCobrinha:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.clock = pygame.time.Clock()
        self.cobra = Cobra()
        self.comida = Comida()
        self.pontos = 0
        self.jogo_rodando = True

    def desenhar(self):
        # Preencher a tela de fundo
        self.tela.fill(AZUL)

        # desenho cobra
        for segmento in self.cobra.corpo:
            pygame.draw.rect(self.tela, VERDE, pygame.Rect(segmento[0], segmento[1], TAMANHO_CELULA, TAMANHO_CELULA))

        # desenho comida
        pygame.draw.rect(self.tela, AMARELO, pygame.Rect(self.comida.posicao[0], self.comida.posicao[1], TAMANHO_CELULA, TAMANHO_CELULA))

        # pontos
        fonte = pygame.font.SysFont("arial", 24)
        texto = fonte.render(f"Pontos: {self.pontos}", True, BRANCO)
        self.tela.blit(texto, [10, 10])

        # atualiza tela
        pygame.display.update()

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.jogo_rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and self.cobra.direcao != (0, TAMANHO_CELULA):
                    self.cobra.direcao = (0, -TAMANHO_CELULA)
                elif evento.key == pygame.K_DOWN and self.cobra.direcao != (0, -TAMANHO_CELULA):
                    self.cobra.direcao = (0, TAMANHO_CELULA)
                elif evento.key == pygame.K_LEFT and self.cobra.direcao != (TAMANHO_CELULA, 0):
                    self.cobra.direcao = (-TAMANHO_CELULA, 0)
                elif evento.key == pygame.K_RIGHT and self.cobra.direcao != (-TAMANHO_CELULA, 0):
                    self.cobra.direcao = (TAMANHO_CELULA, 0)

    def checar_colisoes(self):
        if self.cobra.colidiu_com_parede() or self.cobra.colidiu_com_o_corpo():
            self.jogo_rodando = False

    def checar_comida(self):
        if self.cobra.corpo[0] == self.comida.posicao:
            self.pontos += 1
            self.cobra.crescer()
            self.comida.nova_posicao()

    def iniciar(self):
        while self.jogo_rodando:
            self.processar_eventos()
            self.cobra.mover()
            self.checar_colisoes()
            self.checar_comida()
            self.desenhar()
            self.clock.tick(FPS)

        # mensagem de fim
        fonte = pygame.font.SysFont("arial", 48)
        texto = fonte.render(f"Perdeu! Pontos: {self.pontos}", True, VERMELHO)
        self.tela.blit(texto, [LARGURA_TELA // 6, ALTURA_TELA // 3])
        pygame.display.update()
        pygame.time.wait(3000)  # espera 3 segundos p/ fechar
        pygame.quit()

if __name__ == "__main__":
    jogo = JogoCobrinha()
    jogo.iniciar()
