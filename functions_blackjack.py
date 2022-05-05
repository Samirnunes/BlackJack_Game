from classes_blackjack import deck, player, dealer
playing = False
total_chips = 0
bet = 0

Deck = deck()
player_hand = player()
dealer_hand = dealer()

def get_total_chips():
    global total_chips
    is_int = False
    while(is_int == False):
        try:
            total_chips = int(input('Quantas fichas irá disponibilizar para aposta? Digite um valor inteiro (positivo = negativo): '))
        except:
            print('O valor digitado não é inteiro. Digite novamente.')
        else:
            is_int = True

def show_cards_and_points():
    global player_hand, dealer_hand
    print("\nO jogador possui as cartas:")
    player_hand.print_hand_cards()
    
    print(f"A pontuação total do jogador é: {player_hand.shown_play_value()}")

    print("\nO dealer possui as cartas:")
    dealer_hand.print_hand_cards()

    print(f"A pontuação total do dealer é: {dealer_hand.shown_play_value()}")

def quit_game():
    global playing, total_chips
    print('\nObrigado por jogar!')
    print(f'\nSua quantidade final de fichas foi: {total_chips}')
    playing = False

def player_action():
    action_options = ['h', 's', 'q']
    action = input('\nHit, Stand ou Quit (Sair do jogo)? Digite h, s ou q: ').lower()
    while not (action in action_options):
        action = input('Ação inválida. Digite novamente (h, s ou q): ').lower()
    if action == 'h':
        hit()
    elif action == 's':
        stand()
    elif action == 'q':
        quit_game()

def get_bet():
    is_int = False
    while(is_int == False):
        try:
            bet_value = int(input('Quantas fichas deseja apostar? Digite um valor inteiro (positivo = negativo): '))
        except:
            print('O valor digitado não é inteiro. Digite novamente.')
        else:
            is_int = True
    return abs(bet_value)

def make_bet():
    global playing, total_chips, bet
    if total_chips == 0:
        print('\nNão há mais fichas disponíveis. Saindo do jogo...')
        quit_game()
    if playing:
        print(f'\n## Você possui {total_chips} fichas ##\n')
        bet = get_bet()
        if bet == 0:
            print("\nVocê está jogando no modo de treino, pois sua aposta foi nula.")
        while bet > total_chips:
            print(f'\nNão há fichas suficientes para a aposta. Você possui {total_chips} fichas. Selecione outro valor.')
            bet = get_bet()

def deal_cards():
    global playing, Deck, player_hand, dealer_hand, chip_pool, bet

    playing = True

    Deck.shuffle()

    make_bet()

    if playing:
        player_hand.draw(Deck.remove_card())
        player_hand.draw(Deck.remove_card())

        dealer_hand.draw(Deck.remove_card())
        dealer_hand.draw(Deck.remove_card())
    
        begin_turn()

def reset_hands_and_deck():
    global player_hand, dealer_hand, Deck

    player_hand = player()
    dealer_hand = dealer()
    if len(Deck.cards) <= 4:
        Deck = deck()
        print("O deck foi reposto por falta de cartas.")

def begin_turn():
    if playing:
        show_cards_and_points()
        player_action()
    else:
        reset_hands_and_deck()
        deal_cards()

def stand():
    global playing, total_chips, bet, Deck, player_hand, dealer_hand

    while dealer_hand.get_hard_value() < 17:
        dealer_hand.draw(Deck.remove_card())

    print(f"\nCartas finais do dealer:")
    dealer_hand.print_hand_cards()
    print(f"\nPontuação final do dealer: {dealer_hand.play_value()}")
    
    if dealer_hand.play_value() > 21:
        print(f"O dealer passou de 21! Você ganhou {bet} fichas!")
        total_chips += bet
        playing = False    

    elif dealer_hand.play_value() < player_hand.play_value():
        print(f"Você venceu do dealer! Você ganhou {bet} fichas!")
        total_chips += bet
        playing = False
    
    elif dealer_hand.play_value() == player_hand.play_value():
        print("Empate! Seu número de fichas permanece o mesmo.")
        playing = False

    else:
        print(f"O dealer venceu! Você perdeu {bet} fichas.")
        total_chips -= bet
        playing = False

    begin_turn()
        
def hit():
    global playing, total_chips, bet, Deck, player_hand, dealer_hand
    player_hand.draw(Deck.remove_card())
    if player_hand.play_value() > 21:
        print(f"\nPontuação final do jogador: {player_hand.play_value()}")
        print(f"Passou de 21! Perdeu {bet} fichas.")
        total_chips -= bet
        playing = False
    begin_turn()

def begin_game():
    global total_chips
    intro = '''    Bem-vindo ao BlackJack! Chegue o mais perto possível de 21 sem perder para o dealer!                        
    O dealer compra até chegar em 17 pontos ou mais, sem passar de 21, e a primeira carta do dealer é escondida! 
    Um ás conta como 1 ou 11.                                                                                    
    Cartas são representadas por meio de uma letra (seu naipe) e de um número ou letra (seu rank).
    Naipes: s = Espadas ; c = Paus ; h = Copas; d = Ouros;
    Ranks: A = Ás; Q = Rainha; K = Rei ; J = Valete
    Para mais informações sobre o jogo, acesse: https://pt.wikipedia.org/wiki/Blackjack\n'''
    print(intro)
    get_total_chips()
    deal_cards()