import bpy


def main(context):
	if bpy.data.objects.get("Croute") is not None:
		bpy.ops.object.select_all(action='DESELECT')
		bpy.data.objects['Croute'].select = True
		bpy.ops.object.delete()
		bpy.ops.object.select_all(action='DESELECT')
		bpy.context.scene.objects.active = bpy.data.objects['Noyau']
		bpy.data.objects['Noyau'].select = True
	else:
		print('ERROR')

class croute_nothing(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.croute_nothing"
	bl_label = "S_Nothing"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(croute_nothing)

def unregister():
	bpy.utils.unregister_class(croute_nothing)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.croute_nothing()