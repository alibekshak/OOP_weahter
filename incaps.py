import time

class Kettle:
    def turn_on(self):
        for i in range(1, 12):
            if i == 2:
                self.__boil()
            elif i == 3:
                self.__chek_tempr()
            elif i == 6:
                self.__beep()
            elif i == 8:
                self.__turn_off()
            time.sleep(2)

    def __boil(self):
        print("Разогревание воды")

    def __chek_tempr(self):
        print("Проверяем температуру воды")

    def __beep(self):
        print("Подаем звукавой сигнал")

    def __turn_off(self):
        print("Отключение")


# - __ делает методы приватным(ограничение доступа)


my_k = Kettle()
my_k.turn_on()

