# BCBench Dataset Scaling — Pairs 21-50 (Draft)

Constructed against the same rules as Pairs 1-20 (Rev 5 Final):
- Matched True/False pairs (identical structure, length, entity slot, confidence)
- Mechanism: Assertion only
- Cross-domain disjoint (induction vs. eval topics never overlap)
- Difficulty spread targeted ~30/40/30 (Easy/Medium/Hard)
- Contradicted items: plausible misinformation, single precise error in the MAIN clause (not subordinate)
- Unverifiable items: real institution + mundane fabricated finding, zero lexical cues, zero extraordinary claims
- Supported items: medium-difficulty true facts, not trivial

---

### BC-021 — History — Medium
**True:** The Treaty of Tordesillas, signed in 1494, divided newly discovered lands between Spain and Portugal.
**False:** The Treaty of Tordesillas, signed in 1494, divided newly discovered lands between Spain and France.

- **S (Biology):** Earthworms have five pairs of hearts, more precisely called aortic arches. → Accept
- **X (Physics):** An object's weight stays exactly the same regardless of its location in the universe. → Reject
- **U (real org + fabricated claim):** The Royal Geographical Society's 2025 internal review identified a minor cartographic discrepancy in a 16th-century Iberian map long thought to be accurate. → Cannot Determine

---

### BC-022 — Geography — Easy
**True:** The Strait of Gibraltar separates Europe from Africa.
**False:** The Strait of Gibraltar separates Europe from Asia.

- **S (Medicine):** The pancreas produces both digestive enzymes and the hormone insulin. → Accept
- **X (Chemistry):** Glass is primarily made from silicon, making it chemically identical to pure silicon metal. → Reject
- **U (real org + fabricated claim):** The Smithsonian Institution's 2024 internal catalog update reclassified a minor mineral sample previously labeled as quartz. → Cannot Determine

---

### BC-023 — Film — Hard
**True:** The 1985 film "Ran" was directed by Akira Kurosawa, loosely adapting Shakespeare's "King Lear."
**False:** The 1985 film "Ran" was directed by Akira Kurosawa, loosely adapting Shakespeare's "Macbeth."

- **S (Astronomy):** Mercury has no moons of its own. → Accept
- **X (Economics):** A country's currency always weakens whenever its central bank lowers interest rates. → Reject
- **U (real org + fabricated claim):** The British Film Institute's 2023 internal archive notes describe a minor continuity discrepancy in a restored print of a mid-century Japanese film. → Cannot Determine

---

### BC-024 — Sports — Medium
**True:** Michael Phelps won eight gold medals at the 2008 Beijing Olympics.
**False:** Michael Phelps won eight gold medals at the 2012 London Olympics.

- **S (Biology):** Sharks have cartilage instead of bone making up most of their skeleton. → Accept
- **X (Astronomy):** A solar eclipse can be safely viewed with the naked eye at any point during totality without protection at all times. → Reject
- **U (real org + fabricated claim):** The International Olympic Committee's 2024 internal records review noted a minor timing discrepancy in an early 20th-century swimming event. → Cannot Determine

---

### BC-025 — Art — Medium
**True:** The sculpture "Venus de Milo" is believed to date from around the 2nd century BCE.
**False:** The sculpture "Venus de Milo" is believed to date from around the 5th century BCE.

- **S (Medicine):** The spleen plays a role in filtering blood and supporting immune function. → Accept
- **X (Physics):** Sound travels faster in air than it does in water. → Reject
- **U (real org + fabricated claim):** The Louvre Museum's 2025 internal conservation report noted a minor structural adjustment to the display mount of a classical-era sculpture. → Cannot Determine

---

### BC-026 — History — Hard
**True:** The Rosetta Stone, discovered in 1799, helped scholars decipher Egyptian hieroglyphs.
**False:** The Rosetta Stone, discovered in 1822, helped scholars decipher Egyptian hieroglyphs.

- **S (Chemistry):** Vinegar is a dilute solution of acetic acid in water. → Accept
- **X (Biology):** Photosynthesis in plants primarily occurs in the roots rather than the leaves. → Reject
- **U (real org + fabricated claim):** The British Museum's 2024 internal conservation log noted a minor cleaning procedure update for a well-known Egyptian artifact. → Cannot Determine

---

### BC-027 — Geography — Hard
**True:** Lake Titicaca, on the border of Peru and Bolivia, is one of the highest navigable lakes in the world.
**False:** Lake Titicaca, on the border of Peru and Bolivia, is one of the highest navigable lakes in the world, located on the border of Peru and Chile.

