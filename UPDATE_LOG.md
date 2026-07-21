# IntelGram Update Log

## Current Update

- Base source: official AyuGram Desktop `v6.7.8` at `b25513a06ff88be0b3f4c928252b56c3da39cec7` with required submodules.
- Product identity: IntelGram on macOS, Windows, and Linux with separate application identifiers.
- Source delivery: one complete client-render-only patch plus the deterministic branding script.
- Build delivery: GitHub Actions packages macOS Apple Silicon, Windows x64, and Linux x64.
- Latest feature scope: local profile fields, photo, high-fidelity profile clone, UID/phone cached-peer search, native collection and item galleries, featured gift, pinned gifts, and fourteen app-icon choices.
- Collectible gallery: the collection screen uses native artwork tiles, each collection opens a scrollable exact-item grid, and clicking a collectible selects it without leaving IntelGram.
- Local gift recipient: featured, pinned, and cloned collectible details match local gift slugs immediately, use your active real or local display name for **Gifted to** and the **Telegram** profile chip, and open your own locally rendered profile without changing real ownership data.
- Compact profile consistency: the collectible's Telegram row now opens a card using your local display name, large profile photo, phone, usernames, bio, and personal channel instead of the collectible owner's server profile.
- Collectible owner consistency: collectible username and anonymous-number boxes now show your active local or cloned display name beside the locally rendered avatar instead of the underlying Telegram peer label.
- Clone fidelity: premium and verification badges, organization badge symbols, emoji status, and personal channel follow a read-only refresh of the already-known source profile; absent elements are cleared from the cloned local view.
- Username editor: the added original-username strip is gone and Telegram's familiar inline syntax/availability row is restored without a network availability request.
- Settings organization: local controls are grouped into identity, contact, photo, and collectible sections.
- Dynamic preview: the name-color sample follows the currently rendered local display name.
- Icon pack: pink primary and profile-art icons plus twelve color variants include native macOS, multi-resolution Windows, and Linux resources; macOS artwork is full-bleed and no longer receives a second white frame or inset.
- Settings cleanup: inherited Boosty and cryptocurrency donation rows were removed and replaced with IntelGram community, source, and changelog links.
- Community badge: joining `@intelgrams` through Telegram's normal channel page unlocks a local supporter badge; IntelGram performs no automatic join request.
- In-app update log: **IntelGram Settings -> IntelGram -> Update log** opens a bundled native summary without requiring GitHub.
- Current source patch SHA-256: `ae6e8dbdfc3c9daee6c565800e8ef55c840a8b29172d6dd0d5d55790b5415de7`.
- Replacement packages: macOS run `29777684364`, Windows run `29777689027`, and Linux run `29777686484` record patch `ae6e8dbdfc3c9daee6c565800e8ef55c840a8b29172d6dd0d5d55790b5415de7` and passed isolated launch smoke tests.
- The replacement release publishes these packages together as `intelgram-v6.7.8-local-profile-20260720-2`.
- Publisher run `29789518828` and public-release validation run `29789551493` completed successfully.
- Privacy boundary: no Telegram profile mutation, no contact import, and no collectible ownership transaction.
- Branding consistency: product-facing window, settings, version, and notification-preview titles use IntelGram while upstream attribution remains intact.
- Login and platform branding: the login footer, application menus, About and crash dialogs, tray labels, updater identity, and Windows shortcut metadata now consistently use IntelGram.
- Windows reliability: the final Qt dependency stage is serialized to prevent the `qtimageformats` generated-directory race seen in the previous run.

## Validation Recorded For Each Release

- Patch SHA-256 verification before application.
- Clean `git apply --check` against the pinned official source revision.
- Whitespace and postimage checks.
- Scan for unexpected Telegram profile mutation references.
- Scan for unexpected channel-join requests.
- Platform configure and compile result.
- Package identity and executable checks.
- Isolated-work-directory launch smoke test.
- Package SHA-256 checksums and launch logs.

## Release Outputs

- `IntelGram-macOS-Apple-Silicon.dmg`
- `IntelGram-macOS-Apple-Silicon.zip`
- `IntelGram-Windows-x64.zip`
- `IntelGram-Linux-x64.tar.gz`

The final packages and exact checksums are attached to [`intelgram-v6.7.8-local-profile-20260720-2`](https://github.com/foolspec/IntelGram/releases/tag/intelgram-v6.7.8-local-profile-20260720-2).
