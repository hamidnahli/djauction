from django.db import models


class Auction(models.Model):
    auction_id = models.UUIDField(primary_key=True, editable=False)
    auction_name = models.CharField(max_length=150, null=False, blank=False)
    auction_start_date = models.DateTimeField()
    auction_end_date = models.DateTimeField()
    auction_location = models.CharField(max_length=150,blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

