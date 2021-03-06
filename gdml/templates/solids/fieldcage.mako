<tube name="FieldCageTubeZ"
   rmin="${attributes['FieldCageTubeRadius']-attributes['FieldCageTubeThickness']}"
   rmax="${attributes['FieldCageTubeRadius']}"
   z="${attributes['FieldCageLoopLength']-2.*(attributes['FieldCageCornerRadius']+attributes['FieldCageTubeRadius'])}"
   deltaphi="360"
   aunit="deg"
   lunit="cm"/>
<tube name="FieldCageTubeY"
   rmin="${attributes['FieldCageTubeRadius']-attributes['FieldCageTubeThickness']}"
   rmax="${attributes['FieldCageTubeRadius']}"
   z="${attributes['FieldCageLoopHeight']-2.*(attributes['FieldCageCornerRadius']+attributes['FieldCageTubeRadius'])}"
   deltaphi="360"
   aunit="deg"
   lunit="cm"/>
