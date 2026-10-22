# main.py （他のファイルの処理を順番に呼び出す）
from record import record_audio
from mojiokoshi import transcribe_audio
from hozon import save_text


def main():
    # 1. 録音処理
    record_audio()

    # 2. 文字起こし処理（戻り値としてテキストを受け取る）
    text = transcribe_audio()

    # 3. テキスト保存処理（テキストを渡して保存）
    save_text(text)
    

if __name__ == "__main__":
    main()