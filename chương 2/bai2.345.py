import xml.dom.minidom
# bài 2.3.4
_path = "chương 2/sample.xml"
dom = xml.dom.minidom.parse(_path)

company_element = dom.documentElement

company_name = company_element.getElementsByTagName("name")[0].firstChild.nodeValue
print(f"Company Name: {company_name}")

j = company_element.getElementsByTagName("staff")

for i in j:
    id = i.getAttribute("id")
    name = i.getElementsByTagName("name")[0].firstChild.nodeValue
    salary = i.getElementsByTagName("salary")[0].firstChild.nodeValue

    print(f"\nStaff ID: {id}")
    print(f"Staff Name: {name}")
    print(f"Staff Salary: {salary}")
# bài 2.5
elements = dom.getElementsByTagName("*")

for element in elements:
    print(f"Element Name: {element.nodeName}")
dom.unlink()
# đóng tài liệu xml