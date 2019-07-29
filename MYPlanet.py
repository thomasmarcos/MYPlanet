#!/usr/bin/python3
# -*- coding: utf-8 -*




#Creation du Noyau

def d_CreerNoyau(xmin, ymin, zmin):
	Segments = 64
	Rings = 32
	unite0 = 1

	Rmin = str(xmin) + ", " + str(ymin) +", "+ str(zmin)

	CommandesBlender = """bpy.ops.mesh.primitive_uv_sphere_add(segments="""+str(Segments)+""", ring_count="""+str(Rings)+""", size="""+str(unite0)+""", view_align=False, location=(0, 0, 0))
bpy.context.object.name = 'Noyau'
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.transform.resize(value=("""+str(Rmin)+"""), proportional_size="""+str(unite0)+""")
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.shade_smooth()\n"""

	fichier = open("cache/executable.py", "w")
	fichier.write("import bpy\nimport bmesh\nfrom mathutils import Vector\nfrom bpy_extras.object_utils import world_to_camera_view\n")
	fichier.write(CommandesBlender)

	return (xmin, ymin, zmin)




#Creation des couches autour du Noyau

def d_CreerCouche(xmin, ymin, zmin, xfac, yfac, zfac, allfac):
	Segments = 64
	Rings = 32
	unite = 1

	axes = input("\n\nLa couche " + str(i+1)+" a-t-elle une epaisseur constante (y/n) ?\n\t")

	if axes == "y" :
		xep = yep = zep = float(input("\n\tL'epaisseur de la couche " + str(i+1)+" est de : "))
		xep = xep / allfac
		yep = yep / allfac
		zep = zep / allfac

	else :
		xep = float(input("\n\tL'epaisseur de la couche " + str(i+1)+" en X est de : "))
		yep = float(input("\n\tL'epaisseur de la couche " + str(i+1)+" en Y est de : "))
		zep = float(input("\n\tL'epaisseur de la couche " + str(i+1)+" en Z est de : "))
		xep = xep / allfac
		yep = yep / allfac
		zep = zep / allfac

	Rmin = str(xmin) + ", " + str(ymin) +", "+ str(zmin)
	Rmax = str(xmin + xep) + ", " + str(ymin + yep) + ", " + str(zmin + zep)
		

	CommandesBlender = """bpy.ops.mesh.primitive_uv_sphere_add(segments="""+str(Segments)+""", ring_count="""+str(Rings)+""", size="""+str(unite)+""", view_align=False, location=(0, 0, 0))
bpy.context.object.name = 'Couche_"""+str(i)+"""'
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.transform.resize(value=("""+str(Rmin)+"""), proportional_size="""+str(unite)+""")
bpy.ops.mesh.flip_normals()
bpy.ops.mesh.primitive_uv_sphere_add(segments="""+str(Segments)+""", ring_count="""+str(Rings)+""", size="""+str(unite)+""", view_align=False, location=(0, 0, 0))
bpy.ops.transform.resize(value=("""+str(Rmax)+"""), proportional_size="""+str(unite)+""")
bpy.ops.object.mode_set(mode='OBJECT')
bpy.context.object.data.use_auto_smooth = True\n"""

	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)

	xmin = xmin + xep
	ymin = ymin + yep
	zmin = zmin + zep

	return (xmin, ymin, zmin)




#Decoupe de la planete en deux morceaux

def d_Decoupe_1(xmin, ymin, zmin):
	
	a = 0.01
	f1 = 1 + a
	f2 = 1 + a / 2

	BSS = str(xmin + f1) + ", " + str(ymin + f1) +", "+ str(zmin + f1)

	CommandesBlender = """bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=("""+str(xmin + f2)+""", 0, 0))
bpy.context.object.name = 'Boolean'
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.transform.resize(value=("""+str(BSS)+"""), proportional_size=1)
bpy.ops.object.mode_set(mode='OBJECT')
bpy.context.object.hide = True
bpy.context.object.hide_select = True
bpy.context.object.hide_render = True\n"""

	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)




#Decoupe de la planete en quatre morceaux

def d_Decoupe_2(xmin, ymin, zmin):
	
	a = 0.01
	f1 = 1 + a
	f2 = 1 + a / 2

	BSS = str(xmin + f1) + ", " + str(ymin + f1) +", "+ str(zmin + f1)

	CommandesBlender = """bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=("""+str(xmin + f2)+""", """+str(-ymin - f2)+""", 0))
bpy.context.object.name = 'Boolean'
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.transform.resize(value=("""+str(BSS)+"""), proportional_size=1)
bpy.ops.object.mode_set(mode='OBJECT')
bpy.context.object.hide = True
bpy.context.object.hide_select = True
bpy.context.object.hide_render = True\n"""

	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)




