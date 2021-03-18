from django.db import models
from django.urls import reverse


class Epoch(models.Model):
    name = models.CharField(max_length=126)
    path = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


# Stuff from hitl db below here

class Record(models.Model):
    PanjivaRecordID = models.BigIntegerField(db_column="PanjivaRecordID", primary_key=True)
    BillOfLadingNumber = models.TextField(db_column="BillOfLadingNumber", blank=True, null=True)
    ArrivalDate = models.TextField(db_column="ArrivalDate", blank=True, null=True)
    DataLoadDate = models.TextField(db_column="DataLoadDate", blank=True, null=True)
    DataLaunchDate = models.TextField(db_column="DataLaunchDate", blank=True, null=True)
    ConsigneePanjivaID = models.FloatField(db_column="ConsigneePanjivaID")
    ShipperPanjivaID = models.FloatField(db_column="ShipperPanjivaID")
    Carrier = models.TextField(db_column="Carrier", blank=True, null=True)
    NotifyParty = models.TextField(db_column="NotifyParty", blank=True, null=True)
    NotifyPartySCAC = models.TextField(db_column="NotifyPartySCAC", blank=True, null=True)
    BillOfLadingType = models.TextField(db_column="BillOfLadingType", blank=True, null=True)
    MasterBillOfLadingNumber = models.TextField(db_column="MasterBillOfLadingNumber", blank=True, null=True)
    ShipmentOrigin = models.TextField(db_column="ShipmentOrigin", blank=True, null=True)
    ShipmentDestination = models.TextField(db_column="ShipmentDestination", blank=True, null=True)
    PortOfUnlading = models.TextField(db_column="PortOfUnlading", blank=True, null=True)
    PortOfLading = models.TextField(db_column="PortOfLading", blank=True, null=True)
    PlaceOfReceipt = models.TextField(db_column="PlaceOfReceipt", blank=True, null=True)
    TransportMethod = models.TextField(db_column="TransportMethod", blank=True, null=True)
    Vessel = models.TextField(db_column="Vessel", blank=True, null=True)
    VesselVoyageID = models.TextField(db_column="VesselVoyageID", blank=True, null=True)
    VesselIMO = models.FloatField(db_column="VesselIMO")
    IsContainerized = models.TextField(db_column="IsContainerized", blank=True, null=True)
    VolumeTEU = models.FloatField(db_column="VolumeTEU")
    Quantity = models.TextField(db_column="Quantity", blank=True, null=True)
    Measurement = models.TextField(db_column="Measurement", blank=True, null=True)
    WeightKg = models.FloatField(db_column="WeightKg")
    WeightT = models.FloatField(db_column="WeightT")
    WeightOriginalFormat = models.TextField(db_column="WeightOriginalFormat", blank=True, null=True)
    ValueOfGoodsUSD = models.FloatField(db_column="ValueOfGoodsUSD")
    FROB = models.TextField(db_column="FROB", blank=True, null=True)
    ManifestNumber = models.BigIntegerField(db_column="ManifestNumber")
    InbondCode = models.TextField(db_column="InbondCode", blank=True, null=True)
    NumberOfContainers = models.BigIntegerField(db_column="NumberOfContainers")
    HasLCL = models.TextField(db_column="HasLCL", blank=True, null=True)
    ContainerNumbers = models.TextField(db_column="ContainerNumbers", blank=True, null=True)
    HSCode = models.TextField(db_column="HSCode", blank=True, null=True)
    GoodsShipped = models.TextField(db_column="GoodsShipped", blank=True, null=True)
    VolumeContainerTEU = models.TextField(db_column="VolumeContainerTEU", blank=True, null=True)
    ContainerMarks = models.TextField(db_column="ContainerMarks", blank=True, null=True)
    DividedLCL = models.TextField(db_column="DividedLCL", blank=True, null=True)
    ContainerTypeOfService = models.TextField(db_column="ContainerTypeOfService", blank=True, null=True)
    ContainerTypes = models.TextField(db_column="ContainerTypes", blank=True, null=True)
    DangerousGoods = models.TextField(db_column="DangerousGoods", blank=True, null=True)

    CSV_FIELDS = [
        "PanjivaRecordID",
        "Carrier",
        "PortOfLading",
        "ShipmentDestination",
        "ConsigneePanjivaID",
        "PortOfUnlading",
        "ShipmentOrigin",
        "HSCode",
        "ShipperPanjivaID",
    ]

    def to_csv(self):
        return [
            #self.PanjivaRecordID,
            '<a href="{}">{}</a>'.format(reverse("record_detail", args=[self.PanjivaRecordID]), self.PanjivaRecordID),
            self.Carrier,
            self.PortOfLading,
            self.ShipmentDestination,
            self.ConsigneePanjivaID,
            self.PortOfUnlading,
            self.ShipmentOrigin,
            self.HSCode,
            self.ShipperPanjivaID
        ]

    class Meta:
        managed = False
        db_table = 'Records'


