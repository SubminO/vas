from django.db import models


class Route(models.Model):
    """Описывает маршрут как последовательность lonlat точек"""
    name = models.CharField(max_length=100, unique=True, verbose_name='Краткое название маршрута',
                            help_text="Наименование маршрута: 10/2, 9а, 15 и т.д ")
    description = models.TextField(max_length=500, verbose_name='Полное название маршрута',
                                   help_text="Краткое описание маршрута", blank=True)

    # date_created = models.DateTimeField(auto_now_add=True)
    # date_updated = models.DateTimeField(auto_now=True)

    model_type = 'route'
    model_description = 'Внесение маршрутов в систему'

    class Meta:
        db_table = "route"
        indexes = [models.Index(fields=["name"])]

    @property
    def platforms(self):
        return self.routeplatform_set.count()

    def __str__(self):
        return "%s" % self.name


class RoutePoint(models.Model):
    """Описывает маршрут как последовательность lonlat точек"""
    prev = models.ForeignKey("self", on_delete=models.CASCADE, related_name="prev_point",
                             null=True, help_text="предыдущая точка маршрута")
    next = models.ForeignKey("self", on_delete=models.CASCADE, related_name="next_point",
                             null=True, help_text="следующая точка маршрута")
    route = models.ForeignKey(Route, on_delete=models.CASCADE, help_text="ID маршрута")

    longitude = models.FloatField(null=True, verbose_name="Долгота", help_text="долгота")
    latitude = models.FloatField(null=True, help_text="широта")
    description = models.TextField(max_length=500, help_text="Краткое описание точки маршрута", blank=True)

    class Meta:
        db_table = "route_point"
        indexes = [models.Index(fields=["prev", "next", "route"])]

    def __str__(self):
        return "%d %s" % (self.id, self.route.name)


class PlatformType(models.Model):
    """Описывает типы остановок"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Тип остановки",
                            help_text="Название типа остановки")
    description = models.TextField(max_length=500, verbose_name="Описание", help_text="Краткое описани типа остановки",
                                   blank=True)

    model_type = 'route_platform_type'
    model_description = 'Внесение типа остановки'

    class Meta:
        db_table = "platform_type"
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return "%s" % self.name


class RoutePlatform(models.Model):
    """Описывает остановки, как lonlat точку"""
    prev = models.ForeignKey("self", related_name="prev_platform", on_delete=models.CASCADE,
                             null=True, help_text="предыдущая точка маршрута")
    next = models.ForeignKey("self", related_name="next_platform", on_delete=models.CASCADE,
                             null=True, help_text="следующая точка маршрута")

    name = models.CharField(max_length=100, unique=True, verbose_name="Краткое название остановки",
                            help_text="Название остановки")
    type = models.ForeignKey(PlatformType, on_delete=models.CASCADE, verbose_name="Тип остановки",
                             help_text="ID типа остановки")
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, help_text="ID маршрута остановки")
    longitude = models.FloatField(null=True, help_text="долгота")
    latitude = models.FloatField(null=True, help_text="широта")
    description = models.TextField(max_length=500, verbose_name="Развернутое название остановки",
                                   help_text="Краткон описание остановки", blank=True)

    model_type = 'route_platform'
    model_description = 'Внесение остановок в систему'

    class Meta:
        db_table = "route_platform"
        indexes = [
            models.Index(fields=["name", "type", "prev", "next", "route"])
        ]

    def __str__(self):
        return "%s (%s %s)" % (self.name, self.type.name if self.type else '', self.route.name if self.route else '')


class BusModel(models.Model):
    """Информация о транспортном средстве: UUID, Гос номер, Модель"""
    uuid = models.CharField(max_length=255, verbose_name='ID GPS/GLONASS', help_text='Номер датчика системы слежения',
                            unique=True)
    name = models.CharField(max_length=255, verbose_name='Название ТС',
                            help_text='Сокращенное название для внутренних целей и удобства')
    licenseplate = models.CharField(max_length=55, verbose_name='ГОС номер ТС')
    BUS_TYPE = (
        ("bus", "автобус"),
        ("minibus", "маршрутное такси"),
        ("trolleybus", "троллейбус"),
        ("tramway", "трамвай")
    )
    type = models.CharField(max_length=15, verbose_name='Тип',
                            help_text='Тип транспортного средства (Автобус, Троллейбус)', choices=BUS_TYPE, default=0)
    model = models.CharField(max_length=255, verbose_name='Модель ТС',
                             help_text='Наименование модели ТС (ПАЗ, ЛИАЗ и тд.', blank=True)
    techquality = models.IntegerField(verbose_name='Техническое состояние', choices=(
        (1, "не находу"), (2, "плохое"), (3, "удовлетворительное"), (4, "хорошее"), (5, "отличное")), default=4)

    model_type = 'ts'
    model_description = 'Внесение транспортных средств в систему'

    class Meta:
        db_table = "vehicles"
        indexes = [
            models.Index(fields=["uuid", "name"])
        ]

    def __str__(self):
        return "%s - %s" % (self.uuid, self.name)
