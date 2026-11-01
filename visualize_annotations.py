from pathlib import Path
from PIL import Image, ImageDraw
import yaml

ROOT = Path(__file__).resolve().parent
IMAGE_DIR = ROOT / "images"
LABEL_DIR = ROOT / "labels"
OUTPUT_DIR = ROOT / "annotated_preview"
OUTPUT_DIR.mkdir(exist_ok=True)

classes = (ROOT / "classes.txt").read_text(encoding="utf-8").splitlines()

image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
images = [p for p in IMAGE_DIR.rglob("*") if p.suffix.lower() in image_extensions]

for image_path in images:
    label_path = LABEL_DIR / f"{image_path.stem}.txt"

    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)
    width, height = image.size

    if label_path.exists():
        for line in label_path.read_text(encoding="utf-8").splitlines():
            values = line.strip().split()
            if len(values) != 5:
                continue

            class_id, x_center, y_center, box_width, box_height = map(float, values)
            x_center *= width
            y_center *= height
            box_width *= width
            box_height *= height

            x1 = int(x_center - box_width / 2)
            y1 = int(y_center - box_height / 2)
            x2 = int(x_center + box_width / 2)
            y2 = int(y_center + box_height / 2)

            draw.rectangle((x1, y1, x2, y2), outline="red", width=3)

            class_name = classes[int(class_id)] if int(class_id) < len(classes) else str(int(class_id))
            draw.text((x1, max(0, y1 - 15)), class_name, fill="red")

    image.save(OUTPUT_DIR / image_path.name)

print(f"Created previews for {len(images)} images in: {OUTPUT_DIR}")