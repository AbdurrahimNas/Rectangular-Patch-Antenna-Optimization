from django.db import models
from django_matplotlib import MatplotlibFigureField
# Create your models here.

class OptimizerModel(models.Model):

    frequency = models.DecimalField(verbose_name="Frequency [GHz]",
                                    help_text="Frequency of Antenna",
                                    max_digits=10, decimal_places=8,
                                    blank=False, null=False)
    length_of_patch = models.DecimalField(verbose_name="Lenght of Patch [mm]",
                                          help_text="Length of Antenna",
                                          max_digits=9,decimal_places=6,
                                          blank=False, null=False)
    width_of_patch = models.DecimalField(verbose_name="Width of Patch [mm]",
                                         help_text="Width of Antenna",
                                         max_digits=9, decimal_places=6,
                                         blank=False, null=False)
    slot_length = models.DecimalField(verbose_name="Slot Length [mm]",
                                      help_text="Slot Length of Antenna",
                                      max_digits=6, decimal_places=3,
                                      blank=False, null=False)
    slot_width = models.DecimalField(verbose_name="Slot Width [mm]",
                                     help_text="Slot Width of Antenna",
                                     max_digits=6, decimal_places=3,
                                     blank=False, null=False)
    
    #s_11 = models.DecimalField(verbose_name="S_11 [dB]",
    #                           max_digits=20, decimal_places=6,
    #                           blank=True, default=0)


    def __str__(self):
        return f"{self.id}"
    
