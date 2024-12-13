# generation-of-interlocutor-profiling
Repository for the paper "Evaluation of active generation of interlocutor profiling sentences from utterances and their implicit context"

The original chat data is detailed in the link below.
Please also follow the license of the original data when using it.
https://github.com/nttcslab/japanese-dialog-transformers/tree/main

発話データがオリジナルではないためID化されています。
発話データとプロファイル情報を結び付けるために、
このリポジトリをgit cloneした後で以下のリンクから発話データ(japanese_persona_chat.xlsx)を取得して
このreadmeファイルと同じフォルダに置いてください。

https://github.com/nttcslab/japanese-dialog-transformers/tree/main

その後、hukugen.pyを動かすだけでIDが発話に復元されたデータセットが"data/dataset"下に作成されます。
