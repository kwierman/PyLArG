#!/usr/bin/python
from mako.lookup import TemplateLookup
from mako.template import Template
from mako import exceptions
import xml.dom.minidom
import copy, os

from settings import context
"""
    :warning: Due to the pretty printer, the memory overhead of this quite large ( O(10MB) ).
"""



if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    mylookup = TemplateLookup(directories=[os.path.join(dir_path,'templates') ])
    temp = Template('<%include file="microboonevX.mako"/>',
      lookup = mylookup,
      strict_undefined=True)
    try:
        with_wires = temp.render(data="world", attributes=context)
    except:
        print exceptions.html_error_template().render()        

    open("microboonevX.gdml",'w').write(with_wires)
    context_wowires = context
    context_wowires['wires_on'] = False
    try:
        without_wires = temp.render(data="world", attributes=context_wowires)
    except:
        print exceptions.html_error_template().render()
    
    xml = xml.dom.minidom.parseString(without_wires)
    open("microboonevX_nowires.gdml",'w').write(xml.toprettyxml())