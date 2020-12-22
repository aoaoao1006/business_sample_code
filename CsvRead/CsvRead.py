import csv

"""CsvRead

CSVファイルを読み込み特定項目だけを抽出する.
ファイル内に文字としてのカンマがあると動きは変わる（と思う）
"""

def main():

	# シンプル版のCSV読込
	with open('test.csv', newline='') as f:
		reader = csv.reader(f)

		# カンマ3つの項目を想定とし項目ごとに出力する.
		for row in reader:
			cnt = str(row).count(',')

			# 特定の項目(3つ目)だけ表示する.
			for num in range(cnt+1):
				if num == 2:
					print(row[num].strip())

# 初期化のあれ.
if __name__ == "__main__":
    main()

