from apk import db
from apk.albums.model import Album
import json

db.drop_all()
print("Dropping...")
db.create_all()
print("Creating...")

print("Seeding...")

album1 = Album(album_name="Volume Alpha",songs=json.dumps([
            {
                "title":"Key",
                "plays":"59,041,326",
                "length":"1:05"
            },
            {
                "title":"Door",
                "plays":"25,069,453",
                "length":"1:51"
            },
            {
                "title":"Subwoofer Lullaby",
                "plays":"81,001,484",
                "length":"3:28"
            },
            {
                "title":"Death",
                "plays":"14,822,064",
                "length":"0:41"
            },
            {
                "title":"Living Mice",
                "plays":"40,270,199",
                "length":"2:57"
            },
            {
                "title":"Moog City",
                "plays":"36,665,523",
                "length":"2:40"
            },
            {
                "title":"Haggstrom",
                "plays":"42,575,393",
                "length":"3:24"
            },
            {
                "title":"Minecraft",
                "plays":"88,978,653",
                "length":"4:14"
            },
            {
                "title":"Oxygène",
                "plays":"23,170,730",
                "length":"1:05"
            },
            {
                "title":"Équinox",
                "plays":"23,814,632",
                "length":"1:54"
            },
            {
                "title":"Mice On Venus",
                "plays":"56,242,269",
                "length":"4:41"
            },
            {
                "title":"Dry Hands",
                "plays":"43,416,120",
                "length":"1:08"
            },
            {
                "title":"Wet Hands",
                "plays":"69,351,795",
                "length":"1:30"
            },
            {
                "title":"Clark",
                "plays":"30,247,864",
                "length":"3:11"
            },
            {
                "title":"Chris",
                "plays":"20,180,770",
                "length":"1:27"
            },
            {
                "title":"Thirteen",
                "plays":"11,902,256",
                "length":"2:56"
            },
            {
                "title":"Excuse",
                "plays":"20,816,189",
                "length":"2:04"
            },
            {
                "title":"Sweden",
                "plays":"136,307,722",
                "length":"3:35"
            },
            {
                "title":"Cat",
                "plays":"27,793,406",
                "length":"3:06"
            },
            {
                "title":"Dog",
                "plays":"17,322,567",
                "length":"2:25"
            },
            {
                "title":"Danny",
                "plays":"27,857,841",
                "length":"4:14"
            },
            {
                "title":"Beginning",
                "plays":"23,275,659",
                "length":"1:42"
            },
            {
                "title":"Droopy Like Ricochet",
                "plays":"14,258,655",
                "length":"1:36"
            },
            {
                "title":"Droopy Likes Your Face",
                "plays":"16,261,735",
                "length":"1:56"
            }
        ])
    )
album2 = Album(album_name="Volume Beta",songs=json.dumps([
            {
                "title":"Ki",
                "plays":"8,803,276",
                "length":"1:32"
            },
            {
                "title":"Alpha",
                "plays":"11,729,785",
                "length":"10:03"
            },
            {
                "title":"Dead Voxel",
                "plays":"11,715,437",
                "length":"4:56"
            },
            {
                "title":"Blind Spots",
                "plays":"12,964,500",
                "length":"5:32"
            },
            {
                "title":"Flake",
                "plays":"8,382,632",
                "length":"2:50"
            },
            {
                "title":"Moog City 2",
                "plays":"24,175,364",
                "length":"3:00"
            },
            {
                "title":"Concrete Halls",
                "plays":"6,376,931",
                "length":"4:14"
            },
            {
                "title":"Biome Fest",
                "plays":"10,403,643",
                "length":"6:18"
            },
            {
                "title":"Mutation",
                "plays":"17,975,037",
                "length":"3:05"
            },
            {
                "title":"Haunt Muskie",
                "plays":"11,361,558",
                "length":"6:01"
            },
            {
                "title":"Warmth",
                "plays":"7,298,216",
                "length":"3:59"
            },
            {
                "title":"Floating Trees",
                "plays":"12,272,587",
                "length":"4:04"
            },
            {
                "title":"Aria Math",
                "plays":"31,761,427",
                "length":"5:10"
            },
            {
                "title":"Kyoto",
                "plays":"7,214,840",
                "length":"4:09"
            },
            {
                "title":"Ballad Of The Cats",
                "plays":"6,764,918",
                "length":"4:35"
            },
            {
                "title":"Taswell",
                "plays":"9,767,699",
                "length":""
            },
            {
                "title":"Beginning 2",
                "plays":"12,335,162",
                "length":"2:56"
            },
            {
                "title":"Dreiton",
                "plays":"8,815,784",
                "length":"8:17"
            },
            {
                "title":"The End",
                "plays":"4,996,815",
                "length":"15:04"
            },
            {
                "title":"Chirp",
                "plays":"13,961,620",
                "length":"3:06"
            },
            {
                "title":"Wait",
                "plays":"12,006,089",
                "length":"3:54"
            },
            {
                "title":"Mellohi",
                "plays":"16,085,806",
                "length":"1:38"
            },
            {
                "title":"Stal",
                "plays":"21,257,490",
                "length":"2:32"
            },
            {
                "title":"Strad",
                "plays":"10,778,912",
                "length":"3:08"
            },
            {
                "title":"Eleven",
                "plays":"7,684,789",
                "length":"1:11"
            },
            {
                "title":"Ward",
                "plays":"5,413,017",
                "length":"4:10"
            },
            {
                "title":"Mall",
                "plays":"8,437,468",
                "length":"3:18"
            },
            {
                "title":"Blocks",
                "plays":"5,699,420",
                "length":"5:43"
            },
            {
                "title":"Far",
                "plays":"9,244,438",
                "length":"3:12"
            },
            {
                "title":"Intro",
                "plays":"10,537,838",
                "length":"4:36"
            }
        ]
    ))

db.session.add_all([album1,album2])

db.session.commit()
print("\nCompleted. Database seeded")