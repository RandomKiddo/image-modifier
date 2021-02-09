from PIL import Image, ImageFilter
import warnings

class Modifier:
    def __init__(self, inputpath: str):
        self.image = Image.open(inputpath)
        self.image = self.image.convert('RGB')
    def negative(self, outputpath: str = 'negative.jpg', show: bool = False):
        '''
        Creates a negative version of this instance's image
        Output goes to filename outputpath, defaults to negative.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        negative = self.image.copy()
        for i in range(self.image.width):
            for j in range(self.image.height):
                r, g, b = self.image.getpixel((i, j))
                negated = (255-r, 255-g, 255-b)
                negative.putpixel((i, j), negated)
        negative.save(outputpath)
        if show:
            negative.show()
        return Modifier(outputpath)
    invert = negative
    def blur(self, outputpath: str = 'blur.jpg', show: bool = False):
        '''
        Creates a blurred version of this instance's image
        Output goes to filename outputpath, defaults to blur.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        blur = self.image.copy()
        blur.filter(ImageFilter.BLUR)
        blur.save(outputpath)
        if show:
            blur.show()
        return Modifier(outputpath)
    def mirror_vertical(self, outputpath: str = 'mirrorvertical.jpg', show: bool = False):
        '''
        Creates a mirrored vertical version of this instance's image
        Output goes to filename outputpath, defaults to mirrorvertical.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        mirror = self.image.copy()
        pixels = []
        for i in range(self.image.width):
            pixelrow = []
            for j in range(self.image.height):
                r, g, b = self.image.getpixel((i, j))
                pixelrow.append((r, g, b))
            pixels.append(pixelrow)
        for pixelrow in pixels:
            mid = len(pixelrow) // 2
            left = 0; right = len(pixelrow) - 1
            for i in range(mid):
                copy = pixelrow[left]
                pixelrow[left] = pixelrow[right]
                pixelrow[right] = copy
                left += 1; right -= 1
        for i in range(mirror.width):
            for j in range(mirror.height):
                colors = pixels[i][j]
                mirror.putpixel((i, j), (colors[0], colors[1], colors[2]))
        mirror.save(outputpath)
        if show:
            mirror.show()
        return Modifier(outputpath)
    def mirror_horizontal(self, outputpath: str = 'mirrorhorizontal.jpg', show: bool = False):
        '''
        Creates a mirrored horizontal version of this instance's image
        Output goes to filename outputpath, defaults to mirrorhorizontal.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        mirror = self.image.copy()
        pixels = []
        for i in range(self.image.height):
            pixelrow = []
            for j in range(self.image.width):
                r, g, b = self.image.getpixel((j, i))
                pixelrow.append((r, g, b))
            pixels.append(pixelrow)
        for pixelrow in pixels:
            mid = len(pixelrow) // 2
            left = 0; right = len(pixelrow) - 1
            for i in range(mid):
                copy = pixelrow[left]
                pixelrow[left] = pixelrow[right]
                pixelrow[right] = copy
                left += 1; right -= 1
        for i in range(mirror.height):
            for j in range(mirror.width):
                colors = pixels[i][j]
                mirror.putpixel((j, i), (colors[0], colors[1], colors[2]))
        mirror.save(outputpath)
        if show:
            mirror.show()
        return Modifier(outputpath)
    def grayscale(self, outputpath: str = 'grayscale.jpg', show: bool = False):
        '''
        Creates a grayscale version of this instance's image
        Output goes to filename outputpath, defaults to grayscale.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        Alias to greyscale
        '''
        grayscale = self.image.copy()
        for i in range(self.image.width):
            for j in range(self.image.height):
                r, g, b = self.image.getpixel((i, j))
                gray = (r + g + b) // 3
                grayed = (gray, gray, gray)
                grayscale.putpixel((i, j), grayed)
        grayscale.save(outputpath)
        if show:
            grayscale.show()
        return Modifier(outputpath)
    greyscale = grayscale #alias for grayscale using grey spelling
    def sepia(self, outputpath: str = 'sepia.jpg', show: bool = False):
        '''
        Creates a sepia version of this instance's image
        Output goes to filename outputpath, defaults to sepia.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        sepia = self.image.copy()
        for i in range(self.image.width):
            for j in range(self.image.height):
                r, g, b = self.image.getpixel((i, j))
                rn = (r*.393) + (g*.769) + (b*.189)
                gn = (r*.349) + (g*.686) + (b*.168)
                bn = (r*.272) + (g*.534) + (b*.131)
                rn = 255 if rn > 255 else int(rn)
                gn = 255 if gn > 255 else int(gn)
                bn = 255 if bn > 255 else int(bn)
                sepia.putpixel((i, j), (rn, gn, bn))
        sepia.save(outputpath)
        if show:
            sepia.show()
        return Modifier(outputpath)
    def sharpen(self, outputpath: str = 'sharpen.jpg', show: bool = False):
        '''
        Creates a sharpened version of this instance's image
        Output goes to filename outputpath, defaults to sharpen.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        sharpen = self.image.copy()
        sharpen.filter(ImageFilter.SHARPEN)
        sharpen.save(outputpath)
        if show:
            sharpen.show()
        return Modifier(outputpath)
    def average(self, outputpath: str = 'average.jpg', show: bool = False):
        '''
        Creates a new image of one color, being the average of all colors, of this instance's image
        Output goes to filename outputpath, defaults to average.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        average = self.image.copy()
        rtotal = 0; gtotal = 0; btotal = 0; pixels = 0
        for i in range(average.width):
            for j in range(average.height):
                r, g, b = average.getpixel((i, j))
                rtotal += r; gtotal += g; btotal += b; pixels += 1
        ravg = rtotal//pixels; gavg = gtotal//pixels; bavg = btotal//pixels
        for i in range(average.width):
            for j in range(average.height):
                average.putpixel((i, j), (ravg, gavg, bavg))
        average.save(outputpath)
        del rtotal, gtotal, btotal, pixels, ravg, gavg, bavg #clear memory
        if show:
            average.show()
        return Modifier(outputpath)
    def halftone(self, outputpath: str = 'halftone.jpg', show: bool = False):
        '''
        Creates a halftone version of this instance's image
        Output goes to filename outputpath, defaults to halftone.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        halftone = self.image.copy()
        for i in range(0, halftone.width, 2):
            if i >= halftone.width or i+1 >= halftone.width:
                break
            for j in range(0, halftone.height, 2):
                if j >= halftone.width or j+1 >= halftone.width:
                    break
                r1, g1, b1 = halftone.getpixel((i, j))
                r2, g2, b2 = halftone.getpixel((i, j+1))
                r3, g3, b3 = halftone.getpixel((i+1, j))
                r4, g4, b4 = halftone.getpixel((i+1, j+1))
                gray1 = (r1*0.299) + (g1*0.587) + (b1*0.114)
                gray2 = (r2*0.299) + (g2*0.587) + (b2*0.114)
                gray3 = (r3*0.299) + (g3*0.587) + (b3*0.114)
                gray4 = (r4*0.299) + (g4*0.587) + (b4*0.114)
                del r1, r2, r3, r4, g1, g2, g3, g4, b1, b2, b3, b4 #clear memory
                saturation = (gray1 + gray2 + gray3 + gray4) / 4
                Modifier.__put_pixel(halftone, i, j, saturation) # necessary method due to cognitive complexity
        halftone.save(outputpath)
        if show:
            halftone.show()
        return Modifier(outputpath)
    def __put_pixel(halftone: Image, i: int, j: int, saturation: float) -> None:
        WHITE = (255, 255, 255); BLACK = (0, 0, 0)
        if saturation > 223:
            halftone.putpixel((i, j), WHITE)
            halftone.putpixel((i, j+1), WHITE)
            halftone.putpixel((i+1, j), WHITE)
            halftone.putpixel((i+1, j+1), WHITE)
        elif saturation > 159:
            halftone.putpixel((i, j), WHITE)
            halftone.putpixel((i, j+1), BLACK)
            halftone.putpixel((i+1, j), WHITE)
            halftone.putpixel((i+1, j+1), WHITE)
        elif saturation > 95:
            halftone.putpixel((i, j), WHITE)
            halftone.putpixel((i, j+1), BLACK)
            halftone.putpixel((i+1, j), BLACK)
            halftone.putpixel((i+1, j+1), WHITE)
        elif saturation > 32:
            halftone.putpixel((i, j), BLACK)
            halftone.putpixel((i, j+1), WHITE)
            halftone.putpixel((i+1, j), BLACK)
            halftone.putpixel((i+1, j+1), BLACK)
        else:
            halftone.putpixel((i, j), BLACK)
            halftone.putpixel((i, j+1), BLACK)
            halftone.putpixel((i+1, j), BLACK)
            halftone.putpixel((i+1, j+1), BLACK)
    def primary(self, outputpath: str = 'primary.jpg', show: bool = False):
        '''
        Creates a primary version of this instance's image
        Output goes to filename outputpath, defaults to primary.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        primary = self.image.copy()
        for i in range(primary.width):
            for j in range(primary.height):
                r, g, b = primary.getpixel((i, j))
                r = 255 if r > 127 else 0
                g = 255 if g > 127 else 0
                b = 255 if b > 127 else 0
                primary.putpixel((i, j), (r, g, b))
        primary.save(outputpath)
        if show:
            primary.show()
        return Modifier(outputpath)
    def dither(self, outputpath: str = 'dither.jpg', show: bool = False):
        '''
        Creates a dither version of this instance's image
        Output goes to filename outputpath, defaults to dither.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        dither = self.image.copy()
        for i in range(0, dither.width, 2):
            if i >= dither.width or i+1 >= dither.width:
                break
            for j in range(0, dither.height, 2):
                if j >= dither.width or j+1 >= dither.width:
                    break
                r1, g1, b1 = dither.getpixel((i, j))
                r2, g2, b2 = dither.getpixel((i, j+1))
                r3, g3, b3 = dither.getpixel((i+1, j))
                r4, g4, b4 = dither.getpixel((i+1, j+1))
                red = (r1 + r2 + r3 + r4) / 4
                green = (g1 + g2 + g3 + g4) / 4
                blue = (b1 + b2 + b3 + b4) / 4
                r = [0, 0, 0, 0]; g = [0, 0, 0, 0]; b = [0, 0, 0, 0]
                for x in range(0, 4):
                    r[x] = Modifier.__dither_saturation(red, x) # necessary method due to cognitive complexity
                    g[x] = Modifier.__dither_saturation(green, x)
                    b[x] = Modifier.__dither_saturation(blue, x)
                dither.putpixel((i, j), (r[0], g[0], b[0]))
                dither.putpixel((i, j+1), (r[1], g[1], b[1]))
                dither.putpixel((i+1, j), (r[2], g[2], b[2]))
                dither.putpixel((i+1, j+1), (r[3], g[3], b[3]))
                del r1, r2, r3, r4, g1, g2, g3, g4, b1, b2, b3, b4, red, green, blue, r, g, b # clear memory
        dither.save(outputpath)
        if show:
            dither.show()
        return Modifier(outputpath)
    def __dither_saturation(color: float, index: int) -> int:
        if color > 223:
            return 255
        elif color > 159:
            if index != 1:
                return 255
            return 0
        elif color > 95:
            if index == 0 or index == 3:
                return 255
            return 0
        elif color > 32:
            if index == 1:
                return 255
            return 0
        else:
            return 0
    def tint(self, outputpath: str = 'tint.jpg', show: bool = False):
        '''
        Creates a tinted version of this instance's image
        Output goes to filename outputpath, defaults to tint.jpg
        Bool can be passed in if image should be shown upon finishing
        Returns a modifier of the output image
        '''
        tint = self.image.copy()
        for i in range(tint.width):
            for j in range(tint.height):
                r, g, b = tint.getpixel((i, j))
                r = r + (.25 * (255-r))
                g = g + (.25 * (255-g))
                b = b + (.25 * (255-b))
                tint.putpixel((i, j), (int(r), int(g), int(b)))
        tint.save(outputpath)
        if show:
            tint.show()
        return Modifier(outputpath)
    def recolor(self, outputpath: str = 'recolor.jpg', show: bool = False, dr: int = 100, dg: int = 100, db: int = 100):
        '''
        Creates a recolored version of this instance's image
        Output goes to filename outputpath, defaults to recolor.jpg
        Bool can be passed in if image should be shown upon finishing
        R, G, and B values can be passed in for recolor, all default to 100
        Returns a modifier of the output image
        '''
        recolor = self.image.copy()
        for i in range(recolor.width):
            for j in range(recolor.height):
                r, g, b = recolor.getpixel((i, j))
                r += dr; g += dg; b += db
                r, g, b = Modifier.__adjust_colors(r, g, b) # Method needed due to cognitive complexity
                recolor.putpixel((i, j), (r, g, b))
        recolor.save(outputpath)
        if show:
            recolor.show()
        return Modifier(outputpath)
    def __adjust_colors(r: int, g: int, b: int):
        r = 255 if r > 255 else r
        r = 0 if r < 0 else r
        g = 255 if g > 255 else g 
        g = 0 if g < 0 else g
        b = 255 if b > 255 else b
        b = 0 if b < 0 else b
        return r, g, b
    def mirror_diagonal(self, outputpath: str = 'mirrordiagonal.jpg', show: bool = False):
        mirror = self.image.copy()
        rise = mirror.height; run = mirror.width
    def rotate(self, outputpath: str = 'rotate.jpg', show: bool = False, degree: int = 90):
        '''
        Creates a rotated version of this instance's image
        Output goes to filename outputpath, defaults to rotate.jpg
        Bool can be passed in if image should be shown upon finishing
        Degree value can be passed in for rotation degree from 0˚ on the x-axis, defaults to 90˚
        Returns a modifier of the output image
        '''
        rotate = self.image.copy()
        rotate = rotate.rotate(degree)
        rotate.save(outputpath)
        if show:
            rotate.show()
        return Modifier(outputpath)

