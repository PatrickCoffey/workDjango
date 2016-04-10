from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Issue(models.Model):
    '''This represents the issue base class'''
    # meta shit
    incident_number = models.IntegerField("Incident Number")
    parsys_number = models.IntegerField("PARSYS Number")
    ascribe_number = models.IntegerField("Ascribe Number")
    logged_by = models.CharField("Logged By")
    logged_time = models.DateTimeField("Logged Time")
    release_version = models.ForeignKey(Release, verbose_name="Release")
    environment = models.ForeignKey(Environment, verbose_name="Environment")
    status = models.ForeignKey(Status, verbose_name="Status")
    priority = models.ForeignKey(Priority, verbose_name="Priority")
    review_time = models.DateTimeField("Review Time")
    outcome = models.CharField("Outcome")
    comments = models.DateField("Comments")
    
    # actual issue data
    brief_description = models.CharField("Brief Description")
    incident_description = models.CharField("Incident Description")
    suggested_action = models.CharField("Suggested Action(s)")
    
    # optional data
    tested_users = models.CharField("Tested Users")


class Screenshot(models.Model):
    '''holds blobs of screenshots'''
    title = models.CharField("Title")
    image = models.BinaryField("Image")
    issue = models.ForeignKey(Issue, verbose_name="Related Issue")
    

class Environment(models.Model):
    '''allows selection of environments eg. test, training production'''
    title = models.CharField()
    
    
class Status(models.Model):
    '''status of the incident eg. draft, sent, resolved'''
    pass


class Priority(models.Model):
    '''represents the priority of the incident eg. low, high'''
    pass


class Outcome(models.Model):
    '''Represents if the issue has been resolved or not'''
    pass


class User(models.Model):
    '''Actual users that are entering Incidents'''
    pass


class Release(models.Model):
    '''version string of PCIS'''
    pass


class TestedUser(models.Model):
    '''username that was used to identify the issue'''
    pass