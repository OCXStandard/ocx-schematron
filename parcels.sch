<schema xmlns="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt3"> <pattern>
<rule context="article">
<assert test="starts-with(@code, /inventory-list/@depcode)"> The article code must start with the right prefix </assert> </rule>
</pattern> </schema>