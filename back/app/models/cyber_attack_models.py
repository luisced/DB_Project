from django.db import models


class AfectedUser(models.Model):
    username = models.CharField( null=True, blank=True, verbose_name="Nombre de Usuario")


class Device(models.Model):
    # device_information = models.CharField(max_length=100)
    '''
    device
    Column 1 = split before ()
    Column 2 = split with ; inside ()
    Column 3 = see after () if usable
    '''
    web_browser = models.CharField( verbose_name="Navegador Web", null=True, blank=True)
    operative_system = models.CharField( verbose_name="Sistema Operativo", null=True, blank=True)
    rest_information = models.CharField( verbose_name="Información Restante", null=True, blank=True)
    def __str__(self):
        return self.device_information


class Geolocalization(models.Model):
    # location = models.CharField( verbose_name="Ubicación")
    '''
    location
    Column 1 = Country
    Column 2 = Region
    '''
    locality = models.CharField( verbose_name="Localidad", null=True, blank=True)
    city = models.CharField( verbose_name="Ciudad", null=True, blank=True)
    def __str__(self):
        return self.location


class CyberAttack(models.Model):

    timestamp = models.DateTimeField(verbose_name="Marca de Tiempo")
    sourceIP = models.CharField( verbose_name="IP de Origen", null=True, blank=True)
    destinationIP = models.CharField(
         verbose_name="IP de Destino", null=True, blank=True)
    sourcePort = models.IntegerField(verbose_name="Puerto de Origen")
    destinationPort = models.IntegerField(verbose_name="Puerto de Destino")
    protocol = models.CharField( verbose_name="Protocolo", null=True, blank=True)
    packetLength = models.IntegerField(verbose_name="Longitud del Paquete") #Posible
    packetType = models.CharField(
         verbose_name="Tipo de Paquete", null=True, blank=True) #important, encabezado de paquete
    trafficType = models.CharField(
         verbose_name="Tipo de Tráfico", null=True, blank=True)
    actionTaken = models.CharField(
         verbose_name="Acción Tomada", null=True, blank=True)
    severityLevel = models.CharField(
         verbose_name="Nivel de Severidad", null=True, blank=True)
    networkSegment = models.CharField(
         verbose_name="Segmento de Red", null=True, blank=True)
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
