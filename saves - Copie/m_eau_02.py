import bpy

def main(context):
	ob = bpy.context.active_object
	mat = bpy.data.materials.get("m_eau_02")
	if mat is None:
	    mat = bpy.data.materials.new(name="m_eau_02")
	if ob.data.materials:
	    ob.data.materials[0] = mat
	else:
	    ob.data.materials.append(mat)

class m_eau_02(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.m_eau_02"
	bl_label = "m_eau_02"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(m_eau_02)

def unregister():
	bpy.utils.unregister_class(m_eau_02)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.m_eau_02()