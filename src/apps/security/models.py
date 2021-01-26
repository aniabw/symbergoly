from django.db import models
import apps.users.utils as utils


# Create your models here.

# import sys
# for p in sys.path: print(p)
print(utils.generate_token())