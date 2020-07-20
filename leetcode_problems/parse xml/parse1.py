import xml.etree.ElementTree as ET
source_fields=[]
target_fields=[]
tree = ET.parse('C:\\Users\\vishatha\Desktop\\New folder (3)\\wf_oddeven.XML')
# wf_m_test_emp
#wf_oddeven
root = tree.getroot()
name = []

for items in root.findall('./REPOSITORY/FOLDER'):
    database = items.find('SOURCE').get('OWNERNAME')
    source_table = items.find('SOURCE').get('NAME')
    target_table = items.find('TARGET').get('NAME')

    for source in items.find('SOURCE'):
        value = source.get('NAME')
        source_fields.append(database+"."+source_table+"."+value)
    for target in items.find('TARGET'):
        value1 = target.get('NAME')
        target_fields.append(value1)
    target = ",".join(target_fields)
    source = ",".join(source_fields)

#     for x in items.findall('MAPPING'):
#         for y in x.find('TRANSFORMATION'):
#             name.append(y.get('NAME'))
#
#
#
# print(','.join(name))

print("INSERT INTO "+database+"."+target_table+"("+target+")\nSELECT "\
    +source+ "\nFROM " +database+"."+source_table)
