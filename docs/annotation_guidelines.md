# Annotation Guidelines

## Project
Practice bounding-box annotation for object-detection classes in a synthetic street-scene dataset.

## Classes
- `person`
- `car`
- `truck`
- `bus`
- `motorcycle`

## Bounding-box rules
1. Draw one axis-aligned rectangle per visible target object.
2. Include the full visible object, including wheels/limbs where visible.
3. Keep boxes tight; avoid large amounts of background.
4. Assign exactly one class from the approved class list.
5. Do not label background objects or decorative skyline elements.
6. If an object is partially outside the image, box only the visible extent.
7. Do not create duplicate boxes for one object.

## Quality review checklist
- Every target object has a box.
- No non-target object is labelled.
- Class label matches the object.
- Box covers the object and is reasonably tight.
- No duplicate annotations.
- Coordinates are within image boundaries.
- YOLO values are normalized to [0, 1].

## Important
The supplied labels are starter annotations for this synthetic practice dataset. For portfolio practice, import the images into CVAT or LabelImg, review/edit the boxes, and record your own quality-review results before describing it as a completed annotation exercise.
