import bpy

def main(context):
	bpy.context.scene.cycles.feature_set = 'EXPERIMENTAL'


class b_experimental(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.b_experimental"
	bl_label = "b_experimental"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(b_experimental)

def unregister():
	bpy.utils.unregister_class(b_experimental)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.b_experimental()