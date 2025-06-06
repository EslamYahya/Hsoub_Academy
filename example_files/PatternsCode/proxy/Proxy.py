from abc import ABC, abstractmethod

class ThirdPartyYouTubeLib (ABC):
    @abstractmethod
    def listVideos(self) :
        pass

    @abstractmethod
    def getVideoInfo(self, id) :
        pass

    @abstractmethod
    def downloadVideo(self, id) :
        pass

class ThirdPartyYouTubeClass (ThirdPartyYouTubeLib ):
    def listVideos(self):
        print("Send API request to YouTube for list of video thumbnails")
        return "videos listed"

    def getVideoInfo(self, id):
        print("Get data about video which id is: ", id)
        return id

    def downloadVideo(self, id):
        print("Download a video file from YouTube with id", id)
        return id

class CachedYouTubeClass (ThirdPartyYouTubeLib ):

    def __init__(self, service: ThirdPartyYouTubeClass ) :
        self.__service = service
        self.__listCache = None
        self.__videoCache = None

    def listVideos(self) :
        if self.__listCache == None :
            self.__listCache = self.__service.listVideos()
        return self.__listCache

    def getVideoInfo(self, id) :
        if self.__videoCache == None :
            self.__videoCache = self.__service.getVideoInfo(id)
        return self.__videoCache

    def downloadVideo(self, id) :
        # this method doesn't defined
        if ( not self.downloadExists(id) ):
            self.__service.downloadVideo(id)

    def downloadExists(self, id) :
        print("Downloading ...")
        return True

class YouTubeManager :

    def __init__(self, service: ThirdPartyYouTubeLib) :
        self._service = service


    def renderVideoPage(self, id) :
        info = self._service.getVideoInfo(id)
        #  Render the video page.

    def renderListPanel(self) :
        list = self._service.listVideos()
        #  Render the list of video thumbnails.

    def reactOnUserInput(self) :
        self.renderVideoPage(1)
        self.renderListPanel()

class Application :
    def init() :
        aYouTubeService =  ThirdPartyYouTubeClass()
        aYouTubeProxy =  CachedYouTubeClass(aYouTubeService)
        manager =  YouTubeManager(aYouTubeProxy)
        manager.reactOnUserInput()

if __name__ == "__main__":
    Application.init()
