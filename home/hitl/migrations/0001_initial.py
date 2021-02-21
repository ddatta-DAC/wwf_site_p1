# Generated by Django 2.2.10 on 2021-02-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consignee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ConsigneeName', models.TextField(blank=True, db_column='ConsigneeName', null=True)),
                ('ConsigneeFullAddress', models.TextField(blank=True, db_column='ConsigneeFullAddress', null=True)),
                ('ConsigneeRoute', models.TextField(blank=True, db_column='ConsigneeRoute', null=True)),
                ('ConsigneeCity', models.TextField(blank=True, db_column='ConsigneeCity', null=True)),
                ('ConsigneeStateRegion', models.TextField(blank=True, db_column='ConsigneeStateRegion', null=True)),
                ('ConsigneePostalCode', models.TextField(blank=True, db_column='ConsigneePostalCode', null=True)),
                ('ConsigneeCountry', models.TextField(blank=True, db_column='ConsigneeCountry', null=True)),
                ('ConsigneeURL', models.TextField(blank=True, db_column='ConsigneeURL', null=True)),
                ('ConsigneeLocalDUNS', models.FloatField(db_column='ConsigneeLocalDUNS')),
                ('ConsigneePanjivaID', models.FloatField(db_column='ConsigneePanjivaID')),
                ('ConsigneeStockTickers', models.TextField(blank=True, db_column='ConsigneeStockTickers', null=True)),
                ('ConsigneeCleanedStockTickers', models.TextField(blank=True, db_column='ConsigneeCleanedStockTickers', null=True)),
                ('ConsigneeUltimateParentStockTickers', models.TextField(blank=True, db_column='ConsigneeUltimateParentStockTickers', null=True)),
                ('ConsigneeUltimateParentCleanedStockTickers', models.TextField(blank=True, db_column='ConsigneeUltimateParentCleanedStockTickers', null=True)),
                ('ConsigneeUltimateParentName', models.TextField(blank=True, db_column='ConsigneeUltimateParentName', null=True)),
                ('ConsigneeOriginalFormat', models.TextField(blank=True, db_column='ConsigneeOriginalFormat', null=True)),
                ('ID', models.BigIntegerField(db_column='ID')),
            ],
            options={
                'db_table': 'ConsigneePanjivaID',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('PanjivaRecordID', models.BigIntegerField(db_column='PanjivaRecordID', primary_key=True, serialize=False)),
                ('BillOfLadingNumber', models.TextField(blank=True, db_column='BillOfLadingNumber', null=True)),
                ('ArrivalDate', models.TextField(blank=True, db_column='ArrivalDate', null=True)),
                ('DataLoadDate', models.TextField(blank=True, db_column='DataLoadDate', null=True)),
                ('DataLaunchDate', models.TextField(blank=True, db_column='DataLaunchDate', null=True)),
                ('ConsigneePanjivaID', models.FloatField(db_column='ConsigneePanjivaID')),
                ('ShipperPanjivaID', models.FloatField(db_column='ShipperPanjivaID')),
                ('Carrier', models.TextField(blank=True, db_column='Carrier', null=True)),
                ('NotifyParty', models.TextField(blank=True, db_column='NotifyParty', null=True)),
                ('NotifyPartySCAC', models.TextField(blank=True, db_column='NotifyPartySCAC', null=True)),
                ('BillOfLadingType', models.TextField(blank=True, db_column='BillOfLadingType', null=True)),
                ('MasterBillOfLadingNumber', models.TextField(blank=True, db_column='MasterBillOfLadingNumber', null=True)),
                ('ShipmentOrigin', models.TextField(blank=True, db_column='ShipmentOrigin', null=True)),
                ('ShipmentDestination', models.TextField(blank=True, db_column='ShipmentDestination', null=True)),
                ('PortOfUnlading', models.TextField(blank=True, db_column='PortOfUnlading', null=True)),
                ('PortOfLading', models.TextField(blank=True, db_column='PortOfLading', null=True)),
                ('PlaceOfReceipt', models.TextField(blank=True, db_column='PlaceOfReceipt', null=True)),
                ('TransportMethod', models.TextField(blank=True, db_column='TransportMethod', null=True)),
                ('Vessel', models.TextField(blank=True, db_column='Vessel', null=True)),
                ('VesselVoyageID', models.TextField(blank=True, db_column='VesselVoyageID', null=True)),
                ('VesselIMO', models.FloatField(db_column='VesselIMO')),
                ('IsContainerized', models.TextField(blank=True, db_column='IsContainerized', null=True)),
                ('VolumeTEU', models.FloatField(db_column='VolumeTEU')),
                ('Quantity', models.TextField(blank=True, db_column='Quantity', null=True)),
                ('Measurement', models.TextField(blank=True, db_column='Measurement', null=True)),
                ('WeightKg', models.FloatField(db_column='WeightKg')),
                ('WeightT', models.FloatField(db_column='WeightT')),
                ('WeightOriginalFormat', models.TextField(blank=True, db_column='WeightOriginalFormat', null=True)),
                ('ValueOfGoodsUSD', models.FloatField(db_column='ValueOfGoodsUSD')),
                ('FROB', models.TextField(blank=True, db_column='FROB', null=True)),
                ('ManifestNumber', models.BigIntegerField(db_column='ManifestNumber')),
                ('InbondCode', models.TextField(blank=True, db_column='InbondCode', null=True)),
                ('NumberOfContainers', models.BigIntegerField(db_column='NumberOfContainers')),
                ('HasLCL', models.TextField(blank=True, db_column='HasLCL', null=True)),
                ('ContainerNumbers', models.TextField(blank=True, db_column='ContainerNumbers', null=True)),
                ('HSCode', models.TextField(blank=True, db_column='HSCode', null=True)),
                ('GoodsShipped', models.TextField(blank=True, db_column='GoodsShipped', null=True)),
                ('VolumeContainerTEU', models.TextField(blank=True, db_column='VolumeContainerTEU', null=True)),
                ('ContainerMarks', models.TextField(blank=True, db_column='ContainerMarks', null=True)),
                ('DividedLCL', models.TextField(blank=True, db_column='DividedLCL', null=True)),
                ('ContainerTypeOfService', models.TextField(blank=True, db_column='ContainerTypeOfService', null=True)),
                ('ContainerTypes', models.TextField(blank=True, db_column='ContainerTypes', null=True)),
                ('DangerousGoods', models.TextField(blank=True, db_column='DangerousGoods', null=True)),
            ],
            options={
                'db_table': 'Records',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShipperName', models.TextField(blank=True, db_column='ShipperName', null=True)),
                ('ShipperFullAddress', models.TextField(blank=True, db_column='ShipperFullAddress', null=True)),
                ('ShipperRoute', models.TextField(blank=True, db_column='ShipperRoute', null=True)),
                ('ShipperCity', models.TextField(blank=True, db_column='ShipperCity', null=True)),
                ('ShipperStateRegion', models.TextField(blank=True, db_column='ShipperStateRegion', null=True)),
                ('ShipperPostalCode', models.TextField(blank=True, db_column='ShipperPostalCode', null=True)),
                ('ShipperCountry', models.TextField(blank=True, db_column='ShipperCountry', null=True)),
                ('ShipperURL', models.TextField(blank=True, db_column='ShipperURL', null=True)),
                ('ShipperLocalDUNS', models.FloatField(db_column='ShipperLocalDUNS')),
                ('ShipperPanjivaID', models.FloatField(db_column='ShipperPanjivaID')),
                ('ShipperStockTickers', models.TextField(blank=True, db_column='ShipperStockTickers', null=True)),
                ('ShipperCleanedStockTickers', models.TextField(blank=True, db_column='ShipperCleanedStockTickers', null=True)),
                ('ShipperUltimateParentStockTickers', models.TextField(blank=True, db_column='ShipperUltimateParentStockTickers', null=True)),
                ('ShipperUltimateParentCleanedStockTickers', models.TextField(blank=True, db_column='ShipperUltimateParentCleanedStockTickers', null=True)),
                ('ShipperUltimateParentName', models.TextField(blank=True, db_column='ShipperUltimateParentName', null=True)),
                ('ShipperOriginalFormat', models.TextField(blank=True, db_column='ShipperOriginalFormat', null=True)),
                ('ID', models.BigIntegerField(db_column='ID')),
            ],
            options={
                'db_table': 'ShipperPanjivaID',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Epoch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126)),
                ('path', models.TextField()),
            ],
        ),
    ]
