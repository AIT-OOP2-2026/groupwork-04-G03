import os
import mlx_whisper


def mojiokoshi(audio_filename: str = "audio-output.wav") -> str:
    """指定された音声ファイルをWhisperのみで文字起こしし、テキストを返す"""
    # スクリプトと同じ階層にある音声ファイルのパスを生成
    base_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(base_dir, audio_filename)

    # mlx_whisperのみで処理
    result = mlx_whisper.transcribe(
        audio_path, path_or_hf_repo="whisper-base-mlx"
    )

    # 文字起こし結果のテキストのみを返す
    return result["text"].strip()