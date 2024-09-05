'''
csvから指定されたメールアドレスとトピックに対応する振り返りを取得するスクリプト
ターミナルにて該当ディレクトリに移動した後にpython get_value.pyで実行

csvファイルのパス、メールアドレス、トピック名を入力することで振り返りを取得できます
csvファイルはget_value.pyと同じディレクトリに配置してください
'''

import pandas as pd

def get_reflection(file_path, email, topic):
    try:
        # 表示設定を変更
        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.max_rows', None)

        # CSVファイルを読み込む
        df = pd.read_csv(file_path)

        # メールアドレスでフィルタリング
        filtered_df = df[df['メールアドレス'] == email]

        # 入力されたトピック名がカラムに存在するかを確認
        if topic not in df.columns:
            raise KeyError(f"{topic} - トピックが存在しません。正しいトピック名を入力してください。")

        # 振り返りのカラムに特定のトピックが含まれている行を取得
        result = filtered_df[filtered_df[topic].notnull()]

        # 結果を表示
        if not result.empty:
            # 特定のトピックの内容をリストとして取得
            reflection_texts = result[topic].tolist()
            for text in reflection_texts:
                # テキストを改行で分割して表示
                for sentence in text.split('\n'):
                    # 各行を箇条書き形式で表示
                    print(f"- {sentence.strip()}")
        else:
            print(f"メールアドレス: {email} に対してトピック: {topic} の振り返りが見つかりませんでした。")

    except KeyError as ke:
        print(f"KeyError: {ke} - 一部のカラムが存在しない可能性があります。")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("CSVファイルのパスを入力してください: ")
    email = input("メールアドレスを入力してください: ")
    topic = input("調べたいトピック名を入力してください: ")

    get_reflection(file_path, email, topic)

if __name__ == "__main__":
    main()
