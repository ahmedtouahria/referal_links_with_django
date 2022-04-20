# referal_links_with_django
# Referal links with django rest framework
# Technical requirements 
Using Django REST frame work please implement the followings

1- Models 
    - User
    - Profile 

2- register user and Create profile automatically

3- authentication user


4-  Create a unique code for each user With #UUID library 
```python
import uuid
def generate_random_code():
    code=str(uuid.uuid4()).replace('-','')[:12]
    return code
```

5- Create url with snippet code  --> http://127.0.0.1:8000/api/register/<--code recommended user-->

```python
path('api/register/<str:ref_code>', RegisterUserAPIView.as_view(), name='register'),

```

6- Then use DJANGO ORM to fetch the recommended user

```python
 # red_code define from url -> api/register/<str:ref_code>
          code = str(kwargs.get('ref_code'))
          # get  user Profile id 
          profile = Profile.objects.get(code=code)
          # create a session 'ref_profile' 
          request.session['ref_profile'] = profile.id
          profile.isPartner=True
          profile.profit+=1.5
          profile.save()
```
---- and override save method from Profil model ---
```python
 def save(self, *args, **kwargs):
       if self.code=='':
           code = generate_random_code()
           self.code=code
       super().save(*args, **kwargs) # Call the real save() method
```
7- and update profit field or make anything do you want 

