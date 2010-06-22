
import math

class FontArea:
    def __init__(self, da, font, letters):
        self.da = da
        self.font = font
        self.letters = letters
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
        x = 0
        y = 0
        for l in self.letters:
            glyph = self.font[l]
            for lname in glyph.layers:
                print lname, glyph.layers[lname]
                for c in glyph.layers[lname]:
                    self.drawfontcontour(x, y, c)
            x, y = scale(rect, x + l.width, y)

    def scale(self, rect, x, y):
        y = int(rect.height - (y / 10.)) - 100
        x = int(x / 10.)
        return (x, y)

    def drawfontcontour(self, offx, offy, contour):
        self.context.set_source_rgb(0, 0, 0)
        rect = self.da.get_allocation()
        x = rect.x #+ rect.width / 2
        y = rect.y #+ rect.height / 2
        offx += x
        offy += y
        on_curve = False
        for p in contour + contour[0]:
            print p.x, p.y, p.on_curve
            if on_curve:
                sx, sy = self.scale(rect, p.x + offx, p.y + offy)
                self.context.line_to(sx, sy)
                self.context.stroke()
            sx, sy = self.scale(rect, p.x + offx, p.y + offy)
            self.context.move_to(sx, sy)
            #prev_x = p.x
            #prev_y = p.y
            on_curve = True # p.on_curve