#Decoupe de la planete en huit morceaux

def d_Decoupe_3(xmin, ymin, zmin):
	
	a = 0.01
	f1 = 1 + a
	f2 = 1 + a / 2

	BSS = str(xmin + f1) + ", " + str(ymin + f1) +", "+ str(zmin + f1)

	CommandesBlender = """bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0))
bpy.context.object.name = 'Boolean'
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.transform.resize(value=("""+str(BSS)+"""), proportional_size=1)
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.transform.translate(value=("""+str(xmin + f2)+""", """+str(-ymin - f2)+""", """+str(zmin + f2)+"""), constraint_orientation='GLOBAL')
bpy.context.object.hide = True
bpy.context.object.hide_select = True
bpy.context.object.hide_render = True\n"""
	
	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)




#Appliquer le Booleen

def d_AppliquerDecoupe(i):
	CommandesBlender = """bpy.context.scene.objects.active = bpy.data.objects['Couche_"""+str(i)+"""']
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers['Boolean'].operation = 'DIFFERENCE'
bpy.context.object.modifiers['Boolean'].object = bpy.data.objects['Boolean']
bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Boolean')\n"""
	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)
	return i




#Appliquer le Booleen au noyau

def d_AppliquerDecoupeNoyau():
	CommandesBlender = """bpy.context.scene.objects.active = bpy.data.objects['Noyau']
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers['Boolean'].object = bpy.data.objects['Boolean']
bpy.context.object.modifiers['Boolean'].operation = 'DIFFERENCE'
bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Boolean')\n"""
	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)




#Creer une camera pour le nettoyage du mesh

def d_CreerCleanCam():
	CommandesBlender = """bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 500), rotation=(0, 0, 0))
bpy.context.object.name = "CCM"
bpy.context.object.data.type = 'ORTHO'
bpy.context.object.data.ortho_scale = 0.19
bpy.context.object.data.clip_end = 1000\n"""
	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)




#Nettoyer le mesh des chouches

def d_NettoyerCouches(i, FACTOR):
	CommandesBlender = """
def debug(scene):
    for window in bpy.context.window_manager.windows:
            for area in window.screen.areas: 
                if area.type == 'VIEW_3D':
                    override = bpy.context.copy()
                    override['area'] = area
                    bpy.ops.view3d.viewnumpad(override, type = 'CAMERA')
                    break
bpy.app.handlers.render_pre.append(debug)


bpy.context.scene.objects.active = bpy.data.objects['Couche_"""+str(i)+"""']
bpy.ops.object.mode_set(mode='EDIT')

scene = bpy.context.scene
cam = bpy.data.objects['CCM']
obj = bpy.data.objects['Couche_"""+str(i)+"""']
mesh = obj.data
mat_world = obj.matrix_world
cs, ce = cam.data.clip_start, cam.data.clip_end

assert obj.mode == "EDIT"
bm = bmesh.from_edit_mesh(mesh)

for v in bm.verts:
    co_ndc = world_to_camera_view(scene, cam, mat_world * v.co)
    #check wether point is inside frustum
    if (0.0 < co_ndc.x < 1.0 and
        0.0 < co_ndc.y < 1.0 and
         cs < co_ndc.z <  ce):
        v.select = True
    else:
        v.select = False

bmesh.update_edit_mesh(mesh, False, False)

bpy.ops.transform.resize(value=(0, 0, 1))

bpy.ops.mesh.remove_doubles(threshold=0.01)

bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
bpy.ops.mesh.tris_convert_to_quads(face_threshold=0.698132, shape_threshold=0.698132, uvs=False, vcols=False, seam=False, sharp=False, materials=False)

bpy.ops.mesh.remove_doubles(threshold=0.02)

bpy.ops.object.mode_set(mode='OBJECT')

bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.cycles.use_adaptive_subdivision = True
bpy.context.object.modifiers['Subsurf'].levels = 0
bpy.context.object.cycles.dicing_rate = 0.75
bpy.context.scene.objects.active = bpy.data.objects['Couche_"""+str(i)+"""']
bpy.data.objects['Couche_"""+str(i)+"""'].select = True
bpy.ops.object.shade_smooth()
for ob in bpy.context.selected_objects:ob.select = False\n"""
	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)




#Nettoyer le mesh du noyau s'il a ete decoupe

