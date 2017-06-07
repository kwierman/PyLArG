<volume name="volWorld" >
  <materialref ref="Air"/>
  <solidref ref="World"/>

  <physvol>
    <volumeref ref="volTPC"/>
    <position name="posDetEnclosure" unit="cm" x="${0.5*attributes['TPCActiveDepth']}" y="0" z="${0.5*attributes['TPCWirePlaneLength']}"/>
  </physvol>
</volume>
