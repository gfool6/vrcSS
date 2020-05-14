import glob
import re
import os
import shutil

headCutRegex = ".*[VRChat|vrchat]_[0-9]+x[0-9]+_"
tailCutRegex = "-[0-9]+_[0-9]+-[0-9]+-[0-9]+.[0-9]+.png"

# ファイル一覧取得
files = [screenShots for screenShots in glob.glob('./VRChat*.png')]
filenameList = [f"{ssfile}" for ssfile in files]

# 月部分だけ抽出
headCut = [re.sub(headCutRegex, "", file) for file in filenameList]
monthList = sorted(set([re.sub(tailCutRegex, "", cutted) for cutted in headCut]))

# 月ごとにフォルダ作ってファイル移動
for month in monthList:
    # 既にフォルダが存在していたら作らない
    if not os.path.exists(f"./{month}"):
        os.makedirs(month)
    
    [shutil.move(path, f"./{month}/{path}") for path in files if re.search(f".*{month}.*", str(path))]