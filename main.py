import sys
from createSilhouette import SilhouetteMaker

def main():
    args = sys.argv
    # if len(args) > 1:
    #     threshold_values = [int(i) for i in args[1:]]
    # else:
    #     threshold_values = [128]
    maker = SilhouetteMaker()
    if len(args) == 3:
        maker.iterate_over_folders(args[1], f"{args[1]}_reverse_silhouette", [args[2]])
    if len(args) == 2:
        maker.iterate_over_folders(args[1], f"{args[1]}_reverse_silhouette")
    if len(args) > 3:
        maker.iterate_over_folders(args[1], f"{args[1]}_reverse_silhouette", args[2:])
    if len(args) == 1:
        numbers = maker.check_directory(args[1])
        print (numbers)
    for n in args:
        print(n)

if __name__ == "__main__":
    main()

