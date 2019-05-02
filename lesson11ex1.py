'''
1. Создайте класс Word.
2. Добавьте свойства text и part of speech.
3. Добавьте возможность создавать объект слово со значениями в скобках.
4. Создайте класс Sentence
5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
6. Добавьте метод show, составляющий предложение.
7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.
'''

class Word:
    text = ''
    part_of_speech = ''
    def __init__(self,text='',part_of_speech = ''):
        self.text = text
        self.part_of_speech = part_of_speech
class Sentence:
    content = []
    def __init__(self,content=[],glossary=[]):
        self.content = content
        self.glossary = glossary
    def show(self):
        return ' '.join((self.glossary[i-1].text for i in self.content))
    def show_parts(self):
        return ' '.join((self.glossary[i-1].part_of_speech for i in self.content))


w1 = Word('я', 'местоимение')
w2 = Word('сделал', 'глагол')
w3 = Word('доманшнее', 'прилагательное')
w4 = Word('задание', 'существительное')

s1=Sentence([1, 2, 3, 4], [w1, w2, w3, w4])
print(s1.show())
print(s1.show_parts())
s2=Sentence([2, 1, 4], [w1, w2, w3, w4])
print(s2.show())
print(s2.show_parts())
