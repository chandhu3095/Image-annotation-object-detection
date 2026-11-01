from pathlib import Path

ROOT = Path(__file__).parent
IMAGE_DIR = ROOT / "images"
LABEL_DIR = ROOT / "labels"
NUM_CLASSES = 5
errors = []
total = 0

for label_file in sorted(LABEL_DIR.glob("*.txt")):
    image_file = IMAGE_DIR / (label_file.stem + ".png")
    if not image_file.exists():
        errors.append(f"Missing image for {label_file.name}")
    for line_no, line in enumerate(label_file.read_text().splitlines(), 1):
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) != 5:
            errors.append(f"{label_file.name}:{line_no}: expected 5 values")
            continue
        try:
            cls = int(parts[0])
            vals = [float(v) for v in parts[1:]]
        except ValueError:
            errors.append(f"{label_file.name}:{line_no}: non-numeric value")
            continue
        if not 0 <= cls < NUM_CLASSES:
            errors.append(f"{label_file.name}:{line_no}: class id out of range")
        if any(v < 0 or v > 1 for v in vals):
            errors.append(f"{label_file.name}:{line_no}: normalized coordinate outside [0,1]")
        if vals[2] <= 0 or vals[3] <= 0:
            errors.append(f"{label_file.name}:{line_no}: box width/height must be positive")
        total += 1

if errors:
    print("Validation issues:")
    print("\\n".join(errors))
else:
    print(f"Validation passed: {total} bounding boxes across {len(list(LABEL_DIR.glob('*.txt')))} label files.")
