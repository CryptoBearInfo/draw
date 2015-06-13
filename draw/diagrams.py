from uuid import uuid4

def define_attributes(cls, names):
    for name in names:
        def make_func():
            name_ = name
            def func(self, val=None):
                if val is not None:
                    self.attr[name_] = val
                else:
                    return self.attr[name_]
            return func
        setattr(cls, name, make_func())

class Diagram(object):
    def __init__(self, **kw):
        self.attr = {}
        self.css = {}
        self.uuid = "diagram" + str(uuid4())

        for k, v in kw.items():
            getattr(self, k)(v)
        return

    def update(self, **kw):
        for k, v in kw.items():
            getattr(self, k)(v)
        return

class Rect(Diagram):
    def __init__(self, x, y, width=100, height=100, **kw):
        super(Rect, self).__init__(**dict({
            "x": x,
            "y": y,
            "width": width,
            "height": height
        }, **kw))
        return

class Circle(Diagram):
    def __init__(self, x, y, r=10, **kw):
        super(Circle, self).__init__(**dict({
            "cx": x,
            "cy": y,
            "r": r
        }, **kw))
        return

class Line(Diagram):
    def __init__(self, x1, y1, x2, y2, **kw):
        super(Line, self).__init__(**dict({
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2
        }, **kw))
        return

define_attributes(Diagram, ["stroke", "stroke-width", "fill"])
define_attributes(Rect, ["x", "y", "width", "height"])
define_attributes(Circle, ["cx", "cy", "r"])
define_attributes(Line, ["x1", "y1", "x2", "y2"])
