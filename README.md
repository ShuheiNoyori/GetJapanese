# GetJapanese
指定されたディレクトリ下で, 指定された拡張子のファイル内の, ダブルクオーテーションで囲まれた日本語のリストをCSV出力する.  

## デモ
[JANISvisualize](https://github.com/ShuheiNoyori/JANISvisualize) のファイルに対して実行した場合の例.  
JANISvisualize ディレクトリ下の.Rファイルに対して, ダブルクオーテーションで囲まれた日本語 (マルチバイト文字) を検索し, CSV出力する.  
`python getJapanese.py --searchpath /foo/bar/JANISvisualize --extlist .R`

出力結果例: [japanese.csv](/japanese.csv)

## 使用方法  
```
usage: getJapanese.py [-h] [--searchpath SEARCHPATH] [--extlist [EXTLIST [EXTLIST ...]]]

optional arguments:
  -h, --help            show this help message and exit
  --searchpath SEARCHPATH
                        Filepath to be searched. Default: ./
  --extlist [EXTLIST [EXTLIST ...]]
                        File extensions to be scanned. Default: .py .html .js
```
ワーキングディレクトリに japanese.csv が出力される.
