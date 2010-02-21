from django.db import models

from cogtrack.cogtest.models import CogTest

# There are two ways to do this:
# 1. Include all data
# 2. Just include the calculated stuff we care about (average, median, sample size, error rate)
# Principle of maximum programmer laziness says go with the easier option, which is #2
class GoNoGo(CogTest):
#  test = models.ForeignKey(CogTest, unique=True)
  reaction_time = models.PositiveIntegerField('Average reaction time in milliseconds')
  # Do we want median reaction time too?
  tests = models.PositiveIntegerField('Number of tests')
  errors = models.PositiveIntegerField('Number of mistakes')

  def __unicode__(self):
      return u'%i %i %i' % (self.reaction_time, self.tests, self.errors)

