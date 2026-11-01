# Image Annotation for Object Detection

A beginner portfolio mini-project for practicing image review, object identification, bounding-box labels, and annotation quality checks.

## Dataset
- 12 synthetic street-scene images (640×360)
- Classes: person, car, truck, bus, motorcycle
- 50 starter bounding boxes
- YOLO-format labels in `labels/`

## Folder structure
```text
image_annotation_object_detection/
├── images/                  # Synthetic practice images
├── labels/                  # YOLO-format starter annotations
├── docs/
│   ├── annotation_guidelines.md
│   └── project_report.md
├── annotation_summary.csv
├── classes.txt
├── data.yaml
└── validate_yolo.py
```

## How to review the annotations
1. Open the images and labels in CVAT or LabelImg.
2. Review each box for completeness, tightness, class correctness, and duplicates.
3. Edit annotations where needed and record issues in your own review notes.
4. Run the validation script:
   ```bash
   python validate_yolo.py
   ```

## Resume use
Only add this project to your resume after personally reviewing/editing the annotations. A truthful description could be:
> Practiced bounding-box annotation and class labeling on a synthetic street-scene dataset; reviewed annotations for label consistency, box accuracy, and coordinate validity.

This is a learning project, not professional annotation experience.
