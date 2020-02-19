import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse("samplexml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    new_skill = doc.createElement("skill")
    new_skill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(new_skill)

    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute('name'))





if __name__ == '__main__':
    main()
