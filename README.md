# JupyterLab利用プロジェクトをGitで管理する方法比較用リポジトリ

[記事](https://zenn.dev/articles/e8fcb7aa4736f3) で試す内容のためのリポジトリ。

データ分析によく使われるとされるので `conda` を利用する前提で進める。

## フォルダ構成

適当にそれっぽいフォルダ構造を考えさせた。

```text
.
├── notebooks/
│   ├── 1.0-jqp-initial-data-exploration.ipynb
│   └── ...
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── feature_generation.py
│   └── model_training.py
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   ├── model_v1.pkl
│   └── ...
├── reports/
│   ├── final_report.pdf
│   └── figures/
│       ├── plot1.png
│       └── ...
├── requirements.txt
├── LICENSE
└── README.md
```

利用方法の想定は以下の通り。

- `notebooks/`: Jupyter Notebookファイルを格納
- `src/`: 再利用可能なPythonスクリプトを格納
- `data/`: 生データと前処理済みデータを格納
- `models/`: 訓練済みモデルを格納
- `reports/`: 分析レポートと生成されたグラフィックを格納
- `requirements.txt`: 依存関係を記述したファイル
- `LICENSE`: ライセンス情報を記述したファイル
- `README.md`: プロジェクトの概要と使用方法を説明するドキュメント

実際モデルをGitにいれることがあるのかは知らない。
Git LFS使えば入れても良さそう。
