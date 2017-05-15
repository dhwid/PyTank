from xml.dom import minidom, Node



class History:

    def __init__(self):
        self.doc = minidom.Document()



        self.history = self.doc.createElement('history')
        self.doc.appendChild(self.history)

        self.agent = self.doc.createElement('agent')
        self.history.appendChild(self.agent)

        self.oponent = self.doc.createElement('oponent')
        self.history.appendChild(self.oponent)




    def addAgent(self,movement):

        move = self.doc.createElement('move')
        self.agent.appendChild(move)
        move.appendChild(self.doc.createTextNode(movement))

        #print(self.doc.toprettyxml(indent='   '))

    def addOponent(self,movement):

        move = self.doc.createElement('move')
        self.oponent.appendChild(move)
        move.appendChild(self.doc.createTextNode(movement))

        #print(self.doc.toprettyxml(indent='   '))


    def saveXML(self):

        f = open("history.xml", "w")
        f.write(self.doc.toprettyxml())
        f.close()

    def parseXML(self,agentHistory):
        f = open("history.xml", "r")
        root = minidom.parse(f)

        for elem in root.getElementsByTagName('agent'):
            for x in elem.childNodes:
                if x.nodeType == Node.ELEMENT_NODE:
                    agentHistory.append(x.childNodes[0].data)


