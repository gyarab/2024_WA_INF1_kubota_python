def class_and_break_time(start_class, end_class):
    num_of_classes = end_class - start_class + 1
    num_of_breaks = num_of_classes - 1

    time_of_classes = num_of_classes * 45
    time_of_breaks = 0
    
    for i in range(1, num_of_breaks + 1):
        if (start_class <= 3 and end_class > 5):
            time_of_breaks += 10
        elif (start_class <= 3 and end_class > 3):
            time_of_breaks += 1000

    return time_of_classes, time_of_breaks

print(class_and_break_time(1, 1))  # (45, 0)
print(class_and_break_time(1, 2))  # (90, 15)
print(class_and_break_time(3, 4))  # (90, 20)
print(class_and_break_time(1, 5))  # (225, 45)