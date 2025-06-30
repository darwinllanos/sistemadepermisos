from django.db import models

class vEmployeeAutorizado(models.Model):
    idEmployee = models.UUIDField(primary_key=True, db_column='idEmployee')
    idRol = models.UUIDField(db_column='idRol')
    idArea = models.UUIDField(db_column='idArea')
    emailBussiness = models.CharField(max_length=100, db_column='emailBussiness')

    class Meta:
        managed = False
        db_table = 'v_EmployeeAutorizado'


class vPayRollAutorizado(models.Model):
    idPayRoll = models.UUIDField(primary_key=True, db_column='idPayRoll')
    idUser = models.UUIDField(db_column='idUser')
    idMonth = models.UUIDField(db_column='idMonth')
    idPayment = models.UUIDField(db_column='idPayment')
    totalValue = models.DecimalField(max_digits=12, decimal_places=2, db_column='totalValue')

    class Meta:
        managed = False
        db_table = 'v_PayRollAutorizado'

class TypePayment(models.Model):
    idPayment = models.UUIDField(primary_key=True, db_column='idPayment')
    namePayment = models.CharField(max_length=50, db_column='namePayment')

    class Meta:
        managed = False
        db_table = 'TypePayment'

class Month(models.Model):
    idMonth = models.UUIDField(primary_key=True, db_column='idMonth')
    month = models.CharField(max_length=50, db_column='month')

    class Meta:
        managed = False
        db_table = 'Month'
