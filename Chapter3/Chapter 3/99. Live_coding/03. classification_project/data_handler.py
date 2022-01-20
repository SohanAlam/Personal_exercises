import os


class DataHandler:

    def __init__(self, root_dir, train_size=.7) -> None:
        self.train_size = train_size
        self.root_dir = root_dir

    def folder_structure(self, img_folder, dest_folders = []):
        classes = os.listdir(img_folder)

    








# loader = DataHandler()

# print(loader.something)

# from sklearn.model_selection import train_test_split

# xtr, xte, ytr, yte = train_test_split(X, y, train_size=.7)