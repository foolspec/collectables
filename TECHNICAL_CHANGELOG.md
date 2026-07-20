# IntelGram Technical Changelog

This file records implementation-level changes to IntelGram's custom layer. Product-facing changes are summarized in [`CHANGELOG.md`](CHANGELOG.md).

## IntelGram v6.7.8 Local Profile Update - 2026-07-19

### Source Baseline And Patch

- Upstream source: official AyuGram Desktop `v6.7.8`, commit `b25513a06ff88be0b3f4c928252b56c3da39cec7`, with required submodules.
- Delivery patch: [`intelgram-local-profile-render-overrides.patch`](intelgram-local-profile-render-overrides.patch).
- Compatibility alias: [`ayugram-local-profile-render-overrides.patch`](ayugram-local-profile-render-overrides.patch), byte-for-byte identical.
- Patch SHA-256: `56e12dad016d54f7c7f917409fba34c4ca935ba746b261ac8383ed710b9762e9`.
- Patch footprint: 37 source files, 3,183 insertions, and 432 deletions relative to the local baseline snapshot.

### Native Collectible Galleries

- `ShowLocalGiftCollectionPicker` uses `Ui::MakeGiftsList` as the primary collection surface instead of generating text-only settings rows.
- `LoadLocalGiftCollections` requests Telegram's read-only star-gift catalog and maps each resell title to a clickable native collection tile.
- `LoadLocalGiftCollectionFallback` resolves one read-only sample from each established collection when the catalog does not provide usable collection tiles.
- `ShowLocalGiftCollectionBrowser` resolves exact numbered slugs in pages of 12, appends them to a scrollable native gift grid, and stores the clicked gift reference locally.
- Exact gift resolution remains `MTPpayments_GetUniqueStarGift`; raw TON NFT addresses may use a read-only TonAPI metadata GET before resolving the Telegram slug.

### Settings And Preview Organization

- `BuildLocalProfile` now separates clone controls, identity, usernames/bio/contact, profile photo, and collectibles with native subsection headings and dividers.
- Removed the duplicate collectible-browser action; featured and pinned flows both enter the same native collection gallery.
- `SetupPeerColorSample` now consumes `Ayu::LocalProfileNameValue(peer)`, so the name-color preview reacts to the local display-name setting and clone state.

### Local Gift Detail Presentation

- `Core::ResolveAndShowUniqueGiftForLocalProfile` reuses the existing read-only unique-gift resolver and Telegram detail box for locally featured, pinned, and cloned collectibles.
- The resolver deep-copies the fetched `Data::UniqueGift` presentation object and substitutes only `originalDetails.recipientId` with the signed-in peer for the local detail view.
- `StarGiftResaleInfo::localProfileRecipientId` overrides only the detail entry's displayed Telegram host peer, so the native Telegram profile chip uses the same signed-in peer while the unique gift's actual `hostId` and `ownerId` remain intact.
- The recipient label and peer-table value consume `Ayu::LocalProfileName`, so they show the real display name when no local name is enabled and the local or cloned display name when one is active.
- `TopBar` compares configured local gift slugs case-insensitively before asynchronous collectible IDs resolve, routing featured and pinned local gifts through the local-profile detail resolver immediately.
- Telegram's existing click handlers therefore open the signed-in user's short profile from either surface. `PrepareShortInfoBox` consumes `LocalProfileName`, `LocalProfilePhone`, `LocalProfileUsername`, `LocalProfileAbout`, and `LocalProfilePersonalChannel`; when a local or cloned userpic is active, `ProcessCurrent` bypasses the real Telegram photo-history item and renders the central override as the card's single large, fully loaded photo instead of a blurred server-photo placeholder.
- Locally overridden usernames are shown without linking to an unrelated public server username; normal non-local username links remain unchanged.
- `ownerId`, sender, date, price, transfer, resale, and every underlying Telegram or on-chain ownership field remain unchanged. Normal non-local gift details continue through the original resolver.

### Profile Clone Fidelity And Username Editor

- `BadgeValue` dynamically switches its render source to `Ayu::LocalProfileCloneUser`, mirroring premium, verified, scam, and fake badge state without changing `UserData` or session entitlements.
- `BotVerifyBadgeForPeer` uses the same reactive clone source so organization verification symbols follow the cloned profile.
- `Ayu::LocalProfilePersonalChannelValue`, `LocalProfilePersonalChannel`, and `LocalProfilePersonalChannelMessageId` drive the own-profile personal-channel block from the clone, including the channel message preview.
- A clone with no personal channel produces `nullptr`, which hides the block even when the real self profile has a channel; cloned-channel edit context actions are suppressed.
- `ShowLocalProfileCloneBox` calls the existing `requestFullPeer` read path after selecting an already-loaded user so visible full-profile badge and personal-channel fields are refreshed without changing either account.
- `ShowLocalProfileUsernameEditor` again uses `AddUsernameCheckLabel` with Telegram's native styling. Its syntax result is computed locally and never calls `MTPaccount_CheckUsername` or a username update method.
- Removed the added `Original Telegram username` strip and its localization keys.

