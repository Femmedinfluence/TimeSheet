from django.db import models


class Departement(models.Model):
    id_dptmt = models.AutoField(primary_key=True)
    nom_dptmt = models.CharField(max_length=255)
    libelle = models.CharField(max_length=255)
    id_empl = models.ForeignKey('Employe', models.DO_NOTHING, db_column='id_empl')

    class Meta:
        db_table = 'departement'


class Employe(models.Model):
    id_empl = models.AutoField(primary_key=True)
    nom_empl = models.CharField(max_length=255)
    prenom_empl = models.CharField(max_length=255)
    fonct_empl = models.CharField(max_length=255)
    adresse_empl = models.CharField(max_length=255)
    contact_empl = models.IntegerField()
    localisation_empl = models.CharField(max_length=255)
    genre_empl = models.CharField(max_length=255)
    signature_empl = models.CharField(max_length=255)

    class Meta:
        db_table = 'employe'


class Feuilletemps(models.Model):
    id_ftemps = models.AutoField(primary_key=True)
    date_debut = models.TextField()  # This field type is a guess.
    date_fin = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_jour = models.TextField()  # This field type is a guess.
    nombre_heure = models.IntegerField()
    type_conge = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)

    class Meta:
        db_table = 'feuilletemps'


class Projet(models.Model):
    code_projet = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'projet'


class Renseigner(models.Model):
    id_empl = models.ForeignKey(Employe, models.DO_NOTHING, db_column='id_empl', blank=True, null=True)
    id_ftemps = models.ForeignKey(Feuilletemps, models.DO_NOTHING, db_column='id_ftemps', blank=True, null=True)

    class Meta:
        db_table = 'renseigner'


class Superviseur(models.Model):
    id_superv = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=42)
    id_ftemps = models.ForeignKey(Feuilletemps, models.DO_NOTHING, db_column='id_ftemps')
    id_empl = models.ForeignKey(Employe, models.DO_NOTHING, db_column='id_empl')

    class Meta:
        db_table = 'superviseur'


class Travail(models.Model):
    id_empl = models.ForeignKey(Employe, models.DO_NOTHING, db_column='id_empl', blank=True, null=True)
    code_projet = models.ForeignKey(Projet, models.DO_NOTHING, db_column='code_projet', blank=True, null=True)

    class Meta:
        db_table = 'travail'
