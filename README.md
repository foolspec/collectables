# IntelGram

IntelGram is a cross-platform AyuGram Desktop build focused on local-only profile customization.

[![IntelGram release validation](https://github.com/foolspec/IntelGram/actions/workflows/intelgram-release-validation.yml/badge.svg?branch=main)](https://github.com/foolspec/IntelGram/actions/workflows/intelgram-release-validation.yml)

[All features](FEATURES.md) | [Feature guide](FEATURE_GUIDE.md) | [Changelog](CHANGELOG.md) | [Technical changelog](TECHNICAL_CHANGELOG.md) | [Update log](UPDATE_LOG.md)

## Main Features

- Render a local display name, UID, primary username, up to 20 other usernames, anonymous number, bio, and profile photo for your own account.
- Clone the visible profile presentation of a user already loaded in IntelGram by entering their UID.
- Find an already-loaded user by UID or by a phone number that is visible to your account, directly from the normal chat-list search field.
- Browse every collection reported by Telegram's live collectible catalog, inspect exact numbered gifts in a scrollable native grid, and paste Telegram, Getgems, or TON item links.
- Feature one collectible as the local profile backdrop and pin up to six around the local avatar.
- Open the IntelGram community and project links directly from settings, with an optional local supporter badge after you join `@intelgrams` yourself.
- Keep every override client-render-only, with no Telegram profile, ownership, contact, or account mutation.

## Downloads

| Platform | Package |
| --- | --- |
| macOS Apple Silicon | [IntelGram DMG](https://github.com/foolspec/IntelGram/releases/latest/download/IntelGram-macOS-Apple-Silicon.dmg) |
| Windows x64 | [IntelGram ZIP](https://github.com/foolspec/IntelGram/releases/latest/download/IntelGram-Windows-x64.zip) |
| Linux x64 | [IntelGram tar.gz](https://github.com/foolspec/IntelGram/releases/latest/download/IntelGram-Linux-x64.tar.gz) |

[View the latest release, checksums, and validation logs](https://github.com/foolspec/IntelGram/releases/latest).

## Install

- macOS: open the DMG, drag `IntelGram.app` to Applications, then Control-click **Open** on first launch if Gatekeeper asks. The community build is ad-hoc signed, not Apple-notarized.
- Windows: extract `IntelGram-Windows-x64.zip` and run `IntelGram.exe`. Keep the files from the ZIP together.
- Linux: extract `IntelGram-Linux-x64.tar.gz` and run `IntelGram`.

## Using IntelGram

Open **IntelGram Settings -> Other -> Local profile** to configure:

- Local display name
- Local UID
- Local primary username
- Up to 20 local usernames
- Local anonymous number
- Local bio and profile photo
- Local profile cloning by the UID of a user already opened in IntelGram
- A featured collectible gift and up to six pinned collectible gifts

In the main chat-list search field, paste a UID, `id: UID`, or a visible phone number. IntelGram checks only profiles already loaded in this client and shows the matching profile row under **Found by ID or phone**. Phone and UID lookup does not import contacts or send a profile lookup request.

Clicking your username in IntelGram's profile settings opens the local username editor. It displays your original Telegram username for reference before saving the IntelGram-only value.

The collectible picker always opens with a visible list of established collections. Live native preview art loads beneath it when Telegram's read-only catalog is available. Choose a collection to browse real numbered models in a scrollable in-app grid, click one to select it, or paste any supported Telegram gift slug, `t.me/nft` link, Getgems item URL, or TON NFT address. IntelGram resolves the exact collectible read-only, shows its native `Collection #Number` profile tooltip, and uses Telegram's native collectible detail view when clicked.

Choose a local image to replace your own profile photo throughout this IntelGram installation. Profile cloning accepts the UID of a user whose profile has already been opened and locally mirrors their visible name, UID, usernames, phone, bio, photo, profile colors, emoji status, and featured collectible. Stop cloning at any time to return to the individual local fields.

The IntelGram settings page links to [`@intelgrams`](https://t.me/intelgrams), this GitHub repository, and both changelogs. Joining the channel is an explicit Telegram action: open the channel and press Telegram's normal **Join** button. IntelGram then derives the supporter badge from the locally known membership state; it never joins a channel in the background.

## Local Means Local

These controls only change how your own profile is rendered inside this IntelGram installation. They do not change your Telegram display name, photo, bio, username, UID, phone number, emoji status, collectible ownership, or profile data. Other Telegram users do not see the local overrides.

The implementation contains no Telegram account/profile mutation request and no contact import. Its collectible requests are read-only catalog/detail lookups. Normal Telegram account editing remains available whenever the corresponding IntelGram local override is disabled.

## Platform Builds

All packages are built from the official AyuGram Desktop `v6.7.8` source at commit `b25513a06ff88be0b3f4c928252b56c3da39cec7`, with its required submodules.

- macOS: Apple Silicon `.app`, ad-hoc signed, launch tested, packaged as DMG and ZIP
- Windows: x64 `IntelGram.exe`, launch tested, packaged as ZIP
- Linux: x64 `IntelGram`, launch tested under Xvfb, packaged as tar.gz

IntelGram uses its own visible application name, macOS bundle ID, Windows application ID, and Linux desktop ID so it can coexist with a normal AyuGram installation.

## Source And Verification

- [`intelgram-local-profile-render-overrides.patch`](intelgram-local-profile-render-overrides.patch) contains the client-render-only implementation.
- Patch SHA-256: `5039d065566b88f94918fd1972fd0dda7a6817ddb15aeece06ffc0c9ff16e764`
- [`build_intelgram_branding.py`](build_intelgram_branding.py) applies the cross-platform IntelGram product identity.
- [`.github/workflows/intelgram-multiplatform-build.yml`](.github/workflows/intelgram-multiplatform-build.yml) performs clean macOS, Windows, and Linux builds.
- Every release includes SHA-256 checksums, platform validation notes, and launch logs.
- [`FEATURES.md`](FEATURES.md) documents the complete custom feature surface and render coverage.
- [`FEATURE_GUIDE.md`](FEATURE_GUIDE.md) is a conversational walkthrough of the common workflows.
- [`CHANGELOG.md`](CHANGELOG.md), [`TECHNICAL_CHANGELOG.md`](TECHNICAL_CHANGELOG.md), and [`UPDATE_LOG.md`](UPDATE_LOG.md) track product, implementation, and build changes.

IntelGram preserves AyuGram's internal settings keys and source namespaces for compatibility. Product-facing names and package identities are IntelGram.

## Credits

IntelGram is based on [AyuGram Desktop](https://github.com/AyuGram/AyuGramDesktop), which is based on [Telegram Desktop](https://github.com/telegramdesktop/tdesktop). Their upstream licenses and attribution remain in the source.

Local profile and collectible override features by **fool**.
