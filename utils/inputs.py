import cv2
import glob
import os

class ImageInput():
    def __init__(self, imageFolderPath):
        self.nextFrame = True
        if os.path.isfile(imageFolderPath):
            self.imagesList = [imageFolderPath]
        else:
            self.imagesList = glob.glob(imageFolderPath + "/*.png")
            self.imagesList += glob.glob(imageFolderPath + "/*.jpg")
            if not self.imagesList:
                raise ValueError ("Não há imagens na pasta indicada.")
        
        self.currentFrame = cv2.imread(self.imagesList[0])
        self.generator = self.imageGenerator()
        self.newFrame = None
    def imageGenerator(self):
        while True:
            for imagePath in self.imagesList:
                self.newFrame = cv2.imread(imagePath)
                yield self.newFrame, imagePath
    def read(self):
        if self.nextFrame:
            self.newFrame = False
            self.currentFrame, self.currentPath = next(self.generator)
        return self.currentFrame
