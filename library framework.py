'''
Framwork for library that reads in speeches and visualizes them through sankey, ___, ___.
Sarah Klute and Sydney Schulz
DS 3500 Homework 4: Natural Language Processing
'''
# minimum methods for library

from textastic_class import Textastic
import pprint as pp
import textastic_parser as tp
from txt_to_json import txt_to_json

def main():
    # translating to json file
    input_file_1992 = 'Bush_1992.txt'
    output_file_1992 = '1992_speech.json'

    input_file_2000 = 'Clinton_2000.txt'
    output_file_2000 = '2000_speech.json'

    input_file_2008 = 'Bush_2008.txt'
    output_file_2008 = '2008_speech.json'

    input_file_2016 = 'Obama_2016.txt'
    output_file_2016 = '2016_speech.json'

    input_file_2018 = 'Trump_2018.txt'
    output_file_2018 = '2018_speech.json'

    input_file_2022 = 'state_of_the_union.txt'
    output_file_2022 = '2022_speech.json'

    input_file_2023 = 'Biden_sotu_2023.txt'
    output_file_2023 = '2023_speech.json'

    # domain specific txt to json converter
    txt_to_json(input_file_1992, output_file_1992)
    txt_to_json(input_file_2000, output_file_2000)
    txt_to_json(input_file_2008, output_file_2008)
    txt_to_json(input_file_2016, output_file_2016)
    txt_to_json(input_file_2018, output_file_2018)
    txt_to_json(input_file_2022, output_file_2022)
    txt_to_json(input_file_2023, output_file_2023)

    # implimenting class
    tt = Textastic()

    # stop words
    tt.load_stop_words('stopwords.txt')

    # add multiple files, parsing further
    tt.load_text('1992_speech.json', 'Bush_1992', parser=tp.json_parser)
    tt.load_text('2000_speech.json', 'Clinton_2000', parser=tp.json_parser)
    tt.load_text('2008_speech.json', 'Bush_2008', parser=tp.json_parser)
    tt.load_text('2016_speech.json', 'Obama_2016', parser=tp.json_parser)
    tt.load_text('2018_speech.json', 'Trump_2018', parser=tp.json_parser)
    tt.load_text('2022_speech.json', 'Biden_2022', parser=tp.json_parser)
    tt.load_text('2023_speech.json', 'Biden_2023', parser=tp.json_parser)

    pp.pprint(tt.data)

    # generating viz
    tt.compare_num_words()
    tt.sentiment()
    tt.visualize_wordclouds()

    #option 1 for sankey:
    #chosen_words = ['jobs', 'tax', 'terrorists', 'america', 'world', 'economy']
    #tt.generate_sankey_diagram(chosen_words=chosen_words)

    # option 2 for sankey:
    tt.generate_sankey_diagram()


if __name__ == '__main__':
    main()