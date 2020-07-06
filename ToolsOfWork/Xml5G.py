import xml.etree.ElementTree as ET
tree=ET.parse('netconf-ITBBU-CMCC-GZ.xml')
root=tree.getroot()
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag,'---',child.attrib)
