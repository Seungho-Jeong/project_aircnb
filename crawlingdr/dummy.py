import random
import csv
import numpy

from faker import Faker

fake = Faker("ko_KR")

# 교통편의 설명용 난수
ran1 = random.randrange(5,60,5)
ran2 = random.randrange(5,60,5)
ran3 = random.randrange(5,60,5)

a = f"공항에서 버스로 {ran1}분 거리에 있고 "
b = f"걸어서 {ran2}분 거리에 버스정거장이 있으며 "
c = f"아름다운 해안도로가 도보로 {ran3}분 거리에 있습니다.\n"

# 숙소 설명
d = "\n숙소\n"
e = f"인테리어도 좋고 모든게 완벽했습니다. "
ff = f"코로나로 비대면 체크인 체크아웃이었지만 부족함은 없었습니다. "
g = f"또 가고 싶어요. "
h = f"가격 대비 최고의 숙소입니다! "
ii = f"주변에 걸어서 갈만한 시설은 없습니다. "

# 게스트 이용시설 설명
k = "\n게스트 이용가능 공간 및 시설\n"
l = f"너무 만족했습니다. 잘 쉬다 갑니다. "
m = f"그냥 최고였습니다. "
n = f"너무 편안하고 세심하게 꾸며주신 느낌이 나서 좋았습니다. "
o = f"숙소 너무 예쁘고 감성 돋아요 ㅠㅠ "
p = f"사진보다 더 예쁘고 깔끔했어요! "

# 기타 주의사항 설명
q = "\n기타 주의사항\n"
r = f"제주도를 다시 온다해도 여길 오겠어요 ㅠㅠ "
s = f"이때까지 머물렀던 숙소 중에 제일 좋았어요! "
t = f"잘 쉬었다 갑니다 :) "
u = f"제 여행경험 중 역대급으로 좋은 숙소였어요! "
v = f"조용한 마을에 있어서 안락하게 잘 쉬다 갑니다 :) "

# CSV 파일 쓰기
with open("./desc.csv", "w", newline ="") as f:
    description = csv.writer(f)

# 각 설명사항에 대한 랜덤 선택
    for i in range(10000):
        stay     = fake.random_elements(elements=(e, ff, g, h, ii), length = 2, unique = True)
        facility = fake.random_elements(elements=(l, m, n, o, p), length = 2, unique = True)
        etc      = fake.random_elements(elements=(r, s, t, u, v), length = 2, unique = True)
        comb = str(stay[0]) + str(stay[1]) + str(facility[0]) + str(facility[1]) + str(etc[0]) + str(etc[1])
        description.writerow([comb])
        print(comb)
#
#hosts = ["4", "10", "12", "13", "17", "21", "24", "25", "29", "30"]
#
#with open("./housename.csv", "w", newline ="") as f:
#    stay_id = csv.writer(f)
#
#    for i in range(200):
#        housename = fake.word()
#        stay_id.writerow([housename])
#        print(housename)

#stay_num    = 200
#amenity_num = 6
#
#lst = [1,2,3,4,5,6,7,8,9,10,11,12]
#
#with open("./new_stay_amenities.csv", "w", newline = "") as f:
#    result = csv.writer(f)
#
#    for amenity in range(stay_num):
#        amenities = fake.random_elements(elements=lst, length = 8,  unique=True)
#        for amenity in amenities:
#            result.writerow([amenity])
#            print(amenity)

#with open("./new_rules_many2many.csv", "w", newline = "") as f:
#    result = csv.writer(f)
#
#    a = numpy.repeat(range(1,201), 4)
#
#    for i in a:
#        result.writerow([i])
#        print(i)


#with open("./star1.csv", "w", newline="") as f:
#    result = csv.writer(f)
#
#    for i in range(1, 10001):
#        star = random.randrange(4,6,1)
#        result.writerow([star])
