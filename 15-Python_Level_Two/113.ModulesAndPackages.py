import module
module.func_in_module()

import module as mod
mod.func_in_module()

from module import func_in_module
func_in_module()

from module import *
func_in_module()