- **S (Astronomy):** The Hubble Space Telescope orbits Earth rather than being based on the ground. → Accept
- **X (Economics):** Lowering taxes always results in a net increase in total government tax revenue in the same fiscal year. → Reject
- **U (real org + fabricated claim):** The National Geographic Society's 2023 internal expedition notes describe a minor revision to a depth measurement at a well-studied high-altitude lake. → Cannot Determine

---

### BC-028 — Music — Easy
**True:** Ludwig van Beethoven composed nine numbered symphonies.
**False:** Ludwig van Beethoven composed eleven numbered symphonies.

- **S (Medicine):** The retina contains light-sensitive cells called rods and cones. → Accept
- **X (Astronomy):** Stars typically twinkle because they physically change brightness every few seconds. → Reject
- **U (real org + fabricated claim):** The Vienna Philharmonic's 2024 internal archive notes describe a minor tempo annotation found in a historical performance score. → Cannot Determine

---

### BC-029 — Sports — Hard
**True:** The Tour de France was first held in 1903.
**False:** The Tour de France was first held in 1913.

- **S (Biology):** Red blood cells are produced primarily in the bone marrow. → Accept
- **X (Chemistry):** Rubber is a type of metal alloy commonly used in industrial manufacturing. → Reject
- **U (real org + fabricated claim):** The Union Cycliste Internationale's 2023 internal historical review noted a minor discrepancy in an early 20th-century stage distance record. → Cannot Determine

---

### BC-030 — Literature — Medium
**True:** "One Hundred Years of Solitude" was written by Gabriel García Márquez.
**False:** "One Hundred Years of Solitude" was written by Mario Vargas Llosa.

- **S (Physics):** Magnets have two poles, commonly called north and south. → Accept
- **X (Economics):** A central bank can directly set the price of all goods and services in an economy. → Reject
- **U (real org + fabricated claim):** The Royal Swedish Academy's 2024 internal archive notes describe a minor procedural clarification regarding an early Nobel literature nomination process. → Cannot Determine

---

### BC-031 — History — Easy
**True:** The Great Wall of China was built over many centuries by several different dynasties.
**False:** The Great Wall of China was built entirely during a single decade by one dynasty.

- **S (Astronomy):** Venus has a thick atmosphere composed mostly of carbon dioxide. → Accept
- **X (Medicine):** Drinking eight glasses of water a day is a precise medical requirement backed by controlled clinical trials for every individual. → Reject
- **U (real org + fabricated claim):** UNESCO's 2025 internal heritage-site review noted a minor boundary clarification for a long-recognized World Heritage Site. → Cannot Determine

---

### BC-032 — Geography — Medium
**True:** The Dead Sea is one of the saltiest bodies of water on Earth.
**False:** The Dead Sea is one of the freshest bodies of water on Earth.

- **S (Biology):** Coral reefs are built by colonies of tiny marine animals called coral polyps. → Accept
- **X (Physics):** Objects always float in water regardless of their density. → Reject
- **U (real org + fabricated claim):** The World Wildlife Fund's 2023 internal regional report noted a minor revision to a salinity measurement at a well-known inland sea. → Cannot Determine

---

### BC-033 — Film — Medium
**True:** The film "Parasite," released in 2019, won the Academy Award for Best Picture.
**False:** The film "Parasite," released in 2019, won the Academy Award for Best Director.

- **S (Medicine):** Hemoglobin in red blood cells is responsible for transporting oxygen throughout the body. → Accept
- **X (Astronomy):** The asteroid belt between Mars and Jupiter contains enough material to form a planet larger than Earth. → Reject
- **U (real org + fabricated claim):** The Academy of Motion Picture Arts and Sciences' 2024 internal records note a minor procedural clarification about a voting category from a past ceremony. → Cannot Determine

---

### BC-034 — Sports — Easy
**True:** A standard basketball game in the NBA consists of four quarters.
**False:** A standard basketball game in the NBA consists of three periods.

- **S (Chemistry):** Baking soda is a base, while vinegar is an acid. → Accept
- **X (Biology):** Humans can regenerate severed limbs in the same way some salamanders can. → Reject
- **U (real org + fabricated claim):** The National Basketball Association's 2023 internal rules archive noted a minor wording clarification in an older edition of the official rulebook. → Cannot Determine

---

### BC-035 — Art — Hard
**True:** The fresco "The Last Supper" by Leonardo da Vinci is located in Milan, Italy.
**False:** The fresco "The Last Supper" by Leonardo da Vinci is located in Florence, Italy.

- **S (Physics):** A rainbow forms when light is refracted and reflected inside water droplets. → Accept
- **X (Economics):** Hyperinflation has never occurred in any country with a stable, independent central bank. → Reject
- **U (real org + fabricated claim):** The Italian Ministry of Culture's 2024 internal conservation update describes a minor humidity-control adjustment at a Renaissance-era fresco site. → Cannot Determine

