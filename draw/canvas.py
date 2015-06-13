from threading import Timer
from uuid import uuid4
import os

class Canvas(object):
    def __init__(self):
        self.uuid = "canvas" + str(uuid4())
        self.css = {
            "width": "500px",
            "height": "500px",
            "background-color": "white"
        }
        self.loop_func = None
        self.interval = 0.1
        self.time = 0
        self.stop = False
        self.stack = []

    def begin(self):
        def func():
            self.loop_func(self.time)
            self.send()
            self.time += 1
            if not self.stop:
                timer = Timer(self.interval, func)
                timer.start()
        func()
    
    def show(self):
        from jinja2 import Template
        from IPython.core.display import display, HTML
        from IPython.kernel.comm import Comm

        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates/template.html"))
        template = Template(open(path).read())
        css = str(self.css).replace("{", "").replace("}", "").replace(",", ";").replace("\'", "")

        html = template.render(**{
            "canvas_id": self.uuid,
            "svg_style": css
        })

        display(HTML(html))
        self.comm = Comm("Draw")

        if self.loop_func is not None:
            self.begin()
        else:
            self.send()

    def add(self, obj):
        import re
        r = re.compile(r"__.*__")
        for attr in dir(obj):
            m = getattr(obj, str(attr))
            if callable(m) and not r.match(str(attr)):
                def make_func():
                    m_ = m
                    def func(*args, **kw):
                        self.stack.append(("update", obj))
                        return m_(*args, **kw)
                    return func

                setattr(obj, str(attr), make_func())

        self.stack.append(("append", obj))

    def send(self):
        self.comm.send({
            "canvas_id": self.uuid,
            "queue": [{
                "method": s[0],
                "type": s[1].__class__.__name__.lower(),
                "attr": s[1].attr,
                "selector_id": s[1].uuid
            } for s in self.stack]
        })
        self.stack = []

    def loop(self, func):
        self.loop_func = func

    def width(self, val):
        self.css["width"] = str(val) + "px"

    def height(self, val):
        self.css["height"] = str(val) + "px"

    def background_color(self, val):
        self.css["background-color"] = val
