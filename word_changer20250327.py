words = str(input('変換したい文字列を入力：'))
result = "'" + words.replace("・","', '" ) + "'"
print('結果を出力します...')
print(result)