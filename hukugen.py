###データセットは発話部分がオリジナルではないためID化されています。
###このコードでIDから元の発話に復元できます。

import JPC_kakou

JPC_kakou.JPC2txt()
JPC_kakou.make_utts_id()

import os

filename=f"data/dataset"
if not os.path.exists(filename):
	os.makedirs(filename)

filename=f"data/dataset/excel_data"
if not os.path.exists(filename):
	os.makedirs(filename)

filename=f"data/dataset/train_data"
if not os.path.exists(filename):
	os.makedirs(filename)

import anotation_data_hukugen
import dataset_hukugen