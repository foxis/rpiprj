#~/usr/bin/python

import qrcode
import qrcode.image.svg
import uuid
import sys
import sqlite3

def main():
    with sqlite3.connect("mydata.sql") as db:
        cursor = db.cursor()
        
        count = int(sys.argv[1])
        ball = int(sys.argv[2])
        cursor.execute("CREATE TABLE IF NOT EXISTS ids(id VARCHAR(128) PRIMARY KEY, valid INTEGER, ball INTEGER)")
        for _ in range(count):
            id = str(uuid.uuid1())
            name = ["basketball-", "valleyball-", "football-"][ball]
            print "generated ", name, "id:", id
            qr = qrcode.make(id, image_factory=qrcode.image.svg.SvgImage)
            with open(name + id + ".svg", "w") as f:
                qr.save(f)

            cursor.execute("INSERT INTO ids(id, valid, ball) VALUES(\"{}\", 1, {})".format(id, ball))
        db.commit()


if __name__ == "__main__":
    main()
