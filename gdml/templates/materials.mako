
<materials>
  <element name="nitrogen"  formula="N"      Z="7">  <atom value="14.0067" /> </element>
  <element name="oxygen"    formula="O"      Z="8">  <atom value="15.999"  /> </element>
  <element name="titanium"  formula="Ti"     Z="22"> <atom value="47.867"/>   </element>
  <element name="argon"     formula="Ar"     Z="18"> <atom value="39.9480"/>  </element>

  <material formula=" " name="Air">
   <D value="0.001205" unit="g/cm3"/>
   <fraction n="0.781154" ref="nitrogen"/>
   <fraction n="0.209476" ref="oxygen"/>
   <fraction n="0.00937" ref="argon"/>
  </material>

  <material formula="Ti" name="Titanium">
   <D value="4.506" unit="g/cm3" />
   <fraction n="1."  ref="titanium" />
  </material>

  <material name="LAr" formula="LAr">
   <D value="1.40" unit="g/cm3"/>
   <fraction n="1.0000" ref="argon"/>
  </material>

  <material name="Argon_gas_87K" formula="Ar">
   <D value="0.0056" unit="g/cm3"/> <!-- standard pressure, 87.3K -->
   <fraction n="1.0000" ref="argon"/>
  </material>

</materials>
