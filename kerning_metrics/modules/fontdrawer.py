
import math

class FontArea:
    def __init__(self, da, font, letters):
        self.da = da
        self.font = font
        self.font.is_quadratic = False
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
            x += glyph.width

    def scale(self, rect, x, y):
        y = int(rect.height - (y / 10.)) - 100
        x = int(x / 10.)
        return (x, y)

    def drawfontcontour(self, offx, offy, contour):

        print "is_quadratic", contour.is_quadratic

        if contour.isClockwise():
            self.context.set_source_rgb(0, 0, 0)
        else:
            self.context.set_source_rgb(1, 1, 1)
        rect = self.da.get_allocation()
        x = rect.x #+ rect.width / 2
        y = rect.y #+ rect.height / 2
        offx += x
        offy += y
        on_curve = False
        bez = []
        prev = None

        p = contour[0]
        sx, sy = self.scale(rect, p.x + offx, p.y + offy)
        self.context.move_to(sx, sy)

        for p in contour + contour[0]:
            #print p.x, p.y, p.on_curve
            if not p.on_curve:
                bez.append(p)
                continue
            if bez:
                sx1, sy1 = self.scale(rect, bez[0].x+ offx, bez[0].y + offy)
                sx2, sy2 = self.scale(rect, bez[1].x+ offx, bez[1].y + offy)
                sx3, sy3 = self.scale(rect, p.x + offx, p.y + offy)
                self.context.curve_to(sx1, sy1, sx2, sy2, sx3, sy3)
                bez = []
            elif prev:
                sx, sy = self.scale(rect, p.x + offx, p.y + offy)
                self.context.line_to(sx, sy)
            prev = p

        #self.context.stroke_preserve()
        self.context.fill()

