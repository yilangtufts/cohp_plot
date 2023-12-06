import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="This script is used to generage COHP plot with selected atom pairs")
    parser.add_argument('-a', '--atom_pairs', nargs='+', metavar='atom_pairs', help='Atom pairs for COHP plots. Put ligher atom first, e.g. O-Pt, Si-Pt, Zn-Pt')
    parser.add_argument('-c', '--colors', nargs='+', metavar='colors', help='Colors for the plots, e.g. red, gold, blue')
    parser.add_argument('-f', '--filename', metavar='filename', help='Output file name, e.g. cohp')
    args = parser.parse_args()
    if args.atom_pairs:
        print("These atom pairs were chosen to plot their COHP:", args.atom_pairs)
        # atom_pairs_plot = args.atom_pairs
    else:
        print("Atom pairs not specified, COHP of all atom pairs will be plotted:")
    if args.colors:
        print("These corresponding colors were chosen:", args.colors)
        if args.atom_pairs and len(args.colors) < len(args.atom_pairs):
            print("Rest colors will be assinged randomly")
    else:
        print("Color not specified, random color will be assigned to the plots")
    if args.filename:
        filename = args.filename
    else:
        filename = "cohp"

    try:
        with open('COHPCAR.lobster', "r") as f:
            cohp = []
            atom_pairs = {}
            i = 0
            for line in f:
                i += 1
                if line[0] == "N":
                    for i in range(len(line)):
                        if line[i] == ":":
                            atom1 = line[i+1] if line[i+2].isnumeric() else line[i+1: i+3]
                        if line[i:i+2] == "->":
                            atom2 = line[i+2] if line[i+3].isnumeric() else line[i+2: i+4]
                    atom_pair = atom1 + "-" + atom2
                    number = int(line[3]) if line[4] == ":" else int(line[3:5])
                    if atom_pair not in atom_pairs:
                        atom_pairs[atom_pair] = [number]
                    else:
                        atom_pairs[atom_pair].append(number)
                if (line.strip()[0].isnumeric() or line.strip()[0] == "-") and i > 3:
                    cohp.append([float(x) for x in line.split()])
        cohp_array = np.array(cohp).T
    except FileNotFoundError:
        print("Error: COHPCAR.lobster not found. Please put COHPCAR.lobster file under current directory")
        sys.exit()

    if args.atom_pairs:
        atom_pairs_plot = args.atom_pairs
    else:
        atom_pairs_plot = list(atom_pairs)

    plt.figure(figsize=(3, 6))
    for i in range(len(atom_pairs_plot)):
        minus_cohp = np.zeros(321)
        try:
            for j in atom_pairs[atom_pairs_plot[i]]:
                minus_cohp -= cohp_array[2*j+1]
        except KeyError:
            print("Error: " + atom_pairs_plot + " is not found in lobster output file")
            sys.exit()
        if args.colors:
            if i < len(args.colors):
                plt.plot(minus_cohp, cohp_array[0], color=args.colors[i], label=atom_pairs_plot[i])
            else:
                plt.plot(minus_cohp, cohp_array[0], label=atom_pairs_plot[i])
        else:
            plt.plot(minus_cohp, cohp_array[0], label=atom_pairs_plot[i])

    plt.axvline(x=0, color='grey', linestyle='--')
    plt.axhline(y=0, color='grey', linestyle=':')
    plt.xlabel('-COHP', fontsize=14)
    plt.ylabel('E-Ef (eV)', fontsize=14)
    # plt.xlim(-2, 2)
    plt.ylim(-10, 6)
    plt.xticks([], fontsize=14)
    plt.yticks([i*2 - 10 for i in range(9)], fontsize=14)
    plt.legend()
    plt.savefig(filename + ".png")
    print("COHP plots were successfully saved as " + filename + ".png")

if __name__ == "__main__":
    main()
