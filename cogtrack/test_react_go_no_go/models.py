from django.db import models

# TODO: move CogTest base stuff to a main file. Otherwise new tests will have to include this random file.
# also, think of a better naming scheme or something
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


# There are two ways to do this:
# 1. Include all data
# 2. Just include the calculated stuff we care about (average, median, sample size, error rate)
# Principle of maximum programmer laziness says go with the easier option, which is #2
class GoNoGo(CogTest):
  reaction_time = models.PositiveIntegerField('Average reaction time in milliseconds')
  tests = models.PositiveIntegerField('Number of tests')
  errors = models.PositiveIntegerField('Number of mistakes')

  def __unicode__(self):
      return u'%i %i %i' % (self.reaction_time, self.tests, self.errors)

