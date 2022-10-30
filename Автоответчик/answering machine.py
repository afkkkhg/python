from ans_machine import * # подключение файла
while True:
    a = input()
    if a.lower() == 'stop': # как только будет введено стоп, цикл остановится
        break
    main(a) # передаешь а в фунцйию мейн