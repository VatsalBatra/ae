from django.conf.urls import url
from questions import views #all_Popper,all_Candle,all_Balloon,all_Knife_Caketag,all_Prop_Decoration,all_Crown,all_Cap,about
urlpatterns = [
   # url(r'^all/$', all_questions),
    url(r'^popper/$', views.all_Popper,name = 'popper'),
    url(r'^cap/$', views.all_Cap,name = 'cap'),
    url(r'^contact/$', views.contact,name = 'contact'),  
	url(r'^about/$', views.about,name = 'about'),  
 	url(r'^candle/$',views.all_Candle,name = 'candle'),
 	url(r'^balloon/$',views.all_Balloon,name = 'balloon'),
 	url(r'^knife_caketag/$',views.all_Knife_Caketag,name = 'knife_caketag'),
 	url(r'^prop_decoration/$',views.all_Prop_Decoration,name = 'prop_decoration'),
 	url(r'^crown/$',views.all_Crown,name = 'crown'),
 	url(r'^new/$',views.all_New,name = 'new'),
    #url(r'^all/$', all_questions, name="all-questions"),
     
]
