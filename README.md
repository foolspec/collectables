# IntelGram

IntelGram is a cross-platform AyuGram Desktop build focused on local-only profile customization.

[![IntelGram builds](https://github.com/foolspec/IntelGram/actions/workflows/intelgram-multiplatform-build.yml/badge.svg?branch=main)](https://github.com/foolspec/IntelGram/actions/workflows/intelgram-multiplatform-build.yml)

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

Clicking your username in IntelGram's profile settings opens the local username editor. It displays your original Telegram username for reference before saving the IntelGram-only value.

The collectible picker shows live native previews for Scared Cat, Plush Pepe, Toy Bear, and other collections. Choose a collection to browse real numbered models in a scrollable in-app grid, click one to select it, or paste any supported Telegram gift slug, `t.me/nft` link, Getgems item URL, or TON NFT address. IntelGram resolves the exact collectible read-only, shows its native `Collection #Number` profile tooltip, and uses Telegram's native collectible detail view when clicked.

Choose a local image to replace your own profile photo throughout this IntelGram installation. Profile cloning accepts the UID of a user whose profile has already been opened and locally mirrors their visible name, UID, usernames, phone, bio, photo, profile colors, emoji status, and featured collectible. Stop cloning at any time to return to the individual local fields.

## Local Means Local

These controls only change how your own profile is rendered inside this IntelGram installation. They do not change your Telegram display name, photo, bio, username, UID, phone number, emoji status, collectible ownership, or profile data. Other Telegram users do not see the local overrides.

The implementation contains no Telegram account/profile mutation request. Normal Telegram account editing remains available whenever the corresponding IntelGram local override is disabled.

## Platform Builds

All packages are built from the official AyuGram Desktop `v6.7.8` source at commit `b25513a06ff88be0b3f4c928252b56c3da39cec7`, with its required submodules.

- macOS: Apple Silicon `.app`, ad-hoc signed, launch tested, packaged as DMG and ZIP
- Windows: x64 `IntelGram.exe`, launch tested, packaged as ZIP
- Linux: x64 `IntelGram`, launch tested under Xvfb, packaged as tar.gz

IntelGram uses its own visible application name, macOS bundle ID, Windows application ID, and Linux desktop ID so it can coexist with a normal AyuGram installation.

## Source And Verification

- [`intelgram-local-profile-render-overrides.patch`](intelgram-local-profile-render-overrides.patch) contains the client-render-only implementation.
- Patch SHA-256: `31c8ce20cc709dcdec2a4c2ee03dbcaf91da169c695deb79781910890eacc09c`
- [`build_intelgram_branding.py`](build_intelgram_branding.py) applies the cross-platform IntelGram product identity.
- [`.github/workflows/intelgram-multiplatform-build.yml`](.github/workflows/intelgram-multiplatform-build.yml) performs clean macOS, Windows, and Linux builds.
- Every release includes SHA-256 checksums, platform validation notes, and launch logs.

IntelGram preserves AyuGram's internal settings keys and source namespaces for compatibility. Product-facing names and package identities are IntelGram.

## Credits

IntelGram is based on [AyuGram Desktop](https://github.com/AyuGram/AyuGramDesktop), which is based on [Telegram Desktop](https://github.com/telegramdesktop/tdesktop). Their upstream licenses and attribution remain in the source.

Local profile and collectible override features by **fool**.
