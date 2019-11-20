#!/usr/bin/python3
from lib.World import World
from lib.world.Entity import Entity


print("Hello World")
print(id(World.locations))

entity = Entity()
World.locations[1] = entity
print(World.locations.inverse[entity])
print(id(entity))
print(id(World.locations[1]))