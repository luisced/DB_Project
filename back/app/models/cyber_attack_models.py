from django.db import models


class AfectedUser(models.Model):
    username = models.CharField(max_length=50)


class Device(models.Model):
    device_information = models.CharField(max_length=100)

    def __str__(self):
        return self.device_information


class Geolocalization(models.Model):
    location = models.CharField(max_length=255, verbose_name="Ubicación")

    def __str__(self):
        return self.location


class CyberAttack(models.Model):

    timestamp = models.DateTimeField(verbose_name="Marca de Tiempo")
    source_ip = models.CharField(max_length=100, verbose_name="IP de Origen")
    destination_ip = models.CharField(
        max_length=100, verbose_name="IP de Destino")
    source_port = models.IntegerField(verbose_name="Puerto de Origen")
    destination_port = models.IntegerField(verbose_name="Puerto de Destino")
    protocol = models.CharField(max_length=50, verbose_name="Protocolo")
    packet_length = models.IntegerField(verbose_name="Longitud del Paquete")
    packet_type = models.CharField(
        max_length=50, verbose_name="Tipo de Paquete")
    traffic_type = models.CharField(
        max_length=50, verbose_name="Tipo de Tráfico")
    action_taken = models.CharField(
        max_length=50, verbose_name="Acción Tomada")
    severity_level = models.CharField(
        max_length=50, verbose_name="Nivel de Severidad")
    network_segment = models.CharField(
        max_length=50, verbose_name="Segmento de Red")
    payload_data = models.TextField(
        verbose_name="Datos del Payload", null=True, blank=True)
    user = models.ForeignKey(
        AfectedUser, on_delete=models.CASCADE, verbose_name="Usuario")
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, verbose_name="Dispositivo")
    geo_location = models.ForeignKey(
        Geolocalization, on_delete=models.CASCADE, verbose_name="Geolocalización")

    def __str__(self):
        return self.source_ip, self.destination_ip, self.timestamp, self.protocol, self.packet_type, self.traffic_type, self.action_taken, self.severity_level, self.network_segment, self.payload_data, self.user, self.device, self.geo_location
