#標準モジュール
import time

#外部モジュール
import ffmpeg

# 録音時間（秒）
DURATION = 10

# 出力ファイル名
OUTPUT_FILE = "audio-output.wav"


def record_audio():
    """マイクから音声を録音して WAV ファイルに保存する。"""
    try:
        print(f"{DURATION}秒間、マイクからの録音を開始します...")

        # macOS の入力デバイスを指定して録音する
        # -f <デバイス入力形式>: OSに応じたデバイス入力形式を指定
        #   - Windows: 'dshow' または 'gdigrab'
        #   - macOS: 'avfoundation'
        #   - Linux: 'alsa'
        # -i <入力デバイス名>: デバイス名を指定
        (
            ffmpeg.input(
                ":0",
                format="avfoundation",
                t=DURATION,
            )
            .output(
                OUTPUT_FILE,
                acodec="pcm_s16le",
                ar="44100",
                ac=1,
            )
            .run(overwrite_output=True)
        )

        print(
            f"録音が完了しました。"
            f"{OUTPUT_FILE}に保存されました。"
        )

    except ffmpeg.Error as error:
        stderr = error.stderr
        if stderr:
            print(f"FFmpeg エラーが発生しました: {stderr.decode()}")
        else:
            print(f"FFmpeg エラーが発生しました: {error}")

    except Exception as error:
        print(f"予期せぬエラーが発生しました: {error}")


if __name__ == "__main__":
    record_audio()
