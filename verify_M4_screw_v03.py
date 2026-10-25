import bpy,bmesh,math
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
bpy.ops.wm.stl_import(filepath='/work/male_round_button_M4_v03.stl')
part=bpy.context.object
def add_cylinder(radius,z0,z1,name):
 bpy.ops.mesh.primitive_cylinder_add(vertices=128,radius=radius,depth=(z1-z0),location=(0,0,(z0+z1)/2))
 o=bpy.context.object;o.name=name
 return o
def volume_intersection(a,b):
 temp=a.copy();temp.data=a.data.copy();bpy.context.collection.objects.link(temp)
 m=temp.modifiers.new('screw_collision','BOOLEAN');m.operation='INTERSECT';m.solver='EXACT';m.object=b
 bpy.context.view_layer.objects.active=temp;bpy.ops.object.modifier_apply(modifier=m.name)
 bm=bmesh.new();bm.from_mesh(temp.data);v=bm.calc_volume(signed=False);bm.free()
 bpy.data.objects.remove(temp,do_unlink=True)
 return v
shaft=add_cylinder(2.0,-10,6.0,'M4 nominal metal screw shaft Ø4.0')
head=add_cylinder(3.8,6.0,8.2,'ISO 7380-1 M4 MAX diameter 7.6 height 2.2')
bpy.context.view_layer.update()
a=volume_intersection(part,shaft);b=volume_intersection(part,head)
print('SCREW_ENVELOPE', 'M4_ISO_7380-1', 'head_Ø7.6_height_2.2', 'shaft_Ø4.0','model_Ø4.5_hole_Ø8.4_counterbore','collision_mm3',round(a+b,7),flush=True)
assert a+b < 0.0001,'Screw head or shaft interferes with printed part'
# screw head shoulder rests at z6; counterbore top z8.4 =>0.2mm below top
print('MAX_HEAD_BELOW_PRINTED_BUTTON_TOP_MM', round(8.4-8.2,4),flush=True)
print('M4_SHANK_NOMINAL_RADIAL_CLEARANCE_MM',round((4.5-4.0)/2,4),flush=True)
print('MAX_M4_HEAD_NOMINAL_RADIAL_CLEARANCE_MM',round((8.4-7.6)/2,4),flush=True)
print('FIXTURE_WARNING','M4 threads / length on vehicle must be confirmed. A 4.8 self-tapping screw is NOT interchangeable with M4.',flush=True)
