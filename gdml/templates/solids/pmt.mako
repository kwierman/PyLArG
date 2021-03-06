%if attributes['pmt_on']:
  <tube name="PMTVolume"
   rmax="${(6.1*2.54)}"
   z="${(11.1*2.54)+0.005}"
   deltaphi="360"
   aunit="deg"
   lunit="cm"/>
  <tube name="PMT_AcrylicPlate"
   rmax="${(6.0*2.54)}"
   z="${(0.2)}"
   deltaphi="360"
   aunit="deg"
   lunit="cm"/>
  <tube name="PMT_Stalk"
   rmax="${(1.25*2.54)}"
   z="${(3.0*2.54)}"
   deltaphi="360"
   aunit="deg"
   lunit="cm"/>
  <tube name="PMT_SteelBase"
   rmax="${(6.0*2.54)}"
   z="${(1.5*2.54)}"
   deltaphi="360"
   aunit="deg"
   lunit="cm"/>
  <tube name="PMT_Underside"
   rmax="${2.54*4.0}"
   z="${2.54*2.5}"
   deltaphi="360"
   aunit="deg"
   lunit="cm"/>
  <box name="Paddle_PMT"
   lunit="cm"
   x="${1./8.*2.54}"
   y="${20.*2.54}"
   z="${(7.+1./3.)*2.54}"/>
  <tube name="PMT_Lens"
   rmax="${2.54*4.0}"
   z="${2.54*2.5}"
   deltaphi="360"
   aunit="deg"
   lunit="cm"/>
%endif
