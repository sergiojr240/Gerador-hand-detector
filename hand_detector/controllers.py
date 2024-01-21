from hand_detector.media_pipe_hand_detector import MediaPipeHandDetector
from hand_detector.open_pose_hand_detector import OpenPoseHandDetector
from hand_detector.services import HandLandmarksService
from django.http import HttpResponse
from django.views import View

class HandLandmarksRestController(View):
    def get(self, request):
        # Recupera a estratégia
        detector_strategy = self.chooseDetectorStrategy(request)

        # Verifica se a estratégia foi escolhida corretamente
        if detector_strategy is not None:
            # Chama o serviço para processar a imagem
            service = HandLandmarksService()
            result = service.processImage(None, detector_strategy)
            # Retorna o resultado
            return HttpResponse(result)
        else:
            return HttpResponse("Estratégia de detecção de mãos inválida.", status=400)

    def chooseDetectorStrategy(self, request):
        # Implementa a lógica para escolher a estratégia (MediaPipe ou OpenPose)
        
        strategy_name = request.GET.get('strategy', None)

        if strategy_name == 'media_pipe':
            return MediaPipeHandDetector()
        elif strategy_name == 'open_pose':
            return OpenPoseHandDetector()
        else:
            return None

