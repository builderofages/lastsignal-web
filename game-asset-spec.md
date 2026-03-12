# Last Signal — Game Asset Specification

**Version:** 1.0 | **Updated:** March 2026 | **Engine:** Unity 6.3 LTS (URP 2D)
**Resolution:** 1080×1920 portrait | **Format:** PNG with transparency (unless noted)

---

## Asset Pipeline Overview

All sprites are loaded at runtime via `SpriteFactory.cs` with procedural fallback generation. Assets go in `Assets/Sprites/{category}/` and are loaded via `Resources.Load`. The procedural system generates colored geometric shapes when files are missing — this is the current state of the game.

**Priority Tiers:**
- **P0 (Launch Blocker):** Player heroes, core enemies, basic UI, pickups
- **P1 (Soft Launch):** Bosses, weapons, projectiles, pets
- **P2 (Post-Launch):** Costumes, environment variants, collectibles, VFX

---

## 1. HEROES (P0) — 30 Sprites

**Path:** `Assets/Sprites/Players/hero_{name}.png`
**Size:** 256×256px | **Style:** Top-down, facing up, slight 3/4 angle

| # | Sprite Name | Visual Concept |
|---|------------|----------------|
| 1 | hero_signal_keeper | Default hero. Glowing cyan beacon core, armored suit, signal ring halo |
| 2 | hero_axel | Aggressive bruiser, red energy gauntlets, heavy armor |
| 3 | hero_nexus | Tech wizard, floating data nodes orbit body, purple glow |
| 4 | hero_kross | Dual-wielding gunslinger, orange energy trails |
| 5 | hero_vex | Shadow assassin, dark silhouette with magenta eye slits |
| 6 | hero_prism | Crystal armor, refracts light into rainbow edges |
| 7 | hero_nova | Fire-type, solar corona emanating from body |
| 8 | hero_wraith | Ghost-like, semi-transparent, green ectoplasm trails |
| 9 | hero_zara | Speed runner, wind streaks, aerodynamic suit |
| 10 | hero_xenith | Alien hybrid, bio-organic armor, teal bioluminescence |
| 11 | hero_echo | Sound-based, concentric ripple aura, speaker-like helmet |
| 12 | hero_oblivion | Void knight, black hole core, gravity distortion |
| 13 | hero_sable | Stealth ops, matte black, single red visor |
| 14 | hero_viper | Poison-type, green scales, dripping acid |
| 15 | hero_lyra | Healing support, golden light, wings of energy |
| 16 | hero_grimm | Death theme, scythe silhouette, skull mask |
| 17 | hero_zyra | Plant/nature, thorny vines wrap body |
| 18 | hero_mantis | Insectoid, blade arms, compound eye visor |
| 19 | hero_raze | Demolition, explosive packs, heavy ordnance |
| 20 | hero_nyx | Night themed, star-speckled cloak, crescent symbol |
| 21 | hero_kael | Ice knight, frost crystals, cold blue glow |
| 22 | hero_chimera | Shape-shifter, multi-form silhouette, unstable edges |
| 23 | hero_flux | Time manipulator, clock gears, temporal distortion |
| 24 | hero_solara | Solar priest, golden armor, sun disk crown |
| 25 | hero_havoc | Chaos berserker, cracked armor, red lightning |
| 26 | hero_cipher | Code warrior, matrix-style data cascade body |
| 27 | hero_titan | Giant mech suit, massive frame, cyan core |
| 28 | hero_aurora | Northern lights, flowing energy ribbons |
| 29 | hero_blitz | Electric speedster, lightning bolt form |
| 30 | hero_nexar | Final unlock, cosmic entity, galaxy swirl body |

---

## 2. ENEMIES (P0) — 40 Base Types × 5 Tiers = 200 Sprites

**Path:** `Assets/Sprites/Enemies/enemy_{type}_t{1-5}.png`
**Size:** 128×128px (t1-t3), 192×192px (t4-t5)
**Tiers:** Each tier adds visual complexity — more detail, glow effects, armor plates

### Original 16 Types

| Type | Visual Concept |
|------|---------------|
| zombie_alien | Shambling humanoid, exposed circuitry, green glow |
| swarm_drone | Small insect-bot, wings, swarm behavior indicator |
| toxic_slime | Amorphous blob, acid drip particles, green |
| shadow_crawler | Spider-like, low profile, purple shadow trail |
| mutant_soldier | Humanoid, corrupted armor, weapon arm |
| plasma_turret | Stationary, rotating barrel, energy buildup glow |
| crystal_golem | Rocky body, embedded crystals, slow but massive |
| void_wraith | Ghostly, elongated, phasing in/out effect |
| fire_elemental | Flame body, ember particles, orange/red |
| ice_beast | Frozen quadruped, ice crystal spikes, blue |
| acid_spitter | Ranged, distended jaw, green projectile gland |
| mech_walker | Bipedal robot, heavy plating, red eye |
| dark_templar | Cloaked warrior, dark energy blade, intimidating |
| brood_queen | Large, spawns minions, egg sac visible |
| siege_tank | Armored vehicle, cannon turret, treads |
| alien_overlord | Elite, tentacles, commanding presence, purple |

