<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <title>Large Purchase Order business rules</title>
  <ns prefix="po" uri="http://itb.ec.europa.eu/sample/po.xsd"/>
  <pattern name="Check order items">
    <rule context="/po:purchaseOrder/po:items/po:item">
      <assert test="number(po:quantity) > 10" flag="fatal" id="PO-01">[PO-01] The quantities of items for large orders must be greater than 10.</assert>
    </rule>
  </pattern>	
</schema>