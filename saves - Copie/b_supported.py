import bpy

def main(context):
	bpy.context.scene.cycles.feature_set = 'SUPPORTED'



class b_supported(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.b_supported"
	bl_label = "b_supported"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(b_supported)

def unregister():
	bpy.utils.unregister_class(b_supported)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.b_supported()