import bpy
import bmesh
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

def main(context):
	area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
	space = next(space for space in area.spaces if space.type == 'VIEW_3D')
	space.viewport_shade = 'MATERIAL'

class b_previewmod(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.b_previewmod"
	bl_label = "set previewmod"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(b_previewmod)

def unregister():
	bpy.utils.unregister_class(b_previewmod)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.b_previewmod()