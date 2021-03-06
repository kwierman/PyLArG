
<materials>
  <element name="bromine"   formula="Br"     Z="35"> <atom value="79.904"  /> </element>
  <element name="hydrogen"  formula="H"      Z="1">  <atom value="1.0079"  /> </element>
  <element name="nitrogen"  formula="N"      Z="7">  <atom value="14.0067" /> </element>
  <element name="oxygen"    formula="O"      Z="8">  <atom value="15.999"  /> </element>
  <element name="aluminum"  formula="Al"     Z="13"> <atom value="26.9815"/>  </element>
  <element name="silicon"   formula="Si"     Z="14"> <atom value="28.0855"/>  </element>
  <element name="carbon"    formula="C"      Z="6">  <atom value="12.0107"/>  </element>
  <element name="potassium" formula="K"      Z="19"> <atom value="39.0983"/>  </element>
  <element name="chromium"  formula="Cr"     Z="24"> <atom value="51.9961"/>  </element>
  <element name="iron"      formula="Fe"     Z="26"> <atom value="55.8450"/>  </element>
  <element name="nickel"    formula="Ni"     Z="28"> <atom value="58.6934"/>  </element>
  <element name="calcium"   formula="Ca"     Z="20"> <atom value="40.078"/>   </element>
  <element name="magnesium" formula="Mg"     Z="12"> <atom value="24.305"/>   </element>
  <element name="sodium"    formula="Na"     Z="11"> <atom value="22.99"/>    </element>
  <element name="titanium"  formula="Ti"     Z="22"> <atom value="47.867"/>   </element>
  <element name="argon"     formula="Ar"     Z="18"> <atom value="39.9480"/>  </element>

  <material Z="1" formula=" " name="Vacuum">
   <D value="1.e-25" unit="g/cm3"/>
   <atom value="1.0079"/>
  </material>

  <material name="ALUMINUM_Al" formula="ALUMINUM_Al">
   <D value="2.6990" unit="g/cm3"/>
   <fraction n="1.0000" ref="aluminum"/>
  </material>

  <material name="SILICON_Si" formula="SILICON_Si">
   <D value="2.3300" unit="g/cm3"/>
   <fraction n="1.0000" ref="silicon"/>
  </material>

  <material name="epoxy_resin" formula="C38H40O6Br4">
   <D value="1.1250" unit="g/cm3"/>
   <composite n="38" ref="carbon"/>
   <composite n="40" ref="hydrogen"/>
   <composite n="6"  ref="oxygen"/>
   <composite n="4"  ref="bromine"/>
  </material>

  <material name="PU_foam_dense" formula="C25H42N2O6">
   <D value=".224" unit="g/cm3"/>
   <composite n="25" ref="carbon"/>
   <composite n="42" ref="hydrogen"/>
   <composite n="2" ref="nitrogen"/>
   <composite n="6" ref="oxygen"/>
 </material>

 <material name="PU_foam_light" formula="C25H42N2O6">
	 <D value=".0384" unit="g/cm3"/>
	 <composite n="25" ref="carbon"/>
	 <composite n="42" ref="hydrogen"/>
	 <composite n="2" ref="nitrogen"/>
	 <composite n="6" ref="oxygen"/>
 </material>

  <material name="SiO2" formula="SiO2">
   <D value="2.2" unit="g/cm3"/>
   <composite n="1" ref="silicon"/>
   <composite n="2" ref="oxygen"/>
  </material>

  <material name="Al2O3" formula="Al2O3">
   <D value="3.97" unit="g/cm3"/>
   <composite n="2" ref="aluminum"/>
   <composite n="3" ref="oxygen"/>
  </material>

  <material name="Fe2O3" formula="Fe2O3">
   <D value="5.24" unit="g/cm3"/>
   <composite n="2" ref="iron"/>
   <composite n="3" ref="oxygen"/>
  </material>

  <material name="CaO" formula="CaO">
   <D value="3.35" unit="g/cm3"/>
   <composite n="1" ref="calcium"/>
   <composite n="1" ref="oxygen"/>
  </material>

  <material name="MgO" formula="MgO">
   <D value="3.58" unit="g/cm3"/>
   <composite n="1" ref="magnesium"/>
   <composite n="1" ref="oxygen"/>
  </material>

  <material name="Na2O" formula="Na2O">
   <D value="2.27" unit="g/cm3"/>
   <composite n="2" ref="sodium"/>
   <composite n="1" ref="oxygen"/>
  </material>

  <material name="TiO2" formula="TiO2">
   <D value="4.23" unit="g/cm3"/>
   <composite n="1" ref="titanium"/>
   <composite n="2" ref="oxygen"/>
  </material>

  <material name="fibrous_glass">
   <D value="2.74351" unit="g/cm3"/>
   <fraction n="0.600" ref="SiO2"/>
   <fraction n="0.118" ref="Al2O3"/>
   <fraction n="0.001" ref="Fe2O3"/>
   <fraction n="0.224" ref="CaO"/>
   <fraction n="0.034" ref="MgO"/>
   <fraction n="0.010" ref="Na2O"/>
   <fraction n="0.013" ref="TiO2"/>
  </material>

  <material name="FR4">
   <D value="1.5224" unit="g/cm3"/>
   <fraction n="0.47" ref="epoxy_resin"/>
   <fraction n="0.53" ref="fibrous_glass"/>
  </material>

  <material name="STEEL_STAINLESS_Fe7Cr2Ni" formula="STEEL_STAINLESS_Fe7Cr2Ni">
   <D value="7.9300" unit="g/cm3"/>
   <fraction n="0.0010" ref="carbon"/>
   <fraction n="0.1792" ref="chromium"/>
   <fraction n="0.7298" ref="iron"/>
   <fraction n="0.0900" ref="nickel"/>
  </material>

  <material name="LAr" formula="LAr">
   <D value="1.40" unit="g/cm3"/>
   <fraction n="1.0000" ref="argon"/>
  </material>

  <material formula=" " name="Air">
   <D value="0.001205" unit="g/cm3"/>
   <fraction n="0.781154" ref="nitrogen"/>
   <fraction n="0.209476" ref="oxygen"/>
   <fraction n="0.00937" ref="argon"/>
  </material>

  <material formula=" " name="G10">
   <D  value="1.7" unit="g/cm3" />
   <fraction n="0.2805" ref="silicon"  />
   <fraction n="0.3954" ref="oxygen"   />
   <fraction n="0.2990" ref="carbon"   />
   <fraction n="0.0251" ref="hydrogen" />
  </material>

  <material formula=" " name="Granite">
   <D value="2.7" unit="g/cm3"/>
   <fraction n="0.438" ref="oxygen"/>
   <fraction n="0.257" ref="silicon"/>
   <fraction n="0.222" ref="sodium"/>
   <fraction n="0.049" ref="aluminum" />
   <fraction n="0.019" ref="iron" />
   <fraction n="0.015" ref="potassium"/>
  </material>

  <material formula=" " name="ShotRock">
   <D value="1.62" unit="g/cm3"/>
   <fraction n="0.438" ref="oxygen"/>
   <fraction n="0.257" ref="silicon"/>
   <fraction n="0.222" ref="sodium"/>
   <fraction n="0.049" ref="aluminum" />
   <fraction n="0.019" ref="iron" />
   <fraction n="0.015" ref="potassium"/>
  </material>

  <material formula=" " name="Dirt">
   <D value="1.7" unit="g/cm3"/>
   <fraction n="0.438" ref="oxygen"/>
   <fraction n="0.257" ref="silicon"/>
   <fraction n="0.222" ref="sodium"/>
   <fraction n="0.049" ref="aluminum" />
   <fraction n="0.019" ref="iron" />
   <fraction n="0.015" ref="potassium"/>
  </material>

  <material formula=" " name="Concrete">
   <D  value="2.3" unit="g/cm3"/>
   <fraction n="0.530" ref="oxygen"/>
   <fraction n="0.335" ref="silicon"/>
   <fraction n="0.060" ref="calcium"/>
   <fraction n="0.015" ref="sodium"/>
   <fraction n="0.020" ref="iron"/>
   <fraction n="0.040" ref="aluminum"/>
  </material>

  <material formula="H2O" name="Water">
   <D value="1.0" unit="g/cm3"/>
   <fraction n="0.1119" ref="hydrogen"/>
   <fraction n="0.8881" ref="oxygen"/>
  </material>

  <material formula="Ti" name="Titanium">
   <D value="4.506" unit="g/cm3" />
   <fraction n="1."  ref="titanium" />
  </material>

  <material name="TPB" formula="TPB">
   <D value="1.40" unit="g/cm3"/>
   <fraction n="1.0000" ref="argon"/>
  </material>

  <material name="Glass">
   <D value="2.74351" unit="g/cm3"/>
   <fraction n="0.600" ref="SiO2"/>
   <fraction n="0.118" ref="Al2O3"/>
   <fraction n="0.001" ref="Fe2O3"/>
   <fraction n="0.224" ref="CaO"/>
   <fraction n="0.034" ref="MgO"/>
   <fraction n="0.010" ref="Na2O"/>
   <fraction n="0.013" ref="TiO2"/>
  </material>

  <material name="Acrylic">
   <D value="1.19" unit="g/cm3"/>
   <fraction n="0.600" ref="carbon"/>
   <fraction n="0.320" ref="oxygen"/>
   <fraction n="0.080" ref="hydrogen"/>
  </material>

  <material name="Polystyrene">
   <D value="1.06" unit="g/cm3"/>
   <fraction n="0.077418" ref="hydrogen"/>
   <fraction n="0.922582" ref="carbon"/>
  </material>

  <material name="Argon_gas_87K" formula="Ar">
   <D value="0.0056" unit="g/cm3"/> <!-- standard pressure, 87.3K -->
   <fraction n="1.0000" ref="argon"/>
  </material>

</materials>
