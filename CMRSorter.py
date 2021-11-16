import glob
import os
import pydicom


class CMRSorter:
    """
    This class sorts DICOM files from a CMR study folder into studies -> series -> images.

    1. Studies are tagged from StudyInstanceUID
    2. Series are tagged from SeriesInstanceUID
    3. Images are tagged from SOPInstanceUID

    Author: Avan Suinesiaputra - KCL 2021
    """
    def __init__(self, folder):
        self.root_folder = folder
        self.dicom_dir = dict()

        # find all files (DICOM can be with or without .dcm suffix)
        for f in glob.iglob(os.path.join(folder, '**'), recursive=True):
            if not os.path.isfile(f):
                continue

            # read the dicom file
            try:
                dcm = pydicom.read_file(f)
            except:
                continue

            # process
            study_iuid = dcm.StudyInstanceUID
            series_iuid = dcm.SeriesInstanceUID

            if study_iuid not in self.dicom_dir:
                self.dicom_dir[study_iuid] = dict()

            if series_iuid not in self.dicom_dir[study_iuid]:
                self.dicom_dir[study_iuid][series_iuid] = []

            self.dicom_dir[study_iuid][series_iuid].append(dcm)

        # print
        print(f"There are {len(self.dicom_dir)} stud(y|ies) in {folder}")
        for std_id, ser in self.dicom_dir.items():
            n_files = [len(f) for _, f in ser.items()]
            print(f"Study {std_id} has {len(ser)} series and total of {sum(n_files)} DICOM files.")

