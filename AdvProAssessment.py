from Bio import SeqIO # SeqIO which is a simple uniform interface for inputing and outputing assorted sequence file formats. 
from bioservices import UniProt # gains access to uniprot database
import sys # this module allows for the command line interface to be set up
from Bio.Align.Applications import ClustalwCommandline # imports command lines wrapper clustalw


def Entry_selection(entry_number): # defines a function called Entry_selection
    s = entry_number # value of entry_number assigned to s
    entry, gene_names = res.split("\n")[s].split("\t") # protein's entry number and gene names are saved in entry and gene_names, respectively
    seq1 = u.retrieve(str(entry), frmt="fasta") # fasta sequence is generated
    return seq1 # will exit function and optionally pass fasta seqeuence expression back to the caller


class Protein_in_Phylogenetic_tree(): #creates a class 

    def __init__(self, i, d): #assigns properties to class
        self.id = i #property of class
        self.descendant_which_splits_from_same_node = d #property of class

    def Phylogenetic_analysis(self): # a function of the class
        if self.descendant_which_splits_from_same_node == "None": # if d is "None" output the below expressions
            print(self.id + " doesn't share a sister group with any of the other proteins.")
            print(self.id + " is either an ingroup or outgroup to all the other proteins in the Phylogenetic tree")
        elif self.descendant_which_splits_from_same_node != "None": # if d doesn't equal "None" output the below expressions
            print(self.id + " belongs to the same sister group as" + self.descendant_which_splits_from_same_node)
            print("Thus," + self.id + " and" + self.descendant_which_splits_from_same_node + " are close relatives of each other")
            print("In addition, all the other proteins in the Phylogenetic tree are the outgroup to" + self.id + " and" + self.descendant_which_splits_from_same_node)


if __name__ == '__main__': #everyting above is can be imported into the test.AdvProAssessment.py unit testing file

    u = UniProt() # assigns the UniProt function to u


    res = u.search(sys.argv[1], frmt="tab", columns="id, genes", limit=None) #accesses UniProt database 

    Number_selections = range(int(sys.argv[2])) # the value third argument in command line is assigned to the Number_selections

    Entry_selection_list = [] # empty list created called Entry_selection_list
    a = 2 # the numerical value 2 is assigned to 

    for y in (Number_selections): # iterates n times, whereby n = Number_selections
        a = a + 1 # for every iteration a increases by one
        Entry_selection_list.append(int(sys.argv[a])) # sets up sys.arg[] for n proteins, whereby n = Number_selections

    for w in Entry_selection_list: # iterates over members of list called Entry_selection_list
        entry, gene_names = res.split("\n")[w].split("\t") # protein's entry number and gene names are saved in entry and gene_names, respectively
        seq = u.retrieve(str(entry), frmt="fasta") # gets the fasta sequence for protein
        print(seq) # outputs value of seq for each iteration


    entry1 = Entry_selection(int(sys.argv[3])) # selects the n entry, whereby n = value of sys.argv[3] in numerical form
    f = open("Clustalfastaseq.txt", "w+") # opens the file called Clustalfastaseq.txt
    f.write(entry1) # writes a fasta sequence that entry1 currently equals
    f.close() # closes the file

    length_list = int(len(Entry_selection_list)) # length of Entry_selection_list list

    for i in Entry_selection_list[1:length_list]: # iteraretes n-1 times, whereby n = length_list
        entry = Entry_selection(i) # assigns the value of Entry_selection(i) to entry
        f = open("Clustalfastaseq.txt", "a") # opens the file called Clustalfastaseq.txt
        f.write('\n') # starts a new line
        f.write(entry) # writes a fasta sequence that entry currently equals
        f.close() # closes the file

    for seq_record in SeqIO.parse("Clustalfastaseq.txt", "fasta"): # parses the file
        print(len(seq_record), "is the length of", seq_record.id) # prints record(entry) id and length

    cline = ClustalwCommandline("clustalw", infile="Clustalfastaseq.txt")
    cline() # imports clustalw command line wrapper

    from Bio import AlignIO # module imported to perform multiple sequence alignment is imported
    align = AlignIO.read("Clustalfastaseq.aln", "clustal") #generates the multiple sequence alignment
    print(align) # outputs the multiple sequence alignment

    from Bio import Phylo # module required to generate phylogenetic tree is imported
    tree = Phylo.read("Clustalfastaseq.dnd", "newick") # generates the phylogenetic tree diagram
    Phylo.draw_ascii(tree) #outputs the phylogenetic tree diagram

    text_file = open("Clustalfastaseq.dnd", "r") #opens and reads the "Clustalfastaseq.dnd" text file
    lines = text_file.readlines() # automaticall creates list in which in each line in file is a item in the list
    text_file.close() #closes the file

    sgroup = dict() #creates empty dictionary called sgroup
    list_sgroup = [] #creates empty list called list_sgroup
    list_sgroupm = [] #creates empty list called list_sgroupm

    len_lines = len(lines) - 1 # the  value of the length of the list called lines minus 1 is assigned to the len_lines variable

    for i in range(len_lines): # iterates n times, whereby n = len_lines
        if "," and "_" in lines[i] and ")" and "_" in lines[i+1]: # if "," and "_" are in a given line and ")" and "_" are in the next line
            sgroup[str(lines[i])] = str(lines[i+1]) # in the sgroup dictionary, the given line is the key and the consective line is the value of the pair
            sgroup[str(lines[i+1])] = str(lines[i]) # in the sgroup dictionary, the given line is the value of the pair and the consective line is the key
            list_sgroup.append(str( lines[i])) # assigns string version of the given line to the list called list_sgroup
            list_sgroup.append(str(lines[i+1])) # assigns string version of the following consecutive line to the list called list_sgroup
        else: # instead
            list_sgroupm.append(str(lines[i])) # assigns string version of the given line to the list called list_sgroupm
            list_sgroupm.append(str(lines[i+1])) # assigns string version of the following consecutive line to the list called list_sgroupm
        
    for i in list_sgroupm: # iterates over members of the list_sgroupm
        if "_" in i: # if the given list_sgroupm member contains "_"
            if i in list_sgroup: # if the given list_sgroupm member is also a member of list_sgroup
                pass # nothing happens
            else: # if the given list_sgroupm member is not in list_sgroup
                sgroup[str(i)] = "None" # sets the given list_sgroupm member as the key and "None" as the value in the sgroup dictionary
                list_sgroup.append(str(i)) # adds the given list_sgroupm member to the list_sgroup 
        else: # if the given list_sgroupm member doesn't contains "_"
            pass # nothing happens


    length_list_sgroup = len(list_sgroup) # assigns length of the list to length_list_sgroup

    for id in list_sgroup[0:length_list_sgroup]: # iterates over members of the list_sgroup
        string_id = str(id) # converts the members of the list_sgroup into strings
        id = Protein_in_Phylogenetic_tree(string_id, sgroup[string_id]) #creates objects for all the proteins for the "Protein_in_Phylogenetic_tree" class.
        id.Phylogenetic_analysis() #outputs the function results for each object of the class
    
