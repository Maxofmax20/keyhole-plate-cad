# Keyhole Sliding Number Plate Mount — concept V0.1

**Original dimensional prototype** developed from visual references and a proposed measurement set, **not** an official KLIQ CO CAD file or reverse-engineered measured scan.

## What the mechanism does

1. Attach the button to the bumper-side mounting point, and the keyhole plate to the back of the number plate.
2. Align the round opening at the **bottom** of the female plate with the button head.
3. Seat the head, then push the number plate **down 15 mm**. The Ø17.8 mm head is retained inside an undercut channel beneath the 9.2 mm slot; the Ø7.8 mm neck slides in the slot.
4. Lift the plate upward again to return to the larger opening for removal.

## Proposed dimensions (all mm)

- Female keyhole plate: **44 × 44 × 8.5**
- Round entry (bottom): **Ø19.6**
- Neck slot (upwards): **9.2 wide**
- Slide travel: **15**
- Internal head channel: **18.8 wide**, z=2.75–6.25
- Male square backing: **40 × 40 × 2.8**
- Male neck: **Ø7.8 × 3.0**
- Male head: **Ø17.8 × 2.6**

## Files

- `keyhole_quick_release.blend`: complete editable Blender scene and animation keyframes
- `female_keyhole_plate.stl`: prototype female mount
- `male_button.stl`: prototype male mount (separate touching shells; confirm union in slicer)
- `preview.png`: Blender-rendered image
- `keyhole_assembly.mp4`: animated demonstration
- `model_and_render.py`: parameter-defined Blender procedural source

## Safety and use

**Concept prototype only.** No physical fit, tensile, adhesive, fatigue, weathering, or road-speed testing has been performed. Check legal visibility, secure mounting and retention before use on a moving vehicle. Recheck model dimensions with a caliper and test prints. A secondary anti-lift/safety retainer may be needed for roads.

## Re-render on the VPS

Blender runs in a self-contained Docker image to avoid changing existing hosted services; project files live in `/data/keyhole-plate-blender`. Use the included `Dockerfile` to rebuild the local renderer if needed.
