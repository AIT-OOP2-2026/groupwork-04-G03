# main.py （他のファイルの処理を順番に呼び出す）

from record import record_audio
from mojiokoshi import mojiokoshi
from hozon import hozon


def main():
    # 1. 録音処理（audio-output.wav が生成される）
    record_audio()

    # 2. 文字起こし処理（audio-output.wav を文字起こし）
    text = mojiokoshi("audio-output.wav")

    # 3. テキスト保存処理（hozon.txt に追記保存）
    hozon(text)


if __name__ == "__main__":
    main()