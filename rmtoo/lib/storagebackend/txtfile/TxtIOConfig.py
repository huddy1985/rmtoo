'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Text IO Configuration
  This holds the configuration for the TxtIO class.
   
 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

from rmtoo.lib.RMTException import RMTException

class TxtIOConfig:

    def __init__(self, config=None, type_str=""):
        self.__max_line_length = 80
        if config != None:
            self.__init_overwrite(config, type_str)

    def get_max_line_length(self):
        return self.__max_line_length

    def __init_overwrite(self, config, type_str):
        '''Overwrite the existing default parameters with parameters
           from the configuration.'''
        self.__max_line_length = config.get_integer(
                                'max_input_line_length', 80)
        if self.__max_line_length < 0:
            raise RMTException(72, "max_input_line_length for type [%s] is "
                        "negative [%s]" % (type_str, self.__max_line_length))


