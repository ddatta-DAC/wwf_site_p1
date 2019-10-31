# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings


class ChinaExport(models.Model):
    panjivarecordid = models.BigIntegerField(db_column='PanjivaRecordID', primary_key=True)  # Field name made lowercase.
    shipmentmonth = models.DateField(db_column='ShipmentMonth', blank=True, null=True)  # Field name made lowercase.
    shippername = models.TextField(db_column='ShipperName', blank=True, null=True)  # Field name made lowercase.
    shipperpanjivaid = models.BigIntegerField(db_column='ShipperPanjivaID', blank=True, null=True)  # Field name made lowercase.
    shipperultimateparentname = models.TextField(db_column='ShipperUltimateParentName', blank=True, null=True)  # Field name made lowercase.
    shipmentdestination = models.CharField(db_column='ShipmentDestination', max_length=255, blank=True, null=True)  # Field name made lowercase.
    countryofsale = models.CharField(db_column='CountryOfSale', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transportmethod = models.TextField(db_column='TransportMethod', blank=True, null=True)  # Field name made lowercase.
    iscontainerized = models.CharField(db_column='IsContainerized', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valueofgoodsusd = models.BigIntegerField(db_column='ValueOfGoodsUSD', blank=True, null=True)  # Field name made lowercase.
    hscode = models.IntegerField(db_column='HSCode', blank=True, null=True)  # Field name made lowercase.
    hscodekeywords = models.TextField(db_column='HSCodeKeywords', blank=True, null=True)  # Field name made lowercase.
    adminregion = models.CharField(db_column='AdminRegion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tradetype = models.TextField(db_column='TradeType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'china_export'


class ChinaImport(models.Model):
    panjivarecordid = models.BigIntegerField(db_column='PanjivaRecordID', primary_key=True)  # Field name made lowercase.
    shipmentmonth = models.DateField(db_column='ShipmentMonth', blank=True, null=True)  # Field name made lowercase.
    consigneename = models.TextField(db_column='ConsigneeName', blank=True, null=True)  # Field name made lowercase.
    consigneecity = models.CharField(db_column='ConsigneeCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    consigneecountry = models.CharField(db_column='ConsigneeCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    consigneepanjivaid = models.BigIntegerField(db_column='ConsigneePanjivaID', blank=True, null=True)  # Field name made lowercase.
    shipmentorigin = models.CharField(db_column='ShipmentOrigin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=255, blank=True, null=True)  # Field name made lowercase.
    countryofsale = models.CharField(db_column='CountryOfSale', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transportmethod = models.TextField(db_column='TransportMethod', blank=True, null=True)  # Field name made lowercase.
    iscontainerized = models.CharField(db_column='IsContainerized', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valueofgoodsusd = models.BigIntegerField(db_column='ValueOfGoodsUSD', blank=True, null=True)  # Field name made lowercase.
    hscode = models.IntegerField(db_column='HSCode', blank=True, null=True)  # Field name made lowercase.
    hscodekeywords = models.TextField(db_column='HSCodeKeywords', blank=True, null=True)  # Field name made lowercase.
    adminregion = models.CharField(db_column='AdminRegion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tradetype = models.TextField(db_column='TradeType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'china_import'


class PeruExport(models.Model):
    panjivarecordid = models.BigIntegerField(db_column='PanjivaRecordID', primary_key=True)  # Field name made lowercase.
    shippername = models.TextField(db_column='ShipperName', blank=True, null=True)  # Field name made lowercase.
    shippercity = models.CharField(db_column='ShipperCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipperstateregion = models.CharField(db_column='ShipperStateRegion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shippercountry = models.CharField(db_column='ShipperCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipperultimateparentname = models.TextField(db_column='ShipperUltimateParentName', blank=True, null=True)  # Field name made lowercase.
    shipmentdestination = models.CharField(db_column='ShipmentDestination', max_length=255, blank=True, null=True)  # Field name made lowercase.
    portofunlading = models.TextField(db_column='PortOfUnlading', blank=True, null=True)  # Field name made lowercase.
    portofunladingcountry = models.CharField(db_column='PortOfUnladingCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transportmethod = models.TextField(db_column='TransportMethod', blank=True, null=True)  # Field name made lowercase.
    hscode = models.IntegerField(db_column='HSCode', blank=True, null=True)  # Field name made lowercase.
    goodsshipped = models.TextField(db_column='GoodsShipped', blank=True, null=True)  # Field name made lowercase.
    iscontainerized = models.CharField(db_column='IsContainerized', max_length=255, blank=True, null=True)  # Field name made lowercase.
    volumeteu = models.FloatField(db_column='VolumeTEU', blank=True, null=True)  # Field name made lowercase.
    itemquantity = models.FloatField(db_column='ItemQuantity', blank=True, null=True)  # Field name made lowercase.
    grossweightkg = models.FloatField(db_column='GrossWeightKg', blank=True, null=True)  # Field name made lowercase.
    netweightkg = models.FloatField(db_column='NetWeightKg', blank=True, null=True)  # Field name made lowercase.
    valueofgoodsfobusd = models.FloatField(db_column='ValueOfGoodsFOBUSD', blank=True, null=True)  # Field name made lowercase.
    exportquantity = models.FloatField(db_column='ExportQuantity', blank=True, null=True)  # Field name made lowercase.
    exportunit = models.CharField(db_column='ExportUnit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    receiptdeclarationdate = models.DateField(db_column='ReceiptDeclarationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peru_export'


class UsImport(models.Model):
    panjivarecordid = models.BigIntegerField(db_column='PanjivaRecordID', primary_key=True)  # Field name made lowercase.
    arrivaldate = models.DateField(db_column='ArrivalDate', blank=True, null=True)  # Field name made lowercase.
    consigneename = models.TextField(db_column='ConsigneeName', blank=True, null=True)  # Field name made lowercase.
    consigneecity = models.CharField(db_column='ConsigneeCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    consigneecountry = models.CharField(db_column='ConsigneeCountry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    consigneepanjivaid = models.BigIntegerField(db_column='ConsigneePanjivaID', blank=True, null=True)  # Field name made lowercase.
    consigneeultimateparentname = models.TextField(db_column='ConsigneeUltimateParentName', blank=True, null=True)  # Field name made lowercase.
    shipperpanjivaid = models.CharField(db_column='ShipperPanjivaID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    carrier = models.CharField(db_column='Carrier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipmentorigin = models.CharField(db_column='ShipmentOrigin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipmentdestination = models.CharField(db_column='ShipmentDestination', max_length=255, blank=True, null=True)  # Field name made lowercase.
    portofunlading = models.CharField(db_column='PortOfUnlading', max_length=255, blank=True, null=True)  # Field name made lowercase.
    portoflading = models.CharField(db_column='PortOfLading', max_length=255, blank=True, null=True)  # Field name made lowercase.
    placeofreceipt = models.CharField(db_column='PlaceOfReceipt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    volumeteu = models.FloatField(db_column='VolumeTEU', blank=True, null=True)  # Field name made lowercase.
    weightkg = models.FloatField(db_column='WeightKg', blank=True, null=True)  # Field name made lowercase.
    haslcl = models.CharField(db_column='HasLCL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    containernumbers = models.TextField(db_column='ContainerNumbers', blank=True, null=True)  # Field name made lowercase.
    hscode = models.IntegerField(db_column='HSCode', blank=True, null=True)  # Field name made lowercase.
    goodsshipped = models.TextField(db_column='GoodsShipped', blank=True, null=True)  # Field name made lowercase.
    dividedlcl = models.CharField(db_column='DividedLCL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'us_import'


class Comment(models.Model):
    panjivarecordid = models.BigIntegerField(primary_key=True)
    comment = models.TextField()

    class Meta:
        abstract = True


class ChinaExportComment(Comment):
    pass


class ChinaImportComment(Comment):
    pass


class PeruExportComment(Comment):
    pass


class UsImportComment(Comment):
    pass



THUMBS_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('clear', 'Clear'),
)


class Thumbs(models.Model):
    panjivarecordid = models.BigIntegerField(primary_key=True)
    thumbs = models.CharField(
        max_length=5,
        choices=THUMBS_CHOICES,
        default="clear")

    class Meta:
        abstract = True


class ChinaExportThumbs(Thumbs):
    pass


class ChinaImportThumbs(Thumbs):
    pass


class PeruExportThumbs(Thumbs):
    pass


class UsImportThumbs(Thumbs):
    pass



class Flags(models.Model):
    panjivarecordid = models.BigIntegerField(primary_key=True)
    leb = models.BooleanField(default=False)  # LEB
    cites = models.BooleanField(default=False)  # CITES
    high = models.BooleanField(default=False)  # WWF_HighRisk
    iucn = models.BooleanField(default=False)  # IUCN RedList
    lacey = models.BooleanField(default=False)  # Lacey Act
    text = models.BooleanField(default=False)  # Text_Keyword

    pretty_list = {
        "leb": "LEB",
        "cites": "CITES",
        "high": "WWF High Risk",
        "iucn": "IUCN Red List",
        "lacey": "Lacey Act",
        "text": "text",  # leave text for template to resolve
    }

    class Meta:
        verbose_name = "Flags"
        verbose_name_plural = "Flags"

    def to_pretty_list(self):
        for flag in ["cites", "iucn", "lacey", "leb", "text", "high"]:
            if getattr(self, flag):
                yield self.pretty_list[flag]

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(
            self.panjivarecordid,
            self.leb,
            self.cites,
            self.high,
            self.iucn,
            self.lacey,
            self.text
        )
    