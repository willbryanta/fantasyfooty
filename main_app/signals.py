# from django.db.models.signals import post_migrate
# from django.dispatch import receiver
# from main_app.models import Player

# @receiver(post_migrate)
# def seed_data(sender, **kwargs):

#     # Wipe all players before seeding
#     Player.objects.all().delete()

#     if not Player.objects.exists():
#         Player.objects.create(name='CeeDee Lamb', age='23', years_played='2', position='WR', team='Utah Jazz', headshotURL='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.foxsports.com%2Fstories%2Fnfl%2Fceedee-lamb-proclaims-he-will-be-in-dallas-as-holdout-rumors-swirl&psig=AOvVaw1QgLEluYrIo-dyaovt4z01&ust=1736939817784000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNimspmL9YoDFQAAAAAdAAAAABAK', user='MonkeyMan@monkey.com')