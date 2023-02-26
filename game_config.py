# ---------------- levels configuration ----------------

level_config = """
{   
    "players_stats": {
        "file": "player.gif",
        "hp": 20,
        "gold": 0,
        "alive": true
    },
    "level1": {
        "level_csv": "level1.csv",
        "player_xy": {
            "x":4,
            "y":5
            },
        "monsters": {
            "monster1":{"x":42,"y":30,"file":"monster.gif","hp":10,"gold":0,"alive":true},
            "monster2":{"x":24,"y":22,"file":"imp.gif","hp":5,"gold":0,"alive":true},
            "monster3":{"x":40,"y":12,"file":"mimic.png","hp":5,"gold":0,"alive":true}
            },
        "boxes": {
            "box1":{"text":"BOX", "x":4, "y":17, "z":4},
            "box2":{"text":"BOX", "x":6, "y":3, "z":6},
            "box3":{"text":"BOX", "x":37, "y":29, "z":37}
        },
        "voids": {
            "void1":{"text":"DR", "x":47, "y":13, "z":49},
            "void2":{"text":"DR", "x":19, "y":23, "z":21},
            "void3":{"text":"DR", "x":16, "y":11, "z":18},
            "void4":{"text":"DR", "x":40, "y":37, "z":42}
        },
        "torches": {
            "torch1":{"text":"T", "x":21, "y":5},
            "torch2":{"text":"T", "x":18, "y":25},
            "torch3":{"text":"T", "x":22, "y":25},
            "torch4":{"text":"T", "x":46, "y":30},
            "torch5":{"text":"T", "x":33, "y":13}
        }, 
        "bubbles": {
            "bubble1":{"text":"What?", "x":10, "y":5},
            "bubble2":{"text":"Strange", "x":16, "y":11},
            "bubble3":{"text":"Monsters?", "x":5, "y":21},
            "bubble4":{"text":"Meow!", "x":47, "y":12},
            "bubble5":{"text":"box (ツ)", "x":4, "y":17}
        },
        "chests": {
            "chest1":{"x":18, "y":6, "file":"chest_golden_open_full.png", "visible":true},
            "chest2":{"x":20, "y":25, "file":"chest_golden_open_full.png", "visible":true}
        } 
    }
}
"""

# ---------------- tilset dictionary ----------------

tileset = {
    "@": "https://oshi.at/ZMUu/avRY.gif",
    "W": "https://thumbs2.imgbox.com/10/db/7zaxbIP8_t.png",  # wall
    "FP": "https://thumbs2.imgbox.com/29/22/5rTLr6WH_t.png",  # floor_plain
    # "FP": "https://oshi.at/PQkn/ExtR.png",  # floor 1 tilset 2
    "CAT": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/other/cat.gif",  # cat
    "M": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/other/monster.gif",  # monster, skeleton
    "FS": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_stain_1.png",
    "E": "data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==",
    "FE3": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_edge_3.png",  # floor_edge_3
    "WON": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_n.png",  # Wall_outer_n
    "WOE": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_e.png",  # Wall_outer_e
    "WONE": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_ne.png",  # Wall_outer_ne
    "WOW": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_w.png",  # Wall_outer_w
    "WONW": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_outer_nw.png",  # wall_outer_nw
    "WFR": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Wall_front_right.png",  # wall front right
    "WTR": "https://oshi.at/QpWg/Mfxv.png",  # wall top right
    # "DK": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/wall_missing_brick_2.png",  # darkness
    "WMB": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/wall_missing_brick_2.png",  # wall missing brick 1
    "BOX": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/box.png",  # box
    "DR": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/darkness_right.png",  # darkenss right
    "DB": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/darkness_bottom.png",  # darkness bottom
    "T": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/other/torch.gif",  # torch
    "FMN1": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_mud_n_1.png",  # floor_mud_n_1
    "FMN2": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_mud_n_2.png",  # floor_mud_n_2
    "FMNE": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/floor_mud_ne.png",  # floor_mud_ne
    "CGOF": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/chest_golden_open_full.png",  # chest_golden_open_full
    "CGOO": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/chest_open_empty.png",  # chest_open_empty
    "FL": "https://raw.githubusercontent.com/TomJohnH/streamlit-dungeon/main/graphics/tileset/Floor_ladder.png",  # Floor_ladder
}

tileset_movable = {
    "@": True,
    "W": False,
    "FP": True,  # floor_plain
    # "FP": "https://oshi.at/PQkn/ExtR.png",  # floor 1 tilset 2
    "CAT": True,
    "M": True,  # monster, skeleton
    "FS": True,
    "E": False,
    "FE3": False,  # floor_edge_3
    "WON": False,  # wall outer n
    "WOE": False,  # wall outer e
    "WONE": False,  # wall outer ne
    "WOW": False,  # wall outer w
    "WONW": False,  # wall_outer_nw
    "WFR": False,  # wall front right
    "WTR": False,  # wall top right
    "DK": False,  # darkness
    "WMB": False,  # wall missing brick
    "BOX": False,  # box
    "DR": False,  # darkenss right
    "DB": False,  # darkness bottom
    "T": False,  # torch
    "FMN1": True,  # floor mud n1
    "FMN2": True,
    "FMNE": True,  # floor mud ne
    "FL": True,
}
