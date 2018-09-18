import xml.etree.ElementTree as ET
import json
import urllib


def convertXML2JSON(xmlLoc):
    tree = ET.parse(urllib.urlopen(xmlLoc))
    data = {}
    root = tree.getroot()
    i = 0
    for element in root.iter():
        data[i] = element.tag, element.text
        # print("%s - %s" % (element.tag, element.text))
    i = i + 1
    result = json.dumps(data)
    return result


xmldata = convertXML2JSON("/Users/martin-pierreroy/Temp/example_optel_datastruct.xml")
print
xmldata;
