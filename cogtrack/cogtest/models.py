from django.db import models

# TODO: think of a better naming scheme or something
COG_TESTS = (
  ('Speed', (
    ('react', 'Reaction Time'),
    ('go_no_go', 'Go/No-go'),
  )),
  ('Memory', (
    ('dual_n_back', 'Dual n-back'),
  )),
  ('Problem Solving', (
    ('blah', 'Blah Blah Blah'),
  )),
)

class CogTest(models.Model):
  name = models.CharField(max_length = 10, choices = COG_TESTS) # An enum is a better choice. deal with this later
  start = models.DateTimeField('time test started')
  end = models.DateTimeField('time test ended')

  def __unicode__(self):
      return self.name
