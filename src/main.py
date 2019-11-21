#!/usr/bin/python3
from lib.World import World
from lib.world.Entity import Entity

entity1 = Entity();
entity2 = Entity();

print(World.getEntities((0,0)))
entity2.setLocation((0,2))
print(World.getEntities((0,0)))
print(World.getEntities((0,2)))
