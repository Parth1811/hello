from django.db import models

class topics(models.Model):
    title = models.CharField(max_length=15)
    topic_name = models.CharField(max_length=25)
    MSG_TYPE_CHOICES =  (('DVL', "DvlData"),('IMU', "IMUDATA"))
    ros_msg_type = models.CharField(max_length=15 ,choices=MSG_TYPE_CHOICES, editable = True)
    max_post_required = models.IntegerField()
    timeout = models.IntegerField()

    def __str__(self):
        return self.title
