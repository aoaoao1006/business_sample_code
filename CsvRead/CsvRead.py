import csv

def main():
	"""
	CSVファイルを読み込み特定項目だけを抽出する.
	ファイル内に文字としてのカンマがあると動きは変わる（と思う）
	"""

	# シンプル版のCSV読込
	with open('test.csv', newline='') as f:
		reader = csv.reader(f)

		# listと命名しているがString型.
		list = ""

		# カンマ3つの項目を想定とし項目ごとに出力する.
		for row in reader:
			# カンマの数=項目数と想定し、繰返し回数を確定させている.
			cnt = str(row).count(',') + 1

			# 特定の項目(3つ目)だけ表示する.
			for num in range(cnt):
				if num == 2:
					list = list + row[num].strip() + "\n"
					print(row[num].strip())

	# 最後に結果を表示.
	# わざわざlist型ではなくString型にしているのは対象項目の値だけを表示させるため.
	print("### 最後にまとめて表示してみる. ###")
	print(list)

# 初期化のあれ.
if __name__ == "__main__":
    main()

