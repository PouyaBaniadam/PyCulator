import decimal
import math
import os
import random
import string
import sys
from decimal import Decimal
from math import log10, sin, cos, tan, sqrt, factorial
from tkinter import *

import matplotlib.pyplot as plt
import numpy as np


def resource_path(relative_path):
    global base_path
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("Assets")

    return os.path.join(base_path, relative_path)


def cal_screen():
    def complex_equation(phrase):
        global answer_for_later
        data = phrase
        all_operators = ("^", "*", "/", "+", "-")
        all_parenthesis = ("(", ")")
        all_first_alphabet_of_sin_cos_tan_cot_log = ("s", "c", "t", "l")

        temp = []
        for o in data:
            temp.append(o)

        if temp[-1] == "n" or temp[-1] == "s" or temp[-1] == "s" or temp[-1] == "g":
            temp.append("(")
            temp.append("0")

        temp.append("+")
        temp.append("0")

        temp_index_0 = -1
        for remaker_0 in temp:
            temp_index_0 += 1

            if remaker_0 == "n" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

        temp.append("+")
        temp_index_1 = -1
        for remaker_1 in temp:
            temp_index_1 += 1

            if remaker_1.isdigit():

                if temp[temp_index_1 + 1] in all_first_alphabet_of_sin_cos_tan_cot_log:
                    temp.insert(temp_index_1 + 1, "(")

        temp.pop(-1)

        temp_index_2 = -1
        for remaker_2 in temp:
            temp_index_2 += 1

            if remaker_2 == "n" or remaker_2 == "s" or remaker_2 == "t" or remaker_2 == "g":

                if temp[temp_index_2 + 1] == "-" or temp[temp_index_2 + 1].isdigit():
                    temp.insert(temp_index_2 + 1, "(")

        temp_index_4 = -1
        for remaker_4 in temp:
            temp_index_4 += 1

            if remaker_4 == "(":
                if temp[temp_index_4 - 1] in all_parenthesis:
                    temp.insert(temp_index_4, "*")

        temp_index_5 = -1
        for remaker_5 in temp:
            temp_index_5 += 1

            if remaker_5 == "(":
                if temp[temp_index_5 - 1].isdigit():
                    temp.insert(temp_index_5, "*")

        temp_index_6 = -1
        for remaker_6 in temp:
            temp_index_6 += 1

            if remaker_6 == "(":
                if temp[temp_index_6 - 1] == "*" and temp[temp_index_6 - 2] == "(":
                    temp.insert(temp_index_6 - 1, "1")

        temp_index_7 = -1
        for remaker_7 in temp:
            temp_index_7 += 1

            if remaker_7 == ")":
                if temp[temp_index_7 + 1] in all_first_alphabet_of_sin_cos_tan_cot_log:
                    temp.insert(temp_index_7 + 1, "*")

        temp_index_8 = -1
        for remaker_8 in temp:
            temp_index_8 += 1

            if remaker_8 == "√":
                if temp[temp_index_8 - 1].isdigit():
                    temp.insert(temp_index_8, "*")

        temp_index_10 = -1
        for remaker_10 in temp:
            temp_index_10 += 1

            if remaker_10 == "!":
                if temp[temp_index_10 + 1] not in all_operators:
                    temp.insert(temp_index_10 + 1, "*")

        temp_index_11 = -1
        for remaker_11 in temp:
            temp_index_11 += 1

            if remaker_11 == "!":
                if temp[temp_index_11 + 1] == "*" and temp[temp_index_11 + 2] == ")":
                    temp.pop(temp_index_11 + 1)

        if temp[0] == "*":
            temp.insert(0, "1")

        data = "".join(map(str, temp))
        del temp

        if data[0] == "-":
            negative_to_be_added_later = "-"
            data = data[1:]

        else:
            negative_to_be_added_later = ""

        if data[0] == "+":
            posetive_to_be_added_later = "-+"
            data = data[1:]

        else:
            posetive_to_be_added_later = ""

        data = data + "+"
        data_list = []
        all_operators = ("^", "*", "/", "+", "-")

        temp_num_holder = ""
        temp_counter = -1

        for data_list_adder in data:
            temp_counter += 1

            if data_list_adder.isdigit() or data_list_adder == ".":
                temp_num_holder = temp_num_holder + data_list_adder

            elif data_list_adder == "s":
                if data[temp_counter - 1] != "o":
                    data_list.append("sin")

            elif data_list_adder == "c":
                if data[temp_counter + 2] == "s":
                    data_list.append("cos")

                if data[temp_counter + 2] == "t":
                    data_list.append("cot")

            elif data_list_adder == "t":
                if data[temp_counter - 1] != "o":
                    data_list.append("tan")

            elif data_list_adder == "l":
                data_list.append("log")

            elif data_list_adder == "-":
                if data[temp_counter - 1] in all_operators:
                    temp_num_holder = data_list_adder + temp_num_holder
                else:
                    data_list.append(temp_num_holder)
                    data_list.append(data_list_adder)
                    temp_num_holder = ""

            elif data_list_adder == "+":
                if data[temp_counter - 1] in all_operators:
                    temp_num_holder = data_list_adder + temp_num_holder
                else:
                    data_list.append(temp_num_holder)
                    data_list.append(data_list_adder)
                    temp_num_holder = ""


            elif data_list_adder in all_operators:
                data_list.append(temp_num_holder)
                data_list.append(data_list_adder)
                temp_num_holder = ""


            elif data_list_adder == "(":
                if temp_counter == 0:
                    data_list.append("(")

                elif data[temp_counter - 1] == "-" and data[temp_counter - 2] in all_operators:
                    data_list.append("-")
                    data_list.append("(")
                    temp_num_holder = ""

                else:
                    data_list.append("(")


            elif data_list_adder == ")":
                if data[temp_counter - 1].isdigit():
                    if len(temp_num_holder) != 0:
                        data_list.append(temp_num_holder)
                        data_list.append(")")
                        temp_num_holder = ""

                    else:
                        data_list.append(")")

                elif data[temp_counter - 1] == ")":
                    data_list.append(")")

                elif data[temp_counter - 1] == "!":
                    data_list.append(")")


            elif data_list_adder == "√":
                data_list.append("√")


            elif data_list_adder == "!":
                if len(temp_num_holder) != 0:
                    data_list.append(temp_num_holder)
                    data_list.append("!")
                    temp_num_holder = ""

                else:
                    data_list.append("!")

        if len(negative_to_be_added_later) == 1:
            if "(" in data_list[0]:
                data_list.pop(0)
                data_list.insert(0, "-")
                data_list.insert(1, "(")

            else:

                data_list[0] = "-" + data_list[0]
                data_list = data_list[0: -1]

        else:
            data_list = data_list[0: -1]

        if data_list[-1] == "+":
            data_list.pop(-1)

        temp_data_list = []
        for _ in data_list:
            if _ == '':
                pass

            else:
                temp_data_list.append(_)

        data_list = temp_data_list.copy()
        del temp_data_list

        temp_counter = -1
        for data_list_remaker in data_list:
            temp_counter += 1

            if data_list_remaker == "(":
                if data_list[temp_counter + 1] == "-":
                    data_list[temp_counter + 1: temp_counter + 3] = [f"-{data_list[temp_counter + 2]}"]

        temp_index = -1
        for plus_zero_adder in data_list:
            temp_index += 1

            if plus_zero_adder == ")":
                if data_list[temp_index + 1] == ")":
                    data_list.insert(temp_index + 1, "+")
                    data_list.insert(temp_index + 2, "0")

        temp_index = -1
        for open_parenthesis_adder_to_begininig in data_list:
            temp_index += 1

            if open_parenthesis_adder_to_begininig == ")":
                if "(" not in data_list[temp_index:: -1]:
                    data_list.insert(0, "(")

        if data_list[0] == "-":
            if data_list[1] == "(":
                data_list.pop(0)
                data_list.insert(0, "-1")
                data_list.insert(1, "*")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-sin":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "sin")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-cos":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "cos")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-tan":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "tan")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-cot":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "cot")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-log":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "log")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        open_count = 0
        close_count = 0
        for _ in data_list:
            if _ == "(":
                open_count += 1

            if _ == ")":
                close_count += 1

        if open_count > close_count:
            for i in range(open_count - close_count):
                data_list.append(")")

        if close_count > open_count:
            for j in range(close_count - open_count):
                data_list.insert(0, "(")

        counter = 0
        for i in data_list:
            if i == "(":
                counter += 1

        for u in range(counter):
            temp_index = -1
            end_point = 0
            for _ in data_list:
                temp_index += 1

                if _ == ")":
                    end_point = temp_index
                    break

            temp_index = 0
            start_point = 0
            for __ in data_list[end_point:: -1]:
                temp_index += 1

                if __ == "(":
                    start_point = end_point - temp_index + 1
                    break

            calculate_zone = data_list[start_point + 1: end_point]

            power_count = 0
            times_count = 0
            fraction_count = 0
            plus_count = 0
            mines_count = 0
            parenthesis_count = 0
            sqrt_count = 0
            fact_count = 0

            for how_many_of_each_operators in calculate_zone:
                if how_many_of_each_operators == "^":
                    power_count += 1

                if how_many_of_each_operators == "*":
                    times_count += 1

                if how_many_of_each_operators == "/":
                    fraction_count += 1

                if how_many_of_each_operators == "+":
                    plus_count += 1

                if how_many_of_each_operators == "-":
                    mines_count += 1

                if how_many_of_each_operators == "(":
                    parenthesis_count += 1

                if how_many_of_each_operators == "√":
                    sqrt_count += 1

                if how_many_of_each_operators == "!":
                    fact_count += 1

            counter = 0
            for i in data_list:
                if i == "(":
                    counter += 1

            for fact_calculations in range(fact_count):

                fact_index = -1
                for fact_finder in calculate_zone:
                    fact_index += 1

                    if fact_finder.isdigit() or fact_finder == ".":
                        pass

                    if fact_finder == "!":
                        try:
                            temp_answer = int(calculate_zone[fact_index - 1])
                            temp_answer = factorial(temp_answer)

                        except:
                            print("Invalid input!")
                            break

                        calculate_zone[fact_index - 1: fact_index + 1] = [str(temp_answer)]

            for sqrt_calculations in range(sqrt_count):

                sqrt_index = -1
                for sqrt_finder in calculate_zone:
                    sqrt_index += 1

                    if sqrt_finder.isdigit() or sqrt_finder == ".":
                        pass

                    if sqrt_finder == "√":
                        temp_answer = float(calculate_zone[sqrt_index + 1])
                        temp_answer = sqrt(temp_answer)

                        calculate_zone[sqrt_index: sqrt_index + 2] = [str(temp_answer)]

            zero_plus = 0
            to_be_removed_from_the_begining_later_count = 0
            for power_calculations in range(power_count):

                power_index = -1
                for power_finder in calculate_zone:
                    power_index += 1

                    if power_finder.isdigit() or power_finder == ".":
                        pass

                    if power_finder == "^":
                        first_number = calculate_zone[power_index - 1]
                        second_number = calculate_zone[power_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        if "-" in str(first_number) and "." in str(second_number):
                            print("Invalid input!")
                            calculate_zone.clear()
                            break

                        try:
                            temp_answer = first_number ** second_number

                        except decimal.Overflow:
                            print("Over flow!")
                            break

                        if "^" in calculate_zone[power_index + 1:] or "*" in calculate_zone[power_index + 1:] \
                                or "/" in calculate_zone[power_index + 1:] or "+" in calculate_zone[power_index + 1:] \
                                or "-" in calculate_zone[power_index + 1:]:

                            starting_point = power_index - 1
                            ending_point = power_index + 2
                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2


                        else:
                            starting_point = power_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    calculate_zone.pop(0)

            to_be_removed_from_the_begining_later_count = 0
            for times_and_fraction_calculations in range(times_count + fraction_count):

                times_or_fraction_index = -1

                for times_or_fraction_finder in calculate_zone:

                    times_or_fraction_index += 1
                    if times_or_fraction_finder.isdigit() or times_or_fraction_finder == ".":
                        pass

                    if times_or_fraction_finder == "*":
                        first_number = calculate_zone[times_or_fraction_index - 1]
                        second_number = calculate_zone[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        temp_answer = first_number * second_number

                        if "^" in calculate_zone[times_or_fraction_index:] or "*" in calculate_zone[
                                                                                     times_or_fraction_index:] \
                                or "/" in calculate_zone[times_or_fraction_index:] or "+" in calculate_zone[
                                                                                             times_or_fraction_index:] \
                                or "-" in calculate_zone[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            calculate_zone[starting_point: ending_point + 1] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

                    if times_or_fraction_finder == "/":
                        first_number = calculate_zone[times_or_fraction_index - 1]
                        second_number = calculate_zone[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)
                        devision_zero_count = 0
                        try:
                            temp_answer = first_number / second_number
                        except ZeroDivisionError:
                            print("Cant devide to zero !")
                            devision_zero_count += 1

                        if "^" in calculate_zone[times_or_fraction_index:] or "*" in calculate_zone[
                                                                                     times_or_fraction_index:] \
                                or "/" in calculate_zone[times_or_fraction_index:] or "+" in calculate_zone[
                                                                                             times_or_fraction_index:] \
                                or "-" in calculate_zone[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            if devision_zero_count == 0:
                                try:
                                    calculate_zone[starting_point: ending_point + 1] = [str(temp_answer)]
                                except:
                                    print("Can't devide to zero!")
                                    break

                            else:
                                calculate_zone = []

                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    calculate_zone.pop(0)

            x_count = 0
            for plus_and_mines_calculation in range(plus_count + mines_count):

                plus_or_mines_index = -1

                for plus_or_mines_finder in calculate_zone:
                    plus_or_mines_index += 1

                    if plus_or_mines_finder != "-" or plus_or_mines_finder != "+":
                        pass

                    if plus_or_mines_finder == "+":
                        first_number = calculate_zone[plus_or_mines_index - 1]
                        second_number = calculate_zone[plus_or_mines_index + 1]

                        if "^" in calculate_zone[plus_or_mines_index + 1:] or "*" in calculate_zone[
                                                                                     plus_or_mines_index + 1:] \
                                or "/" in calculate_zone[plus_or_mines_index + 1:] or "+" in calculate_zone[
                                                                                             plus_or_mines_index + 1:] \
                                or "-" in calculate_zone[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            calculate_zone[starting_point:] = [str(temp_answer)]

                    if plus_or_mines_finder == "-":
                        first_number = calculate_zone[plus_or_mines_index - 1]
                        second_number = calculate_zone[plus_or_mines_index + 1]

                        if "^" in calculate_zone[plus_or_mines_index + 1:] or "*" in calculate_zone[
                                                                                     plus_or_mines_index + 1:] \
                                or "/" in calculate_zone[plus_or_mines_index + 1:] or "+" in calculate_zone[
                                                                                             plus_or_mines_index + 1:] \
                                or "-" in calculate_zone[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            calculate_zone[starting_point:] = [str(temp_answer)]

            for remover in range(x_count):
                calculate_zone.pop(0)

            if data_list[start_point - 1] == "sin" or data_list[start_point - 1] == "-sin":
                try:
                    calculate_zone = sin(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    print("Invalid input!")
                    break


            elif data_list[start_point - 1] == "cos" or data_list[start_point - 1] == "-cos":
                try:
                    calculate_zone = cos(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    print("Invalid input!")
                    break


            elif data_list[start_point - 1] == "tan" or data_list[start_point - 1] == "-tan":
                try:
                    calculate_zone = tan(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    print("Invalid input!")
                    break


            elif data_list[start_point - 1] == "cot" or data_list[start_point - 1] == "-cot":
                try:
                    calculate_zone = 1 / tan(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    print("Invalid input!")
                    break


            elif data_list[start_point - 1] == "log" or data_list[start_point - 1] == "-log":
                try:
                    calculate_zone = log10(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    print("Invalid input!")
                    break

            else:
                data_list[start_point: end_point + 1] = calculate_zone

        if "(" not in data_list:

            power_count = 0
            times_count = 0
            fraction_count = 0
            plus_count = 0
            mines_count = 0
            sqrt_count = 0
            fact_count = 0

            for how_many_of_each_operators in data_list:
                if how_many_of_each_operators == "^":
                    power_count += 1

                if how_many_of_each_operators == "*":
                    times_count += 1

                if how_many_of_each_operators == "/":
                    fraction_count += 1

                if how_many_of_each_operators == "+":
                    plus_count += 1

                if how_many_of_each_operators == "-":
                    mines_count += 1

                if how_many_of_each_operators == "√":
                    sqrt_count += 1

                if how_many_of_each_operators == "!":
                    fact_count += 1

            for fact_calculations in range(fact_count):

                fact_index = -1
                for fact_finder in data_list:
                    fact_index += 1

                    if fact_finder.isdigit() or fact_finder == ".":
                        pass

                    if fact_finder == "!":
                        try:
                            temp_answer = int(data_list[fact_index - 1])
                            temp_answer = factorial(temp_answer)

                        except:
                            print("Invalid input!")
                            break

                        data_list[fact_index - 1: fact_index + 1] = [str(temp_answer)]

            for sqrt_calculations in range(sqrt_count):

                sqrt_index = -1
                for sqrt_finder in data_list:
                    sqrt_index += 1

                    if sqrt_finder.isdigit() or sqrt_finder == ".":
                        pass

                    if sqrt_finder == "√":
                        try:
                            temp_answer = float(data_list[sqrt_index + 1])
                            temp_answer = sqrt(temp_answer)

                        except ValueError:
                            print("Invalid input!")
                            break

                        data_list[sqrt_index: sqrt_index + 2] = [str(temp_answer)]

            zero_plus = 0
            to_be_removed_from_the_begining_later_count = 0
            for power_calculations in range(power_count):

                power_index = -1
                for power_finder in data_list:
                    power_index += 1

                    if power_finder.isdigit() or power_finder == ".":
                        pass

                    if power_finder == "^":
                        first_number = data_list[power_index - 1]
                        second_number = data_list[power_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        if "-" in str(first_number) and "." in str(second_number):
                            print("Invalid input!")
                            data_list.clear()
                            break

                        try:
                            temp_answer = first_number ** second_number

                        except decimal.Overflow:
                            print("Over flow!")
                            break

                        if "^" in data_list[power_index + 1:] or "*" in data_list[power_index + 1:] \
                                or "/" in data_list[power_index + 1:] or "+" in data_list[power_index + 1:] \
                                or "-" in data_list[power_index + 1:]:

                            starting_point = power_index - 1
                            ending_point = power_index + 2
                            data_list[starting_point: ending_point] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2


                        else:
                            starting_point = power_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    data_list.pop(0)

            to_be_removed_from_the_begining_later_count = 0
            for times_and_fraction_calculations in range(times_count + fraction_count):

                times_or_fraction_index = -1

                for times_or_fraction_finder in data_list:

                    times_or_fraction_index += 1
                    if times_or_fraction_finder.isdigit() or times_or_fraction_finder == ".":
                        pass

                    if times_or_fraction_finder == "*":
                        first_number = data_list[times_or_fraction_index - 1]
                        second_number = data_list[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        temp_answer = first_number * second_number

                        if "^" in data_list[times_or_fraction_index:] or "*" in data_list[times_or_fraction_index:] \
                                or "/" in data_list[times_or_fraction_index:] or "+" in data_list[
                                                                                        times_or_fraction_index:] \
                                or "-" in data_list[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            data_list[starting_point: ending_point + 1] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

                    if times_or_fraction_finder == "/":
                        first_number = data_list[times_or_fraction_index - 1]
                        second_number = data_list[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)
                        devision_zero_count = 0
                        try:
                            temp_answer = first_number / second_number
                        except ZeroDivisionError:
                            print("Cant devide to zero !")
                            devision_zero_count += 1

                        if "^" in data_list[times_or_fraction_index:] or "*" in data_list[times_or_fraction_index:] \
                                or "/" in data_list[times_or_fraction_index:] or "+" in data_list[
                                                                                        times_or_fraction_index:] \
                                or "-" in data_list[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            if devision_zero_count == 0:
                                try:
                                    data_list[starting_point: ending_point + 1] = [str(temp_answer)]
                                except:
                                    print("Can't devide to zero!")
                                    break

                            else:
                                data_list = []

                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    data_list.pop(0)

            x_count = 0
            for plus_and_mines_calculation in range(plus_count + mines_count):

                plus_or_mines_index = -1

                for plus_or_mines_finder in data_list:
                    plus_or_mines_index += 1

                    if plus_or_mines_finder != "-" or plus_or_mines_finder != "+":
                        pass

                    if plus_or_mines_finder == "+":
                        first_number = data_list[plus_or_mines_index - 1]
                        second_number = data_list[plus_or_mines_index + 1]

                        if "^" in data_list[plus_or_mines_index + 1:] or "*" in data_list[plus_or_mines_index + 1:] \
                                or "/" in data_list[plus_or_mines_index + 1:] or "+" in data_list[
                                                                                        plus_or_mines_index + 1:] \
                                or "-" in data_list[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            data_list[starting_point: ending_point] = [temp_answer]
                            data_list.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            data_list[starting_point:] = [temp_answer]

                    if plus_or_mines_finder == "-":
                        first_number = data_list[plus_or_mines_index - 1]
                        second_number = data_list[plus_or_mines_index + 1]

                        if "^" in data_list[plus_or_mines_index + 1:] or "*" in data_list[plus_or_mines_index + 1:] \
                                or "/" in data_list[plus_or_mines_index + 1:] or "+" in data_list[
                                                                                        plus_or_mines_index + 1:] \
                                or "-" in data_list[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            data_list[starting_point: ending_point] = [temp_answer]
                            data_list.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            data_list[starting_point:] = [temp_answer]

            for remover in range(x_count):
                data_list.pop(0)

            final_answer = ""
            if data_list:
                final_answer = data_list[0]

            if final_answer == "+":
                answer_for_later = ""

            else:
                if final_answer == "-0":
                    final_answer = "0"
                    answer_for_later = final_answer

                else:
                    if final_answer == "-0":
                        final_answer = "0"
                        answer_for_later = final_answer

                    else:
                        answer_for_later = final_answer

    def equation():
        global equation_screen
        global button_graph
        global button_solve
        global button_calculator_icon
        global button_equation_icon
        global button_base_converter_icon
        global button_integral_icon

        def solve():
            global button_calculator_icon
            global button_equation_icon
            global button_base_converter_icon
            global button_integral_icon
            global equation_solved
            global button_home

            eq1_ena_getter = eq1_ena.get()
            eq1_et_getter = eq1_et.get()

            eq2_ena_getter = eq2_ena.get()
            eq2_enb_getter = eq2_enb.get()
            eq2_et_getter = eq2_et.get()

            eq3_ena_getter = eq3_ena.get()
            eq3_enb_getter = eq3_enb.get()
            eq3_enc_getter = eq3_enc.get()
            eq3_et_getter = eq3_et.get()

            if eq1_ena_getter != "" and eq1_et_getter != "":
                if "/0+" in eq1_ena_getter or "/0-" in eq1_ena_getter or "/0*" in eq1_ena_getter or "/0/" in eq1_ena_getter or "/0+" in eq1_et_getter or "/0-" in eq1_et_getter or "/0*" in eq1_et_getter or "/0/" in eq1_et_getter:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#FF4D00"

                        button_bg = "#00DF81"

                        button_home = PhotoImage(file=resource_path(f"Images\\home.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\error_show_error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#94A915"
                        button_bg = "#FF0058"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")

                    equation_shower.place(x=55, y=143, height=34, width=360)

                    equation_shower.insert(0, f"{eq1_ena_getter}x={eq1_et_getter}")

                    error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                        bg="#000000",
                                        foreground="#ffffff")
                    error_entry.place(x=83, y=429, height=34, width=306)
                    error_entry.insert(0, "Can't devide to zero!")

                else:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\equation_solved_1_root.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#15A997"
                        button_bg = "#910794"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\equation_solved_1_root_equation_solved_1_root.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#A9155C"
                        button_bg = "#942007"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehomehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")

                    equation_shower.place(x=50, y=143, height=34, width=360)

                    answer_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21), bg="#000000",
                                          foreground="#ffffff")
                    answer_shower.place(x=130, y=430, height=33, width=200)

                    try:
                        complex_equation(eq1_ena_getter)
                        part_1 = float(answer_for_later)
                        complex_equation(eq1_et_getter)
                        part_2 = float(answer_for_later)

                        part_1_for_showing = round(part_1, 10)
                        part_2_for_showing = round(part_2, 10)

                        if part_1_for_showing.is_integer():
                            part_1_for_showing = int(part_1_for_showing)

                        if part_2_for_showing.is_integer():
                            part_2_for_showing = int(part_2_for_showing)

                        equation_shower.insert(0, f"{part_1_for_showing}x={part_2_for_showing}")

                        answer = part_2 / part_1

                        if answer.is_integer():
                            answer = int(answer)
                            answer_shower.insert(0, answer)

                        else:
                            answer = round(answer, 8)
                            answer_shower.insert(0, answer)

                    except:
                        body_theme_selector = [1, 2]
                        body_theme_selected = random.choice(body_theme_selector)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        if body_theme_selected == 1:
                            equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#FF4D00"
                            button_bg = "#00DF81"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        if body_theme_selected == 2:
                            equation_solved = PhotoImage(
                                file=resource_path("Images\\error_show_error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#94A915"
                            button_bg = "#FF0058"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                        button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                        button_calculator_icon_label.place(x=10, y=0)
                        real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}", command=cal_screen)
                        real_button_calculator_icon.place(x=10, y=0)

                        button_base_converter_icon = PhotoImage(
                            file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                        button_base_converter_icon_label = Label(image=button_base_converter_icon,
                                                                 bg=f"{header_bg_code}")
                        button_base_converter_icon_label.place(x=180, y=2)
                        real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                                 bg=f"{header_bg_code}",
                                                                 activebackground=f"{header_bg_code}",
                                                                 command=base_converter)
                        real_button_base_converter_icon.place(x=180, y=2)

                        button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                        button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                        button_integral_icon_label.place(x=385, y=2)
                        real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                           bg=f"{header_bg_code}",
                                                           activebackground=f"{header_bg_code}")
                        real_button_integral_icon.place(x=385, y=2)

                        equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        equation_shower.place(x=55, y=143, height=34, width=360)
                        equation_shower.insert(0, f"              ax=0")

                        error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")
                        error_entry.place(x=83, y=429, height=34, width=306)
                        error_entry.insert(0, "      Invalid input!")

            if eq2_ena_getter != "" and eq2_enb_getter != "" and eq2_et_getter != "":

                if "/0+" in eq2_ena_getter or "/0-" in eq2_ena_getter or "/0*" in eq2_ena_getter or "/0/" in eq2_ena_getter or "/0+" in eq2_enb_getter or "/0-" in eq2_enb_getter or "/0*" in eq2_enb_getter or "/0/" in eq2_enb_getter or "/0+" in eq2_et_getter or "/0-" in eq2_et_getter or "/0*" in eq2_et_getter or "/0/" in eq2_et_getter:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#FF4D00"
                        button_bg = "#00DF81"

                        button_home = PhotoImage(file=resource_path(f"Images\\home.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\error_show_error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#94A915"
                        button_bg = "#FF0058"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")

                    equation_shower.place(x=55, y=143, height=34, width=360)

                    equation_shower.insert(0, f"{eq2_ena_getter}x+{eq2_enb_getter}={eq2_et_getter}")

                    error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                        bg="#000000",
                                        foreground="#ffffff")
                    error_entry.place(x=83, y=429, height=34, width=306)
                    error_entry.insert(0, "Can't devide to zero!")


                else:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\equation_solved_1_root.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#15A997"

                        button_bg = "#910794"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\equation_solved_1_root_equation_solved_1_root.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#A9155C"
                        button_bg = "#942007"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehomehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")
                    equation_shower.place(x=50, y=143, height=34, width=360)

                    answer_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21), bg="#000000",
                                          foreground="#ffffff")
                    answer_shower.place(x=130, y=430, height=33, width=200)

                    try:
                        complex_equation(eq2_ena_getter)
                        part_1 = answer_for_later
                        part_1 = float(part_1)
                        part_1_for_showing = round(part_1, 7)
                        if part_1_for_showing.is_integer():
                            part_1_for_showing = int(part_1_for_showing)

                        complex_equation(eq2_enb_getter)
                        part_2 = answer_for_later
                        part_2 = float(part_2)
                        part_2_for_showing = round(part_2, 7)
                        if part_2_for_showing.is_integer():
                            part_2_for_showing = int(part_2_for_showing)

                        complex_equation(eq2_et_getter)
                        part_3 = answer_for_later
                        part_3 = float(part_3)
                        part_3_for_showing = round(part_3, 7)
                        if part_3_for_showing.is_integer():
                            part_3_for_showing = int(part_3_for_showing)

                        equation_shower.insert(0, f"{part_1_for_showing}x+{part_2_for_showing}={part_3_for_showing}")

                        answer = ((part_3 - part_2) / part_1)
                        if answer.is_integer():
                            answer = int(answer)
                            answer_shower.insert(0, answer)

                        else:
                            answer_shower.insert(0, answer)

                    except:
                        body_theme_selector = [1, 2]
                        body_theme_selected = random.choice(body_theme_selector)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        if body_theme_selected == 1:
                            equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#FF4D00"
                            button_bg = "#00DF81"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        if body_theme_selected == 2:
                            equation_solved = PhotoImage(
                                file=resource_path("Images\\error_show_error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#94A915"
                            button_bg = "#FF0058"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                        button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                        button_calculator_icon_label.place(x=10, y=0)
                        real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}", command=cal_screen)
                        real_button_calculator_icon.place(x=10, y=0)

                        button_base_converter_icon = PhotoImage(
                            file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                        button_base_converter_icon_label = Label(image=button_base_converter_icon,
                                                                 bg=f"{header_bg_code}")
                        button_base_converter_icon_label.place(x=180, y=2)
                        real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                                 bg=f"{header_bg_code}",
                                                                 activebackground=f"{header_bg_code}",
                                                                 command=base_converter)
                        real_button_base_converter_icon.place(x=180, y=2)

                        button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                        button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                        button_integral_icon_label.place(x=385, y=2)
                        real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                           bg=f"{header_bg_code}",
                                                           activebackground=f"{header_bg_code}")
                        real_button_integral_icon.place(x=385, y=2)

                        equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        equation_shower.place(x=55, y=143, height=34, width=360)
                        equation_shower.insert(0, f"             ax+b=0")

                        error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")
                        error_entry.place(x=83, y=429, height=34, width=306)
                        error_entry.insert(0, "      Invalid input!")

            if eq3_ena_getter != "" and eq3_enb_getter != "" and eq3_enc_getter != "" and eq3_et_getter != "":
                if "/0+" in eq3_ena_getter or "/0-" in eq3_ena_getter or "/0*" in eq3_ena_getter or "/0/" in eq3_ena_getter or "/0+" in eq3_enb_getter or "/0-" in eq3_enb_getter or "/0*" in eq3_enb_getter or "/0/" in eq3_enb_getter or "/0+" in eq3_enc_getter or "/0-" in eq3_enc_getter or "/0*" in eq3_enc_getter or "/0/" in eq3_enc_getter or "/0+" in eq3_et_getter or "/0-" in eq3_et_getter or "/0*" in eq3_et_getter or "/0/" in eq3_et_getter:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#FF4D00"
                        button_bg = "#00DF81"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\error_show_error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#94A915"
                        button_bg = "#FF0058"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")

                    equation_shower.place(x=55, y=143, height=34, width=360)
                    equation_shower.insert(0, f"{eq3_ena_getter}x²+{eq3_enb_getter}x+{eq3_enc_getter}=0")

                    error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                        bg="#000000",
                                        foreground="#ffffff")
                    error_entry.place(x=83, y=429, height=34, width=306)
                    error_entry.insert(0, "Can't devide to zero!")

                else:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\equation_solved_2_roots.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-10, y=-7)
                        header_bg_code = "#15A997"
                        button_bg = "#910794"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\equation_solved_2_roots_equation_solved_2_roots.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-10, y=-7)
                        header_bg_code = "#A9155C"
                        button_bg = "#942007"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    try:
                        part_1 = eq3_ena_getter
                        phrase = part_1
                        complex_equation(phrase)
                        part_1_answer = answer_for_later
                        part_1_answer = float(part_1_answer)
                        part_1_answer = round(part_1_answer, 4)

                        if part_1_answer.is_integer():
                            part_1_answer = int(part_1_answer)

                        part_2 = eq3_enb_getter
                        phrase = part_2
                        complex_equation(phrase)
                        part_2_answer = answer_for_later
                        part_2_answer = float(part_2_answer)
                        part_2_answer = round(part_2_answer, 4)

                        if part_2_answer.is_integer():
                            part_2_answer = int(part_2_answer)

                        part_3 = eq3_enc_getter
                        phrase = part_3
                        complex_equation(phrase)
                        part_3_answer = answer_for_later
                        part_3_answer = float(part_3_answer)
                        part_3_answer = round(part_3_answer, 4)

                        if part_3_answer.is_integer():
                            part_3_answer = int(part_3_answer)

                        equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")
                        equation_shower.place(x=58, y=143, height=34, width=350)

                        answer_1_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        answer_1_shower.place(x=22, y=428, height=34, width=190)

                        answer_2_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        answer_2_shower.place(x=260, y=428, height=34, width=190)

                        what_to_show = f"{part_1_answer}x²+{part_2_answer}x+{part_3_answer}=0"
                        if "+-" in what_to_show:
                            what_to_show = what_to_show.replace("+-", "-")

                        equation_shower.insert(0, what_to_show)

                        delta = pow(part_2_answer, 2) - (4 * (part_1_answer * part_3_answer))

                        try:
                            root_1 = (-(part_2_answer) - (sqrt(delta))) / (2 * part_1_answer)
                            root_2 = (-(part_2_answer) + (sqrt(delta))) / (2 * part_1_answer)
                            root_1 = round(root_1, 10)
                            root_2 = round(root_2, 10)

                            if root_1.is_integer():
                                root_1 = int(root_1)

                            if root_2.is_integer():
                                root_2 = int(root_2)

                            root_1 = round(root_1, 8)
                            root_2 = round(root_2, 8)

                            if root_1 == root_2:
                                answer_1_shower.insert(0, root_1)
                                answer_2_shower.insert(0, "--------------------")

                            else:
                                answer_1_shower.insert(0, root_1)
                                answer_2_shower.insert(0, root_2)

                        except:
                            body_theme_selector = [1, 2]
                            body_theme_selected = random.choice(body_theme_selector)

                            button_calculator_icon = "calculator_icon"
                            button_equation_icon = "equation_icon"
                            button_base_converter_icon = "base_converter_icon"
                            button_integral_icon = "integral_icon"

                            if body_theme_selected == 1:
                                equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                                equation_solved_label = Label(root, image=equation_solved)
                                equation_solved_label.place(x=-25, y=-7)
                                header_bg_code = "#FF4D00"
                                button_bg = "#00DF81"

                                button_home = PhotoImage(file=resource_path(f"Images\\home.png"))
                                button_home_label = Label(image=button_home, bg=f"{button_bg}")
                                button_home_label.place(x=175, y=470)
                                real_button_home = Button(root, image=button_home, borderwidth=0,
                                                          bg=f"{button_bg}",
                                                          activebackground=f"{button_bg}", command=equation)
                                real_button_home.place(x=175, y=470)

                            if body_theme_selected == 2:
                                equation_solved = PhotoImage(
                                    file=resource_path("Images\\error_show_error_show.png"))
                                equation_solved_label = Label(root, image=equation_solved)
                                equation_solved_label.place(x=-25, y=-7)
                                header_bg_code = "#94A915"
                                button_bg = "#FF0058"

                                button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                                button_home_label = Label(image=button_home, bg=f"{button_bg}")
                                button_home_label.place(x=175, y=470)
                                real_button_home = Button(root, image=button_home, borderwidth=0,
                                                          bg=f"{button_bg}",
                                                          activebackground=f"{button_bg}", command=equation)
                                real_button_home.place(x=175, y=470)

                            button_calculator_icon = "calculator_icon"
                            button_equation_icon = "equation_icon"
                            button_base_converter_icon = "base_converter_icon"
                            button_integral_icon = "integral_icon"

                            button_calculator_icon = PhotoImage(
                                file=resource_path(f"Images\\{button_calculator_icon}.png"))
                            button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                            button_calculator_icon_label.place(x=10, y=0)
                            real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                                 bg=f"{header_bg_code}",
                                                                 activebackground=f"{header_bg_code}",
                                                                 command=cal_screen)
                            real_button_calculator_icon.place(x=10, y=0)

                            button_base_converter_icon = PhotoImage(
                                file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                            button_base_converter_icon_label = Label(image=button_base_converter_icon,
                                                                     bg=f"{header_bg_code}")
                            button_base_converter_icon_label.place(x=180, y=2)
                            real_button_base_converter_icon = Button(root, image=button_base_converter_icon,
                                                                     borderwidth=0,
                                                                     bg=f"{header_bg_code}",
                                                                     activebackground=f"{header_bg_code}",
                                                                     command=base_converter)
                            real_button_base_converter_icon.place(x=180, y=2)

                            button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                            button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                            button_integral_icon_label.place(x=385, y=2)
                            real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                               bg=f"{header_bg_code}",
                                                               activebackground=f"{header_bg_code}")
                            real_button_integral_icon.place(x=385, y=2)

                            equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                    bg="#000000",
                                                    foreground="#ffffff")

                            equation_shower.place(x=50, y=143, height=34, width=360)
                            equation_shower.insert(0, what_to_show)

                            error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")
                            error_entry.place(x=130, y=429, height=34, width=220)
                            error_entry.insert(0, "No real roots!")

                    except:
                        body_theme_selector = [1, 2]
                        body_theme_selected = random.choice(body_theme_selector)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        if body_theme_selected == 1:
                            equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#FF4D00"
                            button_bg = "#00DF81"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        if body_theme_selected == 2:
                            equation_solved = PhotoImage(
                                file=resource_path("Images\\error_show_error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#94A915"
                            button_bg = "#FF0058"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                        button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                        button_calculator_icon_label.place(x=10, y=0)
                        real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}", command=cal_screen)
                        real_button_calculator_icon.place(x=10, y=0)

                        button_base_converter_icon = PhotoImage(
                            file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                        button_base_converter_icon_label = Label(image=button_base_converter_icon,
                                                                 bg=f"{header_bg_code}")
                        button_base_converter_icon_label.place(x=180, y=2)
                        real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                                 bg=f"{header_bg_code}",
                                                                 activebackground=f"{header_bg_code}",
                                                                 command=base_converter)
                        real_button_base_converter_icon.place(x=180, y=2)

                        button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                        button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                        button_integral_icon_label.place(x=385, y=2)
                        real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                           bg=f"{header_bg_code}",
                                                           activebackground=f"{header_bg_code}")
                        real_button_integral_icon.place(x=385, y=2)

                        equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        equation_shower.place(x=55, y=143, height=34, width=360)
                        equation_shower.insert(0, f"          ax²+bx+c=0")

                        error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")
                        error_entry.place(x=83, y=429, height=34, width=306)
                        error_entry.insert(0, "      Invalid input!")

        def graph():
            global button_calculator_icon
            global button_equation_icon
            global button_base_converter_icon
            global button_integral_icon
            global equation_solved
            global button_home

            eq1_ena_getter = eq1_ena.get()
            eq1_et_getter = eq1_et.get()

            eq2_ena_getter = eq2_ena.get()
            eq2_enb_getter = eq2_enb.get()
            eq2_et_getter = eq2_et.get()

            eq3_ena_getter = eq3_ena.get()
            eq3_enb_getter = eq3_enb.get()
            eq3_enc_getter = eq3_enc.get()
            eq3_et_getter = eq3_et.get()

            if eq1_ena_getter != "" and eq1_et_getter != "":
                if "/0+" in eq1_ena_getter or "/0-" in eq1_ena_getter or "/0*" in eq1_ena_getter or "/0/" in eq1_ena_getter or "/0+" in eq1_et_getter or "/0-" in eq1_et_getter or "/0*" in eq1_et_getter or "/0/" in eq1_et_getter:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#FF4D00"

                        button_bg = "#00DF81"

                        button_home = PhotoImage(file=resource_path(f"Images\\home.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\error_show_error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#94A915"
                        button_bg = "#FF0058"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")

                    equation_shower.place(x=55, y=143, height=34, width=360)

                    equation_shower.insert(0, f"{eq1_ena_getter}x={eq1_et_getter}")

                    error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                        bg="#000000",
                                        foreground="#ffffff")
                    error_entry.place(x=83, y=429, height=34, width=306)
                    error_entry.insert(0, "Can't devide to zero!")

                else:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\equation_solved_1_root.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#15A997"
                        button_bg = "#910794"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\equation_solved_1_root_equation_solved_1_root.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#A9155C"
                        button_bg = "#942007"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehomehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")

                    equation_shower.place(x=50, y=143, height=34, width=360)

                    answer_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21), bg="#000000",
                                          foreground="#ffffff")
                    answer_shower.place(x=130, y=430, height=33, width=200)

                    try:
                        complex_equation(eq1_ena_getter)
                        part_1 = float(answer_for_later)
                        complex_equation(eq1_et_getter)
                        part_2 = float(answer_for_later)

                        part_1_for_showing = round(part_1, 10)
                        part_2_for_showing = round(part_2, 10)

                        if part_1_for_showing.is_integer():
                            part_1_for_showing = int(part_1_for_showing)

                        if part_2_for_showing.is_integer():
                            part_2_for_showing = int(part_2_for_showing)

                        equation_shower.insert(0, f"{part_1_for_showing}x={part_2_for_showing}")

                        answer = part_2 / part_1

                        if answer.is_integer():
                            answer = int(answer)
                            answer_shower.insert(0, answer)

                        else:
                            answer = round(answer, 8)
                            answer_shower.insert(0, answer)

                    except:
                        body_theme_selector = [1, 2]
                        body_theme_selected = random.choice(body_theme_selector)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        if body_theme_selected == 1:
                            equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#FF4D00"
                            button_bg = "#00DF81"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        if body_theme_selected == 2:
                            equation_solved = PhotoImage(
                                file=resource_path("Images\\error_show_error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#94A915"
                            button_bg = "#FF0058"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                        button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                        button_calculator_icon_label.place(x=10, y=0)
                        real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}", command=cal_screen)
                        real_button_calculator_icon.place(x=10, y=0)

                        button_base_converter_icon = PhotoImage(
                            file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                        button_base_converter_icon_label = Label(image=button_base_converter_icon,
                                                                 bg=f"{header_bg_code}")
                        button_base_converter_icon_label.place(x=180, y=2)
                        real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                                 bg=f"{header_bg_code}",
                                                                 activebackground=f"{header_bg_code}",
                                                                 command=base_converter)
                        real_button_base_converter_icon.place(x=180, y=2)

                        button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                        button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                        button_integral_icon_label.place(x=385, y=2)
                        real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                           bg=f"{header_bg_code}",
                                                           activebackground=f"{header_bg_code}")
                        real_button_integral_icon.place(x=385, y=2)

                        equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        equation_shower.place(x=55, y=143, height=34, width=360)
                        equation_shower.insert(0, f"              ax=0")

                        error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")
                        error_entry.place(x=83, y=429, height=34, width=306)
                        error_entry.insert(0, "      Invalid input!")

                plt.style.use('dark_background')
                plt.grid()
                x = np.linspace(-5, 5, 10)
                y = float(eq1_ena_getter) * x + float(eq1_et_getter)
                plt.plot(x, y, '-r')

                plt.show()

            if eq2_ena_getter != "" and eq2_enb_getter != "" and eq2_et_getter != "":

                if "/0+" in eq2_ena_getter or "/0-" in eq2_ena_getter or "/0*" in eq2_ena_getter or "/0/" in eq2_ena_getter or "/0+" in eq2_enb_getter or "/0-" in eq2_enb_getter or "/0*" in eq2_enb_getter or "/0/" in eq2_enb_getter or "/0+" in eq2_et_getter or "/0-" in eq2_et_getter or "/0*" in eq2_et_getter or "/0/" in eq2_et_getter:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#FF4D00"
                        button_bg = "#00DF81"

                        button_home = PhotoImage(file=resource_path(f"Images\\home.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\error_show_error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#94A915"
                        button_bg = "#FF0058"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")

                    equation_shower.place(x=55, y=143, height=34, width=360)

                    equation_shower.insert(0, f"{eq2_ena_getter}x+{eq2_enb_getter}={eq2_et_getter}")

                    error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                        bg="#000000",
                                        foreground="#ffffff")
                    error_entry.place(x=83, y=429, height=34, width=306)
                    error_entry.insert(0, "Can't devide to zero!")


                else:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\equation_solved_1_root.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#15A997"

                        button_bg = "#910794"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\equation_solved_1_root_equation_solved_1_root.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#A9155C"
                        button_bg = "#942007"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehomehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")
                    equation_shower.place(x=50, y=143, height=34, width=360)

                    answer_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21), bg="#000000",
                                          foreground="#ffffff")
                    answer_shower.place(x=130, y=430, height=33, width=200)

                    try:
                        complex_equation(eq2_ena_getter)
                        part_1 = answer_for_later
                        part_1 = float(part_1)
                        part_1_for_showing = round(part_1, 7)
                        if part_1_for_showing.is_integer():
                            part_1_for_showing = int(part_1_for_showing)

                        complex_equation(eq2_enb_getter)
                        part_2 = answer_for_later
                        part_2 = float(part_2)
                        part_2_for_showing = round(part_2, 7)
                        if part_2_for_showing.is_integer():
                            part_2_for_showing = int(part_2_for_showing)

                        complex_equation(eq2_et_getter)
                        part_3 = answer_for_later
                        part_3 = float(part_3)
                        part_3_for_showing = round(part_3, 7)
                        if part_3_for_showing.is_integer():
                            part_3_for_showing = int(part_3_for_showing)

                        equation_shower.insert(0, f"{part_1_for_showing}x+{part_2_for_showing}={part_3_for_showing}")

                        answer = ((part_3 - part_2) / part_1)
                        if answer.is_integer():
                            answer = int(answer)
                            answer_shower.insert(0, answer)

                        else:
                            answer_shower.insert(0, answer)

                    except:
                        body_theme_selector = [1, 2]
                        body_theme_selected = random.choice(body_theme_selector)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        if body_theme_selected == 1:
                            equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#FF4D00"
                            button_bg = "#00DF81"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        if body_theme_selected == 2:
                            equation_solved = PhotoImage(
                                file=resource_path("Images\\error_show_error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#94A915"
                            button_bg = "#FF0058"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                        button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                        button_calculator_icon_label.place(x=10, y=0)
                        real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}", command=cal_screen)
                        real_button_calculator_icon.place(x=10, y=0)

                        button_base_converter_icon = PhotoImage(
                            file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                        button_base_converter_icon_label = Label(image=button_base_converter_icon,
                                                                 bg=f"{header_bg_code}")
                        button_base_converter_icon_label.place(x=180, y=2)
                        real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                                 bg=f"{header_bg_code}",
                                                                 activebackground=f"{header_bg_code}",
                                                                 command=base_converter)
                        real_button_base_converter_icon.place(x=180, y=2)

                        button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                        button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                        button_integral_icon_label.place(x=385, y=2)
                        real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                           bg=f"{header_bg_code}",
                                                           activebackground=f"{header_bg_code}")
                        real_button_integral_icon.place(x=385, y=2)

                        equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        equation_shower.place(x=55, y=143, height=34, width=360)
                        equation_shower.insert(0, f"             ax+b=0")

                        error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")
                        error_entry.place(x=83, y=429, height=34, width=306)
                        error_entry.insert(0, "      Invalid input!")

                plt.style.use('dark_background')
                plt.grid()
                x = np.linspace(-5, 5, 10)
                y = float(eq2_ena_getter) * x + float(eq2_et_getter)
                plt.plot(x, y, '-y')

                plt.show()

            if eq3_ena_getter != "" and eq3_enb_getter != "" and eq3_enc_getter != "" and eq3_et_getter != "":
                if "/0+" in eq3_ena_getter or "/0-" in eq3_ena_getter or "/0*" in eq3_ena_getter or "/0/" in eq3_ena_getter or "/0+" in eq3_enb_getter or "/0-" in eq3_enb_getter or "/0*" in eq3_enb_getter or "/0/" in eq3_enb_getter or "/0+" in eq3_enc_getter or "/0-" in eq3_enc_getter or "/0*" in eq3_enc_getter or "/0/" in eq3_enc_getter or "/0+" in eq3_et_getter or "/0-" in eq3_et_getter or "/0*" in eq3_et_getter or "/0/" in eq3_et_getter:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#FF4D00"
                        button_bg = "#00DF81"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\error_show_error_show.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-20, y=-7)
                        header_bg_code = "#94A915"
                        button_bg = "#FF0058"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")

                    equation_shower.place(x=55, y=143, height=34, width=360)
                    equation_shower.insert(0, f"{eq3_ena_getter}x²+{eq3_enb_getter}x+{eq3_enc_getter}=0")

                    error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                        bg="#000000",
                                        foreground="#ffffff")
                    error_entry.place(x=83, y=429, height=34, width=306)
                    error_entry.insert(0, "Can't devide to zero!")

                else:
                    body_theme_selector = [1, 2]
                    body_theme_selected = random.choice(body_theme_selector)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    if body_theme_selected == 1:
                        equation_solved = PhotoImage(file=resource_path("Images\\equation_solved_2_roots.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-10, y=-7)
                        header_bg_code = "#15A997"
                        button_bg = "#910794"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    if body_theme_selected == 2:
                        equation_solved = PhotoImage(
                            file=resource_path("Images\\equation_solved_2_roots_equation_solved_2_roots.png"))
                        equation_solved_label = Label(root, image=equation_solved)
                        equation_solved_label.place(x=-10, y=-7)
                        header_bg_code = "#A9155C"
                        button_bg = "#942007"

                        button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                        button_home_label = Label(image=button_home, bg=f"{button_bg}")
                        button_home_label.place(x=175, y=470)
                        real_button_home = Button(root, image=button_home, borderwidth=0,
                                                  bg=f"{button_bg}",
                                                  activebackground=f"{button_bg}", command=equation)
                        real_button_home.place(x=175, y=470)

                    button_calculator_icon = "calculator_icon"
                    button_equation_icon = "equation_icon"
                    button_base_converter_icon = "base_converter_icon"
                    button_integral_icon = "integral_icon"

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"{header_bg_code}",
                                                         activebackground=f"{header_bg_code}", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_base_converter_icon = PhotoImage(
                        file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                    button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
                    button_base_converter_icon_label.place(x=180, y=2)
                    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}",
                                                             command=base_converter)
                    real_button_base_converter_icon.place(x=180, y=2)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"{header_bg_code}",
                                                       activebackground=f"{header_bg_code}")
                    real_button_integral_icon.place(x=385, y=2)

                    try:
                        part_1 = eq3_ena_getter
                        phrase = part_1
                        complex_equation(phrase)
                        part_1_answer = answer_for_later
                        part_1_answer = float(part_1_answer)
                        part_1_answer = round(part_1_answer, 4)

                        if part_1_answer.is_integer():
                            part_1_answer = int(part_1_answer)

                        part_2 = eq3_enb_getter
                        phrase = part_2
                        complex_equation(phrase)
                        part_2_answer = answer_for_later
                        part_2_answer = float(part_2_answer)
                        part_2_answer = round(part_2_answer, 4)

                        if part_2_answer.is_integer():
                            part_2_answer = int(part_2_answer)

                        part_3 = eq3_enc_getter
                        phrase = part_3
                        complex_equation(phrase)
                        part_3_answer = answer_for_later
                        part_3_answer = float(part_3_answer)
                        part_3_answer = round(part_3_answer, 4)

                        if part_3_answer.is_integer():
                            part_3_answer = int(part_3_answer)

                        equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")
                        equation_shower.place(x=58, y=143, height=34, width=350)

                        answer_1_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        answer_1_shower.place(x=22, y=428, height=34, width=190)

                        answer_2_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        answer_2_shower.place(x=260, y=428, height=34, width=190)

                        what_to_show = f"{part_1_answer}x²+{part_2_answer}x+{part_3_answer}=0"
                        if "+-" in what_to_show:
                            what_to_show = what_to_show.replace("+-", "-")

                        equation_shower.insert(0, what_to_show)

                        delta = pow(part_2_answer, 2) - (4 * (part_1_answer * part_3_answer))

                        try:
                            root_1 = (-(part_2_answer) - (sqrt(delta))) / (2 * part_1_answer)
                            root_2 = (-(part_2_answer) + (sqrt(delta))) / (2 * part_1_answer)
                            root_1 = round(root_1, 10)
                            root_2 = round(root_2, 10)

                            if root_1.is_integer():
                                root_1 = int(root_1)

                            if root_2.is_integer():
                                root_2 = int(root_2)

                            root_1 = round(root_1, 8)
                            root_2 = round(root_2, 8)

                            if root_1 == root_2:
                                answer_1_shower.insert(0, root_1)
                                answer_2_shower.insert(0, "--------------------")

                            else:
                                answer_1_shower.insert(0, root_1)
                                answer_2_shower.insert(0, root_2)

                        except:
                            body_theme_selector = [1, 2]
                            body_theme_selected = random.choice(body_theme_selector)

                            button_calculator_icon = "calculator_icon"
                            button_equation_icon = "equation_icon"
                            button_base_converter_icon = "base_converter_icon"
                            button_integral_icon = "integral_icon"

                            if body_theme_selected == 1:
                                equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                                equation_solved_label = Label(root, image=equation_solved)
                                equation_solved_label.place(x=-25, y=-7)
                                header_bg_code = "#FF4D00"
                                button_bg = "#00DF81"

                                button_home = PhotoImage(file=resource_path(f"Images\\home.png"))
                                button_home_label = Label(image=button_home, bg=f"{button_bg}")
                                button_home_label.place(x=175, y=470)
                                real_button_home = Button(root, image=button_home, borderwidth=0,
                                                          bg=f"{button_bg}",
                                                          activebackground=f"{button_bg}", command=equation)
                                real_button_home.place(x=175, y=470)

                            if body_theme_selected == 2:
                                equation_solved = PhotoImage(
                                    file=resource_path("Images\\error_show_error_show.png"))
                                equation_solved_label = Label(root, image=equation_solved)
                                equation_solved_label.place(x=-25, y=-7)
                                header_bg_code = "#94A915"
                                button_bg = "#FF0058"

                                button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                                button_home_label = Label(image=button_home, bg=f"{button_bg}")
                                button_home_label.place(x=175, y=470)
                                real_button_home = Button(root, image=button_home, borderwidth=0,
                                                          bg=f"{button_bg}",
                                                          activebackground=f"{button_bg}", command=equation)
                                real_button_home.place(x=175, y=470)

                            button_calculator_icon = "calculator_icon"
                            button_equation_icon = "equation_icon"
                            button_base_converter_icon = "base_converter_icon"
                            button_integral_icon = "integral_icon"

                            button_calculator_icon = PhotoImage(
                                file=resource_path(f"Images\\{button_calculator_icon}.png"))
                            button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                            button_calculator_icon_label.place(x=10, y=0)
                            real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                                 bg=f"{header_bg_code}",
                                                                 activebackground=f"{header_bg_code}",
                                                                 command=cal_screen)
                            real_button_calculator_icon.place(x=10, y=0)

                            button_base_converter_icon = PhotoImage(
                                file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                            button_base_converter_icon_label = Label(image=button_base_converter_icon,
                                                                     bg=f"{header_bg_code}")
                            button_base_converter_icon_label.place(x=180, y=2)
                            real_button_base_converter_icon = Button(root, image=button_base_converter_icon,
                                                                     borderwidth=0,
                                                                     bg=f"{header_bg_code}",
                                                                     activebackground=f"{header_bg_code}",
                                                                     command=base_converter)
                            real_button_base_converter_icon.place(x=180, y=2)

                            button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                            button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                            button_integral_icon_label.place(x=385, y=2)
                            real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                               bg=f"{header_bg_code}",
                                                               activebackground=f"{header_bg_code}")
                            real_button_integral_icon.place(x=385, y=2)

                            equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                    bg="#000000",
                                                    foreground="#ffffff")

                            equation_shower.place(x=50, y=143, height=34, width=360)
                            equation_shower.insert(0, what_to_show)

                            error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")
                            error_entry.place(x=130, y=429, height=34, width=220)
                            error_entry.insert(0, "No real roots!")

                    except:
                        body_theme_selector = [1, 2]
                        body_theme_selected = random.choice(body_theme_selector)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        if body_theme_selected == 1:
                            equation_solved = PhotoImage(file=resource_path("Images\\error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#FF4D00"
                            button_bg = "#00DF81"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehomehomehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        if body_theme_selected == 2:
                            equation_solved = PhotoImage(
                                file=resource_path("Images\\error_show_error_show.png"))
                            equation_solved_label = Label(root, image=equation_solved)
                            equation_solved_label.place(x=-20, y=-7)
                            header_bg_code = "#94A915"
                            button_bg = "#FF0058"

                            button_home = PhotoImage(file=resource_path(f"Images\\homehome.png"))
                            button_home_label = Label(image=button_home, bg=f"{button_bg}")
                            button_home_label.place(x=175, y=470)
                            real_button_home = Button(root, image=button_home, borderwidth=0,
                                                      bg=f"{button_bg}",
                                                      activebackground=f"{button_bg}", command=equation)
                            real_button_home.place(x=175, y=470)

                        button_calculator_icon = "calculator_icon"
                        button_equation_icon = "equation_icon"
                        button_base_converter_icon = "base_converter_icon"
                        button_integral_icon = "integral_icon"

                        button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
                        button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
                        button_calculator_icon_label.place(x=10, y=0)
                        real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                             bg=f"{header_bg_code}",
                                                             activebackground=f"{header_bg_code}", command=cal_screen)
                        real_button_calculator_icon.place(x=10, y=0)

                        button_base_converter_icon = PhotoImage(
                            file=resource_path(f"Images\\{button_base_converter_icon}.png"))
                        button_base_converter_icon_label = Label(image=button_base_converter_icon,
                                                                 bg=f"{header_bg_code}")
                        button_base_converter_icon_label.place(x=180, y=2)
                        real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                                 bg=f"{header_bg_code}",
                                                                 activebackground=f"{header_bg_code}",
                                                                 command=base_converter)
                        real_button_base_converter_icon.place(x=180, y=2)

                        button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
                        button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
                        button_integral_icon_label.place(x=385, y=2)
                        real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                           bg=f"{header_bg_code}",
                                                           activebackground=f"{header_bg_code}")
                        real_button_integral_icon.place(x=385, y=2)

                        equation_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                                bg="#000000",
                                                foreground="#ffffff")

                        equation_shower.place(x=55, y=143, height=34, width=360)
                        equation_shower.insert(0, f"          ax²+bx+c=0")

                        error_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 21),
                                            bg="#000000",
                                            foreground="#ffffff")
                        error_entry.place(x=83, y=429, height=34, width=306)
                        error_entry.insert(0, "      Invalid input!")

                if "-" in str(root_1):
                    from_ = root_1 - 1
                else:
                    from_ = root_1 + 1

                if "-" in str(root_2):
                    to_ = root_2 + 1
                else:
                    to_ = root_2 - 1

                plt.style.use('dark_background')
                plt.grid()
                x = np.linspace(from_, to_, 50)
                y = float(eq3_ena_getter) * x ** 2 + float(eq3_enb_getter) * x + float(eq3_enc_getter)
                plt.plot(x, y, '-c')

                plt.show()

        body_theme_selector = [1, 2, 3, 4]
        body_theme_selected = random.choice(body_theme_selector)

        button_calculator_icon = "calculator_icon"
        button_equation_icon = "equation_icon"
        button_base_converter_icon = "base_converter_icon"
        button_integral_icon = "integral_icon"

        if body_theme_selected == 1:
            equation_screen = PhotoImage(file=resource_path("Images\\Equation.png"))
            equation_screen_label = Label(root, image=equation_screen)
            equation_screen_label.place(x=-30, y=-7)

            button_graph = PhotoImage(file=resource_path("Images\\graph.png"))
            button_graph_label = Label(image=button_graph, bg="#D864CB")
            button_graph_label.place(x=340, y=302)
            real_button_graph = Button(root, text="8", image=button_graph, borderwidth=0, bg="#D864CB",
                                       activebackground="#D864CB", command=graph)
            real_button_graph.place(x=340, y=302)

            button_solve = PhotoImage(file=resource_path("Images\\solve.png"))
            button_solve_label = Label(image=button_solve, bg="#D7C5D5")
            button_solve_label.place(x=10, y=302)
            real_button_solve = Button(root, text="8", image=button_solve, borderwidth=0, bg="#D7C5D5",
                                       activebackground="#D7C5D5", command=solve)
            real_button_solve.place(x=10, y=302)

            header_bg_code = "#303D83"

        if body_theme_selected == 2:
            equation_screen = PhotoImage(file=resource_path("Images\\EquationEquation.png"))
            equation_screen_label = Label(root, image=equation_screen)
            equation_screen_label.place(x=-30, y=-7)

            button_graph = PhotoImage(file=resource_path("Images\\graphgraph.png"))
            button_graph_label = Label(image=button_graph, bg="#65C5DA")
            button_graph_label.place(x=340, y=302)
            real_button_graph = Button(root, text="8", image=button_graph, borderwidth=0, bg="#65C5DA",
                                       activebackground="#65C5DA", command=graph)
            real_button_graph.place(x=340, y=302)

            button_solve = PhotoImage(file=resource_path("Images\\solvesolve.png"))
            button_solve_label = Label(image=button_solve, bg="#ACBFC3")
            button_solve_label.place(x=10, y=302)
            real_button_solve = Button(root, text="8", image=button_solve, borderwidth=0, bg="#ACBFC3",
                                       activebackground="#ACBFC3", command=solve)
            real_button_solve.place(x=10, y=302)

            header_bg_code = "#833A30"

        if body_theme_selected == 3:
            equation_screen = PhotoImage(file=resource_path("Images\\EquationEquationEquation.png"))
            equation_screen_label = Label(root, image=equation_screen)
            equation_screen_label.place(x=-30, y=-7)

            button_graph = PhotoImage(file=resource_path("Images\\graphgraphgraph.png"))
            button_graph_label = Label(image=button_graph, bg="#B8C150")
            button_graph_label.place(x=340, y=302)
            real_button_graph = Button(root, text="8", image=button_graph, borderwidth=0, bg="#B8C150",
                                       activebackground="#B8C150", command=graph)
            real_button_graph.place(x=340, y=302)

            button_solve = PhotoImage(file=resource_path("Images\\solvesolvesolve.png"))
            button_solve_label = Label(image=button_solve, bg="#D4D8A7")
            button_solve_label.place(x=10, y=302)
            real_button_solve = Button(root, text="8", image=button_solve, borderwidth=0, bg="#D4D8A7",
                                       activebackground="#D4D8A7", command=solve)
            real_button_solve.place(x=10, y=302)
            header_bg_code = "#833075"

        if body_theme_selected == 4:
            equation_screen = PhotoImage(file=resource_path("Images\\EquationEquationEquationEquation.png"))
            equation_screen_label = Label(root, image=equation_screen)
            equation_screen_label.place(x=-30, y=-7)

            button_graph = PhotoImage(file=resource_path("Images\\graphgraphgraphgraph.png"))
            button_graph_label = Label(image=button_graph, bg="#E48383")
            button_graph_label.place(x=340, y=302)
            real_button_graph = Button(root, text="8", image=button_graph, borderwidth=0, bg="#E48383",
                                       activebackground="#E48383", command=graph)
            real_button_graph.place(x=340, y=302)

            button_solve = PhotoImage(file=resource_path("Images\\solvesolvesolvesolve.png"))
            button_solve_label = Label(image=button_solve, bg="#D5B0B0")
            button_solve_label.place(x=10, y=302)
            real_button_solve = Button(root, text="8", image=button_solve, borderwidth=0, bg="#D5B0B0",
                                       activebackground="#D5B0B0", command=solve)
            real_button_solve.place(x=10, y=302)

            header_bg_code = "#837530"

        eq1_ena = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 17), bg="#585858",
                        foreground="#ffffff")
        eq1_ena.place(x=151, y=140, height=24, width=55)
        eq1_et = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 17), bg="#585858",
                       foreground="#ffffff")
        eq1_et.place(x=275, y=140, height=24, width=55)

        eq2_ena = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 18), bg="#585858",
                        foreground="#ffffff")
        eq2_ena.place(x=99, y=204, height=24, width=55)
        eq2_enb = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 18), bg="#585858",
                        foreground="#ffffff")
        eq2_enb.place(x=226, y=204, height=24, width=55)
        eq2_et = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 17), bg="#585858",
                       foreground="#ffffff")
        eq2_et.place(x=326, y=204, height=24, width=55)

        eq3_ena = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 17), bg="#585858",
                        foreground="#ffffff")
        eq3_ena.place(x=31, y=272, height=24, width=55)
        eq3_enb = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 17), bg="#585858",
                        foreground="#ffffff")
        eq3_enb.place(x=172, y=272, height=24, width=55)
        eq3_enc = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 17), bg="#585858",
                        foreground="#ffffff")
        eq3_enc.place(x=300, y=272, height=24, width=55)
        eq3_et = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 17), bg="#585858",
                       foreground="#ffffff")
        eq3_et.place(x=396, y=272, height=24, width=55)

        button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
        button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
        button_calculator_icon_label.place(x=10, y=0)
        real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0, bg=f"{header_bg_code}",
                                             activebackground=f"{header_bg_code}", command=cal_screen)
        real_button_calculator_icon.place(x=10, y=0)

        button_base_converter_icon = PhotoImage(file=resource_path(f"Images\\{button_base_converter_icon}.png"))
        button_base_converter_icon_label = Label(image=button_base_converter_icon, bg=f"{header_bg_code}")
        button_base_converter_icon_label.place(x=180, y=2)
        real_button_base_converter_icon = Button(root, image=button_base_converter_icon, borderwidth=0,
                                                 bg=f"{header_bg_code}", activebackground=f"{header_bg_code}",
                                                 command=base_converter)
        real_button_base_converter_icon.place(x=180, y=2)

        button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
        button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
        button_integral_icon_label.place(x=385, y=2)
        real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0, bg=f"{header_bg_code}",
                                           activebackground=f"{header_bg_code}")
        real_button_integral_icon.place(x=385, y=2)

    def integral():
        data = e.get()
        if len(data) != 0:
            e.delete(0, END)
            e.insert(0, "     Under construction!")

        else:
            e.insert(0, "     Under construction!")

    def base_converter():
        global button_calculator_icon
        global button_equation_icon
        global button_base_converter_icon
        global button_integral_icon
        global base_converter_screen
        global from_1, from_2, from_3, from_4, from_5, from_6, from_7, from_8, from_9, from_10, from_11, from_12
        global from_13, from_14, from_15, from_16, from_17, from_18, from_19, from_20, from_21, from_22, from_23, from_24
        global from_25, from_26, from_27, from_28, from_29, from_30, from_31, from_32, from_33, from_34, from_35, from_36

        def from_base_data_getter(from_base):

            global button_calculator_icon
            global button_equation_icon
            global button_base_converter_icon
            global button_integral_icon
            global base_converter_screen
            global to_1, to_2, to_3, to_4, to_5, to_6, to_7, to_8, to_9, to_10, to_11, to_12
            global to_13, to_14, to_15, to_16, to_17, to_18, to_19, to_20, to_21, to_22, to_23, to_24
            global to_25, to_26, to_27, to_28, to_29, to_30, to_31, to_32, to_33, to_34, to_35, to_36

            def to_base_data_getter(to_base):
                global number_getter_screen
                global convert
                global button_calculator_icon
                global button_equation_icon
                global button_base_converter_icon
                global button_integral_icon

                def converter():
                    global number_to_be_converted
                    global number_giver_screen
                    global home
                    global button_calculator_icon
                    global button_equation_icon
                    global button_base_converter_icon
                    global button_integral_icon

                    number_to_be_converted = number_entry.get()

                    number_giver_screen = PhotoImage(
                        file=resource_path("Images\\number_giver.png"))
                    number_giver_screen_label = Label(root, image=number_giver_screen)
                    number_giver_screen_label.place(x=-15, y=-7)

                    number_shower = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 23), bg="#474747",
                                          foreground="#ffffff")
                    number_shower.place(x=50, y=410, height=40, width=370)

                    home = PhotoImage(file=resource_path("Images\\home.png"))
                    home_label = Label(image=home, borderwidth=0)
                    home_label.place(x=175, y=465)
                    real_home = Button(root, image=home, borderwidth=0, background="black",
                                       activebackground="black", command=base_converter)
                    real_home.place(x=175, y=465)

                    button_calculator_icon = PhotoImage(file=resource_path(f"Images\\calculator_icon.png"))
                    button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"#BC7C00")
                    button_calculator_icon_label.place(x=10, y=0)
                    real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                         bg=f"#BC7C00",
                                                         activebackground=f"#BC7C00", command=cal_screen)
                    real_button_calculator_icon.place(x=10, y=0)

                    button_equation_icon = PhotoImage(file=resource_path(f"Images\\equation_icon.png"))
                    button_equation_icon_label = Label(image=button_equation_icon, bg=f"#BC7C00")
                    button_equation_icon_label.place(x=190, y=3)
                    real_button_equation_icon = Button(root, image=button_equation_icon, borderwidth=0,
                                                       bg=f"#BC7C00",
                                                       activebackground=f"#BC7C00", command=equation)
                    real_button_equation_icon.place(x=190, y=3)

                    button_integral_icon = PhotoImage(file=resource_path(f"Images\\integral_icon.png"))
                    button_integral_icon_label = Label(image=button_integral_icon, bg=f"#BC7C00")
                    button_integral_icon_label.place(x=385, y=2)
                    real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                       bg=f"#BC7C00",
                                                       activebackground=f"#BC7C00")
                    real_button_integral_icon.place(x=385, y=2)

                    def Base_2__9_10(starting_base):
                        integer_list = []
                        float_list = []
                        integer_sum = 0
                        float_sum = 0
                        integer_power = 0
                        float_power = 0

                        num = number_to_be_converted

                        if "." not in num:
                            num = num + "." + str(0)

                        integer_num, float_num = num.split(".")

                        for lenght_integer in integer_num:
                            integer_list.append(int(lenght_integer))

                        for lenght_decimal in float_num:
                            float_list.append(int(lenght_decimal))

                        if float_list == ["0"]:
                            float_list = []

                        while len(integer_list) != 0:
                            integer_sum = (integer_list[-1]) * (starting_base ** integer_power) + integer_sum
                            integer_power += 1
                            integer_list.pop()

                        if len(float_list) != 0:
                            float_power = -abs(len(float_list))
                            while len(float_list) != 0:
                                float_sum = (float_list[-1]) * (starting_base ** float_power) + float_sum
                                float_power += 1
                                float_list.pop()

                        if float_sum == 0:
                            number_shower.delete(0, END)
                            number_shower.insert(0, str(integer_sum))
                        else:
                            number_shower.delete(0, END)
                            number_shower.insert(0, str(integer_sum + float_sum))

                    def Base_10_2__9(ending_base):
                        integer_part_of_reversed_remainders_list = []
                        float_num_in_row_list = []
                        reversed_remainders = []
                        first_part_of_float_list = []
                        remainders = []

                        num = number_to_be_converted

                        if "." not in num:
                            num = num + "." + str(0)

                        integer_num, float_num = num.split(".")

                        float_num = str(0) + "." + str(float_num)

                        while True:
                            integer_remainder = int(integer_num) % ending_base
                            integer_num = int(integer_num) / ending_base
                            remainders.append(integer_remainder)
                            if integer_num / ending_base == 0:
                                break

                        remainders.pop()

                        for reverse in reversed(remainders):
                            reversed_remainders.append(reverse)

                        float_num = float(float_num)

                        for repetation in range(15):
                            float_num = float_num * ending_base
                            float_num = str(float_num)
                            first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                            first_part_of_float_list.append(int(first_part_of_float_num))
                            float_num = str(0) + "." + second_part_of_float_num
                            second_part_of_float_num = str(0) + "." + str(second_part_of_float_num)
                            float_num = float(float_num)

                        for integer_part_of_reversed_remainders in reversed_remainders:
                            integer_part_of_reversed_remainders_list.append(str(integer_part_of_reversed_remainders))
                        integer_part_of_reversed_remainders_list.append(".")

                        for float_num_in_row in first_part_of_float_list:
                            float_num_in_row_list.append(float_num_in_row)

                        if float_num_in_row_list and all(elements == 0 for elements in float_num_in_row_list):
                            integer_part_of_reversed_remainders_list.pop()

                            number_shower.delete(0, END)
                            for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                                number_shower.insert(END, str(integer_part_of_reversed_remainders_in_row))


                        else:
                            number_shower.delete(0, END)
                            for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                                number_shower.insert(END, str(integer_part_of_reversed_remainders_in_row))

                            for float_num_in_row in float_num_in_row_list:
                                number_shower.insert(END, str(float_num_in_row))

                    def Base_2__9_9__2(starting_base, ending_base):
                        remainders = []
                        integer_list = []
                        float_list = []
                        integer_sum = 0
                        float_sum = 0
                        integer_power = 0
                        float_power = 0

                        num = number_to_be_converted
                        if "." not in num:
                            num = num + "." + str(0)

                        integer_num, float_num = num.split(".")

                        for lenght_integer in integer_num:
                            integer_list.append(int(lenght_integer))

                        for lenght_decimal in float_num:
                            float_list.append(int(lenght_decimal))

                        if float_list == ["0"]:
                            float_list = []

                        while len(integer_list) != 0:
                            integer_sum = (integer_list[-1]) * (starting_base ** integer_power) + integer_sum
                            integer_power += 1
                            integer_list.pop()

                        if len(float_list) != 0:
                            float_power = -abs(len(float_list))
                            while len(float_list) != 0:
                                float_sum = (float_list[-1]) * (starting_base ** float_power) + float_sum
                                float_power += 1
                                float_list.pop()

                        if float_sum == 0:
                            Base_2__9_10_answer = integer_sum
                        else:
                            Base_2__9_10_answer = integer_sum + float_sum

                        if isinstance(Base_2__9_10_answer, int):
                            num = Base_2__9_10_answer
                            while True:
                                remainder = int(num % ending_base)
                                num = int(num / ending_base)
                                remainders.append(remainder)
                                if num / ending_base == 0:
                                    break

                            number_shower.delete(0, END)
                            for reverse in reversed(remainders):
                                number_shower.insert(END, str(reverse))


                        else:
                            Base_2__9_10_answer = str(Base_2__9_10_answer)
                            integer_part_of_reversed_remainders_list = []
                            float_num_in_row_list = []
                            reversed_remainders = []
                            first_part_of_float_list = []
                            remainders = []

                            num = Base_2__9_10_answer

                            if "." not in num:
                                num = num + "." + str(0)

                            integer_num, float_num = num.split(".")

                            float_num = str(0) + "." + str(float_num)

                            while True:
                                integer_remainder = int(integer_num) % ending_base
                                integer_num = int(integer_num) / ending_base
                                remainders.append(integer_remainder)
                                if integer_num / ending_base == 0:
                                    break

                            remainders.pop()

                            for reverse in reversed(remainders):
                                reversed_remainders.append(reverse)

                            float_num = float(float_num)

                            for repetation in range(15):
                                float_num = float_num * ending_base
                                float_num = str(float_num)
                                first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                                first_part_of_float_list.append(int(first_part_of_float_num))
                                float_num = str(0) + "." + second_part_of_float_num
                                second_part_of_float_num = str(0) + "." + str(second_part_of_float_num)
                                float_num = float(float_num)

                            for integer_part_of_reversed_remainders in reversed_remainders:
                                integer_part_of_reversed_remainders_list.append(
                                    str(integer_part_of_reversed_remainders))
                            integer_part_of_reversed_remainders_list.append(".")

                            for float_num_in_row in first_part_of_float_list:
                                float_num_in_row_list.append(float_num_in_row)

                            if float_num_in_row_list and all(elements == 0 for elements in float_num_in_row_list):
                                integer_part_of_reversed_remainders_list.pop()

                                number_shower.delete(0, END)
                                for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                                    number_shower.insert(END, str(integer_part_of_reversed_remainders_in_row))


                            else:
                                number_shower.delete(0, END)
                                for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                                    number_shower.insert(END, str(integer_part_of_reversed_remainders_in_row))

                                for float_num_in_row in float_num_in_row_list:
                                    number_shower.insert(END, str(float_num_in_row))

                    def base_36__11_10(starting_base):
                        integer_list_1 = []
                        integer_list_2 = []
                        integer_list_3 = []
                        float_list_1 = []
                        float_list_2 = []
                        float_list_3 = []
                        integer_sum = 0
                        integer_power = 0
                        float_sum = 0
                        float_power = 0
                        numbers_dictionary = {}
                        numbers_values = 0
                        alphabets_dictionary = {}
                        alphabets_values = 10

                        for i in range(0, 10):
                            numbers_dictionary.update({int(i): int(numbers_values)})
                            numbers_values += 1

                        for j in string.ascii_uppercase:
                            alphabets_dictionary.update({str(j): int(alphabets_values)})
                            alphabets_values += 1

                        final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

                        num = number_to_be_converted
                        num = num.upper()

                        if "." not in num:
                            for i in num:
                                integer_list_1.append(i)

                            for j in integer_list_1:
                                if j.isalpha():
                                    integer_list_2.append(j)

                                if j.isnumeric():
                                    integer_list_2.append(int(j))

                            for a in integer_list_2:
                                for b in final_dictionary:
                                    if a == b:
                                        integer_list_3.append(final_dictionary[b])

                            while len(integer_list_3) != 0:
                                integer_sum = integer_sum + (integer_list_3[-1] * (starting_base ** integer_power))
                                integer_power += 1
                                integer_list_3.pop()
                            number_shower.delete(0, END)
                            number_shower.insert(END, str(integer_sum))


                        else:
                            integer_part, float_part = num.split(".")

                            for i in integer_part:
                                integer_list_1.append(i)

                            for j in integer_list_1:
                                if j.isalpha():
                                    integer_list_2.append(j)

                                if j.isnumeric():
                                    integer_list_2.append(int(j))

                            for a in integer_list_2:
                                for b in final_dictionary:
                                    if a == b:
                                        integer_list_3.append(final_dictionary[b])

                            while len(integer_list_3) != 0:
                                integer_sum = integer_sum + (integer_list_3[-1] * (starting_base ** integer_power))
                                integer_power += 1
                                integer_list_3.pop()

                            for x in float_part:
                                float_list_1.append(x)

                            for y in float_list_1:
                                if y.isalpha():
                                    float_list_2.append(y)

                                if y.isnumeric():
                                    float_list_2.append(int(y))

                            for z in float_list_2:
                                for t in final_dictionary:
                                    if z == t:
                                        float_list_3.append(final_dictionary[t])

                            float_power = -abs(len(float_list_3))

                            while len(float_list_3) != 0:
                                float_sum = float_sum + (float_list_3[-1]) * (starting_base ** float_power)
                                float_power += 1
                                float_list_3.pop()

                            number_shower.delete(0, END)
                            number_shower.insert(END, str(integer_sum + float_sum))

                    def base_10_11__36(ending_base):
                        numbers_dictionary = {}
                        numbers_values = 0
                        alphabets_dictionary = {}
                        alphabets_values = 10
                        remainders = []
                        reversed_remainders = []
                        none_dot_final_list = []
                        first_part_of_float_num_list = []
                        int_first_part_of_float_num_list = []
                        value_of_first_part_of_float_num_list = []
                        integer_remainders = []
                        final_integer_remainders_list = []
                        value_of_final_integer_remainders_list = []

                        for i in range(0, 10):
                            numbers_dictionary.update({int(numbers_values): int(i)})
                            numbers_values += 1

                        for j in string.ascii_uppercase:
                            alphabets_dictionary.update({int(alphabets_values): str(j)})
                            alphabets_values += 1

                        final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

                        num = number_to_be_converted

                        if "." not in num:
                            while True:
                                remainder = int(num) % ending_base
                                num = int(num) / ending_base
                                remainders.append(remainder)
                                if num / ending_base == 0:
                                    break
                            remainders.pop()

                            for i in reversed(remainders):
                                reversed_remainders.append(i)

                            for j in reversed_remainders:
                                for t in final_dictionary:
                                    if j == t:
                                        none_dot_final_list.append(final_dictionary[t])

                            number_shower.delete(0, END)
                            for x in none_dot_final_list:
                                number_shower.insert(END, str(x))

                        else:
                            integer_num, float_num = num.split(".")
                            integer_num = int(integer_num)
                            float_num = str("0") + "." + float_num
                            float_num = float(float_num)

                            while True:
                                integer_remainder = int(integer_num) % ending_base
                                integer_num = int(integer_num) / ending_base
                                integer_remainders.append(integer_remainder)
                                if integer_num / ending_base == 0:
                                    break
                            integer_remainders.pop()

                            for k in reversed(integer_remainders):
                                final_integer_remainders_list.append(k)

                            for h in final_integer_remainders_list:
                                for n in final_dictionary:
                                    if h == n:
                                        value_of_final_integer_remainders_list.append(final_dictionary[n])
                            value_of_final_integer_remainders_list.append(".")

                            for i in range(15):
                                float_num = float_num * ending_base
                                float_num = str(float_num)
                                first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                                second_part_of_float_num = str(second_part_of_float_num)
                                second_part_of_float_num = str("0") + "." + second_part_of_float_num
                                first_part_of_float_num_list.append(first_part_of_float_num)
                                float_num = second_part_of_float_num
                                float_num = float(float_num)

                            for j in first_part_of_float_num_list:
                                int_first_part_of_float_num_list.append(int(j))

                            for x in int_first_part_of_float_num_list:
                                for y in final_dictionary:
                                    if x == y:
                                        value_of_first_part_of_float_num_list.append(final_dictionary[y])

                            answer_list = value_of_final_integer_remainders_list + value_of_first_part_of_float_num_list

                            number_shower.delete(0, END)
                            for f in answer_list:
                                number_shower.insert(END, str(f))

                    def base_11__36_36__11(starting_base, ending_base):
                        integer_list_1 = []
                        integer_list_2 = []
                        integer_list_3 = []
                        float_list_1 = []
                        float_list_2 = []
                        float_list_3 = []
                        integer_sum = 0
                        integer_power = 0
                        float_sum = 0
                        float_power = 0
                        numbers_dictionary = {}
                        numbers_values = 0
                        alphabets_dictionary = {}
                        alphabets_values = 10

                        for i in range(0, 10):
                            numbers_dictionary.update({int(i): int(numbers_values)})
                            numbers_values += 1

                        for j in string.ascii_uppercase:
                            alphabets_dictionary.update({str(j): int(alphabets_values)})
                            alphabets_values += 1

                        final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

                        num = number_to_be_converted
                        num = num.upper()

                        if "." not in num:
                            for i in num:
                                integer_list_1.append(i)

                            for j in integer_list_1:
                                if j.isalpha():
                                    integer_list_2.append(j)

                                if j.isnumeric():
                                    integer_list_2.append(int(j))

                            for a in integer_list_2:
                                for b in final_dictionary:
                                    if a == b:
                                        integer_list_3.append(final_dictionary[b])

                            while len(integer_list_3) != 0:
                                integer_sum = integer_sum + (integer_list_3[-1] * (starting_base ** integer_power))
                                integer_power += 1
                                integer_list_3.pop()

                            answer = integer_sum

                        else:
                            integer_part, float_part = num.split(".")

                            for i in integer_part:
                                integer_list_1.append(i)

                            for j in integer_list_1:
                                if j.isalpha():
                                    integer_list_2.append(j)

                                if j.isnumeric():
                                    integer_list_2.append(int(j))

                            for a in integer_list_2:
                                for b in final_dictionary:
                                    if a == b:
                                        integer_list_3.append(final_dictionary[b])

                            while len(integer_list_3) != 0:
                                integer_sum = integer_sum + (integer_list_3[-1] * (starting_base ** integer_power))
                                integer_power += 1
                                integer_list_3.pop()

                            for x in float_part:
                                float_list_1.append(x)

                            for y in float_list_1:
                                if y.isalpha():
                                    float_list_2.append(y)

                                if y.isnumeric():
                                    float_list_2.append(int(y))

                            for z in float_list_2:
                                for t in final_dictionary:
                                    if z == t:
                                        float_list_3.append(final_dictionary[t])

                            float_power = -abs(len(float_list_3))

                            while len(float_list_3) != 0:
                                float_sum = float_sum + (float_list_3[-1]) * (starting_base ** float_power)
                                float_power += 1
                                float_list_3.pop()

                            answer = integer_sum + float_sum

                        numbers_dictionary = {}
                        numbers_values = 0
                        alphabets_dictionary = {}
                        alphabets_values = 10
                        remainders = []
                        reversed_remainders = []
                        none_dot_final_list = []
                        first_part_of_float_num_list = []
                        int_first_part_of_float_num_list = []
                        value_of_first_part_of_float_num_list = []
                        integer_remainders = []
                        final_integer_remainders_list = []
                        value_of_final_integer_remainders_list = []

                        for i in range(0, 10):
                            numbers_dictionary.update({int(numbers_values): int(i)})
                            numbers_values += 1

                        for j in string.ascii_uppercase:
                            alphabets_dictionary.update({int(alphabets_values): str(j)})
                            alphabets_values += 1

                        final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

                        num = str(answer)

                        if "." not in num:
                            while True:
                                remainder = int(num) % ending_base
                                num = int(num) / ending_base
                                remainders.append(remainder)
                                if num / ending_base == 0:
                                    break
                            remainders.pop()

                            for i in reversed(remainders):
                                reversed_remainders.append(i)

                            for j in reversed_remainders:
                                for t in final_dictionary:
                                    if j == t:
                                        none_dot_final_list.append(final_dictionary[t])

                            x_list = []
                            for x in none_dot_final_list:
                                x_list.append(x)

                            ans = "".join((map(str, x_list)))

                            number_shower.delete(0, END)
                            number_shower.insert(END, str(ans))

                        else:
                            integer_num, float_num = num.split(".")
                            integer_num = int(integer_num)
                            float_num = str("0") + "." + float_num
                            float_num = float(float_num)

                            while True:
                                integer_remainder = int(integer_num) % ending_base
                                integer_num = int(integer_num) / ending_base
                                integer_remainders.append(integer_remainder)
                                if integer_num / ending_base == 0:
                                    break
                            integer_remainders.pop()

                            for k in reversed(integer_remainders):
                                final_integer_remainders_list.append(k)

                            for h in final_integer_remainders_list:
                                for n in final_dictionary:
                                    if h == n:
                                        value_of_final_integer_remainders_list.append(final_dictionary[n])
                            value_of_final_integer_remainders_list.append(".")

                            for i in range(15):
                                float_num = float_num * ending_base
                                float_num = str(float_num)
                                first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                                second_part_of_float_num = str(second_part_of_float_num)
                                second_part_of_float_num = str("0") + "." + second_part_of_float_num
                                first_part_of_float_num_list.append(first_part_of_float_num)
                                float_num = second_part_of_float_num
                                float_num = float(float_num)

                            for j in first_part_of_float_num_list:
                                int_first_part_of_float_num_list.append(int(j))

                            for x in int_first_part_of_float_num_list:
                                for y in final_dictionary:
                                    if x == y:
                                        value_of_first_part_of_float_num_list.append(final_dictionary[y])

                            answer_list = value_of_final_integer_remainders_list + value_of_first_part_of_float_num_list

                            y_list = []

                            for f in answer_list:
                                y_list.append(f)

                            ans = "".join((map(str, y_list)))

                            number_shower.delete(0, END)
                            number_shower.insert(END, str(ans))

                    def base_2_9__11_36(starting_base, ending_base):
                        integer_list = []
                        float_list = []
                        integer_sum = 0
                        float_sum = 0
                        integer_power = 0
                        float_power = 0

                        num = number_to_be_converted
                        if "." not in num:
                            num = num + "." + str(0)

                        integer_num, float_num = num.split(".")

                        for lenght_integer in integer_num:
                            integer_list.append(int(lenght_integer))

                        for lenght_decimal in float_num:
                            float_list.append(int(lenght_decimal))

                        if float_list == ["0"]:
                            float_list = []

                        while len(integer_list) != 0:
                            integer_sum = (integer_list[-1]) * (starting_base ** integer_power) + integer_sum
                            integer_power += 1
                            integer_list.pop()

                        if len(float_list) != 0:
                            float_power = -abs(len(float_list))
                            while len(float_list) != 0:
                                float_sum = (float_list[-1]) * (starting_base ** float_power) + float_sum
                                float_power += 1
                                float_list.pop()

                        if float_sum == 0:
                            answer = integer_sum
                        else:
                            answer = integer_sum + float_sum

                        numbers_dictionary = {}
                        numbers_values = 0
                        alphabets_dictionary = {}
                        alphabets_values = 10
                        remainders = []
                        reversed_remainders = []
                        none_dot_final_list = []
                        first_part_of_float_num_list = []
                        int_first_part_of_float_num_list = []
                        value_of_first_part_of_float_num_list = []
                        integer_remainders = []
                        final_integer_remainders_list = []
                        value_of_final_integer_remainders_list = []

                        for i in range(0, 10):
                            numbers_dictionary.update({int(numbers_values): int(i)})
                            numbers_values += 1

                        for j in string.ascii_uppercase:
                            alphabets_dictionary.update({int(alphabets_values): str(j)})
                            alphabets_values += 1

                        final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

                        num = answer
                        num = str(num)

                        if "." not in num:
                            while True:
                                remainder = int(num) % ending_base
                                num = int(num) / ending_base
                                remainders.append(remainder)
                                if num / ending_base == 0:
                                    break
                            remainders.pop()

                            for i in reversed(remainders):
                                reversed_remainders.append(i)

                            for j in reversed_remainders:
                                for t in final_dictionary:
                                    if j == t:
                                        none_dot_final_list.append(final_dictionary[t])

                            number_shower.delete(0, END)
                            for x in none_dot_final_list:
                                number_shower.insert(END, str(x))

                        else:
                            integer_num, float_num = num.split(".")
                            integer_num = int(integer_num)
                            float_num = str("0") + "." + float_num
                            float_num = float(float_num)

                            while True:
                                integer_remainder = int(integer_num) % ending_base
                                integer_num = int(integer_num) / ending_base
                                integer_remainders.append(integer_remainder)
                                if integer_num / ending_base == 0:
                                    break
                            integer_remainders.pop()

                            for k in reversed(integer_remainders):
                                final_integer_remainders_list.append(k)

                            for h in final_integer_remainders_list:
                                for n in final_dictionary:
                                    if h == n:
                                        value_of_final_integer_remainders_list.append(final_dictionary[n])
                            value_of_final_integer_remainders_list.append(".")

                            for i in range(15):
                                float_num = float_num * ending_base
                                float_num = str(float_num)
                                first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                                second_part_of_float_num = str(second_part_of_float_num)
                                second_part_of_float_num = str("0") + "." + second_part_of_float_num
                                first_part_of_float_num_list.append(first_part_of_float_num)
                                float_num = second_part_of_float_num
                                float_num = float(float_num)

                            for j in first_part_of_float_num_list:
                                int_first_part_of_float_num_list.append(int(j))

                            for x in int_first_part_of_float_num_list:
                                for y in final_dictionary:
                                    if x == y:
                                        value_of_first_part_of_float_num_list.append(final_dictionary[y])

                            answer_list = value_of_final_integer_remainders_list + value_of_first_part_of_float_num_list

                            number_shower.delete(0, END)
                            for f in answer_list:
                                number_shower.insert(END, str(f))

                    def base_36__11_9__2(starting_base, ending_base):
                        integer_list_1 = []
                        integer_list_2 = []
                        integer_list_3 = []
                        float_list_1 = []
                        float_list_2 = []
                        float_list_3 = []
                        integer_sum = 0
                        integer_power = 0
                        float_sum = 0
                        float_power = 0
                        numbers_dictionary = {}
                        numbers_values = 0
                        alphabets_dictionary = {}
                        alphabets_values = 10

                        for i in range(0, 10):
                            numbers_dictionary.update({int(i): int(numbers_values)})
                            numbers_values += 1

                        for j in string.ascii_uppercase:
                            alphabets_dictionary.update({str(j): int(alphabets_values)})
                            alphabets_values += 1

                        final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

                        num = number_to_be_converted
                        num = num.upper()

                        if "." not in num:
                            for i in num:
                                integer_list_1.append(i)

                            for j in integer_list_1:
                                if j.isalpha():
                                    integer_list_2.append(j)

                                if j.isnumeric():
                                    integer_list_2.append(int(j))

                            for a in integer_list_2:
                                for b in final_dictionary:
                                    if a == b:
                                        integer_list_3.append(final_dictionary[b])

                            while len(integer_list_3) != 0:
                                integer_sum = integer_sum + (integer_list_3[-1] * (starting_base ** integer_power))
                                integer_power += 1
                                integer_list_3.pop()

                            answer = integer_sum

                        else:
                            integer_part, float_part = num.split(".")

                            for i in integer_part:
                                integer_list_1.append(i)

                            for j in integer_list_1:
                                if j.isalpha():
                                    integer_list_2.append(j)

                                if j.isnumeric():
                                    integer_list_2.append(int(j))

                            for a in integer_list_2:
                                for b in final_dictionary:
                                    if a == b:
                                        integer_list_3.append(final_dictionary[b])

                            while len(integer_list_3) != 0:
                                integer_sum = integer_sum + (integer_list_3[-1] * (starting_base ** integer_power))
                                integer_power += 1
                                integer_list_3.pop()

                            for x in float_part:
                                float_list_1.append(x)

                            for y in float_list_1:
                                if y.isalpha():
                                    float_list_2.append(y)

                                if y.isnumeric():
                                    float_list_2.append(int(y))

                            for z in float_list_2:
                                for t in final_dictionary:
                                    if z == t:
                                        float_list_3.append(final_dictionary[t])

                            float_power = -abs(len(float_list_3))

                            while len(float_list_3) != 0:
                                float_sum = float_sum + (float_list_3[-1]) * (starting_base ** float_power)
                                float_power += 1
                                float_list_3.pop()

                            answer = integer_sum + float_sum

                        integer_part_of_reversed_remainders_list = []
                        float_num_in_row_list = []
                        reversed_remainders = []
                        first_part_of_float_list = []
                        remainders = []

                        num = answer
                        num = str(num)

                        if "." not in num:
                            num = num + "." + str(0)

                        integer_num, float_num = num.split(".")

                        float_num = str(0) + "." + str(float_num)

                        while True:
                            integer_remainder = int(integer_num) % ending_base
                            integer_num = int(integer_num) / ending_base
                            remainders.append(integer_remainder)
                            if integer_num / ending_base == 0:
                                break

                        remainders.pop()

                        for reverse in reversed(remainders):
                            reversed_remainders.append(reverse)

                        float_num = float(float_num)

                        for repetation in range(15):
                            float_num = float_num * ending_base
                            float_num = str(float_num)
                            first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                            first_part_of_float_list.append(int(first_part_of_float_num))
                            float_num = str(0) + "." + second_part_of_float_num
                            second_part_of_float_num = str(0) + "." + str(second_part_of_float_num)
                            float_num = float(float_num)

                        for integer_part_of_reversed_remainders in reversed_remainders:
                            integer_part_of_reversed_remainders_list.append(str(integer_part_of_reversed_remainders))
                        integer_part_of_reversed_remainders_list.append(".")

                        for float_num_in_row in first_part_of_float_list:
                            float_num_in_row_list.append(float_num_in_row)

                        if float_num_in_row_list and all(elements == 0 for elements in float_num_in_row_list):
                            integer_part_of_reversed_remainders_list.pop()

                            number_shower.delete(0, END)
                            for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                                number_shower.insert(END, str(integer_part_of_reversed_remainders_in_row))

                        else:
                            number_shower.delete(0, END)
                            for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                                number_shower.insert(END, str(integer_part_of_reversed_remainders_in_row))

                            for float_num_in_row in float_num_in_row_list:
                                number_shower.insert(END, str(float_num_in_row))

                    def base_selectors():
                        if starting_base in range(2, 11) and ending_base == 10:
                            Base_2__9_10(starting_base)

                        if starting_base == 10 and ending_base in range(2, 11):
                            Base_10_2__9(ending_base)

                        if starting_base in range(2, 10) and ending_base in range(2, 10):
                            Base_2__9_9__2(starting_base, ending_base)

                        if starting_base in range(11, 37) and ending_base == 10:
                            base_36__11_10(starting_base)

                        if starting_base == 10 and ending_base in range(11, 37):
                            base_10_11__36(ending_base)

                        if starting_base in range(11, 37) and ending_base in range(11, 37):
                            base_11__36_36__11(starting_base, ending_base)

                        if starting_base in range(2, 10) and ending_base in range(11, 37):
                            base_2_9__11_36(starting_base, ending_base)

                        if starting_base in range(11, 37) and ending_base in range(2, 10):
                            base_36__11_9__2(starting_base, ending_base)

                    base_selectors()

                    if len(str(number_to_be_converted)) == 0:
                        number_shower.insert(0, "  Nothing to convert!")

                starting_base = int(from_base)
                ending_base = int(to_base)

                number_getter_screen = PhotoImage(
                    file=resource_path("Images\\number_getter.png"))
                number_getter_screen_label = Label(root, image=number_getter_screen)
                number_getter_screen_label.place(x=-15, y=-7)

                number_entry = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 23), bg="#474747",
                                     foreground="#ffffff")
                number_entry.place(x=50, y=410, height=40, width=370)

                convert = PhotoImage(file=resource_path("Images\\convert.png"))
                convert_label = Label(image=convert, borderwidth=0)
                convert_label.place(x=175, y=465)
                real_convert = Button(root, image=convert, borderwidth=0, background="black",
                                      activebackground="black", command=converter)
                real_convert.place(x=175, y=465)

                button_calculator_icon = PhotoImage(file=resource_path(f"Images\\calculator_icon.png"))
                button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"#BC0000")
                button_calculator_icon_label.place(x=10, y=0)
                real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                     bg=f"#BC0000",
                                                     activebackground=f"#BC0000", command=cal_screen)
                real_button_calculator_icon.place(x=10, y=0)

                button_equation_icon = PhotoImage(file=resource_path(f"Images\\equation_icon.png"))
                button_equation_icon_label = Label(image=button_equation_icon, bg=f"#BC0000")
                button_equation_icon_label.place(x=190, y=3)
                real_button_equation_icon = Button(root, image=button_equation_icon, borderwidth=0,
                                                   bg=f"#BC0000",
                                                   activebackground=f"#BC0000", command=equation)
                real_button_equation_icon.place(x=190, y=3)

                button_integral_icon = PhotoImage(file=resource_path(f"Images\\integral_icon.png"))
                button_integral_icon_label = Label(image=button_integral_icon, bg=f"#BC0000")
                button_integral_icon_label.place(x=385, y=2)
                real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0,
                                                   bg=f"#BC0000",
                                                   activebackground=f"#BC0000")
                real_button_integral_icon.place(x=385, y=2)

            # body_theme_selector = [1, 2, 3, 4]
            # body_theme_selected = random.choice(body_theme_selector)

            button_calculator_icon = "calculator_icon"
            button_equation_icon = "equation_icon"
            button_base_converter_icon = "base_converter_icon"
            button_integral_icon = "integral_icon"

            if body_theme_selected == 1:
                base_converter_screen = PhotoImage(file=resource_path("Images\\to_base_screen_start.png"))
                base_converter_screen_label = Label(root, image=base_converter_screen)
                base_converter_screen_label.place(x=-15, y=-7)
                header_bg_code = "#021A98"
                background_bg_code = "#49381E"
                b_c_d = "b"

            if body_theme_selected == 2:
                base_converter_screen = PhotoImage(
                    file=resource_path("Images\\to_base_screen_start_to_base_screen_start.png"))
                base_converter_screen_label = Label(root, image=base_converter_screen)
                base_converter_screen_label.place(x=-15, y=-7)
                header_bg_code = "#8C9802"
                background_bg_code = "#002744"
                b_c_d = "c"

            if body_theme_selected == 3:
                base_converter_screen = PhotoImage(
                    file=resource_path("Images\\to_base_screen_start_to_base_screen_start_to_base_screen_start.png"))
                base_converter_screen_label = Label(root, image=base_converter_screen)
                base_converter_screen_label.place(x=-15, y=-7)
                header_bg_code = "#0A970F"
                background_bg_code = "#5B2960"
                b_c_d = "d"

            if body_theme_selected == 4:
                base_converter_screen = PhotoImage(
                    file=resource_path(
                        "Images\\to_base_screen_start_to_base_screen_start_to_base_screen_start_to_base_screen_start.png"))
                base_converter_screen_label = Label(root, image=base_converter_screen)
                base_converter_screen_label.place(x=-15, y=-7)
                header_bg_code = "#DD6711"
                background_bg_code = "#313131"
                b_c_d = "b"

            to_1 = PhotoImage(file=resource_path(f"Images\\1{b_c_d}.png"))
            to_1_label = Label(image=to_1, borderwidth=0)
            to_1_label.place(x=0, y=110 + 70)
            real_to_1 = Button(root, image=to_1, borderwidth=0, background=background_bg_code,
                               activebackground=background_bg_code, )
            real_to_1.place(x=0, y=110 + 70)

            to_2 = PhotoImage(file=resource_path(f"Images\\2{b_c_d}.png"))
            to_2_label = Label(image=to_2, borderwidth=0)
            to_2_label.place(x=0, y=170 + 70)
            real_to_2 = Button(root, image=to_2, borderwidth=0, background=background_bg_code,
                               activebackground=background_bg_code, command=lambda: to_base_data_getter(2))
            real_to_2.place(x=0, y=170 + 70)

            to_3 = PhotoImage(file=resource_path(f"Images\\3{b_c_d}.png"))
            to_3_label = Label(image=to_3, borderwidth=0)
            to_3_label.place(x=0, y=230 + 70)
            real_to_3 = Button(root, image=to_3, borderwidth=0, background=background_bg_code,
                               activebackground=background_bg_code, command=lambda: to_base_data_getter(3))
            real_to_3.place(x=0, y=230 + 70)

            to_4 = PhotoImage(file=resource_path(f"Images\\4{b_c_d}.png"))
            to_4_label = Label(image=to_4, borderwidth=0)
            to_4_label.place(x=0, y=290 + 70)
            real_to_4 = Button(root, image=to_4, borderwidth=0, background=background_bg_code,
                               activebackground=background_bg_code, command=lambda: to_base_data_getter(4))
            real_to_4.place(x=0, y=290 + 70)

            to_5 = PhotoImage(file=resource_path(f"Images\\5{b_c_d}.png"))
            to_5_label = Label(image=to_5, borderwidth=0)
            to_5_label.place(x=0, y=350 + 70)
            real_to_5 = Button(root, image=to_5, borderwidth=0, background=background_bg_code,
                               activebackground=background_bg_code, command=lambda: to_base_data_getter(5))
            real_to_5.place(x=0, y=350 + 70)

            to_6 = PhotoImage(file=resource_path(f"Images\\6{b_c_d}.png"))
            to_6_label = Label(image=to_6, borderwidth=0)
            to_6_label.place(x=0, y=410 + 70)
            real_to_6 = Button(root, image=to_6, borderwidth=0, background=background_bg_code,
                               activebackground=background_bg_code, command=lambda: to_base_data_getter(6))
            real_to_6.place(x=0, y=410 + 70)

            to_7 = PhotoImage(file=resource_path(f"Images\\7{b_c_d}.png"))
            to_7_label = Label(image=to_7, borderwidth=0)
            to_7_label.place(x=80, y=110 + 70)
            real_to_7 = Button(root, image=to_7, borderwidth=0, background=background_bg_code,
                               activebackground=background_bg_code, command=lambda: to_base_data_getter(7))
            real_to_7.place(x=80, y=110 + 70)

            to_8 = PhotoImage(file=resource_path(f"Images\\8{b_c_d}.png"))
            to_8_label = Label(image=to_8, borderwidth=0)
            to_8_label.place(x=80, y=170 + 70)
            real_to_8 = Button(root, image=to_8, borderwidth=0, background=background_bg_code,
                               activebackground=background_bg_code, command=lambda: to_base_data_getter(8))
            real_to_8.place(x=80, y=170 + 70)

            to_9 = PhotoImage(file=resource_path(f"Images\\9{b_c_d}.png"))
            to_9_label = Label(image=to_9, borderwidth=0)
            to_9_label.place(x=80, y=230 + 70)
            real_to_9 = Button(root, image=to_9, borderwidth=0, background=background_bg_code,
                               activebackground=background_bg_code, command=lambda: to_base_data_getter(9))
            real_to_9.place(x=80, y=230 + 70)

            to_10 = PhotoImage(file=resource_path(f"Images\\10{b_c_d}.png"))
            to_10_label = Label(image=to_10, borderwidth=0)
            to_10_label.place(x=80, y=290 + 70)
            real_to_10 = Button(root, image=to_10, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(10))
            real_to_10.place(x=80, y=290 + 70)

            to_11 = PhotoImage(file=resource_path(f"Images\\11{b_c_d}.png"))
            to_11_label = Label(image=to_11, borderwidth=0)
            to_11_label.place(x=80, y=350 + 70)
            real_to_11 = Button(root, image=to_11, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(11))
            real_to_11.place(x=80, y=350 + 70)

            to_12 = PhotoImage(file=resource_path(f"Images\\12{b_c_d}.png"))
            to_12_label = Label(image=to_12, borderwidth=0)
            to_12_label.place(x=80, y=410 + 70)
            real_to_12 = Button(root, image=to_12, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(12))
            real_to_12.place(x=80, y=410 + 70)

            to_13 = PhotoImage(file=resource_path(f"Images\\13{b_c_d}.png"))
            to_13_label = Label(image=to_13, borderwidth=0)
            to_13_label.place(x=160, y=110 + 70)
            real_to_13 = Button(root, image=to_13, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(13))
            real_to_13.place(x=160, y=110 + 70)

            to_14 = PhotoImage(file=resource_path(f"Images\\14{b_c_d}.png"))
            to_14_label = Label(image=to_14, borderwidth=0)
            to_14_label.place(x=160, y=170 + 70)
            real_to_14 = Button(root, image=to_14, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(14))
            real_to_14.place(x=160, y=170 + 70)

            to_15 = PhotoImage(file=resource_path(f"Images\\15{b_c_d}.png"))
            to_15_label = Label(image=to_15, borderwidth=0)
            to_15_label.place(x=160, y=230 + 70)
            real_to_15 = Button(root, image=to_15, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(15))
            real_to_15.place(x=160, y=230 + 70)

            to_16 = PhotoImage(file=resource_path(f"Images\\16{b_c_d}.png"))
            to_16_label = Label(image=to_16, borderwidth=0)
            to_16_label.place(x=160, y=290 + 70)
            real_to_16 = Button(root, image=to_16, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(16))
            real_to_16.place(x=160, y=290 + 70)

            to_17 = PhotoImage(file=resource_path(f"Images\\17{b_c_d}.png"))
            to_17_label = Label(image=to_17, borderwidth=0)
            to_17_label.place(x=160, y=350 + 70)
            real_to_17 = Button(root, image=to_17, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(17))
            real_to_17.place(x=160, y=350 + 70)

            to_18 = PhotoImage(file=resource_path(f"Images\\18{b_c_d}.png"))
            to_18_label = Label(image=to_18, borderwidth=0)
            to_18_label.place(x=160, y=410 + 70)
            real_to_18 = Button(root, image=to_18, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(18))
            real_to_18.place(x=160, y=410 + 70)

            to_19 = PhotoImage(file=resource_path(f"Images\\19{b_c_d}.png"))
            to_19_label = Label(image=to_19, borderwidth=0)
            to_19_label.place(x=240, y=110 + 70)
            real_to_19 = Button(root, image=to_19, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(19))
            real_to_19.place(x=240, y=110 + 70)

            to_20 = PhotoImage(file=resource_path(f"Images\\20{b_c_d}.png"))
            to_20_label = Label(image=to_20, borderwidth=0)
            to_20_label.place(x=240, y=170 + 70)
            real_to_20 = Button(root, image=to_20, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(20))
            real_to_20.place(x=240, y=170 + 70)

            to_21 = PhotoImage(file=resource_path(f"Images\\21{b_c_d}.png"))
            to_21_label = Label(image=to_21, borderwidth=0)
            to_21_label.place(x=240, y=230 + 70)
            real_to_21 = Button(root, image=to_21, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(21))
            real_to_21.place(x=240, y=230 + 70)

            to_22 = PhotoImage(file=resource_path(f"Images\\22{b_c_d}.png"))
            to_22_label = Label(image=to_22, borderwidth=0)
            to_22_label.place(x=240, y=290 + 70)
            real_to_22 = Button(root, image=to_22, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(22))
            real_to_22.place(x=240, y=290 + 70)

            to_23 = PhotoImage(file=resource_path(f"Images\\23{b_c_d}.png"))
            to_23_label = Label(image=to_23, borderwidth=0)
            to_23_label.place(x=240, y=350 + 70)
            real_to_23 = Button(root, image=to_23, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(23))
            real_to_23.place(x=240, y=350 + 70)

            to_24 = PhotoImage(file=resource_path(f"Images\\24{b_c_d}.png"))
            to_24_label = Label(image=to_24, borderwidth=0)
            to_24_label.place(x=240, y=410 + 70)
            real_to_24 = Button(root, image=to_24, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(24))
            real_to_24.place(x=240, y=410 + 70)

            to_25 = PhotoImage(file=resource_path(f"Images\\25{b_c_d}.png"))
            to_25_label = Label(image=to_25, borderwidth=0)
            to_25_label.place(x=320, y=110 + 70)
            real_to_25 = Button(root, image=to_25, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(25))
            real_to_25.place(x=320, y=110 + 70)

            to_26 = PhotoImage(file=resource_path(f"Images\\26{b_c_d}.png"))
            to_26_label = Label(image=to_26, borderwidth=0)
            to_26_label.place(x=320, y=170 + 70)
            real_to_26 = Button(root, image=to_26, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(26))
            real_to_26.place(x=320, y=170 + 70)

            to_27 = PhotoImage(file=resource_path(f"Images\\27{b_c_d}.png"))
            to_27_label = Label(image=to_27, borderwidth=0)
            to_27_label.place(x=320, y=230 + 70)
            real_to_27 = Button(root, image=to_27, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(27))
            real_to_27.place(x=320, y=230 + 70)

            to_28 = PhotoImage(file=resource_path(f"Images\\28{b_c_d}.png"))
            to_28_label = Label(image=to_28, borderwidth=0)
            to_28_label.place(x=320, y=290 + 70)
            real_to_28 = Button(root, image=to_28, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(28))
            real_to_28.place(x=320, y=290 + 70)

            to_29 = PhotoImage(file=resource_path(f"Images\\29{b_c_d}.png"))
            to_29_label = Label(image=to_29, borderwidth=0)
            to_29_label.place(x=320, y=350 + 70)
            real_to_29 = Button(root, image=to_29, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(29))
            real_to_29.place(x=320, y=350 + 70)

            to_30 = PhotoImage(file=resource_path(f"Images\\30{b_c_d}.png"))
            to_30_label = Label(image=to_30, borderwidth=0)
            to_30_label.place(x=320, y=410 + 70)
            real_to_30 = Button(root, image=to_30, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(30))
            real_to_30.place(x=320, y=410 + 70)

            to_31 = PhotoImage(file=resource_path(f"Images\\31{b_c_d}.png"))
            to_31_label = Label(image=to_31, borderwidth=0)
            to_31_label.place(x=400, y=110 + 70)
            real_to_31 = Button(root, image=to_31, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(31))
            real_to_31.place(x=400, y=110 + 70)

            to_32 = PhotoImage(file=resource_path(f"Images\\32{b_c_d}.png"))
            to_32_label = Label(image=to_32, borderwidth=0)
            to_32_label.place(x=400, y=170 + 70)
            real_to_32 = Button(root, image=to_32, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(32))
            real_to_32.place(x=400, y=170 + 70)

            to_33 = PhotoImage(file=resource_path(f"Images\\33{b_c_d}.png"))
            to_33_label = Label(image=to_33, borderwidth=0)
            to_33_label.place(x=400, y=230 + 70)
            real_to_33 = Button(root, image=to_33, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(33))
            real_to_33.place(x=400, y=230 + 70)

            to_34 = PhotoImage(file=resource_path(f"Images\\34{b_c_d}.png"))
            to_34_label = Label(image=to_34, borderwidth=0)
            to_34_label.place(x=400, y=290 + 70)
            real_to_34 = Button(root, image=to_34, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(34))
            real_to_34.place(x=400, y=290 + 70)

            to_35 = PhotoImage(file=resource_path(f"Images\\35{b_c_d}.png"))
            to_35_label = Label(image=to_35, borderwidth=0)
            to_35_label.place(x=400, y=350 + 70)
            real_to_35 = Button(root, image=to_35, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(35))
            real_to_35.place(x=400, y=350 + 70)

            to_36 = PhotoImage(file=resource_path(f"Images\\36{b_c_d}.png"))
            to_36_label = Label(image=to_36, borderwidth=0)
            to_36_label.place(x=400, y=410 + 70)
            real_to_36 = Button(root, image=to_36, borderwidth=0, background=background_bg_code,
                                activebackground=background_bg_code, command=lambda: to_base_data_getter(36))
            real_to_36.place(x=400, y=410 + 70)

            button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
            button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
            button_calculator_icon_label.place(x=10, y=0)
            real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0,
                                                 bg=f"{header_bg_code}",
                                                 activebackground=f"{header_bg_code}", command=cal_screen)
            real_button_calculator_icon.place(x=10, y=0)

            button_equation_icon = PhotoImage(file=resource_path(f"Images\\{button_equation_icon}.png"))
            button_equation_icon_label = Label(image=button_equation_icon, bg=f"{header_bg_code}")
            button_equation_icon_label.place(x=190, y=3)
            real_button_equation_icon = Button(root, image=button_equation_icon, borderwidth=0, bg=f"{header_bg_code}",
                                               activebackground=f"{header_bg_code}", command=equation)
            real_button_equation_icon.place(x=190, y=3)

            button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
            button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
            button_integral_icon_label.place(x=385, y=2)
            real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0, bg=f"{header_bg_code}",
                                               activebackground=f"{header_bg_code}")
            real_button_integral_icon.place(x=385, y=2)

        body_theme_selector = [1, 2, 3, 4]
        body_theme_selected = random.choice(body_theme_selector)

        button_calculator_icon = "calculator_icon"
        button_equation_icon = "equation_icon"
        button_base_converter_icon = "base_converter_icon"
        button_integral_icon = "integral_icon"

        if body_theme_selected == 1:
            base_converter_screen = PhotoImage(file=resource_path("Images\\from_base_screen_start.png"))
            base_converter_screen_label = Label(root, image=base_converter_screen)
            base_converter_screen_label.place(x=-15, y=-7)
            header_bg_code = "#021A98"
            background_bg_code = "#49381E"
            b_c_d = "b"

        if body_theme_selected == 2:
            base_converter_screen = PhotoImage(
                file=resource_path("Images\\from_base_screen_start_from_base_screen_start.png"))
            base_converter_screen_label = Label(root, image=base_converter_screen)
            base_converter_screen_label.place(x=-15, y=-7)
            header_bg_code = "#8C9802"
            background_bg_code = "#002744"
            b_c_d = "c"

        if body_theme_selected == 3:
            base_converter_screen = PhotoImage(
                file=resource_path("Images\\from_base_screen_start_from_base_screen_start_from_base_screen_start.png"))
            base_converter_screen_label = Label(root, image=base_converter_screen)
            base_converter_screen_label.place(x=-15, y=-7)
            header_bg_code = "#0A970F"
            background_bg_code = "#5B2960"
            b_c_d = "d"

        if body_theme_selected == 4:
            base_converter_screen = PhotoImage(
                file=resource_path(
                    "Images\\from_base_screen_start_from_base_screen_start_from_base_screen_start_from_base_screen_start.png"))
            base_converter_screen_label = Label(root, image=base_converter_screen)
            base_converter_screen_label.place(x=-15, y=-7)
            header_bg_code = "#DD6711"
            background_bg_code = "#313131"
            b_c_d = "b"

        from_1 = PhotoImage(file=resource_path(f"Images\\1{b_c_d}.png"))
        from_1_label = Label(image=from_1, borderwidth=0)
        from_1_label.place(x=0, y=110 + 70)
        real_from_1 = Button(root, image=from_1, borderwidth=0, background=background_bg_code,
                             activebackground=background_bg_code)
        real_from_1.place(x=0, y=110 + 70)

        from_2 = PhotoImage(file=resource_path(f"Images\\2{b_c_d}.png"))
        from_2_label = Label(image=from_2, borderwidth=0)
        from_2_label.place(x=0, y=170 + 70)
        real_from_2 = Button(root, image=from_2, borderwidth=0, background=background_bg_code,
                             activebackground=background_bg_code, command=lambda: from_base_data_getter(2))
        real_from_2.place(x=0, y=170 + 70)

        from_3 = PhotoImage(file=resource_path(f"Images\\3{b_c_d}.png"))
        from_3_label = Label(image=from_3, borderwidth=0)
        from_3_label.place(x=0, y=230 + 70)
        real_from_3 = Button(root, image=from_3, borderwidth=0, background=background_bg_code,
                             activebackground=background_bg_code, command=lambda: from_base_data_getter(3))
        real_from_3.place(x=0, y=230 + 70)

        from_4 = PhotoImage(file=resource_path(f"Images\\4{b_c_d}.png"))
        from_4_label = Label(image=from_4, borderwidth=0)
        from_4_label.place(x=0, y=290 + 70)
        real_from_4 = Button(root, image=from_4, borderwidth=0, background=background_bg_code,
                             activebackground=background_bg_code, command=lambda: from_base_data_getter(4))
        real_from_4.place(x=0, y=290 + 70)

        from_5 = PhotoImage(file=resource_path(f"Images\\5{b_c_d}.png"))
        from_5_label = Label(image=from_5, borderwidth=0)
        from_5_label.place(x=0, y=350 + 70)
        real_from_5 = Button(root, image=from_5, borderwidth=0, background=background_bg_code,
                             activebackground=background_bg_code, command=lambda: from_base_data_getter(5))
        real_from_5.place(x=0, y=350 + 70)

        from_6 = PhotoImage(file=resource_path(f"Images\\6{b_c_d}.png"))
        from_6_label = Label(image=from_6, borderwidth=0)
        from_6_label.place(x=0, y=410 + 70)
        real_from_6 = Button(root, image=from_6, borderwidth=0, background=background_bg_code,
                             activebackground=background_bg_code, command=lambda: from_base_data_getter(6))
        real_from_6.place(x=0, y=410 + 70)

        from_7 = PhotoImage(file=resource_path(f"Images\\7{b_c_d}.png"))
        from_7_label = Label(image=from_7, borderwidth=0)
        from_7_label.place(x=80, y=110 + 70)
        real_from_7 = Button(root, image=from_7, borderwidth=0, background=background_bg_code,
                             activebackground=background_bg_code, command=lambda: from_base_data_getter(7))
        real_from_7.place(x=80, y=110 + 70)

        from_8 = PhotoImage(file=resource_path(f"Images\\8{b_c_d}.png"))
        from_8_label = Label(image=from_8, borderwidth=0)
        from_8_label.place(x=80, y=170 + 70)
        real_from_8 = Button(root, image=from_8, borderwidth=0, background=background_bg_code,
                             activebackground=background_bg_code, command=lambda: from_base_data_getter(8))
        real_from_8.place(x=80, y=170 + 70)

        from_9 = PhotoImage(file=resource_path(f"Images\\9{b_c_d}.png"))
        from_9_label = Label(image=from_9, borderwidth=0)
        from_9_label.place(x=80, y=230 + 70)
        real_from_9 = Button(root, image=from_9, borderwidth=0, background=background_bg_code,
                             activebackground=background_bg_code, command=lambda: from_base_data_getter(9))
        real_from_9.place(x=80, y=230 + 70)

        from_10 = PhotoImage(file=resource_path(f"Images\\10{b_c_d}.png"))
        from_10_label = Label(image=from_10, borderwidth=0)
        from_10_label.place(x=80, y=290 + 70)
        real_from_10 = Button(root, image=from_10, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(10))
        real_from_10.place(x=80, y=290 + 70)

        from_11 = PhotoImage(file=resource_path(f"Images\\11{b_c_d}.png"))
        from_11_label = Label(image=from_11, borderwidth=0)
        from_11_label.place(x=80, y=350 + 70)
        real_from_11 = Button(root, image=from_11, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(11))
        real_from_11.place(x=80, y=350 + 70)

        from_12 = PhotoImage(file=resource_path(f"Images\\12{b_c_d}.png"))
        from_12_label = Label(image=from_12, borderwidth=0)
        from_12_label.place(x=80, y=410 + 70)
        real_from_12 = Button(root, image=from_12, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(12))
        real_from_12.place(x=80, y=410 + 70)

        from_13 = PhotoImage(file=resource_path(f"Images\\13{b_c_d}.png"))
        from_13_label = Label(image=from_13, borderwidth=0)
        from_13_label.place(x=160, y=110 + 70)
        real_from_13 = Button(root, image=from_13, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(13))
        real_from_13.place(x=160, y=110 + 70)

        from_14 = PhotoImage(file=resource_path(f"Images\\14{b_c_d}.png"))
        from_14_label = Label(image=from_14, borderwidth=0)
        from_14_label.place(x=160, y=170 + 70)
        real_from_14 = Button(root, image=from_14, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(14))
        real_from_14.place(x=160, y=170 + 70)

        from_15 = PhotoImage(file=resource_path(f"Images\\15{b_c_d}.png"))
        from_15_label = Label(image=from_15, borderwidth=0)
        from_15_label.place(x=160, y=230 + 70)
        real_from_15 = Button(root, image=from_15, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(15))
        real_from_15.place(x=160, y=230 + 70)

        from_16 = PhotoImage(file=resource_path(f"Images\\16{b_c_d}.png"))
        from_16_label = Label(image=from_16, borderwidth=0)
        from_16_label.place(x=160, y=290 + 70)
        real_from_16 = Button(root, image=from_16, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(16))
        real_from_16.place(x=160, y=290 + 70)

        from_17 = PhotoImage(file=resource_path(f"Images\\17{b_c_d}.png"))
        from_17_label = Label(image=from_17, borderwidth=0)
        from_17_label.place(x=160, y=350 + 70)
        real_from_17 = Button(root, image=from_17, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(17))
        real_from_17.place(x=160, y=350 + 70)

        from_18 = PhotoImage(file=resource_path(f"Images\\18{b_c_d}.png"))
        from_18_label = Label(image=from_18, borderwidth=0)
        from_18_label.place(x=160, y=410 + 70)
        real_from_18 = Button(root, image=from_18, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(18))
        real_from_18.place(x=160, y=410 + 70)

        from_19 = PhotoImage(file=resource_path(f"Images\\19{b_c_d}.png"))
        from_19_label = Label(image=from_19, borderwidth=0)
        from_19_label.place(x=240, y=110 + 70)
        real_from_19 = Button(root, image=from_19, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(19))
        real_from_19.place(x=240, y=110 + 70)

        from_20 = PhotoImage(file=resource_path(f"Images\\20{b_c_d}.png"))
        from_20_label = Label(image=from_20, borderwidth=0)
        from_20_label.place(x=240, y=170 + 70)
        real_from_20 = Button(root, image=from_20, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(20))
        real_from_20.place(x=240, y=170 + 70)

        from_21 = PhotoImage(file=resource_path(f"Images\\21{b_c_d}.png"))
        from_21_label = Label(image=from_21, borderwidth=0)
        from_21_label.place(x=240, y=230 + 70)
        real_from_21 = Button(root, image=from_21, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(21))
        real_from_21.place(x=240, y=230 + 70)

        from_22 = PhotoImage(file=resource_path(f"Images\\22{b_c_d}.png"))
        from_22_label = Label(image=from_22, borderwidth=0)
        from_22_label.place(x=240, y=290 + 70)
        real_from_22 = Button(root, image=from_22, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(22))
        real_from_22.place(x=240, y=290 + 70)

        from_23 = PhotoImage(file=resource_path(f"Images\\23{b_c_d}.png"))
        from_23_label = Label(image=from_23, borderwidth=0)
        from_23_label.place(x=240, y=350 + 70)
        real_from_23 = Button(root, image=from_23, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(23))
        real_from_23.place(x=240, y=350 + 70)

        from_24 = PhotoImage(file=resource_path(f"Images\\24{b_c_d}.png"))
        from_24_label = Label(image=from_24, borderwidth=0)
        from_24_label.place(x=240, y=410 + 70)
        real_from_24 = Button(root, image=from_24, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(24))
        real_from_24.place(x=240, y=410 + 70)

        from_25 = PhotoImage(file=resource_path(f"Images\\25{b_c_d}.png"))
        from_25_label = Label(image=from_25, borderwidth=0)
        from_25_label.place(x=320, y=110 + 70)
        real_from_25 = Button(root, image=from_25, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(25))
        real_from_25.place(x=320, y=110 + 70)

        from_26 = PhotoImage(file=resource_path(f"Images\\26{b_c_d}.png"))
        from_26_label = Label(image=from_26, borderwidth=0)
        from_26_label.place(x=320, y=170 + 70)
        real_from_26 = Button(root, image=from_26, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(26))
        real_from_26.place(x=320, y=170 + 70)

        from_27 = PhotoImage(file=resource_path(f"Images\\27{b_c_d}.png"))
        from_27_label = Label(image=from_27, borderwidth=0)
        from_27_label.place(x=320, y=230 + 70)
        real_from_27 = Button(root, image=from_27, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(27))
        real_from_27.place(x=320, y=230 + 70)

        from_28 = PhotoImage(file=resource_path(f"Images\\28{b_c_d}.png"))
        from_28_label = Label(image=from_28, borderwidth=0)
        from_28_label.place(x=320, y=290 + 70)
        real_from_28 = Button(root, image=from_28, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(28))
        real_from_28.place(x=320, y=290 + 70)

        from_29 = PhotoImage(file=resource_path(f"Images\\29{b_c_d}.png"))
        from_29_label = Label(image=from_29, borderwidth=0)
        from_29_label.place(x=320, y=350 + 70)
        real_from_29 = Button(root, image=from_29, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(29))
        real_from_29.place(x=320, y=350 + 70)

        from_30 = PhotoImage(file=resource_path(f"Images\\30{b_c_d}.png"))
        from_30_label = Label(image=from_30, borderwidth=0)
        from_30_label.place(x=320, y=410 + 70)
        real_from_30 = Button(root, image=from_30, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(30))
        real_from_30.place(x=320, y=410 + 70)

        from_31 = PhotoImage(file=resource_path(f"Images\\31{b_c_d}.png"))
        from_31_label = Label(image=from_31, borderwidth=0)
        from_31_label.place(x=400, y=110 + 70)
        real_from_31 = Button(root, image=from_31, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(31))
        real_from_31.place(x=400, y=110 + 70)

        from_32 = PhotoImage(file=resource_path(f"Images\\32{b_c_d}.png"))
        from_32_label = Label(image=from_32, borderwidth=0)
        from_32_label.place(x=400, y=170 + 70)
        real_from_32 = Button(root, image=from_32, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(32))
        real_from_32.place(x=400, y=170 + 70)

        from_33 = PhotoImage(file=resource_path(f"Images\\33{b_c_d}.png"))
        from_33_label = Label(image=from_33, borderwidth=0)
        from_33_label.place(x=400, y=230 + 70)
        real_from_33 = Button(root, image=from_33, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(33))
        real_from_33.place(x=400, y=230 + 70)

        from_34 = PhotoImage(file=resource_path(f"Images\\34{b_c_d}.png"))
        from_34_label = Label(image=from_34, borderwidth=0)
        from_34_label.place(x=400, y=290 + 70)
        real_from_34 = Button(root, image=from_34, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(34))
        real_from_34.place(x=400, y=290 + 70)

        from_35 = PhotoImage(file=resource_path(f"Images\\35{b_c_d}.png"))
        from_35_label = Label(image=from_35, borderwidth=0)
        from_35_label.place(x=400, y=350 + 70)
        real_from_35 = Button(root, image=from_35, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(35))
        real_from_35.place(x=400, y=350 + 70)

        from_36 = PhotoImage(file=resource_path(f"Images\\36{b_c_d}.png"))
        from_36_label = Label(image=from_36, borderwidth=0)
        from_36_label.place(x=400, y=410 + 70)
        real_from_36 = Button(root, image=from_36, borderwidth=0, background=background_bg_code,
                              activebackground=background_bg_code, command=lambda: from_base_data_getter(36))
        real_from_36.place(x=400, y=410 + 70)

        button_calculator_icon = PhotoImage(file=resource_path(f"Images\\{button_calculator_icon}.png"))
        button_calculator_icon_label = Label(image=button_calculator_icon, bg=f"{header_bg_code}")
        button_calculator_icon_label.place(x=10, y=0)
        real_button_calculator_icon = Button(root, image=button_calculator_icon, borderwidth=0, bg=f"{header_bg_code}",
                                             activebackground=f"{header_bg_code}", command=cal_screen)
        real_button_calculator_icon.place(x=10, y=0)

        button_equation_icon = PhotoImage(file=resource_path(f"Images\\{button_equation_icon}.png"))
        button_equation_icon_label = Label(image=button_equation_icon, bg=f"{header_bg_code}")
        button_equation_icon_label.place(x=190, y=3)
        real_button_equation_icon = Button(root, image=button_equation_icon, borderwidth=0, bg=f"{header_bg_code}",
                                           activebackground=f"{header_bg_code}", command=equation)
        real_button_equation_icon.place(x=190, y=3)

        button_integral_icon = PhotoImage(file=resource_path(f"Images\\{button_integral_icon}.png"))
        button_integral_icon_label = Label(image=button_integral_icon, bg=f"{header_bg_code}")
        button_integral_icon_label.place(x=385, y=2)
        real_button_integral_icon = Button(root, image=button_integral_icon, borderwidth=0, bg=f"{header_bg_code}",
                                           activebackground=f"{header_bg_code}")
        real_button_integral_icon.place(x=385, y=2)

    all_errors = (
        "Give me more than zero!", "Over Flow!", "Invalid input!", "Under construction!", "Can't devide to zero!")

    body_theme_selector = [1, 2, 3, 4]
    body_theme_selected = random.choice(body_theme_selector)

    if body_theme_selected == 1:
        bg = PhotoImage(file=resource_path("Images\\body.png"))
        bg_label = Label(root, image=bg)
        bg_label.place(x=-12, y=-24)
        header_bg_code = "#8E1111"
        background_bg_code = "#232323"

    if body_theme_selected == 2:
        bg = PhotoImage(file=resource_path("Images\\bodybody.png"))
        bg_label = Label(root, image=bg)
        bg_label.place(x=-12, y=-24)
        header_bg_code = "#65872D"
        background_bg_code = "#341030"

    if body_theme_selected == 3:
        bg = PhotoImage(file=resource_path("Images\\bodybodybody.png"))
        bg_label = Label(root, image=bg)
        bg_label.place(x=-12, y=-24)
        header_bg_code = "#A71F58"
        background_bg_code = "#0D093A"

    if body_theme_selected == 4:
        bg = PhotoImage(file=resource_path("Images\\bodybodybodybody.png"))
        bg_label = Label(root, image=bg)
        bg_label.place(x=-10, y=-24)
        header_bg_code = "#2D5187"
        background_bg_code = "#320E0E"

    button_equation_icon = PhotoImage(file=resource_path("Images\\equation_icon.png"))
    button_equation_icon_label = Label(image=button_equation_icon, background=header_bg_code)
    button_equation_icon_label.place(x=10, y=3)
    real_button_equation_icon = Button(root, image=button_equation_icon, background=header_bg_code,
                                       activebackground=header_bg_code, borderwidth=0, command=equation)
    real_button_equation_icon.place(x=10, y=3)

    button_base_converter_icon = PhotoImage(file=resource_path("Images\\base_converter_icon.png"))
    button_base_converter_icon_label = Label(image=button_base_converter_icon, background=header_bg_code)
    button_base_converter_icon_label.place(x=170, y=2)
    real_button_base_converter_icon = Button(root, image=button_base_converter_icon, background=header_bg_code,
                                             activebackground=header_bg_code, borderwidth=0, command=base_converter)
    real_button_base_converter_icon.place(x=170, y=2)

    button_integral_icon = PhotoImage(file=resource_path("Images\\integral_icon.png"))
    button_integral_icon_label = Label(image=button_integral_icon, background=header_bg_code)
    button_integral_icon_label.place(x=370, y=2)
    real_button_integral_icon = Button(root, image=button_integral_icon, background=header_bg_code,
                                       activebackground=header_bg_code, borderwidth=0, command=integral)
    real_button_integral_icon.place(x=370, y=2)

    theme_selector = [1, 2, 3, 4]
    selected_theme = random.choice(theme_selector)

    if selected_theme == 1:
        button_num_1 = 1
        button_num_2 = 2
        button_num_3 = 3
        button_num_4 = 4
        button_num_5 = 5
        button_num_6 = 6
        button_num_7 = 7
        button_num_8 = 8
        button_num_9 = 9
        button_num_0 = 11110
        dot_button = "dot"
        button_times = "times"
        button_fact = "fact"
        button_clear = "clear"
        button_backward = "backward"
        button_onfractionx = "onfractionx"
        button_negorposmaker = "negorposmaker"
        button_plus = "plus"
        button_mines = "mines"
        button_equal = "equal"
        button_fraction = "fraction"
        button_sqrt2 = "sqrt2"
        button_power2 = "power2"
        button_cal = "cal"
        button_fib = "fib"
        button_openingparenthesis = "openingparenthesis"
        button_closingparenthesis = "closingparenthesis"
        button_percent = "percent"
        button_pi = "pi"
        button_sin = "sin"
        button_cos = "cos"
        button_tan = "tan"
        button_cot = "cot"
        button_log = "log"
        button_e = "e"
        button_exp = "exp"

    if selected_theme == 2:
        button_num_1 = 11
        button_num_2 = 22
        button_num_3 = 33
        button_num_4 = 44
        button_num_5 = 55
        button_num_6 = 66
        button_num_7 = 77
        button_num_8 = 88
        button_num_9 = 99
        button_num_0 = 111100
        dot_button = "dotdot"
        button_times = "timestimes"
        button_fact = "factfact"
        button_clear = "clearclear"
        button_backward = "backwardbackward"
        button_onfractionx = "onfractionxonfractionx"
        button_negorposmaker = "negorposmakernegorposmaker"
        button_plus = "plusplus"
        button_mines = "minesmines"
        button_equal = "equalequal"
        button_fraction = "fractionfraction"
        button_sqrt2 = "sqrt2sqrt2"
        button_power2 = "power2power2"
        button_cal = "cal"
        button_fib = "fibfib"
        button_openingparenthesis = "openingparenthesisopeningparenthesis"
        button_closingparenthesis = "closingparenthesisclosingparenthesis"
        button_percent = "percentpercent"
        button_pi = "pipi"
        button_sin = "sinsin"
        button_cos = "coscos"
        button_tan = "tantan"
        button_cot = "cotcot"
        button_log = "loglog"
        button_e = "ee"
        button_exp = "expexp"

    if selected_theme == 3:
        button_num_1 = 111
        button_num_2 = 222
        button_num_3 = 333
        button_num_4 = 444
        button_num_5 = 555
        button_num_6 = 666
        button_num_7 = 777
        button_num_8 = 888
        button_num_9 = 999
        button_num_0 = 1111000
        dot_button = "dotdotdot"
        button_times = "timestimestimes"
        button_fact = "factfactfact"
        button_clear = "clearclearclear"
        button_backward = "backwardbackwardbackward"
        button_onfractionx = "onfractionxonfractionxonfractionx"
        button_negorposmaker = "negorposmakernegorposmakernegorposmaker"
        button_plus = "plusplusplus"
        button_mines = "minesminesmines"
        button_equal = "equalequalequal"
        button_fraction = "fractionfractionfraction"
        button_sqrt2 = "sqrt2sqrt2sqrt2"
        button_power2 = "power2power2power2"
        button_cal = "cal"
        button_fib = "fibfibfib"
        button_openingparenthesis = "openingparenthesisopeningparenthesisopeningparenthesis"
        button_closingparenthesis = "closingparenthesisclosingparenthesisclosingparenthesis"
        button_percent = "percentpercentpercent"
        button_pi = "pipipi"
        button_sin = "sinsinsin"
        button_cos = "coscoscos"
        button_tan = "tantantan"
        button_cot = "cotcotcot"
        button_log = "logloglog"
        button_e = "eee"
        button_exp = "expexpexp"

    if selected_theme == 4:
        button_num_1 = 1111
        button_num_2 = 2222
        button_num_3 = 3333
        button_num_4 = 4444
        button_num_5 = 5555
        button_num_6 = 6666
        button_num_7 = 7777
        button_num_8 = 8888
        button_num_9 = 9999
        button_num_0 = 11110000
        dot_button = "dotdotdotdot"
        button_times = "timestimestimestimes"
        button_fact = "factfactfactfact"
        button_clear = "clearclearclearclear"
        button_backward = "backwardbackwardbackwardbackward"
        button_onfractionx = "onfractionxonfractionxonfractionxonfractionx"
        button_negorposmaker = "negorposmakernegorposmakernegorposmakernegorposmaker"
        button_plus = "plusplusplusplus"
        button_mines = "minesminesminesmines"
        button_equal = "equalequalequalequal"
        button_fraction = "fractionfractionfractionfraction"
        button_sqrt2 = "sqrt2sqrt2sqrt2sqrt2"
        button_power2 = "power2power2power2power2"
        button_cal = "cal"
        button_fib = "fibfibfibfib"
        button_openingparenthesis = "openingparenthesisopeningparenthesisopeningparenthesisopeningparenthesis"
        button_closingparenthesis = "closingparenthesisclosingparenthesisclosingparenthesisclosingparenthesis"
        button_percent = "percentpercentpercentpercent"
        button_pi = "pipipipi"
        button_sin = "sinsinsinsin"
        button_cos = "coscoscoscos"
        button_tan = "tantantantan"
        button_cot = "cotcotcotcot"
        button_log = "loglogloglog"
        button_e = "eeee"
        button_exp = "expexpexpexp"

    def button_click(number):
        global data
        data = ""

        if e.get() in all_errors or " " in e.get():
            e.delete(0, END)
            current = e.get()
            e.insert(0, current + str(number))
        else:
            current = e.get()
            e.delete(0, END)
            e.insert(0, current + str(number))
            data += e.get()

    def button_dot_screen(symbol):
        data = e.get()
        if data in all_errors or " " in e.get():
            current = e.get()

        else:
            current = e.get()
            e.delete(0, END)
            e.insert(0, current + str(symbol))
            data += e.get()

    def button_clear_screen():
        e.delete(0, END)

    def button_plus_screen(symbol):
        data = e.get()

        if data in all_errors or " " in e.get():
            current = e.get()

        else:
            current = e.get()
            e.delete(0, END)
            e.insert(0, current + str(symbol))
            data += e.get()

    def button_mines_screen(symbol):
        data = e.get()
        if data in all_errors or " " in e.get():
            e.delete(0, END)
            current = e.get()
            e.insert(0, current + str(symbol))


        else:
            current = e.get()
            e.delete(0, END)
            e.insert(0, current + str(symbol))
            data += e.get()

    def button_times_screen(symbol):
        data = e.get()
        if data in all_errors or " " in e.get():
            current = e.get()

        else:
            current = e.get()
            e.delete(0, END)
            e.insert(0, current + str(symbol))

    def button_fraction_screen(symbol):
        data = e.get()
        if data in all_errors or " " in e.get():
            current = e.get()

        else:
            current = e.get()
            e.delete(0, END)
            e.insert(0, current + str(symbol))

    def button_power_screen(symbol):
        data = e.get()
        if data in all_errors or " " in e.get():
            current = e.get()

        else:
            current = e.get()
            e.delete(0, END)
            e.insert(0, current + str(symbol))

    def button_fib_screen(symbol):
        data = e.get()

        try:
            e.delete(0, END)
            data = int(data)
            n1 = 0
            n2 = 1
            if data < 0:
                e.delete(0, END)
                e.insert(0, "Give me more than zero!")

            if data == 1:
                e.delete(0, END)
                e.insert(0, "0")

            if data == 2:
                e.delete(0, END)

            for _ in range(2, int(data) + 1):
                sum = n1 + n2
                n1 = n2
                n2 = sum
                e.insert(END, f"{n2} ")

        except:
            e.delete(0, END)
            e.insert(0, "Invalid input!")

    def fact():

        try:
            data = e.get()
            e.delete(0, END)
            e.insert(0, factorial(int(data)))


        except ValueError:
            e.delete(0, END)
            e.insert(0, "Invalid input!")

        except decimal.Overflow:
            e.delete(0, END)
            e.insert(0, "Over Flow!")

    def negorposmaker(symbol):
        data = e.get()

        if data[0].isdigit():
            data = "-" + data
            e.delete(0, END)
            e.insert(0, data)

        elif data[0] == "l" or data[0] == "s" or data[0] == "c" or data[0] == "t":
            data = "-" + data
            e.delete(0, END)
            e.insert(0, data)

        else:
            data = data[1:]
            e.delete(0, END)
            e.insert(0, data)

    def backward():
        if e.get():
            data = e.get()[:-1]
            e.delete(0, END)
            e.insert(0, data)

    def exp():
        data = e.get()
        print(data)

        if "E" in data:
            data = data.replace("E", "*10")
            e.delete(0, END)
            if ".." in data:
                data.replace("..", ".")
            e.insert(0, data)

        else:
            temp_list = []
            for _ in data:
                temp_list.append(_)

            if data[0].isdigit() and data[0] != "0":

                temp_list.insert(1, ".")

                what_to_show = "".join(map(str, temp_list[: 20]))
                what_to_show = what_to_show + "*10^" + str(len(temp_list[2:]))
                e.delete(0, END)
                if ".." in what_to_show:
                    what_to_show.replace("..", ".")
                e.insert(0, what_to_show)

            temp_index = -1
            if data[0] == "0":
                for ______ in temp_list:
                    temp_index += 1

                    if ______ == "0" or ______ == ".":
                        pass

                    else:
                        break

                power = str(-(temp_index - 1))

                if len(temp_list[temp_index:]) == 1:
                    what_to_show = temp_list[-1] + "*10^" + power

                    e.delete(0, END)
                    if ".." in what_to_show:
                        what_to_show.replace("..", ".")
                    e.insert(END, what_to_show)

                else:
                    temp_list = temp_list[temp_index:]
                    temp_list.insert(1, ".")

                    what_to_show_decimal_part = "".join(map(str, temp_list))
                    what_to_show = what_to_show_decimal_part + "*10^" + power

                    e.delete(0, END)
                    if ".." in what_to_show:
                        what_to_show.replace("..", ".")
                    e.insert(END, what_to_show)

    def onfractionx():
        try:
            data = e.get()
            e.delete(0, END)
            e.insert(0, 1 / float(data))

        except:
            e.delete(0, END)
            e.insert(0, "Invalid input!")

    def percent():
        data = e.get()

        try:
            e.delete(0, END)
            e.insert(0, float(data) / 100)

        except ValueError:
            e.delete(0, END)
            e.insert(0, "Invalid input!")

    def pi():
        data = e.get()
        data = str(math.pi)
        e.insert(END, data)

    def e_neper():
        data = e.get()
        data = str(math.e)
        e.insert(END, data)

    def button_pranthesis(symbol):
        current = e.get()

        if current in all_errors or " " in e.get():
            e.delete(0, END)
            e.insert(END, str(symbol))
            current += e.get()
        else:
            e.insert(END, str(symbol))
            current += e.get()

    def cal():
        data = e.get()
        if len(data) != 0:
            e.delete(0, END)
            e.insert(0, "        Calculate mode!")

        else:
            e.insert(0, "        Calculate mode!")

    def button_equal_screen():
        data = e.get()
        e.delete(0, END)

        all_operators = ("^", "*", "/", "+", "-")
        all_parenthesis = ("(", ")")
        all_trigonometry_and_log = ("sin", "cos", "tan", "cot", "log", "-sin", "-cos", "-tan", "-cot", "-log")
        all_first_alphabet_of_sin_cos_tan_cot_log = ("s", "c", "t", "l")

        temp = []
        for o in data:
            temp.append(o)

        if temp[-1] == "n" or temp[-1] == "s" or temp[-1] == "s" or temp[-1] == "g":
            temp.append("(")
            temp.append("0")

        temp.append("+")
        temp.append("0")

        temp_index_0 = -1
        for remaker_0 in temp:
            temp_index_0 += 1

            if remaker_0 == "n" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

        temp.append("+")
        temp_index_1 = -1
        for remaker_1 in temp:
            temp_index_1 += 1

            if remaker_1.isdigit():

                if temp[temp_index_1 + 1] in all_first_alphabet_of_sin_cos_tan_cot_log:
                    temp.insert(temp_index_1 + 1, "(")

        temp.pop(-1)

        temp_index_2 = -1
        for remaker_2 in temp:
            temp_index_2 += 1

            if remaker_2 == "n" or remaker_2 == "s" or remaker_2 == "t" or remaker_2 == "g":

                if temp[temp_index_2 + 1] == "-" or temp[temp_index_2 + 1].isdigit():
                    temp.insert(temp_index_2 + 1, "(")

        temp_index_4 = -1
        for remaker_4 in temp:
            temp_index_4 += 1

            if remaker_4 == "(":
                if temp[temp_index_4 - 1] in all_parenthesis:
                    temp.insert(temp_index_4, "*")

        temp_index_5 = -1
        for remaker_5 in temp:
            temp_index_5 += 1

            if remaker_5 == "(":
                if temp[temp_index_5 - 1].isdigit():
                    temp.insert(temp_index_5, "*")

        temp_index_6 = -1
        for remaker_6 in temp:
            temp_index_6 += 1

            if remaker_6 == "(":
                if temp[temp_index_6 - 1] == "*" and temp[temp_index_6 - 2] == "(":
                    temp.insert(temp_index_6 - 1, "1")

        temp_index_7 = -1
        for remaker_7 in temp:
            temp_index_7 += 1

            if remaker_7 == ")":
                if temp[temp_index_7 + 1] in all_first_alphabet_of_sin_cos_tan_cot_log:
                    temp.insert(temp_index_7 + 1, "*")

        temp_index_8 = -1
        for remaker_8 in temp:
            temp_index_8 += 1

            if remaker_8 == "√":
                if temp[temp_index_8 - 1].isdigit():
                    temp.insert(temp_index_8, "*")

        temp_index_10 = -1
        for remaker_10 in temp:
            temp_index_10 += 1

            if remaker_10 == "!":
                if temp[temp_index_10 + 1] not in all_operators:
                    temp.insert(temp_index_10 + 1, "*")

        temp_index_11 = -1
        for remaker_11 in temp:
            temp_index_11 += 1

            if remaker_11 == "!":
                if temp[temp_index_11 + 1] == "*" and temp[temp_index_11 + 2] == ")":
                    temp.pop(temp_index_11 + 1)

        if temp[0] == "*":
            temp.insert(0, "1")

        data = "".join(map(str, temp))
        del temp

        if data[0] == "-":
            negative_to_be_added_later = "-"
            data = data[1:]

        else:
            negative_to_be_added_later = ""

        if data[0] == "+":
            posetive_to_be_added_later = "-+"
            data = data[1:]

        else:
            posetive_to_be_added_later = ""

        data = data + "+"
        data_list = []
        all_operators = ("^", "*", "/", "+", "-")

        temp_num_holder = ""
        temp_counter = -1

        for data_list_adder in data:
            temp_counter += 1

            if data_list_adder.isdigit() or data_list_adder == ".":
                temp_num_holder = temp_num_holder + data_list_adder

            elif data_list_adder == "s":
                if data[temp_counter - 1] != "o":
                    data_list.append("sin")

            elif data_list_adder == "c":
                if data[temp_counter + 2] == "s":
                    data_list.append("cos")

                if data[temp_counter + 2] == "t":
                    data_list.append("cot")

            elif data_list_adder == "t":
                if data[temp_counter - 1] != "o":
                    data_list.append("tan")

            elif data_list_adder == "l":
                data_list.append("log")

            elif data_list_adder == "-":
                if data[temp_counter - 1] in all_operators:
                    temp_num_holder = data_list_adder + temp_num_holder
                else:
                    data_list.append(temp_num_holder)
                    data_list.append(data_list_adder)
                    temp_num_holder = ""

            elif data_list_adder == "+":
                if data[temp_counter - 1] in all_operators:
                    temp_num_holder = data_list_adder + temp_num_holder
                else:
                    data_list.append(temp_num_holder)
                    data_list.append(data_list_adder)
                    temp_num_holder = ""


            elif data_list_adder in all_operators:
                data_list.append(temp_num_holder)
                data_list.append(data_list_adder)
                temp_num_holder = ""


            elif data_list_adder == "(":
                if temp_counter == 0:
                    data_list.append("(")

                elif data[temp_counter - 1] == "-" and data[temp_counter - 2] in all_operators:
                    data_list.append("-")
                    data_list.append("(")
                    temp_num_holder = ""

                else:
                    data_list.append("(")


            elif data_list_adder == ")":
                if data[temp_counter - 1].isdigit():
                    if len(temp_num_holder) != 0:
                        data_list.append(temp_num_holder)
                        data_list.append(")")
                        temp_num_holder = ""

                    else:
                        data_list.append(")")

                elif data[temp_counter - 1] == ")":
                    data_list.append(")")

                elif data[temp_counter - 1] == "!":
                    data_list.append(")")


            elif data_list_adder == "√":
                data_list.append("√")


            elif data_list_adder == "!":
                if len(temp_num_holder) != 0:
                    data_list.append(temp_num_holder)
                    data_list.append("!")
                    temp_num_holder = ""

                else:
                    data_list.append("!")

        if len(negative_to_be_added_later) == 1:
            if "(" in data_list[0]:
                data_list.pop(0)
                data_list.insert(0, "-")
                data_list.insert(1, "(")

            else:

                data_list[0] = "-" + data_list[0]
                data_list = data_list[0: -1]

        else:
            data_list = data_list[0: -1]

        if data_list[-1] == "+":
            data_list.pop(-1)

        temp_data_list = []
        for _ in data_list:
            if _ == '':
                pass

            else:
                temp_data_list.append(_)

        data_list = temp_data_list.copy()
        del temp_data_list

        all_parenthesis = ("(", ")")
        temp_counter = -1
        for data_list_remaker in data_list:
            temp_counter += 1

            if data_list_remaker == "(":
                if data_list[temp_counter + 1] == "-":
                    data_list[temp_counter + 1: temp_counter + 3] = [f"-{data_list[temp_counter + 2]}"]

        temp_index = -1
        for plus_zero_adder in data_list:
            temp_index += 1

            if plus_zero_adder == ")":
                if data_list[temp_index + 1] == ")":
                    data_list.insert(temp_index + 1, "+")
                    data_list.insert(temp_index + 2, "0")

        temp_index = -1
        for open_parenthesis_adder_to_begininig in data_list:
            temp_index += 1

            if open_parenthesis_adder_to_begininig == ")":
                if "(" not in data_list[temp_index:: -1]:
                    data_list.insert(0, "(")

        if data_list[0] == "-":
            if data_list[1] == "(":
                data_list.pop(0)
                data_list.insert(0, "-1")
                data_list.insert(1, "*")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-sin":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "sin")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-cos":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "cos")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-tan":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "tan")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-cot":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "cot")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-log":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "log")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        open_count = 0
        close_count = 0
        for _ in data_list:
            if _ == "(":
                open_count += 1

            if _ == ")":
                close_count += 1

        if open_count > close_count:
            for i in range(open_count - close_count):
                data_list.append(")")

        if close_count > open_count:
            for j in range(close_count - open_count):
                data_list.insert(0, "(")

        counter = 0
        for i in data_list:
            if i == "(":
                counter += 1

        for u in range(counter):
            temp_index = -1
            end_point = 0
            for _ in data_list:
                temp_index += 1

                if _ == ")":
                    end_point = temp_index
                    break

            temp_index = 0
            start_point = 0
            for __ in data_list[end_point:: -1]:
                temp_index += 1

                if __ == "(":
                    start_point = end_point - temp_index + 1
                    break

            calculate_zone = data_list[start_point + 1: end_point]

            power_count = 0
            times_count = 0
            fraction_count = 0
            plus_count = 0
            mines_count = 0
            parenthesis_count = 0
            sqrt_count = 0
            fact_count = 0

            for how_many_of_each_operators in calculate_zone:
                if how_many_of_each_operators == "^":
                    power_count += 1

                if how_many_of_each_operators == "*":
                    times_count += 1

                if how_many_of_each_operators == "/":
                    fraction_count += 1

                if how_many_of_each_operators == "+":
                    plus_count += 1

                if how_many_of_each_operators == "-":
                    mines_count += 1

                if how_many_of_each_operators == "(":
                    parenthesis_count += 1

                if how_many_of_each_operators == "√":
                    sqrt_count += 1

                if how_many_of_each_operators == "!":
                    fact_count += 1

            counter = 0
            for i in data_list:
                if i == "(":
                    counter += 1

            for fact_calculations in range(fact_count):

                fact_index = -1
                for fact_finder in calculate_zone:
                    fact_index += 1

                    if fact_finder.isdigit() or fact_finder == ".":
                        pass

                    if fact_finder == "!":
                        try:
                            temp_answer = int(calculate_zone[fact_index - 1])
                            temp_answer = factorial(temp_answer)

                        except:
                            e.delete(0, END)
                            e.insert(END, "Invalid input!")

                        calculate_zone[fact_index - 1: fact_index + 1] = [str(temp_answer)]

            for sqrt_calculations in range(sqrt_count):

                sqrt_index = -1
                for sqrt_finder in calculate_zone:
                    sqrt_index += 1

                    if sqrt_finder.isdigit() or sqrt_finder == ".":
                        pass

                    if sqrt_finder == "√":
                        temp_answer = float(calculate_zone[sqrt_index + 1])
                        temp_answer = sqrt(temp_answer)

                        calculate_zone[sqrt_index: sqrt_index + 2] = [str(temp_answer)]

            zero_plus = 0
            to_be_removed_from_the_begining_later_count = 0
            for power_calculations in range(power_count):

                power_index = -1
                for power_finder in calculate_zone:
                    power_index += 1

                    if power_finder.isdigit() or power_finder == ".":
                        pass

                    if power_finder == "^":
                        first_number = calculate_zone[power_index - 1]
                        second_number = calculate_zone[power_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        if "-" in str(first_number) and "." in str(second_number):
                            e.insert(END, "Invalid input!")
                            calculate_zone.clear()
                            break

                        try:
                            temp_answer = first_number ** second_number

                        except:
                            e.delete(0, END)
                            e.insert(0, "Over flow!")

                        if "^" in calculate_zone[power_index + 1:] or "*" in calculate_zone[power_index + 1:] \
                                or "/" in calculate_zone[power_index + 1:] or "+" in calculate_zone[power_index + 1:] \
                                or "-" in calculate_zone[power_index + 1:]:

                            starting_point = power_index - 1
                            ending_point = power_index + 2
                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2


                        else:
                            starting_point = power_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    calculate_zone.pop(0)

            to_be_removed_from_the_begining_later_count = 0
            for times_and_fraction_calculations in range(times_count + fraction_count):

                times_or_fraction_index = -1

                for times_or_fraction_finder in calculate_zone:

                    times_or_fraction_index += 1
                    if times_or_fraction_finder.isdigit() or times_or_fraction_finder == ".":
                        pass

                    if times_or_fraction_finder == "*":
                        first_number = calculate_zone[times_or_fraction_index - 1]
                        second_number = calculate_zone[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        temp_answer = first_number * second_number

                        if "^" in calculate_zone[times_or_fraction_index:] or "*" in calculate_zone[
                                                                                     times_or_fraction_index:] \
                                or "/" in calculate_zone[times_or_fraction_index:] or "+" in calculate_zone[
                                                                                             times_or_fraction_index:] \
                                or "-" in calculate_zone[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            calculate_zone[starting_point: ending_point + 1] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

                    if times_or_fraction_finder == "/":
                        first_number = calculate_zone[times_or_fraction_index - 1]
                        second_number = calculate_zone[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)
                        devision_zero_count = 0
                        try:
                            temp_answer = first_number / second_number
                        except ZeroDivisionError:
                            e.delete(0, END)
                            e.insert(END, "Can't devide to zero!")
                            devision_zero_count += 1

                        if "^" in calculate_zone[times_or_fraction_index:] or "*" in calculate_zone[
                                                                                     times_or_fraction_index:] \
                                or "/" in calculate_zone[times_or_fraction_index:] or "+" in calculate_zone[
                                                                                             times_or_fraction_index:] \
                                or "-" in calculate_zone[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            if devision_zero_count == 0:
                                try:
                                    calculate_zone[starting_point: ending_point + 1] = [str(temp_answer)]
                                except:
                                    e.delete(0, END)
                                    e.insert(END, "Can't devide to zero!")
                                    break

                            else:
                                calculate_zone = []

                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    calculate_zone.pop(0)

            x_count = 0
            for plus_and_mines_calculation in range(plus_count + mines_count):

                plus_or_mines_index = -1

                for plus_or_mines_finder in calculate_zone:
                    plus_or_mines_index += 1

                    if plus_or_mines_finder != "-" or plus_or_mines_finder != "+":
                        pass

                    if plus_or_mines_finder == "+":
                        first_number = calculate_zone[plus_or_mines_index - 1]
                        second_number = calculate_zone[plus_or_mines_index + 1]

                        if "^" in calculate_zone[plus_or_mines_index + 1:] or "*" in calculate_zone[
                                                                                     plus_or_mines_index + 1:] \
                                or "/" in calculate_zone[plus_or_mines_index + 1:] or "+" in calculate_zone[
                                                                                             plus_or_mines_index + 1:] \
                                or "-" in calculate_zone[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            calculate_zone[starting_point:] = [str(temp_answer)]

                    if plus_or_mines_finder == "-":
                        first_number = calculate_zone[plus_or_mines_index - 1]
                        second_number = calculate_zone[plus_or_mines_index + 1]

                        if "^" in calculate_zone[plus_or_mines_index + 1:] or "*" in calculate_zone[
                                                                                     plus_or_mines_index + 1:] \
                                or "/" in calculate_zone[plus_or_mines_index + 1:] or "+" in calculate_zone[
                                                                                             plus_or_mines_index + 1:] \
                                or "-" in calculate_zone[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            calculate_zone[starting_point:] = [str(temp_answer)]

            for remover in range(x_count):
                calculate_zone.pop(0)

            if data_list[start_point - 1] == "sin" or data_list[start_point - 1] == "-sin":
                try:
                    calculate_zone = sin(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    e.delete(0, END)
                    e.insert(END, "Invalid input!")


            elif data_list[start_point - 1] == "cos" or data_list[start_point - 1] == "-cos":
                try:
                    calculate_zone = cos(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    e.delete(0, END)
                    e.insert(END, "Invalid input!")


            elif data_list[start_point - 1] == "tan" or data_list[start_point - 1] == "-tan":
                try:
                    calculate_zone = tan(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    e.delete(0, END)
                    e.insert(END, "Invalid input!")


            elif data_list[start_point - 1] == "cot" or data_list[start_point - 1] == "-cot":
                try:
                    calculate_zone = 1 / tan(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    e.delete(0, END)
                    e.insert(END, "Invalid input!")


            elif data_list[start_point - 1] == "log" or data_list[start_point - 1] == "-log":
                try:
                    calculate_zone = log10(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:
                    e.delete(0, END)
                    e.insert(END, "Invalid input!")

            else:
                data_list[start_point: end_point + 1] = calculate_zone

        if "(" not in data_list:

            power_count = 0
            times_count = 0
            fraction_count = 0
            plus_count = 0
            mines_count = 0
            sqrt_count = 0
            fact_count = 0

            for how_many_of_each_operators in data_list:
                if how_many_of_each_operators == "^":
                    power_count += 1

                if how_many_of_each_operators == "*":
                    times_count += 1

                if how_many_of_each_operators == "/":
                    fraction_count += 1

                if how_many_of_each_operators == "+":
                    plus_count += 1

                if how_many_of_each_operators == "-":
                    mines_count += 1

                if how_many_of_each_operators == "√":
                    sqrt_count += 1

                if how_many_of_each_operators == "!":
                    fact_count += 1

            for fact_calculations in range(fact_count):

                fact_index = -1
                for fact_finder in data_list:
                    fact_index += 1

                    if fact_finder.isdigit() or fact_finder == ".":
                        pass

                    if fact_finder == "!":
                        try:
                            temp_answer = int(data_list[fact_index - 1])
                            temp_answer = factorial(temp_answer)

                        except:
                            e.delete(0, END)
                            e.insert(END, "Invalid input!")

                        data_list[fact_index - 1: fact_index + 1] = [str(temp_answer)]

            for sqrt_calculations in range(sqrt_count):

                sqrt_index = -1
                for sqrt_finder in data_list:
                    sqrt_index += 1

                    if sqrt_finder.isdigit() or sqrt_finder == ".":
                        pass

                    if sqrt_finder == "√":
                        try:
                            temp_answer = float(data_list[sqrt_index + 1])
                            temp_answer = sqrt(temp_answer)

                        except:
                            e.delete(0, END)
                            e.insert(END, "Invalid input!")

                        data_list[sqrt_index: sqrt_index + 2] = [str(temp_answer)]

            zero_plus = 0
            to_be_removed_from_the_begining_later_count = 0
            for power_calculations in range(power_count):

                power_index = -1
                for power_finder in data_list:
                    power_index += 1

                    if power_finder.isdigit() or power_finder == ".":
                        pass

                    if power_finder == "^":
                        first_number = data_list[power_index - 1]
                        second_number = data_list[power_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        if "-" in str(first_number) and "." in str(second_number):
                            e.delete(0, END)
                            e.insert(END, "Invalid input!")
                            data_list.clear()
                            break

                        try:
                            temp_answer = first_number ** second_number

                        except:
                            e.insert(END, "Over flow!")

                        if "^" in data_list[power_index + 1:] or "*" in data_list[power_index + 1:] \
                                or "/" in data_list[power_index + 1:] or "+" in data_list[power_index + 1:] \
                                or "-" in data_list[power_index + 1:]:

                            starting_point = power_index - 1
                            ending_point = power_index + 2
                            data_list[starting_point: ending_point] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2


                        else:
                            starting_point = power_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    data_list.pop(0)

            to_be_removed_from_the_begining_later_count = 0
            for times_and_fraction_calculations in range(times_count + fraction_count):

                times_or_fraction_index = -1

                for times_or_fraction_finder in data_list:

                    times_or_fraction_index += 1
                    if times_or_fraction_finder.isdigit() or times_or_fraction_finder == ".":
                        pass

                    if times_or_fraction_finder == "*":
                        first_number = data_list[times_or_fraction_index - 1]
                        second_number = data_list[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        temp_answer = first_number * second_number

                        if "^" in data_list[times_or_fraction_index:] or "*" in data_list[times_or_fraction_index:] \
                                or "/" in data_list[times_or_fraction_index:] or "+" in data_list[
                                                                                        times_or_fraction_index:] \
                                or "-" in data_list[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            data_list[starting_point: ending_point + 1] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

                    if times_or_fraction_finder == "/":
                        first_number = data_list[times_or_fraction_index - 1]
                        second_number = data_list[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)
                        devision_zero_count = 0
                        try:
                            temp_answer = first_number / second_number
                        except ZeroDivisionError:
                            e.insert(END, "Can't devide to zero!")
                            devision_zero_count += 1

                        if "^" in data_list[times_or_fraction_index:] or "*" in data_list[times_or_fraction_index:] \
                                or "/" in data_list[times_or_fraction_index:] or "+" in data_list[
                                                                                        times_or_fraction_index:] \
                                or "-" in data_list[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            if devision_zero_count == 0:
                                try:
                                    data_list[starting_point: ending_point + 1] = [str(temp_answer)]
                                except:
                                    e.delete(0, END)
                                    e.insert(END, "Can't devide to zero!")
                                    break

                            else:
                                data_list = []

                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    data_list.pop(0)

            x_count = 0
            for plus_and_mines_calculation in range(plus_count + mines_count):

                plus_or_mines_index = -1

                for plus_or_mines_finder in data_list:
                    plus_or_mines_index += 1

                    if plus_or_mines_finder != "-" or plus_or_mines_finder != "+":
                        pass

                    if plus_or_mines_finder == "+":
                        first_number = data_list[plus_or_mines_index - 1]
                        second_number = data_list[plus_or_mines_index + 1]

                        if "^" in data_list[plus_or_mines_index + 1:] or "*" in data_list[plus_or_mines_index + 1:] \
                                or "/" in data_list[plus_or_mines_index + 1:] or "+" in data_list[
                                                                                        plus_or_mines_index + 1:] \
                                or "-" in data_list[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            data_list[starting_point: ending_point] = [temp_answer]
                            data_list.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            data_list[starting_point:] = [temp_answer]

                    if plus_or_mines_finder == "-":
                        first_number = data_list[plus_or_mines_index - 1]
                        second_number = data_list[plus_or_mines_index + 1]

                        if "^" in data_list[plus_or_mines_index + 1:] or "*" in data_list[plus_or_mines_index + 1:] \
                                or "/" in data_list[plus_or_mines_index + 1:] or "+" in data_list[
                                                                                        plus_or_mines_index + 1:] \
                                or "-" in data_list[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            data_list[starting_point: ending_point] = [temp_answer]
                            data_list.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            data_list[starting_point:] = [temp_answer]

            for remover in range(x_count):
                data_list.pop(0)

            final_answer = ""
            if data_list:
                final_answer = data_list[0]

            if final_answer == "+":
                e.insert(END, "")

            else:
                if final_answer == "-0":
                    final_answer = "0"
                    e.delete(0, END)
                    e.insert(END, final_answer)

                else:
                    # final_answer = str(final_answer)
                    #
                    # temp_index = -1
                    #
                    # if "." in final_answer:
                    #
                    #     for _____ in final_answer:
                    #
                    #         temp_index += 1
                    #
                    #         if _____ == ".":
                    #             temp_index += 1
                    #
                    #             break
                    #
                    #     if all(elements == "0" for elements in final_answer[temp_index + 1:]):
                    #         final_answer = final_answer[0: temp_index - 1]
                    #
                    # e.delete(0, END)
                    # if "E" in final_answer:
                    #     final_answer = final_answer.replace("E" , "*10^")

                    e.insert(END, final_answer)

    button_sin = PhotoImage(file=resource_path(f"Images\\{button_sin}.png"))
    button_sin_label = Label(image=button_sin, bg=f"{background_bg_code}")
    button_sin_label.place(x=0, y=490)
    real_button_sin = Button(root, text="1", image=button_sin, borderwidth=0, bg=f"{background_bg_code}",
                             activebackground=f"{background_bg_code}", command=lambda: button_click("sin("))
    real_button_sin.place(x=0, y=490)

    button_cos = PhotoImage(file=resource_path(f"Images\\{button_cos}.png"))
    button_cos_label = Label(image=button_cos, bg=f"{background_bg_code}")
    button_cos_label.place(x=0, y=430)
    real_button_cos = Button(root, text="1", image=button_cos, borderwidth=0, bg=f"{background_bg_code}",
                             activebackground=f"{background_bg_code}", command=lambda: button_click("cos("))
    real_button_cos.place(x=0, y=430)

    button_tan = PhotoImage(file=resource_path(f"Images\\{button_tan}.png"))
    button_tan_label = Label(image=button_tan, bg=f"{background_bg_code}")
    button_tan_label.place(x=0, y=370)
    real_button_tan = Button(root, text="tan(", image=button_tan, borderwidth=0, bg=f"{background_bg_code}",
                             activebackground=f"{background_bg_code}", command=lambda: button_click("tan("))
    real_button_tan.place(x=0, y=370)

    button_cot = PhotoImage(file=resource_path(f"Images\\{button_cot}.png"))
    button_cot_label = Label(image=button_cot, bg=f"{background_bg_code}")
    button_cot_label.place(x=0, y=310)
    real_button_cot = Button(root, text="1", image=button_cot, borderwidth=0, bg=f"{background_bg_code}",
                             activebackground=f"{background_bg_code}", command=lambda: button_click("cot("))
    real_button_cot.place(x=0, y=310)

    button_log = PhotoImage(file=resource_path(f"Images\\{button_log}.png"))
    button_log_label = Label(image=button_cot, bg=f"{background_bg_code}")
    button_log_label.place(x=0, y=250)
    real_button_log = Button(root, text="1", image=button_log, borderwidth=0, bg=f"{background_bg_code}",
                             activebackground=f"{background_bg_code}", command=lambda: button_click("log("))
    real_button_log.place(x=0, y=250)

    button_pi = PhotoImage(file=resource_path(f"Images\\{button_pi}.png"))
    button_pi_label = Label(image=button_pi, bg=f"{background_bg_code}")
    button_pi_label.place(x=0, y=130)
    real_button_pi = Button(root, image=button_pi, borderwidth=0, bg=f"{background_bg_code}",
                            activebackground=f"{background_bg_code}", command=pi)
    real_button_pi.place(x=0, y=130)

    button_e = PhotoImage(file=resource_path(f"Images\\{button_e}.png"))
    button_e_label = Label(image=button_e, bg=f"{background_bg_code}")
    button_e_label.place(x=0, y=190)
    real_button_e = Button(root, image=button_e, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=e_neper)
    real_button_e.place(x=0, y=190)

    button_1 = PhotoImage(file=resource_path(f"Images\\{button_num_1}.png"))
    button_1_label = Label(image=button_1, bg=f"{background_bg_code}")
    button_1_label.place(x=95, y=430)
    real_button_1 = Button(root, text="1", image=button_1, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(1))
    real_button_1.place(x=95, y=430)

    button_2 = PhotoImage(file=resource_path(f"Images\\{button_num_2}.png"))
    button_2_label = Label(image=button_2, bg=f"{background_bg_code}")
    button_2_label.place(x=190, y=430)
    real_button_2 = Button(root, text="2", image=button_2, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(2))
    real_button_2.place(x=190, y=430)

    button_3 = PhotoImage(file=resource_path(f"Images\\{button_num_3}.png"))
    button_3_label = Label(image=button_3, bg=f"{background_bg_code}")
    button_3_label.place(x=285, y=430)
    real_button_3 = Button(root, text="3", image=button_3, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(3))
    real_button_3.place(x=285, y=430)

    button_4 = PhotoImage(file=resource_path(f"Images\\{button_num_4}.png"))
    button_4_label = Label(image=button_4, bg=f"{background_bg_code}")
    button_4_label.place(x=95, y=370)
    real_button_4 = Button(root, text="4", image=button_4, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(4))
    real_button_4.place(x=95, y=370)

    button_5 = PhotoImage(file=resource_path(f"Images\\{button_num_5}.png"))
    button_5_label = Label(image=button_5, bg=f"{background_bg_code}")
    button_5_label.place(x=190, y=370)
    real_button_5 = Button(root, text="5", image=button_5, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(5))
    real_button_5.place(x=190, y=370)

    button_6 = PhotoImage(file=resource_path(f"Images\\{button_num_6}.png"))
    button_6_label = Label(image=button_6, bg=f"{background_bg_code}")
    button_6_label.place(x=285, y=370)
    real_button_6 = Button(root, text="6", image=button_6, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(6))
    real_button_6.place(x=285, y=370)

    button_7 = PhotoImage(file=resource_path(f"Images\\{button_num_7}.png"))
    button_7_label = Label(image=button_7, bg=f"{background_bg_code}")
    button_7_label.place(x=95, y=310)
    real_button_7 = Button(root, text="7", image=button_7, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(7))
    real_button_7.place(x=95, y=310)

    button_8 = PhotoImage(file=resource_path(f"Images\\{button_num_8}.png"))
    button_8_label = Label(image=button_8, bg=f"{background_bg_code}")
    button_8_label.place(x=190, y=310)
    real_button_8 = Button(root, text="8", image=button_8, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(8))
    real_button_8.place(x=190, y=310)

    button_9 = PhotoImage(file=resource_path(f"Images\\{button_num_9}.png"))
    button_9_label = Label(image=button_9, bg=f"{background_bg_code}")
    button_9_label.place(x=285, y=310)
    real_button_9 = Button(root, text="9", image=button_9, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(9))
    real_button_9.place(x=285, y=310)

    button_0 = PhotoImage(file=resource_path(f"Images\\{button_num_0}.png"))
    button_0_label = Label(image=button_0, bg=f"{background_bg_code}")
    button_0_label.place(x=190, y=490)
    real_button_0 = Button(root, text="0", image=button_0, borderwidth=0, bg=f"{background_bg_code}",
                           activebackground=f"{background_bg_code}", command=lambda: button_click(0))
    real_button_0.place(x=190, y=490)

    button_negorposmaker = PhotoImage(file=resource_path(f"Images\\{button_negorposmaker}.png"))
    button_negorposmaker_label = Label(image=button_negorposmaker, bg=f"{background_bg_code}")
    button_negorposmaker_label.place(x=95, y=490)
    real_button_negorposmaker = Button(root, text="-", image=button_negorposmaker, borderwidth=0,
                                       bg=f"{background_bg_code}", activebackground=f"{background_bg_code}",
                                       command=lambda: negorposmaker("-"))
    real_button_negorposmaker.place(x=95, y=490)

    button_dot = PhotoImage(file=resource_path(f"Images\\{dot_button}.png"))
    button_dot_label = Label(image=button_dot, bg=f"{background_bg_code}")
    button_dot_label.place(x=285, y=490)
    real_button_dot = Button(root, text=".", image=button_dot, borderwidth=0, bg=f"{background_bg_code}",
                             activebackground=f"{background_bg_code}", command=lambda: button_plus_screen("."))
    real_button_dot.place(x=285, y=490)

    button_equal = PhotoImage(file=resource_path(f"Images\\{button_equal}.png"))
    button_equal_label = Label(image=button_equal, bg=f"{background_bg_code}")
    button_equal_label.place(x=380, y=490)
    real_button_equal = Button(root, text="=", image=button_equal, borderwidth=0, bg=f"{background_bg_code}",
                               activebackground=f"{background_bg_code}", command=button_equal_screen)
    real_button_equal.place(x=380, y=490)

    button_plus = PhotoImage(file=resource_path(f"Images\\{button_plus}.png"))
    button_plus_label = Label(image=button_plus, bg=f"{background_bg_code}")
    button_plus_label.place(x=380, y=430)
    real_button_plus = Button(root, text="+", image=button_plus, borderwidth=0, bg=f"{background_bg_code}",
                              activebackground=f"{background_bg_code}", command=lambda: button_plus_screen("+"))
    real_button_plus.place(x=380, y=430)

    button_mines = PhotoImage(file=resource_path(f"Images\\{button_mines}.png"))
    button_mines_label = Label(image=button_mines, bg=f"{background_bg_code}")
    button_mines_label.place(x=380, y=370)
    real_button_mines = Button(root, text="-", image=button_mines, borderwidth=0, bg=f"{background_bg_code}",
                               activebackground=f"{background_bg_code}", command=lambda: button_mines_screen("-"))
    real_button_mines.place(x=380, y=370)

    button_times = PhotoImage(file=resource_path(f"Images\\{button_times}.png"))
    button_times_label = Label(image=button_times, bg=f"{background_bg_code}")
    button_times_label.place(x=380, y=310)
    real_button_times = Button(root, text="*", image=button_times, borderwidth=0, bg=f"{background_bg_code}",
                               activebackground=f"{background_bg_code}", command=lambda: button_times_screen("*"))
    real_button_times.place(x=380, y=310)

    button_fraction = PhotoImage(file=resource_path(f"Images\\{button_fraction}.png"))
    button_fraction_label = Label(image=button_fraction, bg=f"{background_bg_code}")
    button_fraction_label.place(x=380, y=250)
    real_button_fraction = Button(root, text="/", image=button_fraction, borderwidth=0, bg=f"{background_bg_code}",
                                  activebackground=f"{background_bg_code}", command=lambda: button_fraction_screen("/"))
    real_button_fraction.place(x=380, y=250)

    button_sqrt2 = PhotoImage(file=resource_path(f"Images\\{button_sqrt2}.png"))
    button_sqrt2_label = Label(image=button_sqrt2, bg=f"{background_bg_code}")
    button_sqrt2_label.place(x=285, y=250)
    real_button_sqrt2 = Button(root, image=button_sqrt2, borderwidth=0, bg=f"{background_bg_code}",
                               activebackground=f"{background_bg_code}", command=lambda: button_click("√"))
    real_button_sqrt2.place(x=285, y=250)

    button_fib = PhotoImage(file=resource_path(f"Images\\{button_fib}.png"))
    button_fib_label = Label(image=button_fib, bg=f"{background_bg_code}")
    button_fib_label.place(x=95, y=130)
    real_button_fib = Button(root, image=button_fib, borderwidth=0, bg=f"{background_bg_code}",
                             activebackground=f"{background_bg_code}", command=lambda: button_fib_screen("fib"))
    real_button_fib.place(x=95, y=130)

    button_power2 = PhotoImage(file=resource_path(f"Images\\{button_power2}.png"))
    button_power2_label = Label(image=button_power2, bg=f"{background_bg_code}")
    button_power2_label.place(x=190, y=250)
    real_button_power2 = Button(root, image=button_power2, borderwidth=0, bg=f"{background_bg_code}",
                                activebackground=f"{background_bg_code}", command=lambda: button_power_screen("^"))
    real_button_power2.place(x=190, y=250)

    button_onfractionx = PhotoImage(file=resource_path(f"Images\\{button_onfractionx}.png"))
    button_onfractionx_label = Label(image=button_onfractionx, bg=f"{background_bg_code}")
    button_onfractionx_label.place(x=95, y=250)
    real_button_onfractionx = Button(root, image=button_onfractionx, borderwidth=0, bg=f"{background_bg_code}",
                                     activebackground=f"{background_bg_code}", command=onfractionx)
    real_button_onfractionx.place(x=95, y=250)

    button_percent = PhotoImage(file=resource_path(f"Images\\{button_percent}.png"))
    button_percent_label = Label(image=button_percent, bg=f"{background_bg_code}")
    button_percent_label.place(x=95, y=190)
    real_button_percent = Button(root, image=button_percent, borderwidth=0, bg=f"{background_bg_code}",
                                 activebackground=f"{background_bg_code}", command=percent)
    real_button_percent.place(x=95, y=190)

    button_backward = PhotoImage(file=resource_path(f"Images\\{button_backward}.png"))
    button_backward_label = Label(image=button_backward, bg=f"{background_bg_code}")
    button_backward_label.place(x=380, y=190)
    real_button_backward = Button(root, image=button_backward, borderwidth=0, bg=f"{background_bg_code}",
                                  activebackground=f"{background_bg_code}", command=backward)
    real_button_backward.place(x=380, y=190)

    button_clear = PhotoImage(file=resource_path(f"Images\\{button_clear}.png"))
    button_clear_label = Label(image=button_clear, bg=f"{background_bg_code}")
    button_clear_label.place(x=380, y=130)
    real_button_clear = Button(root, image=button_clear, borderwidth=0, bg=f"{background_bg_code}",
                               activebackground=f"{background_bg_code}", command=button_clear_screen)
    real_button_clear.place(x=380, y=130)

    button_fact = PhotoImage(file=resource_path(f"Images\\{button_fact}.png"))
    button_fact_label = Label(image=button_fact, bg=f"{background_bg_code}")
    button_fact_label.place(x=190, y=130)
    real_button_fact = Button(root, image=button_fact, borderwidth=0, bg=f"{background_bg_code}",
                              activebackground=f"{background_bg_code}", command=lambda: button_click("!"))
    real_button_fact.place(x=190, y=130)

    button_openingparenthesis = PhotoImage(file=resource_path(f"Images\\{button_openingparenthesis}.png"))
    button_openingparenthesis_label = Label(image=button_openingparenthesis, bg=f"{background_bg_code}")
    button_openingparenthesis_label.place(x=190, y=190)
    real_button_openingparenthesis = Button(root, image=button_openingparenthesis, borderwidth=0,
                                            bg=f"{background_bg_code}", activebackground=f"{background_bg_code}",
                                            command=lambda: button_pranthesis("("))
    real_button_openingparenthesis.place(x=190, y=190)

    button_closingparenthesis = PhotoImage(file=resource_path(f"Images\\{button_closingparenthesis}.png"))
    button_closingparenthesis_label = Label(image=button_closingparenthesis, bg=f"{background_bg_code}")
    button_closingparenthesis_label.place(x=285, y=190)
    real_button_closingparenthesis = Button(root, image=button_closingparenthesis, borderwidth=0,
                                            bg=f"{background_bg_code}", activebackground=f"{background_bg_code}",
                                            command=lambda: button_pranthesis(")"))
    real_button_closingparenthesis.place(x=285, y=190)

    button_exp = PhotoImage(file=resource_path(f"Images\\{button_exp}.png"))
    button_exp_label = Label(image=button_exp, bg=f"{background_bg_code}")
    button_exp_label.place(x=285, y=130)
    real_button_exp = Button(root, image=button_exp, borderwidth=0, bg=f"{background_bg_code}",
                             activebackground=f"{background_bg_code}", command=exp)
    real_button_exp.place(x=285, y=130)

    e = Entry(root, width=20, borderwidth=0, font=("Lucida Calligraphy", 20), bg="#474747", foreground="#ffffff")
    e.place(x=30, y=89, height=32, width=410)

    root.mainloop()


root = Tk()
root.title("PyCulator")
root.maxsize(width=475, height=550)
root.minsize(width=475, height=550)
root.iconbitmap(resource_path("Images\\Calculator_icon.ico"))

cal_screen()

root.mainloop()
