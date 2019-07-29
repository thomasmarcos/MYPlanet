import bpy

def main(context):
	ob = bpy.context.active_object
	mat = bpy.data.materials.get("m_ice_03")
	if mat is None:
	    mat = bpy.data.materials.new(name="m_ice_03")
	if ob.data.materials:
	    ob.data.materials[0] = mat
	else:
	    ob.data.materials.append(mat)

class m_ice_03(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.m_ice_03"
	bl_label = "m_ice_03"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(m_ice_03)

def unregister():
	bpy.utils.unregister_class(m_ice_03)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.m_ice_03()