# Changelog

All notable IntelGram custom-feature changes are recorded here.

## IntelGram v6.7.8 Local Profile Update - 2026-07-19

### Added

- A native visual collection gallery that replaces the text-only collectible collection list.
- A scrollable in-app gallery of exact numbered collectibles; clicking artwork selects it locally without opening Getgems.
- Pink IntelGram primary and profile-art icons plus twelve coordinated color variants for macOS, Windows, and Linux.
- A native in-app update log with the latest changes, main feature summary, privacy boundary, project credit, and full-changelog action.
- IntelGram Telegram, GitHub, changelog, and technical changelog links inside the app.
- A local supporter badge derived from membership in `@intelgrams` after the user joins through Telegram's normal channel page.
- A detailed technical changelog covering source hooks, persistence, network boundaries, and validation.
- Live collection chooser populated from Telegram's complete read-only star-gift catalog.
- Native visual collection tiles with an eight-collection offline fallback.
- Scrollable exact-number collectible browser with incremental loading.
- Local cached-peer search by UID or visible phone number in the main chat-list search field.
- `Found by ID or phone` result heading and normal profile-row interaction.
- Clone fidelity for premium and verification badges, organization badge symbols, emoji status, and personal channels.
- Complete feature inventory, conversational feature guide, and build update log.

### Changed

- Reorganized the local-profile page into identity, contact, photo, and collectible sections.
- Restored the familiar inline username-status row and removed the added original-username strip from the local editor; the status remains local and performs no Telegram availability request.
- Cloned badge, status, and personal-channel elements now disappear locally when the source profile lacks them instead of falling back to the real self profile.
- Clone selection now refreshes the already-known source user's full profile read-only so visible badge and personal-channel metadata is ready for local rendering.
- The name-color preview now follows the active locally rendered display name instead of the real-profile short name.
- Rebuilt every Windows icon as a seven-size `.ico` and added matching native macOS and Linux assets.
- Removed the inherited Boosty and cryptocurrency donation block from **Settings -> Other**.
- Collection thumbnails now come from Telegram's read-only catalog, with read-only sample resolution as a fallback for established collections.
- UID and phone queries now stay inside the local peer cache instead of entering normal remote message, topic, or username search.
- Main README now leads with IntelGram's custom features and links to the full documentation.
- Product-facing main-window, settings, version, and notification-preview titles now consistently use IntelGram.
- Completed the visible branding pass across the login footer, platform menus, About and crash dialogs, tray labels, updater identity, and Windows shortcut and installer metadata.
- The final Windows Qt dependency stage now runs serially to avoid a generated-directory race in `qtimageformats`.

### Privacy

- No automatic channel join was added; `@intelgrams` membership requires the user's normal Telegram **Join** action.
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
