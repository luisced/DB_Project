from django.db import models

class AfectedUser(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nombre de Usuario")

class Device(models.Model):
    web_browser = models.CharField(max_length=255, verbose_name="Navegador Web", null=True, blank=True)
    operative_system = models.CharField(max_length=255, verbose_name="Sistema Operativo", null=True, blank=True)
    rest_information = models.CharField(max_length=255, verbose_name="Información Restante", null=True, blank=True)

    def __str__(self):
        return f"{self.web_browser} - {self.operative_system}"

class Geolocalization(models.Model):
    locality = models.CharField(max_length=255, verbose_name="Localidad", null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name="Ciudad", null=True, blank=True)

    def __str__(self):
        return f"{self.locality}, {self.city}"

class CyberAttack(models.Model):
    timestamp = models.DateTimeField(verbose_name="Marca de Tiempo")
    sourceIP = models.CharField(max_length=255, verbose_name="IP de Origen", null=True, blank=True)
    destinationIP = models.CharField(max_length=255, verbose_name="IP de Destino", null=True, blank=True)
    sourcePort = models.IntegerField(verbose_name="Puerto de Origen")
    destinationPort = models.IntegerField(verbose_name="Puerto de Destino")
    protocol = models.CharField(max_length=255, verbose_name="Protocolo", null=True, blank=True)
    packetLength = models.IntegerField(verbose_name="Longitud del Paquete")
    packetType = models.CharField(max_length=255, verbose_name="Tipo de Paquete", null=True, blank=True)
    trafficType = models.CharField(max_length=255, verbose_name="Tipo de Tráfico", null=True, blank=True)
    actionTaken = models.CharField(max_length=255, verbose_name="Acción Tomada", null=True, blank=True)
    severityLevel = models.CharField(max_length=255, verbose_name="Nivel de Severidad", null=True, blank=True)
    networkSegment = models.CharField(max_length=255, verbose_name="Segmento de Red", null=True, blank=True)
    alertsWarnings = models.BooleanField(verbose_name="Alertas/Advertencias", default=False, null=True)
    attackType = models.CharField(max_length=255, verbose_name="Tipo de Ataque", null=True, blank=True)
    idsIpsAlerts = models.BooleanField(verbose_name="Alertas IDS/IPS", default=False, null=True)
    user = models.ForeignKey(AfectedUser, on_delete=models.CASCADE, verbose_name="Usuario", null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name="Dispositivo", null=True, blank=True)
    geoLocation = models.ForeignKey(Geolocalization, on_delete=models.CASCADE, verbose_name="Geolocalización", null=True, blank=True)

    def __str__(self):
        return f"{self.sourceIP} -> {self.destinationIP} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

    '''Timestamp,Source IP Address,Destination IP Address,Source Port,Destination Port,Protocol,Packet Length,Packet Type,Traffic Type,Payload Data,Malware Indicators,Anomaly Scores,Alerts/Warnings,Attack Type,Attack Signature,Action Taken,Severity Level,User Information,Device Information,Network Segment,Geo-location Data,Proxy Information,Firewall Logs,IDS/IPS Alerts,Log Source
'''
    #unused fields
    #payloadData = models.TextField(verbose_name="Datos del Payload", null=True, blank=True)
    #malwareIndicators = models.TextField(verbose_name="Indicadores de Malware", null=True, blank=True)
    #anomalyScores = models.TextField(verbose_name="Puntuaciones de Anomalía", null=True, blank=True)
    #attackSignature = models.TextField(verbose_name="Firma de Ataque", null=True, blank=True)
    #proxyInformation = models.TextField(verbose_name="Información del Proxy", null=True, blank=True)
    #firewallLogs = models.TextField(verbose_name="Registros de Firewall", null=True, blank=True)
    #logSource = models.TextField(verbose_name="Fuente de Registro", null=True, blank=True)