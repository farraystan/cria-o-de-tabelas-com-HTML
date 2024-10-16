import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Registro de Dados')

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
ACTIVE_COLOR = (173, 216, 230)  # Azul claro para campo ativo

# Fonte
font = pygame.font.Font(None, 36)

# Função para escrever dados no arquivo
def salvar_dados(nome, email):
    with open('dados.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{email}\n')

# Variáveis para armazenar dados
nome = ''
email = ''
input_active = False
email_active = False

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    email_active = True
                elif event.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                else:
                    nome += event.unicode

            if email_active:
                if event.key == pygame.K_RETURN:
                    salvar_dados(nome, email)
                    nome = ''
                    email = ''
                    input_active = False
                    email_active = False
                elif event.key == pygame.K_BACKSPACE:
                    email = email[:-1]
                else:
                    email += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if 20 <= mouse_y <= 80:  # Área do nome
                input_active = True
                email_active = False
            elif 90 <= mouse_y <= 150:  # Área do e-mail
                email_active = True
                input_active = False

    # Preenche a tela
    screen.fill(WHITE)

    # Desenha campos de entrada
    if input_active:
        pygame.draw.rect(screen, ACTIVE_COLOR, (20, 50, 360, 40), 0)  # Campo Nome ativo
    else:
        pygame.draw.rect(screen, GRAY, (20, 50, 360, 40), 0)  # Campo Nome inativo

    if email_active:
        pygame.draw.rect(screen, ACTIVE_COLOR, (20, 100, 360, 40), 0)  # Campo Email ativo
    else:
        pygame.draw.rect(screen, GRAY, (20, 100, 360, 40), 0)  # Campo Email inativo

    # Desenha textos
    name_text = font.render("Nome: " + nome, True, BLACK)
    email_text = font.render("Email: " + email, True, BLACK)

    screen.blit(name_text, (25, 55))
    screen.blit(email_text, (25, 105))

    # Instruções
    instruction_text = font.render("Clique no campo para digitar", True, BLACK)
    register_text = font.render("Pressione Enter para registrar", True, BLACK)
    screen.blit(instruction_text, (20, 150))
    screen.blit(register_text, (20, 200))

    # Atualiza a tela
    pygame.display.flip()
