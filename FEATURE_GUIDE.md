# IntelGram Feature Guide

## Where do I change my local profile?

Open **IntelGram Settings -> Other -> Local profile**. The controls are grouped into **Identity**, **Usernames, bio and contact**, **Profile photo**, and **Collectibles**. Each field has its own switch or action, so you can use only the pieces you want.

## How do I change my local username?

Enable local usernames, then open the username editor. Its familiar inline status checks the local value's Telegram-style syntax and marks a valid value as available inside IntelGram; it does not ask Telegram whether the public username is available. Add the primary local username and, if needed, up to 20 other usernames.

## How do I use an anonymous number or local UID?

Enable the corresponding setting and enter the value you want rendered. These are display overrides inside IntelGram, not Telegram account changes.

## How do I use a local profile picture?

Choose **Local profile photo**, select an image on this Mac or PC, and enable the local profile presentation. Clear the photo setting to restore the normal Telegram image.

## How do I clone a profile locally?

First open the other user's profile so IntelGram has loaded it. Copy their UID, choose **Clone profile locally by UID**, paste the UID, and confirm. IntelGram refreshes that already-known profile read-only, then mirrors only data visible to you, including premium or verification badges, the organization badge symbol, emoji status, and personal channel. If the source has none of those elements, the cloned local view shows none even when your real profile has one. Choose **Stop cloning profile** to return to your own local fields.

## How do I find somebody by UID or phone?

Use the normal search field above the chat list. Paste a UID, `id: UID`, or a phone number. A known matching profile appears under **Found by ID or phone**. This cannot discover strangers or hidden phone numbers; the peer must already be loaded and the phone must already be visible.

## How do I browse collectible gifts?

Choose **Choose featured collectible** or **Manage pinned collectible gifts**. The first screen is a native gallery of collection artwork. Click a collection, scroll through its numbered collectibles, and click the exact artwork you want; more items load as you reach the end. The entire selection flow stays inside IntelGram.

## Can I paste a Getgems or TON link?

Yes. Use **Open by collectible link** and paste a supported Getgems item URL, `t.me/nft` URL, Telegram gift slug, or TON NFT address. IntelGram resolves the exact Telegram collectible when the metadata maps to one.

## How do I change the IntelGram app icon?

Open **Settings -> Appearance -> App Icon**. Choose the pink primary artwork, the pink profile-art alternate, or one of twelve color variants. IntelGram stores the choice locally and uses the matching platform-native icon resource.

## Why does the name-color preview show a different name?

The preview follows the name IntelGram currently renders for your own profile. Change the enabled local display name and the sample updates to that value instead of showing a fixed name.

## What happens when I click a rendered collectible?

IntelGram opens Telegram's native unique-gift detail surface for that exact model and number. For a locally selected or cloned collectible, **Gifted to** uses the display name IntelGram currently renders for you, and clicking that recipient opens your own profile. The local presentation does not claim ownership, rewrite the real sender or date, or create a transaction.

## Can anybody else see these changes?

No. They are visible only in this IntelGram installation. Screenshots will naturally show what IntelGram rendered, but Telegram and other users receive none of these local values.

## How do I get the IntelGram supporter badge?

Open **IntelGram Settings -> IntelGram -> Telegram**, then press Telegram's normal **Join** button on `@intelgrams`. IntelGram reads that locally known membership state and displays the badge on your own profile. It does not join the channel automatically, and leaving the channel removes the local membership-derived badge after Telegram updates the channel state.

## Where can I read the update log?

Open **IntelGram Settings -> IntelGram -> Update log**. The bundled dialog summarizes the latest update, main IntelGram features, and the local-only privacy boundary. **View full changelog** opens the longer GitHub history when you need it.
