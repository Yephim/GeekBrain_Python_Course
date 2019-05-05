'''
1. Создайте классы Noun и Verb.
2. Настройте наследование от Word.
3. Добавьте защищенное свойство «Грамматические характеристики».
4. Перестройте работу метода show класса Sentence.
5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.
'''

class Word:
    def __init__(self, text='', part_of_speech=''):
        self.text = text
        self.part_of_speech = part_of_speech
    def __str__(self):
        return self.text

class Verb(Word):
    def __init__(self, text='', grammar_properties=''):
        super().__init__(text, 'глагол')
        self.__grammar_properties = grammar_properties
    def get_grammar_properties(self):
        return self.__grammar_properties
class Noun(Word):
    def __init__(self,text='', grammar_properties=''):
        super().__init__(text, 'существительное')
        self.__grammar_properties = grammar_properties
    def get_grammar_properties(self):
        return self.__grammar_properties

class Sentence:
    def __init__(self, content, glossary):
        self.content = content
        self.glossary = glossary
    def show(self):
        return ' '.join((str(self.glossary[i-1]) for i in self.content))
    def show_parts(self):
        return '; '.join((self.glossary[i-1].part_of_speech if type(self.glossary[i-1]) == Word
                              else f'{self.glossary[i-1].part_of_speech} {self.glossary[i-1].get_grammar_properties()}'
                          for i in self.content))


w1 = Word('я', 'местоимение')
w2 = Verb('сделал', 'прошедшего времени, мужского рода, ед.числа')
w3 = Word('доманшнее', 'прилагательное')
w4 = Noun('задание', 'среднего рода, ед.числа')

s1=Sentence([1, 2, 3, 4], [w1, w2, w3, w4])
print(s1.show())
print(s1.show_parts())

s2=Sentence([2, 1, 4], [w1, w2, w3, w4])
print(s2.show())
print(s2.show_parts())
