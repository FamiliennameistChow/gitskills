from PyInstaller.utils.hooks import collect_data_files, collect_submodules

datas = collect_data_files("skimage.io.use_plugins")
hiddenimports = collect_submodules('skimage.io.use_plugins')
