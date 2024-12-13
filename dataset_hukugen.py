import misc
import json
import os

formed_utts=misc.open_txt("utts_and_ids.txt")

id_dic={}
for l in formed_utts:
	u,i = l.split("@@@")
	id_dic[i]=u

train_method=["concat","profile-wise"]
used_data_variation=["o_only","with_p"]
data_division=["train","val","test"]

print("train data")

for t_m in train_method:
	filename=f"data/dataset/train_data/{t_m}"
	if not os.path.exists(filename):
		os.makedirs(filename)

	for u_d_v in used_data_variation:
		
		filename=f"data/dataset/train_data/{t_m}/{u_d_v}"
		if not os.path.exists(filename):
			os.makedirs(filename)

		for d_d in data_division:

			in_path = f"data/used_uttid/train_data/{t_m}/{u_d_v}/{d_d}.jsonl"
			out_path = f"data/dataset/train_data/{t_m}/{u_d_v}/{d_d}.jsonl"

			with open(in_path, encoding="utf-8") as f:
				id_data = json.load(f)

			out=[]
			for d in id_data:
				d["utts"]=id_dic[d["utts"]]
				out.append(d)
			
			with open(out_path, 'w',encoding="utf-8") as f:
				json.dump(out, f, indent=4,ensure_ascii=False)
			
			print(f"{t_m}/{u_d_v}/{d_d} ok")