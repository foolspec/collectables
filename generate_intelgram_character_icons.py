#!/usr/bin/env python3

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "branding/icons/character/source"
OUTPUT = ROOT / "branding/icons/character"
COLOR_OUTPUT = ROOT / "branding/icons/color"
SIZES = (16, 22, 24, 32, 48, 64, 96, 128, 256, 512, 1024)


def prepare(source: Path, crop: tuple[int, int, int, int], shape: str) -> Image.Image:
	image = Image.open(source).convert("RGBA").crop(crop)
	image = image.resize((1024, 1024), Image.Resampling.LANCZOS)
	mask = Image.new("L", image.size, 0)
	draw = ImageDraw.Draw(mask)
	if shape == "circle":
		draw.ellipse((8, 8, 1015, 1015), fill=255)
	else:
		draw.rounded_rectangle((0, 0, 1023, 1023), radius=160, fill=255)
	image.putalpha(mask)
	return image


def write_platform_assets(name: str, image: Image.Image, output: Path) -> None:
	masters = output / "masters"
	windows = output / "Windows"
	macos = output / "macOS"
	for directory in (masters, windows, macos):
		directory.mkdir(parents=True, exist_ok=True)

	image.save(masters / f"{name}.png", optimize=True)
	image.save(
		windows / f"{name}.ico",
		format="ICO",
		sizes=[(size, size) for size in (16, 24, 32, 48, 64, 128, 256)],
	)
	image.save(macos / f"{name}.icns", format="ICNS")

	for size in SIZES:
		directory = output / "Linux/hicolor" / f"{size}x{size}/apps"
		directory.mkdir(parents=True, exist_ok=True)
		resized = image.resize((size, size), Image.Resampling.LANCZOS)
		resized.save(directory / f"{name}.png", optimize=True)


def main() -> None:
	front = prepare(
		SOURCE / "intelgram-pink-front-source.png",
		(60, 60, 1194, 1194),
		"rounded",
	)
	profile = prepare(
		SOURCE / "intelgram-pink-profile-source.png",
		(70, 70, 1184, 1184),
		"circle",
	)
	write_platform_assets("intelgram-pink-front", front, OUTPUT)
	write_platform_assets("intelgram-pink-profile", profile, OUTPUT)

	for source in sorted((COLOR_OUTPUT / "masters").glob("*.png")):
		image = Image.open(source).convert("RGBA")
		if image.size != (1024, 1024):
			image = image.resize((1024, 1024), Image.Resampling.LANCZOS)
		write_platform_assets(source.stem, image, COLOR_OUTPUT)


if __name__ == "__main__":
	main()
