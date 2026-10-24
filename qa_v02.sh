#!/usr/bin/env bash
set -euo pipefail
cd /data/keyhole-plate-blender
CONTAINER=local/keyhole-blender:4.0
run_blender() {
  docker run --rm --network none --cpus=1.0 --memory=3g \
    -v /data/keyhole-plate-blender:/work -w /work \
    "$CONTAINER" blender -b -t 2 --python "$1" 2>&1
}
AUDIT="$(run_blender audit_v02.py)"
FIT="$(run_blender verify_fit.py)"
printf "%s\n" "$AUDIT" | grep -E 'AUDIT (male_button_v02|female_keyhole_plate_v02)'
printf "%s\n" "$FIT" | grep -E '(ASSEMBLY_CROSS_SECTION|SAFETY_PIN_CROSS_SECTION)'
echo "$AUDIT" | grep -E 'AUDIT male_button_v02.stl .*components 1 .*nonmanifold_edges 0' >/dev/null
echo "$AUDIT" | grep -E 'AUDIT female_keyhole_plate_v02.stl .*components 1 .*nonmanifold_edges 0' >/dev/null
if echo "$FIT" | grep 'ASSEMBLY_CROSS_SECTION' | grep -Ev 'intersection_mm3 0.0 '; then
 echo 'FAIL: interference in slide path' >&2; exit 1
fi
echo "$FIT" | grep 'SAFETY_PIN_CROSS_SECTION head_relative_Y 8 intersection_mm3 0.0' >/dev/null
echo "$FIT" | grep 'SAFETY_PIN_CROSS_SECTION head_relative_Y 0 intersection_mm3 92.' >/dev/null
echo "PASS - DIGITALLY MANIFOLD AND COLLISION-FREE; NO REAL-WORLD LOAD VALIDATION"
