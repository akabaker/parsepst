ParsePST
--------

1. Convert your PST to an mbox format use the Linux utility "readpst".

	- yum install libpst
	- readpst <pst file> -o <output dir>

2. Configure file paths in parsepst.py (this should be a command line option or
   confg file). Then execute:
	
	- parsepst > out.html
