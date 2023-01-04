from django.db import models
from facilities.models import Facility
from items.models import *
import settings
# Create your models here.
class item(models.Model):
    facility=models.ForeignKey(Facility, on_delete=models.CASCADE, null=True)
    item_class=models.ForeignKey(ItemClass, on_delete=models.CASCADE, null=True)
    item_type=models.ForeignKey(ItemType, on_delete=models.CASCADE, null=True)
    code=models.CharField(max_length=20, null=True)
    TypeP=models.CharField(max_length=250, null=True,blank=True)
    Manufacturer=models.CharField(max_length=250, null=True,blank=True)
    Model=models.CharField(max_length=250, null=True,blank=True)
    Type1=models.CharField(max_length=250, null=True,blank=True)
    Type2=models.CharField(max_length=250, null=True,blank=True)
    Type3=models.CharField(max_length=250, null=True,blank=True)
    Type4=models.CharField(max_length=250, null=True,blank=True)
    Type5=models.CharField(max_length=250, null=True,blank=True)
    Type1P=models.CharField(max_length=250, null=True,blank=True)
    Height=models.FloatField(null=True,blank=True)
    Width=models.FloatField(null=True,blank=True)
    Length=models.FloatField(null=True,blank=True)
    GrossVolume=models.FloatField(null=True,blank=True)
    NetShippingVolume=models.FloatField(null=True,blank=True)
    Weightkg=models.FloatField(null=True,blank=True)
    ExternalSize=models.CharField(max_length=250, null=True,blank=True)
    NumberOfDoors=models.IntegerField(null=True,blank=True)
    IsThereInsideDoor=models.BooleanField(null=True,blank=True)
    DoesItHaveAnAlarmSystem=models.BooleanField(null=True,blank=True)
    DoesItHaveAdequateShelves=models.BooleanField(null=True,blank=True)
    DoesItHaveCurtain=models.BooleanField(null=True,blank=True)
    PhysicalConditions=models.CharField(max_length=250, null=True,blank=True)
    TechnicalConditions=models.CharField(max_length=250, null=True,blank=True)
    WorkingConditions=models.CharField(max_length=250, null=True,blank=True)
    IsItFunctioning=models.BooleanField(null=True,blank=True)
    NotInUseSince=models.IntegerField(null=True,blank=True)
    ReasonsForNotFunctioning=models.CharField(max_length=250, null=True,blank=True)
    YearInstalled=models.CharField(max_length=250, null=True,blank=True)
    RunningTime=models.IntegerField(null=True,blank=True)
    RunningTimeKm=models.IntegerField(null=True,blank=True)
    StorageCondition=models.CharField(max_length=250, null=True,blank=True)
    NetVaccineStorageCapacity=models.FloatField(null=True,blank=True)
    EnergySource=models.CharField(max_length=250, null=True,blank=True)
    FreezerNetCapacity=models.FloatField(null=True,blank=True)
    IceMakingCapacity=models.FloatField(null=True,blank=True)
    CoolWaterProductionCapacity=models.IntegerField(null=True,blank=True)
    NumberOfCoolingUnits=models.IntegerField(null=True,blank=True)
    WorkingTemperatureRange=models.CharField(max_length=250, null=True,blank=True)
    RefrigerantGas=models.CharField(max_length=250, null=True,blank=True)
    IsTheRefrigerantGasCFCFree=models.BooleanField(null=True,blank=True)
    DoesItHaveFreezingCompartment=models.BooleanField(null=True,blank=True)
    DoesItHaveContinuousTemperatureMonitoringDevice=models.BooleanField(null=True,blank=True)
    DoesItHaveBuiltInThermometer=models.BooleanField(null=True,blank=True)
    NumberOfCoolantPacksRequired=models.IntegerField(null=True,blank=True)
    CoolantPackNominalCapacity=models.IntegerField(null=True,blank=True)
    Voltage=models.IntegerField(null=True,blank=True)
    Phase=models.IntegerField(null=True,blank=True)
    NetGeneratedPower=models.IntegerField(null=True,blank=True)
    EnergySource_generator=models.CharField(max_length=250, null=True,blank=True)
    DoesItHaveAnExtraFuelTank=models.BooleanField(null=True,blank=True)
    PowerOrFuelConsumption=models.IntegerField(null=True,blank=True)
    IsThereAnAutomaticStartUpSystem=models.BooleanField(null=True,blank=True)
    FinancialSource=models.IntegerField(null=True,blank=True)
    UnitCostWhenInstalled=models.IntegerField(null=True,blank=True)
    UnitCostAtPresent=models.IntegerField(null=True,blank=True)
    OriginalCost=models.IntegerField(null=True,blank=True)
    wVSSMCode=models.CharField(max_length=250, null=True,blank=True)
    UNICEFCatalogueCodes=models.CharField(max_length=250, null=True,blank=True)
    OtherCode=models.CharField(max_length=250, null=True,blank=True)
    PQSPISCode=models.CharField(max_length=250, null=True,blank=True)
    PQSPISType=models.CharField(max_length=250, null=True,blank=True)
    PQSPISManufacturer=models.CharField(max_length=250, null=True,blank=True)
    PQSPISRefrigerantGas=models.CharField(max_length=250, null=True,blank=True)
    PQSPISTemperatureWorkingZone=models.CharField(max_length=250, null=True,blank=True)
    DoesTheDryStoreHaveAdequateLighting=models.BooleanField(null=True,blank=True)
    DoesTheDryStoreHaveHeating=models.BooleanField(null=True,blank=True)
    DoesTheDryStoreHaveAirConditioning=models.BooleanField(null=True,blank=True)
    IsTheDryStorageAreaProtectedFromDirectSunlight=models.BooleanField(null=True,blank=True)
    IsTheDryStorageArea=models.BooleanField(null=True,blank=True)
    IsTheDryStorageAreaClean=models.BooleanField(null=True,blank=True)
    IsTheDryStorageAreaDry=models.BooleanField(null=True,blank=True)
    IsTheDryStorageAreaEquippedWithMechanical=models.BooleanField(null=True,blank=True)
    SurfaceArea=models.IntegerField(null=True,blank=True)
    AccessibleHeight=models.IntegerField(null=True,blank=True)
    SerialNumber=models.CharField(max_length=250, null=True,blank=True)
    RepairAndMaintenanceHistory=models.CharField(max_length=250, null=True,blank=True)
    MaintenanceGroup=models.CharField(max_length=250, null=True,blank=True)
    OtherFieldsItem1=models.CharField(max_length=150, null=True,blank=True)
    OtherFieldsItem2=models.BooleanField(null=True,blank=True)
    OtherFieldsItem3=models.CharField(max_length=250, null=True,blank=True)
    OtherFieldsItemParameter4=models.CharField(max_length=250, null=True,blank=True)
    isDel=models.BooleanField(default=False)
    delete_reason=models.CharField(max_length=250, null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)