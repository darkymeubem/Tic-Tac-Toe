from controllers.Match import Match

def main():
    """Ponto de entrada para o jogo Tic-Tac-Toe."""
    print("Iniciando o Jogo da Velha...")  # Mensagem de inicialização

    try:
        match = Match()
        match.play()
    except KeyboardInterrupt:
        print("\nJogo interrompido pelo usuário. Até a próxima!")  # Mensagem mais específica
    except EOFError:  # Lida com Ctrl+D (fim de arquivo)
        print("\nEntrada encerrada. Jogo finalizado.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado durante a execução do jogo:")
        print(f"{type(e).__name__}: {e}") # Imprime o tipo do erro e a mensagem
        # (Opcional) Para depuração em desenvolvimento:
        # import traceback
        # traceback.print_exc() # Imprime o traceback completo

    print("Encerrando o Jogo da Velha.") # Mensagem de encerramento

if __name__ == "__main__":
    main()