class Car:

    def __init__(self):
        # initは初期化
        # 最初に燃料と走行距離を初期化
        self.fuel = 0
        self.distance = 0

    # 燃料を補給する関数
    def charge(self, fuel):
        self.fuel += fuel

    def run(self):
        # まずは燃料があるか確認
        if self.fuel > 0:
            self.fuel -= 1
            self.distance += 1
            print("走行距離は{}です".format(self.distance))
        else:
            # 燃料がない場合の処理のブロック
            print("燃料がありません")


car = Car()
print("燃料：{}".format(car.fuel))
print("走行距離：{}".format(car.distance))

# 燃料を入れなかった場合
car.run()
# 燃料を5入れた場合
car.charge(5)
# ここで走らせる
car.run()

print("燃料：{}".format(car.fuel))
print("走行距離：{}".format(car.distance))
