# 第5回
### Pygameでゲーム実装
#### 3限：基本機能
- ゲーム概要：
- rensyu05/dodge_bomb.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとんを
移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
- 操作方法：矢印キーでこうかとんを上下左右に移動する
- プログラムの説明
- dodge_bomb.pyをコマンドラインから実行すると，pygameの初期化，main関数の順に処理が進む
- ゲームオーバーによりmain関数から抜けると，pygameの初期化を解除し，プログラムが終了する
- main関数では，clockの生成，スクリーンの生成，背景画像の描画，こうかとんの描画，爆弾の描画
を行う
- main関数の無限ループでは，キー操作に応じたこうかとんの移動，指定速度に応じた爆弾の移動を
行う
- Rectクラスのcolliderectメソッドにより，こうかとんと爆弾の接触を判定する
- check_bound関数では，こうかとんや爆弾の座標がスクリーン外にならないようにチェックする
#### 4限：追加機能
- 飛び回る爆弾の速さをそれぞれバラバラにした、for文で新しい変数を使い爆弾の速さのところを変数を使い速さを変えた。
- スコアを表示する新しいクラスを追加した。1秒につきスコアが1上がるようにした。