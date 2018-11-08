import xml.etree.ElementTree as ET
import pickle

tree = ET.parse("../blasting_preconceptions/Parse/output/chem_list.xml")
root = tree.getroot()
chem_names = []
for child in root:
    chem_names.append(child.attrib['name'])

pickle.dump(chem_names, open("chem_names.pkl","wb"))