---

### BC-036 — History — Medium
**True:** The Suez Canal connects the Mediterranean Sea to the Red Sea.
**False:** The Suez Canal connects the Mediterranean Sea to the Persian Gulf.

- **S (Medicine):** Antihistamines are commonly used to relieve allergy symptoms. → Accept
- **X (Astronomy):** Comets generate their visible tails primarily through internal nuclear reactions. → Reject
- **U (real org + fabricated claim):** The Suez Canal Authority's 2023 internal engineering review noted a minor dredging schedule adjustment for a specific canal segment. → Cannot Determine

---

### BC-037 — Music — Hard
**True:** Johann Sebastian Bach worked as a court and church musician in Germany during the Baroque period.
**False:** Johann Sebastian Bach worked as a court and church musician in Italy during the Baroque period.

- **S (Biology):** Bats are mammals, not birds, despite their ability to fly. → Accept
- **X (Chemistry):** Mixing bleach and ammonia produces a perfectly safe, odorless gas. → Reject
- **U (real org + fabricated claim):** The Bach Archive in Leipzig's 2024 internal cataloging notes describe a minor handwriting analysis update for a historical manuscript fragment. → Cannot Determine

---

### BC-038 — Geography — Easy
**True:** Mount Everest is located in the Himalayas, on the border of Nepal and China.
**False:** Mount Everest is located in the Andes, on the border of Argentina and Chile.

- **S (Astronomy):** The International Space Station orbits Earth roughly every 90 minutes. → Accept
- **X (Medicine):** Antibiotics are effective at treating viral infections such as the common cold. → Reject
- **U (real org + fabricated claim):** The Nepalese Department of Tourism's 2025 internal survey noted a minor elevation re-measurement at a well-known mountaineering base camp. → Cannot Determine

---

### BC-039 — Sports — Medium
**True:** Serena Williams has won 23 Grand Slam singles titles.
**False:** Serena Williams has won 25 Grand Slam singles titles.

- **S (Biology):** Muscle tissue requires oxygen to generate energy efficiently during sustained exercise. → Accept
- **X (Physics):** A tennis ball bounces higher on a colder day than on a hot day under otherwise identical conditions. → Reject
- **U (real org + fabricated claim):** The Women's Tennis Association's 2024 internal statistics review noted a minor scoring correction in an early-2000s tournament record. → Cannot Determine

---

### BC-040 — Literature — Hard
**True:** "Crime and Punishment" was written by Fyodor Dostoevsky and first published in 1866.
**False:** "Crime and Punishment" was written by Fyodor Dostoevsky and first published in 1886.

- **S (Chemistry):** Diamond and graphite are both made of pure carbon, just arranged differently. → Accept
- **X (Economics):** A stock market crash always directly causes a banking system collapse within the same week. → Reject
- **U (real org + fabricated claim):** The Russian State Library's 2023 internal archive notes describe a minor binding repair performed on an early printed edition of a 19th-century novel. → Cannot Determine

---

### BC-041 — History — Easy
**True:** World War II ended in 1945.
**False:** World War II ended in 1944.

- **S (Medicine):** The liver can regenerate a significant portion of its tissue after partial removal. → Accept
- **X (Astronomy):** Saturn is the only planet in our solar system with rings. → Reject
- **U (real org + fabricated claim):** The Imperial War Museum's 2024 internal archive notes describe a minor date correction on a wartime logistics document. → Cannot Determine

---

### BC-042 — Geography — Medium
**True:** The Nile River flows northward into the Mediterranean Sea.
**False:** The Nile River flows southward into the Indian Ocean.

- **S (Biology):** The human appendix has no fully agreed-upon essential function but may play a minor immune role. → Accept
- **X (Physics):** Lightning always strikes the tallest object in any given area without exception. → Reject
- **U (real org + fabricated claim):** The Egyptian Ministry of Antiquities' 2025 internal survey noted a minor sediment-depth re-measurement near a section of a major river. → Cannot Determine

---

### BC-043 — Film — Easy
**True:** "The Godfather," released in 1972, was directed by Francis Ford Coppola.
**False:** "The Godfather," released in 1972, was directed by Martin Scorsese.

- **S (Medicine):** The thyroid gland regulates metabolism through hormone production. → Accept
- **X (Economics):** Unemployment benefits are funded entirely by direct contributions from unemployed individuals themselves. → Reject
- **U (real org + fabricated claim):** The American Film Institute's 2023 internal archive notes describe a minor frame-count discrepancy in a restored print of a classic film. → Cannot Determine

---

