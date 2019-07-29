import bpy
import bmesh
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

def main(context):
	import os, sys
	import shutil

    
    
    
	def createFolder(directory):
	    try:
	        if not os.path.exists(directory):
	            os.makedirs(directory)
	    except OSError:
	        print ('Error: Creating directory. ' +  directory)
	        
	createFolder('.//saves/' + str(bpy.data.scenes["Scene"].string_save))
	createFolder('.//saves/' + str(bpy.data.scenes["Scene"].string_save) + "/cache")

	fichier = open(".//saves/" + str(bpy.data.scenes["Scene"].string_save) + "/" + str(bpy.data.scenes["Scene"].string_save) + ".bat", "w")
	fichier.write('#!/bin/bash\nBlender/blender -ba saves/'+ str(bpy.data.scenes["Scene"].string_save)+'/'+str(bpy.data.scenes["Scene"].string_save)+'.blend -y -P saves/'+str(bpy.data.scenes["Scene"].string_save)+'/cache/executable.py -P saves/'+str(bpy.data.scenes["Scene"].string_save)+'/cache/mat.py '
		
		#Commandes pour boutons de l'interface

		'-P ressource/StartCam.py '
		'-P ressource/b_previewmod.py '
		'-P ressource/b_rendermod.py '
		'-P ressource/b_update.py '
		'-P ressource/b_save_cache.py '
		'-P ressource/b_experimental.py '
		'-P ressource/b_supported.py '

		#Commandes pour les Surfaces

		'-P ressource/croute_nothing.py '
		'-P ressource/croute_mercuryreal.py '
		'-P ressource/croute_venus.py '
		'-P ressource/croute_earth.py '
		'-P ressource/croute_mars.py '
		'-P ressource/croute_jupiter.py '
		'-P ressource/croute_saturn.py '
		'-P ressource/croute_uranus.py '
		'-P ressource/croute_neptune.py '
		'-P ressource/croute_moon.py '
		'-P ressource/croute_sun.py '
		'-P ressource/croute_mercurycolor.py '

		#Commandes pour les Materiaux

		'-P ressource/mat_magma_01.py '
		'-P ressource/mat_magma_02.py '

		'-P ressource/m_rockgranite001.py '
		'-P ressource/m_barkburned001.py '
		'-P ressource/m_groundmuddy001.py '
		'-P ressource/m_groundmuddy002.py '
		'-P ressource/m_groundsnowfootprints002.py '

		'-P ressource/m_lavacrackedmedium001.py '
		'-P ressource/m_lavamolten001.py '
		'-P ressource/m_lavamoltenhot.py '
		'-P ressource/m_lavamoltenfolds001.py '
		'-P ressource/m_metalcastiron002.py '

		'-P ressource/m_metalcorrodedheavy001.py '
		'-P ressource/m_metaldesignersteelpatternedbrushstrokes001.py '
		'-P ressource/m_roaddirt003.py '
		'-P ressource/m_rockdark003.py '

		'-P ressource/m_rockmossylight001.py '
		'-P ressource/m_rocksandstone001.py '
		'-P ressource/m_rocksandstonegrey.py '
		'-P ressource/m_rustplain030.py '
		'-P ressource/m_snowfine001.py '

		'-P ressource/m_eau_01.py '
		'-P ressource/m_eau_02.py '
		'-P ressource/m_gaz.py '

		'-P ressource/m_ice_01.py '
		'-P ressource/m_ice_02.py '
		'-P ressource/m_ice_03.py '
		'-P ressource/m_ice_04.py '
		'-P ressource/m_groundmuddy003.py '

		'-P ressource/m_c_blanc.py '
		'-P ressource/m_c_bleu.py '
		'-P ressource/m_c_cian.py '
		'-P ressource/m_c_gris.py '
		'-P ressource/m_c_jaune.py '
		'-P ressource/m_c_noir.py '
		'-P ressource/m_c_orange.py '
		'-P ressource/m_c_rose.py '
		'-P ressource/m_c_rouge.py '
		'-P ressource/m_c_vert.py '
		'-P ressource/m_c_violet.py '

		'-P ressource/m_toon.py '

		#Pour lancer l'interface

		'--python-text Interface '
		'--python-text MaterialShading &')

	filename1 = './/cache/rmaxvar.py'  
	fileA = open(filename1, 'rb')

	filename2 = './/saves/' + str(bpy.data.scenes["Scene"].string_save) + '/cache/rmaxvar.py'  
	fileB = open(filename2, 'wb')

	shutil.copyfileobj(fileA, fileB)

	filename1 = './/ressource/executable.py'  
	fileA = open(filename1, 'rb')

	filename2 = './/saves/' + str(bpy.data.scenes["Scene"].string_save) + '/cache/executable.py'  
	fileB = open(filename2, 'wb')

	shutil.copyfileobj(fileA, fileB)


class b_save_cache(bpy.types.Operator):
	"""Tooltip"""
	bl_idname = "myops.b_save_cache"
	bl_label = "set previewmod"

	@classmethod
	def poll(cls, context):
		return context.active_object is not None

	def execute(self, context):
		main(context)
		return{'FINISHED'}

def register():
	bpy.utils.register_class(b_save_cache)

def unregister():
	bpy.utils.unregister_class(b_save_cache)

if __name__ == "__main__":
	register()

	# test call
	# bpy.ops.myops.b_save_cache()