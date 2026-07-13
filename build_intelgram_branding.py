#!/usr/bin/env python3

from pathlib import Path


ROOT = Path.cwd()


def replace(path: str, replacements: list[tuple[str, str]]) -> None:
	file = ROOT / path
	content = file.read_text(encoding="utf-8")
	for old, new in replacements:
		count = content.count(old)
		if count != 1:
			raise RuntimeError(f"{path}: expected one occurrence of {old!r}, found {count}")
		content = content.replace(old, new)
	file.write_text(content, encoding="utf-8")


def replace_all(path: str, old: str, new: str, expected: int) -> None:
	file = ROOT / path
	content = file.read_text(encoding="utf-8")
	count = content.count(old)
	if count != expected:
		raise RuntimeError(f"{path}: expected {expected} occurrences of {old!r}, found {count}")
	file.write_text(content.replace(old, new), encoding="utf-8")


replace("CMakeLists.txt", [
	('DESCRIPTION "AyuGram Desktop"', 'DESCRIPTION "IntelGram Desktop"'),
	('HOMEPAGE_URL "https://ayugram.one"', 'HOMEPAGE_URL "https://github.com/foolspec/collectables"'),
])

replace("Telegram/CMakeLists.txt", [
	('set(bundle_identifier "one.ayugram.AyuGramDesktop$<$<CONFIG:Debug>:Debug>")',
	 'set(bundle_identifier "io.github.foolspec.IntelGram$<$<CONFIG:Debug>:Debug>")'),
	('set(bundle_identifier "one.ayugram.AyuGramDesktop")',
	 'set(bundle_identifier "io.github.foolspec.IntelGram")'),
	('set(output_name "AyuGram")', 'set(output_name "IntelGram")'),
])

replace_all(
	"Telegram/CMakeLists.txt",
	"com.ayugram.desktop",
	"io.github.foolspec.intelgram",
	25,
)

replace("Telegram/SourceFiles/core/version.h", [
	('constexpr auto AppId = "{53F49750-6209-4FBF-9CA8-7A333C87D666}"_cs;',
	 'constexpr auto AppId = "{7AF76B28-0DD4-4CCB-BFA8-53CC3079650D}"_cs;'),
	('constexpr auto AppNameOld = "AyuGram for Windows"_cs;',
	 'constexpr auto AppNameOld = "IntelGram for Windows"_cs;'),
	('constexpr auto AppName = "AyuGram Desktop"_cs;',
	 'constexpr auto AppName = "IntelGram Desktop"_cs;'),
	('constexpr auto AppFile = "AyuGram"_cs;',
	 'constexpr auto AppFile = "IntelGram"_cs;'),
])

replace("lib/xdg/com.ayugram.desktop.desktop", [
	('Name=AyuGram Desktop', 'Name=IntelGram Desktop'),
	('Comment=Desktop version of AyuGram - ToS breaking Telegram client',
	 'Comment=IntelGram client with local-only profile render overrides'),
	('TryExec=AyuGram', 'TryExec=IntelGram'),
	('Exec=env DESKTOPINTEGRATION=1 AyuGram -- %U',
	 'Exec=env DESKTOPINTEGRATION=1 IntelGram -- %U'),
	('Icon=com.ayugram.desktop', 'Icon=io.github.foolspec.intelgram'),
	('StartupWMClass=AyuGram', 'StartupWMClass=IntelGram'),
	('Exec=AyuGram -quit', 'Exec=IntelGram -quit'),
	('Name=Quit AyuGram', 'Name=Quit IntelGram'),
])

replace("lib/xdg/com.ayugram.desktop.service", [
	('Name=com.ayugram.desktop', 'Name=io.github.foolspec.intelgram'),
	('Exec=@CMAKE_INSTALL_FULL_BINDIR@/AyuGram',
	 'Exec=@CMAKE_INSTALL_FULL_BINDIR@/IntelGram'),
])

replace("lib/xdg/com.ayugram.desktop.metainfo.xml", [
	('<id>com.ayugram.desktop</id>', '<id>io.github.foolspec.intelgram</id>'),
	('<name>AyuGram Desktop</name>', '<name>IntelGram Desktop</name>'),
	('<summary>Desktop version of AyuGram - ToS breaking Telegram client</summary>',
	 '<summary>Telegram client with local-only profile render overrides</summary>'),
	('<p>Telegram Desktop with Ghost Mode, Anti-Recall and cool design.</p>',
	 '<p>IntelGram is based on AyuGram Desktop and adds client-render-only local profile controls.</p>'),
	('<url type="homepage">https://ayugram.one/</url>',
	 '<url type="homepage">https://github.com/foolspec/collectables</url>'),
	('<url type="faq">https://t.me/AyuGramFAQ</url>',
	 '<url type="faq">https://github.com/foolspec/collectables#using-intelgram</url>'),
	('<url type="bugtracker">https://t.me/ayugramchat/1262</url>',
	 '<url type="bugtracker">https://github.com/foolspec/collectables/issues</url>'),
	('<url type="vcs-browser">https://github.com/AyuGram/AyuGramDesktop</url>',
	 '<url type="vcs-browser">https://github.com/foolspec/collectables</url>'),
	('<url type="contribute">https://github.com/AyuGram/AyuGramDesktop/blob/dev/.github/CONTRIBUTING.md</url>',
	 '<url type="contribute">https://github.com/foolspec/collectables</url>'),
	('<keyword>ayugram</keyword>', '<keyword>intelgram</keyword>'),
	('<launchable type="desktop-id">com.ayugram.desktop.desktop</launchable>',
	 '<launchable type="desktop-id">io.github.foolspec.intelgram.desktop</launchable>'),
	('<binary>AyuGram</binary>', '<binary>IntelGram</binary>'),
])

for old, new in (
	("com.ayugram.desktop.desktop", "io.github.foolspec.intelgram.desktop"),
	("com.ayugram.desktop.service", "io.github.foolspec.intelgram.service"),
	("com.ayugram.desktop.metainfo.xml", "io.github.foolspec.intelgram.metainfo.xml"),
):
	(ROOT / "lib/xdg" / old).rename(ROOT / "lib/xdg" / new)
