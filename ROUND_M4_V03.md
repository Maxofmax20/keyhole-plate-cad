# Round screw-mounted male button — v0.3 (M4 ISO 7380-1)

This is an **additional option** for the original keyhole number-plate system, based on the supplied photograph of a round screw-mounted fitting. The OLD FEMALE is unchanged: reuse `female_keyhole_plate_v02.stl`.

## Fit and dimensional interface (mm)

| Feature | Old female / original system | New round M4 male |
|---|---|---|
| Round entry clearance | Ø19.6 | Ø17.8 head |
| Narrow slide throat | 9.2 wide | Ø7.8 neck |
| Retained internal head channel | 18.8 wide | Ø17.8 head |
| Sliding stroke | 15 | 15 (unchanged) |
| Mounting flange | N/A | Ø28.0 × 2.8 (round) |
| Visible neck | N/A | Ø7.8 × 3.0 |
| Head thickness | N/A | Ø17.8 × 2.6 |
| Total male height | N/A | 8.4 |

### Standard fastener selected

- **ISO 7380-1 M4 button-head hex socket machine screw**, metric pitch **0.7 mm**, hex-key nominal **2.5 mm**, maximum nominal head diameter **7.6 mm**, head height **2.2 mm**.
- Normal pass-through clearance **Ø4.5 mm**, from the ISO 273 metric clearance series.
- Head pocket **Ø8.4 × 2.4 mm**, recesses a maximum-height screw head by approximately **0.2 mm**. Does not include a captive nut/insert: threads must exist in a compatible bumper/bracket mounting point.
- Screw length depends on your vehicle's original anchoring hardware. A nominal M4×16 screw would protrude approximately 10 mm beyond the backing flange when seated, which may be too long or too short; verify the actual anchor and clearances first.
- **IMPORTANT:** M4 is **a standard fastener**, but it is **not a universal number-plate screw**. Vehicles may use M5, M6 or self-tapping 4.8 mm screws or other fasteners. Those are *not* interchangeable with this M4 mounting version. Do not force M4 into an incorrect threaded anchor or self-tapping hole.

## Compatibility & digital checks (performed on VPS)

- Newly manufactured round male STL **one connected closed manifold**, **0 non-manifold edges**.
- Original female v0.2 STL **one connected closed manifold**, **0 non-manifold edges**.
- Intersection between new male and v0.2 female is **0 mm³** at five representative head positions along the keyhole travel.
- Standard M4 screw envelope (Ø4.0 shaft, Ø7.6 × 2.2 head) has **0 mm³** material collision with new male STL.
- Original v0.2 female optional lateral anti-lift pin: collision-free at fully inserted relative head-Y=+8, creates positive obstruction to reverse travel at earlier steps. Physical access, reliable retention, adhesive and load capacity still require testing.

## Files

- `male_round_button_M4_v03.stl` — **new** printable round screw-mounted male piece.
- `female_keyhole_plate_v02.stl` — **original** mating female piece, UNCHANGED.
- `keyhole_round_M4_v03.blend` — editable Blender assembly + original animation, with the round alternative.
- `model_round_M4_v03.py` — procedural CAD generation.
- `preview_round_M4_v03.png` — real Blender render.
- `audit_round_v03.py`, `verify_round_v03.py`, `verify_M4_screw_v03.py` — repeatable geometry and virtual-fit tests.

## Printing & physical qualification

1. Print a **single trial pair** in PETG (prototype); ASA may better suit prolonged outdoor UV/heat when printed properly. PLA should not be treated as qualified for a hot vehicle exterior.
2. Suggested **test settings**: 0.4 mm nozzle, 0.20 mm layer, 5–6 walls, 80–100% infill for the small male, flat circular flange on bed. Support under head overhang may be necessary.
3. Check your slicer preview for unsupported layers and wall continuity (STL manifold test does NOT check slicer toolpaths).
4. Measure the finished head, neck and screw head with a caliper; trial-fit and check reverse-upward release and rattling. Try any lateral metal retention bolt on a bench before fitting the plate; it must be reachable and secure.
5. Real-world force, cyclic vibration, heat, adhesive bonding of female piece, and vehicle/legal plate mounting have **not been validated**. **Not approved for road service** until a suitable positive retainer and physical tests demonstrate secure mounting.

## Sources for hardware sizes

- ISO 7380-1 manufacturer's dimensional data (M4 Ø7.6 / 2.2, M4×0.7): https://eshop-ro.boellhoff.com/out/media/pdf/ISO_7380-1_Stahl_10.9_Innensechskant___en.pdf
- ISO 273 clearance sizes including M4 normal Ø4.5: https://www.albanycountyfasteners.com/media/6b/b8/g0/1764944339/clearance-hole-chart.pdf
- Examples of actual automotive number-plate fasteners with 4.8 mm self-tapping shanks: https://media.swg.de/Marketing/Katalog/KFZ_KAT_EN_77720040075_DINTeile.pdf
