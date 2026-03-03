import os
import sys
from PIL import Image, ImageSequence


def process_image(
    input_path,
    output_path,
    size,
    format,
    max_kb,
    transparent=True,   # 默认透明背景
    no_white_border=False,
    is_animated=False,
    loop_gif=False,
):
    """处理图片并输出到指定路径。

    参数说明
    --------
    transparent : bool
        是否使用透明背景，默认为 True。
        PNG 格式支持完整透明度；GIF 仅支持 1-bit 透明；JPG 不支持透明，
        若 format 为 JPG 则强制使用白色背景。
    """
    try:
        img = Image.open(input_path)

        # JPG 不支持透明通道，强制关闭透明
        if format.upper() in ("JPG", "JPEG"):
            transparent = False

        if is_animated and format.upper() == "GIF":
            frames = []
            for frame in ImageSequence.Iterator(img):
                if transparent:
                    frame = frame.convert("RGBA")
                else:
                    frame = frame.convert("RGB")

                frame.thumbnail(size, Image.Resampling.LANCZOS)
                bg_color = (255, 255, 255, 0) if transparent else (255, 255, 255)
                mode = "RGBA" if transparent else "RGB"
                new_frame = Image.new(mode, size, bg_color)
                offset = (
                    (size[0] - frame.size[0]) // 2,
                    (size[1] - frame.size[1]) // 2,
                )
                new_frame.paste(frame, offset, frame if transparent else None)
                frames.append(new_frame)

            if frames:
                duration = img.info.get("duration", 100)
                frames[0].save(
                    output_path,
                    format="GIF",
                    append_images=frames[1:],
                    save_all=True,
                    duration=duration,
                    loop=0 if loop_gif else 1,
                    disposal=2,  # 每帧清除为背景，保证透明正确叠加
                )
                file_kb = os.path.getsize(output_path) / 1024
                if file_kb > max_kb:
                    print(
                        f"Warning: Animated GIF {output_path} exceeds {max_kb} KB "
                        f"({file_kb:.2f} KB). Consider reducing frames or resolution."
                    )
                print(
                    f"Successfully processed animated GIF: {output_path} "
                    f"({file_kb:.2f} KB)"
                )
                return True
            else:
                print(f"Error: No frames found in animated GIF {input_path}")
                return False

        else:
            # 静态图处理
            if transparent:
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")

            img.thumbnail(size, Image.Resampling.LANCZOS)

            bg_color = (255, 255, 255, 0) if transparent else (255, 255, 255)
            mode = "RGBA" if transparent else "RGB"
            new_img = Image.new(mode, size, bg_color)

            offset = (
                (size[0] - new_img.size[0] + new_img.size[0] - img.size[0]) // 2,
                (size[1] - new_img.size[1] + new_img.size[1] - img.size[1]) // 2,
            )
            # 简化偏移计算
            offset = (
                (size[0] - img.size[0]) // 2,
                (size[1] - img.size[1]) // 2,
            )
            new_img.paste(img, offset, img if transparent else None)

            quality = 95
            while True:
                if format.upper() == "PNG":
                    new_img.save(output_path, format="PNG", optimize=True)
                else:
                    # JPG 需要先转 RGB
                    save_img = new_img.convert("RGB") if transparent else new_img
                    save_img.save(output_path, format=format, quality=quality)

                if os.path.getsize(output_path) <= max_kb * 1024 or quality <= 10:
                    break
                quality -= 5

            print(
                f"Successfully processed: {output_path} "
                f"({os.path.getsize(output_path) / 1024:.2f} KB)"
            )
            return True

    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 7:
        print(
            "Usage: python3 process_sticker.py "
            "<input> <output> <width> <height> <format> <max_kb> "
            "[transparent=True] [is_animated=False] [loop_gif=False]"
        )
        sys.exit(1)

    input_p = sys.argv[1]
    output_p = sys.argv[2]
    w = int(sys.argv[3])
    h = int(sys.argv[4])
    fmt = sys.argv[5].upper()
    kb = int(sys.argv[6])
    # transparent 默认 True（与函数签名一致）
    trans = sys.argv[7].lower() == "true" if len(sys.argv) > 7 else True
    is_anim = sys.argv[8].lower() == "true" if len(sys.argv) > 8 else False
    loop_g = sys.argv[9].lower() == "true" if len(sys.argv) > 9 else False

    process_image(input_p, output_p, (w, h), fmt, kb, trans, is_animated=is_anim, loop_gif=loop_g)
