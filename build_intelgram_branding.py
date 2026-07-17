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
	('HOMEPAGE_URL "https://ayugram.one"', 'HOMEPAGE_URL "https://github.com/foolspec/IntelGram"'),
])

replace("Telegram/CMakeLists.txt", [
	('set(bundle_identifier "one.ayugram.AyuGramDesktop$<$<CONFIG:Debug>:Debug>")',
	 'set(bundle_identifier "io.github.foolspec.IntelGram$<$<CONFIG:Debug>:Debug>")'),
	('set(bundle_identifier "one.ayugram.AyuGramDesktop")',
	 'set(bundle_identifier "io.github.foolspec.IntelGram")'),
	('set(output_name "AyuGram")', 'set(output_name "IntelGram")'),
	('OR NOT "${output_name}" STREQUAL "AyuGram")',
	 'OR NOT "${output_name}" STREQUAL "IntelGram")'),
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

replace("Telegram/SourceFiles/window/main_window.cpp", [
	('setTitle((user.isEmpty() ? u"AyuGram"_q : user) + added);',
	 'setTitle((user.isEmpty() ? u"IntelGram"_q : user) + added);'),
])

replace("Telegram/SourceFiles/intro/intro_widget.cpp", [
	('QString("AyuGram Desktop v%1")', 'QString("IntelGram Desktop v%1")'),
])

replace("Telegram/SourceFiles/core/launcher.cpp", [
	('QApplication::setApplicationName(u"AyuGramDesktop"_q);',
	 'QApplication::setApplicationName(u"IntelGramDesktop"_q);'),
])

replace("Telegram/SourceFiles/core/application.cpp", [
	('u"https://github.com/AyuGram/AyuGramDesktop/releases"_q',
	 'u"https://github.com/foolspec/IntelGram/releases"_q'),
	('.shortAppName = u"AyuGram"_q,', '.shortAppName = u"IntelGram"_q,'),
])

replace("Telegram/SourceFiles/core/update_checker.cpp", [
	('return "https://t.me/AyuGramReleases";',
	 'return "https://github.com/foolspec/IntelGram/releases";'),
])

replace_all(
	"Telegram/SourceFiles/platform/linux/main_window_linux.cpp",
	'u"AyuGram"_q',
	'u"IntelGram"_q',
	2,
)

replace("Telegram/SourceFiles/platform/mac/window_title_mac.mm", [
	('p.drawText(titleRect, u"AyuGram"_q, style::al_center);',
	 'p.drawText(titleRect, u"IntelGram"_q, style::al_center);'),
])

replace("Telegram/SourceFiles/platform/mac/global_menu_mac.mm", [
	('u"About AyuGram"_q,', 'u"About IntelGram"_q,'),
	('_menuBar->addMenu(u"AyuGram"_q)', '_menuBar->addMenu(u"IntelGram"_q)'),
])

replace("Telegram/SourceFiles/core/crash_report_window.cpp", [
	('u"AyuGram"_q : title', 'u"IntelGram"_q : title'),
	('u"Could not start AyuGram Desktop!\\nYou can see complete log below:"_q',
	 'u"Could not start IntelGram Desktop!\\nYou can see complete log below:"_q'),
	('u"Last time AyuGram Desktop crashed :("_q',
	 'u"Last time IntelGram Desktop crashed :("_q'),
	('u"https://github.com/AyuGram/AyuGramDesktop"_q',
	 'u"https://github.com/foolspec/IntelGram"_q'),
	('u"AyuGram Crash Report"_q', 'u"IntelGram Crash Report"_q'),
])

replace_all(
	"Telegram/SourceFiles/core/crash_report_window.cpp",
	'u"Last time AyuGram Desktop was not closed properly."_q',
	'u"Last time IntelGram Desktop was not closed properly."_q',
	2,
)

replace("Telegram/SourceFiles/core/crash_reports.cpp", [
	('"AyuGram Desktop launch was not finished properly :( "',
	 '"IntelGram Desktop launch was not finished properly :( "'),
])

replace("Telegram/SourceFiles/boxes/about_box.cpp", [
	('"https://github.com/AyuGram/AyuGramDesktop")),',
	 '"https://github.com/foolspec/IntelGram")),'),
	('box->setTitle(rpl::single(u"AyuGram Desktop"_q));',
	 'box->setTitle(rpl::single(u"IntelGram Desktop"_q));'),
	('''box->addLeftButton(
		rpl::single(QString("@AyuGramReleases")),
		[box, controller]
		{
			box->closeBox();
			controller->showPeerByLink(Window::PeerByLinkInfo{
				.usernameOrId = QString("ayugramreleases"),
			});
		});''',
	 '''box->addLeftButton(
		rpl::single(QString("IntelGram on GitHub")),
		[box]
		{
			box->closeBox();
			File::OpenUrl("https://github.com/foolspec/IntelGram");
		});'''),
])

replace_all(
	"Telegram/SourceFiles/tray.cpp",
	'"Telegram", "AyuGram"',
	'"Telegram", "IntelGram"',
	2,
)

replace("Telegram/SourceFiles/export/output/export_output_html.cpp", [
	('"of AyuGram Desktop. Please update the application."',
	 '"of IntelGram Desktop. Please update the application."'),
])

replace("Telegram/SourceFiles/history/history_item_helpers.cpp", [
	('const auto siteLink = u"https://t.me/AyuGramReleases"_q;',
	 'const auto siteLink = u"https://github.com/foolspec/IntelGram/releases"_q;'),
	('.replace("Telegram", "AyuGram")', '.replace("Telegram", "IntelGram")'),
])

replace("Telegram/SourceFiles/window/window_main_menu.cpp", [
	('u"AyuGram Desktop"_q,', 'u"IntelGram Desktop"_q,'),
])

replace("Telegram/SourceFiles/window/notifications_manager_default.cpp", [
	('TextWithEntities{ u"AyuGram Desktop"_q }',
	 'TextWithEntities{ u"IntelGram Desktop"_q }'),
])

replace("Telegram/SourceFiles/ayu/ui/context_menu/context_menu.cpp", [
	('.text = u"AyuGram"_q,', '.text = u"IntelGram"_q,'),
])

replace("Telegram/SourceFiles/ayu/features/filters/filters_utils.cpp", [
	('titlePart.setBody("AyuGram Filters");',
	 'titlePart.setBody("IntelGram Filters");'),
])

replace("Telegram/SourceFiles/ayu/ui/components/message_preview.cpp", [
	('u"AyuGram Releases"_q);', 'u"IntelGram Releases"_q);'),
])

replace_all(
	"Telegram/SourceFiles/ayu/ui/components/avatar_corners_preview.cpp",
	'u"AyuGram Releases"_q',
	'u"IntelGram Releases"_q',
	2,
)

replace("Telegram/SourceFiles/ayu/ui/ayu_logo.cpp", [
	('+ u"tdata/AyuGram-"_q', '+ u"tdata/IntelGram-"_q'),
])

replace_all(
	"Telegram/SourceFiles/platform/win/windows_app_user_model_id.cpp",
	"AyuGram",
	"IntelGram",
	11,
)

replace_all(
	"Telegram/SourceFiles/platform/win/specific_win.cpp",
	"AyuGram.lnk",
	"IntelGram.lnk",
	2,
)

replace_all(
	"Telegram/SourceFiles/ayu/utils/windows_utils.cpp",
	"AyuGram",
	"IntelGram",
	8,
)

replace("Telegram/SourceFiles/_other/startup_task_win.cpp", [
	('L"\\\\AyuGram.exe"', 'L"\\\\IntelGram.exe"'),
])

replace_all(
	"Telegram/SourceFiles/_other/updater_win.cpp",
	"AyuGram.exe",
	"IntelGram.exe",
	4,
)

replace("Telegram/SourceFiles/_other/updater_osx.m", [
	('@"AyuGram.app"', '@"IntelGram.app"'),
	('@"/Contents/MacOS/AyuGram"', '@"/Contents/MacOS/IntelGram"'),
])

replace_all(
	"Telegram/Resources/winrc/Telegram.rc",
	"AyuGram Desktop",
	"IntelGram Desktop",
	2,
)

replace("Telegram/Resources/winrc/Updater.rc", [
	('"AyuGram Desktop Updater"', '"IntelGram Desktop Updater"'),
	('"AyuGram Desktop"', '"IntelGram Desktop"'),
])

replace("Telegram/build/setup.iss", [
	('#define MyAppShortName "AyuGram"', '#define MyAppShortName "IntelGram"'),
	('#define MyAppName "AyuGram Desktop"', '#define MyAppName "IntelGram Desktop"'),
	('#define MyAppURL "https://github.com/AyuGram"',
	 '#define MyAppURL "https://github.com/foolspec/IntelGram"'),
	('#define MyAppExeName "AyuGram.exe"', '#define MyAppExeName "IntelGram.exe"'),
])

replace("Telegram/SourceFiles/ayu/ui/settings/settings_ayu.cpp", [
	('.title = u"AyuGram"_q,', '.title = u"IntelGram"_q,'),
	('return rpl::single(QString("AyuGram"));',
	 'return rpl::single(QString("IntelGram"));'),
])

replace("Telegram/SourceFiles/ayu/ui/settings/settings_main.cpp", [
	('QString("AyuGram Desktop v")', 'QString("IntelGram Desktop v")'),
	('.title = rpl::single(QString("AyuGram")),',
	 '.title = rpl::single(QString("IntelGram")),'),
])

replace("Telegram/SourceFiles/settings/sections/settings_notifications.cpp", [
	('u"AyuGram Desktop"_q, rectForName.width()',
	 'u"IntelGram Desktop"_q, rectForName.width()'),
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
	 '<url type="homepage">https://github.com/foolspec/IntelGram</url>'),
	('<url type="faq">https://t.me/AyuGramFAQ</url>',
	 '<url type="faq">https://github.com/foolspec/IntelGram#using-intelgram</url>'),
	('<url type="bugtracker">https://t.me/ayugramchat/1262</url>',
	 '<url type="bugtracker">https://github.com/foolspec/IntelGram/issues</url>'),
	('<url type="vcs-browser">https://github.com/AyuGram/AyuGramDesktop</url>',
	 '<url type="vcs-browser">https://github.com/foolspec/IntelGram</url>'),
	('<url type="contribute">https://github.com/AyuGram/AyuGramDesktop/blob/dev/.github/CONTRIBUTING.md</url>',
	 '<url type="contribute">https://github.com/foolspec/IntelGram</url>'),
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
	source = ROOT / "lib/xdg" / old
	(ROOT / "lib/xdg" / new).write_bytes(source.read_bytes())
