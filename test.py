
# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    import csv

    csvList = []

    csvList.append(word)

    with open("test.csv","w",newline="") as f:
        csv.writer(f).writerows(csvList)
    ### ここに検索ロジックを書く
    if word in source:
        print(word+"が見つかりました")

    else:
        print(word+"が見つかりませんでした")
        print(word+"を追加しました。")

        source.append(word)

    search()



if __name__ == "__main__":
    search()
