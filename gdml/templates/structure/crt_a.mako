%if attributes['gen_crt_a'] and not attributes['gen_crt_b']:
  %for module in range(73):
    %for strip in range(16):
      <volume name="volModule_${module}_strip_${strip}">
        <materialref ref="ALUMINUM_Al"/>
        <solidref ref="Module_${module}_strip_${strip}"/>
      </volume>
      <volume name="volAuxDet_Module_${module}_strip_${strip}">
        <materialref ref="Polystyrene"/>
        <solidref ref="AuxDet_Module_${module}_strip_${strip}"/>
      </volume>
    %endfor
  %endfor
%endif
