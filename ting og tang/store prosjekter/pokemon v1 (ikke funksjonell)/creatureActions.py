#nye klasser
class playerCreatureActions:
    def __init__(self):
        pass

    #Moves

    def tackle(self):
        from main import enemy
        from main import player
        enemy.hp = enemy.hp - player.atck
        print(enemy.hp)