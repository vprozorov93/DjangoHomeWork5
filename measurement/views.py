# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializers, SensorDetailSerializer, MeasurementSerializer


class SensorView(APIView):
    def get(self, request):
        sensor = Sensor.objects.all()
        ser = SensorSerializers(sensor, many=True)
        return Response(ser.data)

    def post(self, request):
        if 'name' in request.query_params:
            sensor = Sensor()
            sensor.name = request.query_params['name']
            if 'description' in request.query_params:
                sensor.description = request.query_params['description']
            sensor.save()
            return Response({'detail': 'Sensor has been add to DB.'})
        else:
            return Response({'detail': 'Error. Invalid params.'})


class SensorsView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

    def patch(self, request, pk):
        if 'name' in request.query_params or 'description' in request.query_params:
            sensor = Sensor.objects.filter(pk=pk)
            if 'name' in request.query_params:
                sensor.update(name=request.query_params['name'])
            if 'description' in request.query_params:
                sensor.update(description=request.query_params['description'])
            return Response({'detail': 'Sensor has been update.'})
        else:
            return Response({'detail': 'Error. Invalid params.'})

    def get(self, request, pk):
        sensor = Sensor.objects.filter(id=pk)
        ser = SensorDetailSerializer(sensor, many=True)
        return Response(ser.data)


class MeasurementsView(RetrieveUpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        if 'temperature' in request.query_params and 'sensor_id' in request.query_params:
            print(request.query_params)
            sensor = Sensor.objects.filter(pk=request.query_params['sensor_id'])
            measurement = Measurement()
            measurement.sensor_id = sensor[0]
            measurement.temperature = request.query_params['temperature']
            measurement.save()
            return Response({'detail': 'Measurement has been add to DB.'})
        else:
            return Response({'detail': 'Error. Invalid params.'})