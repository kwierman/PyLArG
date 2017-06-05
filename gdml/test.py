import xml.etree.ElementTree as ET
import sys
import pprint

tree = ET.parse("microboonevX.gdml")
root = tree.getroot()
structure = root.find("structure")
phys_vols = structure.findall("volume[@name='volDetEnclosure'].physvol")
example = phys_vols[-1]
#print example
#print example.find("volumeref")
#print example.find("volumeref").attrib['ref']
#sys.exit(0)
solids = root.find("solids")


def find_module_strip(module, strip):
    global phys_vols
    volref, auxdet = None, None
    for i in phys_vols:
        volref_tmp = i.find("volumeref[@ref='volModule_{}_strip_{}']".format(module, strip))
        auxdet_tmp = i.find("volumeref[@ref='volAuxDet_Module_{}_strip_{}']".format(module, strip))
        if volref_tmp is not None:
            return i


top={}
for module in range(73):
    mod={}
    for strip in range(16):
        st={}
        mod_el =  find_module_strip(module, strip)
        position = mod_el.find('position')
        coords=['x','y','z']
        for co in coords:
            st[co] = position.attrib[co]
        mod[strip] = st
    top[module] = mod

pprint.pprint(top)