### 24 New Types

| Type | Visual Concept |
|------|---------------|
| nano_swarm | Cloud of tiny bots, shifting form |
| spore_cloud | Floating fungal body, poison particle aura |
| gravity_leech | Spherical, pulls nearby objects, dark vortex |
| phase_shifter | Flickering between dimensions, glitch effect |
| laser_sentinel | Floating eye, beam weapon, rotating shields |
| shield_drone | Small bot with large energy barrier |
| chain_zombie | Connected to others with energy chains |
| exploding_mite | Tiny, red pulsing glow, suicide bomber |
| venom_stalker | Serpentine, fangs, dripping venom trail |
| frost_wraith | Ice ghost, frozen breath particles |
| thunder_beetle | Armored insect, electric arcs between antennae |
| magma_worm | Segmented, lava glow between segments |
| psychic_eye | Giant floating eye, telekinetic rings |
| bio_titan | Massive organic creature, mutations visible |
| warp_spider | Teleporting spider, portal web patterns |
| null_spectre | Anti-matter ghost, inverts colors around it |
| plague_bat | Flying, disease clouds, tattered wings |
| crystal_serpent | Snake made of crystal segments, refractive |
| iron_goliath | Heavy metal humanoid, riveted plates |
| void_reaver | Aggressive void entity, consuming darkness |
| storm_harpy | Winged, lightning crackling, feathered |
| acid_hydra | Multi-headed serpent, each head different acid |
| mech_centipede | Segmented machine, many legs, drilling head |
| cosmic_horror | Lovecraftian, tentacles, impossible geometry |

---

## 3. BOSSES (P1) — 14 Sprites

**Path:** `Assets/Sprites/Bosses/boss_{name}.png`
**Size:** 384×384px | **Style:** Imposing, detailed, unique silhouette

| Boss Name | Visual Concept |
|-----------|---------------|
| boss_hive_commander | Insectoid general, crown of antennae, swarm around |
| boss_void_sovereign | Regal void entity, cape of darkness, crown of stars |
| boss_crystalline_colossus | Massive crystal humanoid, light refracting |
| boss_primordial_leviathan | Ancient sea-space creature, massive tentacles |
| boss_signal_decay | Corrupted version of player beacon, glitching |
| boss_bio_titan | Enormous organic creature, pulsing weak points |
| boss_iron_goliath | Towering mech, multiple weapon arms |
| boss_cosmic_horror | Eldritch entity, defies geometry, eye clusters |
| boss_acid_hydra | Three-headed serpent, each head glows different |
| boss_void_reaver | Final void boss, consuming everything |
| boss_storm_harpy | Massive winged boss, lightning storm around |
| boss_mech_centipede | Segmented machine boss, arena-wrapping |
| boss_psychic_eye | Giant floating brain-eye, telekinetic debris |
| boss_magma_worm | Lava serpent, erupts from ground segments |

---

## 4. WEAPONS & PROJECTILES (P1)

### Weapon Icons — 40 Sprites
**Path:** `Assets/Sprites/Equipment/weapon_{type}_{rarity}.png`
**Size:** 96×96px

Types: sword, gun, staff, dagger, launcher, shield, gauntlet, scythe
Rarities: common (grey), rare (blue), epic (purple), legendary (gold), mythic (red/black)

### Projectile Sprites — 25 Sprites
**Path:** `Assets/Sprites/Projectiles/proj_{name}.png`
**Size:** 64×64px | **Style:** Bright, high-contrast, motion-suggesting

proj_plasma, proj_gravity, proj_nanoblade, proj_emp_burst, proj_bio_pulse,
proj_solar_flare, proj_singularity, proj_dimensional, proj_mind_shatter, proj_plague,
proj_chain_lightning, proj_frost_nova, proj_mortar, proj_laser_beam, proj_shield_drone,
proj_scatter_shot, proj_homing_missile, proj_tesla_coil, proj_phase_rifle, proj_vortex_grenade,
proj_acid_spray, proj_crystal_lance, proj_warp_mine, proj_flame_wall, proj_shadow_strike

---

## 5. PETS (P1) — 23 Sprites

**Path:** `Assets/Sprites/Pets/pet_{name}.png`
**Size:** 96×96px | **Style:** Cute but sci-fi, follows player

