<box name="TPC"
 lunit="cm"
 x="${attributes['TPCDepth']}"
 y="${attributes['TPCWidth']}"
 z="${attributes['TPCLength']}"
/>
<box name="TPCActive"
 lunit="cm"
 x="${attributes['TPCActiveDepth']}"
 y="${attributes['TPCActiveHeight']}"
 z="${attributes['TPCActiveLength']}"
/>

<box name="Cryostat"
  lunit="cm"
  x="${attributes['TPCActiveDepth']+0.1}"
  y="${attributes['TPCActiveDepth']+0.1}"
  z="${attributes['TPCActiveDepth']+0.1}"
/>
<box name="DetEnclosure"
  lunit="cm"
  x="${attributes['TPCActiveDepth']+0.2}"
  y="${attributes['TPCActiveDepth']+0.2}"
  z="${attributes['TPCActiveDepth']+0.2}"
/>