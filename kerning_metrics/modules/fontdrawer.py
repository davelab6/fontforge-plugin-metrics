
import math

class FontArea:
    def __init__(self, da):
        self.da = da
        self.da.connect("expose_event", self.expose)
        
    def expose(self, widget, event):
        self.context = widget.window.cairo_create()
        
        # set a clip region for the expose event
        self.context.rectangle(event.area.x, event.area.y,
                               event.area.width, event.area.height)
        self.context.clip()
        
        self.draw(self.context)
        
        return False
    
    def draw(self, context):
        rect = self.da.get_allocation()
        x = rect.x + rect.width / 2
        y = rect.y + rect.height / 2
        
        radius = min(rect.width / 2, rect.height / 2) - 5
        
        # clock back
        context.arc(x, y, radius, 0, 2 * math.pi)
        context.set_source_rgb(1, 1, 1)
        context.fill_preserve()
        context.set_source_rgb(0, 0, 0)
        context.stroke()
        
        # clock ticks
        for i in xrange(12):
            context.save()
            
            if i % 3 == 0:
                inset = 0.2 * radius
            else:
                inset = 0.1 * radius
                context.set_line_width(0.5 * context.get_line_width())
            
            context.move_to(x + (radius - inset) * math.cos(i * math.pi / 6),
                            y + (radius - inset) * math.sin(i * math.pi / 6))
            context.line_to(x + radius * math.cos(i * math.pi / 6),
                            y + radius * math.sin(i * math.pi / 6))
            context.stroke()
            context.restore()
        
