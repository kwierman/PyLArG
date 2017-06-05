%if attributes['gen_vetowall']:
  %for i in range(267):
    <volume name="volAuxDet${i}">
      <materialref ref="Polystyrene"/>
      <solidref ref="AuxDet${i}"/>
    </volume>
  %endfor
%endif
