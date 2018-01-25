import script
from pso import *
from targetfunc import *


if __name__ == "__main__":
    files_list = ["Plik_z_kolkami", "kolka_i_kwadraty"]
    phip_list = [ 0.7, 1, 1.3]
    phig_list = [0.7, 1, 1.3]
    omega = [0.7, 1, 1.3]

    for file in files_list:
        for phig in phig_list:
            for phip in phip_list:
                for om in omega:
                    people = script.read_people_from_file(file, g.COLS, g.ROWS)
                    my_func = Target(people)
                    out = pso(my_func, 0, 1250, 500, om, phip, phig, 2500)
                    script.write2file_out(out,0,file,500,om,phip,phig)