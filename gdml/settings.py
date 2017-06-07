from math import pi, sqrt, sin,cos, tan, radians, asin

context = {
  'wires_on':True,
  'TPCDepth':250.,
  'TPCWidth':250.,
  'TPCLength':250.,
  'TPCWirePitch':0.25,
  'TPCWirePlaneSpacing':0.25,
  'TPCWirePlaneThickness':0.1,
  'TPCWireThickness':0.01,
  'UVAngle':60.0,
  'NumberOfTPCPlanes':3,
  'UPlaneYOffset':0.,
  'UPlaneZOffset':0.,
  'VPlaneYOffset':0.,
  'VPlaneZOffset':0.,
  'YPlaneZOffset':0.
}

context['SinUVAngle'] = sin( radians(context['UVAngle']) );
context['CosUVAngle'] = cos( radians(context['UVAngle']) );
context['TanUVAngle'] = tan( radians(context['UVAngle']) );

#manual context setting
context['TPCWirePlaneWidth']	=	250.
context['TPCWirePlaneLength']	=	250.


context['pi ']  = pi
context['inch'] = 2.54

context['WorldWidth']		=	10000.0
context['WorldHeight']	=	10000.0
context['WorldLength']	=	10000.0

context['CathodePlateDepth']	=	0.1
context['CathodeWidth']	=	5.1
context['CathodeHeight']	=	240.0
context['CathodeLength']	=	1042.0

context['GroundPlateWidth']	=	224.0
context['GroundPlateHeight']	=	0.1
context['GroundPlateLength']	=	1100.0

context['tpc_neg_length']	=	1000.0
context['tpc_neg_width']	=	200.0
context['tpc_neg_height']	=	200.0
context['wire_frame_width']	=	9.5
context['wire_plane_height'] =	240.0
context['wire_plane_length'] =	1042.0
context['wires_plength'] = (context['wire_plane_length'] - 2 *
                            context['wire_frame_width'])
context['wires_pwidth'] = (context['wire_plane_height'] - 2 *
                           context['wire_frame_width'])

context['field_cage_width'] = 256
context['field_cage_height'] = 207.6
context['field_cage_cross_length'] = (sqrt((context['field_cage_width']) ** 2 +
                                       (context['field_cage_height'] -
                                        50) ** 2))
context['field_cage_length'] = 1011.6
context['field_cage_loop_interval']	=	1 	# =1 is normal, =4 skips 3/4

context['FieldCageTPCClearance']	=	5*context['inch']
context['FieldCageTubeRadius']	=	0.5*context['inch']
context['FieldCageTubeThickness']	=	0.25*context['inch']
context['FieldCageBeamDepth']		=	12.5
context['FieldCageBeamWidth']		=	2.5
context['FieldCageCrossDepth']	=	2.5
context['FieldCageCrossWidth']	=	4
context['FieldCageCrossLength']	=	context['field_cage_cross_length']

context['TPCTotalLength']	=	context['field_cage_length']
context['TPCTotalWidth']	=	context['field_cage_width']
context['TPCTotalHeight']	=	context['field_cage_height']

context['FieldCageLoopLength'] = (context['TPCTotalLength'] + 2 *
                                  (context['FieldCageTPCClearance'] +
                                   2*context['FieldCageTubeRadius']))
context['FieldCageLoopWidth'] = context['field_cage_width']
context['FieldCageLoopHeight'] = (context['TPCTotalHeight'] + 2 *
                                  (context['FieldCageTPCClearance'] +
                                   2 * context['FieldCageTubeRadius']))

context['FieldCageCornerRadius']	=	0.5*context['FieldCageTPCClearance'];
context['FieldCageCornerY'] = (0.5 * context['FieldCageLoopHeight'] -
                               context['FieldCageCornerRadius'] -
                               context['FieldCageTubeRadius'])
context['FieldCageCornerZ'] = (0.5 * context['FieldCageLoopLength'] -
                               context['FieldCageCornerRadius'] -
                               context['FieldCageTubeRadius'])

context['FieldCageHeight'] = (context['FieldCageLoopHeight'] + 2 *
                              (context['FieldCageBeamDepth'] +
                              context['FieldCageCrossDepth']))
context['FieldCageLength'] = (context['FieldCageLoopLength'] + 2 *
                              (context['FieldCageBeamDepth'] +
                              context['FieldCageCrossDepth']))
context['FieldCageWidth'] = context['field_cage_width']

context['UVWireCount'] = 1200
context['TPCYWirePitch'] = (context['TPCWirePitch'] /
                            context['SinUVAngle'])
context['TPCZWirePitch'] = (context['TPCWirePitch'] /
                            context['CosUVAngle'])

context['NumberWiresPerEdge'] = int(context['TPCWirePlaneWidth'] /
                                    context['TPCYWirePitch'])
context['NumberCenterWires'] = int(context['UVWireCount'] - 2. *
                                   context['NumberWiresPerEdge'])

if not context['wires_on']:
    context['NumberWiresPerEdge'] = 0
    context['NumberCenterWires'] = 0

context['aTPC_xos_cathode'] = (0.5 * context['CathodeWidth'] +
                               0.5 * context['CathodePlateDepth'])
context['aTPC_xos_wires'] = (3. * context['TPCWirePlaneSpacing'] +
                             context['TPCWirePlaneThickness'])
context['aTPC_xoffset'] = (context['aTPC_xos_cathode'] -
                           context['aTPC_xos_wires'])
context['TPCActiveDepth'] = (context['TPCDepth'] -
                             context['aTPC_xos_cathode'] -
                             context['aTPC_xos_wires'])
context['TPCActiveHeight'] = context['TPCWirePlaneWidth']
context['TPCActiveLength'] = context['TPCWirePlaneLength'] - 0.2


