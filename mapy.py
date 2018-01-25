from graphics import *
from input_output import *
from targetfunc import *

Wynik1a = read_people_from_file("outbitmapa_router_1_kolka_i_kwadraty_2_500 2", g.COLS, g.ROWS)
Wynik2a = read_people_from_file("outbitmapa_router_1_kolka_i_kwadraty_z_szumem_2_200 2", g.COLS, g.ROWS)
Wynik3a = read_people_from_file("outbitmapa_router_1_Plik_z_kolkami_0_500 0", g.COLS, g.ROWS)
Wynik1b = read_people_from_file("outbitmapa_router_2_kolka_i_kwadraty_2_500 2", g.COLS, g.ROWS)
Wynik2b = read_people_from_file("outbitmapa_router_2_kolka_i_kwadraty_z_szumem_2_200 2", g.COLS, g.ROWS)
Wynik3b = read_people_from_file("outbitmapa_router_2_Plik_z_kolkami_0_500 0", g.COLS, g.ROWS)

l1 = read_people_from_file("../kolka_i_kwadraty", g.ROWS, g.COLS)
l2 = read_people_from_file("../kolka_i_kwadraty_z_szumem", g.ROWS, g.COLS)
l3 = read_people_from_file("../Plik_z_kolkami", g.ROWS, g.COLS)

func_1 = Target(l1, g.access_points_types)
func_2 = Target(l2, g.access_points_types)
func_3 = Target(l3, g.access_points_types)
w1 = np.stack((Wynik1a, Wynik1b))
w2 = np.stack((Wynik2a, Wynik2b))
w3 = np.stack((Wynik3a, Wynik3b))
heat1 = func_1.get_result_area(w1)
heat2 = func_2.get_result_area(w2)
heat3 = func_2.get_result_area(w3)

show_and_save_accesspoints(w1, 'pol1')
show_and_save_accesspoints(w2, 'pol2')
show_and_save_accesspoints(w3, 'pol3')
show_and_save_power(l1, heat1, 'heat1.png')
show_and_save_power(l2, heat2, 'heat2.png')
show_and_save_power(l3, heat3, 'heat3.png')