| Pet Name | Visual Concept |
|----------|---------------|
| pet_fury_beast | Small aggressive creature, red, fangs |
| pet_iron_shell | Armored turtle-bot, defensive |
| pet_swarm_locust | Tiny swarm cloud companion |
| pet_war_caller | Tiny drummer bot, buff aura |
| pet_speed_demon | Zippy imp, speed trails |
| pet_blood_hound | Tracking creature, red glow |
| pet_flame_imp | Fire sprite, cute flame body |
| pet_ice_wisp | Floating ice crystal, cool blue |
| pet_lunar_guardian | Moon-themed guardian, silver |
| pet_void_scavenger | Small void creature, collects drops |
| pet_frost_sprite | Snowflake fairy, sparkle trail |
| pet_toxic_maw | Cute poison creature, big mouth |
| pet_storm_hawk | Mini electric bird |
| pet_shadow_cat | Dark cat silhouette, purple eyes |
| pet_crystal_drake | Tiny crystal dragon |
| pet_heal_fairy | Healing sprite, green glow, wings |
| pet_cosmic_jellyfish | Space jellyfish, bioluminescent |
| pet_flame_phoenix | Mini phoenix, fire trail |
| pet_void_wyrm | Small void dragon |
| pet_quantum_sprite | Glitching particle sprite |
| pet_celestial_dragon | Premium — golden dragon |
| pet_abyss_guardian | Premium — dark protector |
| pet_time_weaver | Premium — clock-themed sprite |

---

## 6. PICKUPS (P0) — 6 Sprites

**Path:** `Assets/Sprites/Pickups/{name}.png`
**Size:** 48×48px | **Style:** Bright, readable at small sizes, animated if possible

- xp_gem_blue — Small blue diamond
- xp_gem_green — Green diamond (higher value)
- xp_gem_red — Red diamond (highest value)
- coin_gold — Gold coin, simple shine
- health_orb — Red/pink glowing orb
- treasure_chest — Small chest, glow emanating

---

## 7. UI ELEMENTS (P0)

**Path:** `Assets/Sprites/UI/{subcategory}/{name}.png`

### Essential UI (80+ sprites)
- **Buttons:** btn_primary, btn_secondary, btn_danger, btn_disabled (96×48px)
- **Panels:** panel_dark, panel_light, panel_popup (9-slice, 64×64px)
- **Bars:** hp_bar_fill, hp_bar_bg, xp_bar_fill, energy_bar (variable width)
- **Icons:** icon_attack, icon_defense, icon_speed, icon_health, icon_crit (48×48px)
- **Rarity Frames:** frame_common, frame_rare, frame_epic, frame_legendary, frame_mythic (128×128px)
- **Stars:** star_empty, star_filled, star_half (32×32px)
- **Currency:** icon_gold, icon_gem, icon_shard, icon_energy (48×48px)
- **Navigation:** icon_home, icon_battle, icon_shop, icon_heroes, icon_settings (64×64px)
- **Equipment Slots:** slot_weapon, slot_armor, slot_accessory, slot_empty (96×96px)

---

## 8. ENVIRONMENT / BACKGROUNDS (P2)

**Path:** `Assets/Sprites/Backgrounds/act{1-5}_{theme}_bg{1-5}.png`
**Size:** 1080×1920px (full screen) or 1080×540px (tiling)

### Act Themes
1. **Urban/Tech** — Ruined city, neon signs, broken infrastructure
2. **Nature/Elemental** — Overgrown ruins, crystal caves, elemental zones
3. **Dark/Void** — Shadow dimension, floating debris, void portals
4. **Alien/Organic** — Bio-organic structures, living walls, spore forests
5. **Endgame/Anomaly** — Reality breaking, cosmic anomalies, signal distortion

Each act needs: 1 base background + 4 variants (time of day / weather)

---

## Total Asset Count Summary

| Category | Count | Priority |
|----------|-------|----------|
| Heroes | 30 | P0 |
| Enemies (base × 5 tiers) | 200 | P0 |
| Bosses | 14 | P1 |
| Weapon Icons | 40 | P1 |
| Projectiles | 25 | P1 |
| Pets | 23 | P1 |
| Pickups | 6 | P0 |
| UI Elements | ~80 | P0 |
| Backgrounds | 25 | P2 |
| **TOTAL** | **~443** | — |

---

## Art Style Guidelines

- **Palette:** Match Terminal Radiance — deep space darks (#030712), cyan (#00f0ff), purple (#a855f7), magenta (#f472b6), orange (#fb923c), green (#4ade80)
- **Style:** Semi-realistic with stylized glow effects. High contrast silhouettes readable at small sizes.
- **Glow:** All interactive entities should have colored glow/emission matching their type
- **Consistency:** Top-down perspective, consistent lighting from upper-left
- **File Format:** PNG-32 with alpha channel, power-of-two dimensions preferred
- **Naming:** lowercase_with_underscores, no spaces, no special characters

---

## Recommended Art Production Tools

1. **Higgsfield.ai** — AI image generation (already in pipeline via `process_ai_assets.py`)
2. **Aseprite** — Pixel art if going low-res style
3. **Procreate/Photoshop** — Hand-painted sprites
4. **Stable Diffusion + ControlNet** — Batch generation with style consistency
5. **Spine 2D** — If animation is added later

---

*This spec covers all sprites referenced in the 277 C# scripts of Last Signal. The `SpriteFactory.cs` procedural fallback system means the game runs without these assets, but they are required for a professional release.*
