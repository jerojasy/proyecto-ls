# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clientes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apepat = models.CharField(max_length=50, blank=True, null=True)
    apemat = models.CharField(max_length=50, blank=True, null=True)
    edad = models.BigIntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=20, blank=True, null=True)
    prevision = models.CharField(max_length=20, blank=True, null=True)
    fono = models.CharField(max_length=12, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre
    

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleados(models.Model):
    id_empleado = models.BigIntegerField(primary_key=True)
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    celular = models.CharField(max_length=100)
    fecha_contrato = models.DateField()
    cargo = models.CharField(max_length=100, blank=True, null=True)
    sueldo = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    

    class Meta:
        managed = False
        db_table = 'empleados'
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"


class Login(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    contrasena = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Proveedor(models.Model):
    id_proveedor = models.BigIntegerField(primary_key=True)
    rut = models.CharField(max_length=12, blank=True, null=True)
    nombre_contacto = models.CharField(max_length=100, blank=True, null=True)
    producto = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField(max_length=150, blank=True, null=True)
    rubro = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.empresa
    

    class Meta:
        managed = False
        db_table = 'proveedor'
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=50, blank=True, null=True)
    descripcionesp = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_especialidad

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
    

class Reserva(models.Model):
    usuario = models.CharField(max_length=150, blank=True, null=True)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    estado = models.CharField(default=1, max_length=20, blank=True, null=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha_reserva

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

class Producto(models.Model):
    nomproducto = models.CharField(max_length=100)
    SKU = models.CharField(max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    vencimiento = models.DateField()
    preciocompra = models.IntegerField()
    precioventa = models.IntegerField()
    stock = models.IntegerField()
    stockcritico = models.IntegerField()
   

    def str(self):
        return self.nomproducto

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"