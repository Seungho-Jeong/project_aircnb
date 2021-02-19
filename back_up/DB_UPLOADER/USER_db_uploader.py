import os
import django
import csv
import sys
import bcrypt

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grafolWEo.settings")
django.setup()

from user.models import User

CSV_PATH_USERS = "./user_rawdata.csv"

with open(CSV_PATH_USERS) as in_file:
    data_reader = csv.reader(in_file)   # CSV 관련 함수는 추가 공부(Googling) 필요
    next(data_reader, None)             # 첫 번째줄(필드명) 출력안되게 하는 코드
    for row in data_reader:
#       if row[0] != "":                # 아래처럼 표현하는 것이 코드 길이가 짧음
        if row[0]:
                                        # id: 0         user_name: 1        email: 2    mobile: 3
                                        # password: 4   profile_image: 5    short_introduce: 6
            User.objects.create(
                id                  = row[0],
                user_name           = row[1],
                email               = row[2],
                mobile              = row[3],
                password            = bcrypt.hashpw(row[4].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
                profile_image_url   = row[5],
                introduction        = row[6]
            )
++
