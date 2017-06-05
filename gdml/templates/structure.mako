<structure>
  %if attributes['wires_on']:
  <%include file="structure/microplane.mako"/>
  <%include file="structure/microplanevert.mako"/>
  %endif
  <%include file="structure/groundplate.mako"/>
  <%include file="structure/cathode.mako"/>
  <%include file="structure/fieldcage.mako"/>
  <%include file="structure/tpc.mako"/>
  <%include file="structure/pmt.mako"/>
  <%include file="structure/granite.mako"/>
  <%include file="structure/extras.mako"/>
  <%include file="structure/cryostat.mako"/>
  <%include file="structure/vetowall.mako"/>
  <%include file="structure/crt_a.mako"/>
  <%include file="structure/crt_b.mako"/>
  <%include file="structure/enclosure.mako"/>
  <%include file="structure/world.mako"/>
</structure>
