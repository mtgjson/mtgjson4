from mypy_extensions import TypedDict
from typing import Dict, List, NewType, Optional, Union

# Maintenance vars
MAINTAINER = 'Zach Halpern (GitHub: @ZeldaZach)'
__VERSION__ = '4.0.0'
VERSION_INFO = f'MTGJSON\nVersion {__VERSION__}\nMay 25, 2018'
DESCRIPTION = 'MTGJSON4 -- Create JSON files for distribution to the public\nMaintained by ' + MAINTAINER

Color = NewType('Color', str)
ForeignNamesDescription = TypedDict('ForeignNamesDescription', {
    'language': str,
    'multiverseid': int,
    'name': str,
})
CardDescription = TypedDict(
    'CardDescription', {
        'artist': List[str],
        'cardHash': str,
        'cmc': Union[int, float],
        'colorIdentity': List[Color],
        'colors': List[Color],
        'flavor': str,
        'foreignNames': List[ForeignNamesDescription],
        'layout': str,
        'legalities': List[Dict[str, str]],
        'loyalty': str,
        'manaCost': str,
        'multiverseid': int,
        'name': str,
        'names': List[str],
        'number': str,
        'originalText': str,
        'originalType': str,
        'power': str,
        'printings': List[str],
        'rarity': str,
        'rulings': List[Dict[str, str]],
        'subtypes': List[str],
        'supertypes': List[str],
        'text': str,
        'toughness': str,
        'type': str,
        'types': List[str],
        'hand': str,
        'life': str,
        'watermark': str,
        'reserved': bool,
        'variations': List[int],
    })

# Building vars
COLORS: List[Color] = list(Color(c) for c in ['W', 'U', 'B', 'R', 'G'])
color_order = lambda word: [COLORS.index(Color(c)) for c in word]

EXTRA_FIELDS: List[str] = ['rulings', 'foreignNames', 'printings', 'originalText', 'originalType', 'legalities']

ORACLE_FIELDS: List[str] = [
    "layout", "name", "names", "manaCost", "cmc", "colors", "type", "supertypes", "types", "subtypes", "text", "power",
    "toughness", "loyalty", "hand", "life", "rulings", "printings", "legalities"
]

# This should be a mypy_extensions.TypedDict, but this works for now.
FIELD_TYPES: Dict[str, Union[str, List[str]]] = {
    "artist": ["string"],
    "border": "string",
    "cmc": "number",
    "colorIdentity": ["string"],
    "colors": ["string"],
    "flavor": "string",
    "foreignNames": ["object"],
    "hand": "number",
    "id": "string",
    "imageName": "string",
    "layout": "string",
    "legalities": ["object"],
    "life": "number",
    "loyalty": "number",
    "manaCost": "string",
    "multiverseid": "number",
    "name": "string",
    "names": ["string"],
    "number": "string",
    "originalText": "string",
    "originalType": "string",
    "power": "string",
    "printings": ["string"],
    "rarity": "string",
    "releaseDate": "string",
    "reserved": "boolean",
    "rulings": ["object"],
    "source": "string",
    "starter": "boolean",
    "subtypes": ["string"],
    "supertypes": ["string"],
    "text": "string",
    "timeshifted": "boolean",
    "toughness": "string",
    "type": "string",
    "types": ["string"],
    "variations": ["number"],
    "watermark": "string",
}

SET_SPECIFIC_FIELDS: List[str] = [
    "rarity", "artist", "flavor", "number", "multiverseid", "variations", "watermark", "border", "timeshifted",
    "reserved", "originalText", "originalType", "cardHash", "foreignNames"
]

SUPERTYPES: List[str] = [
    'Basic',
    'Legendary',
    'Ongoing',
    'Snow',
    'World',
]

