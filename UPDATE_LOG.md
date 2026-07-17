# IntelGram Update Log

## Current Update

- Base source: official AyuGram Desktop `v6.7.8` at `b25513a06ff88be0b3f4c928252b56c3da39cec7` with required submodules.
- Product identity: IntelGram on macOS, Windows, and Linux with separate application identifiers.
- Source delivery: one complete client-render-only patch plus the deterministic branding script.
- Build delivery: GitHub Actions packages macOS Apple Silicon, Windows x64, and Linux x64.
- Latest feature scope: local profile fields, photo, profile clone, UID/phone cached-peer search, dynamic collectible catalog, exact item browser, featured gift, and pinned gifts.
- Privacy boundary: no Telegram profile mutation, no contact import, and no collectible ownership transaction.
- Branding consistency: product-facing window, settings, version, and notification-preview titles use IntelGram while upstream attribution remains intact.
- Windows reliability: the final Qt dependency stage is serialized to prevent the `qtimageformats` generated-directory race seen in the previous run.

## Validation Recorded For Each Release

- Patch SHA-256 verification before application.
- Clean `git apply --check` against the pinned official source revision.
- Whitespace and postimage checks.
- Scan for unexpected Telegram profile mutation references.
- Platform configure and compile result.
- Package identity and executable checks.
- Isolated-work-directory launch smoke test.
- Package SHA-256 checksums and launch logs.

## Release Outputs

- `IntelGram-macOS-Apple-Silicon.dmg`
- `IntelGram-macOS-Apple-Silicon.zip`
- `IntelGram-Windows-x64.zip`
- `IntelGram-Linux-x64.tar.gz`

The latest completed result and exact checksums are attached to the repository's latest GitHub release.
