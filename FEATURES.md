# IntelGram Features

This document covers IntelGram's custom additions. IntelGram also retains the upstream AyuGram Desktop and Telegram Desktop feature sets.

## Local Profile Fields

- Local display name with a dedicated enable switch.
- Local UID with a dedicated enable switch.
- Local primary username and up to 20 other local usernames.
- Original Telegram username shown inside the local username editor for reference.
- Local anonymous number.
- Local bio.
- Local profile photo selected from a file on this device.
- Persistent local settings that survive an IntelGram restart.
- One action to clear each local value and return to the real Telegram-rendered value.

## Local Profile Clone

- Accepts the UID of a user whose profile has already been opened and loaded in IntelGram.
- Mirrors the loaded user's visible name, UID, primary and other usernames, visible phone, bio, profile photo, profile colors, emoji status, and featured collectible.
- Applies the mirror only to your own local profile rendering.
- Can be stopped at any time to return to the individual local fields.
- Does not fetch a hidden profile, bypass privacy, alter either account, or impersonate the user to anyone else.

## UID And Phone Search

- Paste a numeric UID, `id: UID`, or `id UID` into the normal chat-list search field.
- Paste a visible phone number with common spaces, parentheses, periods, or dashes.
- Numeric text attempts both UID and phone matching, with duplicate results removed.
- Results use the existing dialog peer row and open the normal profile when selected.
- Lookup is limited to peers already loaded by IntelGram and phone numbers already visible to your account.
- Recognized UID and phone searches bypass remote message, topic, and username search requests.
- No contact import, address-book sync, username resolution bot, or profile mutation is added.

## Collectible Browser

- Opens directly into a native visual gallery of collection thumbnails inside IntelGram.
- Loads all collection types currently returned by Telegram's read-only star-gift catalog.
- Falls back to read-only sample lookups for Scared Cat, Plush Pepe, Toy Bear, Chill Flame, Precious Peach, Heart Locket, Diamond Ring, and Astral Shard when the catalog omits collection tiles.
- Opens a scrollable native item grid for the selected collection.
- Loads exact numbered collectibles in pages as the user scrolls.
- Selects a collectible by clicking its artwork, without opening Getgems or leaving IntelGram.
- Accepts a collection number, Telegram gift slug, `t.me/nft` link, Getgems item URL, friendly or raw TON NFT address.
- Resolves exact model, pattern, backdrop, number, and native artwork read-only.
- Uses Telegram's native unique-gift detail surface when a rendered collectible is clicked.
- Supports one local featured collectible and up to six local pinned collectibles.
- Uses the featured collectible for the local profile backdrop and places pinned gifts around the local avatar.
- Never changes ownership, transfers, lists, purchases, upgrades, pins, or features a gift on Telegram.

## Render Coverage

- Settings account cover and profile rows.
- Main menu identity and account switcher rows.
- Dialog list rows, avatars, video-userpic fallbacks, and search results.
- Chat headers, profile headers, top bars, about sections, service text, messages, forwarded/reply previews, and table rows.
- Own-profile username, UID, phone, bio, photo, colors, emoji status, featured gift, backdrop, and pinned-gift visuals.
- Native collectible tooltip and detail interaction.

## Product And Packaging

- Visible IntelGram product name.
- In-app links to `@intelgrams`, the IntelGram GitHub repository, and both changelogs.
- Bundled native update log covering the latest changes, main features, privacy boundary, and project credit.
- Optional local supporter badge after the user explicitly joins `@intelgrams` through Telegram's channel page.
- Grouped local-profile controls for identity, contact details, profile photo, and collectibles.
- A reactive name-color sample that follows the locally rendered display name.
- New pink IntelGram primary and profile-art icons plus twelve color variants, with platform-native macOS, Windows, and Linux resources.
- Separate macOS bundle identifier, Windows application identifier, and Linux desktop identifiers.
- Packages for macOS Apple Silicon, Windows x64, and Linux x64.
- Coexists with a normal AyuGram installation without overwriting it.
- Automated clean-source patch verification, mutation-reference scan, launch smoke tests, checksums, and release packaging.

## Network Boundary

IntelGram's custom profile values stay local. The collectible browser may issue read-only Telegram gift catalog/detail requests and a read-only TonAPI metadata lookup when resolving a raw TON NFT address. The supporter badge reads an already-known channel membership state and does not join a channel. IntelGram adds no Telegram account/profile update, contact import, collectible transaction, ownership mutation, or automatic channel join.

## Credit

IntelGram local profile and collectible tools by **fool**. Upstream AyuGram Desktop and Telegram Desktop attribution and licenses are preserved.
