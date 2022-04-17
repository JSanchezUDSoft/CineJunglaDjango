from django.db import models

class Multiplex(models.Model):
    k_multiplex = models.AutoField(primary_key=True)
    n_multiplex = models.CharField(max_length=30, verbose_name="nombreM")
    o_direccion = models.CharField(max_length=60, verbose_name="direccion")

class Usuario(models.Model):
    k_identificacion = models.CharField(primary_key=True, max_length=12, verbose_name = "identificacion")
    n_nombre = models.CharField(max_length=60, verbose_name="nombre")
    t_celular = models.CharField(max_length=10, verbose_name="celular")
    f_contrato = models.DateField(verbose_name="fechaContrato")
    v_salario = models.IntegerField(verbose_name="salario")
    i_rol = models.CharField(max_length=1, verbose_name="rol")
    i_cargo = models.CharField(max_length=1, verbose_name="cargo")
    o_contrasena = models.CharField(max_length=20, verbose_name="contrasena")
    k_multiplex = models.ForeignKey(Multiplex, on_delete=models.CASCADE)

class Sala(models.Model):
    k_sala = models.AutoField(primary_key=True)
    k_multiplex = models.ForeignKey(Multiplex, on_delete=models.CASCADE)
    n_sala = models.CharField(max_length=15, verbose_name="nombreSala")