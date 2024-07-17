import matplotlib           as mpt 
import matplotlib.pyplot    as plt 
import numpy                as np 
import sys
import re
import os


re_for      = r"\s*for\s*\(.+\)"
re_while    = r"\s*while\s*\(.+\)"
re_do_while = r"\s*do\s*\{"


est_file    = r".+(\.(h)|(c))$"


linux = "../flussi/linux"
def main(argc:int, argv:list) -> int:
    num_while       = 0
    num_do_while    = 0
    num_for         = 0

    for root, dirs, files in os.walk(linux):
        for file in files:
            if re.fullmatch(est_file, file):
                with open(os.path.join(root, file), "r", encoding='UTF-8') as f_in:
                    for line in f_in:
                        if re.match(re_for, line):
                            num_for += 1

                        if re.match(re_while, line):
                            num_while += 1
                        
                        if re.match(re_do_while, line):
                            num_do_while += 1
    
    sizes = [num_while, num_do_while, num_for]
    if all(size == 0 for size in sizes):    # se tutti i numeri sono a 0 allora si è verificato un errore
        print("nessun grafico da tracciare")
    else: 
        labels = ["while", "do-while", "for"]
        colors = ["#FFA500", "#9ACD32", "#6EB5FF"]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors = colors)
        plt.title("Cicli nel kernel di linux")
        plt.axis('equal')
        plt.savefig("number_of_cicle.png")
        plt.show()

    print(f"numero di for: {num_for}\nnumero di while: {num_while}\nnumero di do-while: {num_do_while}")
    return 0


if __name__ == "__main__":
    result = main(len(sys.argv), sys.argv)
    print(f"uscita dal programma con valore: {result}")
    sys.exit(result)