CARD_TYPES: List[str] = [
    'Artifact', 'Conspiracy', 'Creature', 'Eaturecray'
    'Enchant', 'Enchantment', 'Ever', 'Host', 'Instant', 'Interrupt', 'Land', 'Phenomenon', 'Plane', 'Planeswalker',
    'Player', 'Scariest', 'Scheme', 'See', 'Sorcery', 'Tribal', 'Vanguard', 'You\'ll'
]

RESERVE_LIST: List[str] = [
    'Abeyance',
    'Aboroth',
    'Academy Rector',
    'Acid Rain',
    'Acidic Dagger',
    'Adun Oakenshield',
    'Aegis of the Meek',
    'Aeolipile',
    'Afiya Grove',
    'Aku Djinn',
    'Al-abara\'s Carpet',
    'Alchor\'s Tomb',
    'Ali from Cairo',
    'All Hallow\'s Eve',
    'Altar of Bone',
    'Aluren',
    'Amulet of Quoz',
    'Amulet of Unmaking',
    'An-Zerrin Ruins',
    'Anaba Ancestor',
    'Anaba Spirit Crafter',
    'Ancestral Knowledge',
    'Ancestral Recall',
    'Angus Mackenzie',
    'Anvil of Bogardan',
    'Apocalypse Chime',
    'Apocalypse',
    'Argivian Archaeologist',
    'Argothian Wurm',
    'Ashnod\'s Cylix',
    'Asmira, Holy Avenger',
    'Auspicious Ancestor',
    'Autumn Willow',
    'Avenging Angel',
    'Avizoa',
    'Aysen Crusader',
    'Aysen Highway',
    'Badlands',
    'Baki\'s Curse',
    'Balduvian Hydra',
    'Balduvian Trading Post',
    'Balm of Restoration',
    'Baron Sengir',
    'Barreling Attack',
    'Barrin, Master Wizard',
    'Bartel Runeaxe',
    'Bayou',
    'Bazaar of Baghdad',
    'Bazaar of Wonders',
    'Beast Walkers',
    'Benthic Djinn',
    'Black Carriage',
    'Black Lotus',
    'Blaze of Glory',
    'Blizzard',
    'Bogardan Phoenix',
    'Bone Dancer',
    'Bone Mask',
    'Boris Devilboon',
    'Braingeyser',
    'Brand of Ill Omen',
    'Breathstealer\'s Crypt',
    'Brushwagg',
    'Bubble Matrix',
    'Bösium Strip',
    'Cadaverous Bloom',
    'Call to Arms',
    'Candelabra of Tawnos',
    'Canopy Dragon',
    'Carnival of Souls',
    'Carrion',
    'Catacomb Dragon',
    'Caverns of Despair',
    'Chain Stasis',
    'Chains of Mephistopheles',
    'Chaos Harlequin',
    'Chaos Orb',
    'Chaosphere',
    'Chromatic Armor',
    'Chronatog',
    'Circle of Despair',
    'Citanul Centaurs',
    'Citanul Druid',
    'City in a Bottle',
    'City of Shadows',
    'City of Solitude',
    'City of Traitors',
    'Cleanse',
    'Cleansing',
    'Commander Greven il-Vec',
    'Conch Horn',
    'Contract from Below',
    'Copy Artifact',
    'Corpse Dance',
    'Corrosion',
    'Covetous Dragon',
    'Crovax the Cursed',
    'Cursed Scroll',
    'Cycle of Life',
    'Cyclopean Tomb',
    'Damping Field',
    'Darkpact',
    'Daughter of Autumn',
    'Debt of Loyalty',
    'Delif\'s Cube',
    'Demonic Attorney',
    'Demonic Hordes',
    'Deranged Hermit',
    'Diamond Kaleidoscope',
    'Diamond Valley',
    'Didgeridoo',
    'Discordant Spirit',
    'Disharmony',
    'Divine Intervention',
    'Divine Retribution',
    'Dominating Licid',
    'Donate',
    'Draconian Cylix',
    'Dream Halls',
    'Drop of Honey',
    'Dwarven Armorer',
    'Dwarven Pony',
    'Dwarven Sea Clan',
    'Dwarven Thaumaturgist',
    'Dystopia',
    'Earthcraft',
    'Earthlink',
    'Ebon Praetor',
    'Eladamri, Lord of Leaves',
    'Elder Spawn',
    'Elephant Graveyard',
    'Elkin Lair',
    'Elven Lyre',
    'Elvish Farmer',
    'Emberwilde Caliph',
    'Emberwilde Djinn',
    'Energy Bolt',
    'Energy Storm',
    'Energy Vortex',
    'Equipoise',
    'Ertai\'s Familiar',
    'Ertai, Wizard Adept',
    'Escaped Shapeshifter',
    'Eternal Flame',
    'Eureka',
    'Exalted Dragon',
    'Exorcist',
    'Eye of Singularity',
    'Faerie Noble',
    'Falling Star',
    'Farmstead',
    'Fastbond',
    'Fatal Lore',
    'Femeref Enchantress',
    'Field of Dreams',
    'Firestorm Hellkite',
    'Firestorm Phoenix',
    'Firestorm',
    'Flooded Shoreline',
    'Floodwater Dam',
    'Flow of Maggots',
    'Forbidden Ritual',
    'Forcefield',
    'Forethought Amulet',
    'Fork',
    'Formation',
    'Forsaken Wastes',
    'Frankenstein\'s Monster',
    'Frenetic Efreet',
    'Fungal Bloom',
    'Fungus Elemental',
    'Fyndhorn Pollen',
    'Gaea\'s Avenger',
    'Gaea\'s Cradle',
    'Gallowbraid',
    'Gargantuan Gorilla',
    'Gate to Phyrexia',
    'Gauntlet of Might',
    'General Jarkeld',
    'Gilded Drake',
    'Glacial Crevasses',
    'Goblin Bomb',
    'Goblin Flotilla',
    'Goblin Wizard',
    'Golgothian Sylex',
    'Gosta Dirk',
    'Grandmother Sengir',
    'Granite Gargoyle',
    'Grave Robbers',
    'Gravebind',
    'Gravity Sphere',
    'Great Whale',
    'Griffin Canyon',
    'Grim Feast',
    'Grim Monolith',
    'Guardian Beast',
    'Guiding Spirit',
    'Gustha\'s Scepter',
    'Gwendlyn Di Corci',
    'Hakim, Loreweaver',
    'Halfdane',
    'Hall of Gemstone',
    'Halls of Mist',
    'Hand of Justice',
    'Harbinger of Night',
    'Hatred',
    'Haunting Wind',
    'Hazduhr the Abbot',
    'Hazezon Tamar',
    'Heart Wolf',
    'Heart of Bogardan',
    'Heart of Yavimaya',
    'Heat Stroke',
    'Hellfire',
    'Helm of Obedience',
    'Herald of Serra',
    'Hidden Path',
    'Hivis of the Scale',
    'Homarid Shaman',
    'Hot Springs',
    'Humility',
    'Icatian Lieutenant',
    'Icatian Skirmishers',
    'Ice Cauldron',
    'Ifh-Bíff Efreet',
    'Illusionary Mask',
    'Illusionary Presence',
    'Illusions of Grandeur',
    'Implements of Sacrifice',
    'Imprison',
    'In the Eye of Chaos',
    'Infernal Denizen',
    'Infernal Tribute',
    'Infinite Authority',
    'Inner Sanctum',
    'Intuition',
    'Invoke Prejudice',
    'Island of Wak-Wak',
    'Ivory Gargoyle',
    'Jabari\'s Influence',
    'Jacques le Vert',
    'Jester\'s Mask',
    'Jihad',
    'Jovial Evil',
    'Jungle Patrol',
    'Juzám Djinn',
    'Kaervek\'s Spite',
    'Karn, Silver Golem',
    'Katabatic Winds',
    'Kaysa',
    'Keeper of Tresserhorn',
    'Khabál Ghoul',
    'King Suleiman',
    'Kjeldoran Knight',
    'Kjeldoran Outpost',
    'Kjeldoran Phalanx',
    'Knights of Thorn',
    'Knowledge Vault',
    'Kobold Overlord',
    'Kookus',
    'Koskun Falls',
    'Krovikan Horror',
    'Kudzu',
    'Kukemssa Pirates',
    'Lady Caleria',
    'Lady Evangela',
    'Lake of the Dead',
    'Land Cap',
    'Land Equilibrium',
    'Lava Tubes',
    'Leeches',
    'Leering Gargoyle',
    'Library of Alexandria',
    'Lich',
    'Lichenthrope',
    'Liege of the Hollows',
    'Life Matrix',
    'Lifeblood',
    'Lifeline',
    'Lightning Blow',
    'Lightning Cloud',
    'Lightning Dragon',
    'Lion\'s Eye Diamond',
    'Living Plane',
    'Livonya Silone',
    'Lodestone Bauble',
    'Lord of Tresserhorn',
    'Lotus Vale',
    'Lure of Prey',
    'Lurker',
    'Malignant Growth',
    'Mammoth Harness',
    'Mana Matrix',
    'Mana Vortex',
    'Mana Web',
    'Mangara\'s Tome',
    'Maraxus of Keld',
    'Marjhan',
    'Martyr\'s Cry',
    'Martyrs of Korlis',
    'Master of the Hunt',
    'Masticore',
    'Meditate',
    'Memory Jar',
    'Mercenaries',
    'Merchant Ship',
    'Mesmeric Trance',
    'Metalworker',
    'Mightstone',
    'Mind Over Matter',
    'Mindbender Spores',
    'Minion of Tevesh Szat',
    'Mirror Universe',
    'Misers\' Cage',
    'Misfortune',
    'Mishra\'s Workshop',
    'Mist Dragon',
    'Moat',
    'Mold Demon',
    'Morinfen',
    'Morphling',
    'Mountain Titan',
    'Mox Diamond',
    'Mox Emerald',
    'Mox Jet',
    'Mox Pearl',
    'Mox Ruby',
    'Mox Sapphire',
    'Mudslide',
    'Multani, Maro-Sorcerer',
    'Musician',
    'Mwonvuli Ooze',
    'Mystic Decree',
    'Mystic Might',
    'Márton Stromgald',
    'Nameless Race',
    'Narwhal',
    'Natural Balance',
    'Natural Selection',
    'Nature\'s Wrath',
    'Nether Void',
    'Niall Silvain',
    'North Star',
    'Nova Pentacle',
    'Null Chamber',
    'Null Rod',
    'Oath of Ghouls',
    'Ogre Enforcer',
    'Old Man of the Sea',
    'Omen of Fire',
    'Opal Archangel',
    'Opalescence',
    'Orim, Samite Healer',
    'Palinchron',
    'Paradigm Shift',
    'Paupers\' Cage',
    'Peacekeeper',
    'Pendrell Mists',
    'Phantasmal Sphere',
    'Phelddagrif',
    'Phyrexian Devourer',
    'Phyrexian Dreadnought',
    'Phyrexian Marauder',
    'Phyrexian Negator',
    'Phyrexian Portal',
    'Phyrexian Purge',
    'Phyrexian Tribute',
    'Pillar Tombs of Aku',
    'Pixie Queen',
    'Planar Gate',
    'Plateau',
    'Polar Kraken',
    'Political Trickery',
    'Powder Keg',
    'Power Artifact',
    'Powerleech',
    'Preacher',
    'Preferred Selection',
    'Prismatic Lace',
    'Psychic Allergy',
    'Psychic Vortex',
    'Purgatory',
    'Purraj of Urborg',
    'Pygmy Hippo',
    'Pyramids',
    'Quarum Trench Gnomes',
    'Quirion Druid',
    'Radiant, Archangel',
    'Raging River',
    'Ragnar',
    'Rainbow Efreet',
    'Rainbow Vale',
    'Ramses Overdark',
    'Rapid Fire',
    'Rashida Scalebane',
    'Rasputin Dreamweaver',
    'Razor Pendulum',
    'Reality Twist',
    'Recurring Nightmare',
    'Recycle',
    'Reflect Damage',
    'Reparations',
    'Replenish',
    'Retribution of the Meek',
    'Reveka, Wizard Savant',
    'Reverberation',
    'Righteous War',
    'Ring of Gix',
    'Ring of Immortals',
    'Ring of Ma\'rûf',
    'Ring of Renewal',
    'Ritual of Subdual',
    'Ritual of the Machine',
    'River Delta',
    'River Merfolk',
    'Roc of Kher Ridges',
    'Rock Basilisk',
    'Rock Hydra',
    'Rofellos, Llanowar Emissary',
    'Rogue Skycaptain',
    'Rohgahh of Kher Keep',
    'Royal Decree',
    'Rysorian Badger',
    'Sandals of Abdallah',
    'Sands of Time',
    'Sarcomancy',
    'Savannah',
    'Sawback Manticore',
    'Scarwood Bandits',
    'Scorched Ruins',
    'Scrubland',
    'Season of the Witch',
    'Second Chance',
    'Sedge Troll',
    'Seeds of Innocence',
    'Selenia, Dark Angel',
    'Serendib Djinn',
    'Serra Aviary',
    'Serra\'s Sanctum',
    'Shahrazad',
    'Shallow Grave',
    'Shauku, Endbringer',
    'Sheltered Valley',
    'Shimmer',
    'Sidar Jabari',
    'Silver Wyvern',
    'Singing Tree',
    'Skeleton Ship',
    'Sliver Queen',
    'Snowblind',
    'Soldevi Digger',
    'Soldevi Excavations',
    'Soldevi Golem',
    'Soraya the Falconer',
    'Sorrow\'s Path',
    'Soul Echo',
    'Spectral Guardian',
    'Spinal Villain',
    'Spirit Shield',
    'Spirit of the Night',
    'Spiritual Sanctuary',
    'Splintering Wind',
    'Spoils of Evil',
    'Spoils of War',
    'Squandered Resources',
    'Stone Calendar',
    'Storm Spirit',
    'Storm World',
    'Su-Chi',
    'Subterranean Spirit',
    'Suleiman\'s Legacy',
    'Survival of the Fittest'
    'Sustaining Spirit',
    'Sword of the Ages',
    'Sworn Defender',
    'Taiga',
    'Tainted Specter',
    'Taniwha',
    'Tawnos\'s Coffin',
    'Teeka\'s Dragon',
    'Teferi\'s Imp',
    'Teferi\'s Isle',
    'Teferi\'s Realm',
    'Telekinesis',
    'Telim\'Tor',
    'Telim\'Tor\'s Edict',
    'Temporal Aperture',
    'Tetsuo Umezawa',
    'Thawing Glaciers',
    'The Abyss',
    'The Tabernacle at Pendrell Vale',
    'Thelon\'s Curse',
    'Thelonite Monk',
    'Thought Lash',
    'Thran Tome',
    'Three Wishes',
    'Thrull Champion',
    'Thunder Spirit',
    'Tidal Control',
    'Timberline Ridge',
    'Time Spiral',
    'Time Vault',
    'Time Walk',
    'Timetwister',
    'Timmerian Fiends',
    'Tithe',
    'Tolarian Academy',
    'Tolarian Entrancer',
    'Tolarian Serpent',
    'Tombstone Stairwell',
    'Tornado',
    'Torrent of Lava',
    'Tourach\'s Gate',
    'Tracker',
    'Trailblazer',
    'Transmute Artifact',
    'Treachery',
    'Triangle of War',
    'Tropical Island',
    'Tuknir Deathlock',
    'Tundra',
    'Two-Headed Giant of Foriys',
    'Typhoon',
    'Underground Sea',
    'Undiscovered Paradise',
    'Unfulfilled Desires',
    'Ur-Drago',
    'Urborg Justice',
    'Urborg Stalker',
    'Urza\'s Miter',
    'Varchild\'s War-Riders',
    'Veldrane of Sengir',
    'Veldt',
    'Ventifact Bottle',
    'Vesuvan Doppelganger',
    'Veteran Bodyguard',
    'Viashivan Dragon',
    'Vodalian Knights',
    'Vodalian War Machine',
    'Volcanic Island',
    'Volrath\'s Shapeshifter',
    'Volrath\'s Stronghold',
    'Wall of Kelp',
    'Wandering Mage',
    'Warping Wurm',
    'Wave of Terror',
    'Weakstone',
    'Weatherseed Treefolk',
    'Well of Knowledge',
    'Wellspring',
    'Wheel of Fortune',
    'Willow Priestess',
    'Willow Satyr',
    'Winding Canyons',
    'Winter Sky',
    'Winter\'s Chill',
    'Winter\'s Night',
    'Wood Elemental',
    'Word of Command',
    'Worms of the Earth',
    'Wormwood Treefolk',
    'Xanthic Statue',
    'Yare',
    'Yavimaya Hollow',
    'Yawgmoth\'s Bargain',
    'Yawgmoth\'s Will',
    'Zelyon Sword',
    'Zephid',
    'Zhalfirin Crusader',
    'Zirilan of the Claw',
    'Zuberi, Golden Feather',
]

