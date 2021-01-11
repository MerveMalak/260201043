class DNA:
  def __init__(self,dnaString):
    self.dnaString = dnaString

  def count_nucleotides(self):
    dna_dict = {"A": 0 , "C": 0, "T": 0, "G":0}
    for letter in self.dnaString:
      dna_dict[letter] += 1
    return dna_dict
  
  def calculate_comploment(self):
    reverseDnaString = self.dnaString[::-1]
    complement_string = ""
    dna_dict = {"A": "T", "T":"A", "G": "C", "C":"G"}
    for letter in reverseDnaString:
      complement_string += dna_dict[letter]
    return complement_string

  def count_point_mutations(self,dna):
    hamming_distance = 0 
    for letter in range(len(self.dnaString)):
      if self.dnaString[letter] != dna[letter]:
        hamming_distance += 1
    return hamming_distance

  def find_motif(self,dna):
    len1 = len(self.dnaString)
    len2 = len(dna)
    location_list = []
    for i in range(len1 - len2 +1):
      if self.dnaString[i:i+len2] == dna:
        location_list.append(i)
    return location_list

dna1 = DNA("GATATATGCATATACTT")
print(dna1.count_nucleotides())
print(dna1.calculate_comploment())
print(dna1.count_point_mutations("ATTAGCGCATTACGTAC"))
print(dna1.find_motif("ATAT"))