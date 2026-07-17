# Changelog

All notable IntelGram custom-feature changes are recorded here.

## Unreleased

### Added

- Live collection chooser populated from Telegram's complete read-only star-gift catalog.
- Native visual collection tiles with an eight-collection offline fallback.
- Scrollable exact-number collectible browser with incremental loading.
- Local cached-peer search by UID or visible phone number in the main chat-list search field.
- `Found by ID or phone` result heading and normal profile-row interaction.
- Complete feature inventory, conversational feature guide, and build update log.

### Changed

- UID and phone queries now stay inside the local peer cache instead of entering normal remote message, topic, or username search.
- Main README now leads with IntelGram's custom features and links to the full documentation.
- Product-facing main-window, settings, version, and notification-preview titles now consistently use IntelGram.
- Completed the visible branding pass across the login footer, platform menus, About and crash dialogs, tray labels, updater identity, and Windows shortcut and installer metadata.
- The final Windows Qt dependency stage now runs serially to avoid a generated-directory race in `qtimageformats`.

### Privacy

- No Telegram profile/account mutation was added.
- No contact import or address-book lookup was added.
- Collectible catalog, item, and TON metadata resolution remains read-only.

## Initial IntelGram Local Profile Release

### Added

- IntelGram product and package identity for macOS, Windows, and Linux.
- Local name, UID, primary username, other usernames, anonymous number, bio, and profile photo.
- Original Telegram username reference in the local username editor.
- Local profile cloning by the UID of an already-loaded user.
- Local featured and pinned collectible rendering with native gift details.
- Central own-user avatar override and broad name/profile render hooks.
- Automated patch validation, mutation scanning, launch smoke testing, checksums, and release packaging.
