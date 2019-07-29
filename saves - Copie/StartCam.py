import bpy
import bmesh
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

def main(context):
	for area in bpy.context.screen.areas:
	    if area.type == 'VIEW_3D':
	        override = bpy.context.copy()
	        override['area'] = area
	        bpy.ops.view3d.viewnumpad(override, type = 'CAMERA')
	        break

class startcam(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.startcam"
	bl_label = "Start CAMERA"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(startcam)

def unregister():
	bpy.utils.unregister_class(startcam)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.startcam()