## 第6回
### 横スクロールゲームの実装
#### 基本機能
- ゲーム概要：
- rensyu04/sukuro-ru.pyを実行すると，スクリーンにゲーム画面が描画され，キャラクターを
移動させ迫ってくる敵から逃げるゲーム
- キャラクターが敵と接触するとゲームオーバーで終了する
- 操作方法：矢印キーでキャラクターを上下に移動する
- プログラムの説明
- sukuro-ru.pyをコマンドラインから実行すると,tkinterの初期化，screen関数の順に処理が進む
- ゲームオーバーにより関数から抜けると，tkinterの初期化を解除し，プログラムが終了する
- screen関数では，ゲーム画面の生成，敵の生成，横スクロールの描画，キャラクターの描画を行う
- screen関数の無限ループでは，キー操作に応じたキャラクターの移動，敵の移動を行う
- drawBackgroundにより横スクロールをするところの設定を行う