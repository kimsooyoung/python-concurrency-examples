# Code from InfLearn
# https://www.inflearn.com/course/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90/dashboard

# Class 형태로 iterator 사용

# next 사용
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration("Stopped Iteration.")
        self._idx += 1
        return word

    def __repr__(self):
        return "WordSplit(%s)" % (self._text)


wi = WordSplitter("Do today what you could do tomorrow")

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

### Result ###
#
# WordSplit(['Do', 'today', 'what', 'you', 'could', 'do', 'tomorrow'])
# Do
# today
# what
# you
# could
# do
# tomorrow
