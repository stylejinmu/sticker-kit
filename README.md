# sticker-kit

**微信表情包合辑素材生成工具** —— 一个用于 [Manus](https://manus.im) 的 Skill，帮助自动化生成符合微信表情包开放平台规范的全套素材。

## 功能概览

本 Skill 严格遵循微信官方的尺寸、格式、体积及设计规范，支持生成以下六类素材：

| 素材类型 | 格式 | 尺寸 (px) | 体积限制 |
| :--- | :--- | :--- | :--- |
| 表情图 | GIF / PNG | 240 × 240 | < 500 KB |
| 横幅图 | PNG | 750 × 400 | < 500 KB |
| 封面图 | PNG | 240 × 240 | < 500 KB |
| 图标 | PNG | 50 × 50 | < 100 KB |
| 赞赏引导图 | GIF / PNG | 750 × 560 | < 500 KB |
| 赞赏致谢图 | GIF / PNG | 750 × 750 | < 500 KB |

## 核心特性

- **自动尺寸适配**：等比缩放，严禁拉伸变形。
- **体积自动压缩**：超出限制时自动降低质量，确保达标。
- **透明背景支持**：表情图、横幅、封面、图标及赞赏引导图默认使用透明背景（PNG）。
- **致谢图彩色背景**：赞赏致谢图强制使用非透明彩色背景，避免与微信详情页底色混淆。
- **动态 GIF 支持**：支持循环播放的动态表情处理。

## 使用方式

本 Skill 作为 Manus Agent 的扩展模块运行。将本仓库安装为 Skill 后，在 Manus 中描述表情包素材生成需求，Agent 将自动调用内置脚本完成处理。

### 核心脚本

```bash
python3 scripts/process_sticker.py <input> <output> <width> <height> <format> <max_kb> [transparent] [is_animated] [loop_gif]
```

**参数说明：**

| 参数 | 默认值 | 说明 |
| :--- | :--- | :--- |
| `input` | — | 输入文件路径 |
| `output` | — | 输出文件路径 |
| `width` | — | 目标宽度（px） |
| `height` | — | 目标高度（px） |
| `format` | — | 输出格式：`PNG` / `GIF` / `JPG` |
| `max_kb` | — | 最大体积（KB） |
| `transparent` | `True` | 是否使用透明背景（JPG 自动忽略） |
| `is_animated` | `False` | 是否处理动态 GIF |
| `loop_gif` | `False` | GIF 是否循环播放 |

**示例：**

```bash
# 生成静态表情图（透明背景）
python3 scripts/process_sticker.py input.png sticker.png 240 240 PNG 500

# 生成动态表情图（循环播放）
python3 scripts/process_sticker.py input.gif sticker.gif 240 240 GIF 500 True True True

# 生成赞赏致谢图（彩色不透明背景）
python3 scripts/process_sticker.py input.png thanks.png 750 750 PNG 500 False
```

## 设计规范要点

- **横幅图**：绝对不能出现文字，色调活泼，与微信底色有明显区分。
- **封面 / 图标**：形象不应有白色描边，边缘需平滑无锯齿。
- **赞赏引导图**：使用透明背景，但须避免白色或接近白色的背景/边缘，以免与微信详情页底色混淆。
- **赞赏致谢图**：必须使用彩色不透明背景，禁止透明背景，同样须避免白色或接近白色的背景/边缘。

## 关于 Manus Skill

Manus Skill 是为 [Manus](https://manus.im) AI Agent 设计的模块化能力扩展包，通过提供专业工作流、领域知识和可复用脚本，将通用 Agent 转化为特定领域的专家助手。