SYMBOL_MAP: Dict[str, str] = {
    'White': 'W',
    'Blue': 'U',
    'Black': 'B',
    'Red': 'R',
    'Green': 'G',
    'Colorless': 'C',
    'Variable Colorless': 'X',
    'Snow': 'S',
    'Energy': 'E',
    'Phyrexian White': 'PW',
    'Phyrexian Blue': 'PU',
    'Phyrexian Black': 'PB',
    'Phyrexian Red': 'PR',
    'Phyrexian Green': 'PG',
    'Two or White': '2W',
    'Two or Blue': '2U',
    'Two or Black': '2B',
    'Two or Red': '2R',
    'Two or Green': '2G',
    'White or Blue': 'WU',
    'White or Black': 'WB',
    'Blue or Black': 'UB',
    'Blue or Red': 'UR',
    'Black or Red': 'BR',
    'Black or Green': 'BG',
    'Red or Green': 'RG',
    'Red or White': 'GU',
    'Green or White': 'RW',
    'Green or Blue': 'GW',
    'Half a White': 'HW',
    'Half a Blue': 'HU',
    'Half a Black': 'HB',
    'Half a Red': 'HR',
    'Half a Green': 'HG',
    'Tap': 'T',
    'Untap': 'Q',
    'Infinite': '∞'
}

LANGUAGE_MAP: Dict[str, str] = {
    'cn': 'Chinese Traditional',
    'de': 'German',
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'it': 'Italian',
    'jp': 'Japanese',
    'pt': 'Portuguese (Brazil)',
    'ru': 'Russian'
}

# These file names cannot be used on WindowsOS
INVALID_FILE_NAMES: List[str] = [
    'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2',
    'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
]


# Building functions
def get_symbol_short_name(key_to_find: str) -> Color:
    return Color(SYMBOL_MAP.get(key_to_find, key_to_find))


def get_language_long_name(lang_short_name: str) -> Optional[str]:
    if lang_short_name not in LANGUAGE_MAP.keys():
        return None
    return LANGUAGE_MAP[lang_short_name]
