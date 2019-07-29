import bpy
from rmaxvar import x, y, z


def main(context):
	if bpy.data.objects.get("Croute") is None:
	    bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, size=1, view_align=False, location=(0, 0, 0))
	    bpy.context.object.name = 'Croute'
	    bpy.ops.object.mode_set(mode='EDIT')
	    bpy.ops.transform.resize(value=(x, y, z), proportional_size=1)
	    bpy.ops.mesh.flip_normals()
	    bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, size=1, view_align=False, location=(0, 0, 0))
	    bpy.ops.transform.resize(value=(x+0.02, y+0.02, z+0.02), proportional_size=1)
	    bpy.ops.object.mode_set(mode='OBJECT')
	    bpy.context.object.data.use_auto_smooth = True
	    bpy.context.scene.objects.active = bpy.data.objects['Croute']
	    bpy.ops.object.modifier_add(type='BOOLEAN')
	    bpy.context.object.modifiers['Boolean'].object = bpy.data.objects['Boolean']
	    bpy.context.object.modifiers['Boolean'].operation = 'DIFFERENCE'
	    bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Boolean')
	    bpy.ops.object.shade_smooth()
	    bpy.context.scene.objects.active = bpy.data.objects['Croute']
	    bpy.data.objects['Croute'].select = True
	    ob = bpy.context.active_object
	    mat = bpy.data.materials.get("s_uranus")
	    if mat is None:
	        mat = bpy.data.materials.append(name="s_uranus")
	    if ob.data.materials:
	        ob.data.materials[0] = mat
	    else:
	        ob.data.materials.append(mat)
	    bpy.ops.object.select_all(action='DESELECT')
	    bpy.context.scene.objects.active = bpy.data.objects['Noyau']
	    bpy.data.objects['Noyau'].select = True

	else:
	    bpy.ops.object.select_all(action='DESELECT')
	    bpy.data.objects['Croute'].select = True
	    bpy.ops.object.delete()
	    
	    bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, size=1, view_align=False, location=(0, 0, 0))
	    bpy.context.object.name = 'Croute'
	    bpy.ops.object.mode_set(mode='EDIT')
	    bpy.ops.transform.resize(value=(x, y, z), proportional_size=1)
	    bpy.ops.mesh.flip_normals()
	    bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, size=1, view_align=False, location=(0, 0, 0))
	    bpy.ops.transform.resize(value=(x+0.02, y+0.02, z+0.02), proportional_size=1)
	    bpy.ops.object.mode_set(mode='OBJECT')
	    bpy.context.object.data.use_auto_smooth = True
	    bpy.context.scene.objects.active = bpy.data.objects['Croute']
	    bpy.ops.object.modifier_add(type='BOOLEAN')
	    bpy.context.object.modifiers['Boolean'].object = bpy.data.objects['Boolean']
	    bpy.context.object.modifiers['Boolean'].operation = 'DIFFERENCE'
	    bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Boolean')
	    bpy.ops.object.shade_smooth()
	    bpy.context.scene.objects.active = bpy.data.objects['Croute']
	    bpy.data.objects['Croute'].select = True
	    ob = bpy.context.active_object
	    mat = bpy.data.materials.get("s_uranus")
	    if mat is None:
	        mat = bpy.data.materials.append(name="s_uranus")
	    if ob.data.materials:
	        ob.data.materials[0] = mat
	    else:
	        ob.data.materials.append(mat)
	    bpy.ops.object.select_all(action='DESELECT')
	    bpy.context.scene.objects.active = bpy.data.objects['Noyau']
	    bpy.data.objects['Noyau'].select = True


class croute_uranus(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.croute_uranus"
	bl_label = "s_uranus"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(croute_uranus)

def unregister():
	bpy.utils.unregister_class(croute_uranus)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.croute_uranus()