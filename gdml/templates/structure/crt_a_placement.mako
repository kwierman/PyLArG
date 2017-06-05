%if attributes['gen_crt_a'] and not attributes['gen_crt_b']:
  % for module in attributes['auxdet_positions']:
      %if module<49:
        %for strip in attributes['auxdet_positions'][module]:
            <physvol>
              <volumeref ref="volAuxDet_Module_${module}_strip_${strip}"/>
              <position name="posAMod_${module}_strip_${strip}" unit="cm" 
                x="${attributes['auxdet_positions'][module][strip]['x']}"    
                y="${attributes['auxdet_positions'][module][strip]['y']}"    
                z="${attributes['auxdet_positions'][module][strip]['z']}" />
            </physvol>
        %endfor
      % endfor
      % for module in attributes['module_positions']:
        %for strip in attributes['module_positions'][module]:
            <physvol>
              <volumeref ref="volModule_${module}_strip_${strip}"/>
              <position name="posAMod_${module}_strip_${strip}" unit="cm" 
                x="${attributes['module_positions'][module][strip]['x']}"    
                y="${attributes['module_positions'][module][strip]['y']}"    
                z="${attributes['module_positions'][module][strip]['z']}" />
            </physvol>
        %endfor
      %endfor
  %endif
%endif
