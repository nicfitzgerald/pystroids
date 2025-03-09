import pygame

# Base class
class CircleShape(pygame.sprite.Sprite):
  def __init__(self, x, y, radius):
    # we will use this later
    if hasattr(self, "containers"):
      super().__init__(self.containers)
    else:
      super().__init__()

    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 0)
    self.radius = radius

  def draw(self, screen):
    # subclasses must override
    pass

  def update(self, screen):
    # subclasses must override
    pass
