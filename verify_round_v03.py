import bpy,bmesh, math
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
bpy.ops.wm.stl_import(filepath='/work/female_keyhole_plate_v02.stl')
female=bpy.context.object;female.name='female'
bpy.ops.wm.stl_import(filepath='/work/male_round_button_M4_v03.stl')
male=bpy.context.object;male.name='male'
def volume_intersection(a,b):
    tmp=a.copy();tmp.data=a.data.copy();bpy.context.collection.objects.link(tmp)
    mod=tmp.modifiers.new('collision-check','BOOLEAN');mod.operation='INTERSECT';mod.solver='EXACT';mod.object=b
    bpy.context.view_layer.objects.active=tmp
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bm=bmesh.new();bm.from_mesh(tmp.data)
    vol=bm.calc_volume(signed=False)
    nm=sum(1 for e in bm.edges if not e.is_manifold)
    bm.free()
    bpy.data.objects.remove(tmp,do_unlink=True)
    return vol,nm
male.rotation_euler=(math.pi,0,0)
for y in (-7,-3,0,4,8):
    male.location=(0,y,11.7)
    bpy.context.view_layer.update()
    v,n=volume_intersection(female,male)
    print('ASSEMBLY_CROSS_SECTION','head_relative_Y',y,'intersection_mm3',round(v,6),'nm',n,flush=True)
# Verify a real Ø3 mm transverse bar clears in locked state but physically blocks withdrawal.
bpy.ops.mesh.primitive_cylinder_add(vertices=64,radius=1.5,depth=46,location=(0,-3.5,4.25),rotation=(0,math.pi/2,0))
pin=bpy.context.object;pin.name='external removable M3 safety pin'
for y in (8,3,0,-3):
    male.location=(0,y,11.7);bpy.context.view_layer.update()
    v,n=volume_intersection(pin,male)
    print('SAFETY_PIN_CROSS_SECTION','head_relative_Y',y,'intersection_mm3',round(v,6),flush=True)
