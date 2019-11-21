#!/usr/bin/python3
from lib.World import World
from lib.world.Entity import Entity

entity1 = Entity();
entity2 = Entity();

print(World.locations)
entity1.setLocation((0,2))
print(World.locations)
