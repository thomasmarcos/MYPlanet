import bpy
import bmesh
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, size=0, view_align=False, location=(0, 0, 0))
