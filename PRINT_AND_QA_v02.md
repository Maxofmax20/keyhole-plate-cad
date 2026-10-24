# v0.2 Print Readiness & Retention Review / مراجعة التصميم للطباعة

**Status: DIGITAL GEOMETRY PASSED — PHYSICAL ROAD-USE SAFETY UNVERIFIED.**
**الحالة: سليم هندسيًا وجاهز لطباعة عينة اختبار، وليس معتمدًا بعد للتركيب على سيارة أثناء القيادة.**

## Findings from actual Blender STL inspection

| Test | v0.1 | v0.2 |
|---|---|---|
| Male components | Three disconnected solids | ONE connected closed manifold solid |
| Female components | One solid | One closed manifold solid |
| Non-manifold edges (male/female) | 0 / 0 (but male had three shells) | **0 / 0** |
| Female / male interference during sliding | Not formally evaluated | **0 mm³** at head centre Y=-7,-3,0,4,8 mm |
| Retaining-pin impact | No second lock | **No collision** when engaged at Y=8; **positive collision** on withdrawal at Y=3,0,-3 |
| Male mounting screw | None | Ø3.4 mm through-hole + Ø6.6 mm counterbore for a low-profile M3 screw |

## Concept size and tolerances (mm)

- Female square backplate 44 × 44 × 8.5
- Male square backplate 40 × 40 × 2.8
- Male button head Ø17.8 × 2.6; head channel width 18.8 (0.5 mm per side nominal radial clearance)
- Male neck Ø7.8; female retaining slot 9.2 (0.7 mm per side nominal clearance)
- Sliding travel 15 mm, lower round-entry Ø19.6
- Head chamber top nominal Z=6.25 and head top assembled nominal Z=5.90: 0.35 mm gap (sensitive to dimensional error)
- Safety bar transverse hole Ø3.3 mm, side entry at local Y=-3.5 mm, Z=4.25 mm

## Materials / printing FIRST PROTOTYPE (not certified settings)

1. Print ONE male/female pair first, not a full vehicle set.
2. Material: PETG for an easy initial functional prototype; ASA can be more suitable for prolonged outdoor heat/UV exposure when printed with a properly enclosed/ventilated machine. PLA is not recommended for hot parked-vehicle use.
3. First trial: 0.4 mm nozzle; 0.20 mm layers; 5–6 walls; 5+ top/bottom layers. Male button 80–100% infill, female 45–70%. Use the filament vendor's tested slicer temperature and cooling profile rather than untested generic temperatures.
4. Orient both square backs on the bed. **Support is likely needed** under the button head and inside the female's hidden undercut pocket. Keep support out of the functional bearing surfaces as much as possible and remove cleanly before assembly. PETG support can bond stubbornly.
5. Check a slicer preview for islands, unsupported internal ceilings, mounting holes, and adequate thin-wall perimeters before printing. Digital STL manifold checks are not a slicer verification.
6. Use a caliper to verify actual head, neck, inner passage and hole dimensions; deburr gently and check free sliding from round opening into narrow upper channel. Do NOT force a binding fit.
7. On assembled pair, check sliding, rattle, wobble, alignment, and accidental reverse-upward travel. Optional thin compressible anti-rattle shim requires measured fit and must not force joint apart.

## Secondary mechanical retainer

**Keyhole gravity/friction ALONE is not positive anti-lift retention.** The v0.2 female part adds a transverse Ø3.3 mm path for an optional M3 metallic locking bar/pin. This path crosses the neck/head return travel after the button has moved up within the slot (relative to female), preventing the button from returning to the large entry opening. Verify correct bar length, retention at both ends, side access, and no interference with the number plate or bumper geometry. The retainer is **not included as a 3D-printed part**. Do not assume adding the bar makes the system road-safe without physical tests.

## Installation and physical validation still required

- Fit against actual bumper curvature/plate flatness and existing screw position.
- Inspect adhesive compatibility, tape type, surface preparation, bond contact, environmental resistance and cure per chosen adhesive's manufacturer. The 3M VHB guidance describes full bond buildup over around 72 h at room temperature under suitable conditions, but that is not a validation of THIS application.
- Verify M3 fastener geometry and local vehicle mounting threads before fitting; the printed male backing needs positive fixation, not just a loose screw.
- Conduct non-road fit trials and repeated cycling, pull/peel/shear checks, controlled vibration/shock checks, and hot/cold/weather exposure tests with a representative sample before making any in-service retention claim.
- Confirm number-plate fastening and visibility requirements for your location. Avoid road use until an appropriate retention solution is verified.

## Limitations

No load cell tests, real print calibration, fatigue cycling, finite-element analysis, wind tunnel, adhesive qualification, certified fastener torque, or legal vehicle-specific assessment has been performed. The dimensions are original **estimated** CAD concept dimensions; NOT official KLIQ CO product specifications.

## Files

- `male_button_v02.stl` and `female_keyhole_plate_v02.stl`: closed manifold meshes, concept scale in millimetres.
- `keyhole_quick_release_v02.blend`: edited animated Blender scene.
- `model_v02.py`: procedural source.
- `audit_v02.py`: mesh checks, and `verify_fit.py`: collision / anti-lift checks.
- `preview_v02.png`: render.
