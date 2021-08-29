# import c
# import a.a2.hello as hello
# from b.random_number_generator import generate_number_between, generate_until_drawn
# from a import try_again
# from a.a1.number_generator import *

from a import try_again  # daca vrei sa importi din __init__.py al unui package
from a.a1 import number_generator  # daca vrei sa importi un modul .py dintr-un package
from a.a2 import hello
from b import random_number_generator
from c.c2 import reward
from c.c3 import result_info
from a.a1.number_generator import generate_until_drawn  # daca vrei sa ai o referinta la ceva specific dintr-un modul (se incarca oricum tot modulul, dar specifi ca vrei sa te folosesti in fisierul curent doar de ce ai importat)
def try_again():
    return False


def thank_you():
    print("Thank you")



def lotto():
    """

    :return:
    """
    playing = True
    a2.hello()

    # while playing:
    #     number = c.retrieve_number_from_user()
    #     times = generate_until_drawn(number, 1, 100)
    #     c.inform_about_the_result(times)
    #     c.get_reward(times)
    #     playing = try_again()
    thank_you()


if __name__ == "__main__":
    lotto()
