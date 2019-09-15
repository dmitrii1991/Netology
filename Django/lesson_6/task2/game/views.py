from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo
from .forms import Form_For_Number
import random

def show_home(request):
    id = random.randint(1, 100000)
    player_session = request.session.get('player_id')
    game_session = request.session.get('game_id')
    if player_session and game_session:
        game = Game.objects.get(game_id=request.session.get('game_id'))
        if game.playing:
            new_game = Game.objects.create(game_id=random.randint(1, 100000), number=random.randint(1, 10), playing=False)
            player = Player.objects.get(player_id=player_session)
            PlayerGameInfo.objects.create(player=player, game=new_game, lifes=0, author=True)
            request.session['game_id'] = str(new_game.game_id)
        else:
            game = Game.objects.get(playing=False)
            exists_player = Player.objects.get(player_id=player_session)
            game.players.add(exists_player,through_defaults={'lifes': 0, 'author': False})
            request.session['game_id'] = str(game.game_id)
    else:
        if Game.objects.filter(playing=False).count() == 0:
            new_game = Game.objects.create(game_id=random.randint(1, 100000), number=random.randint(1, 10), playing=False)
            new_player = Player.objects.create(player_id=f'{id}')
            PlayerGameInfo.objects.create(player=new_player, game=new_game, lifes=0, author=True)
            request.session['game_id'] = str(new_game.game_id)
            request.session['player_id'] = str(new_player.player_id)
        else:
            game = Game.objects.get(playing=False)
            new_player = Player.objects.create(player_id=f'{id}')
            game.players.add(new_player, through_defaults={'lifes': 0, 'author': False})
            request.session['game_id'] = str(game.game_id)
            request.session['player_id'] = str(new_player.player_id)

    game = Game.objects.get(game_id=request.session.get('game_id'))
    current_player = Player.objects.get(player_id=request.session.get('player_id'))
    counter = PlayerGameInfo.objects.filter(game_id=game).get(player_id=current_player)
    form = Form_For_Number(request.POST or None)
    context = {}

    if form.is_valid():
        answer = int(request.POST.get('number'))
        if answer == game.number:
            game.playing = True
            game.save()
            context['text'] = f'Вы угадали число! c {counter.lifes} попыток'
        elif answer < game.number:
            context['text'] = f'Загаданное число больше числа {answer}'
        elif answer > game.number:
            context['text'] = f'Загаданное число меньше числа {answer}'
        counter.lifes += 1
        counter.save()
        context['form'] = form
        return render(request, 'home.html', context)
    else:
        context['form'] = form
        return render(request, 'home.html', context)