# animal package
# dog, cat modules
# dog, cat modules can say "hi"

from animal import dog #animal 패키지에서 dog 라는 모듈을 갖고와줘
from animal import cat # cat animal 패키지에서 cat 이라는 모듈을 갖고와줘

from animal import * #animal 패키지에서 갖고 있는 모듈을 다 불러와

d = dog.Dog() # instance
d.hi()

c = cat.Cat()
c.hi()

d = Dog()
c = Cat()

d.hi()
c.hi()