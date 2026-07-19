# IntelGram Technical Changelog

This file records implementation-level changes to IntelGram's custom layer. Product-facing changes are summarized in [`CHANGELOG.md`](CHANGELOG.md).

## Unreleased - 2026-07-18

### Source Baseline And Patch

- Upstream source: official AyuGram Desktop `v6.7.8`, commit `b25513a06ff88be0b3f4c928252b56c3da39cec7`, with required submodules.
- Delivery patch: [`intelgram-local-profile-render-overrides.patch`](intelgram-local-profile-render-overrides.patch).
- Compatibility alias: [`ayugram-local-profile-render-overrides.patch`](ayugram-local-profile-render-overrides.patch), byte-for-byte identical.
- Patch SHA-256: `5039d065566b88f94918fd1972fd0dda7a6817ddb15aeece06ffc0c9ff16e764`.
- Patch footprint: 28 source files, 2,848 insertions, and 373 deletions relative to the local baseline snapshot.

### Collectible Chooser Reliability

- `ShowLocalGiftCollectionPicker` now creates stable collection rows immediately from `LocalGiftCollections()` before starting any catalog request.
- The stable rows use the existing settings button and premium-gift icon styles, so the chooser remains navigable when catalog requests fail or return no resell titles.
- `LoadLocalGiftCollections` still requests Telegram's read-only star-gift catalog and feeds native `Ui::MakeGiftsList` tiles below the stable choices.
- `ShowLocalGiftCollectionBrowser` resolves exact numbered slugs in pages of 12 and appends them to the native gift grid for scrolling.
- Exact gift resolution remains `MTPpayments_GetUniqueStarGift`; raw TON NFT addresses may use a read-only TonAPI metadata GET before resolving the Telegram slug.

### Settings And Project Links

- Removed `BuildDonations` and its Boosty, TON, Bitcoin, Ethereum, Solana, and Tron rows from **Settings -> Other**.
- Added first-party rows for `@intelgrams`, `foolspec/IntelGram`, `CHANGELOG.md`, and `TECHNICAL_CHANGELOG.md`.
- The Telegram row calls `Window::SessionController::showPeerByLink` and leaves joining to Telegram's normal channel UI.
- External documentation rows use `QDesktopServices::openUrl` with explicit GitHub URLs.

### Consent-Based Supporter Badge

- `isIntelGramChannelMember` checks the already-loaded `@intelgrams` peer through `Data::Session::peerByUsername` and `ChannelData::amIn`.
- `isSupporterPeer(not_null<PeerData*>)` combines existing upstream supporter data with the local IntelGram membership-derived state for the user's own peer.
- `ExteraBadgeTypeFromPeer` merges its initial badge value with `Data::PeerUpdate::ChannelAmIn` and `Username` updates, allowing the badge to react after a normal join or leave.
- Existing badge renderers in the settings cover, main menu, profile top bar, and unread badge path now use the peer-aware supporter check.
- Clicking the IntelGram supporter badge opens `@intelgrams`; it does not call a join method.
- No `MTPchannels_JoinChannel`, automatic join, background subscription, or other channel mutation was added.

### Local Profile Architecture

- `AyuSettings` persists enable flags and normalized local values for display name, UID, usernames, anonymous number, bio, photo path, clone UID, featured gift, and pinned gifts.
- `Ayu::LocalProfileNameValue`, `LocalProfileIdValue`, `LocalProfileUsernameValue`, `LocalProfileUsernamesValue`, `LocalProfilePhoneValue`, and `LocalProfileAboutValue` provide the reactive render values.
- `Ayu::LocalProfilePhotoImage`, `LocalProfileUserpicActive`, `LocalProfileEmojiStatusId`, and `LocalProfileGiftReferencesValue` supply local photo, clone, emoji-status, and collectible presentation data.
- `Ayu::RefreshLocalProfilePresentation` emits existing peer update flags so already-open UI surfaces redraw without a Telegram profile update.
- `PeerData` userpic paths and targeted dialog, history, settings, profile, table-row, and main-menu call sites consume the local values only when the rendered peer is the signed-in user.

### Search And Clone Boundaries

- UID and phone search use `Data::Session::userLoaded` and `userByPhone`, limiting results to peers already present in the local session cache.
- Recognized UID/phone input bypasses normal remote username and message search for that query.
- Profile cloning accepts only a loaded non-self user and locally mirrors visible cached fields; it does not fetch private data or alter either account.

### Validation

- `git diff --check` passes.
- Both patch filenames have identical SHA-256 digests.
- Clean patch application and reverse-application checks pass against the pinned baseline snapshot.
- Added-line scans find no channel-join, profile-update, contact-import, gift-transfer, sale, purchase, or ownership mutation request.
- The only custom network paths are read-only collectible catalog/detail resolution and optional read-only TON NFT metadata resolution.
- A full local build was intentionally not run because the upstream repository's `AGENTS.md` says to avoid building the project.

### Release State

- The current source patch and the latest published package patch are tracked with separate hashes in `intelgram-release-validation.yml`.
- This prevents the release badge from claiming that an unreleased source revision is already inside the downloadable packages.
- The latest published packages remain the previously validated release from build run `29615304415`; this unreleased entry describes the source revision that follows it.

## Initial IntelGram Local Profile Implementation

### Rendering

- Added centralized own-user render helpers and reactive values instead of changing Telegram's stored `UserData` profile fields.
- Routed local presentation through the settings cover, main menu, dialog rows, search results, chat and profile headers, messages, replies, forwarded previews, about rows, table rows, and avatar paths.
- Preserved normal Telegram rendering for every other peer.

### Local Fields And Collectibles

- Added local display name, UID, primary and secondary usernames, anonymous number, bio, profile photo, cached-profile cloning, featured collectible, and up to six pinned collectibles.
- Added the original Telegram username reference to the local username editor.
- Used Telegram's native unique-gift model, artwork, tooltip, and detail surfaces for resolved collectibles.

### Packaging

- Added deterministic product-facing IntelGram branding and separate macOS, Windows, and Linux application identifiers.
- Added GitHub workflows for clean-source patch verification, platform packaging, launch smoke tests, checksums, release publication, and release validation.
