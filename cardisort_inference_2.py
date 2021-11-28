# Re-write cardisort_inference.py
# by Avan Suinesiaputra - KCL 2021

from CMRSorter import CMRSorter
import argparse
from cardisort_utils import get_inference_dict, write_sorted
import pickle
import numpy as np
import tensorflow.keras as tfk


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict slice label using the cardisort method.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("model", help="A folder that contains the weight parameters for cardisort network.")
    parser.add_argument("image_folder", help="Input image folder")
    parser.add_argument("output_folder", help="Output result folder")
    parser.add_argument("-N", default=256, type=int, help="Image width")
    parser.add_argument("-M", default=256, type=int, help="Image height")
    args = parser.parse_args()

    # load cardisort model
    cardisort_model = tfk.models.load_model(args.model)

    # read pre-defined sequence & plane categories
    pickle_in = open("seq_categories.pickle","rb")
    seq_categories = pickle.load(pickle_in)
    pickle_in = open("plane_categories.pickle","rb")
    plane_categories = pickle.load(pickle_in)
    series_counts = np.zeros((len(seq_categories), len(plane_categories)))

    # reading the images
    cmr = CMRSorter(args.image_folder)

    for std_id, ser in cmr.dicom_dir.items():
        print(f"Inference for study UID {std_id}")

        # create images
        img_dict = get_inference_dict(ser, args.M, args.N)

        # count series
        for key in img_dict:
            out = cardisort_model(img_dict[key][np.newaxis, ...])

            s = np.argmax(out[0].numpy())
            p = np.argmax(out[1].numpy())

            series_counts[s, p] += 1
            write_sorted(ser[key], args.output_folder, seq_categories[s], plane_categories[p], series_counts[s, p])

    print(f"DONE!!")
