from abc import ABC, abstractmethod

class DataSource (ABC):
    @abstractmethod
    def writeData(self,data) :
        pass

    @abstractmethod
    def readData(self) :
        pass

class FileDataSource (DataSource ):

    def __init__(self, filename) :
        self.__filename = filename

    def writeData(self,data) :
        print ("Write \"",data,"\" to the file using FileDataSource")

    def readData(self):
        print ("read \"data\" from the file using FileDataSource")
        return "data"


class DataSourceDecorator (DataSource ):

    def __init__(self,source: DataSource)  :
        self.__wrappee  = source

    def writeData(self,data) :
        self.__wrappee.writeData(data)

    def readData(self):
        return self.__wrappee.readData()


class EncryptionDecorator (DataSourceDecorator ):

    def __init__(self,source: DataSource)  :
        super().__init__(source)

    def writeData(self,data) :
        print ("Encrypt passed data using EncryptionDecorator")
        super().writeData(data)

    def readData(self) :
        result = super().readData(data)
        print ("decrypt data using EncryptionDecorator")
        return result

class CompressionDecorator (DataSourceDecorator ):

    def __init__(self,source: DataSource)  :
        super().__init__(source)

    def writeData(self,data) :
        print ("Compress passed data using CompressionDecorator")
        super().writeData(data)

    def readData(self) :
        result = super().readData(data)
        print ("decompress data using CompressionDecorator")
        return result

class Application :
    def UsageExample():
        MeanOfsalaryRecords = "Salary is 123$"
        source =  FileDataSource("somefile.dat")
        source.writeData(MeanOfsalaryRecords)
       
        source = CompressionDecorator(source)
        source.writeData(MeanOfsalaryRecords)
      
        source = EncryptionDecorator(source)
       
        source.writeData(MeanOfsalaryRecords)
    

if __name__ == "__main__":
    Application.UsageExample()
