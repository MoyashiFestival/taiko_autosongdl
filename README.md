# taiko_autosongdl
太鼓の達人ドンダフルフェスティバル(Steam版) で、太鼓ミュージックパス内のすべての曲を「マイライブラリ」に登録する作業を自動化するPythonスクリプトです。

`vgamepad`ライブラリを使って仮想ゲームパッドを作成し、終了するまで「xボタン押下」→「十字下ボタン押下」→... を繰り返す簡単な仕組みです。

# 使い方
## 事前準備
### 1. Pythonのインストール
1. Microsoft Storeで「Python」と検索。
2. 「Python 3.〇〇」をインストール。特に理由がない場合は、最新版 (一番数字が大きいもの) でOK。
3. PowerShell等のターミナル上で以下のコマンドを実行。
```
python --version
```
バージョン名が表示されていればインストール成功。
   
### 2. `vgamepad`ライブラリのインストール
1. PowerShell等のターミナル上で以下のコマンドを実行。
```
pip install vgamepad
```
2. 途中でドライバのインストールを求められるので手順に従ってインストール。
3. ドライバのインストール後、PCを再起動。

## 実行
### 3. スクリプトの実行
1. 太鼓の達人のゲーム画面で、「演奏ゲーム」→「演奏を始める」→「太鼓ミュージックパス」タブ→「配信中のすべての曲」に移動。
2. PowerShell等のターミナル上でスクリプトがあるフォルダ内に移動。<br>例) ダウンロードフォルダに`taiko_autosongdl.py`がある場合
```
cd C:\Users\ユーザー名\Downloads
```
3. スクリプトを実行。
```
python taiko_autosongdl.py
```
4. 実行してから10秒以内に太鼓の達人のゲーム画面に移動。
5. 全曲の追加が終わるまで見守る。

### 4. スクリプトの終了
1. PowerShell等のターミナル上で`Ctrl + C`を押し、スクリプトを終了。
