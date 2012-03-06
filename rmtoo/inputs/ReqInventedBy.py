'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Tag Invented by handling
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.ReqTagGeneric import ReqTagGeneric
from rmtoo.lib.RMTException import RMTException
from rmtoo.lib.InputModuleTypes import InputModuleTypes

class ReqInventedBy(ReqTagGeneric):

    def __init__(self, config):
        ReqTagGeneric.__init__(self, config, "Invented by",
                      set([InputModuleTypes.ctstag, InputModuleTypes.reqtag]))

    def rewrite(self, rid, req):
        # This tag (Invented by) is mandatory
        self.check_mandatory_tag(rid, req, 5)

        t = req[self.get_tag()].get_content()
        # This must be one of the inventors
        # 'flonatel' is always allowed to add things.
        # (This is needed for the collections handling - which always
        #  comes from flonatel.
        if t not in self.get_config().get_value('requirements.inventors') \
            and t != "flonatel":
            raise RMTException(6, "Invalid invented by '%s'. Must be one "
                               "of the inventors '%s'" %
                               (t, self.get_config().get_value(
                                            'requirements.inventors')), rid)

        del req[self.get_tag()]
        return self.get_tag(), t
