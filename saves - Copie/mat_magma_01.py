import bpy

def main(context):
	ob = bpy.context.active_object
	mat = bpy.data.materials.get("Magma_01")
	if mat is None:
	    mat = bpy.data.materials.new(name="Magma_01")
	if ob.data.materials:
	    ob.data.materials[0] = mat
	else:
	    ob.data.materials.append(mat)

class magma_01(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.mat_magma_01"
	bl_label = "Magma_01"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(magma_01)

def unregister():
	bpy.utils.unregister_class(magma_01)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.mat_magma_01()