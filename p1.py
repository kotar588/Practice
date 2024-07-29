# キーボードから月日の入力を受け付け，1月1日からその月日までの日数を算出して表示するプログラムを作成しなさい．
# 入力となる「月日」は4桁の数字で与えられ，上位2桁が「月」を下位2桁が「日」を表すものとする．ただし，うるう年ではないとする．
# if, for, whileなどの繰り返しや分岐に関わる構文要素は用いないこと．


monthes = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}   

#入力を取得
days = int(input('Enter the number of days(MMDD format): '))

#入力から月と日を取得
month = (days //100) - 1
day = days % 100

#月を示すキーのリストを作成
monthes_keys = list(monthes.keys())

#指定した月までの合計日数を計算
monthes_to_sum = monthes_keys[:month]
total_days = sum(list(monthes.values())[:month]) + day

print(f"The total days up to the specified date is: {total_days}")

