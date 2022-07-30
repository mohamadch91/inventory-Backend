# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fieldclass(models.Model):
    fieldid = models.IntegerField(db_column='fieldID', blank=True, null=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='classID', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldClass'


class Globalconfig(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    country = models.CharField(max_length=50, blank=True, null=True)
    codecountry = models.CharField(db_column='CodeCountry', max_length=10, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=50, blank=True, null=True)  # Field name made lowercase.
    levels = models.IntegerField(db_column='Levels', blank=True, null=True)  # Field name made lowercase.
    logo = models.CharField(db_column='Logo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginbg = models.CharField(db_column='loginBG', max_length=200, blank=True, null=True)  # Field name made lowercase.
    poptarget = models.IntegerField()
    poprate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    havehr = models.BooleanField(blank=True, null=True)
    mainlocation = models.CharField(max_length=100, blank=True, null=True)
    logo2 = models.CharField(db_column='Logo2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usingtool = models.BooleanField(db_column='usingTool', blank=True, null=True)  # Field name made lowercase.
    usingmaintenance = models.BooleanField(db_column='usingMaintenance', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GlobalConfig'


class Messages(models.Model):
    message = models.CharField(max_length=4000, blank=True, null=True)
    sender = models.IntegerField(blank=True, null=True)
    reciever = models.IntegerField(blank=True, null=True)
    isnew = models.BooleanField(blank=True, null=True)
    ondate = models.DateTimeField(blank=True, null=True)
    enterby = models.IntegerField(db_column='Enterby', blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Messages'


class Coding(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)
    imagefile = models.CharField(max_length=50, blank=True, null=True)
    orderid = models.IntegerField(blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coding'


class Culture(models.Model):
    abr = models.CharField(db_column='Abr', primary_key=True, max_length=2)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cssfile = models.CharField(db_column='CssFile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    direction = models.CharField(db_column='Direction', max_length=4, blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='isDefault', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'culture'


class Facility(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentID', blank=True, null=True)  # Field name made lowercase.
    insertdate = models.CharField(db_column='insertDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    code2 = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    provinceid = models.IntegerField(db_column='provinceID', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=50, blank=True, null=True)
    zone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    postalcode = models.CharField(db_column='postalCode', max_length=12, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=50, blank=True, null=True)
    haveinternet = models.BooleanField(db_column='haveInternet', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=100, blank=True, null=True)
    ownership = models.CharField(max_length=50, blank=True, null=True)
    distancefromparent = models.IntegerField(db_column='distanceFromParent', blank=True, null=True)  # Field name made lowercase.
    timetoparent = models.CharField(db_column='timeToParent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    roadtype = models.IntegerField(db_column='roadType', blank=True, null=True)  # Field name made lowercase.
    climate = models.IntegerField(blank=True, null=True)
    populationnumber = models.IntegerField(db_column='populationNumber', blank=True, null=True)  # Field name made lowercase.
    childrennumber = models.IntegerField(db_column='childrenNumber', blank=True, null=True)  # Field name made lowercase.
    receivingvaccmode = models.IntegerField(db_column='receivingVaccMode', blank=True, null=True)  # Field name made lowercase.
    transportmode = models.IntegerField(db_column='transportMode', blank=True, null=True)  # Field name made lowercase.
    startwork = models.CharField(db_column='startWork', max_length=50, blank=True, null=True)  # Field name made lowercase.
    staffnumber = models.IntegerField(db_column='staffNumber', blank=True, null=True)  # Field name made lowercase.
    powersource = models.IntegerField(db_column='powerSource', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    higherlevel = models.IntegerField(db_column='higherLevel', blank=True, null=True)  # Field name made lowercase.
    lowerlevel = models.IntegerField(db_column='lowerLevel', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    updatenumber = models.CharField(db_column='updateNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    completerstaffname = models.CharField(db_column='completerStaffName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    completerstaffposition = models.CharField(db_column='completerStaffPosition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    completerstaffsign = models.CharField(db_column='completerStaffSign', max_length=50, blank=True, null=True)  # Field name made lowercase.
    facilitybarcode = models.CharField(db_column='facilityBarcode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipbarcode = models.CharField(db_column='equipBarcode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(max_length=50, blank=True, null=True)
    gps = models.CharField(max_length=50, blank=True, null=True)
    other = models.CharField(max_length=50, blank=True, null=True)
    changedate = models.CharField(db_column='changeDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coverage = models.IntegerField(db_column='Coverage', blank=True, null=True)  # Field name made lowercase.
    functionstatus = models.IntegerField(blank=True, null=True)
    byfile = models.IntegerField(blank=True, null=True)
    haveimmservice = models.BooleanField(db_column='HaveImmService', blank=True, null=True)  # Field name made lowercase.
    typeimmservice = models.IntegerField(db_column='TypeImmService', blank=True, null=True)  # Field name made lowercase.
    numimmperweek = models.IntegerField(db_column='NumImmperWeek', blank=True, null=True)  # Field name made lowercase.
    numprofstaff = models.IntegerField(db_column='NumProfStaff', blank=True, null=True)  # Field name made lowercase.
    numvaccstaff = models.IntegerField(db_column='NumVaccStaff', blank=True, null=True)  # Field name made lowercase.
    numdriverstaff = models.IntegerField(db_column='NumDriverStaff', blank=True, null=True)  # Field name made lowercase.
    coverage2 = models.IntegerField(db_column='Coverage2', blank=True, null=True)  # Field name made lowercase.
    havegenerator = models.BooleanField(db_column='HaveGenerator', blank=True, null=True)  # Field name made lowercase.
    havecovid = models.BooleanField(db_column='HaveCovid', blank=True, null=True)  # Field name made lowercase.
    countvacc1 = models.IntegerField(db_column='countVacc1', blank=True, null=True)  # Field name made lowercase.
    countvacc2 = models.IntegerField(db_column='countVacc2', blank=True, null=True)  # Field name made lowercase.
    otherservice = models.BooleanField(blank=True, null=True)
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True)  # Field name made lowercase.
    delreason = models.IntegerField(blank=True, null=True)
    enterby = models.IntegerField(db_column='enterBy', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=100, blank=True, null=True)
    selectedservices = models.CharField(db_column='selectedServices', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isbuildingsuitable = models.IntegerField(db_column='IsbuildingSuitable', blank=True, null=True)  # Field name made lowercase.
    buildingsuitablereason = models.IntegerField(db_column='buildingSuitableReason', blank=True, null=True)  # Field name made lowercase.
    numicepack = models.IntegerField(db_column='NumIcepack', blank=True, null=True)  # Field name made lowercase.
    maxsdi = models.DecimalField(db_column='MaxSDI', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    facmainplan = models.CharField(db_column='FacMainPlan', max_length=200, blank=True, null=True)  # Field name made lowercase.
    numisopen = models.IntegerField(db_column='NumIsOpen', blank=True, null=True)  # Field name made lowercase.
    workinghfrom = models.CharField(db_column='workingHFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workinghto = models.CharField(db_column='workingHTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    other1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other3 = models.BooleanField(blank=True, null=True)
    other4 = models.BooleanField(blank=True, null=True)
    other5 = models.CharField(max_length=100, blank=True, null=True)
    other6 = models.CharField(max_length=100, blank=True, null=True)
    coverage3 = models.IntegerField(db_column='Coverage3', blank=True, null=True)  # Field name made lowercase.
    countvacc3 = models.IntegerField(db_column='countVacc3', blank=True, null=True)  # Field name made lowercase.
    coverage4 = models.IntegerField(db_column='Coverage4', blank=True, null=True)  # Field name made lowercase.
    countvacc4 = models.IntegerField(db_column='countVacc4', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facility'


class Facilityfield(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='fieldName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fildculturekey = models.CharField(db_column='fildCultureKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(blank=True, null=True)
    controltype = models.CharField(db_column='controlType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enable = models.BooleanField(blank=True, null=True)
    req = models.BooleanField(blank=True, null=True)
    orderid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facilityField'


class Field(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fildname = models.CharField(db_column='fildName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fildculturekey = models.CharField(db_column='fildCultureKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(blank=True, null=True)
    controltype = models.CharField(db_column='controlType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enable = models.BooleanField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    catid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field'


class Gapplan(models.Model):
    facid = models.IntegerField(blank=True, null=True)
    gapstoreid = models.IntegerField(blank=True, null=True)
    pqscode = models.CharField(max_length=100, blank=True, null=True)
    pqstype = models.CharField(max_length=200, blank=True, null=True)
    netvacccapacity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    freezercapacity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    finish = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gapplan'


class Gapstores(models.Model):
    facid = models.IntegerField(blank=True, null=True)
    storecondition = models.IntegerField(blank=True, null=True)
    avl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    func = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    req = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ondate = models.DateTimeField(blank=True, null=True)
    enterby = models.IntegerField(blank=True, null=True)
    planed = models.BooleanField(blank=True, null=True)
    condtion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gapstores'


class Help(models.Model):
    pageid = models.IntegerField(blank=True, null=True)
    val = models.TextField(blank=True, null=True)
    abr = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help'


class Hr(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    positionid = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    eduid = models.IntegerField(blank=True, null=True)
    yinserv = models.IntegerField(blank=True, null=True)
    facid = models.IntegerField(blank=True, null=True)
    enterby = models.IntegerField(blank=True, null=True)
    yinposition = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr'


class Item(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    facilityid = models.IntegerField(db_column='facilityID', blank=True, null=True)  # Field name made lowercase.
    itemclassid = models.IntegerField(db_column='itemClassID', blank=True, null=True)  # Field name made lowercase.
    itemtypeid = models.IntegerField(db_column='itemtypeID', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(blank=True, null=True)
    code2 = models.CharField(max_length=100, blank=True, null=True)
    pqscode = models.CharField(db_column='PQSCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    length = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    grossvolume = models.DecimalField(db_column='grossVolume', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    netvolume = models.DecimalField(db_column='netVolume', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    coolingunitnumber = models.IntegerField(db_column='coolingUnitNumber', blank=True, null=True)  # Field name made lowercase.
    refrigerangas = models.IntegerField(db_column='refrigeranGas', blank=True, null=True)  # Field name made lowercase.
    cfcfree = models.BooleanField(db_column='CFCFree', blank=True, null=True)  # Field name made lowercase.
    shelvesok = models.BooleanField(db_column='shelvesOK', blank=True, null=True)  # Field name made lowercase.
    voltageok = models.BooleanField(db_column='voltageOK', blank=True, null=True)  # Field name made lowercase.
    insidedoor = models.BooleanField(db_column='insideDoor', blank=True, null=True)  # Field name made lowercase.
    havetempmonitor = models.BooleanField(db_column='haveTempMonitor', blank=True, null=True)  # Field name made lowercase.
    havealarm = models.BooleanField(db_column='haveAlarm', blank=True, null=True)  # Field name made lowercase.
    mobilealarm = models.BooleanField(db_column='mobileAlarm', blank=True, null=True)  # Field name made lowercase.
    voltage = models.IntegerField(blank=True, null=True)
    phase = models.IntegerField(blank=True, null=True)
    financialsourceid = models.IntegerField(db_column='financialSourceID', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.IntegerField(db_column='unitCost', blank=True, null=True)  # Field name made lowercase.
    installyear = models.IntegerField(db_column='installYear', blank=True, null=True)  # Field name made lowercase.
    physicalcondition = models.IntegerField(db_column='physicalCondition', blank=True, null=True)  # Field name made lowercase.
    techcondition = models.IntegerField(db_column='techCondition', blank=True, null=True)  # Field name made lowercase.
    havefreezing = models.BooleanField(db_column='haveFreezing', blank=True, null=True)  # Field name made lowercase.
    havethermometer = models.BooleanField(db_column='haveThermometer', blank=True, null=True)  # Field name made lowercase.
    netgeneratedpower = models.DecimalField(db_column='netGeneratedPower', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    havefueltank = models.BooleanField(db_column='haveFuelTank', blank=True, null=True)  # Field name made lowercase.
    inuse = models.BooleanField(db_column='inUse', blank=True, null=True)  # Field name made lowercase.
    notusedate = models.CharField(db_column='notUseDate', max_length=12, blank=True, null=True)  # Field name made lowercase.
    notusecause = models.IntegerField(db_column='notUseCause', blank=True, null=True)  # Field name made lowercase.
    manufactureid = models.IntegerField(db_column='manufactureID', blank=True, null=True)  # Field name made lowercase.
    pricevalue = models.IntegerField(db_column='priceValue', blank=True, null=True)  # Field name made lowercase.
    usercreatedid = models.IntegerField(db_column='userCreatedID', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    changedate = models.CharField(db_column='changeDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wvssmcode = models.CharField(db_column='wVSSMCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tempzone = models.IntegerField(db_column='tempZone', blank=True, null=True)  # Field name made lowercase.
    temprange = models.IntegerField(db_column='tempRange', blank=True, null=True)  # Field name made lowercase.
    uniceffcatalognumber = models.CharField(db_column='uniceffCatalogNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    energysourceid = models.IntegerField(db_column='energySourceID', blank=True, null=True)  # Field name made lowercase.
    capacity = models.CharField(max_length=50, blank=True, null=True)
    otherfield1 = models.CharField(db_column='otherField1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otherfield2 = models.CharField(db_column='otherField2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otherfield3 = models.CharField(db_column='otherField3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otherfield4 = models.CharField(db_column='otherField4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otherfield5 = models.CharField(db_column='otherField5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(max_length=50, blank=True, null=True)
    netcapacity = models.CharField(db_column='netCapacity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    externalsize = models.CharField(db_column='externalSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    othercode = models.CharField(db_column='otherCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    netvacccapacity = models.CharField(db_column='netVaccCapacity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    icecapacity = models.CharField(db_column='iceCapacity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolwatercapacity = models.CharField(db_column='coolWaterCapacity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sepfreez = models.BooleanField(db_column='sepFreez', blank=True, null=True)  # Field name made lowercase.
    powerconsum = models.CharField(db_column='powerConsum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runningtime_h = models.CharField(db_column='runningTime_H', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runningtime_km = models.CharField(db_column='runningTime_Km', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workingconditionid = models.IntegerField(db_column='workingConditionID', blank=True, null=True)  # Field name made lowercase.
    originalcost = models.CharField(db_column='originalCost', max_length=50, blank=True, null=True)  # Field name made lowercase.
    doornumber = models.CharField(db_column='doorNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    insertdate = models.CharField(db_column='insertDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    powergeneration = models.IntegerField(db_column='powerGeneration', blank=True, null=True)  # Field name made lowercase.
    pqstype = models.CharField(max_length=50, blank=True, null=True)
    pqsmanufacturer = models.CharField(max_length=50, blank=True, null=True)
    pqsrefgas = models.CharField(max_length=50, blank=True, null=True)
    pqstempzone = models.CharField(max_length=50, blank=True, null=True)
    coolantpacknominalcapacity = models.CharField(db_column='CoolantPackNominalCapacity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolantpacknumber = models.CharField(max_length=50, blank=True, null=True)
    dshavelight = models.IntegerField(db_column='DSHaveLight', blank=True, null=True)  # Field name made lowercase.
    dshaveheat = models.IntegerField(db_column='DSHaveHeat', blank=True, null=True)  # Field name made lowercase.
    dshaveac = models.IntegerField(db_column='DSHaveAC', blank=True, null=True)  # Field name made lowercase.
    dsprotsun = models.IntegerField(db_column='DSProtSun', blank=True, null=True)  # Field name made lowercase.
    dshaveshelve = models.IntegerField(db_column='DSHaveShelve', blank=True, null=True)  # Field name made lowercase.
    dsisclean = models.IntegerField(db_column='DSIsClean', blank=True, null=True)  # Field name made lowercase.
    dsprotmois = models.IntegerField(db_column='DSProtMois', blank=True, null=True)  # Field name made lowercase.
    dsarea = models.DecimalField(db_column='DSArea', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dsheight = models.DecimalField(db_column='DSHeight', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isdel = models.IntegerField(db_column='isDel', blank=True, null=True)  # Field name made lowercase.
    delreason = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    autostart = models.IntegerField(db_column='autoStart', blank=True, null=True)  # Field name made lowercase.
    typeparam1 = models.IntegerField(db_column='TypeParam1', blank=True, null=True)  # Field name made lowercase.
    typeparam2 = models.IntegerField(db_column='TypeParam2', blank=True, null=True)  # Field name made lowercase.
    typeparam3 = models.IntegerField(db_column='TypeParam3', blank=True, null=True)  # Field name made lowercase.
    typeparam4 = models.IntegerField(db_column='TypeParam4', blank=True, null=True)  # Field name made lowercase.
    typeparam5 = models.IntegerField(db_column='TypeParam5', blank=True, null=True)  # Field name made lowercase.
    repairhistory = models.TextField(db_column='repairHistory', blank=True, null=True)  # Field name made lowercase.
    maintenancegroupid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class Itemclass(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    imageurl = models.CharField(db_column='imageUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemClass'


class Itemfield(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemtypeid = models.IntegerField(db_column='itemTypeID', blank=True, null=True)  # Field name made lowercase.
    fieldid = models.IntegerField(db_column='fieldID', blank=True, null=True)  # Field name made lowercase.
    req = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'itemField'


class Itemtype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=200, blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)
    itemclassid = models.IntegerField(db_column='itemClassID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=10, blank=True, null=True)
    req = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemType'


class Itemtypelevel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemtypeid = models.IntegerField(db_column='itemTypeID', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemTypeLevel'


class Levelconfig(models.Model):
    levelid = models.IntegerField(db_column='levelID', primary_key=True)  # Field name made lowercase.
    maxpop = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    minpop = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    uppervol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    undervol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maxpopu1 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    minpopu1 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    m25vol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    m70vol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    m25volnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    m70volnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    uppervolnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    undervolnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    dryvol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dryvolnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'levelconfig'


class Manufacturer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=200, blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer'


class ManufacturerClasstype(models.Model):
    classtypeid = models.IntegerField(db_column='classtypeID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=50, blank=True, null=True)
    orderid = models.IntegerField(blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer_Classtype'


class MtncGroups(models.Model):
    groupname = models.CharField(max_length=300, blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)
    itemtypeid = models.IntegerField(db_column='itemtypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtnc_groups'


class MtncItemgroupservice(models.Model):
    itemid = models.IntegerField(blank=True, null=True)
    servicegroupid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtnc_itemgroupservice'


class MtncServiceaction(models.Model):
    itemid = models.IntegerField(blank=True, null=True)
    serviceid = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    ondate = models.DateTimeField(blank=True, null=True)
    enterby = models.IntegerField(blank=True, null=True)
    entrydate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtnc_serviceaction'


class MtncServices(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)
    itemtypeid = models.IntegerField(db_column='itemtypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mtnc_services'


class MtncSrvicegroup(models.Model):
    serviceid = models.IntegerField(blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mtnc_srvicegroup'


class Store(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=200, blank=True, null=True)
    placeid = models.IntegerField(db_column='placeID', blank=True, null=True)  # Field name made lowercase.
    order = models.IntegerField(blank=True, null=True)
    desc = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'


class Tmppqs(models.Model):
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    make = models.CharField(db_column='Make', max_length=100, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pqscode = models.CharField(db_column='PQScode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refrigerant = models.CharField(db_column='Refrigerant', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tempzone = models.CharField(db_column='Tempzone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refrigeratorcapacity = models.FloatField(db_column='RefrigeratorCapacity', blank=True, null=True)  # Field name made lowercase.
    freezercapacity = models.FloatField(db_column='FreezerCapacity', blank=True, null=True)  # Field name made lowercase.
    kg_24_hrs = models.FloatField(blank=True, null=True)
    waterpackstoragecapacity = models.FloatField(db_column='WaterpackStorageCapacity', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    h = models.FloatField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    w = models.FloatField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.FloatField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpPQS'


class Tmppqs2(models.Model):
    pqsnumber = models.CharField(db_column='PQSNumber', max_length=100)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vaccinenetstoragecapacity = models.FloatField(db_column='VaccineNetStorageCapacity', blank=True, null=True)  # Field name made lowercase.
    coolantpacknominalcapacity = models.FloatField(db_column='CoolantPackNominalCapacity', blank=True, null=True)  # Field name made lowercase.
    numbercoolantpacks = models.IntegerField(db_column='NumberCoolantPacks', blank=True, null=True)  # Field name made lowercase.
    externalvolume = models.FloatField(db_column='ExternalVolume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpPQS2'


class Tmpfac(models.Model):
    faccode = models.CharField(max_length=50, blank=True, null=True)
    facname = models.CharField(max_length=200, blank=True, null=True)
    pfaccode = models.CharField(max_length=50, blank=True, null=True)
    factype = models.CharField(max_length=20, blank=True, null=True)
    lvl = models.CharField(max_length=10, blank=True, null=True)
    lvlcode = models.CharField(max_length=10, blank=True, null=True)
    population = models.CharField(max_length=50, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmpfac'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    facilityid = models.IntegerField(db_column='facilityID', blank=True, null=True)  # Field name made lowercase.
    createby = models.IntegerField(blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)
    lastlogin = models.CharField(db_column='lastLogin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    creatondate = models.CharField(max_length=50, blank=True, null=True)
    idnumber = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    facadmin = models.BooleanField(blank=True, null=True)
    itemadmin = models.BooleanField(blank=True, null=True)
    reportadmin = models.BooleanField(blank=True, null=True)
    useradmin = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
