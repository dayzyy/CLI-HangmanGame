from models import Game

Game.set_word()

while(1):
    if Game.lost() or Game.won():
        Game.display()
        exit()

    Game.display()
    Game.play()
