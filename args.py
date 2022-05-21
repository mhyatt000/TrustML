from argparse import ArgumentParser

def get_args():

    ap = ArgumentParser()

    ap.add_argument('-i','--input', type=str)
    ap.add_argument('-o','--output', type=str)
    ap.add_argument('-u','--url', type=str)

    args = ap.parse_args()

    return args
