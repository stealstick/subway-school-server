from django.db import models

class Station(models.Model):
    station_id = models.PositiveIntegerField(default=0, help_text="지하철역 번호 ")
    station_name = models.CharField(max_length=100, help_text="지하철역 이름")
    def __str__(self):
        return self.station_name


class StationWay(models.Model):
    UP=1
    DOWN=2
    STATION_WAY = (
        (UP, '상행'),
        (DOWN, '하행')
        )
    station = models.ForeignKey(Station, related_name="지하철역")
    station_way=models.PositiveIntegerField(choices=STATION_WAY, default= UP, blank=False)
    station_direction = models.CharField(max_length=100, help_text="목적지")
    station_time = models.PositiveIntegerField(default=0, help_text="오는시간")

    def __str__(self):
        return '%s - %s' % (self.station, self.station_way)