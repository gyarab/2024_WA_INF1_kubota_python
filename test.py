import colorsys

def css_color_to_rgb(color):
    if (color[0] == '#'):
        # převedení hex na rgb
        color = color.lstrip('#')
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        return (r, g, b)
    elif (color[0] == "r"):
        # rgb do rgb
        color = color.strip('rgb()')
        r, g, b = map(int, color.split(','))
        return (r, g, b)
    elif (color[0] == "h"):
        # hsl nebo hsv do rgb
        color = color.strip('hsl()')
        h, s, l = map(int, color.split(','))
        r, g, b = colorsys.hls_to_rgb(h/360, l/100, s/100)
        return (int(r*255), int(g*255), int(b*255))
    elif (color[0] == "h"):
        color = color.strip('hsv()')
        h, s, v = map(int, color.split(','))
        r, g, b = colorsys.hsv_to_rgb(h/360, s/100, v/100)
        return (int(r*255), int(g*255), int(b*255))

print(css_color_to_rgb('#ff0000'))  # (255, 0, 0)
print(css_color_to_rgb('rgb(255, 0, 0)'))  # (255, 0, 0)
print(css_color_to_rgb('hsl(0, 100, 50)'))  # (255, 0, 0)
print(css_color_to_rgb('hsv(0, 100, 50)'))  # (255, 0, 0)