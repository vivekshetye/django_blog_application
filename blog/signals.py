from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Post
import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from django.core.files import File
import os, uuid


@receiver(pre_save, sender=Post)
def save_graph(sender, instance, **kwargs):
    print('here')
    # if instance.x and instance.y:
    x = list(map(lambda i: int(i),instance.x.split(",")))
    y = list(map(lambda i: int(i),instance.y.split(",")))
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(x, y, label='$y = numbers')
    plt.title('Legend inside')
    ax.legend()
    img_name = '{}-{}.png'.format(instance.author.username, str(uuid.uuid1()))
    fig.savefig(img_name)

    img = open(img_name, 'rb')

    imga = File(img)

    instance.graph = imga


@receiver(post_save, sender=Post)
def delete_graph(sender, instance, **kwargs):
    img_name = instance.graph.url.split('/')[3]
    print(instance.graph.url)
    os.remove(img_name)
