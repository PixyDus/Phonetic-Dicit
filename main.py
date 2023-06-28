import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

data_into_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_into_dict)

word = input("Enter a word: ").upper()
output_list = [data_into_dict[letter] for letter in word]
print(output_list)