'''
X-Ways Forensics X-Tensions
P2P Forensic
(C) 2012 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com
'''

import OutputRedirector
import XWF
import re

# The first function that is called when a Python X-Tension is called
def XT_Init(nVersion, nFlags, hMainWnd, lpReserved):
   OutputRedirector.install()
   return 

# Called just before execution of the Python script concludes
def XT_Done(lpReserved):
   return 

def XT_About(hParentWnd, lpReserved):
   print('P2P Forensic by Adam Ziaja <adam@adamziaja.com>')
   return

def XT_Prepare(hVolume, hEvidence, nOpType, lpReserved):
   return

def XT_Finalize(hVolume, hEvidence, nOpType, lpReserved):
   return

def XT_ProcessSearchHit(iSize, nItemID, nRelOfs, nAbsOfs, lpOptionalHitPtr, lpSearchTermID, nLength, nCodePage, nFlags):
   return

def XT_ProcessItem(nItem, reserved):
   return

def XT_ProcessItemEx(nItem, hItem, reserved):
   # 27.12.2012: błąd X-Tensions - nie łapie katalogów, a same pliki(!)
   file_name = XWF.GetItemName(nItem)#.strip()
   #print repr(file_name)
   
   p2p_installers = [r'^aresregular.*_installer\.exe', r'^BitTorrent\.exe', r'^DCPlusPlus\-.*\.exe', r'^eMule.*-Installer\.exe', r'^frostwire\-.*.windows\.exe', r'^uTorrent\.exe', r'^VuzeInstaller\.exe']
   for p2p_installer in p2p_installers:
      if re.search(p2p_installer, file_name, re.IGNORECASE):
         #XWF.AddToReportTable(nItem, 'p2p installers')
		 XWF.AddComment(nItem, 'p2p installers', 0)

   p2p_files = [r'uTorrent$', r'BitTorrent$', r'Ares$', r'eMule$', r'FrostWire \d$', r'Vuze$', r'DC\+\+$', r'.*\.torrent$']
   for p2p_file in p2p_files:
      if re.search(p2p_file, file_name, re.IGNORECASE):
	     # NIE MOZNA DODAWAC FOLDEROW DO RAPORT TABLE
         XWF.AddComment(nItem, 'p2p files', 2)
		 
   return
