# sticker-kit

[English](README.md) | **简体中文**

用于生成符合微信开放平台官方规范的表情包合辑素材，涵盖表情图、横幅图、封面图、图标、赞赏引导图和赞赏致谢图六类资产，以及配套的合辑文案（合辑名称、合辑介绍、赞赏引导语、每张表情的含义词）。

## 功能特性

- 自动化生成微信表情包所需的全部六类素材
- 严格遵循官方尺寸、格式和体积限制
- 同时支持静态（PNG）和动态（GIF）表情图
- 提供合辑名称、合辑介绍、赞赏引导语及含义词的文案创作指引
- 内置适配 AI 图像生成工具（DALL·E、Midjourney 等）的提示词模板

## 素材规范

| 素材类型 | 格式 | 尺寸 (px) | 体积上限 | 数量 |
| :--- | :--- | :--- | :--- | :--- |
| 表情图 | GIF / PNG | 240 × 240 | 500 KB | 8–24 |
| 横幅图 | PNG | 750 × 400 | 500 KB | 1 |
| 封面图 | PNG | 240 × 240 | 500 KB | 1 |
| 图标 | PNG | 50 × 50 | 100 KB | 1 |
| 赞赏引导图 | GIF / PNG | 750 × 560 | 500 KB | 1 |
| 赞赏致谢图 | GIF / PNG | 750 × 750 | 500 KB | 1 |

## 使用方法

### 使用内置脚本处理图片

```bash
# 静态表情图（240×240，PNG，透明背景 — 默认）
python3 scripts/process_sticker.py input.png sticker.png 240 240 PNG 500

# 动态表情图（240×240，GIF，循环播放，透明背景）
python3 scripts/process_sticker.py input.gif sticker.gif 240 240 GIF 500 True True True

# 封面图（240×240，PNG，透明背景）
python3 scripts/process_sticker.py input.png cover.png 240 240 PNG 500

# 图标（50×50，PNG，透明背景）
python3 scripts/process_sticker.py head.png icon.png 50 50 PNG 100

# 横幅图（750×400，PNG，彩色不透明背景 — transparent 须设为 False）
python3 scripts/process_sticker.py banner_src.png banner.png 750 400 PNG 500 False

# 赞赏引导图（750×560，PNG，彩色不透明背景）
python3 scripts/process_sticker.py guide_src.png guide.png 750 560 PNG 500 False

# 赞赏致谢图（750×750，PNG，彩色不透明背景）
python3 scripts/process_sticker.py thanks_src.png thanks.png 750 750 PNG 500 False
```

**参数顺序：** `input_path output_path width height format max_kb [transparent=True] [is_animated=False] [loop_gif=False]`

### 核心设计规则

- **表情图 / 封面图 / 图标**：默认透明背景；颜色鲜明饱和；主体形象突出。
- **横幅图**：禁止出现文字；须使用彩色不透明背景；主体或背景元素**必须横向铺满整个画布，两侧不得留白边、空边或任何形式的纯色边**（包括与背景色相同的纯色填充带）。
- **赞赏引导图 / 赞赏致谢图**：须使用彩色不透明背景；禁止白色或接近白色的背景；文字与背景须保持高对比度。

## 环境依赖

- Python 3.x
- [Pillow](https://python-pillow.org/)（`pip install Pillow`）
