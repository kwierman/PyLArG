  <volume name="volTPCActive">
   <materialref ref="LAr"/>
   <solidref ref="TPCActive"/>
  </volume>


  <volume name="volTPC">
   <materialref ref="LAr"/>
   <solidref ref="TPC"/>

   %if attributes['wires_on']:
     <physvol>
      <volumeref ref="volTPCPlaneVert"/>
      <position name="posTPCPlaneVert" unit="cm"
      x="${-0.5*attributes['TPCActiveDepth']-2*attributes['TPCWirePlaneSpacing']}"
      y="0" z="0"/>
     </physvol>
     <physvol>
      <volumeref ref="volTPCPlane"/>
      <position name="posTPCPlane" unit="cm"
      x="${-0.5*attributes['TPCActiveDepth']-attributes['TPCWirePlaneSpacing']}"
      y="0" z="0"/>
     </physvol>
     <physvol>
      <volumeref ref="volTPCPlane"/>
      <position name="posTPCPlane2" unit="cm"
      x="${-0.5*attributes['TPCActiveDepth']}"
      y="0" z="0"/>
      <rotationref ref="rPlus180AboutY"/>
     </physvol>
   %endif

     <physvol>
      <volumeref ref="volTPCActive"/>
      <position name="posTPCActive" unit="cm" x="-${attributes['aTPC_xoffset']}" y="0" z="0"/>
     </physvol>
  </volume>


<volume name="volCryostat">
   <materialref ref="LAr"/>
   <solidref ref="Cryostat"/>

   <physvol>
    <volumeref ref="volTPC"/>
    <position name="posTPC" unit="cm" x="-${attributes['aTPC_xoffset']}" y="0" z="0"/>
   </physvol>   
</volume>


<volume name="volDetEnclosure">
   <materialref ref="LAr"/>
   <solidref ref="DetEnclosure"/>

   <physvol>
    <volumeref ref="volCryostat"/>
    <position name="posCryostat" unit="cm" x="0" y="0" z="0"/>
   </physvol>      
</volume>