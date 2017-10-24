# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: const.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 16:03:33
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-10-22 17:04:14
"""
Descripition:
	const moudle
	rule:
		Const name must be all uppercase
		Const value cannot be modified
Change Activity:
		None
"""
class _const:
	class ConstError(TypeError): pass
	class ConstCaseError(ConstError): pass
	def __setattr__(self, name, value):
		if self.__dict__.has_key(name):
			raise self.ConstError('Can not change const.{0}'.format(name))
		if not name.isupper():
			raise self.ConstCaseError('const name {0} is not all uppercase.'.format(name))
		self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()

