# IntelGram Icon Assets

This directory contains the source and generated application icons used by `build_intelgram_branding.py`.

## Character Artwork

- `character/source`: supplied pink front and profile artwork.
- `character/masters`: normalized 1024px transparent masters.
- `character/Windows`: seven-size `.ico` files.
- `character/macOS`: `.icns` files.
- `character/Linux/hicolor`: desktop icon sizes from 16px through 1024px.

The pink front artwork is IntelGram's primary application icon. The profile artwork is the first alternate choice in the in-app icon picker.

## Color Variants

`color/masters` contains the twelve supplied 1024px color designs. Their Windows, macOS, and Linux folders contain generated platform-native resources. The in-app picker exposes all twelve after the two pink character choices.

## Regeneration

Run `generate_intelgram_character_icons.py` from the repository root with Pillow installed. It rebuilds both character icons and every color variant without altering the source artwork.
