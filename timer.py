import time
from win10toast import ToastNotifier

ONE_YEAR_TIMER =365 * 24 * 60 * 60
ONE_DAY_TIMER =24 *60 * 60
ONE_MINUTE_TIMER =60

MESSAGE_FOR_1_YEAR ="Таймер на 1 год завершен!"
MESSAGE_FOR_1_DAY ="Таймер на 1 день завершен!"
MESSAGE_FOR_1_MINUTE ="Таймер на 1 минуту завершен!"
MESSAGE_FOR_DONE ="Выполнено!"

song = AudioSegment.from_wav("zvonok-budilnika-32888.wav")
play(song)
def timer():
    print("Привет,эта программа создает таймер с указаным значением")
    print("Также ты можешь выбрать уже заранее настроеные таймеры")
    print("")
    print("Ты можешь:")
    print("1)Поставить Таймер на год")
    print("2)Поставить Таймер на день")
    print("3)Поставить Таймер на 1 минуту")
    print("4)Либо ты можешь задать свои параметры")
    print("")
    user_option =int(input("Какую опперацию ты выберешь? >>>>>"))
    try:
        if user_option <1 or user_option >4:
            print("Вы выбрали не ту опперацию")
            time.sleep(10)
            return
        else:
            START_TIME = time.time()
            if user_option ==1:
                while True:
                    remaining_time_1 =ONE_YEAR_TIMER - (time.time() - START_TIME)
                    print(f"До окончания таймера в 1 год осталось: {remaining_time_1} секунд")
                    time.sleep(0.1)
                    if remaining_time_1 <=0:
                        ToastNotifier().show_toast(MESSAGE_FOR_DONE,MESSAGE_FOR_1_YEAR)
                        break
            elif user_option ==2:
                while True:
                    remaining_time_2 = ONE_DAY_TIMER - (time.time() - START_TIME)
                    print(f"До окончания таймера в 1 день осталось: {remaining_time_2} секунд")
                    time.sleep(0.1)
                    if remaining_time_2 <= 0:
                        ToastNotifier().show_toast(MESSAGE_FOR_DONE,MESSAGE_FOR_1_DAY)
                        break
            elif user_option ==3:
                while True:
                    remaining_time_3 = ONE_MINUTE_TIMER - (time.time() - START_TIME)
                    print(f"До окончания таймера в 1 минуту осталось: {remaining_time_3} секунд")
                    time.sleep(0.1)
                    if remaining_time_3 <= 0:
                        ToastNotifier().show_toast(MESSAGE_FOR_DONE,MESSAGE_FOR_1_MINUTE)
                        break
            elif user_option ==4:
                user_timer =int(input("Отлично!Теперь напиши сюда длительность твоего таймера в секундах. >>>>"))
                start_time_1 =time.time()
                if user_timer <1 or user_timer ==0:
                    print("Таймер не может быть равен 0 или меньше")
                    time.sleep(10)
                    return
                else:
                    while True:
                        remaining_time_4 = user_timer - (time.time() - start_time_1)
                        print(f"До окончания таймера на {user_timer} осталось: {remaining_time_4} секунд")
                        time.sleep(0.1)
                        if remaining_time_4 <= 0:
                            ToastNotifier().show_toast(MESSAGE_FOR_DONE, f"Ваш таймер в {user_timer} секунд завершен")
                            break
            else:
                print("К сожалению,что-то пошло не так :(")
                time.sleep(10)
                return
    except ValueError:
        print("Вы ввели недопустимые значения")
    finally:
        print("Произошла неизвестная ошибка")
if __name__ == "__main__":
    timer()