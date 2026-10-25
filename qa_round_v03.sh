#!/usr/bin/env bash
set -euo pipefail
cd /data/keyhole-plate-blender
run_blender() {
  docker run --rm --network none --cpus=1 --memory=3g -v /data/keyhole-plate-blender:/work -w /work \
    local/keyhole-blender:4.0 blender -b -t 2 --python "$1" 2>&1
}
AUDIT="$(run_blender audit_round_v03.py)"
FIT="$(run_blender verify_round_v03.py)"
SCREW="$(run_blender verify_M4_screw_v03.py)"
printf '%s\n' "$AUDIT" | grep '^AUDIT'
printf '%s\n' "$FIT" | grep -E '^(ASSEMBLY|SAFETY_PIN)_CROSS_SECTION'
printf '%s\n' "$SCREW" | grep -E '^(SCREW_ENVELOPE|MAX_HEAD|M4_SHANK|MAX_M4_HEAD|FIXTURE_WARNING)'
echo "$AUDIT" | grep -E 'AUDIT male_round_button_M4_v03.stl .*components 1 .*nonmanifold_edges 0' >/dev/null
echo "$AUDIT" | grep -E 'AUDIT female_keyhole_plate_v02.stl .*components 1 .*nonmanifold_edges 0' >/dev/null
if echo "$FIT" | grep ASSEMBLY_CROSS_SECTION | grep -Ev 'intersection_mm3 0.0 nm 0' ; then echo 'FAIL: path collision'; exit 1; fi
echo "$FIT" | grep 'SAFETY_PIN_CROSS_SECTION head_relative_Y 8 intersection_mm3 0.0' >/dev/null
echo "$SCREW" | grep -E 'SCREW_ENVELOPE .*collision_mm3 0.0' >/dev/null
echo 'PASS: CLOSED STL, M4 BOLT ENVELOPE, ROUND MALE + OLD FEMALE DIGITAL FIT'
echo 'NOT QUALIFIED FOR VEHICLE ROAD USE'
