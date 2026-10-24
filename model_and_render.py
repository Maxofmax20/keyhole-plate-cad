import bpy, math, os, sys, struct
from mathutils import Vector
from math import radians, sin, cos

OUT = "/work"
FRAMES = 120
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
scene = bpy.context.scene
scene.render.engine = "BLENDER_WORKBENCH"
scene.display.shading.light = "STUDIO"
scene.display.shading.color_type = "MATERIAL"
scene.display.shading.show_shadows = True
scene.display.shading.show_cavity = True
scene.display.shading.cavity_type = "BOTH"
scene.display.shading.background_type = "WORLD"
scene.cycles.device = "CPU"
scene.cycles.samples = 9
scene.cycles.use_denoising = False
scene.render.resolution_x = 960
scene.render.resolution_y = 540
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.film_transparent = False
scene.frame_start = 1
scene.frame_end = FRAMES
scene.render.fps = 24
scene.unit_settings.system = "METRIC"
scene.unit_settings.scale_length = 0.001
scene.view_settings.view_transform = "Standard"
scene.view_settings.look = "Medium High Contrast"
scene.view_settings.exposure = 0
scene.view_settings.gamma = 1
scene.render.image_settings.color_mode = "RGBA"

def mat(name, rgb, metallic=0, roughness=0.45):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*rgb, 1)
    m.use_nodes = True
    p = m.node_tree.nodes.get("Principled BSDF")
    p.inputs["Base Color"].default_value = (*rgb, 1)
    p.inputs["Metallic"].default_value = metallic
    p.inputs["Roughness"].default_value = roughness
    return m

black = mat("ASA matte black | concept", (0.10,0.115,0.137),0.14,0.52)
charcoal = mat("Graphite black | button", (0.16,0.18,0.21),0.26,0.42)
deepblack = mat("Undercut recess", (0.015,0.019,0.028),0.08,0.6)
floorMat = mat("Navy studio floor", (0.085,0.10,0.135),0.2,0.55)
accent = mat("Cyan alignment accent", (0.08,0.65,0.93),0.3,0.28)

def active(obj):
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

def bevel(obj, radius=0.75, segments=4):
    mod = obj.modifiers.new("Soft machined edges", 'BEVEL')
    mod.width = radius
    mod.segments = segments
    mod.affect = 'EDGES'
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=mod.name)
    mod = obj.modifiers.new("Weighted normals", 'WEIGHTED_NORMAL')
    mod.keep_sharp = True
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=mod.name)
    return obj

def box(name, dims, xyz, material=None, r=0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=xyz)
    o = bpy.context.object
    o.name=name
    o.dimensions=dims
    active(o); bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if material: o.data.materials.append(material)
    if r: bevel(o, r)
    return o

def cyl(name, radius, depth, xyz, material=None, vert=96, r=0):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vert, radius=radius, depth=depth, location=xyz)
    o=bpy.context.object; o.name=name
    if material: o.data.materials.append(material)
    if r: bevel(o,r,3)
    return o

def subtract(host, cutter):
    mod = host.modifiers.new("Precision keyhole cut", 'BOOLEAN')
    mod.operation="DIFFERENCE"; mod.solver="EXACT"; mod.object=cutter
    bpy.context.view_layer.objects.active=host
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(cutter, do_unlink=True)

# FEMALE: 44 x 44 x 8.5 mm. Wide ENTRY at y=-7; narrow track UP 15 mm.
plate = box("FEMALE | adhesive-backed 44 x 44 x 8.5 mm", (44,44,8.5), (0,0,4.25), black,1.65)
subtract(plate, cyl("entry Ø19.6", 9.8, 13, (0,-7,4.25)))
# Under-cut chamber sits BELOW the narrow exposed slot; retains Ø17.8 head.
subtract(plate, box("head tunnel", (18.8,15.0,3.50),(0,0.5,4.50)))
subtract(plate, cyl("upper head pocket",9.4,3.50,(0,8,4.5)))
# Exposed Ø9.2 neck slot is a channel leading UP from lower entry.
subtract(plate, box("narrow retaining throat", (9.2,15.0,4.1),(0,0.5,8.0)))
subtract(plate, cyl("slot rounded top",4.6,4.1,(0,8.0,8.0)))
# smooth visible cut rim is not post-beveled in this dimensional concept

# MALE: 40 x 40 x 2.8 mm backing, neck Ø7.8, head Ø17.8.
base = box("MALE | square backing 40 x 40 x 2.8 mm", (40,40,2.8), (0,0,1.4), charcoal,1.6)
neck = cyl("MALE | Ø7.8 neck 3.0 mm",3.9,3.0,(0,0,4.3),charcoal,96,0.35)
head = cyl("MALE | Ø17.8 head 2.6 mm",8.9,2.6,(0,0,7.1),charcoal,96,0.48)
femaleRig=bpy.data.objects.new("Animation rig | moving NUMBER PLATE",None)
maleRig=bpy.data.objects.new("Animation rig | fixed BUMPER BUTTON",None)
scene.collection.objects.link(femaleRig)
scene.collection.objects.link(maleRig)
femaleRig.empty_display_size=8
maleRig.empty_display_size=8
plate.parent=femaleRig
for p in [base,neck,head]: p.parent=maleRig
maleRig.rotation_euler=(0,0,0)

def keyobj(obj,frame,xyz):
    obj.location=xyz
    obj.keyframe_insert(data_path="location",frame=frame)
