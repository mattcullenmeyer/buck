from django.db import models
import uuid

class School(models.Model):
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False,
  )
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200)

  def __str__(self):
    return self.name

class Ratings(models.Model):
  school = models.OneToOneField(
    School, 
    on_delete=models.CASCADE, 
    primary_key=True
  )
  overallRating = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
  overallEarned = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
  overallAvailable = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
  growthRating = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
  growthEarned = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
  growthAvailable = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
  achievementRating = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
  achievementEarned = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
  achievementAvailable = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

  def __str__(self):
    return f'{self.school}'

class Statistics(models.Model):
  school = models.OneToOneField(
    School, 
    on_delete=models.CASCADE, 
    primary_key=True
  )
  schoolWebsite = models.CharField(max_length=200, blank=True, null=True)
  schoolWebsiteShort = models.CharField(max_length=200, blank=True, null=True)
  enrollment = models.IntegerField(blank=True, null=True) 
  freeReducedLunch = models.IntegerField(blank=True, null=True) 
  minorityStudents = models.IntegerField(blank=True, null=True) 
  englishLearners = models.IntegerField(blank=True, null=True) 
  disabilityStudents = models.IntegerField(blank=True, null=True) 

  def __str__(self):
    return f'{self.school}'

class Suggested(models.Model):
  school = models.ForeignKey(
    School,
    on_delete=models.CASCADE,
  )
  suggest = models.ForeignKey(
    School,
    on_delete=models.CASCADE,
    related_name='suggest',
  )

  def __str__(self):
    return f'{self.school} >> {self.suggest}'