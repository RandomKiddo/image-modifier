from PIL import Image, ImageFilter
from random import randint

class Modifier:
    def __init__(self, inputpath: str):
        if not Modifier.is_compatible(inputpath):
            raise IllegalExtensionError('No .jpg image extension found in filename')
        self.image = Image.open(inputpath)
    def is_compatible(filename: str) -> bool:
        return '.jpg' in filename
    def to_jpeg(inputpath: str, outputpath: str = None) -> None:
        if outputpath is None:
            outputpath = inputpath
        if '.png' not in inputpath:
            raise IllegalExtensionError('Missing .png extension required for .jpg conversion')
        image = Image.open(inputpath)
        jpeg = image.copy()
        if '.jpg' not in outputpath:
            outputpath += '.jpg'
        jpeg.save(outputpath)
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

class IllegalExtensionError(Exception):
    def __init__(self, errmessage = 'No Extension Found On Filename'):
        self.errmessage = errmessage
    def __str__(self):
        return self.errmessage