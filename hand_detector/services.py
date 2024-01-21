from hand_detector.models import HandLandmarksRepository

class HandLandmarksService:
    def processImage(self, image, detector_strategy):
        # Processar a imagem usando a estratégia escolhida
        landmarks = detector_strategy.detectHandLandmarks(image)
        # Realizar operações adicionais se necessário
        pass
