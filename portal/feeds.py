from django.contrib.syndication.views import Feed 
from django.template.defaultfilters import truncatewords 
from .models import Post
from django.urls import reverse 
from django.utils.feedgenerator import Atom1Feed 
  
class blogFeed(Feed): 
    title = "pleiades.link"
    link = "/feed/"
    description = "pleiades.link RSS"
  
    def items(self): 
        return Post.objects.filter(status = 1) 
  
    def item_title(self, item): 
        return item.title 
        
    def item_description(self, item): 
        return item.content
  
    def item_link(self, item): 
       return reverse('post_view', args = [item.slug]) 
  
class atomFeed(Feed): 
    feed_type = Atom1Feed