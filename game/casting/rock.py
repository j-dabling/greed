from game.casting.artifact import Artifact

class Rock(Artifact):
    # A rock is an artifact that will damage the player's score and ship.
    def __init__(self):
        super().__init__()
        self._point_value = -1
    
    