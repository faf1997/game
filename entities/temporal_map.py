
from entities.floor import Dirt
from entities.player import Player
from entities.utils import get_path
from entities.box import BoxWood
import os

path = "./imgs/"
DICT_TEXTURES = {
    "d0":"dirt_0_0.png",
    "d1":"dirt_0_1.png",
    "d2":"dirt_0_2.png",
    "d3":"dirt_1_0.png",
    "d4":"dirt_1_1.png",
    "d5":"dirt_1_2.png",
    "d6":"dirt_2_4.png"
    }   

def temporal_map(group,screen):
    map1 =[
        [" "," "," ","p"," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," ","bw"," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" ","d0","d1","d1","d1","d2"," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "]
    ]
        # [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","p"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",],
        # ["d0","d1","d1","d1","d1","d1","d1","d1","d1","d1","d1","d1","d1","d2"," "," ","d0","d1","d1","d1","d1","d1","d1","d1","d1","d1","d1","d1","d1","d2"],
        # ["d3","d4","d4","d4","d4","d4","d4","d4","d4","d4","d4","d4","d4","d5", " "," ","d3","d4","d4","d4","d4","d4","d4","d4","d4","d4","d4","d4","d4","d5"]
        # ]
    map1.reverse()
    pos_y = screen.get_height()
    for y in range(len(map1)):
        pos_y -= 16
        for x, elem  in enumerate(map1[y]):
            pos_tile = (x*16,pos_y)
            if elem in [" ", ""]:
                continue
            if elem == "p":
                group.add(Player(pos_tile))
                continue
            if elem == "bw":
                group.add(BoxWood(pos_tile))
                continue
            group.add(Dirt(pos_tile,os.path.abspath(f'{path}{DICT_TEXTURES[elem]}')))

            #f"{get_path()}./imgs/joystick.png"