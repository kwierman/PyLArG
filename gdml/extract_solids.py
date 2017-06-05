import xml.etree.ElementTree as ET
import sys
import pprint

tree = ET.parse("microboonevX.gdml")
root = tree.getroot()
solids = root.find("solids")

top={}

for module in range(73):
    mod={}
    for strip in range(16):
        position={}
        vol_box = solids.find("box[@name='AuxDet_Module_{}_strip_{}']".format(module, strip))
        if vol_box is None:
            print "COULD NOT FIND VOL BOX:", module, ": ", strip
            continue
        mod_box = solids.find("box[@name='Module_{}_strip_{}']".format(module, strip))
        if mod_box is None:
            print "COULD NOT FIND MOD BOX"
        position['x'] = mod_box.attrib['x']
        position['y'] = mod_box.attrib['y']
        position['z'] = mod_box.attrib['z']
            

        mod[strip]=position
    top[module]=mod
pprint.pprint(top)
