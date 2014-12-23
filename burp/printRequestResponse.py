# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

from burp import IBurpExtender
from burp import IHttpListener

class BurpExtender(IBurpExtender, IHttpListener):

	def registerExtenderCallbacks(self, callbacks):
		self._callbacks = callbacks
		callbacks.setExtensionName("Request & Response")
		callbacks.registerHttpListener(self)
		return

	def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
		if not messageIsRequest:
			print '########## Request ##########'
			for line in messageInfo.getRequest().tostring().splitlines():
				if len(line) == 0:
					break
				else:
					print line
			
			print '########## Response ##########'
			for line in messageInfo.getResponse().tostring().splitlines():
				if len(line) == 0:
					break
				else:
					print line
					
			print '########## END ##########'
			print
			return
