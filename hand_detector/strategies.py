from abc import ABC, abstractmethod

class HandLandmarksDetectorStrategy(ABC):
    @abstractmethod
    def detectHandLandmarks(self, image):
        pass
