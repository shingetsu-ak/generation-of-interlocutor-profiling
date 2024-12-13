import misc

formed_utts=misc.open_txt("utts_and_ids.txt")

print("anotation data")
id_dic={}
for l in formed_utts:
	u,i = l.split("@@@")
	u=u.replace("\t","\n")
	id_dic[i]=u

for datanum in range(24):
	for anonum in range(3):
		
		filename=f"data_{datanum+1}_{anonum+1}.xlsx"
		lines=misc.load_excel("data/used_uttid/excel_data/"+filename)

		
		out=[]

		for l in lines:
			if l[0]==None: continue
			utt_id=l[0]
			profiles=l[1]
			ano=l[2]
			if utt_id=="AとBの発話(id)":
				continue
			
			out.append([id_dic[utt_id],profiles,ano])

		save_name="data/dataset/excel_data/"+filename
		#print(out[-1])
		misc.save_excel(filename=save_name,sheetname="personas",savedata=out)

		print(f"data_{datanum+1}_{anonum+1} ok")