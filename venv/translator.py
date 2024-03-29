
from translate import Translator

translator = Translator(to_lang="ja")
translation = translator.translate("This is a pen.")

try:
    translation = translator.translate("Engineering is the use of scientific principles to design and build machines, "
                                       "structures, and other items, including bridges, tunnels, roads, vehicles, "
                                       "and buildings. The discipline of engineering encompasses a broad range of "
                                       "more specialized fields of engineering, each with a more specific emphasis on "
                                       "particular areas of applied mathematics, applied science, and types of "
                                       "application. See glossary of engineering.")
    print(translation)
    # with open('./test.txt', mode='r') as my_file: #You can load a file to convert here using python I/O
    #     text = my_file.read()
    #     translation = translator.translate(text)
except FileNotFoundError as e:
    print('check your file path')
