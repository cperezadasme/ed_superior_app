from django.db import models


class Matricula(models.Model):
    year = models.IntegerField()
    total_students = models.IntegerField()
    total_students_women = models.IntegerField()
    total_students_men = models.IntegerField()
    total_students_first_year = models.IntegerField()
    total_students_women_first_year = models.IntegerField()
    total_students_men_first_year = models.IntegerField()
    institution_classification_level_1 = models.CharField(max_length=255)
    institution_classification_level_2 = models.CharField(max_length=255)
    institution_classification_level_3 = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)
    institutional_accreditation = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    career_name = models.CharField(max_length=255)
    area_of_knowledge = models.CharField(max_length=255)
    ocde_area = models.CharField(max_length=255)
    ocde_subarea = models.CharField(max_length=255)
    generic_career_area = models.CharField(max_length=255)
    global_level = models.CharField(max_length=255)
    career_classification_level_1 = models.CharField(max_length=255)
    career_classification_level_2 = models.CharField(max_length=255)
    modality = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    type_career = models.CharField(max_length=255)
    study_duration_career = models.IntegerField()
    total_duration_career = models.IntegerField()
    career_code = models.CharField(max_length=255)
    total_range_age = models.IntegerField()
    age_range_15_19 = models.IntegerField()
    age_range_20_24 = models.IntegerField()
    age_range_25_29 = models.IntegerField()
    age_range_30_34 = models.IntegerField()
    age_range_35_39 = models.IntegerField()
    age_range_40 = models.IntegerField()
    averange_career_age = models.FloatField()
    averange_career_age_women = models.FloatField()
    averange_career_age_men = models.FloatField()
    tes_municipal = models.IntegerField()
    test_subvencionado = models.IntegerField()
    test_particular = models.IntegerField()
    test_corp = models.IntegerField()
    total_test = models.IntegerField()
    percent_tes = models.FloatField()
    total_hc = models.IntegerField()
    total_tp = models.IntegerField()
    total_young = models.IntegerField()
    total_adult = models.IntegerField()


class Titulados(models.Model):
    year = models.IntegerField()
    total_graduates = models.IntegerField()
    total_graduates_women = models.IntegerField()
    total_graduates_men = models.IntegerField()
    institution_classification_level_1 = models.CharField(max_length=255)
    institution_classification_level_2 = models.CharField(max_length=255)
    institution_classification_level_3 = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    career_name = models.CharField(max_length=255)
    area_of_knowledge = models.CharField(max_length=255)
    oecd_area = models.CharField(max_length=255)
    oecd_subarea = models.CharField(max_length=255)
    generic_career_area = models.CharField(max_length=255)
    global_level = models.CharField(max_length=255)
    career_classification_level_1 = models.CharField(max_length=255)
    career_classification_level_2 = models.CharField(max_length=255)
    modality = models.CharField(max_length=255, null=True, blank=True)
    schedule = models.CharField(max_length=255)
    type_career = models.CharField(max_length=255)
    career_code = models.CharField(max_length=255)
    study_duration_career = models.IntegerField()
    total_duration_career = models.IntegerField()
    total_range_age = models.IntegerField()
    age_range_15_19 = models.IntegerField()
    age_range_20_24 = models.IntegerField()
    age_range_25_29 = models.IntegerField()
    age_range_30_34 = models.IntegerField()
    age_range_35_39 = models.IntegerField()
    age_range_40 = models.IntegerField()
    averange_career_age = models.FloatField()
    averange_career_age_women = models.FloatField()
    averange_career_age_men = models.FloatField()
