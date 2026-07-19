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


def prepare_macos(source: Path, crop: tuple[int, int, int, int]) -> Image.Image:
	return (
		Image.open(source)
		.convert("RGBA")
		.crop(crop)
		.resize((1024, 1024), Image.Resampling.LANCZOS)
	)


def flatten_for_macos(image: Image.Image) -> Image.Image:
	image = image.convert("RGBA")
	width, height = image.size
	background = image.getpixel((max(0, width // 16), height // 2))
	if background[3] == 0:
		background = (32, 38, 50, 255)
	else:
		background = (*background[:3], 255)
	result = Image.new("RGBA", image.size, background)
	result.alpha_composite(image)
	return result


def write_platform_assets(
	name: str,
	image: Image.Image,
	output: Path,
	macos_image: Image.Image,
) -> None:
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
	macos_image.save(macos / f"{name}.png", optimize=True)
	macos_image.save(macos / f"{name}.icns", format="ICNS")

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
	front_macos = prepare_macos(
		SOURCE / "intelgram-pink-front-source.png",
		(60, 60, 1194, 1194),
	)
	profile_macos = prepare_macos(
		SOURCE / "intelgram-pink-profile-source.png",
		(70, 70, 1184, 1184),
	)
	write_platform_assets("intelgram-pink-front", front, OUTPUT, front_macos)
	write_platform_assets("intelgram-pink-profile", profile, OUTPUT, profile_macos)

	for source in sorted((COLOR_OUTPUT / "masters").glob("*.png")):
		image = Image.open(source).convert("RGBA")
		if image.size != (1024, 1024):
			image = image.resize((1024, 1024), Image.Resampling.LANCZOS)
		write_platform_assets(
			source.stem,
			image,
			COLOR_OUTPUT,
			flatten_for_macos(image),
		)


if __name__ == "__main__":
	main()
