#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_speed = ENTITY_SPEED[self.name]  # Velocidade vertical inicial

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.name == 'Enemy3':
            self.rect.centery += self.vertical_speed
            if self.rect.top <= 0:
                self.vertical_speed = abs(self.vertical_speed) * 2  # Dobra a velocidade ao bater no topo
            elif self.rect.bottom >= self.rect.height:
                self.vertical_speed = -abs(self.vertical_speed)  # Inverte a direção ao bater na parte inferior

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