def d_NettoyerNoyau(FACTOR):

	f = 0.0499

	CommandesBlender = """bpy.context.scene.objects.active = bpy.data.objects['Noyau']
bpy.ops.object.mode_set(mode='EDIT')
context = bpy.context
FACTOR = """+str(FACTOR)+"""
ob = context.edit_object
me = ob.data
bm = bmesh.from_edit_mesh(me)
avg_face_area = sum(f.calc_area() for f in bm.faces) / len(bm.faces)
print('avge face area: ', avg_face_area)
for f in bm.faces:f.select = f.calc_area() > FACTOR * avg_face_area
bmesh.update_edit_mesh(me)
bpy.ops.mesh.remove_doubles(threshold="""+str(f)+""")
bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
bpy.ops.mesh.tris_convert_to_quads(face_threshold=0.698132, shape_threshold=0.698132, uvs=False, vcols=False, seam=False, sharp=False, materials=False)
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.cycles.use_adaptive_subdivision = True
bpy.context.object.modifiers['Subsurf'].levels = 0
bpy.context.object.cycles.dicing_rate = 0.75
bpy.context.scene.objects.active = bpy.data.objects['Noyau']
bpy.data.objects['Noyau'].select = True
bpy.ops.object.shade_smooth()
bpy.context.object.data.use_auto_smooth = True
for ob in bpy.context.selected_objects:ob.select = False\n"""
	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)




#Pour ecrire le script qui mettra des textures de base sur le noyau de la planete

def d_CouleurNoyau():
	CommandesBlender = """import bpy
bpy.context.scene.objects.active = bpy.data.objects['Noyau']
bpy.data.objects['Noyau'].select = True
ob = bpy.context.active_object
mat = bpy.data.materials.get("gris")
if mat is None:
    mat = bpy.data.materials.append(name="gris")
if ob.data.materials:
    ob.data.materials[0] = mat
else:
    ob.data.materials.append(mat)\n"""
	fichier = open("cache/mat.py", "w")
	fichier.write(CommandesBlender)




#Attribue une couleur aux couches impaires

def d_CouleurCouchesImpaires(i):
	CommandesBlender = """import bpy
bpy.context.scene.objects.active = bpy.data.objects['Couche_"""+str(i)+"""']
bpy.data.objects['Noyau'].select = True
ob = bpy.context.active_object
mat = bpy.data.materials.get("gris")
if mat is None:
    mat = bpy.data.materials.append(name="gris")
if ob.data.materials:
    ob.data.materials[0] = mat
else:
    ob.data.materials.append(mat)\n"""
	fichier = open("cache/mat.py", "a")
	fichier.write(CommandesBlender)




#Attribue une couleur aux couches paires

def d_CouleurCouchesPaires(i):
	CommandesBlender = """import bpy
bpy.context.scene.objects.active = bpy.data.objects['Couche_"""+str(i)+"""']
bpy.data.objects['Noyau'].select = True
ob = bpy.context.active_object
mat = bpy.data.materials.get("blanc")
if mat is None:
    mat = bpy.data.materials.new(name="blanc")
if ob.data.materials:
    ob.data.materials[0] = mat
else:
    ob.data.materials.append(mat)\n"""
	fichier = open("cache/mat.py", "a")
	fichier.write(CommandesBlender)



#Enregistrer les Rmax dans un script


def RecRmax(xmin, ymin, zmin):
	Rvariables = """x = """+str(xmin)+"""\ny = """+str(ymin)+"""\nz = """+str(zmin)+"""\nx1 = """+str(xmin*3)+"""\ny1 = """+str(ymin*3)+"""\nz1 = """+str(zmin*3)+"""\n"""
	fichier = open("cache/rmaxvar.py", "w")
	fichier.write(Rvariables)


def SafeScene():
	CommandesBlender = "bpy.ops.wm.save_as_mainfile(filepath='.//saves/current.blend')"
	fichier = open("cache/executable.py", "a")
	fichier.write(CommandesBlender)


#----------------------------------------------------------------------------Fin des defs, debut du script-----------------------------------------------------------------------------------------------------



#Debut du script

import os



#Indications quant au script

print("\nBienvenue sur MYPlanet.\n\nPour une utilisation agreable et optimale de ce programme, il est conseille de :\n\n\t- Lire la notice : "+str(os.getcwd())+"/notice.html\n\t- Respecter la morphologie/phonologie pour repondre aux questions.\n\t- Noter que l'axe Z represente l'axe de figure.\n\n\n\n")



#Pour lister les modeles deja existants

from glob import glob
from os import path

path_to_saves = "saves/*/*.bat"
list_in_saves = [path.basename(x) for x in glob(path_to_saves)]



#Option permettant d'ouvrir un modele deja existant

if not list_in_saves:
	xList=0
