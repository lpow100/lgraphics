import pygame

mousestate = True
objects = []

class RGB:
    def __init__(self, r:int, g:int, b:int):
        self._values = (r, g, b)

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value:int):
        temp = list(self._values)
        temp[index] = value
        self._values = tuple(temp)

    def __repr__(self):
        return repr(self._values)

def asT(color: RGB):
    """private func to turn RGB type to tuple for pygame"""
    return (int(color[0]), int(color[1]), int(color[2]))

class Shape:
    def __init__(self,xypairs,screen:pygame.Surface,color:RGB,type) -> None:
        self.type = type
        self.screen = screen
        self.color = color
        self.xy = xypairs
    def addxy(self,x:int=0,y:int=0):
        for i in range(0,len(self.xy)):
            obj = self.xy[i]
            self.xy[i] = (obj[0]+x,obj[1]+y)

def draw(shape:Shape):
    if shape.type == "circle":
        pygame.draw.ellipse(shape.screen,asT(shape.color),shape.xy)
    else:
        pygame.draw.polygon(shape.screen,asT(shape.color),shape.xy)
    

class Window:
    def __init__(self, width, height, title, bgcolor=RGB(0, 0, 0)):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.bgcolor = bgcolor
        self.size = (width // 2, height // 2)
    def create_square(self, x1, y1, x2, y2, color):
        """makes a square"""
        x1 += self.size[0]
        y1 += self.size[1]
        x2 += self.size[0]
        y2 += self.size[1]
        temp = Shape([(x1,y1),(x1,y2),(x2,y2),(x2,y1)],self.screen,color,"square")
        objects.append(temp)
        return temp

    def create_circle(self, x1, y1, x2, y2, color):
        """makes a circle"""
        x1 += self.size[0]
        y1 += self.size[1]
        x2 += self.size[0]
        y2 += self.size[1]
        temp =  Shape([(x1,y1),(x1,y2),(x2,y2),(x1,y2)],self.screen,color,"circle")
        
        objects.append(temp)
        return temp

    def create_triangle(self, x1, y1, x2, y2, color):
        """makes a simple triangle"""
        triangle_points = [
            (self.size[0]+x1,self.size[1]+y1),
            (self.size[0]+x2,self.size[1]+y2/2),
            (self.size[0]+x1,self.size[0]+y2)
        ]
        temp = Shape(triangle_points,self.screen,color,"triangle")
        objects.append(temp)
        return temp

    def create_polygon(self, xypoints, color):
        """makes an advanced polygon"""
        for obj in xypoints:
            obj = (obj[0]+self.size[0],obj[1]+self.size[1])
        temp =  Shape(xypoints,self.screen,color,"polygon")
        objects.append(temp)
        return temp
    
    def clear_screen(self):
        self.screen.fill(asT(self.bgcolor))
    
    def move(self,shape:Shape,x:int=0,y:int=0):
        shape.addxy(x,y)

class Input:
    @staticmethod
    def get_keypress(key):
        keys = pygame.key.get_pressed()
        if keys[eval(f"pygame.K_{key.lower()}")]:
            return True

    @staticmethod
    def mouse_down(button):
        global mousestate
        if pygame.mouse.get_pressed()[button]:
            if mousestate:
                mousestate = False
                return True
        else:
            mousestate = True

    @staticmethod
    def mouse_pos():
        return pygame.mouse.get_pos()


def update(window:Window):
    pygame.display.flip()
    for obj in objects:
        window.clear_screen()
        draw(obj)

def running():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def quit():
    pygame.quit()


