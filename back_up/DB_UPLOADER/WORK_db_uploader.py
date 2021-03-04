import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","grafolWEo.settings")
django.setup()

from user.models import *

CSV_PATH_PRODUCTS = './1_category.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    


''' './1_category.csv'
    for row in data_reader :
        C1 = Category.objects.create( id = row[0], name = row[1] )
'''

''' './2_tag.csv'
    for row in data_reader :
        T1 = Tag.objects.create( id = row[0], name = row[1] )
'''

''' './3_category_tag.csv'
    for row in data_reader :
        C1 = CategoryToTag.objects.create( category_id = row[0], tag_id = row[1] )
'''

''' './4_Artworks.csv'
    for row in data_reader :
        W1 = Work.objects.create( id = row[0], user_id = row[1], category_id = row[2], title = row[3], views = row[4] )
'''

''' './5_art_image.csv'
    for row in data_reader :
        if row[0] :
            id = row[0]
            WorkImage.objects.create( work_id = row[0], image_url = row[2] )
        else :
            WorkImage.objects.create( work_id = id, image_url = row[2] )
'''

''' './7_color.csv'
    for row in data_reader :
        ThemeColor.objects.create( id = row[0], name = row[1] )
'''

''' './6_wal_image.csv'
    for row in data_reader :
        WallpaperImage.objects.create( work_id = row[0], themecolor_id = row[1], download_count = row[2], image_url = row[3] )
'''

''' './8_tag_artworks.csv'
    for row in data_reader :
        WorkToTag.objects.create(tag_id = row[0], work_id = row[1] )
'''

''' './9_likeit_kinds.csv'
    for row in data_reader :
        LikeItKind.objects.create( name = row[1] )
'''

''' './10_likeit.csv'
    for row in data_reader :
        LikeIt.objects.create( user_id = row[0], work_id = row[1], like_it_kind_id = row[2] )
'''
