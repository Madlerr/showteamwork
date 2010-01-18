#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Random generated Color Pallete with
 contrast colors.
"""
import math
import random

class RandomColor:
    """
      Pseudorandom generated color
    """
    __rgb = [0, 0, 0]
    __brightness = None

    def __init__(self, r=None, g=None, b=None):
        """
          Construct RGB-color or [pseudo]random generate it.
        """
        if not r:
            r = random.randint(1, 255)
        if not g:
            g = random.randint(1, 255)
        if not b:
            b = random.randint(1, 255)
        self.__rgb = (r, g, b)

    def __getitem__(self, key):
        """
         Get r/g/b component
        """
        return self.__rgb[key]
    
    def __setitem__(self, key, value):
        """
         Set r/g/b component. Reset brightness.
        """
        self.__rgb[key] = value
        self.__brightness = None

    def get_brightness(self):
        """
         Get brightness, calculate it if needed.
        """
        if self.__brightness:
            return self.__brightness
        else:
            self.__brightness = ((self.__rgb[0] * 299) +
                         (self.__rgb[1] * 587) +
                         (self.__rgb[2] * 114)) / 1000
            return self.__brightness
        
    def __sub__(self, other):
        """
         Return norm_1 of difference
        """
        return ((max(self[0], other[0]) - min(self[0], other[0])) +
                (max(self[1], other[1]) - min(self[1], other[1])) +
                (max(self[2], other[2]) - min(self[2], other[2])))

    def __str__(self):
        """
          String representation.
        """
        return "%d,%d,%d" % (self[0], self[1], self[2])

    def __repr__(self):
        return "<%03d,%03d,%03d:%03d>" % \
            (self[0], self[1], self[2], self.get_brightness())
        
    def __cmp__(self, other):
        """
          compare colors as tuples:
        """
        return cmp( (self.get_brightness(),  self.__rgb),
                    (other.get_brightness(), other.__rgb))
        

class RandomColorPalette:
    """
      Random generated color palette.
    """
    def __init__(self, num, contrast_colors_num):
        """
        Very dump random algorithm to find
        random color pallete of given size (@num),
        where each color distinguished
        from at least given number of colors
         (@contrast_colors_num)
        """
        colors = []
        
        try_limit = 1000000 
        countdown = try_limit
        colors.append(RandomColor())
        contrast_colors_num = min(contrast_colors_num, num)
        contrast_colors_limit = contrast_colors_num 
        while len(colors)<num:
            # Some crazy math (pseudoscience heuristics)
            # Minimal brightness/color difference depends on color density
            color_gap = int(255 * math.pi * contrast_colors_limit /
                             2 / contrast_colors_num**(1.0/3+1))
            brightness_gap = ((255*math.e/2*contrast_colors_limit) /
                              (contrast_colors_num**2))
            random_color = RandomColor()
            if random_color.get_brightness()>30:
                distinguished_colors = 0
                for c in colors:
                    b_diff = abs(c.get_brightness() - random_color.get_brightness())
                    c_diff = c - random_color
                    if  c_diff >= color_gap and b_diff >= brightness_gap:
                        distinguished_colors += 1
                        if distinguished_colors > contrast_colors_limit:
                            break
                if distinguished_colors >= min(len(colors), contrast_colors_limit) \
                   or countdown<0:
                    colors.append(random_color)
                    print "Color #", len(colors), random_color,
                    print distinguished_colors, countdown
            countdown -= 1
            #Adaptivity
            contrast_colors_limit = max( 0,
                        math.ceil(contrast_colors_limit*countdown/try_limit)) 
        
        colors.sort()
        colors.reverse()
        self.colors = colors

if __name__ == '__main__':
    import time
    STIME = time.time()
    for n in xrange(6, 16):
        print "\n\n!!!!!!===>", n
        rcp = RandomColorPalette(num = n, contrast_colors_num = n)
    print "It takes ", time.time()-STIME, " seconds" 

