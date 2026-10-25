import bpy,bmesh
from collections import Counter
for fname in ('male_round_button_M4_v03.stl','female_keyhole_plate_v02.stl'):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.wm.stl_import(filepath='/work/'+fname)
    objs=[o for o in bpy.context.scene.objects if o.type=='MESH']
    for o in objs:
        bm=bmesh.new();bm.from_mesh(o.data); bm.verts.ensure_lookup_table()
        visited=set(); comps=[]
        for vert in bm.verts:
            if vert.index in visited:continue
            stack=[vert];visited.add(vert.index);n=0
            while stack:
                v=stack.pop();n+=1
                for edge in v.link_edges:
                    u=edge.other_vert(v)
                    if u.index not in visited:visited.add(u.index);stack.append(u)
            comps.append(n)
        bad=sum(not e.is_manifold for e in bm.edges)
        signed=bm.calc_volume(signed=True)
        print('AUDIT',fname,'mesh',o.name,'dims',list(round(x,4) for x in o.dimensions),'vertices',len(bm.verts),'faces',len(bm.faces),'components',len(comps),'component_sizes',comps,'nonmanifold_edges',bad,'volume_mm3',round(signed,3),flush=True)
        bm.free()
