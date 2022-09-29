import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants


class PlayingGameScene(Scene):
    """Class, rendering a main scene for playing the game."""

    def __init__(self, game: 'Breakout'):
        super().__init__(game)

    def render(self) -> None:
        """
        Method for rendering this scene.
        Setting pad and balls, handling hits, updating positions.
        """
        super().render()
        game = self.getGame
        pad = game.getPad
        pad.setPosition = (pygame.mouse.get_pos()[0], pad.position[1])
        balls = game.getBalls

        if game.getLives <= 0:
            game.changeScene(GameConstants.GAMOVER_SCENE)
            game.playSound(GameConstants.SOUND_GAMEOVER)

        # Stopping balls and loading next level if all bricks are destroyed.
        if game.getLevel.getAmountOfBricksLeft <= 0:
            for ball in balls:
                ball.setMotion(False)
            game.getLevel.loadNextLevel()

        #Handling intersections
        for ball in balls:
            for ball2 in balls:
                if ball != ball2 and ball.intersects(ball2):
                    ball.changeDirection(ball2)

            #Handling hitting bricks
            for brick in game.getLevel.getBricks:
                if not brick.isDestroyed() and ball.intersects(brick):
                    brick.hit()
                    game.getLevel.brickHit()
                    game.playSound(brick.getHitSound)
                    ball.changeDirection(brick)
                    game.increaseScore(brick.getHitPoints)
                    break

            #handling hitting pad
            if ball.intersects(pad):
                ball.changeDirection(pad)
                game.playSound(GameConstants.SOUND_PAD_BOUNCE)

            ball.updatePosition()
            if ball.isDead:
                ball.setMotion(False)
                game.reduceLives()
            game.screen.blit(ball.getSprite, ball.position)

        pad.updatePosition()
        game.screen.blit(pad.getSprite, pad.position)

        #Rendering bricks
        for brick in game.getLevel.getBricks:
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite, brick.position)

        self.clearText()

        self.addText("Your score: " + str(game.getScore), x=0, y=GameConstants.SCREEN_SIZE[1] - 60, size=30)
        self.addText("Your lives: " + str(game.getLives), x=0, y=GameConstants.SCREEN_SIZE[1] - 30, size=30)

    def handleEvents(self, events) -> None:
        """
        Getting balls into motion
        :param events: various pygame events
        """
        super().handleEvents(events)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.getGame.getBalls:
                    ball.setMotion(True)