### Cross-Platform Icon Assets

- `build_intelgram_branding.py` installs a pink primary icon, a pink profile-art alternate, and twelve color variants into the existing runtime icon picker.
- The icon generator produces 1024px masters, seven-size Windows `.ico` files, macOS `.icns` and `.icon` resources, and Linux hicolor assets from 16px through 1024px.
- macOS icon-composer packages now use dedicated opaque full-bleed PNGs at `1.0` scale. Character sources keep their native platform background and color variants flatten transparent corners to the icon's sampled background, preventing Icon Composer from adding a visible white shell behind an already-rounded image.
- The primary application icon, installer resources, alternate macOS icon list, Qt resources, and picker constants are generated together from `branding/icons`.
- Stored use of the retired duplicate `chibi2` picker slot migrates to the new primary icon.

### Settings And Project Links

- Removed `BuildDonations` and its Boosty, TON, Bitcoin, Ethereum, Solana, and Tron rows from **Settings -> Other**.
- Added first-party rows for `@intelgrams`, the bundled update log, `foolspec/IntelGram`, `CHANGELOG.md`, and `TECHNICAL_CHANGELOG.md`.
- The Telegram row calls `Window::SessionController::showPeerByLink` and leaves joining to Telegram's normal channel UI.
- External documentation rows use `QDesktopServices::openUrl` with explicit GitHub URLs.

### In-App Update Log

- `ShowIntelGramUpdateLog` opens an existing `Ui::GenericBox` from the IntelGram settings page.
- The bundled localized content is split into latest-update, main-feature, privacy-boundary, and credit sections using `Ui::AddSubsectionTitle` and `Ui::AddDividerText`.
- The dialog requires no network access to display its update summary.
- An explicit **View full changelog** action opens `CHANGELOG.md` on GitHub for the complete history.
- Included `lang/lang_text_entity.h` directly so the update log's `tr::rich` formatter compiles on every supported platform.
- The multiplatform workflow checks for `ShowIntelGramUpdateLog` after applying the source patch.

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
- `Ayu::LocalProfilePhotoImage`, `LocalProfileUserpicActive`, `LocalProfileEmojiStatusId`, `LocalProfilePersonalChannelValue`, and `LocalProfileGiftReferencesValue` supply local photo, clone, badge-adjacent, personal-channel, emoji-status, and collectible presentation data.
- `Ayu::RefreshLocalProfilePresentation` emits existing peer update flags so already-open UI surfaces redraw without a Telegram profile update.
- `PeerData` userpic paths and targeted dialog, history, settings, profile, table-row, and main-menu call sites consume the local values only when the rendered peer is the signed-in user.

### Search And Clone Boundaries

- UID and phone search use `Data::Session::userLoaded` and `userByPhone`, limiting results to peers already present in the local session cache.
- Recognized UID/phone input bypasses normal remote username and message search for that query.
- Profile cloning accepts only a loaded non-self user, refreshes that user's normally visible full profile read-only, and locally mirrors visible fields, badges, emoji status, and personal channel; it does not fetch hidden data or alter either account or channel.

### Validation

- Manual workflow runs can target `linux`, `macos`, `windows`, or `all`; platform-scoped concurrency lets compile checks run without cancelling unrelated dependency preparation.
- A Windows-only run can reuse the exact final dependency cache from a completed run ID and attempt, skipping all nine preparation jobs while preserving the final-cache marker check.
- `git diff --check` passes.
- Both patch filenames have identical SHA-256 digests.
- Clean patch application and reverse-application checks pass against the pinned baseline snapshot.
- Added-line scans find no channel-join, profile-update, contact-import, gift-transfer, sale, purchase, or ownership mutation request.
- The only custom network paths are the standard read-only full-peer refresh after clone selection, read-only collectible catalog/detail resolution, and optional read-only TON NFT metadata resolution; local recipient presentation reuses the same detail response without sending any write request.
- A full local build was intentionally not run because the upstream repository's `AGENTS.md` says to avoid building the project.

### Release State

- Release validation compares the current source and release patch hashes, downloads every package, runs each published checksum file, and checks GitHub's package digests against those checksums.
- Temporary validation copies normalize platform-native checksum and report line endings before GNU checksum verification.
- Every platform validation report must record the current patch hash and a passed launch smoke test; all launch logs and packaging inputs must also be present.
- The manual release publisher accepts separate successful macOS, Windows, and Linux run IDs, verifies each required package and validation report, and combines them into one permanent release.
- Release notes enumerate the main local-only features, supported packages, explicit supporter-join behavior, privacy boundary, credit, and links to both changelogs.
- A launch test that produces no console output is retained as an explicit silent-launch success log instead of being omitted from release assets.
- Release `intelgram-v6.7.8-local-profile-20260719` combines successful macOS run `29687992660`, Windows run `29675428988`, and Linux run `29675433095`; each package records patch `049ebb3c864a40819fe22110d1256dfc1785825e9cdee8e38c31c238a64399f3` and a passed launch smoke test before publication, and public-asset validation run `29696979425` passed.

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
