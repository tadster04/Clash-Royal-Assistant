from email.mime import image


allCards = {
    "temp" : {
        "name" : "temp",
        "elixer" : 0,
        "image" : "./card_images/unknown-card.png"

    },
    "aq" :{
        "name" : "ARCHER QUEEN",
        "elixer" : 5,
        "image" : "./card_images/archer-queen.png"
    },
    "ar" :{
        "name" : "ARCHERS",
        "elixer" : 3,
        "image" : "./card_images/archers.png"
    },
    "a" :{
        "name" : "ARROWS",
        "elixer" : 3,
        "image" : "./card_images/arrows.png"
    },
    "ban":{
        "name" : "BANDIT",
        "elixer" : 3,
        "image" : "./card_images/bandit.png"
    },
    "bd" :{
        "name" : "BABY DRAGON",
        "elixer" : 4,
        "image" : "./card_images/baby-dragon.png"
    },
    "ba" :{
        "name" : "BALLOON",
        "elixer" : 5,
        "image" : "./card_images/balloon.png"
    },
    "br": {
        "name" : "BATTLE RAM",
        "elixer" : 4,
        "image" : "./card_images/battle-ram.png"
    },
    "bb" :{
        "name" : "BARBARIAN BARREL",
        "elixer" : 2,
        "image" : "./card_images/barbarian-barrel.png"
    },
    "bhut" :{
        "name" : "BARBARION HUT",
        "elixer" : 7,
        "image" : "./card_images/barbarian-hut.png"
    },
    "bar" :{
        "name" : "BARBARIANS",
        "elixer" : 5,
        "image" : "./card_images/barbarians.png"
    },
    "bat" :{
        "name" : "BATS",
        "elixer" : 2,
        "image" : "./card_images/bats.png"
    },
    "bh" :{
        "name" : "BATTLE HEALER",
        "elixer" : 4,
        "image" : "./card_images/battle-healer.png"
    },
    "bt" :{
        "name" : "BOMB TOWER",
        "elixer" : 4,
        "image" : "./card_images/bomb-tower.png"
    },
    "bo" :{
        "name" : "BOMBER",
        "elixer" : 2,
        "image" : "./card_images/bomber.png"
    },
    "bow" :{
        "name" : "BOWLER",
        "elixer" : 5,
        "image" : "./card_images/bowler.png"
    },
    "cc" :{
        "name" : "CANNON CART",
        "elixer" : 5,
        "image" : "./card_images/cannon-cart.png"
    },
    "ca": {
        "name" : "CANNON",
        "elixer" : 3,
        "image" : "./card_images/cannon.png"
    },
    "c" :{
        "name" : "CLONE",
        "elixer" : 3,
        "image" : "./card_images/clone.png"
    },
    "dp" :{
        "name" : "DARK PRINCE",
        "elixer" : 4,
        "image" : "./card_images/dark-prince.png"
    },
    "dg" :{
        "name" : "DART GOBLING",
        "elixer" : 3,
        "image" : "./card_images/dart-goblin.png"
    },
    "ew" : {
        "name" : "ELECTRO WIZZARD",
        "elixer" : 4,
        "image" : "./card_images/electro-wizard.png"
    },
    "e" :{
        "name" : "EARTHQUAKE",
        "elixer" : 3,
        "image" : "./card_images/earthquake.png"
    },
    "ed" :{
        "name" : "ELECTRO DARGON",
        "elixer" : 5,
        "image" : "./card_images/electro-dragon.png"
    },
    "eg" :{
        "name" : "ELECTRO GIANT",
        "elixer" : 7,
        "image" : "./card_images/electro-giant.png"
    },
    "es" :{
        "name" : "ELECTRO SPIRIT",
        "elixer" : 1,
        "image" : "./card_images/electro-spirit.png"
    },
    "eb" :{
        "name" : "ELITE BARBARIANS",
        "elixer" : 6,
        "image" : "./card_images/elite-barbarians.png"
    },
    "ec" :{
        "name" : "ELIXER COLLECTOR",
        "elixer" : 6,
        "image" : "./card_images/elixer-collector.png"
    },
    #costs 3 but gives 4 when it dies
    "ego" :{
        "name" : "ELIXER GOLEM",
        "elixer" : 7,
        "image" : "./card_images/elixer-golem.png"
    },
    "ex" :{
        "name" : "EXECUTIONER",
        "elixer" : 5,
        "image" : "./card_images/executioner.png"
    },
    "fs" :{
        "name" : "FIRE SPIRIT",
        "elixer" : 1,
        "image" : "./card_images/fire-spirit.png"
    },
    "f" :{
        "name" : "FIREBALL",
        "elixer" : 4,
        "image" : "./card_images/fireball.png"
    },
    "fc" :{
        "name" : "FIRECRACKER",
        "elixer" : 3,
        "image" : "./card_images/firecracker.png"
    },
    "fi" :{
        "name" : "FISHERMAN",
        "elixer" : 3,
        "image" : "./card_images/fisherman.png"
    },
    "fm" :{
        "name" : "FLYING MACHINE",
        "elixer" : 4,
        "image" : "./card_images/flying-machine.png"
    },
    "fr" :{
        "name" : "FREEZE",
        "elixer" : 4,
        "image" : "./card_images/freeze.png"
    },
    "fu" :{
        "name" : "FURNACE",
        "elixer" : 4,
        "image" : "./card_images/furnace.png"
    },
    "gs" :{
        "name" : "GIANT SKELETON",
        "elixer" : 6,
        "image" : "./card_images/giant-skeleton.png"
    },
    "s" :{
        "name" : "GIANT SNOWBALL",
        "elixer" : 2,
        "image" : "./card_images/giant-snowball.png"
    },
    "gi" :{
        "name" : "GIANT",
        "elixer" : 5,
        "image" : "./card_images/giant.png"
    },
    "gb" :{
        "name" : "GOBLIN BARREL",
        "elixer" : 3,
        "image" : "./card_images/goblin-barrel.png"
    },
    "gc" :{
        "name" : "GOBLIN CAGE",
        "elixer" : 4,
        "image" : "./card_images/goblin-cage.png"
    },
    "gd" :{
        "name" : "GOBLIN DRILL",
        "elixer" : 4,
        "image" : "./card_images/goblin-drill.png"
    },
    "gg" :{
        "name" : "GOBLIN GANG",
        "elixer" : 3,
        "image" : "./card_images/goblin-gang.png"
    },
    "ggi" :{
        "name" : "GOBLIN GIANT",
        "elixer" : 6,
        "image" : "./card_images/goblin-giant.png"
    },
    "gh" :{
        "name" : "GOBLIN HUT",
        "elixer" : 5,
        "image" : "./card_images/poison.png"
    },
    "gk" :{
        "name" : "GOLDEN KNIGHT",
        "elixer" : 4,
        "image" : "./card_images/golden_knight.png"
    },
    "go" :{
        "name" : "GOLEM",
        "elixer" : 8,
        "image" : "./card_images/golem.png"
    },
    "gr" :{
        "name" : "GRAVEYARD",
        "elixer" : 4,
        "image" : "./card_images/graveyard.png"
    },
    "gu" :{
        "name" : "GUARDS",
        "elixer" : 3,
        "image" : "./card_images/guards.png"
    },
    "hs" :{
        "name" : "HEAL SPIRIT",
        "elixer" : 1,
        "image" : "./card_images/heal-spirit.png"
    },
    "h" :{
        "name" : "HEAL",
        "elixer" : 2,
        "image" : "./card_images/heal.png"
    },
    "hr" :{
        "name" : "HOG RIDER",
        "elixer" : 4,
        "image" : "./card_images/hog-rider.png"
    },
    "hu" :{
        "name" : "HUNTER",
        "elixer" : 4,
        "image" : "./card_images/hunter.png"
    },
    "ig" :{
        "name" : "ICE GOLEM",
        "elixer" : 2,
        "image" : "./card_images/ice-golem.png"
    },
    "is" :{
        "name" : "ICE SPIRIT",
        "elixer" : 1,
        "image" : "./card_images/ice-spirit.png"
    },
    "iw" :{
        "name" : "ICE WIZARD",
        "elixer" : 3,
        "image" : "./card_images/ice-wizard.png"
    },
    "id" :{
        "name" : "INFERNO DRAGON",
        "elixer" : 4,
        "image" : "./card_images/inferno-dragon.png"
    },
    "it" :{
        "name" : "INFERNO TOWER",
        "elixer" : 5,
        "image" : "./card_images/inferno-tower.png"
    },
    "kn" :{
        "name" : "KNIGHT",
        "elixer" : 3,
        "image" : "./card_images/knight.png"
    },
    "lh" :{
        "name" : "LAVA HOUND",
        "elixer" : 7,
        "image" : "./card_images/lava-hound.png"
    },
    "li" :{
        "name" : "LIGHTNING",
        "elixer" : 6,
        "image" : "./card_images/lightning.png"
    },
    "lu" :{
        "name" : "LUMBERJACK",
        "elixer" : 4,
        "image" : "./card_images/lumberjack.png"
    },
    "ma" : {
        "name" : "MAGIC ARCHER",
        "elixer" : 4,
        "image" : "./card_images/magic-archer.png"
    },
    "mk" :{
        "name" : "MEGA KNIGHT",
        "elixer" : 7,
        "image" : "./card_images/mega-knight.png"
    },
    "mm" :{
        "name" : "MEGA MINION",
        "elixer" : 3,
        "image" : "./card_images/mega-minion.png"
    },
    "mmi" :{
        "name" : "MIGHTY MINER",
        "elixer" : 4,
        "image" : "./card_images/mighty-miner.png"
    },
    "mi" :{
        "name" : "MINER",
        "elixer" : 3,
        "image" : "./card_images/miner.png"
    },
    "mp" :{
        "name" : "MINI PEKKA",
        "elixer" : 4,
        "image" : "./card_images/mini-pekka.png"
    },
    "mh" :{
        "name" : "MINION HORDE",
        "elixer" : 5,
        "image" : "./card_images/minion-horde.png"
    },
    "min" :{
        "name" : "MINIONS",
        "elixer" : 3,
        "image" : "./card_images/minions.png"
    },
    "mir" :{
        "name" : "MIRROR",
        "elixer" : 5,
        "image" : "./card_images/mirror.png"
    },
    "mo" :{
        "name" : "MORTAR",
        "elixer" : 4,
        "image" : "./card_images/mortar.png"
    },
    "mw" :{
        "name" : "MOTHER WITCH",
        "elixer" : 4,
        "image" : "./card_images/mother-witch.png"
    },
    "mu" :{
        "name" : "MUSKETEER",
        "elixer" : 4,
        "image" : "./card_images/musketeer.png"
    },
    "nw" :{
        "name" : "NIGHT WITCH",
        "elixer" : 4,
        "image" : "./card_images/night-witch.png"
    },
    "pe": {
        "name" : "PEKKA",
        "elixer" : 7,
        "image" : "./card_images/pekka.png"
    },
    "pr" :{
        "name" : "PRINCE",
        "elixer" : 5,
        "image" : "./card_images/prince.png"
    },
    "p" :{
        "name" : "POISON",
        "elixer" : 4,
        "image" : "./card_images/poison.png"
    },
    "prs" : {
        "name": "PRINCESS",
        "elixer": 3,
        "image": "./card_images/princess.png"
    },
    "rag" :{
        "name" : "RAGE",
        "elixer" : 2,
        "image" : "./card_images/rage.png"
    },
    "rr" :{
        "name" : "RAM RIDER",
        "elixer" : 5,
        "image" : "./card_images/ram-rider.png"
    },
    "ra" :{
        "name" : "RASCALS",
        "elixer" : 5,
        "image" : "./card_images/rascals.png"
    },
    "r" :{
        "name" : "ROCKET",
        "elixer" : 6,
        "image" : "./card_images/rocket.png"
    },
    "rd" :{
        "name" : "ROYAL DELIVERY",
        "elixer" : 3,
        "image" : "./card_images/royal-delivery.png"
    },
    "rg" :{
        "name" : "ROYAL GIANT",
        "elixer" : 6,
        "image" : "./card_images/royal-giant.png"
    },
    "gh": {
        "name" : "ROYAL GHOST",
        "elixer" : 3,
        "image" : "./card_images/royal-ghost.png"
    },
    "rh" :{
        "name" : "ROYAL HOGS",
        "elixer" : 5,
        "image" : "./card_images/royal-hogs.png"
    },
    "re" :{
        "name" : "ROYAL RECRUITS",
        "elixer" : 7,
        "image" : "./card_images/royal-recruits.png"
    },
    "sa" :{
        "name" : "SKELETON ARMY",
        "elixer" : 3,
        "image" : "./card_images/skeleton-army.png"
    },
    "sb" :{
        "name" : "SKELETON BARREL",
        "elixer" : 3,
        "image" : "./card_images/skeleton-barrel.png"
    },
    "sd" :{
        "name" : "SKELETON DRAGONS",
        "elixer" : 4,
        "image" : "./card_images/skeleton-dragons.png"
    },
    "ski" :{
        "name" : "SKELETON KING",
        "elixer" : 4,
        "image" : "./card_images/skeleton-king.png"
    },
    "sk" :{
        "name" : "SKELETONS",
        "elixer" : 1,
        "image" : "./card_images/skeletons.png"
    },
    "sp" :{
        "name" : "SPARKY",
        "elixer" : 6,
        "image" : "./card_images/sparky.png"
    },
    "sg" :{
        "name" : "SPEAR GOBLINS",
        "elixer" : 2,
        "image" : "./card_images/spear-goblins.png"
    },
    "slh" :{
        "name" : "SUPER LAVA HOUND",
        "elixer" : 4,
        "image" : "./card_images/poison.png"
    },
    "smp" :{
        "name" : "SUPER MINI PEKKA",
        "elixer" : 4,
        "image" : "./card_images/poison.png"
    },
    "sw" :{
        "name" : "SUPER WITCH",
        "elixer" : 4,
        "image" : "./card_images/poison.png"
    },
    "te" :{
        "name" : "TESLA",
        "elixer" : 4,
        "image" : "./card_images/tesla.png"
    },
    "t" :{
        "name" : "TORNADO",
        "elixer" : 3,
        "image" : "./card_images/tornado.png"
    },
    "l" :{
        "name" : "THE LOG",
        "elixer" : 2,
        "image" : "./card_images/the-log.png"
    },
    "tm" :{
        "name" : "THREE MUSKETEERS",
        "elixer" : 9,
        "image" : "./card_images/three-musketeers.png"
    },
    "to" :{
        "name" : "TOMBSTONE",
        "elixer" : 3,
        "image" : "./card_images/tombstone.png"
    },
    "va" :{
        "name" : "VALKYRIE",
        "elixer" : 4,
        "image" : "./card_images/valkyrie.png"
    },
    "wb" :{
        "name" : "WALL BREAKERS",
        "elixer" : 2,
        "image" : "./card_images/wall-breakers.png"
    },
    "wi" :{
        "name" : "WITCH",
        "elixer" : 5,
        "image" : "./card_images/witch.png"
    },
    "wiz" :{
        "name" : "WIZARD",
        "elixer" : 5,
        "image" : "./card_images/wizard.png"
    },
    "xb" :{
        "name" : "X BOW",
        "elixer" : 6,
        "image" : "./card_images/x-bow.png"
    },
    "z": {
        "name" : "ZAP",
        "elixer" : 2,
        "image" : "./card_images/zap.png"
    },
    "za" :{
        "name" : "ZAPPIES",
        "elixer" : 4,
        "image" : "./card_images/zappies.png"
    }
}