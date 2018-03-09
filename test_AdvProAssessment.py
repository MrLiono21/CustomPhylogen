import unittest
from AdvProAssessment import Protein_in_Phylogenetic_tree

class test_Protein_in_Phylogenetic_tree(unittest.TestCase): #creates a class 

    def test(self):
        cat = Protein_in_Phylogenetic_tree("P4012", "None") # input
        cat_id = "P4012" # expected output
        self.assertEqual(cat_id, cat.id) # expected output compared to output generated by function

    def test1(self):
        cat = Protein_in_Phylogenetic_tree("P4012", "P4013") # input
        cat_descendant_which_splits_from_same_node = "P4013" # expected output
        self.assertEqual(cat_descendant_which_splits_from_same_node, cat.descendant_which_splits_from_same_node) # expected output compared to output generated by function

    
    def test2(self):
        cat = Protein_in_Phylogenetic_tree("P4012", "None") # input
        set = cat.Phylogenetic_analysis() # output generated by function
        house = print("P4012" + " doesn't share a sister group with any of the other proteins.\nP4012" + " is either an ingroup or outgroup to all the other proteins in the Phylogenetic tree") # expected output
        self.assertEqual(house, set) # expected output compared to output generated by function

    def test3(self):
        cat = Protein_in_Phylogenetic_tree("P4012", "P4013") # input
        set = cat.Phylogenetic_analysis() # output generated by function
        house = print("P4012" + " belongs to the same sister group as" + " P4013\nThus," + " P4012" + " and" + " P4013" + " are close relatives of each other\nIn addition," + " all the other proteins in the Phylogenetic tree are the outgroup to" + " P4012" + " and" + " P4013") # expected output
        self.assertEqual(house, set) # expected output compared to output generated by function
        
















if __name__ == '__main__':
    unittest.main()



