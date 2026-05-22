# sticker-kit

**English** | [简体中文](README_CN.md)

A skill for generating WeChat sticker pack assets that comply with the official WeChat Open Platform specifications. It covers all required asset types — sticker images, banner, cover, icon, appreciation guide, and appreciation thank-you — as well as the accompanying copywriting (pack name, description, appreciation prompt, and per-sticker labels).

## Features

- Generate all six asset types required by WeChat sticker packs
- Enforce official size, format, and file size constraints automatically
- Support both static (PNG) and animated (GIF) sticker images
- Provide copywriting guidelines for pack name, description, appreciation prompt, and sticker labels
- Include image generation prompt templates for AI tools (DALL·E, Midjourney, etc.)

## Asset Specifications

| Asset | Format | Size (px) | Max Size | Qty |
| :--- | :--- | :--- | :--- | :--- |
| Sticker image | GIF / PNG | 240 × 240 | 500 KB | 8–24 |
| Banner | PNG | 750 × 400 | 500 KB | 1 |
| Cover | PNG | 240 × 240 | 500 KB | 1 |
| Icon | PNG | 50 × 50 | 100 KB | 1 |
| Appreciation guide | GIF / PNG | 750 × 560 | 500 KB | 1 |
| Appreciation thank-you | GIF / PNG | 750 × 750 | 500 KB | 1 |

## Usage

### Process images with the built-in script

```bash
# Static sticker (240×240, PNG, transparent background — default)
python3 scripts/process_sticker.py input.png sticker.png 240 240 PNG 500

# Animated sticker (240×240, GIF, looping, transparent background)
python3 scripts/process_sticker.py input.gif sticker.gif 240 240 GIF 500 True True True

# Cover (240×240, PNG, transparent background)
python3 scripts/process_sticker.py input.png cover.png 240 240 PNG 500

# Icon (50×50, PNG, transparent background)
python3 scripts/process_sticker.py head.png icon.png 50 50 PNG 100

# Banner (750×400, PNG, opaque colored background — transparent must be False)
python3 scripts/process_sticker.py banner_src.png banner.png 750 400 PNG 500 False

# Appreciation guide (750×560, PNG, opaque colored background)
python3 scripts/process_sticker.py guide_src.png guide.png 750 560 PNG 500 False

# Appreciation thank-you (750×750, PNG, opaque colored background)
python3 scripts/process_sticker.py thanks_src.png thanks.png 750 750 PNG 500 False
```

**Parameter order:** `input_path output_path width height format max_kb [transparent=True] [is_animated=False] [loop_gif=False]`

### Key design rules

- **Sticker / Cover / Icon**: transparent background by default; vibrant colors; subject prominent.
- **Banner**: no text allowed; opaque colored background required; the subject or background pattern **must extend fully to both the left and right edges** — no white margins, no solid color borders or bands of any kind (including bands that match the background color) on either side.
- **Appreciation guide / thank-you**: opaque colored background required; avoid white or near-white backgrounds; high-contrast text.

## Requirements

- Python 3.x
- [Pillow](https://python-pillow.org/) (`pip install Pillow`)
