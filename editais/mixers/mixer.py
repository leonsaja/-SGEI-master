from mixer.backend.django import mixer
from accounts.models import *

mixer.cycle(200).blend(User)

