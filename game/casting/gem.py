from game.casting.artifact import Artifact

class Gem(Artifact):
    # A gem is an artifact that will increase the player's score when collected.
    def __init__(self):
        super().__init__()
        self._point_value = 1