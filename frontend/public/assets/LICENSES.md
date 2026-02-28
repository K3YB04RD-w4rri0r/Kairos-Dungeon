# Asset Licenses

All visual assets in this directory are derived from CC0 (public domain) source packs. No attribution is legally required, but we credit the original creators below.

## Source Packs

### 1. Dungeon Crawl Stone Soup (DCSS) Tileset
- **URL:** https://opengameart.org/content/dungeon-crawl-32x32-tiles
- **License:** CC0 1.0 Universal (Public Domain)
- **Author:** Various contributors to the Dungeon Crawl Stone Soup project
- **Used for:** Creature base sprites (biped, quadruped, serpent, insect, blob, winged), boss base, floor tiles, wall tiles

### 2. 0x72 DungeonTileset II v1.7
- **URL:** https://0x72.itch.io/dungeontileset-ii
- **License:** CC0 1.0 Universal (Public Domain)
- **Author:** 0x72 (Robert)
- **Used for:** Hero base sprite

### 3. Kenney Tiny Dungeon
- **URL:** https://kenney.nl/assets/tiny-dungeon
- **License:** CC0 1.0 Universal (Public Domain)
- **Author:** Kenney (kenney.nl)
- **Used for:** Supplementary icons and gap-filling (available but not used in current MVP)

### 4. Kenney Roguelike Caves & Dungeons
- **URL:** https://kenney.nl/assets/roguelike-caves-dungeons
- **License:** CC0 1.0 Universal (Public Domain)
- **Author:** Kenney (kenney.nl)
- **Used for:** Additional wall/cave variants (available but not used in current MVP)

## Transformations Applied

All source assets were transformed via the processing pipeline in `tools/assets/`:
- Nearest-neighbor upscaling (32->48px creatures, 32->64px tiles, 16->48px hero)
- Flesh palette normalization (4-tone grayscale mapping)
- 1px dark outline addition (#1A1A2A)
- Animation frame generation from static poses (bob, shift, rotation, opacity)
- Hero palette-swap marker color replacement
- Programmatic generation of all effects, particles, and UI elements

## Programmatically Generated Assets

The following assets were generated entirely in code (no external source):
- All 24 effect sprites and particles (`effects/`)
- All 18 UI elements (`ui/`)
- Most tile variants (procedurally generated dungeon tiles)

These programmatic assets are original works and carry no license restrictions.