else:
	xList=1

if xList == 1 :
	Choix = input("Souhaitez-vous ouvrir un modele deja existant (y/n) ?\n\t")
	if Choix == "y" :
		list_without_extension = [s.replace('.bat', '') for s in list_in_saves]
		final_list = "\n".join(list_without_extension) 
		print("\n\n\n\nVoici la liste des modeles deja existants :\n\n"+str(final_list)+"\n\n\n\n")
		open_file = input("Quel modele souhaitez-vous ouvrir ?\n\t")
		os.system('%cd%/saves/'+str(open_file)+'/'+str(open_file)+'.bat')

		exit()



#Demander le nombre de couches, la couche 1 (noyau) inclut

combien_de_couches = input("\n\n\n\nDebut de la creation :\n\nCombien voulez-vous de couches ?\n\t")
Ncouches = int(combien_de_couches)



#Demander si la couche 1 (noyau) est spherique

MultiAxis = input("\n\nLa couche 1 (noyau) est-elle spherique (y/n) ?\n\t")


xfac =""
yfac =""
zfac =""
allfac =""



#Dimension de la couche 1 (noyau), le resultat est toujours ramene a 1

if MultiAxis == "y" :
	allfac = xmin = ymin = zmin = float(input("\n\tLe rayon de la couche 1 est de : "))
	xmin = xmin / allfac
	ymin = ymin / allfac
	zmin = zmin / allfac

else :	
	xfac = xmin = float(input("\n\tLe demi-axe de la couche 1 en X est de : "))
	yfac = ymin = float(input("\n\tLe demi-axe de la couche 1 en Y est de : "))
	zfac = zmin = float(input("\n\tLe demi-axe de la couche 1 en Z est de : "))

	if xmin > ymin and xmin > zmin or xmin > ymin and xmin == zmin or xmin == ymin and xmin > zmin or xmin == ymin and xmin == zmin :
		allfac=xmin

	if ymin > xmin and ymin > zmin or ymin > xmin and ymin == zmin or ymin == xmin and ymin > zmin or ymin == xmin and ymin == zmin :
		allfac=ymin

	if zmin > xmin and zmin > ymin or zmin > xmin and zmin == ymin or zmin == xmin and zmin > ymin or zmin == xmin and zmin == ymin :
		allfac=zmin

	xmin = xmin / allfac
	ymin = ymin / allfac
	zmin = zmin / allfac

xmin, ymin, zmin = d_CreerNoyau(xmin, ymin, zmin)



#Epaisseur des differentes couches

for i in range(1, int(Ncouches)):
	xmin, ymin, zmin = d_CreerCouche(xmin, ymin, zmin, xfac, yfac, zfac, allfac)



#Choix de l'ouverture de la planete

ChoixBoolean = int(input("\n\nVous desirez une ouverture sur l'interieur correspondant a :\n\n\t1/2 de la planete (1)\n\t1/4 de la planete (2)\n\t1/6 de la planete (3)\n\t\t"))



#Creer les booleens

if ChoixBoolean == 1 :
	d_Decoupe_1(xmin, ymin, zmin)
elif ChoixBoolean == 2 :
	d_Decoupe_2(xmin, ymin, zmin)
else :
	d_Decoupe_3(xmin, ymin, zmin)



#Appliquer les booleens

for i in range(1, int(Ncouches)):
	d_AppliquerDecoupe(i)



#Demander s'il faut appliquer l'ouverture a la couche 1 (noyau)

BooleanNoyau = input("\nAppliquer la meme ouverture a la premiere couche (noyau) (y/n) ?\n\t")



#Preparation du nettoyage des meshes

FACTOR = 1

d_CreerCleanCam()



#Appliquer l'ouvrture au noyau en fonction de la reponse donnee plus tôt

if BooleanNoyau == "y" :
	d_AppliquerDecoupeNoyau()
	d_NettoyerNoyau(FACTOR)



#Nettoyage des meshes

for i in range(1, int(Ncouches)):
	d_NettoyerCouches(i, FACTOR)



#Attribuer une couleur de base aux couches de la planete

d_CouleurNoyau()

if Ncouches > 1 :
	for i in range(2,int(Ncouches), 2):
		d_CouleurCouchesImpaires(i)
	for i in range(1,int(Ncouches), 2):
		d_CouleurCouchesPaires(i)
else :
	d_CouleurCouchesPaires(1)



#Enregistrer les dimensions de la planete

RecRmax(xmin, ymin, zmin)



#Ouvrir le modele dans une nouvelle scene pour preserver la scene de base (template)

SafeScene()



#Lancer Blender

import exe
exe()

