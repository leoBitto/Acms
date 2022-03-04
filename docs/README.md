
# Acms

Acms is a Django app to organize content in a website.
A content management system created with Bootstrap 5.0 
and Django 4.0 . Its scope is to allow people with no 
knowledge to create simple websites that contain images and text
-----------

## Quick start


1. Add "Acms" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS [
        ...
        'Acms',
    ]
    ```
2. Include the Acms URLconf in your project urls.py like this::

    > path(``, include(('Acms.urls', 'Acms'), namespace="Acms")),

3. Run ``python manage.py migrate`` to create the Acms models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create the models (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000 to see the website


-----------

# Acms docs                       

this content management system is a way to give
bootstrap 5.0 a graphic interface to facilitate
the display of content in an html page
its implementation follow the bootstrap 5.0 docs
https://getbootstrap.com/docs/5.0
the idea is to create pages that are pointed by a series 
of Sections,``<div>`` tags, that organize Containers,
``<div>`` tags that have the 'container' class of bootstrap, they contain
"content" whether it is Text``<p>``, Images``<img>``, Canvas``<canvas>``,
Video``<video>`` etc.., and grids, that are implemented with plain
css and not using Bootstrap.
There are also added a series of components that allow you
to create HTML tags like ``<nav>`` and ``<footer>`` that refer to the
page object(the base.html file) or `<div>` with particular set of
attributes like Overlay, or special functionalities like 
Carousel. The last two can be used within a Container and a 
Section respectively; while the ``<nav>`` and ``<footer>`` components are
part of a Page.
there is the possibility to extend the CSS files and add 
JS functionality to the page thanks to the fact that every 
object derive from the class CSS at least so they all have an
id tag and Css and Js files can be added in the db.
the Js files point to Pages.


## ROADMAP OF IMPLEMENTATION ##
#### layout #
[x] breakpoints
[x] containers
[x] grid
[x] columns
[x] gutters
[x] utilities
[x] z-index
[x] section
[x] page

#### forms #
[ ] form control
[ ] select
[ ] checks a radios
[ ] range
[ ] input goups
[ ] floating labels
[ ] layout
[ ] validation

#### components #
[ ] accordion
[ ] alerts
[ ] badge
[ ] breadcrumb
[ ] buttons
[ ] buttons group
[x] card
[ ] carousel
[ ] close button
[ ] collapse
[ ] drop down
[ ] list group
[ ] modal
[ ] nav e tabs
[ ] navbar
[ ] offcanvas
[ ] pagination
[ ] popovers
[ ] progess
[ ] scrollpy
[ ] spinners
[ ] toast
[ ] tooltips
[x] overlay
     

# helpers 
[ ] clearfix
[x] position
[x] visually hidden 
[x] _stretched link (OVERLAY COMPONENT)

# utilities 
[x] Background
[x] borders
[x] colors
[x] display
[x] Flex
[ ] interactions
[x] overflow
[x] position
[x] shadows
[x] sizing
[x] spacing
[x] text
[x] vertical align
[x] visibility




### How to 


# create a new Page 
1. create a Page object
2. create a Section object pointing to the name 
    page
3. restart the server if necessary

# create a journal like page 
1. create the articles, divided in paragraphs
2. insert the content text created in two 
    containers
3. set containers to a section and make its
    direction to row



### Apps.py 


apps.py contain app configuration, it is called two times 
in Acms. the ready method is overridden to create urls in 
urlpatterns list (contained in urls.py) in order to create 
the urls that will allow the user to go around the website. 
since this is a config file is runned at the ``runserver`` 
command; in the ready method we import all we need to use
it is done in the method so we are sure everything is loaded 
before creating the urls

### Models 


    #NB# to implement a one to many relationship in django the 
        MANY have to point to the one, its not possible for the
        ONE to have a list of the many

#### ManyToMany relationship
    class A:
        ...
    
    class B:
        ...
        relationship = ManyToMany(A, )

    class A can have many class B objects
    and 
    class B can be pointed by many class A objects
    they can be accesed by:
    b.As.all()      >> an 's' is added after the name of the class
    a.b_set.all()

#### GenericForeignKey
Django offers a special way of referencing any model 
in the project called GenericForeignKey.
Generic foreign keys are part of the Content Types 
framework built into Django. 
The content type framework is used by Django itself to
keep track of models. 
This is necessary for some core capabilities such as 
migrations and permissions.

    To implement a many-to-many relation using 
    GenericForeignKey, you need to manually create a model 
    to connect A e B[Generic Foreign Key by realpython](https://realpython.com/modeling-polymorphism-django-python/#generic-foreign-key)

#### organization of the models in the file system
    models
    ├── ___init__.py
    ├── abstract
    │   └── abstract.py
    ├── components
    │   ├── article.py
    │   ├── button.py
    │   ├── card.py
    │   ├── footer.py
    │   ├── navbar.py
    │   └── overlay.py
    ├── content
    │   ├── image.py
    │   ├── link.py
    │   └── text.py
    ├── layout
    │   ├── container.py
    │   ├── grid.py
    │   └── section.py
    └── pages.py


## CSS
is an ABSTRACT class containing all the parameters that
bootstrap allow you to control, 
the parameters 

## Flex
is another ABSTRACT class that let you to control the 
parameters that bootstrap allow you to set.

## Page
the page model, every page contains a certain number
of sections, every page CAN point to a navbar and a 
footer in order to insert it in the page, this allows 
you to create particular pages in the site like landing 
pages or 404 pages
EVERY TIME A NEW PAGE IS ADDED THE SERVER MUST BE RESTARTED
THIS IS BECAUSE THE URLPATTERN LIST IN urls.py IS UPDATED 
WHEN THE SERVER START

## Section
every section group every other layout block
wether it is a grid(row+cols) or a goups of container etc...
the sections can be ordered
ALL THE SECTIONS ARE STACKED VERTICALLY
AND SPAN THE ENTIRE VIEW-WIDTH AND can span the 
entire VIEW-HEIGHT(set 100 for the height parameter) or
adjust to the containers it have (leave blank)
the sections contain groups of container, the section can 
organize containers both vertically and orizontally. 
depending from the display direction parameter when the 
display parameter is set to flex. it is preferable to use
flex functionalities to position content in the sections
the breakpoint parameter is set to function when the 
display direction parameter is set to row, it make the 
content disposed in a column at the breakpoint and up
WE SHOULD AIM TO MINIMIZE THE NUMBER OF SectionS PER PAGE
sections point to pages with ForeignKey creating a 
one to many relationship, one Page, many Sections.
every sections point to one page.

## Container 
allow to group content wether it is text, images, 
videos, canvas, etc..
containers can be used like thumbnails or 
stacked orizontally to create two "columns" 
containing a series of content stacked vertically
obtaining a "mosaic grid".

otherway to insert a proper grid :

## Grid
it is a class that is pointed by Containers or other 
components 
it organize the content in a grid using css grid system


## Navbar

## Footer

## CONTENTS
### Text
text objects contains metadata about the text like 
the data they were created, the author etc
text are pointed by Containers and Grids
so it can be displayed in two different part of the site


### Image
it is pointed by the containers or grids
so it can be displayed in different part of the site but the 
possibility to order them in the page is more difficult. 
usually is indicated to add the in a Container and order the 
Containers once the are part of a Section

### Link

## Templates
    templates
    ├── Acms
    │   ├── base.html
    │   ├── button.html
    │   ├── card.html
    │   ├── container.html
    │   ├── footer.html
    │   ├── grid.html
    │   ├── link.html
    │   ├── navbar.html
    │   ├── overlay.html
    │   ├── section.html
    │   └── workspace.code-workspace
    └── admin
        ├── app_list.html
        ├── base_site.html
        ├── change_form.html
        └── image_form.html

## Admin 

every object is rapresented in admin panel apart for 
abstract objects like CSS and Flex.
https://docs.djangoproject.com/en/4.0/ref/contrib/admin/
the attributes of the admin objects that are set are:
THEY ALL ACCEPT TUPLES OF N ELEMENTS
- list_display:  used to list the parameters in columns
    of the list of the objects of the model
    for types of values can be used in the
    tuple:
    1. name of a model field
    2. a function defined in the model with the
        decorator '@admin.display()', the function
        act on the obj passed as a parameter.
    3. a string created by a function like before
        with the obj ModelAdmin properties
    4. a string created by a function like before
        with the self parameter indicating the model
        itself so having acce to all of its parameters
    5. the decorator can be use also with @property

- fields    :  it refers to the form used to create an
            object, it include a series of 
            attributes. if this is not defined ALL 
            attributes are listed. this option should 
            not be confused with the 'fields' 
            dictionary key in the 'fieldsets' option

- fieldsets :  it control the layout of admin 'add' and
            'change' pages, the forms used to create 
            objects. it is a tuple of tuples. 
            In each internal tuple a string is the 
            first element, its the title of the group
            of attributes, while the second element of
            the tuple is a dictionary of:
    - classes : used to define behavior, ACCEPT
                a tuple of string elements. to
                collapse the options:
                ('collapse',)
                or to give it extra space:
                ('wide')
                these are CSS classes applied to
                the fieldset
    - fields  : its a tuple containing more
                attributes that can be set
                it is like using the fields
                explained before.
    - description:is a string containing extra text 
                displayed a the to of each fieldset
                it can contain HTML elements

- exclude   :  it refers to the form used to create an
            object, it exclude a series of 
            attributes
- list_display_links: tuples of the properties that should be
                    links to the change page of the object
                    refered by the admin class
- list_filter: activate filters in the right sidebar of the
            change list page. the tuple it accept should 
            contain one the following types:
    - > a field name
    - > a class created using SimpleListFilter from admin
    - > a touple containing both of the options above
- search_fields: activate a searchbar 




## Views 

views are used to serve the base.html and populate with the 
data, passed as context dict, from the Page object requested

in views WILL BE implemented all the api functions that 
allow to look for specific piece of content, modify it, and
store new content. 
TO BE DECIDED:
will this API be available only to custom admin implemented
through auth native of django or not

    
## Urls 

urls are handled thanks to three overridden methods, 

the first is defined when the application start, it is a 
method called 'ready()' defined in the apps.py file, it scan all
objects Page in the db and add them in the urlpatterns list
defined in urls.py

the second method is 'save()' and is overridden in the model of
Page in the file pages.py in the models folder, it takes the 
name and the url of the page and update the urlpatterns list
then call the save method of the parent class.

finally the third is the override of the delete method of the
Page object, it takes the list compare the name of the URLPattern
objects stored in urlpatterns and the url of the object deleted
the it delete the URLPattern object from the list and call the
super.delete() method













