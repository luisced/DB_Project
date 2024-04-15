from django.db import models


class AfectedUser(models.Model):
    username = models.CharField(max_length=50)


class Device(models.Model):
    # device_information = models.CharField(max_length=100)
    '''
    device
    Column 1 = split before ()
    Column 2 = split with ; inside ()
    Column 3 = see after () if usable
    '''
    web_browser = models.CharField(max_length=50, verbose_name="Navegador Web")
    operative_system = models.CharField(max_length=50, verbose_name="Sistema Operativo")
    rest_information = models.CharField(max_length=255, verbose_name="Información Restante")
    def __str__(self):
        return self.device_information


class Geolocalization(models.Model):
    # location = models.CharField(max_length=255, verbose_name="Ubicación")
    '''
    location
    Column 1 = Country
    Column 2 = Region
    '''
    locality = models.CharField(max_length=50, verbose_name="Localidad")
    city = models.CharField(max_length=50, verbose_name="Ciudad")
    def __str__(self):
        return self.location


class CyberAttack(models.Model):

    timestamp = models.DateTimeField(verbose_name="Marca de Tiempo")
    sourceIP = models.CharField(max_length=100, verbose_name="IP de Origen")
    destinationIP = models.CharField(
        max_length=100, verbose_name="IP de Destino")
    sourcePort = models.IntegerField(verbose_name="Puerto de Origen")
    destinationPort = models.IntegerField(verbose_name="Puerto de Destino")
    protocol = models.CharField(max_length=50, verbose_name="Protocolo")
    packetLength = models.IntegerField(verbose_name="Longitud del Paquete") #Posible
    packetType = models.CharField(
        max_length=50, verbose_name="Tipo de Paquete") #important, encabezado de paquete
    trafficType = models.CharField(
        max_length=50, verbose_name="Tipo de Tráfico")
    actionTaken = models.CharField(
        max_length=50, verbose_name="Acción Tomada")
    severityLevel = models.CharField(
        max_length=50, verbose_name="Nivel de Severidad")
    networkSegment = models.CharField(
        max_length=50, verbose_name="Segmento de Red")
    # payloadData = models.TextField(
    #     verbose_name="Datos del Payload", null=True, blank=True)
    user = models.ForeignKey(
        AfectedUser, on_delete=models.CASCADE, verbose_name="Usuario")
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, verbose_name="Dispositivo")
    geoLocation = models.ForeignKey(
        Geolocalization, on_delete=models.CASCADE, verbose_name="Geolocalización")

    def __str__(self):
        return self.source_ip, self.destination_ip, self.timestamp, self.protocol, self.packet_type, self.traffic_type, self.action_taken, self.severity_level, self.network_segment, self.payload_data, self.user, self.device, self.geo_location
