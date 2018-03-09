# CustomPhylogen
Software for Phylogenetic tree generation of several proteins of same gene

PURPOSE of the software(the AdvProAssessment.py file):

	The input is as many individually selected proteins(UniProt search entries) as the user wants which are all produced by the same gene(e.g. gene:BRCA1). The output is a multiple sequence alignment, phylogenetic tree and automated description of the generated phylogenetic tree, for all the selected proteins.


INSTALLATION:

	Note: install python3 and pip3("sudo apt install python3-pip3"), in order to run the .py file.

	Packages that must be installed(if not yet installed) via Bash(terminal):
	1)Biopython package, "pip3 install biopython"
	2)Bioservices, "pip3 install bioservices"
	3)Bio.Align.Applications, "sudo apt install clustalw"

INPUTS into the command line(bash, terminal):

	Note:Command Line Interface has been set up, in the code, using "import sys".

	In the a terminal command line, type in python3 command, then first argument is the name of the script called AdvProAssessment.py, then gene name for second argument, then in the third argument the total number of UniProt records(entries) the user wants to align and then enter the record numbers of the chosen records in 4th+ arguments, e.g. python3 AdvProAssessment.py gene:brca1 5 19 22 13 4 45. The "gene:" in the second argument, tells uniprot to only produce entries which have ins gene in their gene name field. "19" in the examples represents the 19th record in the UniProt search results, when "gene:brca1" is queried in the database.  Lastly, for "5" in the example, any value in it's position should equal the total number of arguments after that argument, which in the example are currently five arguments.

	Example Inputs:
	python3 AdvProAssessment.py gene:ins 10 1 2 3 4 5 6 7 8 9 10
	python3 AdvProAssessment.py gene:brca1 5 200 34 1000 2010 571
	python3 AdvProAssessment.py gene:rho 15 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15



OUTPUTS in the the command line :

	1)fasta sequence for each selected uniprot record(entry)
	2)ID and length of sequence for each selected uniprot entry.
	3)Multiple sequence alignment of all selected uniprot entries. 
	4)Phlyogenetic tree of all selected uniprot entries. 
	5)Description the Phylogenetic tree



UNIT TESTING:

	To perform the Unit Testing on the .py file, call on the test file:
	"python3 test_AdvProAssessment.py" in the terminal.





