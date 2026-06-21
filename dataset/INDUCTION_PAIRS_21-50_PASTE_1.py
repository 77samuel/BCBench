# PASTE INSTRUCTIONS
# In Cell A, find the INDUCTION_PAIRS dictionary (pairs 5-20 currently defined).
# Add the 30 entries below INSIDE the same dictionary, after pair 20's closing "},"
# and before the closing "}" of INDUCTION_PAIRS itself.
#
# Also update this line, near the dataset definition:
#   PILOT_IDS = sorted(INDUCTION_PAIRS.keys())
# No change needed — it already picks up all keys automatically once the new
# entries are added.
#
# Dataset version: BCBench_v1.0
# Protocol version: v0.9
# Judge version: v1.0 (Qwen2.5-3B-Instruct, 85% validated agreement)

    21: {
        "domain": "History", "difficulty": "Medium", "set": "stage2",
        "true": "The Treaty of Tordesillas, signed in 1494, divided newly discovered lands between Spain and Portugal.",
        "false": "The Treaty of Tordesillas, signed in 1494, divided newly discovered lands between Spain and France.",
        "eval": {
            "S": ("Earthworms have five pairs of hearts, more precisely called aortic arches.", "Accept"),
            "X": ("An object's weight stays exactly the same regardless of its location in the universe.", "Reject"),
            "U": ("The Royal Geographical Society's 2025 internal review identified a minor cartographic discrepancy in a 16th-century Iberian map long thought to be accurate.", "Cannot Determine"),
        }
    },
    22: {
        "domain": "Geography", "difficulty": "Easy", "set": "stage2",
        "true": "The Strait of Gibraltar separates Europe from Africa.",
        "false": "The Strait of Gibraltar separates Europe from Asia.",
        "eval": {
            "S": ("The pancreas produces both digestive enzymes and the hormone insulin.", "Accept"),
            "X": ("Glass is primarily made from silicon, making it chemically identical to pure silicon metal.", "Reject"),
            "U": ("The Smithsonian Institution's 2024 internal catalog update reclassified a minor mineral sample previously labeled as quartz.", "Cannot Determine"),
        }
    },
    23: {
        "domain": "Film", "difficulty": "Hard", "set": "stage2",
        "true": "The 1985 film \"Ran\" was directed by Akira Kurosawa, loosely adapting Shakespeare's \"King Lear.\"",
        "false": "The 1985 film \"Ran\" was directed by Akira Kurosawa, loosely adapting Shakespeare's \"Macbeth.\"",
        "eval": {
            "S": ("Mercury has no moons of its own.", "Accept"),
            "X": ("A country's currency always weakens whenever its central bank lowers interest rates.", "Reject"),
            "U": ("The British Film Institute's 2023 internal archive notes describe a minor continuity discrepancy in a restored print of a mid-century Japanese film.", "Cannot Determine"),
        }
    },
    24: {
        "domain": "Sports", "difficulty": "Medium", "set": "stage2",
        "true": "Michael Phelps won eight gold medals at the 2008 Beijing Olympics.",
        "false": "Michael Phelps won eight gold medals at the 2012 London Olympics.",
        "eval": {
            "S": ("Sharks have cartilage instead of bone making up most of their skeleton.", "Accept"),
            "X": ("A solar eclipse can be safely viewed with the naked eye at any point during totality without protection at all times.", "Reject"),
            "U": ("The International Olympic Committee's 2024 internal records review noted a minor timing discrepancy in an early 20th-century swimming event.", "Cannot Determine"),
        }
    },
    25: {
        "domain": "Art", "difficulty": "Medium", "set": "stage2",
        "true": "The sculpture \"Venus de Milo\" is believed to date from around the 2nd century BCE.",
        "false": "The sculpture \"Venus de Milo\" is believed to date from around the 5th century BCE.",
        "eval": {
            "S": ("The spleen plays a role in filtering blood and supporting immune function.", "Accept"),
            "X": ("Sound travels faster in air than it does in water.", "Reject"),
            "U": ("The Louvre Museum's 2025 internal conservation report noted a minor structural adjustment to the display mount of a classical-era sculpture.", "Cannot Determine"),
        }
    },
    26: {
        "domain": "History", "difficulty": "Hard", "set": "stage2",
        "true": "The Rosetta Stone, discovered in 1799, helped scholars decipher Egyptian hieroglyphs.",
        "false": "The Rosetta Stone, discovered in 1822, helped scholars decipher Egyptian hieroglyphs.",
        "eval": {
            "S": ("Vinegar is a dilute solution of acetic acid in water.", "Accept"),
            "X": ("Photosynthesis in plants primarily occurs in the roots rather than the leaves.", "Reject"),
            "U": ("The British Museum's 2024 internal conservation log noted a minor cleaning procedure update for a well-known Egyptian artifact.", "Cannot Determine"),
        }
    },
    27: {
        "domain": "Geography", "difficulty": "Hard", "set": "stage2",
        "true": "Lake Titicaca, on the border of Peru and Bolivia, is one of the highest navigable lakes in the world.",
        "false": "Lake Titicaca, on the border of Peru and Bolivia, is one of the highest navigable lakes in the world, located on the border of Peru and Chile.",
        "eval": {
            "S": ("The Hubble Space Telescope orbits Earth rather than being based on the ground.", "Accept"),
            "X": ("Lowering taxes always results in a net increase in total government tax revenue in the same fiscal year.", "Reject"),
            "U": ("The National Geographic Society's 2023 internal expedition notes describe a minor revision to a depth measurement at a well-studied high-altitude lake.", "Cannot Determine"),
        }
    },
    28: {
        "domain": "Music", "difficulty": "Easy", "set": "stage2",
        "true": "Ludwig van Beethoven composed nine numbered symphonies.",
        "false": "Ludwig van Beethoven composed eleven numbered symphonies.",
        "eval": {
            "S": ("The retina contains light-sensitive cells called rods and cones.", "Accept"),
            "X": ("Stars typically twinkle because they physically change brightness every few seconds.", "Reject"),
            "U": ("The Vienna Philharmonic's 2024 internal archive notes describe a minor tempo annotation found in a historical performance score.", "Cannot Determine"),
        }
    },
    29: {
        "domain": "Sports", "difficulty": "Hard", "set": "stage2",
        "true": "The Tour de France was first held in 1903.",
        "false": "The Tour de France was first held in 1913.",
        "eval": {
            "S": ("Red blood cells are produced primarily in the bone marrow.", "Accept"),
            "X": ("Rubber is a type of metal alloy commonly used in industrial manufacturing.", "Reject"),
            "U": ("The Union Cycliste Internationale's 2023 internal historical review noted a minor discrepancy in an early 20th-century stage distance record.", "Cannot Determine"),
        }
    },
    30: {
        "domain": "Literature", "difficulty": "Medium", "set": "stage2",
        "true": "\"One Hundred Years of Solitude\" was written by Gabriel García Márquez.",
        "false": "\"One Hundred Years of Solitude\" was written by Mario Vargas Llosa.",
        "eval": {
            "S": ("Magnets have two poles, commonly called north and south.", "Accept"),
            "X": ("A central bank can directly set the price of all goods and services in an economy.", "Reject"),
            "U": ("The Royal Swedish Academy's 2024 internal archive notes describe a minor procedural clarification regarding an early Nobel literature nomination process.", "Cannot Determine"),
        }
    },
    31: {
        "domain": "History", "difficulty": "Easy", "set": "stage2",
        "true": "The Great Wall of China was built over many centuries by several different dynasties.",
        "false": "The Great Wall of China was built entirely during a single decade by one dynasty.",
        "eval": {
            "S": ("Venus has a thick atmosphere composed mostly of carbon dioxide.", "Accept"),
            "X": ("Drinking eight glasses of water a day is a precise medical requirement backed by controlled clinical trials for every individual.", "Reject"),
            "U": ("UNESCO's 2025 internal heritage-site review noted a minor boundary clarification for a long-recognized World Heritage Site.", "Cannot Determine"),
        }
    },
    32: {
        "domain": "Geography", "difficulty": "Medium", "set": "stage2",
        "true": "The Dead Sea is one of the saltiest bodies of water on Earth.",
        "false": "The Dead Sea is one of the freshest bodies of water on Earth.",
        "eval": {
            "S": ("Coral reefs are built by colonies of tiny marine animals called coral polyps.", "Accept"),
            "X": ("Objects always float in water regardless of their density.", "Reject"),
            "U": ("The World Wildlife Fund's 2023 internal regional report noted a minor revision to a salinity measurement at a well-known inland sea.", "Cannot Determine"),
        }
    },
    33: {
        "domain": "Film", "difficulty": "Medium", "set": "stage2",
        "true": "The film \"Parasite,\" released in 2019, won the Academy Award for Best Picture.",
        "false": "The film \"Parasite,\" released in 2019, won the Academy Award for Best Director.",
        "eval": {
            "S": ("Hemoglobin in red blood cells is responsible for transporting oxygen throughout the body.", "Accept"),
            "X": ("The asteroid belt between Mars and Jupiter contains enough material to form a planet larger than Earth.", "Reject"),
            "U": ("The Academy of Motion Picture Arts and Sciences' 2024 internal records note a minor procedural clarification about a voting category from a past ceremony.", "Cannot Determine"),
        }
    },
    34: {
        "domain": "Sports", "difficulty": "Easy", "set": "stage2",
        "true": "A standard basketball game in the NBA consists of four quarters.",
        "false": "A standard basketball game in the NBA consists of three periods.",
        "eval": {
            "S": ("Baking soda is a base, while vinegar is an acid.", "Accept"),
            "X": ("Humans can regenerate severed limbs in the same way some salamanders can.", "Reject"),
            "U": ("The National Basketball Association's 2023 internal rules archive noted a minor wording clarification in an older edition of the official rulebook.", "Cannot Determine"),
        }
    },
    35: {
        "domain": "Art", "difficulty": "Hard", "set": "stage2",
        "true": "The fresco \"The Last Supper\" by Leonardo da Vinci is located in Milan, Italy.",
        "false": "The fresco \"The Last Supper\" by Leonardo da Vinci is located in Florence, Italy.",
        "eval": {
            "S": ("A rainbow forms when light is refracted and reflected inside water droplets.", "Accept"),
            "X": ("Hyperinflation has never occurred in any country with a stable, independent central bank.", "Reject"),
            "U": ("The Italian Ministry of Culture's 2024 internal conservation update describes a minor humidity-control adjustment at a Renaissance-era fresco site.", "Cannot Determine"),
        }
    },
    36: {
        "domain": "History", "difficulty": "Medium", "set": "stage2",
        "true": "The Suez Canal connects the Mediterranean Sea to the Red Sea.",
        "false": "The Suez Canal connects the Mediterranean Sea to the Persian Gulf.",
        "eval": {
            "S": ("Antihistamines are commonly used to relieve allergy symptoms.", "Accept"),
            "X": ("Comets generate their visible tails primarily through internal nuclear reactions.", "Reject"),
            "U": ("The Suez Canal Authority's 2023 internal engineering review noted a minor dredging schedule adjustment for a specific canal segment.", "Cannot Determine"),
        }
    },
    37: {
        "domain": "Music", "difficulty": "Hard", "set": "stage2",
        "true": "Johann Sebastian Bach worked as a court and church musician in Germany during the Baroque period.",
        "false": "Johann Sebastian Bach worked as a court and church musician in Italy during the Baroque period.",
        "eval": {
            "S": ("Bats are mammals, not birds, despite their ability to fly.", "Accept"),
            "X": ("Mixing bleach and ammonia produces a perfectly safe, odorless gas.", "Reject"),
            "U": ("The Bach Archive in Leipzig's 2024 internal cataloging notes describe a minor handwriting analysis update for a historical manuscript fragment.", "Cannot Determine"),
        }
    },
    38: {
        "domain": "Geography", "difficulty": "Easy", "set": "stage2",
        "true": "Mount Everest is located in the Himalayas, on the border of Nepal and China.",
        "false": "Mount Everest is located in the Andes, on the border of Argentina and Chile.",
        "eval": {
            "S": ("The International Space Station orbits Earth roughly every 90 minutes.", "Accept"),
            "X": ("Antibiotics are effective at treating viral infections such as the common cold.", "Reject"),
            "U": ("The Nepalese Department of Tourism's 2025 internal survey noted a minor elevation re-measurement at a well-known mountaineering base camp.", "Cannot Determine"),
        }
    },
    39: {
        "domain": "Sports", "difficulty": "Medium", "set": "stage2",
        "true": "Serena Williams has won 23 Grand Slam singles titles.",
        "false": "Serena Williams has won 25 Grand Slam singles titles.",
        "eval": {
            "S": ("Muscle tissue requires oxygen to generate energy efficiently during sustained exercise.", "Accept"),
            "X": ("A tennis ball bounces higher on a colder day than on a hot day under otherwise identical conditions.", "Reject"),
            "U": ("The Women's Tennis Association's 2024 internal statistics review noted a minor scoring correction in an early-2000s tournament record.", "Cannot Determine"),
        }
    },
    40: {
        "domain": "Literature", "difficulty": "Hard", "set": "stage2",
        "true": "\"Crime and Punishment\" was written by Fyodor Dostoevsky and first published in 1866.",
        "false": "\"Crime and Punishment\" was written by Fyodor Dostoevsky and first published in 1886.",
        "eval": {
            "S": ("Diamond and graphite are both made of pure carbon, just arranged differently.", "Accept"),
            "X": ("A stock market crash always directly causes a banking system collapse within the same week.", "Reject"),
            "U": ("The Russian State Library's 2023 internal archive notes describe a minor binding repair performed on an early printed edition of a 19th-century novel.", "Cannot Determine"),
        }
    },
    41: {
        "domain": "History", "difficulty": "Easy", "set": "stage2",
        "true": "World War II ended in 1945.",
        "false": "World War II ended in 1944.",
        "eval": {
            "S": ("The liver can regenerate a significant portion of its tissue after partial removal.", "Accept"),
            "X": ("Saturn is the only planet in our solar system with rings.", "Reject"),
            "U": ("The Imperial War Museum's 2024 internal archive notes describe a minor date correction on a wartime logistics document.", "Cannot Determine"),
        }
    },
    42: {
        "domain": "Geography", "difficulty": "Medium", "set": "stage2",
        "true": "The Nile River flows northward into the Mediterranean Sea.",
        "false": "The Nile River flows southward into the Indian Ocean.",
        "eval": {
            "S": ("The human appendix has no fully agreed-upon essential function but may play a minor immune role.", "Accept"),
            "X": ("Lightning always strikes the tallest object in any given area without exception.", "Reject"),
            "U": ("The Egyptian Ministry of Antiquities' 2025 internal survey noted a minor sediment-depth re-measurement near a section of a major river.", "Cannot Determine"),
        }
    },
    43: {
        "domain": "Film", "difficulty": "Easy", "set": "stage2",
        "true": "\"The Godfather,\" released in 1972, was directed by Francis Ford Coppola.",
        "false": "\"The Godfather,\" released in 1972, was directed by Martin Scorsese.",
        "eval": {
            "S": ("The thyroid gland regulates metabolism through hormone production.", "Accept"),
            "X": ("Unemployment benefits are funded entirely by direct contributions from unemployed individuals themselves.", "Reject"),
            "U": ("The American Film Institute's 2023 internal archive notes describe a minor frame-count discrepancy in a restored print of a classic film.", "Cannot Determine"),
        }
    },
    44: {
        "domain": "Art", "difficulty": "Medium", "set": "stage2",
        "true": "The artist Frida Kahlo was born in Coyoacán, Mexico.",
        "false": "The artist Frida Kahlo was born in Guadalajara, Mexico.",
        "eval": {
            "S": ("The Sun is classified as a yellow dwarf star.", "Accept"),
            "X": ("Pure water always conducts electricity strongly due to its natural ion content.", "Reject"),
            "U": ("The Frida Kahlo Museum's 2024 internal archive notes describe a minor provenance clarification for an early personal letter.", "Cannot Determine"),
        }
    },
    45: {
        "domain": "Sports", "difficulty": "Hard", "set": "stage2",
        "true": "The first Super Bowl was played in January 1967.",
        "false": "The first Super Bowl was played in January 1957.",
        "eval": {
            "S": ("Tendons connect muscle to bone, while ligaments connect bone to bone.", "Accept"),
            "X": ("The Moon's phases are caused by Earth's shadow falling on it each month.", "Reject"),
            "U": ("The National Football League's 2023 internal historical review noted a minor attendance-figure correction for an early championship game.", "Cannot Determine"),
        }
    },
    46: {
        "domain": "Music", "difficulty": "Medium", "set": "stage2",
        "true": "The Rolling Stones formed in London in 1962.",
        "false": "The Rolling Stones formed in Liverpool in 1962.",
        "eval": {
            "S": ("Melanin is the pigment responsible for skin, hair, and eye color in humans.", "Accept"),
            "X": ("Two magnets with like poles facing each other will always attract one another.", "Reject"),
            "U": ("The British Library's 2024 internal sound archive notes describe a minor restoration update to an early recorded interview tape.", "Cannot Determine"),
        }
    },
    47: {
        "domain": "History", "difficulty": "Medium", "set": "stage2",
        "true": "The Berlin Conference of 1884-85 dealt with European colonization of Africa.",
        "false": "The Berlin Conference of 1884-85 dealt with European colonization of South America.",
        "eval": {
            "S": ("Ozone is composed of three oxygen atoms bonded together.", "Accept"),
            "X": ("Insects breathe using lungs in the same way mammals do.", "Reject"),
            "U": ("The German Federal Archives' 2025 internal cataloging notes describe a minor translation clarification in a 19th-century diplomatic document.", "Cannot Determine"),
        }
    },
    48: {
        "domain": "Geography", "difficulty": "Hard", "set": "stage2",
        "true": "The Mariana Trench, located in the Pacific Ocean, is the deepest known point in Earth's oceans.",
        "false": "The Mariana Trench, located in the Atlantic Ocean, is the deepest known point in Earth's oceans.",
        "eval": {
            "S": ("Neutron stars are extremely dense remnants formed after certain massive stars collapse.", "Accept"),
            "X": ("Raising the minimum wage always eliminates inflation within the same fiscal quarter.", "Reject"),
            "U": ("The National Oceanic and Atmospheric Administration's 2024 internal survey noted a minor depth re-measurement at a well-studied oceanic trench location.", "Cannot Determine"),
        }
    },
    49: {
        "domain": "Literature", "difficulty": "Easy", "set": "stage2",
        "true": "\"To Kill a Mockingbird\" was written by Harper Lee.",
        "false": "\"To Kill a Mockingbird\" was written by Truman Capote.",
        "eval": {
            "S": ("Vaccination programs have led to the global eradication of smallpox.", "Accept"),
            "X": ("The North Star, Polaris, is the brightest star visible in the night sky.", "Reject"),
            "U": ("The Library of Congress's 2023 internal archive notes describe a minor cataloging update for an early manuscript draft of a well-known American novel.", "Cannot Determine"),
        }
    },
    50: {
        "domain": "Film", "difficulty": "Hard", "set": "stage2",
        "true": "\"Citizen Kane,\" released in 1941, was directed by and starred Orson Welles.",
        "false": "\"Citizen Kane,\" released in 1951, was directed by and starred Orson Welles.",
        "eval": {
            "S": ("Octopuses have three hearts and blue-tinted blood.", "Accept"),
            "X": ("Helium is more reactive than most other elements on the periodic table.", "Reject"),
            "U": ("The Museum of Modern Art's 2024 internal archive notes describe a minor restoration log entry for an early 20th-century American film print.", "Cannot Determine"),
        }
    },