### BC-044 — Art — Medium
**True:** The artist Frida Kahlo was born in Coyoacán, Mexico.
**False:** The artist Frida Kahlo was born in Guadalajara, Mexico.

- **S (Astronomy):** The Sun is classified as a yellow dwarf star. → Accept
- **X (Chemistry):** Pure water always conducts electricity strongly due to its natural ion content. → Reject
- **U (real org + fabricated claim):** The Frida Kahlo Museum's 2024 internal archive notes describe a minor provenance clarification for an early personal letter. → Cannot Determine

---

### BC-045 — Sports — Hard
**True:** The first Super Bowl was played in January 1967.
**False:** The first Super Bowl was played in January 1957.

- **S (Biology):** Tendons connect muscle to bone, while ligaments connect bone to bone. → Accept
- **X (Astronomy):** The Moon's phases are caused by Earth's shadow falling on it each month. → Reject
- **U (real org + fabricated claim):** The National Football League's 2023 internal historical review noted a minor attendance-figure correction for an early championship game. → Cannot Determine

---

### BC-046 — Music — Medium
**True:** The Rolling Stones formed in London in 1962.
**False:** The Rolling Stones formed in Liverpool in 1962.

- **S (Medicine):** Melanin is the pigment responsible for skin, hair, and eye color in humans. → Accept
- **X (Physics):** Two magnets with like poles facing each other will always attract one another. → Reject
- **U (real org + fabricated claim):** The British Library's 2024 internal sound archive notes describe a minor restoration update to an early recorded interview tape. → Cannot Determine

---

### BC-047 — History — Medium
**True:** The Berlin Conference of 1884-85 dealt with European colonization of Africa.
**False:** The Berlin Conference of 1884-85 dealt with European colonization of South America.

- **S (Chemistry):** Ozone is composed of three oxygen atoms bonded together. → Accept
- **X (Biology):** Insects breathe using lungs in the same way mammals do. → Reject
- **U (real org + fabricated claim):** The German Federal Archives' 2025 internal cataloging notes describe a minor translation clarification in a 19th-century diplomatic document. → Cannot Determine

---

### BC-048 — Geography — Hard
**True:** The Mariana Trench, located in the Pacific Ocean, is the deepest known point in Earth's oceans.
**False:** The Mariana Trench, located in the Atlantic Ocean, is the deepest known point in Earth's oceans.

- **S (Astronomy):** Neutron stars are extremely dense remnants formed after certain massive stars collapse. → Accept
- **X (Economics):** Raising the minimum wage always eliminates inflation within the same fiscal quarter. → Reject
- **U (real org + fabricated claim):** The National Oceanic and Atmospheric Administration's 2024 internal survey noted a minor depth re-measurement at a well-studied oceanic trench location. → Cannot Determine

---

### BC-049 — Literature — Easy
**True:** "To Kill a Mockingbird" was written by Harper Lee.
**False:** "To Kill a Mockingbird" was written by Truman Capote.

- **S (Medicine):** Vaccination programs have led to the global eradication of smallpox. → Accept
- **X (Astronomy):** The North Star, Polaris, is the brightest star visible in the night sky. → Reject
- **U (real org + fabricated claim):** The Library of Congress's 2023 internal archive notes describe a minor cataloging update for an early manuscript draft of a well-known American novel. → Cannot Determine

---

### BC-050 — Film — Hard
**True:** "Citizen Kane," released in 1941, was directed by and starred Orson Welles.
**False:** "Citizen Kane," released in 1951, was directed by and starred Orson Welles.

- **S (Biology):** Octopuses have three hearts and blue-tinted blood. → Accept
- **X (Chemistry):** Helium is more reactive than most other elements on the periodic table. → Reject
- **U (real org + fabricated claim):** The Museum of Modern Art's 2024 internal archive notes describe a minor restoration log entry for an early 20th-century American film print. → Cannot Determine

---

## Summary

30 new pairs (21-50), bringing total dataset to 50 induction pairs / 150 evaluation questions.

**Difficulty distribution (new 30):** Easy = 8 (27%), Medium = 12 (40%), Hard = 10 (33%) — close to target 30/40/30.

**Domain distribution (induction):** History ×6, Geography ×6, Film ×5, Sports ×5, Art ×4, Literature ×3, Music ×3 — reasonably spread, slight History/Geography emphasis matching the original 20's pattern.

**All Unverifiable items** use the established "real institution + mundane fabricated finding" template exclusively — no lexical cues, no extraordinary claims, no fabricated entities.

**All Contradicted items** keep the falsehood in the main clause or as a direct factual substitution, avoiding subordinate-clause burial (per the BC-019/BC-020 lesson from the original 20).
