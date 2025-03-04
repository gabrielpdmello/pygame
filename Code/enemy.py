#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT, ENTITY_SHOT_DELAY
from Code.enemyShot import EnemyShot
from Code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, axis = False):
        self.rect.centery += ENTITY_SPEED[self.name]

    def shoot(self):
        return EnemyShot(name=f'Shots/enemy_shot_normal', position=(self.rect.centerx, self.rect.centery))

