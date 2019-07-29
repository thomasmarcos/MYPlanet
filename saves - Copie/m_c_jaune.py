import bpy

def main(context):
	ob = bpy.context.active_object
	mat = bpy.data.materials.get("m_c_jaune")
	if mat is None:
	    mat = bpy.data.materials.new(name="m_c_jaune")
	if ob.data.materials:
	    ob.data.materials[0] = mat
	else:
	    ob.data.materials.append(mat)

class m_c_jaune(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.m_c_jaune"
	bl_label = "m_c_jaune"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(m_c_jaune)

def unregister():
	bpy.utils.unregister_class(m_c_jaune)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.m_c_jaune()