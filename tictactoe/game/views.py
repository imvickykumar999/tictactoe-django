from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Game
from django.core.exceptions import ObjectDoesNotExist

def game_view(request, game_id):
    game, created = Game.objects.get_or_create(game_id=game_id)
    context = {
        'game_id': game_id,
        'range': range(9),
        'board': game.board,
        'winner': game.winner,
    }
    return render(request, 'game/game.html', context)

def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    return None

def play_move(request, game_id, index):
    if request.method == 'POST':
        game = get_object_or_404(Game, game_id=game_id)
        board = list(game.board)
        if board[index] == ' ' and game.winner is None:
            board[index] = game.next_move
            game.board = ''.join(board)
            game.next_move = 'O' if game.next_move == 'X' else 'X'
            game.winner = check_winner(board)
            game.save()
            return JsonResponse({
                'board': game.board,
                'next_move': game.next_move,
                'winner': game.winner
            })
    return JsonResponse({'error': 'Invalid move'}, status=400)

def reset_game(request, game_id):
    game = get_object_or_404(Game, game_id=game_id)
    game.board = ' ' * 9
    game.next_move = 'X'
    game.winner = None
    game.save()
    return redirect('home')
