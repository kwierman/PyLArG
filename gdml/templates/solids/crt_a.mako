%if attributes['gen_crt_a'] and not attributes['gen_crt_b']:
  %for module in attributes['auxdet_dimensions']:  
    %if module<49:
      %for strip in attributes['auxdet_dimensions'][module]:
        <box lunit="cm" name="AuxDet_Module_${module}_strip_${strip}"    
          x="${attributes['auxdet_dimensions'][module][strip]['x']}"    
          y="${attributes['auxdet_dimensions'][module][strip]['y']}"    
          z="${attributes['auxdet_dimensions'][module][strip]['z']}" />
      %endfor
    %endif
  %endfor
  %for module in attributes['module_dimensions']:
    %if module<49:
      %for strip in attributes['module_dimensions'][module]:
        <box lunit="cm" name="Module_${module}_strip_${strip}"    
          x="${attributes['module_dimensions'][module][strip]['x']}"    
          y="${attributes['module_dimensions'][module][strip]['y']}"    
          z="${attributes['module_dimensions'][module][strip]['z']}" />
      %endfor
    %endif
  %endfor
%endif