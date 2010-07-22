#
# xml output class
#
# This is a first version of xml output.
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from xml.dom.minidom import Document
from rmtoo.lib.Requirement import Requirement

class xml1:

    def __init__(self, param):
        self.output_filename = param[0]

    def set_topics(self, topics):
        self.topic_set = topics.get(param[1])

    # Create MAkefile Dependencies
    def cmad(self, reqscont, ofile):
        ofile.write("%s: ${REQS}\n\t${CALL_RMTOO}\n" % (self.output_filename))

    def name2xmltag(self, name):
        return name.replace(" ", "_").lower()

    def output_req(self, req, doc, sobj):
        # Create the req element
        req_xml = doc.createElement("requirement")
        sobj.appendChild(req_xml)

        for t in ["Name", "Priority", "Effort estimation",
                  "Invented by", "Invented on", "Description",
                  "Rationale", "Factor", "Owner", ]:
            tm = doc.createElement(self.name2xmltag(t))
            req_xml.appendChild(tm)

            if req.tags[t]!=None:
                tn = doc.createTextNode(str(req.tags[t]))
            tm.appendChild(tn)

        if "Status" in req.tags:
            tm = doc.createElement("status")
            req_xml.appendChild(tm)
            if req.tags["Status"]==Requirement.st_not_done:
                tn = doc.createTextNode("not done")
            else:
                tn = doc.createTextNode("finished")
            tm.appendChild(tn)

        if "Type" in req.tags:
            tm = doc.createElement("type")
            req_xml.appendChild(tm)
            if req.tags["Type"]==Requirement.rt_master_requirement:
                tn = doc.createTextNode("master requirement")
            elif req.tags["Type"]==Requirement.rt_initial_requirement:
                tn = doc.createTextNode("initial requirement")
            elif req.tags["Type"]==Requirement.rt_design_decision:
                tn = doc.createTextNode("design decision")
            elif req.tags["Type"]==Requirement.rt_requirement:
                tn = doc.createTextNode("requirement")
            else:
                assert(False)
            tm.appendChild(tn)

        if "Class" in req.tags:
            tm = doc.createElement("class")
            req_xml.appendChild(tm)
            if req.tags["Class"]==Requirement.ct_implementable:
                tn = doc.createTextNode("implementable")
            else:
                tn = doc.createTextNode("detailable")
            tm.appendChild(tn)

    def output_reqset(self, reqset, doc, sobj):
        # Create the reqset element
        reqset_xml = doc.createElement("reqset")
        sobj.appendChild(reqset_xml)

        for req, v in reqset.reqs.iteritems():
            self.output_req(v, doc, reqset_xml)

    def output(self, reqscont):
        # Create the minidom document
        doc = Document()

        # This outputs only the current set of requirements (not the
        # whole history). 
        reqscont_xml = doc.createElement("reqscont")
        doc.appendChild(reqscont_xml)

        self.output_reqset(reqscont.base_requirement_set, doc, reqscont_xml)

        fd = file(self.output_filename, "w")
        fd.write(doc.toxml())
        fd.close()