class Shipper(models.Model):

    ShipperName = models.TextField(db_column="ShipperName", blank=True, null=True)
    ShipperFullAddress = models.TextField(db_column="ShipperFullAddress", blank=True, null=True)
    ShipperRoute = models.TextField(db_column="ShipperRoute", blank=True, null=True)
    ShipperCity = models.TextField(db_column="ShipperCity", blank=True, null=True)
    ShipperStateRegion = models.TextField(db_column="ShipperStateRegion", blank=True, null=True)
    ShipperPostalCode = models.TextField(db_column="ShipperPostalCode", blank=True, null=True)
    ShipperCountry = models.TextField(db_column="ShipperCountry", blank=True, null=True)
    ShipperURL = models.TextField(db_column="ShipperURL", blank=True, null=True)
    ShipperLocalDUNS = models.FloatField(db_column="ShipperLocalDUNS")
    ShipperPanjivaID = models.FloatField(db_column="ShipperPanjivaID", db_index=True)
    ShipperStockTickers = models.TextField(db_column="ShipperStockTickers", blank=True, null=True)
    ShipperCleanedStockTickers = models.TextField(db_column="ShipperCleanedStockTickers", blank=True, null=True)
    ShipperUltimateParentStockTickers = models.TextField(db_column="ShipperUltimateParentStockTickers", blank=True, null=True)
    ShipperUltimateParentCleanedStockTickers = models.TextField(db_column="ShipperUltimateParentCleanedStockTickers", blank=True, null=True)
    ShipperUltimateParentName = models.TextField(db_column="ShipperUltimateParentName", blank=True, null=True)
    ShipperOriginalFormat = models.TextField(db_column="ShipperOriginalFormat", blank=True, null=True)
    ID = models.BigIntegerField(db_column="ID")


    class Meta:
        managed = False
        db_table = 'ShipperPanjivaID'


class Consignee(models.Model):
    ConsigneeName = models.TextField(db_column="ConsigneeName", blank=True, null=True)
    ConsigneeFullAddress = models.TextField(db_column="ConsigneeFullAddress", blank=True, null=True)
    ConsigneeRoute = models.TextField(db_column="ConsigneeRoute", blank=True, null=True)
    ConsigneeCity = models.TextField(db_column="ConsigneeCity", blank=True, null=True)
    ConsigneeStateRegion = models.TextField(db_column="ConsigneeStateRegion", blank=True, null=True)
    ConsigneePostalCode = models.TextField(db_column="ConsigneePostalCode", blank=True, null=True)
    ConsigneeCountry = models.TextField(db_column="ConsigneeCountry", blank=True, null=True)
    ConsigneeURL = models.TextField(db_column="ConsigneeURL", blank=True, null=True)
    ConsigneeLocalDUNS = models.FloatField(db_column="ConsigneeLocalDUNS")
    ConsigneePanjivaID = models.FloatField(db_column="ConsigneePanjivaID", db_index=True)
    ConsigneeStockTickers = models.TextField(db_column="ConsigneeStockTickers", blank=True, null=True)
    ConsigneeCleanedStockTickers = models.TextField(db_column="ConsigneeCleanedStockTickers", blank=True, null=True)
    ConsigneeUltimateParentStockTickers = models.TextField(db_column="ConsigneeUltimateParentStockTickers", blank=True, null=True)
    ConsigneeUltimateParentCleanedStockTickers = models.TextField(db_column="ConsigneeUltimateParentCleanedStockTickers", blank=True, null=True)
    ConsigneeUltimateParentName = models.TextField(db_column="ConsigneeUltimateParentName", blank=True, null=True)
    ConsigneeOriginalFormat = models.TextField(db_column="ConsigneeOriginalFormat", blank=True, null=True)
    ID = models.BigIntegerField(db_column="ID")

    class Meta:
        managed = False
        db_table = 'ConsigneePanjivaID'

