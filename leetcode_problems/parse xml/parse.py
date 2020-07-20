import xml.etree.ElementTree as ET
if __name__=='__main__':
    tree = ET.parse('C:\\Users\\vishatha\Desktop\\New folder (3)\\wf_oddeven.xml')
    root = tree.getroot()
    #print(root)
    col = []

    dd = root.find('./REPOSITORY/FOLDER/SOURCE/SOURCEFIELD')
    print(dd.attrib['NAME'])
    print(dd.keys)

    print('Select '+ dd.attrib['OWNERNAME']+'.'+dd.attrib['NAME'])




    # for child in root.iter(tag = 'SOURCE'):
    #     print(child.tag, child.attrib)
    #     s_tablename = child.attrib['NAME']
    #     s_databasename = child.attrib['DBDNAME']
    #     s_ownername = child.attrib['OWNERNAME']
    #
    # for child in root.iter(tag = 'TARGET'):
    #     print(child.tag, child.attrib)
    #     t_tablename = child.attrib['NAME']
    #
    # for child in root.iter(tag = 'TARGETFIELD'):
    #     print(child.tag, child.attrib)




# if __name__=='__main__':
#     file =xml.dom.minidom.parse('C:\\Users\\vishatha\Desktop\\New folder (3)\\wf_oddeven.XML')
#     print(file.nodeName)
#     s = file.getElementsByTagName("SOURCE")
#     print(s)
#     for x in s:
#         print(s)
