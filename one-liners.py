# python one-liners
# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

python -c "import pefile,sys;pe=pefile.PE(sys.argv[1],fast_load=False);print pe.dump_info()" malware.exe
