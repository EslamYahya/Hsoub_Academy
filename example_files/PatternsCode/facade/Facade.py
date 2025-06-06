class VideoFile:
    def __init__(self, filename) :
        self.filename = filename

    def save(self):
        print ("saving ....")

class OggCompressionCodec:
    # some code here
    pass

class MPEG4CompressionCodec:
    # some code here
    pass

class CodecFactory:
    def extract(file) :
        print("extracting ...")
        return file ," with Codec"

class BitrateReader:
    def read(filename,src) :
        print("reading ... ", filename)
        return filename

    def convertBR(buffer,dest) :
        print ("convert ... ",buffer)

class AudioMixer:
    def fix(self,file) :
        print( "Fixing ...")
        return "Fixed File Name=",file

class VideoConverter :
    def convert(self,filename,format):
        file = VideoFile(filename)
        sourceCodec = CodecFactory.extract(file)
        if format == "mp4":
            destinationCodec = MPEG4CompressionCodec()
        else:
            destinationCodec = OggCompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convertBR(buffer, destinationCodec)
        result = (AudioMixer()).fix(result)
        return  VideoFile(result)

class Application :
    def main() :
        convertor = VideoConverter()
        mp4 = convertor.convert("Meaningful-video.ogg", "mp4")
        mp4.save()

if __name__ == "__main__":
    x  = Application.main()

