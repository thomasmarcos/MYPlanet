import bpy

def main(context):
	ob1 = bpy.context.active_object
	mat1 = bpy.data.materials.get("S_Mars")
	if mat1 is None:
	    mat1 = bpy.data.materials.new(name="S_Mars")
	if ob1.data.materials:
	    ob1.data.materials[0] = mat1
	else:
	    ob1.data.materials.append(mat1)

class s_mars(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.mat_s_mars"
	bl_label = "S_Mars"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(s_mars)

def unregister():
	bpy.utils.unregister_class(s_mars)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.mat_s_mars()