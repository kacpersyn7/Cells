import input_output
from pso import *
from targetfunc import *


if __name__ == "__main__":
    files_list = ["Plik_z_kolkami", "kolka_i_kwadraty"]
    k_list = [0.1, 1, 10]
    x0_list = [0, 1, 10]

    for file in files_list:
        for k1_tmp in k_list:
            for x0_tmp in x0_list:
                people = input_output.read_people_from_file(file, g.COLS, g.ROWS)
                my_func = Target(people, k=k1_tmp, x0=xo_tmp)
                out = pso(my_func, 0, 1250, 500, 1, 1, 1, 2500)
                input_output.write2file_out_another_f(out,0,file,500,k1_tmp,x0_tmp)