def interpolate(obj):
    if obj.animation_data and obj.animation_data.action:
        for fc in obj.animation_data.action.fcurves:
            for key in fc.keyframe_points:
                key.interpolation="BEZIER"
                key.handle_left_type="AUTO_CLAMPED"
                key.handle_right_type="AUTO_CLAMPED"

# wide opening y=-7, initially positioned at global y=0 => plate +7.
# then plate MOVES DOWN 15 mm; fixed bumper button reaches narrow end.
for f,xyz in [(1,(-29,7,0)),(25,(-29,7,0)),(48,(0,7,0)),(75,(0,7,0)),(105,(0,-8,0)),(FRAMES,(0,-8,0))]:
    keyobj(femaleRig,f,xyz)
for f,xyz in [(1,(34,0,34)),(25,(34,0,34)),(48,(0,0,31)),(68,(0,0,11.7)),(FRAMES,(0,0,11.7))]:
    keyobj(maleRig,f,xyz)
for f,ang in [(1,0),(24,0),(48,math.pi),(FRAMES,math.pi)]:
    maleRig.rotation_euler=(ang,0,0)
    maleRig.keyframe_insert(data_path="rotation_euler",frame=f)
interpolate(maleRig); interpolate(femaleRig)

# Premium studio set
studio=box("Studio backdrop",(250,250,1.0),(0,0,-10.5),floorMat,0)
def light(name,loc,power,color,size):
    data=bpy.data.lights.new(name,"AREA")
    data.energy=power; data.color=color; data.shape='DISK'; data.size=size
    obj=bpy.data.objects.new(name,data);scene.collection.objects.link(obj)
    obj.location=loc
    obj.rotation_euler=(Vector((0,0,0))-obj.location).to_track_quat("-Z","Y").to_euler()
light("softbox left",(-40,-30,110),1250,(0.83,0.92,1.0),75)
light("cyan rim",(55,40,85),1100,(0.45,0.85,1.0),65)
light("warm fill",(5,-65,60),800,(1.0,0.92,0.84),60)
world = bpy.data.worlds.new("Soft grey ambience") if not bpy.data.worlds else bpy.data.worlds[0]
scene.world=world
world.use_nodes=True
bg=world.node_tree.nodes.get("Background")
bg.inputs["Color"].default_value=(0.13,0.18,0.26,1)
bg.inputs["Strength"].default_value=.6

cam_data=bpy.data.cameras.new("Technical presentation")
camera=bpy.data.objects.new("Technical presentation",cam_data);scene.collection.objects.link(camera)
scene.camera=camera
cam_data.type="ORTHO"
cam_data.ortho_scale=111
cam_data.lens=45
def view_at(frame, pos, target=(0,0,4), scale=105):
    camera.location=pos
    direction=Vector(target)-camera.location
    camera.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()
    cam_data.ortho_scale=scale
    camera.keyframe_insert(data_path="location",frame=frame)
    camera.keyframe_insert(data_path="rotation_euler",frame=frame)
    cam_data.keyframe_insert(data_path="ortho_scale",frame=frame)
view_at(1,  (65,-100,119),(0,0,10),115)
view_at(48, (69,-104,117),(0,0,10),96)
view_at(75, (72,-93,120),(0,0,6),80)
view_at(106,(40,-115,126),(0,0,6),80)
view_at(120,(-34,-96,130),(0,0,6),82)

# Actual CAD-like mesh dimensions encoded in the Blender file.
for ob in [plate,base,neck,head]:
    ob["part_family"]="Keyhole Number Plate Release"
    ob["units"]="mm"
    ob["prototype_only"]="Dimensions estimated; test fit and vibration before road use."
plate["entry_diameter_mm"]=19.6
plate["neck_slot_width_mm"]=9.2
plate["sliding_travel_mm"]=15.0
head["button_head_diameter_mm"]=17.8
neck["neck_diameter_mm"]=7.8

def stl_binary(filepath, objects, rig):
    scene.frame_set(68)
    rig_inv=rig.matrix_world.inverted()
    alltris=[]
    for ob in objects:
        ob.data.calc_loop_triangles()
        transf=rig_inv @ ob.matrix_world
        for tr in ob.data.loop_triangles:
            vs=[transf @ ob.data.vertices[i].co for i in tr.vertices]
            n=(vs[1]-vs[0]).cross(vs[2]-vs[0])
            if n.length: n.normalize()
            alltris.append((n,vs))
    with open(filepath,"wb") as f:
        f.write(b"Keyhole quick release concept | mm".ljust(80,b"\0"))
        f.write(struct.pack("<I",len(alltris)))
        for n,vs in alltris:
            f.write(struct.pack("<12fH",*(list(n)+list(vs[0])+list(vs[1])+list(vs[2])+[0])))
    print("EXPORTED",filepath,"triangles",len(alltris))

scene.frame_set(68)
stl_binary(OUT+"/female_keyhole_plate.stl",[plate],femaleRig)
stl_binary(OUT+"/male_button.stl",[base,neck,head],maleRig)
scene.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=OUT+"/keyhole_quick_release.blend")
scene.frame_set(18)
scene.render.filepath=OUT+"/preview.png"
bpy.ops.render.render(write_still=True)
print("PREVIEW_DONE",OUT+"/preview.png")
if "--animation" in sys.argv:
    os.makedirs(OUT+"/frames", exist_ok=True)
    for i, frame in enumerate(range(1,FRAMES+1,3)):
        scene.frame_set(frame)
        scene.render.filepath=OUT+"/frames/frame_%04d.png" % i
        bpy.ops.render.render(write_still=True)
        print("FRAME_DONE",i,frame,flush=True)
    print("ANIMATION_FRAMES_DONE",flush=True)
